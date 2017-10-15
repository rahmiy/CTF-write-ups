# De-ICE: S1.110 - write-up

https://www.vulnhub.com/entry/de-ice-s1110,9/

We do a netdiscover to figure our the server's IP. Instead of manually doing nmap, nikto, etc. We will try Sparta and probe the web server. We can ftp to the server, and put in anoynmous with any password. We find a shadow file at download/etc and can `get shadow` and `get core`. We then use `john --wordlist:/usr/share/wordlists/rockyou.txt shadow` to yield no finds strangely. So, we try `strings core` to see some hashed passwords. We then use `john --wordlist:/usr/share/wordlists/rockyou.txt corepass` to get only 2 cracked password.

```
root:Complexity:13574:0:::::
bbanter:Zymurgy:13571:0:99999:7:::
```

Once again, root gets denied from ssh, so we log in using bbanter. I tried to sudo su at first, but later found out that sudo asks for your own password whereas we want to be asked the root password, so just su is sufficient. We change to root and then we can `locate *.enc` and `updatedb` to find the customer information encrypted file at `/mnt/live/memory/changes/home/root/.save`. There is another file `copy.sh` which neatly tells us the encryption used, so we `openssl enc -d -aes-256-cbc -salt -in customer_account.csv.enc -out /home/ftp/incoming -pass file:/etc/ssl/certs/pw` and finally log in to the ftp server to get the decrypted file. DONE! This challenge was much easier than its previous, good work De-ICE!
