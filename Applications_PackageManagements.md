# 📍️ Application

# 📍️ group:PackageManagements

## Debian

### source.list

```shell
part1 part2 part3 part4
```

* part1
    * deb: دانلود فایل‌های اجرایی
    * deb-src: دانلود سورس پکیج‌شده که برای دِوِلُپ یا دیباگ استفاده می‌شود
* part2
    * URL
* part3
    * bullseye → Debian11
* part4
    * Main:بطور کامل توسط شرکت سازنده پشتیبانی می‌شود
    * Restricted: پشتیبانی می‌شود ولی بطور کامل پشتیبانی نمیشود مثل درایور های شرکت ان ویدیا
    * Universe: توسط کامیونتی‌ها پشتیبانی می‌شود و برنامه های رسمی نیستند
    * Multiverse: رایگان نیستنتد
    * partner: [بهروز: باید بررسی شود]
    * می‌تواند چندین قسمت باشد یعنی هم شامل main و هم شامل Universe و هم شامل موارد دیگر باشد

☑️ **Examples:**

```shell
# 1️⃣️ Debian11:
  cat /etc/apt/sources.list|grep -v -E '#|$^'|grep . 
  deb http://deb.debian.org/debian/ bullseye main contrib non-free 
  deb-src http://deb.debian.org/debian/ bullseye main contrib non-free 
  deb http://security.debian.org/debian-security bullseye-security main contrib non-free 
  deb-src http://security.debian.org/debian-security bullseye-security main contrib non-free 
  deb http://deb.debian.org/debian/ bullseye-updates main contrib non-free 
  deb-src http://deb.debian.org/debian/ bullseye-updates main contrib non-free 

# ✅ Debian11: HOME
  deb http://deb.debian.org/debian/ bullseye main
  deb-src http://deb.debian.org/debian/ bullseye main
  deb http://security.debian.org/debian-security bullseye-security main contrib
  deb-src http://security.debian.org/debian-security bullseye-security main contrib
  deb http://deb.debian.org/debian/ bullseye-updates main contrib
  deb-src http://deb.debian.org/debian/ bullseye-updates main contrib
  deb http://security.debian.org/ bullseye-security main

```

### ✅️ apt

* [install] PackageName
    * install --fix-broken
* [remove] PackageName
* [purge] PackageName
* [show] PackageName
* [list] PackageName
* [search] PackageName

☑️ **Examples:****

* sudo apt download $(sudo apt-cache depends php7.0 | awk '{print$2}'|grep -v ">"|grep -v "<") # DownloadAllDependency
* apt --option Acquire::HTTP::Proxy="socks5h://127.0.0.1:9150" update

### ✅️ apt-get

* [install] PackageName #نصب بسته
    * [install] PackageName --print-urls #نمایش آدرس دانلود بسته‌ها
        * بجای نصب فقط آدرس «یوآرال» نمایش خواهد داد
* [update] #بروزرسانی لیست همه بسته‌های موجود در مخازن
* [upgrade] #آپگرید همه بسته‌ّای نصب شده به نسخه جدیدتر
* [remove] PackageName #حذف یک بسته با پسوند دب از روی سیستم توسط ابزار اَپْت
* [check] # بررسی وضعیت پیش‌نیاز‌ها یا همان دیپندنسی
* [clean] #پاک کردن کش که شامل بسته‌های پسوند دب دانلود شده است
    * [clean] all #حذف تمام کش مدیریت بسته

☑️ **Examples:**

* sudo apt-get download php && apt-cache depends -i php |awk '/Depends:/ {print $2}' | xargs apt-get download # DownloadAllDependency

### ✅️ apt-cache

* apt-cache search PackageName #جستجوی بسته موردنظر

### ✅️ ap-cdrom

ap-cdrom install PackageName #نصب یا آپگرید یک بسته باپسوند دب از روی سی‌دی‌رام

### ✅️ dpkg

