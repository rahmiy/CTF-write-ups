# Insecure CAPTCHA - Low/Medium/High/Impossible


## Low/Medium/High

This is an interesting topic as there are Python libraries that could attempt to solve these. More recently, captcha have increased in difficulty by selecting portion of the image. However, this challenge has less to do with breaking the captcha, and more with how the captcha is implemented. For low difficulty, we see that after resolving the captcha, we confirm the changes in the password. Looking at the parameters in the network tab, we see the variable step. Simply altering it will confirm the changes e.g. `?step=2&password_new=password&password_conf=password&Change=Change.`. Similarly, for medium, we have another parameter `pass_captcha` which we need to set to true.
