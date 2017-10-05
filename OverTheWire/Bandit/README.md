#  OverTheWire: Bandit

http://overthewire.org/wargames/bandit/

Self explantory write-up, explanations kept to a minimum

### Level 0

```
root@kali:~# ssh bandit0@bandit.labs.overthewire.org -p 2220 
The authenticity of host '[bandit.labs.overthewire.org]:2220 ([176.9.9.172]:2220)' can't be established.
ECDSA key fingerprint is SHA256:SCySwNrZFEHArEX1cAlnnaJ5gz2O8VEigY9X80nFWUU.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[bandit.labs.overthewire.org]:2220,[176.9.9.172]:2220' (ECDSA) to the list of known hosts.
 _                     _ _ _   
| |__   __ _ _ __   __| (_) |_ 
| '_ \ / _` | '_ \ / _` | | __|
| |_) | (_| | | | | (_| | | |_ 
|_.__/ \__,_|_| |_|\__,_|_|\__|
                               
a http://www.overthewire.org wargame.

bandit0@bandit.labs.overthewire.org's password: 
Welcome to Ubuntu 14.04 LTS (GNU/Linux 4.4.0-92-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

### Level 1

```
root@kali:~# ssh bandit1@bandit.labs.overthewire.org -p 2220 
 _                     _ _ _   
| |__   __ _ _ __   __| (_) |_ 
| '_ \ / _` | '_ \ / _` | | __|
| |_) | (_| | | | | (_| | | |_ 
|_.__/ \__,_|_| |_|\__,_|_|\__|
                               
a http://www.overthewire.org wargame.

bandit1@bandit.labs.overthewire.org's password: 
Welcome to Ubuntu 14.04 LTS (GNU/Linux 4.4.0-92-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

bandit1@bandit:~$ ls    
-
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

### Level 2

Ommitting the ssh part now.
```
bandit2@bandit:~$ ls -lah 
total 28K
drwxr-xr-x  3 bandit2 bandit2 4.0K Oct  4 23:38 .
drwxr-xr-x 30 root    root    4.0K Oct  4 23:38 ..
-rw-r--r--  1 bandit2 bandit2  220 Apr  9  2014 .bash_logout
-rw-r--r--  1 bandit2 bandit2 3.6K Apr  9  2014 .bashrc
drwx------  2 bandit2 bandit2 4.0K Oct  4 23:38 .cache
-rw-r--r--  1 bandit2 bandit2  675 Apr  9  2014 .profile
-rw-r-----  1 bandit3 bandit2   33 Sep 28 14:04 spaces in this filename
bandit2@bandit:~$ cat spaces\ in\ this\ filename (or double quotes the filename works with spaces)
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

### Level 3

```
bandit3@bandit:~$ ls -lah
total 28K
drwxr-xr-x  4 bandit3 bandit3 4.0K Oct  4 23:41 .
drwxr-xr-x 30 root    root    4.0K Oct  4 23:41 ..
-rw-r--r--  1 bandit3 bandit3  220 Apr  9  2014 .bash_logout
-rw-r--r--  1 bandit3 bandit3 3.6K Apr  9  2014 .bashrc
drwx------  2 bandit3 bandit3 4.0K Oct  4 23:41 .cache
-rw-r--r--  1 bandit3 bandit3  675 Apr  9  2014 .profile
drwxr-xr-x  2 root    root    4.0K Sep 28 14:04 inhere
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ ls -lah
total 12K
drwxr-xr-x 2 root    root    4.0K Sep 28 14:04 .
drwxr-xr-x 4 bandit3 bandit3 4.0K Oct  4 23:41 ..
-rw-r----- 1 bandit4 bandit3   33 Sep 28 14:04 .hidden
bandit3@bandit:~/inhere$ cat .hidden 
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

### Level 4

```
bandit4@bandit:~$ ls -lah
total 28K
drwxr-xr-x  4 bandit4 bandit4 4.0K Oct  4 23:43 .
drwxr-xr-x 30 root    root    4.0K Oct  4 23:43 ..
-rw-r--r--  1 bandit4 bandit4  220 Apr  9  2014 .bash_logout
-rw-r--r--  1 bandit4 bandit4 3.6K Apr  9  2014 .bashrc
drwx------  2 bandit4 bandit4 4.0K Oct  4 23:43 .cache
-rw-r--r--  1 bandit4 bandit4  675 Apr  9  2014 .profile
drwxr-xr-x  2 root    root    4.0K Sep 28 14:04 inhere
bandit4@bandit:~$ cd inhere/
bandit4@bandit:~/inhere$ ls -lah
total 48K
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file00
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file01
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file02
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file03
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file04
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file05
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file06
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file07
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file08
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file09
drwxr-xr-x 2 root    root    4.0K Sep 28 14:04 .
drwxr-xr-x 4 bandit4 bandit4 4.0K Oct  4 23:43 ..
bandit4@bandit:~/inhere$ 
bandit4@bandit:~/inhere$ cat ./-file00
��Cʡ#8�+�����bandit4@bandit:~/inhere$ cat ./-file02
��㫫�Gd�i���d�����@ǘ��	
                                H�bandit4@bandit:~/inhere$ cat ./-file01
��V��TH��U:�%@J,���O��ca3���C7bandit4@bandit:~/inhere$ cat ./-file03
��ֱ����?G[�Og)e�B;�KKjx�g�9��bandit4@bandit:~/inhere$ cat ./-file04
��=G�L�E���z�������̋
                     �0�2��bandit4@bandit:~/inhere$ cat ./-file05
�a��1Sg�å�vs�X��?sC�H�
                       ف�f��bandit4@bandit:~/inhere$ cat ./-file06
���A�`���H@��Cz���-ԕo$/�#�bandit4@bandit:~/inhere$ cat ./-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

### Level 5

```
bandit5@bandit:~/inhere$ find ./ -size 1033c
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ```                                                                                                                                                                                                                                                                                                                                                       
### Level 6

```
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password

^C
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

### Level 7

```
bandit7@bandit:~$ cat data.txt | grep millionth
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

### Level 8

```
bandit8@bandit:~$ cat data.txt | sort | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

### Level 9
Data.txt is binary with different extension, better to use strings

```
bandit9@bandit:~$ strings data.txt | grep '='
========== the
R=ev2,
NF=!^
M5Q=
========== password
TuI@=
========== iss
c       =$
w=RO
eD=p
jR=JlB
G========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
:=*1p
KA=%
```

### Level 10

```
bandit10@bandit:~$ base64 -d data.txt
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```


### Level 11
Used a rot13 decryptor `The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu`

### Level 12

```
root@kali:~# scp -P 2220 bandit12@bandit.labs.overthewire.org:~/data.txt ~/
 _                     _ _ _   
| |__   __ _ _ __   __| (_) |_ 
| '_ \ / _` | '_ \ / _` | | __|
| |_) | (_| | | | | (_| | | |_ 
|_.__/ \__,_|_| |_|\__,_|_|\__|
                               
a http://www.overthewire.org wargame.

bandit12@bandit.labs.overthewire.org's password: 
data.txt                                      100% 2546   105.2KB/s   00:00

root@kali:~# xxd -r data.txt > data1.txt
root@kali:~# file data1.txt
data1.txt: gzip compressed data, was "data2.bin", last modified: Thu Sep 28 14:04:06 2017, max compression, from Unix
root@kali:~# gzip -d data1.txt
gzip: data1.txt: unknown suffix -- ignored
root@kali:~# mv data1.txt file.bin
root@kali:~# zcat file.bin | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

```

### Level 13
We use the private key to log in to bandit14

```
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost
...

...
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

### Level 14

```
bandit14@bandit:~$ nc localhost 30000
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr
```

### Level 15

```
bandit15@bandit:~$ openssl s_client -ign_eof -connect localhost:30001
CONNECTED(00000003)
depth=0 CN = 8f75dc271013
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = 8f75dc271013
verify return:1
...

...
BfMYroe26WYalil77FoDi9qh59eK5xNr
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd

read:errno=0
```

### Level 16

```
bandit16@bandit:~$ nmap -p 31000-32000 -sV  localhost

Starting Nmap 6.40 ( http://nmap.org ) at 2016-09-09 01:39 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00050s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE VERSION
31046/tcp open  echo
31518/tcp open  msdtc   Microsoft Distributed Transaction Coordinator (error)
31691/tcp open  echo
31790/tcp open  msdtc   Microsoft Distributed Transaction Coordinator (error)
31960/tcp open  echo
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at http://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 41.34 seconds

bandit16@bandit:~$ openssl s_client -connect localhost:31790
CONNECTED(00000003)
depth=0 CN = 8f75dc271013
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = 8f75dc271013
verify return:1
---
Certificate chain
 0 s:/CN=8f75dc271013
   i:/CN=8f75dc271013
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICvjCCAaagAwIBAgIJALADbwWQ0u9aMA0GCSqGSIb3DQEBCwUAMBcxFTATBgNV
BAMTDDhmNzVkYzI3MTAxMzAeFw0xNzA5MTYwNzAyMjRaFw0yNzA5MTQwNzAyMjRa
MBcxFTATBgNVBAMTDDhmNzVkYzI3MTAxMzCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBALmjBUTlmjROJUssm+rAlFADFfzrz+xCH0qUXryou5/wW8pnQ6nG
HbdeRIBwTVGFiDIKRbFdWQU4BbrfjEhyGn9d7eh/3GV09ZdvLDYRoLmJ4tDF8CiC
wGl9GufcWr3zeaNYa8CwVdtWam8umhMICrsv7B5iV9RdSQfudUtVbr26SBVyuhBm
m0t7Su6rLCrrGtshdIihjk4k67bBMpSNAOduhpp79UgIPKcwJUhRJHTcji3m/IQ8
O9zNS25oL8KhMn7e/Xe70kztstq0ShMsx8feutONnGulUOlaEMMqW+HSWgnVeG/r
mU9Nzwn++4qxe16OvvmXAzctH2RlDx7XbcsCAwEAAaMNMAswCQYDVR0TBAIwADAN
BgkqhkiG9w0BAQsFAAOCAQEADHODX5CcMLI5fdumzly5FAVg5Yc22eDGNhmyhi/N
kDhP6QYw+HW5nWEYapc9m/ZQGEEoxr+wj6qeEhscxRxpuEIcunZsLKcoAmToyXeO
ANMslQugRcGqN57Pt0h5VuctLMa3ickeVPFvV6gxJSHBNRK1iN8nrfsy+zR+stzI
xcjIuakDDxMKFtb/1TMKf4/EsimSQLS0WXLjbxfQ/J510O4/Of0tmZI0ZIG+cKmM
V5hAOtuuAk6jREfWYJQ3DB+phv7PO9s2FpofVJss5PK4NWDS7UQOv359ZOJ85ZpJ
ihGxDqV7IAHJZNM9lvFXz/+EOn1oTGW9V8bAwt34OVYoPw==
-----END CERTIFICATE-----
subject=/CN=8f75dc271013
issuer=/CN=8f75dc271013
---
No client certificate CA names sent
---
SSL handshake has read 1682 bytes and written 637 bytes
---
New, TLSv1/SSLv3, Cipher is DHE-RSA-AES256-SHA
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : SSLv3
    Cipher    : DHE-RSA-AES256-SHA
    Session-ID: 0B6E7E510F03F05921CCA9FE98DB274611DABD2011182EF60587DF3BDC48E41D
    Session-ID-ctx: 
    Master-Key: 375A7219724235F91EFDBB5FE3A806D887D233792B5F4304F010230191E8E6623CEF71423C0C8359FE45C918AF202268
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    Start Time: 1507220566
    Timeout   : 300 (sec)
    Verify return code: 18 (self signed certificate)
---
cluFn7wTiGryunymYOu4RcffSxQluehd
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

read:errno=0
bandit16@bandit:~$ mkdir /tmp/test/
bandit16@bandit:~$ cd /tmp/test
bandit16@bandit:/tmp/test$ touch sshkey.private
bandit16@bandit:/tmp/test$ nano sshkey.private
bandit16@bandit:/tmp/test$ nano sshkey.private
bandit16@bandit:/tmp/test$ chmod 600 sshkey.private
bandit16@bandit:/tmp/test$ ssh -i sshkey.private bandit17@localhost
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is ee:4c:8c:e7:57:2c:bc:63:24:b8:e6:23:27:63:72:9f.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'localhost' (ECDSA) to the list of known hosts.
```

### Level 17

```
bandit17@bandit:~$ diff passwords.new passwords.old
42c42
< kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
---
> bECYSoXjOeGseirUCztuCBDF3xXqE7By
```

### Level 18

```
ssh bandit18@bandit.labs.overthewire.org "bash --norc"
or
ssh bandit18@bandit.labs.overthewire.org cat readme

IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```

### Level 19
```
bandit19@bandit:~$ ./bandit20-do /bin/sh
$ ls
bandit20-do
$ whoami
bandit20
$ cat /etc/bandit_pass/bandit20 <-------- bandit passwords found in this location
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```

### Level 20

```
bandit20@bandit:~$ ls
suconnect
bandit20@bandit:~$ ./suconnect
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the
correct password from the other side, the next password is transmitted back.
 

bandit20@bandit:~$ nc -l 1234
 
(in another shell)
bandit20@bandit:~$ ./suconnect 1234
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
 
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Password matches, sending next password
```

### Level 21

```
bandit21@bandit:~$ cd /etc/cron.d/
bandit21@bandit:/etc/cron.d$ ls -lah
total 32K
drwxr-xr-x   2 root root 4.0K Sep 28 14:04 .
drwxr-xr-x 119 root root 4.0K Oct  5 17:44 ..
-rw-r--r--   1 root root  102 Feb  9  2013 .placeholder
-rw-r--r--   1 root root  355 May 25  2013 cron-apt
-rw-r--r--   1 root root  120 Sep 28 14:04 cronjob_bandit22
-rw-r--r--   1 root root  122 Sep 28 14:04 cronjob_bandit23
-rw-r--r--   1 root root  120 Sep 28 14:04 cronjob_bandit24
-rw-r--r--   1 root root  510 Aug  4 20:03 php5
bandit21@bandit:/etc/cron.d$ cat cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```

### Level 22
bandit22@bandit:~$ cd /etc/cron.d/
bandit22@bandit:/etc/cron.d$ cat cronjob_bandit23
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget


bandit22@bandit:/etc/cron.d$ echo I am user bandit23 | md5sum | cut -d ' ' -f 1 
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:/etc/cron.d$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

### Level 23
Very simple, don't be overwhelmed. The script below exectues and then deletes the scripts. We just need to create a script that reads the pass on bandit24 and then put it in /var/spool/bandit24

```
bandit23@bandit:~$ cd /etc/cron.d/
bandit23@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
	echo "Handling $i"
	timeout -s 9 60 ./$i
	rm -f ./$i
    fi
done


bandit23@bandit:/etc/cron.d$ bandit23@bandit:/etc/cron.d$ ls /var/spool
bandit24  cron  mail  plymouth  rsyslog

bandit23@bandit:/etc/cron.d$ mkdir /tmp/test
bandit23@bandit:/etc/cron.d$ cd /tmp/test
bandit23@bandit:/tmp/test$ nano script.sh
    #!/bin/bash

    cat /etc/bandit_pass/bandit24 > /tmp/test/pass
    
bandit23@bandit:/tmp/test$ chmod 777 script.sh
bandit23@bandit:/tmp/test$ cp script.sh /var/spool/bandit24
bandit23@bandit:/tmp/test$ cat pass
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```

### Level 24
Similarly, in level 23, we create a different script

```
#!/bin/bash
passwd="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

for a in {0-10000}
do
    echo $passwd' '$a | nc localhost 30002 >> result &
done


bandit24@bandit:/tmp/test$ chmod 777 script.sh
bandit24@bandit:/tmp/test$ ./script.sh
bandit24@bandit:/tmp/test$ sort result | uniq -u

Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
```