* [-i PackageName.deb] # نصب آپگرید یک بسته
* [-r <Package>] #حذف یک بسته نصب شده
* [-l] # نمایش همه بسته‌های با پسوند دِب نصب شده در سیستم
* [-s PackageName] # نمایش اطلاعات مربوط به یک بسته خاص نصب شده در سیستم
* [-L PackageName] # نمایش لیست فایل‌ّای مربوط به یک بسته نصب شده
* [-L PackageName] # لیست تمام فایل‌های یک برنامه
    * dpkg -L vim
* [--contents PackageName.deb] # نمایش لیست فایل‌های مربوط به یک بسته که هنوز نصب نشده
* [-S /bin/ping] # بررسی اینکه فایل موردنظر به کدام بسته تعلق دارد

### ✅️ dpkg-query

* dpkg-query -L <PackageName> # نمایش تمام فایل‌ها و فولدرهای نصب شده از یک بسته
* dpkg-query --list # نمایش لیست تمام برنامه‌های نصب شده با جزئیات آن

### ✅️ dpkg-deb

* dpkg-deb -c <PackageName>.deb # تمام فایل‌هایی که قرار است با این بسته در سیستم نصب شود
* dpkg-deb -I FileName.deb # دریافت اطلاعات فایل به همراه تمامی دیپندنسی های این بسته(آی بزرگ)

### LocalRepository[DVD]

1. download DVD From Debian website
2. sudo vim /etc/apt/sources.list
3. mount file to specific directory with next line command:
    1. [temporary]:sudo mount -o loop /home/behrooz/App/DVD/debian-9.3.0-amd64-DVD-1.iso /media/repo_1
    2. [Permanently]:
        1. sudo vim /etc/fstab
        2. edit: /home/behrooz/App/DVD/debian-9.3.0-amd64-DVD-1.iso /media/repo_1 iso9660 defaults 0 0
4. sudo vim /etc/apt/sources.list
5. add:  deb [trusted=yes] file:///media/repo_1 stretch main contrib
6. sudo mount -a
7. lsblk
   dpkg -S /bin/ping # بررسی اینکه فایل موردنظر به کدام بسته تعلق دارد

### LocalRepository[WEB]

1. apt-get install build-essential apache2
2. mkdir /var/www/html/packages /var/www/html/packages/amd64
3. mount /dev/cdrom /media/cdrom
4. DVD1:find /media/cdrom/pool/ -name "*.deb" -exec cp {} /var/www/html/packages/amd64 \;
5. DVD2:find /media/cdrom/pool/ -name "*.deb" -exec cp {} /var/www/html/packages/amd64 \;
6. DVD3:find /media/cdrom/pool/ -name "*.deb" -exec cp {} /var/www/html/packages/amd64 \;
7. cd /var/www/html/packages/amd64/
8. dpkg-scanpackages . /dev/null | gzip -9c > Packages.gz

* SERVER:
    * vim /etc/apt/sources.list: `deb file:/var/www/html/packages/amd64/ /`
* CLIENT
    * vim /etc/apt/sources.list: `deb <http://192.168.1.150/packages/amd64/> /`

## CentOS

### ✅️ yum

* yum whatprovides "*CA.pl" #چه بسته‌هایی این نام را درون خود دارند
* yum -y install PackageName #دانلود و نصب یک بسته «آرپی‌ام»از مخازن
* yum localinstall PackageName #نصب یک بسته «آرپی‌ام» و تلاش برای حل پیش‌نیازها با استفاده از مخازن
* yum -y update #آپدیت همه بسته های «آرپی‌ام» نصب شده در سیستم
* yum update PackageName #آپگرید یک سته «آرپی‌ام» به نسخه جدیدتر
* yum remove PackageName #حذف یک بسته «آرپی‌ام» با استفاده از ابزار یام
* yum list #نمایش لیست همه بسته‌های نصب شده در سیستم
* yum search PackageName #پیدا کردن یک بسته از مخازن
* yum clean PackageName #پاک کردن کش که شمال بسته‌های «آرپی‌ام» دانلود شده توسط یام است
* yum clean headers #پاک کردن همه فایل‌های هِدِر که سیستم برای حل پیش‌نیازها از آنها استفاده می‌کند
* yum clean all #پاک کردن همه فایل‌های هِدِر و کش

### ✅️ rpm

