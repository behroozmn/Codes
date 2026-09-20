# 🅰️ Application and Shortcuts

## 🅱️ General

* ShortcutGeneral(AllApps)
    * [Shift+F10]: در هر برنامه‌ای همانند راست کلیک عمل خواهد کرد
    * [Alt+F10]: Toggle windows Size
    * [Alt+F] : نمایش منوها
    * F6: change to sidebar


* BigBlueButton:سامانه ویدئوکنفرانس متن‌باز بابت انجام امور مجازی(راه اندازی شده در داتشگاه علامه طباطبایی)
* Moodle: آموزش از راه دور(حضورغیاب و کلاس بندی و مدیریت کلاسا) که علامه طباطبایی راه اندازی کرده(برای کلاس مجازی در
  دوران کرونا)(طرح مصباح حوزه مشکات پلائین)

## 🅱️ goldendict

* -no-bidi:سبب راست چین شدن نوشته در افزونه گنوم می‌شود
    * trans -b -s en -t fa -no-bidi -- LDWORD

## 🅱️ Eitaa

* رزولیشن و سایز استیکر در ایتا
    * ← سایز ۵۱۲ * ۵۱۲
    * ← رزولیشن ۷۲

```shell
#Google All-->Fa
trans -e google -t fa -show-original n -show-original-phonetics n -show-translation y -no-ansi -show-translation-phonetics n -show-prompt-message n -show-languages n -show-original-dictionary n -show-dictionary n -show-alternatives n "%GDWORD%" -no-bidi

# Google En-->Fa
trans -e google -s en -t fa -show-original n -show-original-phonetics n -show-translation y -no-ansi -show-translation-phonetics n -show-prompt-message n -show-languages n -show-original-dictionary n -show-dictionary n -show-alternatives n "%GDWORD%" -no-bidi

#Google Ar-->Fa
trans -e google -s ar -t fa -show-original n -show-original-phonetics n -show-translation y -no-ansi -show-translation-phonetics n -show-prompt-message n -show-languages n -show-original-dictionary n -show-dictionary n -show-alternatives n "%GDWORD%" -no-bidi
```

## 🅱️ Firefox

* Shortcut
    * [ctrl+sift+b]: Hide|Show BookmarksMenu
