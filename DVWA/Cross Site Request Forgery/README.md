# Cross Site Request Forgery - Low/Medium/High/Impossible


## Low/Medium/High

We see that changing the password makes a POST request to send some parameters over. For example, on low it is `http://192.168.1.24/DVWA/vulnerabilities/csrf/?password_new=asd1&password_conf=asd1&Change=Change#`. This can be easily executed through some sort of tag, e.g. img src or maybe a shortened link through email so that the attacker can make the user set the password of his choice. Also, it may be possible to use invisible iframe to hide these executions

Medium level checks the header is coming from the same domain and Hard has a CSRF token. One possible way to execute this attack would be to use the stored XSS attack (which are commonly used together) to store the something like use client sided JS to read the CSRF token with document.getID, then run the CSRF url with the token attached.
