#!/bin/bash

#assign default value to variable if variable is empty otherwise assign null
#اگر متغیر مقدار داشته باشد هیچ کاری نمیکند
#اگر متغیر مقدار نداشته باشد آنگاه مقدار پیش‌فرض تعیین شده را در آن میریزد
: "${variable:=defaultValue}"



#تبدیل به حروف بزرگ
Name=BeHrOoz
echo "${Name^^}"   #BEHROOZ


#تبدیل به حروف کوچک
Name=BeHrOoz
echo  "${Name,,}" # behrooz

#حذف کاراکتر از ابتدای یک متغیر
Name=behroozbehrooz
echo  "${Name#b}"    # ehroozbehrooz
echo  "${Name#be}"   # hroozbehrooz
echo  "${Name#b*r}"  # oozbehrooz(Remove b until r) → حذف پیشامد اول
echo  "${Name##b*r}" # ooz(Remove b until r)        → حذف بزرگترین  پیشامد
path="/home/Files/Documents/salam.txt"
echo ${path##*[/]}      #→ show only BaseName(FileName) # حذف بزرگترین پیشامدی که آخر آن اسلش است و قبل آن هرجیزی می‌تواند باشد

#حذف کاراکتر از آخر یک متغیر
Name=behroozbehrooz
echo  "${Name%z}"   # behroozbehroo
echo  "${Name%ooz}" # behroozbehr
echo  "${Name%h*z}" # behroozbe
echo  "${Name%%h*z}" # be            → حذف بزرگترین  پیشامد
Filename=salam.txt
echo "${Filename%.*}" 

# تبدیل یک کاراکتر به کاراکتر دیگر از محتویات یک متغیر
Name=behroozbehrooz
echo  "${Name/o/t}"   #once change: o → t     (behrtozbehrooz)
echo  "${Name//o/t}"  #All change : o → t     (behrttzbehrttz) 

#نمایش از اندیس شروع تا اندیس اتمام
Name=behrooz
echo  "${Name:0}"      # → behrooz
echo  "${Name:2}"      # → hrooz
echo  "${Name:0:2}"    # → be
echo  "${Name::2}"     # → be
echo  "${Name:3:5}"    # → rooz
echo  "${Name:0:-1}"   # → behroo
echo  "${Name:0:-4}"   # → beh
echo  "${Name::-4}"    # → beh


echo $$                # → Pid of current shell


#variable indirect expansion
  #تعریف متغیرها
  var1="Hello"
  var2="var1"
  # گسترش غیرمستقیم
  echo ${!var2}  # این خط "Hello" را چاپ می‌کند