* about:about
    * about:config:[Accept]
        * webRTCL
            * url:media.peerconnection.enabled
            * toggle
                * false: Disable
                * True: enable
            * [url](https://browserleaks.com)
    * browser
        * browser.cache.disk.enable: فعال یا غیرفعال کردن کش دیسک
        * browser.link.open_newwindow: تنظیم رفتار باز کردن پنجره‌های جدید
        * browser.link.open_newwindow: تنظیم باز کردن پنجره‌های جدید (در همان پنجره، در تب جدید و ...)
        * browser.sessionstore.restore_on_demand: بارگذاری تب‌های غیرفعال در زمان راه‌اندازی
        * browser.startup.homepage: تنظیم صفحه اصلی مرورگر
        * browser.tabs.closeWindowWithLastTab: اجازه به بستن پنجره با آخرین تب
        * browser.tabs.loadInBackground: بارگذاری تب‌های جدید در پس‌زمینه
        * browser.tabs.warnOnClose: هشدار در مورد بستن تب‌ها
        * browser.urlbar.suggest.bookmark: پیشنهاد بوکمارک‌ها در نوار آدرس
        * browser.urlbar.suggest.history: پیشنهاد تاریخچه در نوار آدرس
    * dom
        * dom.allow_scripts_to_close_windows: اجازه به اسکریپت‌ها برای بستن پنجره‌ها
        * dom.disable_open_click_delay: تنظیم تأخیر در باز کردن پنجره‌های جدید
        * dom.disable_open_during_load: جلوگیری از باز شدن پنجره‌های جدید در حین بارگذاری
        * dom.disable_window_status_change: جلوگیری از تغییر وضعیت پنجره‌ها توسط اسکریپت‌ها
        * dom.event.contextmenu.enabled: فعال یا غیرفعال کردن منوی راست‌کلیک
        * dom.webnotifications.enabled: فعال یا غیرفعال کردن نوتیفیکیشن‌های وب
    * extensions
        * extensions.logging.enabled: فعال یا غیرفعال کردن لاگ‌گیری برای افزونه‌ها. اگر فعال باشد، اطلاعات بیشتری در
          مورد فعالیت‌های افزونه‌ها ثبت می‌شود
        *
        extensions.webextensions.restrictedDomains: [تنظیمات مربوط به دامنه‌های محدود برای افزونه‌ها] [لیستی از دامنه‌هایی که افزونه‌ها نمی‌توانند به آن‌ها دسترسی پیدا کنند][این تنظیم به امنیت افزونه‌ها کمک می‌کند]
        * extensions.webextensions.storage.enabled: فعال یا غیرفعال کردن ذخیره‌سازی محلی برای افزونه‌ها. اگر غیرفعال
          باشد، افزونه‌ها نمی‌توانند داده‌های محلی را ذخیره کنند
    * general
        * general.autoScroll: فعال یا غیرفعال کردن اسکرول خودکار. اگر فعال باشد، می‌توانید با کلیک و کشیدن ماوس، صفحه را
          به صورت خودکار اسکرول کنید
        * general.smoothScroll: فعال یا غیرفعال کردن اسکرول نرم. اگر فعال باشد، اسکرول به صورت نرم و پیوسته انجام می‌شود
        * general.useragent.override: تغییر User-Agent مرورگر. این تنظیم می‌تواند برای شبیه‌سازی مرورگرهای دیگر یا
          دستگاه‌های مختلف استفاده شود
        * general.warnOnAboutConfig: هشدار در مورد خطرات تغییر تنظیمات در about:config. اگر فعال باشد، هنگام ورود به این
          صفحه هشدار نمایش داده
    * layout
        * layout.css.devPixelsPerPx: تنظیم مقیاس DPI برای نمایش. می‌تواند برای بهبود وضوح متن و عناصر در صفحه استفاده
          شود
        * layout.css.grid.enabled: فعال یا غیرفعال کردن پشتیبانی از CSS Grid Layout. اگر غیرفعال باشد، مرورگر از این
          ویژگی پشتیبانی نخواهد کرد
        * layout.word_select.eat_space_to_next_word: تعیین می‌کند که آیا فضای خالی بین کلمات در هنگام انتخاب کلمات
          نادیده گرفته شود یا خیر
        * layout.word_select.eat_space_to_next_word: تنظیم رفتار انتخاب کلمات
    * media
        * media.autoplay.default: تنظیمات مربوط به پخش خودکار رسانه‌ها. مقادیر شامل "0" (اجازه به پخش خودکار)، "1" (
          سکوت) و "2" (غیرفعال) است
        * media.mediasource.enabled: فعال یا غیرفعال کردن Media Source Extensions (MSE) که به وب‌سایت‌ها اجازه می‌دهد
          رسانه‌ها را به صورت داینامیک بارگذاری کنند
        * media.mediasource.mp4.enabled: فعال یا غیرفعال کردن پشتیبانی از فرمت MP4 در Media Source Extensions
        * media.peerconnection.enabled: فعال یا غیرفعال کردن WebRTC، که برای ارتباطات صوتی و تصویری در مرورگر استفاده
          می‌شود
    * network
        * network.dns.disableIPv6: غیرفعال کردن IPv6 در DNS. اگر این تنظیم فعال باشد، مرورگر فقط از IPv4 استفاده خواهد
          کرد.
        * network.http.pipelining: فعال یا غیرفعال کردن HTTP Pipelinin
        * network.http.pipelining: فعال یا غیرفعال کردن HTTP Pipelining، که به مرورگر اجازه می‌دهد چندین درخواست HTTP را
          به طور همزمان ارسال کند و بهبود سرعت بارگذاری صفحات را فراهم کند
        * network.http.referer.default: تعیین می‌کند که چه مقداری به عنوان هدر Referer به وب‌سایت‌ها ارسال شود. مقادیر
          شامل "0" (همه اطلاعات)، "1" (فقط دامنه) و "2" (غیرفعال) است
        * network.http.referer.trimmingPolicy: سیاست برش هدر Referer را تعیین می‌کند. می‌تواند شامل برش دامنه یا مسیر
          باشد
        * network.http.referer.XOriginPolicy: تعیین می‌کند که آیا هدر Referer برای درخواست‌های بین‌دامنه ارسال شود یا
          خیر. این تنظیم می‌تواند به امنیت کمک کند و از افشای اطلاعات حساس جلوگیری کند
        * network.http.referer.XOriginPolicy: تنظیمات مربوط به ارسال Referer
        * network.proxy.type: تنظیمات مربوط به پروکسی
        * network.proxy.type: نوع پروکسی مورد استفاده را مشخص می‌کند. مقادیر شامل "0" (غیرفعال)، "1" (تنظیمات پروکسی
          دستی) و "2" (تنظیمات پروکسی خودکار) است
        * network.trr.mode: تنظیمات مربوط به DNS-over-HTTPS (DoH). مقادیر مختلفی دارد که می‌تواند شامل غیرفعال، فعال، یا
          استفاده از DNS-over-HTTPS به عنوان پیش‌فرض باشد
    * privacy
        * privacy.clearOnShutdown: پاک‌سازی داده‌ها (کش، تاریخچه و ...) هنگام خروج از مرورگر
        * privacy.donottrackheader.enabled: فعال یا غیرفعال کردن ارسال هدر "Do Not Track" به وب‌سایت‌ها
        * privacy.firstparty.isolate: فعال یا غیرفعال کردن ایزوله‌سازی اولین‌طرف برای جلوگیری از ردیابی
        * privacy.resistFingerprinting: فعال یا غیرفعال کردن مقاومت در برابر اثر انگشت‌زنی
        * privacy.trackingprotection.cryptomining.enabled: فعال یا غیرفعال کردن حفاظت در برابر استخراج ارز دیجیتال
        * privacy.trackingprotection.enabled: فعال یا غیرفعال کردن حفاظت از ردیابی
        * privacy.trackingprotection.pbmode.enabled: فعال یا غیرفعال کردن حفاظت از ردیابی در حالت خصوصی
        * privacy.trackingprotection.socialtracking.enabled: فعال یا غیرفعال کردن حفاظت در برابر ردیابی اجتماعی
    * security
        * security.csp.enable: فعال یا غیرفعال کردن Content Security Policy
        * security.default_personal_cert: تنظیم گواهی‌نامه شخصی پیش‌فرض
        * security.fileuri.strict_origin_policy: تنظیمات مربوط به سیاست‌های منبع برای فایل‌های محلی
        * security.mixed_content.block_active_content: جلوگیری از بارگذاری محتوای مختلط
        * security.mixed_content.block_active_content: جلوگیری از بارگذاری محتوای مختلط (HTTP در HTTPS)
        * security.ssl.enable_ocsp_stapling: فعال یا غیرفعال کردن OCSP Stapling برای بررسی اعتبار گواهی‌نامه‌ها
        * security.tls.version.max: حداکثر نسخه TLS مورد استفاده
        * security.tls.version.min: حداقل نسخه TLS مورد استفاده
    * services
        * services.sync.enabled: فعال یا غیرفعال کردن همگام‌سازی داده‌ها با حساب فایرفاکس
        * services.sync.engine.addons: همگام‌سازی افزونه‌ها
        * services.sync.engine.bookmarks: همگام‌سازی بوکمارک‌ها
        * services.sync.engine.passwords: همگام‌سازی پسوردها
        * services.sync.engine.tabs: همگام‌سازی تب‌ها
        * services.sync.prefs.sync.*: همگام‌سازی تنظیمات خاص با حساب فایرفاکس

## 🅱️ [jetbrains]

* Name
    * IntlliJ → JAVA
    * Pycharm → Python
    * CLion → C/C++
    * PHPstorm → PHP
    * DataGrip → DatabaseTools
    * Webstorm → html AND css AND js
    * Rider → ASP.NET,Visual Basic.NET,#C AND more
    * AppCode → apple(زبان های سویفت , C, objective-C و ++C)
    * GoLand: → go
    * RubyMine → ruby
* shortcut
    * [ALT+Insert]:‌ autoGenerate[Getter , Setter,Tostring, ...]
    * [psvm]: تمام ساختار تابع مین را خوکار ایجاد میکند
* theme
  * Ayu Dark(Island): بهروز از این استفاده میکنه گاها
  * dracula vscode
  * night-owl-native
  * vscode dark
  * vscode dark modern
  * one dark
* Plugins
  * Markdown-index


رفع مشکل کپی و چسباندن در layout فارسی در پای چارم ۲۰۲۵.۳ و دبیان۱۲

```python
export GDK_BACKEND=wayland
./pycharm.sh
```

## 🅱️ VScode

* Extension
    * javaScript
    * HTML CSS Support
    * HTML Snippets
    * JavaScript (ES6) code snippets
* python
    * autopep[autopep8]
* plugin
    * [install] material icon theme
    * [install] material theme
* shortcut
    * [CTRL+K+T] Theme
    * [Alt+Shift+F]: مرتب سازی ظاهر
    * [Ctrl + A + C]: کامنت کردن چندین خط که هایلایت شده است
    * [Ctrl + L]: select Current line
    * [Ctrl + D]:  select Current word
    * [Ctrl + Shift + K]: Delete Current Line
    * Ctrl+Shift+L: Select all occurrences of current selection
    * Ctrl+A+C #کامنت کردن چندین خط که هایلایت شده است
* shellcheck
    * shellcheck disable=SC2207,SC2128,SC2116,SC1072

## 🅱️ Eclips

* ctrl+H=search
* ctrl+Shift+R=search in resource
* ctrl+Shift+M=Move to matched couple brackets
* ctrl+Shift+f=Fix or Redesigne code layout
* Shift+Alt+R=Rename
* ctrl+/=comment or uncomment
* ctrl+F11=run
* ctrl+j=search
* ctrl+L=go to line
* ctrl+d=remove line
* shift+ctrl+enter= new line at above
* alt+/=auto complete
* ctrl+(-)=collapse
* ctrl+(+)=Expand block

## 🅱️ Gnome

### ✅️GnomeShellExtensions

- ~/.local/share/gnome-shell/extensions/
- **extension.js**: This is the main extension file and contains three main functions:
   ```
   function init () {}
   function enable () {}
   function disable() {}
   ```
- **metadata.json**: This file contains the extension information. You can create it like this
    ```
   {
   "name":"Example#1",
   "description":"Hello World",
   "shell-version":["3.36"], #array Shell versions that Extension supports
   "url":"", #GitLab or GitHub URL
   "uuid":"example@example.com", #Universally Unique Identifier.
   "version":1.0
   }
   ```
- **prefs.js**[optional]: This is the main preferences file that loads a GTK window as your extension settings.
    - Without this file your extension won’t have any settings dialogue.
- **stylesheet.css**[optional]:  This file contains css classes to style your elements.
- Enable Extension(if edit and want to see)
    - X11 Press alt-f2, type r, press enter to restart the GNOME shell.
    - Wayland Logout and re-login.
- Debug
    - `journalctl -f -o cat /usr/bin/gnome-shell` #To Debug the Extension (extension.js)
    - `journalctl -f -o cat /usr/bin/gnome-shell-extension-prefs` #To Debug the Extension Preferences (prefs)
    - log('Message'); #To log a message use log:

### ✅️ تغییرات مربوطه در زمینه بک‌گراند گنوم

```shell
gsettings set org.gnome.desktop.background picture-uri none
gsettings set org.gnome.desktop.background primary-color '#e8e8e8'
gsettings set org.gnome.desktop.background color-shading-type 'solid'
gsettings list-keys org.gnome.desktop.background
gsettings get org.gnome.desktop.background picture-options
gsettings get org.gnome.desktop.background picture-uri

```

## 🅱️ Gimp

* در گیمپ درحین رنگ‌آمیزی اگر شیفت را بگیری رنگ بک‌گراند را درنظر می‌گیرد(که شرت‌کات آن می‌شود کنترل و نقطه) و فورگران
  می‌شود شرت‌کات کنترل و کاما

## 🅱️ MPV

* Shortcut
  * [[]:Speed Decrease
  * []]:Speed Increase
  * [s]: ScreeanShot
  * [/] or [9]: volume Decrease
  * [*] or [0]: Volume Increase
  * [p]: Pause
  * [F]: fullscreen Toggle
  * [Alt + 0]: Current-Screen: 0.5
  * [Alt + 1]: Current-Screen: 1
  * [Alt + 2]: Current-Screen: 2
  * [.]: slow motion
  * 
# 🅰️ group:PackageManagements

## 🅱️ Debian

### 📁️ apt.conf

```shell
# hide autoremove warning at apt command
sudo echo 'APT::Get::HideAutoRemove "1";' | sudo tee /etc/apt/apt.conf.d/99-hide-autoremove
```

### 📁️ source.list

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

### ✅️apt

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

### ✅️apt-get

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

* sudo apt-get download php && apt-cache depends -i php |awk '/Depends:/ {print $2}' | xargs apt-get download #
  DownloadAllDependency

### ✅️apt-cache

* apt-cache search PackageName #جستجوی بسته موردنظر

### ✅️ap-cdrom

ap-cdrom install PackageName #نصب یا آپگرید یک بسته باپسوند دب از روی سی‌دی‌رام

### ✅️dpkg

* [-i PackageName.deb] # نصب آپگرید یک بسته
* [-r <Package>] #حذف یک بسته نصب شده
* [-l] # نمایش همه بسته‌های با پسوند دِب نصب شده در سیستم
* [-s PackageName] # نمایش اطلاعات مربوط به یک بسته خاص نصب شده در سیستم
* [-L PackageName] # نمایش لیست فایل‌ّای مربوط به یک بسته نصب شده
* [-L PackageName] # لیست تمام فایل‌های یک برنامه
    * dpkg -L vim
* [--contents PackageName.deb] # نمایش لیست فایل‌های مربوط به یک بسته که هنوز نصب نشده
* [-S /bin/ping] # بررسی اینکه فایل موردنظر به کدام بسته تعلق دارد

### ✅️dpkg-query

* dpkg-query -L <PackageName> # نمایش تمام فایل‌ها و فولدرهای نصب شده از یک بسته
* dpkg-query --list # نمایش لیست تمام برنامه‌های نصب شده با جزئیات آن

### ✅️dpkg-deb

* dpkg-deb -c <PackageName>.deb # تمام فایل‌هایی که قرار است با این بسته در سیستم نصب شود
* dpkg-deb -I FileName.deb # دریافت اطلاعات فایل به همراه تمامی دیپندنسی های این بسته(آی بزرگ)

### ✅️LocalRepository[DVD]

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

### ✅️LocalRepository[WEB]

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

## 🅱️ CentOS

### ✅️yum

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

### ✅️rpm

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

### ✅️EPEL

Epel: Extra Packages for Enterprise Linux

* install
    * Cenots 7 64bit : rpm -ivh <http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-7.noarch.rpm>
    * Cenots 6 64bit :rpm -ivh <http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm>
    * Cenots 6 32bit :rpm -ivh <http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm>
    * Cenots 5 64bit :rpm -ivh <http://download.fedoraproject.org/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm>
    * Cenots 5 32bit :rpm -ivh <http://download.fedoraproject.org/pub/epel/5/i386/epel-release-5-4.noarch.rpm>
* configFile
    * /etc/yum.repos.d/epel.repo

### ✅️rpmbuld

* rpmbuild -rebuild PackageName.src.rpm #ساختن یک فایل «آرپی‌ام» از روی سورس یک بسته «آرپی‌ام»

### ✅️rpm2cpio

```shell
rpm2cpio PackageName | cpio -extract -make directories *bin* #استخراج فایل‌های اجرایی از یک بسته «آرپی‌ام»
```
