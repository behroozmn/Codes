# 📍️ REGEX

<div dir="rtl">

* REGEX: RegularExpression
* ^: معرف ابتدای کلمه
* ^: گاهی معنی NOT می‌دهد ← علامتر carret داخل کروشه
* $: معرف انتهای کلمه
* .: معرف کاراکتری حتما باید باشد ولی مهم نیست چه چیزی باشد
* اگر دستور مشخص کند که اگر کاراکتر اول x و کاراکتر y فلان باشد آنگاه به z تبدیل بنماید، اگر خطی دارای تنها یک x باشد در این دستور هیچ تغییری نمیکند

</div>

* [[:alnum:]] - [A-Za-z0-9] Alphanumeric characters
* [[:alpha:]] - [A-Za-z] Alphabetic characters
* [[:blank:]] - [ \t] Space or tab characters only
* [[:cntrl:]] - [\x00-\x1F\x7F] Control characters
* [[:digit:]] - [0-9] Numeric characters
* [[:graph:]] - [!-~] Printable and visible characters
* [[:lower:]] - [a-z] Lower-case alphabetic characters
* [[:print:]] - [ -~] Printable (non-Control) characters
* [[:punct:]] - [!-/:-@[-`{-~] Punctuation characters
* [[:space:]] - [ \t\v\f\n\r] All whitespace chars
* [[:upper:]] - [A-Z] Upper-case alphabetic characters
* [[:xdigit:]] - [0-9a-fA-F] Hexadecimal digit characters

```shell
cat /etc/passwd | grep "^b" #تمام خط‌هایی که اول آن با b شروع می‌شود
cat /etc/passwd | grep "^[b]" #تمام خط‌هایی که اول آن با b شروع می‌شود
cat /etc/passwd | grep "^[abc]" #تمام خط‌هایی که اول آن a یا b یا c باشد
cat /etc/passwd | grep "^[a-h]"#تمام خط‌هایی که اول آن a تا h باشد
cat /etc/passwd | grep "^[a-c][f-n]" #کاراکتر اول از حرف a تا c و کاراکترر دوم ار حروف f تا n باشد
cat /etc/passwd | grep "^[a-n]..[f]" #کاراکتر اول از a تا n باشد و کاراکتر دوم و سوم مهم نیست ولی کاراکتر چهارم باید f باشد
cat /etc/passwd | grep "^[^b]" #تمام خط‌هایی که اول آن با b شروع نمی‌شود
cat /etc/passwd | grep n$ #تمام خط‌هایی که آخر آن به n ختم شود
cat /etc/passwd | grep [n]$ #تمام خط‌هایی که آخر آن به n ختم شود
cat /etc/passwd | grep [abc]$ #تمام خط‌هایی که آخر آن a یا b یا c باشد
cat /etc/passwd | grep [a-h]$ #تمام خط‌هایی که آخر آن a تا h باشد
```

# 📍️ Fonts

<div dir="rtl">

- [eot] این فرمت را مایکروسافت برای استفاده در وب سایت معرفی کرد اما استفاده از آن تنها برای مرورگر اینترنت اکسپلورر میسر می باشد .
- [ttf] این فرمت را اپل در اواخر دهه ۸۰ میلادی برای استفاده در PostScript توسعه داد و از اون زمان به عنوان فرمت استاندارد فونت‌ها شناخته شده است . بیشتر مرورگرها از این فرمت پشتیبانی می‌کنند غیر از اینترنت اکسپلورر.
- [svg] این فرمت بر اساس فرمت SVG (تصاویر مقایس‌پذیر) ساخته شده و سافاری در سیستم عامل iOS قبل از نسخه ۵ فقط از این نوع فونت پشتیبانی می‌کرد. در کل پشتیبانی مرورگرها از این فرمت خوب نیست و برای فارسی هم قابل استفاده نیست.
- [woff] این فرمت را موزیلا در سال ۲۰۰۹ برای استفاده در وب توسعه داد و حالا کنسرسیوم وب اون رو به رسمیت می‌شناسه. این فرمت رو بیشتر مرورگرهای مدرن و اینترنت اکسپلورر ۹ به بعد پشتیبانی می‌کنند.
- [woff2] این فرمت نسل بعد از WOFF است که توسط mozilla ارائه شده است . همچنین به دلیل فشرده سازی بهتر باعث میشود تا کار لود کردن فونت خیلی سریع تر انجام شود که در نهایت لود سریع تر وبسایت را بدنبال خواهد داشت .
- فونت خوب فارسی
    - ara baghdad
    - qurantaha
    - تبسم
- محبوبیت فونت‌ها
    - ایران سنس
    - ایران‌یکان
    - یکان
    - وزیر
    - شبنم
    - کودک
    - ساحل
    - یکان بخ
    - دروید نسخ
    - دانا
    - ایران

</div>

```
TrueType 	         font/ttf
OpenType 	         font/otf
Web Open Font Format 	 font/woff
Web Open Font Format2    font/woff2
```

![SanAndSansSerifs.png](/home/Files/01-Programming/GitHub/Codes/_srcFiles/Images/SanAndSansSerifs.png "SanAndSansSerifs.png")
![Kerning.png](/home/Files/01-Programming/GitHub/Codes/_srcFiles/Images/Kerning.png "Kerning.png")

# 📍️ Commands

## ✅️ awk

### Concepts

* [$0] → print all column
* [OFS] → Output field separator
    * awk -F ":" 'OFS="-" {print $1,$7}' /etc/passwd #نمایش تنها ستون اول و هفتم و یک خط تیره بین این دو ستون
    * awk -F ":" ‘{print $1 "→" $3}’ /etc/passwd ⇄ awk -F ':' 'OFS="→" {print $1,$3}' /etc/passwd ⇄ awk -F ':' 'BEGIN{OFS="→";}{print $1,$3}' /etc/passwd #کاراکتر خاص بین ستون‌ها
* && → AND
* || → OR
* [!] → NOT (!= Means not equal)
* [-F '<Pattern>'] or [--field-separator '<Pattern>'] → splitter
    * echo "192.168.1.1"| awk -F '.' '{ print $1" "$2" "$3" "$4;}'
* [$NF] → prints the last columns
    * awk -F ':' '{print $NF}' /etc/passwd #نمایش ستون آخر
    * awk 'NF>=3' #نمایش خطوطی که محتوی ۳ستون و بیشتر باشند
* [NR] → prints the line number(NumberRecord)
    * cat /etc/passwd | awk 'NR%2==1' #تمام خطوط فرد
    * cat /etc/passwd | awk 'NR%2==0' #تمام خطوط زوج
    * awk '$0 ~ "user" {print NR}' /etc/passwd #نمایش خطی که کلمه یوزر در آن وجود دارد
    * awk '{print NR"-"$0}' /etc/passwd #نمایش تمام خطوط به همراه شماره خط و یک خط تیره
    * awk 'NR==6 {print$1}' ⇄ awk '{if(NR==6) print$1}' #نمایش فقط خط۶
    * awk '/user/ {print$0;x=NR+2;next}(NR<=x) {print$0}' /etc/passwd #نمایش الگو و ۲ خط پس از الگو(حتی اگر چند الگو داشته باشیم)

### spliter

* awk -F ':' '{print $1}' /etc/passwd #نمایش ستون‌دوم با جداکننده دو نقطه

### [PATTERN]

* `awk '/PATTERN/ {print}'`  #نمایش خطوط حاولی الگو
* `awk '/PATTERN1/&&/PATTERN2/ {print$0}'`
* `awk '$0 ~ "PATTERN" {print$0}'`
* `awk '/^PATTERN$/ {print}'` #خطوطی که دقیقا حاوی الگو باشند و کاراکتر اضافی نداشته باشند
* `awk '! /PATTERN/'` #عدم نمایش الگو
* `awk '$0 !~ "PATTERN1|PATTERN2" {print$0}'` #عدم نمایش الگوها
* `awk '/PATTERN/{found=1} found'`  #نمایش الگو تا انتهای خروجی
    * {found=1}: وقتی الگو پیدا شد، متغیر را به ۱ تنظیم می‌کند
    * found: هر خط بعد از الگو چاپ شود
* `awk '/startPattern/{found=1} /endPattern/{print; found=0} found' file.txt` #نمایش از الگو اول تا الگوی دوم
    * `awk /startPattern/{found=1}`: وقتی الگوی "شروع شونده" پیدا شد، متغیر را به ۱ تنظیم می‌کند
    * `awk /endPattern/{print; found=0}`: وقتی الگوی "پایان‌پذیر" پیدا شد، خط را چاپ می‌کند و متغیر را به تنظیم می‌کند (یعنی از این به بعد هیچ خطی چاپ نخواهد شد)
    * found: هر خطی را که بین "الگوی استارت" و "الگوی پایان" است، چاپ کند
* `awk -v pattern="$PATTERN" -F ":" '$1 ~ pattern {print$0}' /etc/passwd` #[Behroooz: PATTERN=user]

### [PATTERN Eexactly]

* `awk ‘/\<PATTERN\>/ {print$0}’ File.txt` #match whole words only
* `awk -F ":" 'match($1,/\<....\>/) {print$0}'` ⇄ `awk '/^\<....\>/ {print$0}'` #ستون اول دقیقا ۴کاراکتر باشد
* `awk -v EID="$enclosure" -v SLT="$slot" '-F[:\t]' '$1 == EID && $2 == SLT {print$4}'`

### Trim

* `awk 'gsub("^[ \t]*","") {print $0}'` #حذف تمام خط‌فاصله‌های ابتدایی هر سطر
* `awk 'gsub("[ \t]*$" ,"") {print$0}'` #حذف تمام خط‌فاصله‌های انتهایی هر سطر
* `awk  '!/^$/'` ⇄ `awk '/./'`  #حذف خط خالی

### Functions

* [getline]: به ازای هر «گِت‌لاین» یک خط را نادیده می‌گیرد و به خط بعد می‌رود
    * `awk '/PATTERN/ {getline;print$0}'` #نمایش خط بعد از خطی که الگو یافت شده است
    * `awk '/PATTERN/ {print$0;getline;print$0}'` #خط الگو و خط بعد از الگو
* [sqrt]
    * `awk '{ print sqrt(625)}'` ⇄ `echo 625|awk '{print sqrt($0)}'`
* [match]
    * `awk -F ":" 'match($1,/\<....\>/) {print$0}'` ⇄ `awk '/^\<....\>/ {print$0}'` #ستون اول دقیقا ۴کاراکتر باشد
* [gsub]
    * `awk '{gsub(";",""); print $2}'` #حذف کاراکتر سمیکالون
    * `awk 'gsub("^[ \t]*","") {print $0}'` #حذف تمام خط‌فاصله‌های ابتدایی هر سطر
    * `awk 'gsub("[ \t]*$" ,"") {print$0}'` #حذف تمام خط‌فاصله‌های انتهایی هر سطر
* [substr]
    * `echo "hello, how are you?" | awk '{ print substr( $0, 3 ) }'` #حذف دو کاراکتر اول یک عبارت
* [lenght]
    * `echo "hello, how are you?" | awk '{ print substr( $0, 1, length($0)-1 ) }'` #حذف آخرین کاراکتر
    * `echo "hello, how are you?" | awk '{ print substr( $0, 2, length($0) - 2)}'`
* [tolower]
    * `awk '{print tolower($0)}'`

### کدنویسی

* `awk '{if(Condition1){action} else if(Condition2){action} else {action}}'`
* `awk -F":" '{if($1=="user") print "====> " $1; else if($1 == "root") print $1 " =====> " $7; else print "[" $0 "]"}' /etc/passwd`
* `awk -F ":" '$3>=1000 {print $1,$3,$NF}' /etc/passwd`
* `awk '{<CONDITION> print$1}'`
* `awk 'BEGIN{print "salam";}{print $0}'` #دقیقا ورودی را به خروجی هدایت میکند و تنها در اولین خط یک سلام اضافه میکند
* `awk -F ':' 'BEGIN{OFS="→";}{print $1,$3}' /etc/passwd ⇄ awk -F ":" ‘{print $1 "→" $3}’ /etc/passwd ⇄ awk -F ':' 'OFS="→" {print $1,$3}' /etc/passwd` #OFS کاراکتر خاص بین ستون‌ها

[OnlineTools](https://awk.js.org)

## ✅️ cat

* [-E]: نمایش انتهای خط که مثلا کاراکتر دالر باشد

```shell
cat -E fileName
```

## ✅️ dos2unix

```shell
dos2unix filedos.txt fileUnix.txt #تبدیل فرمت یک فایل متنی از سیستم ام اس داس به سیتمس یونیکس
```

## ✅️ echo

* `echo -e`: Display a message containing special characters

```shell
echo -e "You know nothing, Jon Snow.\n\t- Ygritte"
# output:You know nothing, Jon Snow.
#                - Ygritte
```

```shell
echo -e 'Here \vthe \vspaces \vhave \vvertical \vtab \vspaces.'
#Here
#     the
#         spaces
#                have
#                     vertical
#                              tab
#                                  spaces.
#

```

## ✅️ find

### Time

* [-mmin n]  → File's data was last modified less than, more than or exactly n minutes ago
    * [-mmin -60] ⇉ فایل‌های تغییر یافته در ۶۰دقیقه گذشته
    * [-mmin +60] ⇉ فایل‌های تغییر یافته از ۶۰ دقیقه پیش به قبل
* [-mtime n] → File's data was last modified less than, more than or exactly n*24 hours ago
* [-amin n]   → File was last accessed less than, more than or exactly n minutes ago
* [-atime n]  → File was last accessed less than, more than or exactly n*24 hours ago
* [-cmin n]   → File's status was last changed less than, more than or exactly n minutes ago
* [-ctime n]  → File's status was last changed less than, more than or exactly n*24 hours ago
* [-newermt]
    * [-newermt '-2 seconds'] → فایل‌هایی که تا دوثانیه پیش تغییر کرده‌اند

### Type

* [-type d] → Directory
* [-type f] → RegularFile
* [-type l] → SymbolicLink
* [-type s] → Socket
* [-type b] → block device Or block (buffered) special

### Size

* [-size +2G] → بزرگتر از دو گیگابایت
* [-size -10k] → کمتر از ۱۰ کیلوبایت
* [-size +10M -size -20M] → بزرگتر از ۱۰مگابایت و کوچکتر از ۲۰ مگابایت

### Perm

* [-perm 777]
* [! -perm 777] → NOT(without permission)
* [-perm 2644] → Find all the SGID bit files whose permissions are set to 644
* [-perm 1551] → Find all the Sticky Bit set files whose permission is 551
* [-perm /u=s] → Find all SUID set files.
* [-perm /g=s] → Find all SGID set files
* [-perm /u=r] → Find all Read-Only files
* [-perm /a=x] → Find all Executable files

### Other

* [-maxdepth X] → تعداد دایرکتوری هایی که بصورت بازگشتی مشاهده شود
    * بصورت دیفالت نامحدود است و همه زیر دایرکتوری مشاهده می‌شود
* [-empty]
    * find . -type f -empty
* [-name]
    * [-name] → جستجوی برمبنای نام
    * [-iname] → نادیده گرفتن حروف بزرگ و کوچک و آوردن هردو
    * find <Dir> -name behrooz.txt
* [-user]
    * [-user root]
* [-group]
    * [-group behrooz]
* [-print0] → رکوردهای یافت شده پشت‌سرهم در یک خط چاپ شوند
* [-print] → رکوردهای یافت شده توسط خط جدید از هم تفکیک شوند

### Examples

* [find / -type f -perm 0777 -print -exec chmod 644 {} \;] → Find all 777 permission files and use the chmod command to set permissions to 644
* [find / -type d -perm 777 -print -exec chmod 755 {} \;]  → Find all 777 permission directories and use the chmod command to set permissions to 755
* [find . -type f -name "tecmint.txt" -exec rm -f {} \;]         → To find a single file called tecmint.txt and remove it
* [find . -type f -name "*.mp3" -exec rm -f {} \;] → To find and remove multiple files such as .mp3 then use
* [find . -type f -name "*.txt" -exec rm -f {} \;]    → To find and remove multiple files such as .txt then use
* [find ./backup -type f -print0] → show all regular file wth path
* [find path -name file_name |xargs grep string] → پیدا کردن محتوی خاص در داخل فایل‌ها
* [find . -type f | xargs grep "example"]
* [] →

## ✅️ grep

### Switchs

* [--color=auto] →نمایش رنگی
    * grep --color=auto user /etc/passwd #کلمه جستجو شده رنگی نمایش داده خواهد شد
* [-i] → ignore any case sensitivity
* [-c] → count for the number of occurrences of the matched pattern in a file
* [-o] → Print only the matched parts of a matching line, with each such part on a separate output line.
* [-n] → لحاظ کردن حروف کوچک یا بزرگ[دقیقا دنبال عبارت روبرو بگرد اگر بزرگ است یا کوچک]
* [-v] → عدم نمایش خطوط پیدا شده
    * echo -ne "۱\n\n\n\n۲\n۳\n\n۴" | grep -v "^$" #حذف خط خالی
* [-m] → فقط چند مورد(برحسب خط) از موارد یافت شده را نشان بده
    * grep -m 5 nologin /etc/passwd #‌فقط ۵ خط از موارد یافت شده را نشان بده و بقیه را نادیده بگیر
* [-A] → نمایش تعداد خط پس از الگو
    * grep -A 3 systemd /etc/passwd
* [-B] → نمایش تعدا خط قبل از الگو
    * grep -B 3 systemd /etc/passwd
* [-C] → نمایش تعداد خط قبل و پس از الگو
    * grep -C 3 systemd /etc/passwd
* [-e] → Egrep
    * grep -E "one|two|three"   ⇄ egrep  "one|two|three" #multi flter
    * ldd /sbin/ifconfig | grep -E -o '/lib.*\.[0-9]'  ⇄ ldd /sbin/ifconfig | egrep -o '/lib.*\.[0-9]' #نمایش ماژول‌های یک برنامه

* [-w] → match whole words only #مثال توجه شود
    * cat /tmp/salam\
      behrooz mohamadi\
      behrooz1 mohama\
      behrooz123 behrooz\
      behrooz12\
      behroo\
    * cat /tmp/salam |grep -w behrooz\
      behrooz mohamadi\
      behrooz123 behrooz

### Repetition(تکرار)

**Repetition:** A regular expression may be followed by one of several repetition operators:

* ? The preceding item is optional and matched at most once.
* \* The preceding item will be matched zero or more times.
* \+ The preceding item will be matched one or more times.
* {n} The preceding item is matched exactly n times.
* {n,} The preceding item is matched n or more times.
* {,m} The preceding item is matched at most m times. This is a GNU extension.
* {n,m} The preceding item is matched at least n times, but not more than m times.

### EXAMPLE

* grep -E "[a]{3}" File.txt ⇄ grep  "[a]\{3\}" File.txt ⇄ egrep "[a]{3}" File.txt #خطوطی که حرف a سه مرتبه تکرار شده باشد
* grep "^<PATTERN>" File → هرچیزی که شروع خط با یک الگو باشد
* grep "<PATTERN>$" File → هرچیزی که پایان خط با یک الگو باشد

## ✅️ sed

* برای Not کردن یک علامت تعجب قبل از d یا s یا غیره قرار دهید
* برای در نظر نگرفتن case sensitive تنها کنار g یک آی بزرگ قرار دهید(یا تنها فقط یک آی قرار دهید)

### [s] → substitute

* echo  "day day day day" | sed 's/day/(day)/g' #out: (day) (day) (day) (day)
* echo  "day day day day" | sed 's/day/(&)/g' → #out: (day) (day) (day) (day)
* echo  "day day day day" | sed 's/day/night/' #تغییر فقط در اولی → #out: night day day day
* echo  "day day day day" | sed 's/day/night/2' #تغییر فقط در دومی → #out: day night day day
* echo  "day day day day" | sed 's/day/night/3' #تغییر فقط در سومی → #out: day day night day
* echo  "day day day day" | sed 's/day/night/3g' #تغییر در سومی به بعد → #out: day day night night
* echo  "day day day day" | sed 's/[a-f]/r/g' → #out: rry rry rry rry #substitute [a-f]  waith r
* sed 's/^[a-d]*/r/g' → #out: اگر کاراکتر «آ» تا کاراکتر «د» هر چند بار تکرار شده بود(در ابتدای خط) بجای آن «آر» قرار بده(حتی اگر صفر بار تکرار شده بود یعنی خط خالی بود)
* sed '3 s/<X>/<Y>/g' File.txt ⇉ #Change only in Line 3
* sed '3,5 s/<X>/<Y>/g' ⇉ #Change in Line 3 until line5
* sed '3,$    s/<X>/<Y>/g' ⇉ #Change in Line 3 until End
* sed /'^/,$ s/<X>/<Y>/g' ⇉ #Change in Line 1 until End [Carrot must be between  slash]
* sed -e 's/ *$//' #كاركتر خالي در آخر هر سطر را پاك كن
* sed -e 's/00*/0/g' #صفرهاي متعدد را با يك صفر تعويض كن

### [d] → delete

* sed '<NUM>d' #حذف خط شماره خاص
    * echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" |sed '7d' #نمایش همه بجز خط شماره هفتم
* sed '5d' File.txt #حذف خط خاص[مثلا  خط ۵]
* sed '$d' File.txt #حذف خط آخر
* sed '4,$d' File.txt #حذف خط چهارم تا آخر
* sed '/<X>/d' File.txt #حذف یک الگو از فایل
* sed -i '/<td>الگو<\/td>/{n;d}' FILE.txt #حذف یک خط پس از یک الگو
* sed '/^$/ d' File.tx #پاک کردن خطی که خالی هست و چیزی در آن نیست
* sed '/ *#/d;/^$/d' File.txt @تمام خطوط خالی و همچنین خطوط شامل کامنت حذف شود
* sed '/./!d' ⇄ sed '/^$/d'#حذف خط خالی

### [q]

* sed '<NUM>q;d' #نمایش خط شماره خاص از فایل
    * echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" |sed '6q;d' #نمایش فقط خط شماره ۶
* sed '<NUM>q' #نمایش تعداد خط اول
    * echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" |sed '6q' #نمایش 6 خط اول

### [p] → Print twice

* sed 'p' file #Print every line twice on output
* sed '6p' #print line 6 twice(every line once)
    * echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" |sed '6p' #

### [n] → سوییچ «اِن» سبب می‌شود که هرخط فقط یک بار چاپ شود

* sed -n 'p' file #print every line only once
* sed -n <NUM>p File.txt # نمایش فقط یک خط خاص
    * cat /etc/passwd|nl|sed '4q;d'
    * cat /etc/passwd|nl|sed -n 4p
    * cat /etc/passwd|nl|sed -n '4p;4q'
    * cat /etc/passwd|nl|awk '{if(NR==4) print $0}'
    * cat /etc/passwd|nl|head -n 4| tail -n +4
      هر۴تای بالا یکسان هستند
* sed -n '1,3 p' file #چاپ خط یک تا سه
* sed -n '1,8p' file #چاپ خط یک تا هشت
* sed -n '/^[a]/ p' file # خطوطی که خط اول با «آ» شروع می‌شود را چاپ کن
* sed -n '/^[a]/ !p' file #خطوطی که خط اول با «آ» شروع می‌شود را چاپ نکن
* sed -n '/string1/p' # نمایش خطوطی که شامل کلمه استرینگ۱ باشد

### [NOT]

* sed '!s/day/night/g'

## ✅️ tail

* [-<n>]
    * نمایش تعداد خط آخر
* tail [+<n>]
    * از خط شماره «اِن» شروع کن به نمایش

```shell
echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" | tail -3
8 eight
9 nine
10 ten
```

```shell
echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" | tail +3
3 three
4 four
5 five
6 six
7 seven
8 eight
9 nine
10 ten
```

## ✅️ tr

‌تبدیل کاراکتر به کاراکتر دیگر

* [-d]: حذف کاراکتر هایی که معین می‌شود
* [-c]: معکوس حذف یعنی تنها این کاراکترها را نگه‌داری کن
    * `tr -dc '0-9'` #نگهداری تنها اعداد و حذف همه کاراکترها

```shell
echo behrooz | tr 'o' 'u' #--> out: behruuz
```

## ✅️ unix2dos

```shell
unix2dos fileUnix.txt filedos.txt #تبدیل فرمت یک فایل متنی از سیستم ام اس داس به سیتمس یونیکس 
```

## ✅️ vim

### C → Change

- کارهای مربوط به change و دقیقا کارهای همان d را میکند ولی با این تفاوت که وارد مود نوشتن می‌شود
- حذف کاراکتر و رفتن به مود نوشتن

| syntax: c [number] motion | Description                                                  |
|---------------------------|--------------------------------------------------------------|
| `ce`                      | حذف کلمه از مکان کرسر تا انتهای کلمه و رفتن به مود نوشتن[ce] |
| `c2w`                     | حذف کلمه از مکان کرسر تا انتهای کلمه و رفتن به مود نوشتن[ce] |
| `c$`                      | حذف تا انتهای خط                                             |
| `ce`                      | Change rest of current word                                  |
| ``                        |                                                              |

### D → Remove

- کارهای حذف توسط این کاراکتر در مود نرمال انجام می‌شود
- حذف کاراکتر و باقی ماندن در مود نرمال

| syntax: d [number] motion | Description                                                                                |
|---------------------------|--------------------------------------------------------------------------------------------|
| `dw`                      | حذف یک کلمه:در ابتدای کلمه قرار بگیرید و d و سپس w را بفشرید(Delete word)                  |
| `de`                      | حذف یک کلمه: در ابتدای کلمه قرار بگیرید و d و سپس e را بفشرید(Delete (cut) to end of word) |
| `$d`                      | حذف یک خط کامل: حالت‌اول:در ابتدای خط قرار بگیرید و d و سپس $ را بفشرید                    |
| `^d`                      | حذف یک خط کامل: حالت‌دوم:در انتهای خط قرار بگیرید و d و سپس ^ را بفشرید                    |
| `d2w`                     | Delete (cut) next two words                                                                |
| `d3w`                     | حذف سه کلمه‌ی بعد از مکان نما و رفتن به اول کلمه بعد                                       |
| `d3e`                     | حذف سه کلمه‌ی بعد از مکان نما                                                              |
| `dd`                      | Delete(removex,cut) current line                                                           |
| `4dd`                     | remove 4 line                                                                              |
| `5dd`                     | Delete 5 lines                                                                             |
| `d$`                      | Delete (cut) to end of line                                                                |
| `D`                       | Delete (cut) to end of line (one char)                                                     |

### R → Replace

- کارهای حذف توسط این کاراکتر در مود نرمال انجام می‌شود
- کارهای مربوط به replace

| syntax: r [number] motion | Description                                                                                                                            |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `r<CHAR>`                 | در مود نرمال بخواهیم یک کاراکتر را تغییر دهیم ابتدا r را میفشاریم و سپس کاراکتر را وارد می‌کنیم                                        |
| `r<CHAR>esc`              | درمود نرمال بخواهیم چند کاراکتر را تغییر دهیم آنگاه زدن r و رفتن در مود replce و فشردن کاراکترها و در انتها فشردن esc                  |
| `:r<space><FullFilename>` | وارد کردن دیتای یک فایل دیگر در مکان کرسر آنگاه کرسر را در مکان مورد نظر قرار داده و فشردن کاراکتر : سپس r و فاصله و آدرس فایل         |
| `:r !date`                | ۴-وارد کردن دیتای یک دستور در مکان کرسر‌ آنگاه کرسر را در مکان مورد نظر قرار داده و فشردن کاراکتر : سپس r و فاصله و علامت تعجب و دستور |

### S → Substitude

| syntax: s [number] motion | Description                                                |
|---------------------------|------------------------------------------------------------|
| `:%s/foo/bar/<Enter>`     | Replace first 'foo' with 'bar' on every line               |
| `:s/foo/bar<Enter>`       | Replace first 'foo' with 'bar' on line                     |
| `:%s/foo/bar/gc<Enter>`   | Confirm replace all 'foo' with 'bar' in file               |
| `:s/foo/bar/gc<Enter>`    | Confirm replace all 'foo' with 'bar' on line               |
| `:s/foo/bar/g<Enter>`     | Replace all 'foo' with 'bar' on line                       |
| `:s/foo/bar/i<Enter>`     | Ignore case replace first 'foo' with 'bar'                 |
| `:%s/foo/bar/g<Enter>`    | Replace all 'foo' with 'bar' in file                       |
| `:%s/old/new/gc`          | تغییر کلمه در همه فایل به همراه پرسش                       |
| `:s/old/new/gc`           | تغییر کلمه در همه موارد موجود در خط به همراه پرسش از کاربر |
| `:s/old/new/g`            | تغییر کلمه در همه موارد موجود در خط                        |
| `:s/old/new`              | تغییر کلمه فقط در اولین مورد پیدا شده                      |
| `:sp<Enter>`              | New window above                                           |

### w → Write

| syntax: w [number] motion | Description   |
|---------------------------|---------------|
| `:w<Enter>`               | Save changes  |
| `:wq<Enter>`              | Save and exit |

#### ذخیره بخشی از محتوی فایل

1. زدن دکمه v [در مود نرمال] تا به حالت ویژوال مود برود
2. جابجایی کلید های بالا پایین و انتخاب خطوط مورد نیاز
3. بدون زدن دکمه دیگری فشردن دکمه :
4. سپس فشردن w و فاصله و آدرس مکان ذخیره
5. زدن اینتر

- `w /tmp/Behrooz.txt`

### Y → Yunk

| syntax: y [number] motion | Description                    |
|---------------------------|--------------------------------|
| `y$`                      | Yank (copy) to end of line     |
| `ye`                      | Yank (copy) to end of word     |
| `yw`                      | Yank to beginning of next word |
| `yy`                      | Yank (copy) line               |

### Visual Mode

| Command              | Description                   |
|----------------------|-------------------------------|
| `:w filename<Enter>` | Write selection to 'filename' |
| `v`                  | Visual mode select characters |
| `V`                  | Visual mode highlight lines   |
| `~`                  | Swap case                     |
| `>`                  | Shift right                   |
| `<`                  | Shift left                    |
| `c`                  | Change highlighted text       |
| `y`                  | Yank (copy) highlighted text  |
| `d`                  | Cut highlighted text          |
| `=`                  | Re-indent selection           |

---

### Bookmarks

| Command         | Description                 |
|-----------------|-----------------------------|
| `:marks<Enter>` | Show bookmarks              |
| `ma`            | Mark position 'a'           |
| ``a``           | Go to bookmark position 'a' |
| ````            | Go to previous position     |

---

### Set

| Command            | Description                                         |
|--------------------|-----------------------------------------------------|
| `:set hls<Enter>`  | Set highlight matching phrases(های‌لایت‌کردن‌جستجو) |
| `:set ic<Enter>`   | Set ignore case                                     |
| `:set is<Enter>`   | Set incremental search                              |
| `:set nois<Enter>` | Turn off incremental search                         |
| `:set number`      | نمایش شماره خطوط                                    |

<div dir="rtl">

### General Commands

- برای اینکه در اول خط چندین خط یک متن رو اضافه کنیم: در mode کامند دکمه CTRL+V را میزنیم تا به Mode تحت عنوان VisualBlock برویم سپس با arrow پایین و بالا و چپ و راست کنیم و محدوده را انتخاب نمایید سپس CTRL+I سبب نوشتن کاراکتر می‌شود پس از اتمام وارد کردن کاراکتر های مد نظر escape را بزنید تا برای همه محدوده بلاک اعمال شود
- در مود کامند در این برنامه کاراکتر % یعنی فایل کنونی
- برای کپی بخشی از فایل متنی ابتدا در مود نرمال کلید v را بفشرید و وارد ویژوآل مود شوید و بدون زدن دکمه دیگر دکمه بالا پایین و چپ و راست را بزنید و محتوی را انتخاب کرده و در انتها y را بزنید(با اینکار در بافر قرار می‌گیرد) سپس در مکان کرسر p را بزنید
- در محیط vim هرگاه یک دونقطه و یک علامت تعجب بزنید، هر دستوری که بخواهید قابل اجرا خواهد بود  `:!ls /tmp` و `:!/tmp/behrooz.sh`

</div>

- g: Global
- c: Confirm(در هنگام پرسش از کاربر)
- /: Search after cursor
- ?: Search before cursor

| Command                  | Description                                             |
|--------------------------|---------------------------------------------------------|
| `$`                      | Move to end of line                                     |
| `0`                      | Move to beginning of line                               |
| `:10,16s/old/new/gc`     | تغییر کلمه فقط در خطوط بین 10 تا 16 به همراه پرسش       |
| `12G`                    | Go to line 12                                           |
| `12`                     | Go to line 12                                           |
| `20l`                    | Go to column 20                                         |
| `:2,9s/foo/bar/g<Enter>` | Replace all 'foo' with 'bar' between lines 2 and 9      |
| `5b`                     | Move 5 words backward                                   |
| `5j`                     | Move down 5 lines                                       |
| `5k`                     | Move up 5 lines                                         |
| `5.`                     | Repeat last change 5 times                              |
| `5w`                     | Move 5 words forward                                    |
| `a`                      | Append                                                  |
| `A`                      | Append at end of line                                   |
| `b`                      | [Move to beginning of word [OR] Move to previous word ] |
| `ctrl+b`                 | Move backward one screen                                |
| `ctrl+e`                 | Scroll down                                             |
| `ctrl+f`                 | Move forward one screen                                 |
| `ctrl+g`                 | Show file info                                          |
| `ctrl+I`                 | رفتن به مکان جستجوی صورت گرفته                          |
| `ctrl+i`                 | Move to newer position                                  |
| `ctrl+o`                 | Move language autocomplete backward                     |
| `ctrl+o`                 | Move to older position                                  |
| `ctrl+O`                 | رفتن به مکان شروع جستجو                                 |
| `ctrl+p`                 | Move autocomplete backward                              |
| `ctrl+r`                 | Redo                                                    |
| `ctrl+x`                 | Move language autocomplete forward                      |
| `ctrl+y`                 | Scroll up                                               |
| `:e<Enter>`              | Open new file                                           |
| `:e filename<Enter>`     | Set current buffer to 'filename'                        |
| `e`                      | Move to end of word(کرسر را به انتهای کلمه بعدی می‌برد) |
| `ESC`                    | Exit insert mode to normal mode                         |
| `?foo<Enter>`            | Search backwards for 'foo'                              |
| `/foo<Enter>`            | Search forwards for 'foo'                               |
| `fw`                     | Move to next 'w' on line                                |
| `Fw`                     | Move to previous 'w' on line                            |
| `ga`                     | Show character info                                     |
| `gg`                     | Go to beginning of file                                 |
| `G`                      | Go to end of file                                       |
| `%`                      | Go to matching parenthesis or bracket                   |
| `:help cmd<Enter>`       | Lookup 'cmd' in help                                    |
| `h`                      | Move left one character                                 |
| `H`                      | Move to first line of screen                            |
| `i`                      | Insert                                                  |
| `I`                      | Insert at start of line                                 |
| `j`                      | Move down one line                                      |
| `K`                      | Look up word in man pages                               |
| `k`                      | Move up one line                                        |
| `l`                      | Move right one character                                |
| `L`                      | Move to last line of screen                             |
| `:!ls<Enter>`            | Execute 'ls' command                                    |
| `:make<Enter>`           | Run make                                                |
| `M`                      | Move to middle line of screen                           |
| `^`                      | Move to first non-whitespace char                       |
| `n`                      | Search next                                             |
| `N`                      | Search previous                                         |
| `O`                      | Insert new line above                                   |
| `o`                      | Insert new line below                                   |
| `p`                      | Paste                                                   |
| `P`                      | Paste before cursor                                     |
| `:qa<Enter>`             | Close all windows                                       |
| `:q<Enter>`              | Close current window                                    |
| `:q<Enter>`              | Quit                                                    |
| `:q!<Enter>`             | Quit without saving                                     |
| `r`                      | Change char and return to cmd mode                      |
| `:r !cmd<Enter>`         | Execute and insert results of 'cmd'                     |
| `R`                      | Enter replace mode                                      |
| `.`                      | Repeat last change                                      |
| `;`                      | Repeat last f, F, t, or T                               |
| `,`                      | Repeat last f, F, t, or T reversed                      |
| `:r filename<Enter>`     | Read and insert 'filename'                              |
| `:!rm filename<Enter>`   | Delete 'filename'                                       |
| `rx`                     | Replace current char with 'x'                           |
| `#`                      | Search for current word backward                        |
| `*`                      | Search for current word forward                         |
| `tw`                     | Move before next 'w' on line                            |
| `Tw`                     | Move before previous 'w' on line                        |
| `u`                      | Undo                                                    |
| `U`                      | Undo all changes to current line                        |
| `vim -t foo<Enter>`      | Start editing where foo is defined                      |
| `:vs<Enter>`             | New window to left                                      |
| `w`                      | Move to next word(کرسر را به ابتدای کلمه بعدی می‌برد)   |
| `:x<Enter>`              | Save and exit if modified                               |
| `zt`                     | Scroll current line to top of window                    |
| `:set background=dark`   |                                                         |
| `:syntax enable`         |                                                         |
| `:syntax on`             |                                                         |
| `:syntax off`            |                                                         |

### Files

#### 📁️ [~/.vim/color](http://amirsamimi.ir/vimrc)

```shell
cat ~/.vim/colors 

" Vim color file
"
" Author: Tomas Restrepo <tomas@winterdom.com>
"
" Note: Based on the monokai theme for textmate
" by Wimer Hazenberg and its darker variant
" by Hamish Stuart Macpherson
"

hi clear

set background=dark
if version > 580
    " no guarantees for version 5.8 and below, but this makes it stop
    " complaining
    hi clear
    if exists("syntax_on")
        syntax reset
    endif
endif
let g:colors_name="molokai"

if exists("g:molokai_original")
    let s:molokai_original = g:molokai_original
else
    let s:molokai_original = 0
endif


hi Boolean         guifg=#AE81FF
hi Character       guifg=#E6DB74
hi Number          guifg=#AE81FF
hi String          guifg=#E6DB74
hi Conditional     guifg=#F92672               gui=bold
hi Constant        guifg=#AE81FF               gui=bold
hi Cursor          guifg=#000000 guibg=#F8F8F0
hi Debug           guifg=#BCA3A3               gui=bold
hi Define          guifg=#66D9EF
hi Delimiter       guifg=#8F8F8F
hi DiffAdd                       guibg=#13354A
hi DiffChange      guifg=#89807D guibg=#4C4745
hi DiffDelete      guifg=#960050 guibg=#1E0010
hi DiffText                      guibg=#4C4745 gui=italic,bold

hi Directory       guifg=#A6E22E               gui=bold
hi Error           guifg=#960050 guibg=#1E0010
hi ErrorMsg        guifg=#F92672 guibg=#232526 gui=bold
hi Exception       guifg=#A6E22E               gui=bold
hi Float           guifg=#AE81FF
hi FoldColumn      guifg=#465457 guibg=#000000
hi Folded          guifg=#465457 guibg=#000000
hi Function        guifg=#A6E22E
hi Identifier      guifg=#FD971F
hi Ignore          guifg=#808080 guibg=bg
hi IncSearch       guifg=#C4BE89 guibg=#000000

hi Keyword         guifg=#F92672               gui=bold
hi Label           guifg=#E6DB74               gui=none
hi Macro           guifg=#C4BE89               gui=italic
hi SpecialKey      guifg=#66D9EF               gui=italic

hi MatchParen      guifg=#000000 guibg=#FD971F gui=bold
hi ModeMsg         guifg=#E6DB74
hi MoreMsg         guifg=#E6DB74
hi Operator        guifg=#F92672

" complete menu
hi Pmenu           guifg=#66D9EF guibg=#000000
hi PmenuSel                      guibg=#808080
hi PmenuSbar                     guibg=#080808
hi PmenuThumb      guifg=#66D9EF

hi PreCondit       guifg=#A6E22E               gui=bold
hi PreProc         guifg=#A6E22E
hi Question        guifg=#66D9EF
hi Repeat          guifg=#F92672               gui=bold
hi Search          guifg=#FFFFFF guibg=#455354
" marks column
hi SignColumn      guifg=#A6E22E guibg=#232526
hi SpecialChar     guifg=#F92672               gui=bold
hi SpecialComment  guifg=#465457               gui=bold
hi Special         guifg=#66D9EF guibg=bg      gui=italic
hi SpecialKey      guifg=#888A85               gui=italic
if has("spell")
    hi SpellBad    guisp=#FF0000 gui=undercurl
    hi SpellCap    guisp=#7070F0 gui=undercurl
    hi SpellLocal  guisp=#70F0F0 gui=undercurl
    hi SpellRare   guisp=#FFFFFF gui=undercurl
endif
hi Statement       guifg=#F92672               gui=bold
hi StatusLine      guifg=#455354 guibg=fg
hi StatusLineNC    guifg=#808080 guibg=#080808
hi StorageClass    guifg=#FD971F               gui=italic
hi Structure       guifg=#66D9EF
hi Tag             guifg=#F92672               gui=italic
hi Title           guifg=#ef5939
hi Todo            guifg=#FFFFFF guibg=#BB0000 gui=bold

hi Typedef         guifg=#66D9EF
hi Type            guifg=#66D9EF               gui=none
hi Underlined      guifg=#808080               gui=underline

hi VertSplit       guifg=#808080 guibg=#080808 gui=bold
hi VisualNOS                     guibg=#403D3D
hi Visual                        guibg=#403D3D
hi WarningMsg      guifg=#FFFFFF guibg=#333333 gui=bold
hi WildMenu        guifg=#66D9EF guibg=#000000

if s:molokai_original == 1
   hi Normal          guifg=#F8F8F2 guibg=#272822
   hi Comment         guifg=#75715E
   hi CursorLine                    guibg=#3E3D32 gui=underline
   hi CursorColumn                  guibg=#3E3D32
   hi LineNr          guifg=#BCBCBC guibg=#3B3A32
   hi NonText         guifg=#BCBCBC guibg=#3B3A32
else
   hi Normal          guifg=#F8F8F2 guibg=#1B1D1E
   hi Comment         guifg=#465457
   hi CursorLine                    guibg=#293739
   hi CursorColumn                  guibg=#293739
   hi LineNr          guifg=#BCBCBC guibg=#232526
   hi NonText         guifg=#BCBCBC guibg=#232526
end

"
" Support for 256-color terminal
"
if &t_Co > 255
   hi Boolean         ctermfg=135
   hi Character       ctermfg=144
   hi Number          ctermfg=135
   hi String          ctermfg=144
   hi Conditional     ctermfg=161               cterm=bold
   hi Constant        ctermfg=135               cterm=bold
   hi Cursor          ctermfg=16  ctermbg=253
   hi Debug           ctermfg=225               cterm=bold
   hi Define          ctermfg=81
   hi Delimiter       ctermfg=241

   hi DiffAdd                     ctermbg=24
   hi DiffChange      ctermfg=181 ctermbg=239
   hi DiffDelete      ctermfg=162 ctermbg=53
   hi DiffText                    ctermbg=102 cterm=bold

   hi Directory       ctermfg=118               cterm=bold
   hi Error           ctermfg=219 ctermbg=89
   hi ErrorMsg        ctermfg=199 ctermbg=253    cterm=bold
   hi Exception       ctermfg=118               cterm=bold
   hi Float           ctermfg=135
   hi FoldColumn      ctermfg=67  ctermbg=16
   hi Folded          ctermfg=67  ctermbg=16
   hi Function        ctermfg=118
   hi Identifier      ctermfg=208
   hi Ignore          ctermfg=244 ctermbg=232
   hi IncSearch       ctermfg=193 ctermbg=16

   hi Keyword         ctermfg=161               cterm=bold
   hi Label           ctermfg=229               cterm=none
   hi Macro           ctermfg=193
   hi SpecialKey      ctermfg=81  

   hi MatchParen      ctermfg=16  ctermbg=208 cterm=bold
   hi ModeMsg         ctermfg=229
   hi MoreMsg         ctermfg=229
   hi Operator        ctermfg=161

   " complete menu
   hi Pmenu           ctermfg=81  ctermbg=16
   hi PmenuSel        ctermfg=208  ctermbg=236
   hi PmenuSbar                   ctermbg=232
   hi PmenuThumb      ctermfg=81

   hi PreCondit       ctermfg=118               cterm=bold
   hi PreProc         ctermfg=118
   hi Question        ctermfg=81
   hi Repeat          ctermfg=161               cterm=bold
   hi Search          ctermfg=253 ctermbg=66

   " marks column
   hi SignColumn      ctermfg=118 ctermbg=235
   hi SpecialChar     ctermfg=161               cterm=bold
   hi SpecialComment  ctermfg=245               cterm=bold
   hi Special         ctermfg=81  
   hi SpecialKey      ctermfg=245

   hi Statement       ctermfg=161               cterm=bold
   hi StatusLine      ctermfg=238 ctermbg=253
   hi StatusLineNC    ctermfg=244 ctermbg=232
   hi StorageClass    ctermfg=208
   hi Structure       ctermfg=81
   hi Tag             ctermfg=161
   hi Title           ctermfg=166
   hi Todo            ctermfg=231 ctermbg=232   cterm=bold

   hi Typedef         ctermfg=81
   hi Type            ctermfg=81                cterm=none
   hi Underlined      ctermfg=244               cterm=underline

   hi VertSplit       ctermfg=244 ctermbg=232   cterm=bold
   hi VisualNOS                   ctermbg=238
   hi Visual                      ctermbg=235
   hi WarningMsg      ctermfg=231 ctermbg=238   cterm=bold
   hi WildMenu        ctermfg=81  ctermbg=16

   hi Normal          ctermfg=252 ctermbg=233
   hi Comment         ctermfg=59
   hi CursorLine                  ctermbg=234   cterm=underline
   hi CursorColumn                ctermbg=234
   hi LineNr          ctermfg=250 ctermbg=234
   hi NonText         ctermfg=250 ctermbg=233
end
```

#### 📁️ ~/.vimrc

```shell

:set number " Display line numbers on the left side
:set ls=2 " This makes Vim show a status line even when only one window is shown
:filetype plugin on " This line enables loading the plugin files for specific file types
:set tabstop=4 " Set tabstop to tell vim how many columns a tab counts for. Linux kernel code expects each tab to be eight columns wide.
:set expandtab " When expandtab is set, hitting Tab in insert mode will produce the appropriate number of spaces.
:set softtabstop=4 " Set softtabstop to control how many columns vim uses when you hit Tab in insert mode. If softtabstop is less than tabstop and expandtab is not set, vim will use a combination of tabs and spaces to make up the desired spacing. If softtabstop equals tabstop and expandtab is not set, vim will always use tabs. When expandtab is set, vim will always use the appropriate number of spaces.
:set shiftwidth=4 " Set shiftwidth to control how many columns text is indented with the reindent operations (<< and >>) and automatic C-style indentation. 
:setlocal foldmethod=indent " Set folding method
:set t_Co=256 " makes Vim use 256 colors
:set nowrap " Don't Wrap lines!
":colorscheme molokai "Set colorScheme
:set nocp " This changes the values of a LOT of options, enabling features which are not Vi compatible but really really nice
:set clipboard=unnamed
:set clipboard=unnamedplus
:set autoindent " Automatic indentation
:set cindent " This turns on C style indentation
:set si " Smart indent
:syntax enable " syntax highlighting
:set showmatch " Show matching brackets
:set hlsearch " Highlight in search
"":set ignorecase " Ignore case in search
:set noswapfile " Avoid swap files
:set mouse=a " Mouse Integration
:set cursorline " Highlight current line

" auto complete for ( , " , ' , [ , { 
:inoremap        (  ()<Left>
:inoremap        "  ""<Left>
:inoremap        `  ``<Left>
:inoremap        '  ''<Left>
:inoremap        [  []<Left>
:inoremap      {  {}<Left>

" auto comment and uncooment with F6 and F7 key
:autocmd FileType c,cpp,java,scala let b:comment_leader = '// '
:autocmd FileType sh,ruby,python   let b:comment_leader = '# '
:autocmd FileType vim   let b:comment_leader = '" '

:noremap <silent> #6 :<C-B>silent <C-E>s/^/<C-R>=escape(b:comment_leader,'\/')<CR>/<CR>:nohlsearch<CR> " commenting line with F6
:noremap <silent> #7 :<C-B>silent <C-E>s/^\V<C-R>=escape(b:comment_leader,'\/')<CR>//e<CR>:nohlsearch<CR> " uncommenting line with F7

:noremap <silent> #3 :tabprevious<CR> " switch to previous tab with F3
:noremap <silent> #4 :tabnext<CR> " switch to next tab with F2
:map <F8> :setlocal spell! spelllang=en_us<CR> " check spelling with F8
:set pastetoggle=<F2> " Paste mode toggle with F2 Pastemode disable auto-indent and bracket auto-compelation and it helps you to paste code fro elsewhere .


" plugins
" autocomplpop setting
:set omnifunc=syntaxcomplete " This is necessary for acp plugin
:let g:acp_behaviorKeywordLength = 1 "  Length of keyword characters before the cursor, which are needed to attempt keyword completion

" airline plugin setting
:let g:airline_theme='minimalist' " set airline plugin theme
:let g:airline#extensions#tabline#enabled = 1 " showing tabs 
:let g:airline_powerline_fonts = 1
if !exists('g:airline_symbols')
    let g:airline_symbols = {}
  endif

 " unicode symbols
  let g:airline_left_sep = '»'
  let g:airline_left_sep = '▶'
  let g:airline_right_sep = '«'
  let g:airline_right_sep = '◀'

"vim-airline-clock 
:let g:airline#extensions#clock#format = '%c'

" NERDTree plugin setting

"toggle showing NERDTree with F9
:map <F9> :NERDTreeToggle<CR> 

"open a NERDTree automatically when vim starts up if no files were specified
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

" close vim if the only window left open is a NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" Open file in new tab with ctrl + t
:let NERDTreeMapOpenInTab='<c-t>'

"indentLine 
:let g:indentLine_char = '.'


" vim-plug
" Plugins will be downloaded under the specified directory.
call plug#begin('~/.vim/plugged')

Plug 'https://github.com/rakr/vim-one.git'
Plug 'https://github.com/scrooloose/nerdtree.git'
Plug 'https://github.com/Shougo/vimshell.vim.git'
"Plug 'Shougo/vimproc.vim', {'do' : 'make'}
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'https://github.com/skywind3000/asyncrun.vim.git'

" List ends here. Plugins become visible to Vim after this call.
call plug#end()


" ۲۴ bit true colors
"Use 24-bit (true-color) mode in Vim/Neovim when outside tmux.
"If you're using tmux version 2.2 or later, you can remove the outermost $TMUX check and use tmux's 24-bit color support
"(see < http://sunaku.github.io/tmux-24bit-color.html#usage > for more information.)
if (empty($TMUX))
 if (has("nvim"))
    "For Neovim 0.1.3 and 0.1.4 < https://github.com/neovim/neovim/pull/2198 >
    let $NVIM_TUI_ENABLE_TRUE_COLOR=1

 endif
  "For Neovim > 0.1.5 and Vim > patch 7.4.1799 < https://github.com/vim/vim/commit/61be73bb0f965a895bfb064ea3e55476ac175162 >
  "Based on Vim patch 7.4.1770 (`guicolors` option) < https://github.com/vim/vim/commit/8a633e3427b47286869aa4b96f2bfc1fe65b25cd >
  " < https://github.com/neovim/neovim/wiki/Following-HEAD#20160511 >

 if (has("termguicolors"))
   set termguicolors
 endif
endif

" scary colorscheme
:let g:srcery_italic = 1
:let g:srcery_bold = 1
:let g:srcery_transparent_background = 0
:let g:srcery_underline = 1
:let g:srcery_undercurl = 1
:let g:srcery_inverse = 1
:let g:srcery_inverse_matches = 1
:let g:srcery_inverse_match_paren = 1
:let g:srcery_dim_lisp_paren = 1
:color srcery
:colorscheme srcery


"set colorscheme and airline theme according to daylight time
" if strftime("%H") < 12 && strftime("%H") > 7 
"       set background=light
"       let g:airline_theme='silver'
"       colorscheme buttercream
" else
"       colorscheme srcery
"     let g:airline_theme='minimalist' " set airline plugin theme
" endif
"
function Light()
        set background=light
        let g:airline_theme='silver'
        colorscheme buttercream
endfunction

function Dark()
    let g:srcery_transparent_background = 0
    let g:airline_theme='minimalist'
    color srcery
    colorscheme srcery
endfunction


:command LightTheme call Light()
:command DarkTheme call Dark()

" show qss file ighlighting like css files 
au BufRead,BufNewFile *.qss set filetype=css

"call pylint
:autocmd FileType python :map <F10> :AsyncRun pylint ./%<CR><CR>
:map <F12> :bw!<CR> 
"asyncrun.vim
:let g:asyncrun_open = 8
:let $PYTHONUNBUFFERED=1
:autocmd FileType python :noremap <F5> :AsyncRun -raw python % <CR> 
:autocmd FileType sh  :noremap <F5> :AsyncRun bash % <CR> 

```

## ✅️ logger

```
-i, --id              log the process ID too
-t, --tag [tag]       mark every line with this tag
-n, --server [name]   write to this remote syslog server
-T, --tcp             use TCP only
-d, --udp             use UDP only
-f, --file [file]     log the contents of this file
-h, --help            display this help text and exit
-S, --size [num]      maximum size for a single message (default 1024)
-P, --port [port]     use this port for UDP or TCP connection
-p, --priority [prio] mark given message with this priority
-s, --stderr          output message to standard error as well
-u, --socket [socket] write to this Unix socket
-V, --version         output version information and exit
```


Example:
```shell
echo "MESSAGES" | logger -p user.warn
logger -p auth.info "MESSAGES"
Command | logger
Command | logger -t salamm
```