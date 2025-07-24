# 🅰️ Cloud

<div dir="rtl">

* دو پروژه openstack و vcloud(که opensource نیست و لایسنس آن خیلی گرون است) در زمینه کلود کار می‌کنند
* openstack حدودا 70 گیگ اطلاعات دانلود میکند و میشود در یک شبکه مجازی vmware داخلی بالا آورد
* openstack می‌تواند cpu یا Hard یا GPU یا هر چیز دیگر را به تعداد زیاد فراهم کند و EndUser اصلا نمی‌فهمد که این موارد در یک سیستم نیستند
* در بستر اینترنت شرکت یا سایت digitalOcean و AWS که مخفف Amazon Web Services است ماشین مجازی ارائه می‌دهند
* در digitalOcean به ماشین مجازی droplet می‌گویند که حاوی رم و سی پی یو و جزییات دیگر است که هنگام ساخته شدن باید تعریف شود
* برای ارتباط گرفتن با شرکت های ارائه دهنده خدمات کلود(مثلا ماشین مجازی) توسط کامندلاین باید در چهار چوب API ارائه شده توسط این سایت‌ها اقدام نماییم و برای ارتباط حتما باید token ایجاد نماییم و توسط آن توکن دستورات را به شرکت میزبان ارائه دهنده ماشین مجازی کلود بدهیم(معمولا در منوی API دنبال ایجاد توکن ساختن بگردید)
* توسط دستور docker-machine می‌توان یک ماشین مجازی توسط کامند لاین در سایت دیجیتال اوشن ساخت که به اصطلاح می‌گویند ماشین مجازی provision می‌کنیم

# 🅰️ ESX

* نصب بسته sudo apt install open-vm-tools سبب نصب وی ام ویر تولز می‌شود

## 🅱️ [OVFTools](https://techtik.com/2022/07/02/ovf-tools/)

* OVFTools #برنامه ویندوزی برای خروجی گرفتن از ماشین‌های مجازی موجود در سرور ای‌اس‌ایکس استفاده می‌شود
    * Dwonload [OVFTools](http://ftp.tucha13.net/pub/software/VMware-ovftool-4.1.0/)

</div>

1. cd
    * [Windows] cd C:\Program Files\VMware\VMware OVF Tool #
    * [Linux] [URL3](https://mikebosland.com/installing-ovftool/)
        * `sudo ./VMware-ovftool-4.4.1-16812187-lin.x86_64.bundle --extract ovftool` and `cd ovftool`
3. `list s`
    * [Windows]: ovftools vi://192.168.10.90
    * [Linux]: vmware-ovftool/ovftool vi://192.168.10.90
4. Create OVF
    * [Windows]: ovftools vi://192.168.10.90/Gitlab-Group C:\Users\alika\Desktop\ovf
    * [Linux]: vmware-ovftool/ovftool vi://192.168.10.90/Gitlab-Group /tmp/ovf
5. `ovftool vi://192.168.1.38/WinSRV2020-2`

# 🅰️ KVM

* UIApp: ProxMox
* vms extention: *.QEMO
* در ایران معمولا کامند لاین استفاده می‌شود و پروکس‌موکس استفاده نمی‌شود



