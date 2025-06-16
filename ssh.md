<div dir="rtl">

# 1.concepts

* نرم افزار termius نرم افزار ssh و scp و sftp و tunnel است که هم نسخه موبایلی و هم نسخه لینوکسی دارد و تخصصی در بحث اس اس اچ کار کرده است
*

# 2.files

* **sshd_config**:  فایل تنظیماتی سرویس اس اس اچ سرور(یعنی سرویس اس اس اچ سرور چه تنظماتی داشته باشد)
* **ssh_config**:  فایل تنظیماتی کلاینتی اس اس اچ(یعنی در هنگام اس اس اچ به سرورهای متفاوت چه تنظیماتی داشته باشد)
* **~/.ssh/known_hosts**: Contains a list of host keys for all hosts the user has logged into that are not already in the systemwide list of known host keys(fingerprint).
* **~/.ssh/authorized_keys**: اگر کلید عمومی کسی رو در این فایل قرار بدهیم دیگر از او پسورد نمی‌گیرد و مستقیما لاگین می‌نماید

# Options

* **PubkeyAuthentication**: آیا احراز هویت با استفاده از کلید عمومی (Public Key Authentication) مجاز است یا خیر
    * yes: احراز هویت با کلید عمومی مجاز و سرور به کلیدهای عمومی کلاینت‌ها توجه می‌کند
    * no: احراز هویت با کلید عمومی غیرفعال می‌شود و کلاینت‌ها نمی‌توانند از روش احراز هویت با استفاده از کلید عمومی برای احراز هویت استفاده کنند
* **ClientAliveCountMax**: تعیین حداکثر تعداد پیام‌های alive با قابلیت بدون پاسخ ماندن از کلاینت و در غیر اینصورت قطع اتصال
* **ClientAliveInterval**(برحسب ثانیه): تعیین مقدار زمان ارسال پیامalive به کلاینت و اگر کلاینت به این پیام‌ها پاسخ ندهد و زمان تعریف شده (که باClientAliveCountMaxتعیین می‌شود) بگذرد، سرور اتصال را قطع می‌کند
    * اگر ClientAliveIntervalبرابر60ثانیه وClientAliveCountMaxبرابر3باشد،سرور هر۶۰ثانیه یک بار پیام "alive" ارسال می‌کند و اگر کلاینت به 3 پیام متوالی پاسخ ندهد، سرور اتصال را قطع خواهد کرد
* **ListenAddress**: اگر چند کارت شبکه داشته باشیم با این مولفه تعیین می‌کنیم که از کدام آی پی (تنظیم شده روی کارت شبکه) اس اس اچ پذیفته شود
* **PasswordAuthentication**: authentication with text password
* **AllowUsers**: کاربران مجاز برای لاگین
* **DenyUsers**: کاربران غیر مجاز برای لاگین
* **AllowGroups**: گروه‌های مجاز لاگین
* **DenyGroups**: گروه‌های غیر غیر مجاز برای لاگین
* **PermitRootLogin**: آیا یوزر روت بتواند لاگین نماید یا خیر
* **X11Forwarding**: آیا رابط کاربری بتواند فوروارد شود
* **AllowTcpForwarding**: سرور بتواند پروتکل‌های تونل را بپذیرد
* **LoginGraceTime**: تعیین مدت زمان برای لاگین و احراز هویت یک کاربر به سیستم
    * defaults:2min
    * recommended:30s or 1m

</div>
