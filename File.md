<div dir="rtl">

# 1. 🅰️Concepts

* فایل: مجموعه‌ای از سری داده که به‌صورت یک واحد ذخیره‌سازی(در حافظه اصلی یا جانبی یا حافظه موقت) شوند
  *RawData:
    * «داده‌خام» پردازش و قالب‌بندى نشده
    * اطلاعاتى كه جمع‌آورى شده‌اند، اما بررسى نشده‌اند.
    * متادیتا: ارائه توضیحات خلاصه راجع به فایل
    * استفاده از متادیتا، کارایی را افزایش داده و طبقه‌بندی را آسان می‌کنند.ـ متادیتا‌ها در متغیرهایی قابل تغییر و حذف یا اضافه‌شدن، ذخیره می‌شوند.
* Inode:
    * در سافت لینک آی نود عوض می‌شود ولی در هارد لینک آی نود عوض نمی‌شود
    * دستورات زیر آی نود یک فایل را به ما می‌دهد
    * `ls -i File` or `stat File`
* Link
    * HardLink
        * مقدار آی‌نود مشابه است. هارد لینک روی دایرکتوری ها قابل اجرا نیست
        * تنها در یک پارتیشن(فایل سیستم) قابل اجرا است
        * توسط دستور زیر می‌توان آی‌نود را مشاهده کرد [ls -i file.txt; stat file.txt]
        * بهتر است جستجوی هاردلینک توسط شماره آی نود جستجو شود `find . -inum 89`
    * SoftLink
        * در سافت لینک آی نود متفاوت است
        * امکان ساخت سافت لینک برای دایرکتوری وجود دارد ولی برای هارد لینک امکان ساخت دایرکتوری وجود ندارد
        * توسط دستور زیر می‌توان آی‌نود را مشاهده کرد `ls -i file.txt; stat file.txt`
    * FileDescriptor
        * در لینوکس همه چیز حتی دایرکتوری‌ها و سخت‌افزارها فایل هستند. هر فایل نیز یک عدد مخصوص به خود را دارد که file descriptor یا FD نامیده می شود.
        * سیستم عامل این FD را زمانی اختصاص می دهد که فایل باز شده باشد.
        * مثلا اگر یک برنامه خروجی خود را به FD مربوط به پرینتر ارسال کند آنگاه خروجی مورد نظر پرینت گرفته می شود.
    * Access Control
        * DAC یا Discretionary Access Control
            * لینوکس بصوتر یش فرض از این روش استفاده می‌کند
            * در این روش owner یک ریسورس(فایل یا دایرکتوری یا هرچیزی که از طریق شبکه به آن دسترسی داشت) کنترل کاملی بر روی آن دارد بصورتی که می تواند به سایرین دسترسی های مختلف بدهد و یا حتی مالک آن را تغییر دهد
            * روش کنترل دسترسی بسیار راحت و انعطاف پذیر است ولی در عین حال خیلی ایمن نیست.
        * MAC یا Mandatory Access Control
            * دسترسی‌ها بجای تعیین شدن توسط owner توسط سیستم تعیین می‌شود
            * تمامی user ها و resource ها دارای یک label خواهند بود که سطح اعتماد را تعیین می‌کند.
            * برای دسترسی به یک resource، کاربر باید در سطحی مساوی و یا بالاتر از سطح آن resource باشد.
            * عموما سیستم هایی که دارای دیتای بسیار مهمی هستند مانند سیستم های دولتی و نظامی، از روش MAC استفاده می کنند که از طریق [SELinux](https://actobit.com/actomag/1399/selinux/) پیاده‌سازی می شود.

```shell
rename "s/jpeg$/jpg/" *.jpeg  # convert all jpeg to jpg
```

<div style="display: flex; flex-direction: column; align-items: center;">


![MetaData.png](_srcFiles/Images/MetaData.png "MetaData.png")
![link-links2.jpg](_srcFiles/Images/link-links2.jpg "link-links2.jpg")

</div>

# 2. 🅰️ Accessibility

- در نسخه لینوکس‌های کوچک دستور adduser وجود دارد(توزیع لینوکس alpine) و دستور useradd دستور بزرگتری و با ابزارهای بیشتری است.

```shell
who #Current Login Users
who -a #نمایش تمامی اطلاعات
who -b #زمان بوت شدن سیستم
who -r #نمایش ران لول فعلی
who -q #تعداد کاربران لاگین و نام آنها

/sbin/usermod -s /sbin/nologin Behrooz #change user to nonlogin user

sudo last reboot #مشاهده ریبوت‌های انجام شده در سیستم در گذشته
```

## 2.1. 🅱️ Sudo

```shell
sudo
sudo -u <USER> whoami #اجرای دستور با کاربر خاص
sudo -- bash -c 'pwd; hostname; whoami' #Execute Multiple command
sudo cat /etc/sudoers.d/Behrooz
    user    ALL=NOPASSWD: /usr/bin/nmap 
    user    ALL=NOPASSWD: /usr/bin/apt 
    user    ALL=NOPASSWD: /usr/bin/sudo 
    user    ALL=NOPASSWD: /usr/bin/chmod 
    user    ALL=NOPASSWD: /usr/bin/chown 
    user    ALL=NOPASSWD: /usr/bin/vim 
    user    ALL=NOPASSWD: /usr/bin/systemctl 
    user    ALL=NOPASSWD: /usr/bin/updatedb 
    user    ALL=NOPASSWD: /usr/bin/dpkg 
    user    ALL=NOPASSWD: /usr/sbin/shutdown 
    user    ALL=NOPASSWD: /usr/bin/killall 
    user    ALL=NOPASSWD: /usr/bin/kill 
    behrooz ALL=(ALL) NOPASSWD: ALL # Run sudo command without password
```

# 3. 🅰️SpecialAttributes

* a: تنها در حالت اضافه شدن(الحاقی) قابلیت تغییر خواهد داشت.یعنی فایل کم نمی‌شود ولی زیاد می‌شود
* c: اجازه فشرده‌سازی و بازکردن خودکار یک فایل را به کرنل می‌دهد
* d: در این حالت در هنگام اجرای ابزار سیستمی دامپ یا نسخه پشتیبان در پارتیشن‌های «ای‌ایکس‌تی۳» از فایل مورد نظر پشتیبان تهیه نخواهد شد
* i: حتی توسط کاربر روت قابلیت تغییر نخواهد داشت
* s: امن بودن در برابر حذف شدن
* S: تغییرات در فایل همزمان برروی دیسک ذخیره خواهد شد
* u: اجازه بازیابی محتویات یک فایل حتی اگرکه کنسل شده باشد را می‌دهد

```shell
lsattr: show Special attributes in directory
chattr [+|-]<attributes> file.txt
chattr +a file.txt
chattr -a file.txt
```

# 4. 🅰️Permission

```shell
# r → Read
# w → Write
# x → Execute
# u → USER
# g → GROUP
# o → OTHER
# a → ALL
```

## 4.1. 🅱️ SUID

اگر فایلی این دسترسی را داشته باشد یعنی استفاده از این فایل با دسترسی مشابه روت صورت خواهد گرفت

What’s the benefit? The passwd command needs to edit files like /etc/passwd, /etc/shadow to change the password. These files are owned by root and can only be modified by root. But thanks to the setuid flag (SUID bit), a regular user will also be able to modify these files (that are owned by root) and change his/her password.

```shell
$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 59640 Mar 22 2019 /usr/bin/passwd
```

<div style="display: flex; flex-direction: column; align-items: center;">


![permissions.webp](_srcFiles/Images/permissions.webp "permissions.webp")

![permission.jpg](_srcFiles/Images/permission.jpg "permission.jpg")

![linux-special-permissions-explained.webp](_srcFiles/Images/linux-special-permissions-explained.webp "linux-special-permissions-explained.webp")

![linux-special-permission-suid-guid-sticky-bit.webp](_srcFiles/Images/linux-special-permission-suid-guid-sticky-bit.webp "linux-special-permission-suid-guid-sticky-bit.webp")

![perm_special.png](_srcFiles/Images/perm_special.png "perm_special.png")

![permis-accessmodes.jpg](_srcFiles/Images/permis-accessmodes.jpg "permis-accessmodes.jpg")

![sgid-linux.webp](_srcFiles/Images/sgid-linux.webp "sgid-linux.webp")

![sticky-bit-linux.webp](_srcFiles/Images/sticky-bit-linux.webp "sticky-bit-linux.webp")

![suid-linux.webp](_srcFiles/Images/suid-linux.webp "suid-linux.webp")


</div>

```shell
chmod o-w File.txt → Remove write from OTHER group
chmode u=rw,g=rwx,o=r file.txt
chmod u+x file.txt → add EXECUTE to USER group
```

# 5. 🅰️Backup

* برای بک‌آپ گرفتن مهم است که دیتای خود را دسته‌بندی کرده باشید
* انواع بک‌آپ گیری
    * fullBackup: همه دیتارا بکاپ می‌گیرد
    * Incremental: نسبت به fullBackupآخری هر جی اضافه دارد را بک‌آپ می‌گیرد
    * Differential: نسبت به یک نسخه خاص هرچی تفاوت دارد را بک‌آپ می‌گیرد
    * snapshot: همانند differential است

## 5.1. 🅱️ Apps

* backula یک برنامه فوق‌العاده قوی برای بک آپ از هر چیزی است که هم کامند و هم دسکتاپ و هم وب ارائه داده است

```shell
cp /Path/FileName{,.Backup} #CreateBackup
```



### 5.1.1. ✅️rsync

سوییج‌های دستور آرسینک

* a : تکراری کپی نشود و فقط جدید کپی شود
* h: خوانا برای انسان
* v: توضیحات زیاد داده شود

```shell
cp /Path/FileName{,.Backup} #CreateBackup
rsync -avh /home/behrooz/dire /tmp
rsync -avh /home/behrooz/dire behrooz@192.168.10.88:/home/SecondCopy
```

## 5.2. 🅱️ Archive and Compressing

```shell
tar -czvf Directory.tar.gz Directory --remove-files
tar tf File.tar.gz #فقط نمایش محتویات
tar j #bzip2
tar Uf File.tar Dir #آپدیت کن از فایل‌های جدید

```

# 6. 🅰️Tape

* برای ذخیره‌سازی بک‌آپ از نوار استفاده می‌شود
* opration در دستور mt موارد زیر را شامل می‌شود:
    * status: نمایش وضعیت
    * load: لود نمودن نوار(به تازگی خودشان لود می‌شوند)
    * fsf: به تعداد عددی که وارد میشود برو جلو یعنی fsf3 یعنی اشاره‌گر را سه فایل ببر جلو
    * bsf: به تعداد عددی که وارد میشود برو عقب یعنی bsf3 یعنی اشاره‌گر را سه فایل ببر عقب
    * erase: پاک کردن کل نوار
    * tell: بگو اشاره‌گر کجاست
    * eof: یعنی End Of current Data یعنی اگر اشاره‌گر وسط یک فایل بود اشاره‌گر را به انتهای آن اشاره‌گر ببر
    * rewind: اشاره‌گر را به اول منتقل کن
    * eject: بیرون بردن دیوایس
    * offline: آفلاین کردن دیوایس

```shell
ls /dev/st* #show device
ls /dev/nst* #show device
mt -f /dev/st0 <opration>
```

سناریوی زیر را مشاهده نمایید

```shell
mt -f /dev/st0 load
mt -f /dev/st0 erase
mt -f /dev/st0 rewind
tar cf /dev/st0 <DirectoryOfData> #شروع به گرفتن بک‌آپ کرده و در فایل اول نوار وارد میکند و اشاره‌گر میرود به انتهای فایل اول
sleep <یک ماه>
mt -f /dev/st0 rewind # برور به اول نوار
mt -f /dev/st0 fsf1 #یک فایل برو جلو
tar xf /dev/st0 /home/restorMyData #بازیابی بک‌آپ از نوار

```

<div style="display: flex; flex-direction: column; align-items: center;">

![performbasicfile-archcompress1.jpg](_srcFiles/Images/performbasicfile-archcompress1.jpg "performbasicfile-archcompress1.jpg")
![performbasicfile-compratio2.jpg](_srcFiles/Images/performbasicfile-compratio2.jpg "performbasicfile-compratio2.jpg")
![performbasicfile-over2.jpg](_srcFiles/Images/performbasicfile-over2.jpg "performbasicfile-over2.jpg")
![performbasicfile-targzipbzip2_.jpg](_srcFiles/Images/performbasicfile-targzipbzip2_.jpg "performbasicfile-targzipbzip2_.jpg")

</div>

# 7. 🅰️ExtensionType OR FileType

* [*.so]: فایل‌های کتابخانه‌ای داینامیک در لینوکس
    * فایل‌های SharedObject در لینوکس dynamic library می‌باشند که معادل DLL در ویندوز هستند
    * فایل تجمیع‌شده از چندین «آبجکت‌کد» «کامپایل شده» باهم برای ایجاد فایل Library جهت انتقال و استفاده در محل دیگر
    * فایل .so یک کتابخانه داینامیک (dynamic library)  است که شامل توابع قابل اجرا هست که برنامه‌ها می‌تونن به صورت پویا (در زمان اجرا) ازشون استفاده کنن.
    * معمولا در مسیرهای `/usr/lib/` یا `/usr/local/lib/` یا `/lib/` قرار دارند
    * استفاده مشترک توابع بین برنامه‌ها
* [*.DLL]:  فایل‌های کتابخانه‌ای داینامیک در ویندوز
    * عبارت DLL مخفف Dynamic Link Library مب‌باشد
    * معادل *.so در لینوکس است
    * استفاده مشترک توابع بین برنامه‌ها

</div>

# 8. 🅰️ FileNames

## 8.1. 🅱️ Named Pipe

فایل با پسوند p در لینوکس، یک فایل توخالی و بدون حجم روی دیسک است که صرفاً به عنوان یک پل ارتباطی (لوله) بین دو برنامه عمل می‌کند. این فایل به شما اجازه می‌دهد داده‌ها را به صورت زنده، بدون اشغال فضای هارد دیسک و بین برنامه‌هایی که هیچ ارتباطی با هم ندارند، جابه‌جا کنید.

* تفاوت فایل معمولی و پایت
    *     فایل معمولی (Regular File - با حرف - شروع می‌شود): مثل یک سطل یا انبار است. داده‌ها را روی هارد دیسک ذخیره می‌کند، حجم دارد و هر زمان بخواهید می‌توانید آن را باز کرده و بخوانید.
    * پایپ معمولی (Anonymous Pipe - همان علامت | در ترمینال): مثل یک لوله آب موقت است که فقط وقتی دو دستور را در یک خط به هم وصل می‌کنید (مثلاً cat file | grep text) در حافظه RAM ایجاد می‌شود و به محض تمام شدن دستور، از بین می‌رود. نام و مسیری در فایل‌سیستم ندارد.
    * پایپ نام‌دار (Named Pipe - با حرف p شروع می‌شود): مثل یک لوله آب ثابت و لوله‌کشی شده در ساختمان است. این فایل داده‌ای را روی هارد دیسک ذخیره نمی‌کند (به همین دلیل در ls -l حجم آن 0 بایت است). این فایل فقط یک "مسیر" یا "نقطه اتصال" در فایل‌سیستم است که دو برنامه کاملاً مجزا و مستقل می‌توانند از طریق آن با هم ارتباط برقرار کنند.
* ویژگی‌های کلیدی Named Pipe:
    * عدم ذخیره‌سازی داده: داده‌ها فقط از درون آن "عبور" می‌کنند. اگر برنامه‌ای داده‌ای را به آن بنویسد، داده بلافاصله باید توسط برنامه خواننده خوانده شود، وگرنه در حافظه بافر می‌شود (که حجم بسیار کمی دارد).
    * رفتار مسدودکننده (Blocking Behavior): این مهم‌ترین ویژگی است.
        * اگر برنامه‌ای بخواهد در لوله بنویسد، اما برنامه‌ای برای خواندن از آن باز نباشد، برنامه نویسنده متوقف (Freeze/Block) می‌شود و منتظر می‌ماند تا کسی لوله را باز کند.
        * برعکس، اگر برنامه‌ای بخواهد از لوله بخواند، اما کسی داده‌ای به آن نفرستاده باشد، برنامه خواننده متوقف می‌شود تا داده برسد.
    * قانون FIFO: داده‌ها دقیقاً به همان ترتیبی که وارد لوله شده‌اند، از آن خارج می‌شوند.
* کاربردها
    * ارتباط بین پردازش‌های کاملاً مجزا (IPC): فرض کنید دو اسکریپت یا برنامه کاملاً مستقل دارید (مثلاً یکی با پایتون نوشته شده و دیگری با Bash) و می‌خواهید به صورت زنده با هم داده رد و بدل کنند. شما یک Named Pipe می‌سازید. اسکریپت A داده‌ها را در آن می‌نویسد و اسکریپت B آن را می‌خواند. چون این فایل در فایل‌سیستم وجود دارد، هر دو برنامه می‌توانند با
      استفاده از مسیر آن (مثلاً /tmp/my_pipe) به آن دسترسی پیدا کنند.
    * دور زدن محدودیت برنامه‌ها (مثل مثال lnav):بسیاری از برنامه‌های قدیمی یا خاص، فقط می‌توانند فایل را به عنوان ورودی بخوانند و نمی‌توانند ورودی را از Standard Input (stdin) یا پایپ (|) دریافت کنند. با ساختن یک Named Pipe، شما یک "فایل" جعلی ایجاد می‌کنید. برنامه فکر می‌کند دارد یک فایل معمولی را می‌خواند، اما در باطن، یک برنامه دیگر در حال ریختن
      داده‌های زنده (Stream) داخل آن است.
    * انتقال و ایمپورت دیتابیس‌های حجیم: وقتی می‌خواهید یک دیتابیس چند ده گیگابایتی را از سرور A به سرور B منتقل کنید، اگر از فایل معمولی استفاده کنید، باید ابتدا یک فایل ۵۰ گیگابایتی روی دیسک بسازید (که هم زمان‌بر است و هم فضای دیسک را پر می‌کند). با استفاده از Named Pipe (یا پایپ معمولی در شبکه)، خروجی mysqldump یا pg_dump مستقیماً مثل آب در لوله
      به سرور مقصد هدایت شده و همان لحظه در دیتابیس مقصد ایمپورت می‌شود. هیچ فایل موقتی روی دیسک ساخته نمی‌شود.
    * تست و شبیه‌سازی ورودی‌های شبکه یا دستگاه‌ها:توسعه‌دهندگانی که روی برنامه‌هایی کار می‌کنند که قرار است از روی یک پورت شبکه، یک فایل لاگ زنده، یا یک دستگاه سخت‌افزاری (مثل اسکنر یا سنسور) داده بخوانند، می‌توانند یک Named Pipe بسازند. آن‌ها می‌توانند داده‌های از پیش ضبط شده را داخل این لوله بریزند تا برنامه‌شان فکر کند در حال دریافت داده زنده از
      یک منبع خارجی است.
    * ه) ایجاد تانل‌های شبکه و پروکسی‌های ساده:در ترکیب با ابزارهایی مثل socat یا netcat، از Named Pipeها برای ساخت تانل‌های امنیتی، پورت فورواردینگ‌های پیچیده SSH، یا ایجاد پروکسی‌های سبک برای عبور دادن ترافیک شبکه استفاده می‌شود.
