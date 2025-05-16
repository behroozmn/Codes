
 [ابزار آنلاین برای تمرین](https://awk.js.org)
# Concepts

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


# spliter

  * awk -F ':' '{print $1}' /etc/passwd #نمایش ستون‌دوم با جداکننده دو نقطه


# [PATTERN]

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
  * `awk /endPattern/{print; found=0}`: وقتی الگوی "پایان‌پذیر" پیدا شد، خط را چاپ می‌کند و متغیر را به  تنظیم می‌کند (یعنی از این به بعد هیچ خطی چاپ نخواهد شد)
  *  found: هر خطی را که بین "الگوی استارت" و "الگوی پایان" است، چاپ کند
* awk -v pattern="$PATTERN" -F ":" '$1 ~ pattern {print$0}' /etc/passwd #[Behroooz: PATTERN=user]

# [PATTERN Eexactly]

* `awk ‘/\<PATTERN\>/ {print$0}’ File.txt` #match whole words only
* `awk -F ":" 'match($1,/\<....\>/) {print$0}'` ⇄ `awk '/^\<....\>/ {print$0}'` #ستون اول دقیقا ۴کاراکتر باشد
* `awk -v EID="$enclosure" -v SLT="$slot" '-F[:\t]' '$1 == EID && $2 == SLT {print$4}'`


# Trim
* `awk 'gsub("^[ \t]*","") {print $0}'` #حذف تمام خط‌فاصله‌های ابتدایی هر سطر
* `awk 'gsub("[ \t]*$" ,"") {print$0}'` #حذف تمام خط‌فاصله‌های انتهایی هر سطر
* `awk  '!/^$/'` ⇄ `awk '/./'`  #حذف خط خالی 



# Functions

* [getline]: به ازای هر «گِت‌لاین» یک خط را نادیده می‌گیرد و به خط بعد می‌رود
  * awk '/PATTERN/ {getline;print$0}' #نمایش خط بعد از خطی که الگو یافت شده است
  * awk '/PATTERN/ {print$0;getline;print$0}'#خط الگو و خط بعد از الگو
* [sqrt]
  * awk '{ print sqrt(625)}' ⇄ echo 625|awk '{print sqrt($0)}'
* [match]
  * awk -F ":" 'match($1,/\<....\>/) {print$0}' ⇄ awk '/^\<....\>/ {print$0}' #ستون اول دقیقا ۴کاراکتر باشد
* [gsub]
  * awk '{gsub(";",""); print $2}' #حذف کاراکتر سمیکالون
  * awk 'gsub("^[ \t]*","") {print $0}' #حذف تمام خط‌فاصله‌های ابتدایی هر سطر
  * awk 'gsub("[ \t]*$" ,"") {print$0}' #حذف تمام خط‌فاصله‌های انتهایی هر سطر
* [substr]
  * echo "hello, how are you?" | awk '{ print substr( $0, 3 ) }' #حذف دو کاراکتر اول یک عبارت
* [lenght]
  * echo "hello, how are you?" | awk '{ print substr( $0, 1, length($0)-1 ) }' #حذف آخرین کاراکتر
  * echo "hello, how are you?" | awk '{ print substr( $0, 2, length($0) - 2)}'
* [tolower]
  * awk '{print tolower($0)}'
# کدنویسی

* awk '{if(Condition1){action} else if(Condition2){action} else {action}}'
* awk -F":" '{if($1=="user") print "====> " $1; else if($1 == "root") print $1 " =====> " $7; else print "[" $0 "]"}' /etc/passwd
* awk -F ":" '$3>=1000 {print $1,$3,$NF}' /etc/passwd
* awk '{<CONDITION> print$1}'
* awk 'BEGIN{print "salam";}{print $0}' #دقیقا ورودی را به خروجی هدایت میکند و تنها در اولین خط یک سلام اضافه میکند
* awk -F ':' 'BEGIN{OFS="→";}{print $1,$3}' /etc/passwd ⇄ awk -F ":" ‘{print $1 "→" $3}’ /etc/passwd ⇄ awk -F ':' 'OFS="→" {print $1,$3}' /etc/passwd #OFS کاراکتر خاص بین ستون‌ها



