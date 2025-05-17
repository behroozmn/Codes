# Switchs

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

# Repetition

**Repetition:** A regular expression may be followed by one of several repetition operators:

* ? The preceding item is optional and matched at most once.
* \* The preceding item will be matched zero or more times.
* \+ The preceding item will be matched one or more times.
* {n} The preceding item is matched exactly n times.
* {n,} The preceding item is matched n or more times.
* {,m} The preceding item is matched at most m times. This is a GNU extension.
* {n,m} The preceding item is matched at least n times, but not more than m times.

# EXAMPLE

* grep -E "[a]{3}" File.txt ⇄ grep  "[a]\{3\}" File.txt ⇄ egrep "[a]{3}" File.txt #خطوطی که حرف a سه مرتبه تکرار شده باشد
* grep "^<PATTERN>" File → هرچیزی که شروع خط با یک الگو باشد
* grep "<PATTERN>$" File → هرچیزی که پایان خط با یک الگو باشد