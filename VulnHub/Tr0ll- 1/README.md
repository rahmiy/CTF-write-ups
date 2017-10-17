# Tr0ll: 1

https://www.vulnhub.com/entry/tr0ll-1,100/

Doing an nmap we see ftp, ssh and http are open. Considering the items fastest to check, I went to ftp to try login with anonymous. I find a pcap file and follow the tcp stream to find sup3rs3cr3tdirlol. Plugging this into the http we get ` 192.168.1.105/sup3rs3cr3tdirlol`. It  seems to be a binary, so we run it and it asks to find an address. Ran it through gdb and ida, but it didnt allow me to access 0x0856BF. Instead, I plugged it into the web url to give more directories. We see a list of usernames in `http://192.168.1.105/0x0856BF/good_luck/which_one_lol.txt` and a password in `http://192.168.1.105/0x0856BF/this_folder_contains_the_password/Pass.txt`. In fact the password is not the content of the file but the filename itself. Fair play. We can now ssh with overflow:Pass.txt

## Privilege Escalation

We do a `uname -a` and a searchsploit of the machine's name. We can run the overlayfs exploit https://www.exploit-db.com/exploits/37292/. Alternatively, we see that we get kicked out after a certain amount of time. This could be a cron task. So we find the `crontab -l` and cd to that cron and try to `cat cleaner.py`. We try to find suid bit files that may give us access. We run `find / -perm +6000 -type f -exec ls -ld {} \; 2>&1 | grep -v "Permission denied` or `find / -perm -2 -type f 2>/dev/null`. We see that the /lib/log/cleaner.py and see that it uses a wildcard. This reminded me of the hackthebox challenge Joker, which you can find the walkthrough by IppSec on YouTube, but less complicated as I later realised you can edit the script to add yourself (overflow) to the sudoers or spawn shell.
