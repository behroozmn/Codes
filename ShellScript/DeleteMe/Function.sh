# در صورتی که بخواهید یک تابع نوشته شده را محفاظت کنید, و جلوی آپدیت شدن آن را بگیرید از دستور زیر استفاده نمایید
readonly -f Func

# استفاده از تابع مِین
#!/usr/bin/env bash
main() {

    exit 0
}
main "$@"


# EqualArgsAndName
# اگر بخواهیم آرگومان‌های مجاز ورودی یک اسکریپت را نام توابع قرار بدهیم(هیچ متنی خارج از تابع نباید نوشته شود) در این صورت: 
# تمامی توابع و بدنه‌های آن را نوشته و در انتها کُل اسکریپت، عبارت زیر را قرار بدهید. در این صورت فقط آن تابع به اجرا در خواهد آمد
func1 () {...} 
func2 () {...} 
${1}

# بررسی وجود آرگومان
if [ -z $1 ];then
    echo Please provide an argument
fi
echo Your argument was $ARG


# Parameters:
name () {
    # Body
    echo "$@" # function all arguments array
    echo $# # number of function arguments
    echo "$?" # last function/command return code
}


# Local/Global
# بعضی متغیر ها مثل x و y بسیار پراستفاده هستند و ممکن است این نام‌ها را قبلآ بعنوان تغیر سراسری استفاده کرده‌باشد
# برای رفع تداخل این دو متغیر سراسری و لوکال(داخل تابع) همنام از دستور local در درون تابع استفاده نمایید.
#!/bin/bash 
x=100 
func () { local x=1; echo $x;} 
echo $x; #out:100 
func #out: 1
#local x=1