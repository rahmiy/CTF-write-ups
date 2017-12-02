# DVWA Write-ups
Write-up for Damn Vulnerable Web Application (DVWA)

## Setup - Kali Linux

If you are using Kali Linux, you will need to follow this [video](https://www.youtube.com/watch?v=TIUjANlD1tc). Essentially, you need to get php5 (including MySQL), which was removed from the rolling main. So, you will need to add an entry into the source files and install it. The additional stuff after 10mins mark on the video is not needed.

Make sure that you `a2dismod php7.0 and a2enmod 5.6` when you have it installed. Also, since Kali Linux uses MariaDB, you must create a user, also shown in the video.

Finally, log in with default admin:password.
