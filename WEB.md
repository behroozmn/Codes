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

# 4. 🅰️Commands

## 4.1. 🅱️curl

دستورات یا مرورگر‌های مشابه متنی ترمینال: links و links2 و lynx(دستور www-browser)

```shell
curl -I itsee.ir #نمایش هدرهای یک سایت
curl -u username:password -T file.tar.gz ftp://ftp_server
```

## 4.2. 🅱️wget

- [-b] → قرار دادن پروسه دانلود در بک‌گراند و عدم نمایش و این معمولا برای فایل‌های بزرگ کاربرد دارد
- [-c] → اگر دانلود متوقف شد مجددا ادامه دانلود را از سر گیرد
- [-f]: ایجاد یک فایل برای لاگ شدن وضعیت پیشرفت دانلود
- [-i] → ذخیره چندین یو‌آر‌ال در فایل و سپس دانلود لینک‌ها از فایل
    - wget -i ./FileName.txt
- [-l]: سطح بازگشت را تعیین میکند
    - اِل است و نه آی
- [-np] or [--no-parent] عدم رجوع به مسیر بالاتر
- [-O] Name → انتخاب نام جدید به فایل دانلود شده
- [-o ./download.log] → ذخیره لاگ در یک فایل بجای نمایش در ترمینال
- [-P]: قرار دادن در یک فولدر دیگر
    - [-P /documents/websites]:تمام محتوا به فهرست مشخص شده ما می رود
- [-Q5m] → پایان دانلود وقتی سایز دانلود شده از مقدار ۵مگابایت فراتر برود
- [-r] or [--recursive] دانلود به صورت بازگشتی
- [-R] or [--reject] → عدم دانلود یک نوع فایل معین ، در هنگام دانلود
    - wget -P documents/archives/ https://wordpress.org/latest.zip
- [--limit-rate=200k] → تعیین سرعت دانلود
- [--user-agent] → برخی سایت‌ها با تشخیص اینکه شما از مرورگر برای دانلود استفاده نمی‌کنید،می‌تونن اجازه دانلود به شما ندهند و شما توسط این گزینه نقاب می‌زنید و تحت عنوان مثلا فایرفاکس متصل می‌شوید
    - wget --user-agent="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092416 Firefox/3.0.3" <URL>
- [--tries] → تعداد پیش‌فرض تلاش مجدد برای دانلود عدد۲۰ است و می‌تونیم آنرا تغییر دهیم
    - wget --tries=75 URL
- [--spider]: قراردادن در وضعیت اسپایدر
- [-mirror]: دانلود را بازگشتی می کند
- [-convert-links]: همه لینک‌ها برای استفاده آفلاین مناسب تبدیل خواهند شد
- [-page-requisites]: موارد زیر شامل تمام فایل‌های ضروری مانند «سی‌اِس‌اِس» و «جِی‌اِس» و تصاویر می شود
- [-no-parent]:تضمین می‌کند که دایرکتوری‌های بالای سلسله مراتب دانلود نمی‌شوند


- `wget --ftp-user=USERNAME --ftp-password=PASSWORD DOWNLOAD-URL`
- `wget --spider --force-html -r -l5 htp://dl.folan.net/Movie/ 2>&1 | grep '^--' | awk '{ print $3 }' | grep -v '\.css\|js\|png\|gif\|jpg$' | grep -v '\/$'`
- `wget --mirror --convert-links --page-requisites --no-parent -P documents/websites/ URL` #می توان از دستور wget برای دانلود محتوای کل سایت استفاده کرد
- `wget -r -np -R "index.html*" https://shop.hemat-elec.ir/wp-content/themes/irankala/assets/fonts` # Note: دانلود فایل های مشخص شده
    - wget -r -A.pdf

</div>