* رعایت ملاحظات زیر در حین استفاده از این نوع فایل‌ها
    * حتماً آن‌ها را پاک کنید: چون این فایل‌ها در فایل‌سیستم (مثلاً /tmp) ساخته می‌شوند، بعد از اتمام کار باید با دستور rm /tmp/live_journal آن‌ها را پاک کنید. اگر سیستم ریستارت شود معمولاً /tmp پاک می‌شود، اما در سرورهای آپتایم بالا، فایل‌های اضافی باقی می‌مانند.
    * مراقب قفل شدن (Hang) ترمینال باشید: به دلیل همان "رفتار مسدودکننده"، اگر شما در ترمینال دستور cat /tmp/my_pipe را بزنید، ترمینال قفل می‌شود و منتظر می‌ماند. اگر فراموش کنید که یک برنامه دیگر باید داده را به آن بفرستد، ترمینال شما برای همیشه فریز می‌شود! (برای خروج از این حالت Ctrl+C را بزنید).
    * معمولاً یک‌بار مصرف هستند: در بسیاری از پیاده‌سازی‌ها، به محض اینکه برنامه نویسنده فایل را ببندد، برنامه خواننده نیز به محض خواندن آخرین داده، فایل را می‌بندد (EOF دریافت می‌کند). برای استفاده مداوم و زنده (مثل مثال journalctl -f)، باید از ابزارهایی استفاده کنید که مدام فایل را باز نگه می‌دارند یا ساختار حلقه (Loop) بسازید.

