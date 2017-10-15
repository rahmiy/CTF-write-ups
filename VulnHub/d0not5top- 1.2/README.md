# d0not5top: 1.2 write-up

https://www.vulnhub.com/entry/d0not5top-12,191/

Make sure your attacker lab machine (Kali Linux) is in the same (virtual) network as d0not5top. First, we need to do some reconnaissance work. We find locate the d0not5top IP with:

`root@kali:~# nmap -sP 192.168.1.*` or `root@kali:~# netdiscover` or (to get more information about open ports) `nmap -sC -p- -A --open -T4 192.168.1.85`

then search for open ports:

```
root@kali:~# nmap 192.168.1.85

Starting Nmap 7.60 ( https://nmap.org ) at 2017-09-13 00:20 BST
Nmap scan report for D0Not5top.home (192.168.1.85)
Host is up (0.00011s latency).
Not shown: 995 closed ports
PORT    STATE SERVICE
22/tcp  open  ssh
25/tcp  open  smtp
53/tcp  open  domain
80/tcp  open  http
111/tcp open  rpcbind
MAC Address: 00:0C:29:DA:17:0C (VMware)

Nmap done: 1 IP address (1 host up) scanned in 1.74 seconds

```

Now with this information, I'll go through logically my steps on which flags I found first.

### Flag 3 - SMTP
netcat to the open port SMTP gives us a cryptic looking message. It looks like a hexdump, so we pipe that message into xxd.
```
root@kali:~# nc 192.168.1.85 25
220 46 4c 34 36 5f 33 3a 32 396472796 63637756 8656874 327231646434 717070756 5793437 347 3767879610a EXIM SMTP

root@kali:~# echo "46 4c 34 36 5f 33 3a 32 396472796 63637756 8656874 327231646434 717070756 5793437 347 3767879610a" | xxd -r -ps
FL46_3:29dryf67uheht2r1dd4qppuey474svxya

```

### Flag 1 - view-source:http://192.168.1.85/control/
Port 80 is open which lead to a website. We first scan with `nikto -h 192.168.1.85` to find many directories, most which are just empty. We also do a wfuzz to find more directories nikto does not check for: `wfuzz -c -z file,/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt --hc 404,301 http://192.168.1.85/FUZZ/`. wp-admin directory is probably a wordpress website. 

We find control from wfuzz to see the page source in the browser and we have our flag:
`view-source:http://192.168.1.85/control/`
`FL46_1:urh8fu3i039rfoy254sx2xtrs5wc6767w`

### Flag 2 - view-source:http://192.168.1.85/control/js/
Now we can fuzz `wfuzz -c -z file,/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt --hc 404,301 http://192.168.1.85/control/FUZZ/` to find more directories. Investigating a bit further, we find a README.MadBro file in the JS folder.
```
FL101110_10:111101011101
1r101010q10svdfsxk1001i1
11ry100f10srtr1100010h10
```
From the first line, we definitely know its binary. At first I thought it was chunked but it is not. Taking FL101110_10, 101110 is 46 in decimal. So, we have our flag:

`FL46_2:39331r42q2svdfsxk9i13ry4f2srtr98h2`

### Flag 4 - http://d0not5topme.ctf
To find more files, missed by wfuzz (e.g. files with extensions) we can use gobuster, `gobuster -u http://192.168.1.85/control/ -f -e -x html,jpg,css,txt,png,gif,lock,zip,git,php -w /usr/share/wordlists/dirb/common.txt` to find http://192.168.1.85/control/hosts.txt

We see that an entry d0not5topme.ctf which we can add to our own host file through /etc/hosts. E.g. add entry `192.168.1.85 192.168.1.135   d0not5topme.ctf`. Visiting the website gives a forum, we can use `nikto -h d0not5topme.ctf` to find more information about the site. However, with a little luck, at the registration page, clicking on "I do not agree to those terms" sends a weird parameter. We can use the developer tools > network tab, to see the form data. We have a parameter `FLaR6yF1nD3rZ_html` being sent. Visiting the page http://d0not5topme.ctf/FLaR6yF1nD3rZ_html, gives us some crytpic message. This is in BrainFuck and decoding it gives us our flag:
`FL46_4:n02bv1rx5se4560984eedchjs72hsusu9`

