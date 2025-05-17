# Switchs

* if: Input File
    * if=IMAGE.img
* of: Output File
    * of=/dev/sdc
* bs: BlockSize تعداد بایت هایی است که در یک زمان خوانده یا نوشته می شود
    * مطمین شین که اندازه بلوک مضربی از ۱۰۲۴ که برابر با ۱ کیلوبایت است استفاده شود.
    * bs=1M
    * bs=1K
* status:
    * progress:‌اطلاع از میزان پیشرفت
* conv:روش تبدیل فایل ورودی و نوشتن روی دیسک مقصد چگونه است
    * noerror: کپی کردن داده ها در صورت برخورد به هر گونه خطا ادامه یابد
    * sync: استفاده از همگام‌سازی بین ورودی و خروجی
    * fdatasync:‌ بافر به درستی پاکسازی و مجدداً نوشته شود و خطایی رخ ندهد
    * ucase: تبدیل به حروف بزرگ
        * dd if=~/file1 of=~/file2 conv=ucase # برای تبدیل کل محتویات فایل به حروف بزرگ
    * lcase: تبدیل به حروف کوچک
        * dd if=~/file1 of=~/file2 conv=lcase # برای تبدیل کل محتویات فایل به حروف کوچک
    * ascii: تبدیل فایلی ازهر فرمت به فرمت اسکی
        * dd if=textfile.ebcdic of=textfile.ascii conv=ascii
    * ebcdic: تبدیل فایل از هر فرمت به فرمت «اِب‌دیک» که بیشتر از «مِین‌فِرِیم»ها بازیابی می‌شود\
        * dd if=textfile.ascii of=textfile.ebcdic conv=ebcdic
* count: تعداد انجام عملیات

# Examples

* dd if=/dev/sda1 of=/dev/sdb1 bs=4096 conv=noerror,sync
    * Note: برای کپی یک پارتیشن رو یک پارتیشن دیگر از دستور زیر استفاده می کنیم
* dd if=/dev/cdrom of=/mycd.iso
* dd if=/dev/sda of=/tmp/sdaMBR.img bs=512 count=1 #MBR size is 512 byte
* dd if=debian.iso of=/dev/sda bs=4M conv=fdatasync status=progress # ساخت یک فلش با قابلیت بوت
* dd if=/dev/da0 conv=sync,noerror bs=128K | gzip -c | ssh behrooz@server1 dd of=centos-core-7.gz # نبودن فضا کافی و ذخیره در ریموت