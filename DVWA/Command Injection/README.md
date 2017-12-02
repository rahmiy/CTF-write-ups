# Command Injection - Low/Medium/High/Impossible


## Low/Medium/High

Command injection can easily be achieved by performing `;ls`. More info can be found on [OWASP](https://www.owasp.org/index.php/Command_Injection). A couple of options to try for would be to backticks, semicolons, '&' operator and pipes.

From there, we can view running processes, name of machine, configuration files (of server, website), logs, core files, groups, shadow, etc. 