The lesson here is to check everything including cookies, source code and headers, albeit a little disappointing.

### Flag 5 -  http://g4m35.ctf/H3x6L64m3/textures/skybox/dawnclouds/nz.jpg
Now playing around with the login section, we can see it gave the form Board Administrator links to Megusta@G4M35.ctf. We add this into our host file and visit the page. We can see that we may need to hack this game, possibly. We can see that it runs through JS, so we can do it via the console. Alternatively, we can check the JS files through the network tab to see anything interesting. In the game.js, we see the GAME_OVER function returns what looks like a URL to go to a directory (/H3x6L64m3). We can now visit http://g4m35.ctf/H3x6L64m3/, which happens to be another game that is run on three.js this time. We run `nikto -h http://g4m35.ctf/H3x6L64m3/` to find any interesting. Visiting the directories we see that  textures/skybox/dawnclouds folder has some pictures with the code on them. 

```
\106\114\64\66\137\65\72\60\71\153\70\67\150\66\147\64\145\62\65\147\150\64\64\
167\141\61\162\171\142\171\146\151\70\71\70\150\156\143\144\165
```

This is in octal and converting it gives us our flag
`FL46_5:09K87H6G4E25GH44WA1RYBYFI898HNCDU`

### Flag 6 - ssh MeGustaKing@192.168.1.58
After beating the game or found in http://g4m35.ctf/H3x6L64m3/bkcore/hexgl/Gameplay.js, we have our next domain https://t3rm1n4l.ctf/, we add this to our host file as well. This leads to a terminal, which requires a password. Funny enough, the password is the same as the user, t3rm1n4l.ctf. Now that we are in, we can try to find what is inside. However, we denied most of the time. We can use `grep * *` to find anything on the system. We found a directory with the name  M36u574.ctf and added this to our hosts file once again. 

https://M36u574.ctf reloads each page with a new image. There must be some metadata on these images. Now checking each one, we find that kingmegusta.jpg has something interesting. `file kingmegusta.jpg` did not give the whole string, so I had to use online tools or exiftool to give `MeGustaKing:$6$e1.2NcUo$96SfkpUHG25LFZfA5AbJVZjtD4fs6fGetDdeSA9HRpbkDw6y5nauwMwRNPxQnydsLzQGvYOU84B2nY` This looks like a password, so we use save that in a file called pass, and run `john --wordlist:/usr/share/wordlists/rockyou.txt pass`. To note, you need to have unzipped the rockyou.txt.bz2. We now have the password `**********`, that is actually the password btw.

Rememeber, the ssh port was open, we can now `ssh MeGustaKing@192.168.1.58` and log in. We get some code at the login message which looks like base64.

```
echo "U2FsdGVkX1/vv715OGrvv73vv73vv71Sa3cwTmw4Mk9uQnhjR1F5YW1adU5ISjFjVEZ2WW5sMk0zUm9kemcwT0hSbE5qZDBaV3BsZVNBS++/ve+/ve+/vWnvv704OCQmCg==" | base64 -d Salted__�y8j���Rkw0Nl82OnBxcGQyamZuNHJ1cTFvYnl2M3Rodzg0OHRlNjd0ZWpleSAK���i�88$&
    
echo "Rkw0Nl82OnBxcGQyamZuNHJ1cTFvYnl2M3Rodzg0OHRlNjd0ZWpleSAK" | base64 -d
FL46_6:pqpd2jfn4ruq1obyv3thw848te67tejey
```

### Flag 7 - 
It also looked like there was another username due to the login message "Uh0h.. u n0 burtieo". Now, we try to bruteforce with 
`hydra -l burtieo -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.85` to get the password `Lets you update your FunNotes and more!` which took a a couple of hours. We can login via `ssh burtieo@192.168.1.85`. We can run `compgen -c ` to find what commands are available. The idea here is to escalate our privlege to be root.



