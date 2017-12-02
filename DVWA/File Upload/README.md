# File Upload - Low/Medium/High/Impossible


## Low/Medium/High

For low, this is a simple case of uploading a reverse shell such as php-reverse-shell.php, and then visiting the link through `http://192.168.1.23/DVWA/hackable/uploads/php-reverse-shell.php`

For medium, there changing the extension could bypass this and/or intercepting and changing the content type to `image/jpeg` would work as it doesnt really check the filename extension explicitly. As for high, we have to upload the jpeg extension of the shell and then manually change the extension e.g `mv php-reverse-shell.php.jpeg php-reverse-shell.php` through other options such as the command injection one.
