# FristiLeaks: 1.3

https://www.vulnhub.com/entry/fristileaks-13,133/

We netdiscover to find http://192.168.1.90 and then do a nmap to only find port 80 HTTP open. So, we visit the site and perform our normal scans.

```
nikto -h http://192.168.1.90
gobuster -u http://192.168.1.90/ -f -e -x html,jpg,css,txt,png,gif,lock,zip,git,php -w /usr/share/wordlists/dirb/common.txt
dirb http://192.168.1.90/ /usr/share/wordlists/dirb/common.txt
```

Nothing interesting in the robots.txt file and its respective pages. We read the front page again and try with http://192.168.1.90/fristi/ to get the front page. Doing a gobuster `gobuster -u http://192.168.1.90/fristi -f -e -x html,jpg,css,txt,png,gif,lock,zip,git,php -w /usr/share/wordlists/dirb/common.txt` gives us a upload.php and upload page, which redirects us.  In the view source, we see some base64 code and try to decode it to get a possible password. We find a user so we try eezeepz:keKkeKKeKKeKkEkkEk and we're in.

Once again, we upload the shell found [here](http://pentestmonkey.net/tools/web-shells/php-reverse-shell) (making sure we set the attacker's IP in the reverse shell) which is rejected due to not correct extension, instead we try `php-reverse-shell.php.jpg` and it is accepted. We can now `nc -lvp 1234` and go to http://192.168.1.90/fristi/uploads/php-reverse-shell.php.jpg to execute, now we are in. Now, we can `cd /home/eezeepz` and `cat notes.txt` to execute the script in tmp to give us root access.
