<div dir="rtl">

![uri.png](_srcFiles/Images/uri.png "uri.png")

# 1. 🅰️HTTP(Hypertext Transfer Protocol)

* Port:80
* پروتکل http بهترین ابزار دسترسی فایل بدون داشتن دسترسی public برای عموم است
* مرورگرها قابلیت اتصال به سرور تحت پروتکل http/https دارد
* وب‌سایت: یک سایت نمایش است با ملاحظات خود
* وب اپلیکیشن: یک برنامه سازمانی است که درقالب وب به نمایش درمی‌آید
*

## 1.1. 🅱️HTTP Methods

* Get: همواره پارامترها را در یوآرآل می‌فرستد
    * Selectation
* Postاطلاعات را در بادی می‌فرستد
    * مقداری از گِت با امنیت‌تر است
    * ارسال مقدار زیاد را فقط با پست می‌توان ارسال کرد
    * Insertation
* Head(Like GET but only headers)
* Put: معمولا جایی که در فضای بروزرسانی است
* Patch(apply patial modifications to a resource)
    * از سمت کلاینت مودیفیکیشن کوچک ارسال کنین
* Delete
    * برای حذف مقداری
* Trace
    * آیا سرور زنده است یا خیر
* Option(http methods that the server supports)
    * چه متدهایی را ساپورت می‌کند
* Connect(Establishes a tunnel to a server)
    * ارتباط تونل

## 1.2. 🅱️Headers.Request

* Get:
* Host:
    * itsee.ir
* accept: کلاینت چه مواردی را انتظار دارد
    * text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
* user-agent: مرورگر چه چیزی است
    * Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
* Accept-Encoding: برای تسهیل مشخص می‌شود که این مرورگر قابلیت فهم چه نوع فشرده‌سازی را دارد
    * gzip, deflate
* Accept-Language:
    * en-US,en;q=0.5
* Connection
    * keep-alive
* If-Modified-Since:
    * Fri, 24 Mar 2023 10:47:57 GMT
* If-None-Match
    * "1d18-641d7fdd-43aeb9c7c101613e;gz"
* Upgrade-Insecure-Requests
    * 1

## 1.3. 🅱️Headers.Response

* ServerResponseCode(Status):
    * 200:OK
* Connection
    * Keep-Alive
* Date: اگر مرورگر کش کرده و تغییر نداشته همونو نشون بده
    * Mon,03 Apr 2023 06:31:47 GMT
* Etag
    * "1d18-641d7fdd-43aeb9c7c101613e;gz"
* Server
    * LiteSpeed
* Vary
    * User-Agent

![httpBasicSession.png](_srcFiles/Images/httpBasicSession.png "httpBasicSession.png")

# 2. 🅰️HTTPS(Secure Hypertext Transfer Protocol)

* Port: 443
* پروتکل http که با ssl امنیت آن افزایش یافته است

![httpsBasicSession.png](./_srcFiles/Images/httpsBasicSession.png "httpsBasicSession.png")

# 3. 🅰️CGI(Common Gateway Interface)

* CGI یا Common Gateway Interface: استانداردی برای تولید صفحات پویای وب توسط سرور که حاوی مشکلاتی بود:
* تاخیر در تعداد کلاینت زیاد
* هر درخواست یک پردازه جدید یعنی بار افزوده برای سرور بود
* محدود برای برخی زبان‌ها(زبان‌های محدود به پلتفرم)
* باید قابلیت CGI را در وب‌سرور فعال نمایید
* قابلیت Get و Post وجود دارد
* دارای برخی CGI Environment Variables

```shell
#!/usr/bin/python

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Hello World - First CGI Program</title>'
print '</head>'
print '<body>'
print '<h2>Hello World! This is my first CGI program</h2>'
print '</body>'
print '</html>'
# OUTPUT: 
# Hello World! This is my first CGI program
```

[Link](http://www.test.com/cgi-bin/hello_get.py?first_name=ZARA&last_name=ALI)

```shell

#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s %s</h2>" % (first_name, last_name)
print "</body>"
print "</html>"
OUTPUT:
Hello ZARA ALI
```

[URL](http://localhost/cgi-bin/env.sh?namex=valuex&namey=valuey&namez=valuez)

```shell
#Shellscript CGI
#!/bin/bash
echo "Content-type: text/html"
echo ""
echo '&lt;html&gt;'
echo '&lt;head&gt;'
echo '&lt;meta http-equiv="Content-Type" content="text/html; charset=UTF-8"&gt;'
echo '&lt;title&gt;Environment Variables&lt;/title&gt;'
echo '&lt;/head&gt;'
echo '&lt;body&gt;'
echo 'Environment Variables:'
echo '&lt;pre&gt;'
/usr/bin/env
echo '&lt;/pre&gt;'

echo '&lt;/body&gt;'
echo '&lt;/html&gt;'

exit 0

```

> تصویر نمایی از حالت قدیمی را نمایش میدهد
![cgi.jpg](./_srcFiles/Images/cgi.jpg "cgi.jpg")

</div>