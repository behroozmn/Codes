



# Time

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

# Type 

* [-type d] → Directory
* [-type f] → RegularFile
* [-type l] →  SymbolicLink
* [-type s] → Socket
* [-type b] → block device Or block (buffered) special

# Size

* [-size +2G] → بزرگتر از  دو گیگابایت
* [-size -10k] → کمتر از ۱۰ کیلوبایت 
* [-size +10M -size -20M] → بزرگتر از ۱۰مگابایت و کوچکتر از ۲۰ مگابایت
  
# Perm

* [-perm 777]
* [! -perm 777] → NOT(without permission)
* [-perm 2644] → Find all the SGID bit files whose permissions are set to 644
* [-perm 1551] → Find all the Sticky Bit set files whose permission is 551
* [-perm /u=s] → Find all SUID set files.
* [-perm /g=s] → Find all SGID set files
* [-perm /u=r] → Find all Read-Only files
* [-perm /a=x] → Find all Executable files
  
# Other

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


# Examples

* [find / -type f -perm 0777 -print -exec chmod 644 {} \;] → Find all 777 permission files           and use the chmod command to set permissions to 644
* [find / -type d -perm 777 -print -exec chmod 755 {} \;]  → Find all 777 permission directories and use the chmod command to set permissions to 755
* [find . -type f -name "tecmint.txt" -exec rm -f {} \;]         → To find a single file called tecmint.txt and remove it
* [find . -type f -name "*.mp3" -exec rm -f {} \;] → To find and remove multiple files such as .mp3 then use
* [find . -type f -name "*.txt" -exec rm -f {} \;]    → To find and remove multiple files such as .txt    then use
* [find ./backup -type f -print0] →  show all regular file wth path
* [find path -name file_name |xargs grep string] → پیدا کردن محتوی خاص در داخل فایل‌ها
* [find . -type f | xargs grep "example"]
* [] → 