* rpm -ivh Package.rpm #نصب یک بسته جدید
* rpm -ivh nodeeps Package.rpm #نصب یک بسته بدون درنظر گرفتن بسته‌های پیش‌نیاز
* rpm -U Package.rpm # آپگرید یک بسته بدون تغییر فایل‌های تنظیماتی مربوط به آن بسته
* rpm -F Package.rpm #آپگرید یک بسته فقط در حالتی که آن بسته نصب شده باشد
* rpm -e PackageName #حذف یک بسته از سیستم
* rpm -qa #نمایش همه بسته‌هایی که در سیستم نصب شده است
* rpm -qi PackageName #نمایش اطلاعات مربوط به یک بسته نصب شده
* rpm -qg "System Environment/Daemons" #نمایش بسته‌های «آرپی‌ام» مربوط به یک گروه نرم‌افزاری
* rpm -ql PackageName #نمایش لیست فایل‌های مربوط به یک بسته «آرپی‌ام» نصب شده
* rpm -qc PackageName #نمایش لیست فایل‌های تنظیماتی مربوط به یک بسته «آرپی‌ام» نصب شده
* rpm -q PackageName -whatrequires #نمایش لیست پیش‌نیازهای یک بسته «آرپی‌ام» نصب شده
* rpm -q PackageName -whatprovides #نمایش قابلیت‌های یک بسته «آرپی‌ام» مدنظر
* rpm -q PackageName -scripts #نمایش اسکریپت‌های اجرا شده در حین عمل نصب یا حذف یک بسته «آرپی‌ام» مدنظر
* rpm -q PackageName -changelog #نمایش تغییر اتیک بسته «آرپی‌ام» نسبت به نسخه‌ی قبلی
* rpm -qf /etc/httpd/conf/httpd.conf #بررسی اینکه فایل مورد نظر به کدلم بسته‌ی «آرپی‌ام» تعلق دارد
* rpm -qp PackageName -l #نمایش لیست فایل‌های مربوط به یک بسته «آرپی‌ام» که هنوز نصب نشده است
* rpm -import /media/cdrom/RPM-GPG-KEY #وارد کردن کلید
* rpm -cheksig Package.rpm #بررسی سالم بودن یک بسته «آرپی‌ام» مدنظر
* rpm -qa gpg-pubkey #بررسی سالم بودن همه بسته‌های نصب شده
* rpm -V PackageName #چک کردن حجم و هش «ام‌دی‌فایو» و مجوز و سایر مشخصات یک بسته «آرپی‌ام» مدنظر
* rpm -Va #چک کردن حجم و کد هش «ام‌دی‌فایو» و مجوز و سایر مشخصات همه بسته‌های «آرپی‌ام» مدنظر
* rpm -Vp PackageName.rpm #جک کردن حجم و هش «ام‌دی‌فایو» و سایر مشخصات یک بسته «آرپی‌ام» نصب نشده
* rpm -ivh /usr/src/redhat/RPMS/`arch`/PackageName.rpm #نصب یک بسته ساخته‌شده از سورس یک‌بسته «آرپی‌ام» مدنظر

### EPEL

Epel: Extra Packages for Enterprise Linux

* install
    * Cenots 7 64bit : rpm -ivh <http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-7.noarch.rpm>
    * Cenots 6 64bit :rpm -ivh <http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm>
    * Cenots 6 32bit :rpm -ivh <http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm>
    * Cenots 5 64bit :rpm -ivh <http://download.fedoraproject.org/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm>
    * Cenots 5 32bit :rpm -ivh <http://download.fedoraproject.org/pub/epel/5/i386/epel-release-5-4.noarch.rpm>
* configFile
    * /etc/yum.repos.d/epel.repo

### ✅️ rpmbuld

* rpmbuild -rebuild PackageName.src.rpm #ساختن یک فایل «آرپی‌ام» از روی سورس یک بسته «آرپی‌ام»

### ✅️ rpm2cpio

```shell
rpm2cpio PackageName | cpio -extract -make directories *bin* #استخراج فایل‌های اجرایی از یک بسته «آرپی‌ام»
```
