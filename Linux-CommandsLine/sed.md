* برای Not کردن یک علامت تعجب قبل از d یا s یا غیره قرار دهید
* برای در نظر نگرفتن case sensitive تنها کنار g یک آی بزرگ قرار دهید(یا تنها فقط یک آی قرار دهید)

# [s] → substitute

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

# [d] → delete

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

# [q]

* sed '<NUM>q;d' #نمایش خط شماره خاص از فایل
    * echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" |sed '6q;d' #نمایش فقط خط شماره ۶
* sed '<NUM>q' #نمایش تعداد خط اول
    * echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" |sed '6q' #نمایش 6 خط اول

# [p] → Print twice

* sed 'p' file #Print every line twice on output
* sed '6p' #print line 6 twice(every line once)
    * echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" |sed '6p' #

# [n]  → سوییچ «اِن» سبب می‌شود که هرخط فقط یک بار چاپ شود

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

# [NOT]

* sed '!s/day/night/g'