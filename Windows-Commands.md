# FILEs

* [C:/users/AppData/Roaming/Microsoft/Windows/StartMenu/Programs/Startup] # هر برنامه را که در این مسیر قرار بدهید در حین بالا آمدن آن کاربر به اجرا در خواهد آمد
* [C:/windows\system32\Drivers\etc\host] #دی ان اس ساده ویندوز
* [C:/windows\system32\Drivers\etc\services] #نام و شماره پروتکل ها و اطلاعات آن

# RUN

* %APPDATA% → Open App Data Folder
* %systemroot% → Open Windows Folder
* %systemdrive% → Open Windows Folder
* %windir% → Open current Windows Folder
* \\<IP or Name> #open UNC path(باز کردن پوشه اشتراکی)
* \\192.168.10.2 \f $ #باز کردن یک درایور که باید دسترسی وجود داشته باشد
* shell:startup #باز کردن برنامه‌های استارت شونده درهنگام بوت سیستم


* systeminfo.exe #نمایش اطلاعات سیستم
* msinfo32
* msconfig #یکی از موارد استارت‌آپ در ویندوز
* ncpa.cpl #network adapter setting
* mstsc #Open Remote Desktop
* diskmgmt.msc #Disk Managements
* hdwwiz.cpl #device manager
* timedate.cpl #time date
* appwiz.cpl #install or uninstall app
* compmgmt.msc # show computer managements

# COMMANDS

## Attributes

نمایش و تغییر در ویژگی فایل‌های موجود در دایرکتوری

* R → Read-only file attribute
* A → Archive file attribute
* S → System file attribute
* H → Hidden file attribute
* I → Not content indexed file attribute
* Examples:
    * attrib <File1> +h #هیدِن کردن فایل
    * attrib <File1> -h

## Color

تغییر رنگ محیط کامند

* color # Default
* color XY
* X=Background
* Y=foreground
* colorCode:
    * 0 → Black
    * 1 → Blue
    * 2 → Green
    * 3 → Aqua
    * 4 → red
    * 5 → Purple
    * 6 → Yellow
    * 7 → While
    * 8 → Gray
    * 9 → Light Blue
    * A → Light Green
    * B → Light Aqua
    * C → Light Red
    * D → Light Purplr
    * E → Light Yellow
    * F → Bright White
* Example
    * color 1a #back:Blue characters:Green
    * color 2a #back:Green characters:Green
    * color 2 #back:Black characters:DarkGreen
    * color 1 #back:Black characters:Blue
    * color F #back:Black characters:White
    * color 1F #back:Blue characters:White

## Net

* net user
    * net user /? # help
    * net user <Name> /add
    * net user <Name> <Password> /add
    * net user <Name> /delete
    * net user <Name> * /add #با زدن اینتر پسورد می‌خواهد
    * net user <Name> /comment=""
    * net user <Name> /fullname=""
    * net user <Name> /password:NO #پسورد قابلیت تغییر نخواهد داشت
    * net user <Name> /time: M,09:00am-10:00pm; #تعیین محدوده زمانی برای لاگین یک کاربر(در این مثال روزهای دوشنبه ساعت ۹ الی ۱۰)
    * net user <Name> /time: w-f,09:00am-10:00pm; #تعیین محدوده زمانی برای لاگین یک کاربر(در این مثال روزهای جهارشنبه تا جمعه ساعت ۹ الی ۱۰)
    * net user <Name> /time:all; #همیشه بتواند لاگین نماید
    * net user <Name> /active:NO; #غیر فعال کردن یک کاربر
    * net user <Name> /expired:2025 09 09; #تعیین زمان غیرفعال کردن یک کاربر
* Net group
    * net group <GroupName> /add
* net localgroup <GroupName> /add
    * net localgroup <GroupName> <userForJoinToGroup>/add
    * net localgroup <GroupName> <userForJoinToGroup>/delete
    * net localgroup #show all groups
* Net share
    * net share # show all shared directory
    * net share Ali="d:\newFolder" /remark="توضیحات"
    * net share Ali="d:\newFolder" /user=5 #همزمان ۵ نفر بتوانند متصل شوند
    * net share Ali /delete
* Net View
    * net view \\192.168.10.88 #فایل های اشتراکی در دیگران
* Net Accounts
    * net accounts #نمایش مشخصات
* Net sh #تغییر آی پی

# Other

* date /t #show time
* driverquery #view installed driver
* diskpart #دستوری که در ویندوز کارهای دیسک مَنِیجْمِنت را انجام میدهد و حتی یک فلش را بوت می‌کند
    * "rescan" | diskpart
    * list disk
    * select disk 3
    * select partition 2
    * extend size=SizeInMB
    * list vol
* get mac /s IpAddress #دریافت مک‌آدرس یک آی‌پی
* winver #ورژن ویندوز
* mspaint #باز کردن برنامهم پِیْنْت در ویندوز
* tilte "Expresion" #set title for CMD
* start # start new cmd windows
* fc file1 file2 #show compare
* path #show commands path
* sc start|stop <ServiceName>
* systeminfo
* netstat
    * netstat -a #Listen port
    * netstat -e #Nic
* ipconfig
    * ipconfig /flushdns #پاک کردن حافظه موقت دی ان اس
    * ipconfig /release
    * ipconfig /renew #get ip from dhcp
* set #show all variables
* tree #show Folders
    * tree /F #show files in folder
* type file.txt #show content
* wmic #دیتا درباره همه چیز از سیستم که برای استفاده باید از هلپ استفاده شود
    * wmic diskdrive get /format:list
    * wmic diskdrive get /all
    * wmic diskdrive get model,name,size,status
* whoami
    * whoami /all #اطلاعات خیلی زیاد از کاربران و گروه‌ها و غیره
    * نکته مهم:در قسمت «اِس‌آی‌دی» کاربران ویندوز، سه حرف آخر ۵۰۰ به منزله کاربر روت است
* Command /?
* help command
* defrag #Defragment a partition
    * defrag d:
    * defrag d: -f
    * defrag d: -a #Only Analize
* find
    * find -i "expression" file1.txt #جستجو در محتویات برای یافتن عبارت
* findstr: همانند grep در لینوکس

# Shortcut

* win+F1: به دستور قبل نگاه می‌کند و دقیقا به ازای هر «اِف۱» یک کاراکتر از دستور بالایی نمایش داده می‌شود
* F7: تمام دستورات زده شده را در قالب یک پنجره جدید به نمایش در می‌آورد
* Alt+F7: پاک کردن حافظه دستورات زده شده در کامندلاین
* F9: استفاده از شماره در «سی‌ام‌دی» دستور برای اجرای دوباره
* Shift+F10:  باز شدن پنجره مشکی‌رنگ «سی‌ام‌دی» یا همان «کامندپرامپت» در حین نصب در ویندوز
* Shift+F10:  راست کلیک