## 8.2. 📁️ /sbin/init

* اولین برنامه ایکه برای اجرای دیگر پردازه‌ها به اجرا درمی‌آید
* اول می‌رود سراغ /sbin/init اگرنبود می‌رود سراغ /etc/init و اگر نبود میرود سراغ /bin/sh
* سه برنامه برای initiate کردن پردزه ‌ها وجود دارد:۱-sysV که سیستم۵ هم نامیده می‌شود ۲-systemdجدید است۳-upstart برای اوبونتو بود که استفبال نشد

## 8.3. 📁️ /proc

تمام محتویات مسیر آن توسط کرنل[kernel] پر می‌شود

* /proc/cmdline: Arguments passed to the Linux kernel at boot time
    * OOT_IMAGE=/boot/vmlinuz-5.10.0-20-amd64 root=UUID=4bfb45d2-d701-44c7-8941-9d52d2f6f227 ro quiet
* /proc/net/dev: All about Network
    * cat /proc/net/dev | column -t
* /proc/cpuinfo
* /proc/filesystems: A text listing of the filesystems which are supported by the kernel
* /proc/meminfo
* /proc/modules: A text list of the modules that have been loaded by the system
* /proc/mounts: list of all the filesystems currently mounted on the system
* /proc/net/arp: This holds an ASCII readable dump of the kernel ARP table
* /proc/swaps: Swap areas in use
* /proc/sys/kernel/hostname]
* /proc/sys/kernel/pty/nr: This read-only file indicates how many pseudoterminals are currently in use #نمایش تعداد ترمینال‌های باز
* /proc/sys/kernel/pid_max: ماکزیمم تعداد پردازه قابل استفاده در لینوکس توسط این فایل معین شده است که نباید از آن فراتر رود
* /proc/interrupts: show interrupt request on system
* /proc/version]
* /proc/<PID>/fd
    * ls -la /proc/<PID>/fd #لیست فایل‌های باز یک پردازه
    * ls -l /proc/<PID>/fd | wc -l
