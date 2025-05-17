# 1.Concepts

* در سیستم‌عامل لینوکس مبحث udev عاملی برای مدیریت سیستم و دستگاه است که به طور خودکار دستگاه‌های متصل به سیستم را شناسایی و پیکربندی می‌کند.
* در سیستم‌عامل‌های لینوکسی دستور udevadm برای فعال‌سازی مجدد رویدادهای udev استفاده می‌شود
* دستور [udevadm trigger]: ارسال فرمان به «udev» جهت ایجاد رویدادهای جدید برای دستگاه‌های متصل
    * به گونه‌ای که قوانین و اسکریپت‌های مربوط به دستگاه‌ها(شامل بارگذاری ماژول‌های هسته، تنظیم مجدد مجوزها، یا اجرای اسکریپت‌های خاص) دوباره اجرا شوند
    * حاصل نمودن اطمینان از صحت إعمال تغییرات در پیکربندی دستگاه‌ها یا قوانین udev
    * تغیین کلاس خاصی از دیوایس‌ها(مثلا فقط بلاک‌ها و غیره) که بخواهیم تحت تأثیر قرار بگیرند با سوییچ subsystem-match

# 2.Switch

## trigger

udevadm **trigger** [options] [devpath(such as /dev/sda)|file|unit]

**options**

* [--action=]:
    * add
    * remove
    * change
    * move
    * online
    * offline
    * bind
    * unbind
* [--subsystem-match=]
    * block: برای دستگاه‌های بلاک (مانند دیسک‌های سخت و SSDها)
        * net: برای دستگاه‌های شبکه (مانند کارت‌های شبکه)
            * udevadm trigger --subsystem-match=net #فعالسازی مجدد رویدادها برای دستگاه‌های شبکه
    * usb: برای دستگاه‌های USB
    * pci: برای دستگاه‌های PCI
    * tty: برای دستگاه‌های ترمینال (مانند tty و pty)
    * input: برای دستگاه‌های ورودی (مانند کیبورد و ماوس)
    * sound: برای دستگاه‌های صوتی
    * video: برای دستگاه‌های ویدیویی (مانند دوربین‌ها)
    * char: برای دستگاه‌های کاراکتری (مانند دستگاه‌های سریال)
    * firmware: دستگاه‌های مربوط به فریمور
    * backlight: دستگاه‌های نور پس‌زمینه (مانند صفحه‌نمایش)
    * dmi: اطلاعات DMI (دستگاه‌های سخت‌افزاری)
    * gpu: دستگاه‌های گرافیکی
    * scsi: دستگاه‌های SCSI
    * md: دستگاه‌های RAID (مدیریت دیسک)
        * برای مشاهده لیست کامل(البته وابسته به توزیع لینوکس و سخت‌افزار) از دستور زیر استفاده نمایید
            * ls /sys/class/

# 3.info

Query the udev database for device information

udevadm **info** [options] [devpath(such as /dev/sda)|file|unit]

* [-t] or [--tree]: نمایش در ساختار درختی
* [-c] or [--cleanup-db]: Cleanup the udev database
    * sudo udevadm info --cleanup-db /dev/sdb
    * توصیه‌می‌شوددر ادامه دستور زیر را بزنید
    * sudo udevadm trigger /dev/sdb

# 4.Examples

* `udevadm trigger  --subsystem-match=block --action=add $disk`
* `sudo udevadm info /dev/sda`
* ```shell
  for disk in /dev/sda /dev/sdb; do
  udevadm trigger  --subsystem-match=block --action=add $disk 
  done
  ```
* `sudo udevadm info /dev/sdb`



