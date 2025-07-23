# 📍️ Concepts

* Nice
    * هر پروسس دارای مولفه Nice است که هر چه این عدد کوچک‌تر باشد یعنی این پروسس اولویت بالاتری دارد.
    * بصورت پیش فرض اولویت بسیاری از سرویس ها صفر است
    * محدوده آن از منفی ۲۰ تا عدد ۱۹ می‌باشد برای تغییر اولویت سرویس‌ها و پردازه‌ها
    * اگر یک سرویس در حال اجرا باشد و بخواهید اولویت آنرا در همان حال تغییر و اعمال نمایید باید از دستور renice استفاده نمایید.
    * کرنل هیچ وقت نمی تواند میزان NI را تغییر دهد. کرنل برای بالاتر بردن اولویت ستون PR را در دستور top تغییر می‌دهد
* Zombie process:
    * وقتی در اصطلاح یک process در لینوکس می میرد، فورا از حافظه رَم پاک نمی شود و یک descriptor از آن باقی می ماند که مقدار بسیار کمی از حافظه را به خود اختصاص می دهد. سپس آن پروسه در حالت EXIT-ZOMBIE قرار گرفته و از طریق یک سیگنال SIGCHLD به پروسه parent خود اطلاع می دهد که مرده است. در نهایت پروسه parent یک wait() system call اجرا می کند تا از
      طریق آن وضعیت آن پروسه و سایر اطلاعاتش را بخواند. با پایان این مرحله آن پروسه کاملا از بین می رود. این مراحل معمولا به سرعت انجام می شود و شما وضعیت zombie را برای آن نخواهید دید. اما اگر پروسه parent درست برنامه نویسی نشده باشد و wait() call را اجرا نکند، آن پروسه در وضعیت zombie باقی می ماند. حال یا باید بصورت دستی SIGCHLD را با دستور kill
      -s SIGCHLD pid اجرا کنید و بجای pid، شماره پروسه مادر را وارد کنید تا مجدد پروسه مادر wait() call را صادر کند اما اگر باز اینکار را نکند مجبور خواهید بود با استفاده از سیگنال SIGKILL پروسه مادر را از بین ببرید. در این حالت پروسه init که PID شماره ۱ را دارد، به عنوان parent پروسه child معرفی می شود و این پروسه نیز بصورت دوره ای wait() call را
      صادر می کند که در نتیجه، پروسه های زامبی در نهایت کُشته می شوند. البته عموما زامبی ها مشکلی ایجاد نمی کنند و حتی نمی توان از آنها به عنوان پروسه نام برد. برای همین هم نمی توان به روش های رایج آنها را kill کرد. زامبی ها هیچ فضایی از پردازشگر نمی گیرند. تنها مشکلی که ایجاد می کنند اینست که یک PID به خود اختصاص می دهند و اگر تعداد آنها زیاد شود،
      بصورتی که شماره ای برای پروسه های جدید باقی نماند، دچار مشکل خواهیم شد.
* ماکزیمم تعداد پردازه قابل استفاده در لینوکس توسط فایل /proc/sys/kernel/pid_max معین شده است که نباید از آن فراتر رود

# 📍️ SIGNALs

* SIGNALS:SIGTERM: Sent to a process to request its termination.(Signal Terminate)
    * Code: 15 # به برنامه ها فرصت اجرای کد هنگام خروج را میدهد
    * When the system is shutdown or rebooted
    * `kill -s SIGTERM <pid>`
* SIGINT: when a user wishes to interrupt the process, Sent to a process for its controlling terminal(Signal interrupt)
    * SIGINT=Ctrl+c
    * `kill -s SIGINT <pid>`
* SIGHUP: (Signal hangup)
    * `kill -s SIGHUP <pid>` عمل «ریلود» نمودن یک سرویس
* SIGKILL:
    * Code: 9 #سرویس را مجبور می کنید که بلافاصله و بدون اجرای آن کدها، خروج کند
    * `kill -s SIGKILL <pid>`
    * به برنامه‌ها فرصت اجرای کد هنگام خروج داده نمی‌شود و به زور پردازه‌ها ناگهانی تمام می‌شوند
* SIGCHLD
    * `kill -s SIGCHLD pid` #pid: parentProcess of Zombie process
    * بررسی مجدد پردازه و درصورت لزوم بستن کامل پروسه

# 📍️ Commands

## ✅️ fuser

```shell
fuser #پروسس‌هایی که دارد از یک فایل استفاده میکنند

```

## ✅️ gnome-system-monitor

```shell
gnome-system-monitor
```

## ✅️ htop

## ✅️ iostat

## ✅️ kill

بصورت پیش فرض اگر هیچ سیگنالی نزنید از سیگنال ۱۵ استفاده می نماید

## ✅️ lscpu

## ✅️ mpstat

* [-P]: custome cpu(Default:all)#خالی باشد همه را همه سی‌پی‌یو‌ها را مد نظر قرار میدهد

```shell
apt install sysstat
mpstat -p 0 
```

## ✅️ nice

```shell
nice -n 5 tar -czf backup.tar.gz /root/*
nice -n 10 apt-get upgrade

```

## ✅️ pgrep

## ✅️ pidof

## ✅️ pkill

بستن تمام برنامه‌هایی که نام وارد شده در آن وجود دارد

```shell
pkill -9 apache
```

## ✅️ process status [ps](https://parsdev.com/blog/linux-ps-aux-command)

```shell
ps axu  #every process on the system using BSD syntax 
ps ax   #every process on the system using BSD syntax
[ps -ejH] or [ps axjf] #To print a process tree
```

## ✅️ renice

```shell
renice -10 -p 22678
```

## ✅️ top

* [-u] → User Process
    * `sudo top -u <user>`
* [-c] → Show Full Path of process
    * `sudo top -c`
* [-n] → counter of result
    * `sudo top -n 10`
* Shortcuts
    * [Shift+P] در برنامه top: مرتب‌سازی برحسب درصد پردازش
    * [Shift+u]: تعیین کردن این که کدام نام کاربری را رصد نماییم
* [توضیحات ستون‌های دستور]
    * State: این ستون وضعیت پردازه‌ها را نمایش می‌دهد
        * [Z](Zombie):Cannot kill 2-it is an entry and not process
        * [D]:1-Cannot kill 2-show «uninterruptible sleep» process such as IO on disk
    * [NI]: Priority of nice(Note: kernel cannot change NI Priority)
    * [PR]: Real priority(PR = 20 + NI)
        * User cannot change PR Priority
        * kernel can temprory change PR Priority
        * کرنل در حالت فوق می‌تواند این اولویت را تغییر دهد
            * کاهش اولویت: استفاده بلند مدت از «سی‌پی‌یو» توسط یک پروسه
            * افزایش اولیت:پروسه در طولانی مدت از «سی‌پی‌یو» استفاده نکرده باشد


## ✅️ global


```shell
systemctl status smb | grep PID
ss -utlpn | grep <PIDnumber>
```


# 📍️ Files

## 📁️ /proc/cpuinfo