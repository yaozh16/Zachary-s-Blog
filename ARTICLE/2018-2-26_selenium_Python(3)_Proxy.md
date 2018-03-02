# 2018-2-26_selenium_Python(3)_Proxy
## Method
\[
\frac{1}{2}
\]
**code**
```
from selenium.webdriver.common.proxy import *  
ip=rdl(zd.keys())  
myProxy = ip  
proxy = Proxy({  
'proxyType': ProxyType.MANUAL,  
'httpProxy': myProxy,  
'ftpProxy': myProxy,  
'sslProxy': myProxy,  
'noProxy': ''   
})  
driver=webdriver.Firefox(proxy=proxy)  
```