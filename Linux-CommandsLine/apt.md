# apt

* apt install PackageName
* apt install --fix-broken
* apt remove PackageName
* apt purge PackageName
* apt show PackageName
* apt list PackageName
* apt search PackageName


## #xample

* sudo apt download $(sudo apt-cache depends php7.0 | awk '{print$2}'|grep -v ">"|grep -v "<") # DownloadAllDependency
* apt --option Acquire::HTTP::Proxy="socks5h://127.0.0.1:9150" update

# apt-get

* apt-get install PackageName #نصب بسته
* apt-get install PackageName --print-urls #نمایش آدرس دانلود بسته‌ها
  * بجای نصب فقط آدرس «یوآرال» نمایش خواهد داد
* apt-get update #بروزرسانی لیست همه بسته‌های موجود در مخازن
* apt-get upgrade #آپگرید همه بسته‌ّای نصب شده به نسخه جدیدتر
* apt-get remove PackageName #حذف یک بسته با پسوند دب از روی سیستم توسط ابزار اَپْت
* apt-get check # بررسی وضعیت پیش‌نیاز‌ها یا همان دیپندنسی
* apt-get clean #پاک کردن کش که شامل بسته‌های پسوند دب دانلود شده است
* apt-get clean all #

## Example

* sudo apt-get download php && apt-cache depends -i php |awk '/Depends:/ {print $2}' | xargs apt-get download  # DownloadAllDependency

# apt-cache

* apt-cache search PackageName #جستجوی بسته موردنظر

# ap-cdrom

ap-cdrom install PackageName #نصب یا آپگرید یک بسته باپسوند دب از روی سی‌دی‌رام



# LocalRepository



1. download  DVD From Debian website
2. sudo vim /etc/apt/sources.list
3. mount file to specific directory with next line command:
   1. [temporary]:sudo mount -o loop /home/behrooz/App/DVD/debian-9.3.0-amd64-DVD-1.iso /media/repo_1
   2. [Permanently]:
      1. sudo vim /etc/fstab
      2. edit: /home/behrooz/App/DVD/debian-9.3.0-amd64-DVD-1.iso    /media/repo_1  iso9660   defaults   0    0
4. sudo vim /etc/apt/sources.list
5. add:  deb [trusted=yes] file:///media/repo_1 stretch main contrib
6. sudo mount -a
7. lsblk