* /proc/<PID>/limits: مشاهده محدودیت‌های یک پردازه
* /proc/sys/fs/file-max: # مشاهده محدودیت مجموع فایل‌های باز در سیستم یعنی حداکثر تعداد فایل‌هایی است که می‌توانند به طور همزمان در سیستم باز باشند

# 9. 🅰️Command

## 9.1. 🅱️ fio

```shell
fio --name=Rand_RW_100_8K --rw=randrw --direct=1 --rwmixwrite=100  --ioengine=windowsaio --time_based  --runtime=1800  --size=30tib --blocksize=8k  --numjobs=8 --filesize=4tib --thread --group_reporting --filename="\\.\PhysicalDrive2"  --output="c:\1403-08-29-TestRand100Write-T2.txt"
```

## 9.2. 🅱️ tree

نمایش فایل‌های بصورت درختی

```shell
tree -fi #نمایش تنها لیست فایل‌ها بصورت نام کامل
```

## 9.3. 🅱️ ulimit

get and set user limits

```shell
ulimit --help
ulimit -n #مشاهده محدودیت تعداد فایل‌های باز برای هر پردازه
ulimit -n <new_limit> #Temprory #the maximum number of open file
vim /etc/security/limits.conf # اگر بخواهیم بصورت دائمی باشد
```

# 10. 🅰️ Hash

* هش همواره یک طرفه است و مانند کدینگ نیست که امکان دیکد داشته باشد

```shell
echo -n <STRING>|md5sum # linux
certutil -hashfile <file> MD5 # MicrosoftWindows
# 6. [Server1: find ./backup -type f -print0 | xargs -0 md5sum > /checksums_backup.md5] && [Server2: md5sum -c checksums_backup.md5] → checksum
```

## 10.1. 🅱️

## 10.2. 🅱️

## 10.3. 🅱️