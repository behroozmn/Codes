<div dir="rtl">

# Concepts

* فایل: مجموعه‌ای از سری داده که به‌صورت یک واحد ذخیره‌سازی(در حافظه اصلی یا جانبی یا حافظه موقت) شوند
*

```shell
rename "s/jpeg$/jpg/" *.jpeg   تبدیل همه جی پگ ها به چی پی جی
```

# Backup

* برای بک‌آپ گرفتن مهم است که دیتای خود را دسته‌بندی کرده باشید
* انواع بک‌آپ گیری
    * fullBackup: همه دیتارا بکاپ می‌گیرد
    * Incremental: نسبت به fullBackupآخری هر جی اضافه دارد را بک‌آپ می‌گیرد
    * Differential: نسبت به یک نسخه خاص هرچی تفاوت دارد را بک‌آپ می‌گیرد
    * snapshot: همانند differential است

## Apps

* backula یک برنامه فوق‌العاده قوی برای بک آپ از هر چیزی است که هم کامند و هم دسکتاپ و هم وب ارائه داده است

```shell
cp /Path/FileName{,.Backup} #CreateBackup
```

---

### rsync

سوییج‌های دستور آرسینک

* a : تکراری کپی نشود و فقط جدید کپی شود
* h: خوانا برای انسان
* v: توضیحات زیاد داده شود

```shell
cp /Path/FileName{,.Backup} #CreateBackup
rsync -avh /home/behrooz/dire /tmp
rsync -avh /home/behrooz/dire behrooz@192.168.10.88:/home/SecondCopy
```

## Archive and Compressing

```shell
tar -czvf Directory.tar.gz Directory --remove-files
tar tf File.tar.gz #فقط نمایش محتویات
tar j #bzip2
tar Uf File.tar Dir #آپدیت کن از فایل‌های جدید

```

# Tape

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





# ExtensionType OR FileType

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