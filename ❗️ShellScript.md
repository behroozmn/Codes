# 🅰️ CheetSeet And General

```
~     Home directory
$     Denote a variable (as in $HOME or $USER)
&     Run a command in the background
;     Command termination
&&    Continue to the next command upon success (AND)
||    Continue to the next command upon failure (OR)
|     Use output of the first command as input for the next
'     Treat all contents as literal
"     Treat spaces as literal, but expand variables 
\     Treat the next character as literal
( )   Execute contents in a subshell
{ ;}  Execute in current shell (terminate with semi-colon)
[  ]  Test expression
(( )) Evaluate contents as a mathematical expression
[[ ]] Test expression, returning 0 or 1

>  Overwrite existing content
<  Overwrite existing content
>> Append to existing content
<< Append to existing content

?  Match exactly one of any character
*  Match zero or more of any character

[0-9]    Any digit
[a-z]    Any lowercase alpha
[A-Z]    Any uppercase alpha
[a-zA-Z] Any lowercase or uppercase alpha
[abc]    Only a, b, and c
[!a-z]   No lowercase alpha
[!1-3]   No 1, 2, or 3, but all other digits
[b-hot]  Lowercase b through h, and the letter o and the letter t
[A-M0-9] Uppercase alpha A through M, and any digit

\b     Backspace
\e     Escape
\f     Form feed (like a non-returning newline)
\n     Newline
\r     Carriage return
\t     Horizontal tab
\v     Vertical tab
\\     Backslash
\cH    Control-H
\uHHHH Unicode character of hexadecimal value HHHH
\NNN   8-bit character with octal value NNN
```

- Indention: در شل اسکریپت به هیچ عنوان از تب استفاده نشود و تنها از اسپیس استفاده شود و اگر بخواهیم بحث indentation را رعایت نماییم از دو اسپیس استفاده مینماییم
- Note: فرق sh و bash این است که گاهی ممکن است لینوکس آنقدر کوچک شده باشد که برنامه bash را نداشته باشد و تنها یک شل Customشده کوچک داشته باشد و این شل توسط دستور sh شناخته می شود و در این صورت اگر بجای /bin/sh عبارت /bin/bash قرار بدید ممکن است اسکریپت نتواند شل را اجرا نماید.(معمولا sh به bash اشاره دارد)

```shell
# ✅️Command.returnCode.Check.success
#!/bin/bash
if command >/dev/null 2>&1; then
    echo "succeed"
else
    echo "failed"
fi

# ✅️Command.returnCode.Check.failed
#!/bin/bash
# check if last command failed
if ! command >/dev/null 2>&1; then
    echo "failed"
else
    echo "succeed"
fi

# ✅️Command.ReturnCode
# برای صحت سنجی اجرای یک دستور ، استفاده از دو بلاک [] پشت سر هم غلط است
# 1-هرچیزی که در قسمت [ ] قرار بگیرد به مثابه یک دستور مستقل که دارای returnCode است در نظر گرفته خواهد شد
# 2-در صورت صحیح بودن[ شرط] اول، Command1 یک returnCode جدید صادر خواهد کرد
[1]
x=0
[ "$x == "0" ] && command1 (exitCode is 0)
[ "$x == "1" ] && command2
echo $?

output: command1
returnCode 1

[2]
[ "$?" == "0" ] && Command1
[ "$?" == "10" ] && Command2

# ✅️Command.output
#!/bin/bash
cd /tmp
result="$(pwd)"
echo "$result" #[output] → /tmp

# ✅️Command.GetPassword
# get text as input from user without showing
echo "Please enter your password: "
read -rs password
echo "${password}"

# ✅️ Port Scan
host=$1
port_first=1
port_last=65535
echo >/dev/tcp/$host/$port >/dev/null 2>&1 && echo "$port open"

```
* بررسی اتصال به اینترنت
```shell
while true; do ping 8.8.8.8 -c 2 > /tmp/ping.log  && zenity --info --text="$(date +%T).\n\nInternet is OK." --title="Coffee time" --ok-label="exit" && exit; sleep 2; done;

```

```shell
_time=$(date +%Y/%m/%d-%H:%M:%S)
if /usr/bin/zenity --question --title="یادآوری" --text="${_time}\nثبت فعالیت کنونی :" --ok-label="ثبت" --cancel-label="عدم ثبت"; then
	echo "${_time}-Registry successfully done" >>"/tmp/Behrooz.log"
fi
```
# 🅰️ String

```shell
myCustomString="  Behrooz Mohammadi Nasab Sahzabi  "

lowercase="${myCustomString,,}"  # behrooz mohammadi nasab sahzabi
uppercase="${myCustomString^^}"  # BEHROOZ MOHAMMADI NASAB SAHZABI
trimmed_RemoveWhiteSpace_leading_and_trailing=$(echo -e "${string}" | sed -e 's/^[[:space:]]*//' | sed -e 's/[[:space:]]*$//')  
trimmed_RemoveWhiteSpace_all=$(echo -e "${string}" | tr -d '[:space:]')
TrimLeft_RemoveLeadingWhiteSpace=$(echo -e "${string}" | sed -e 's/^[[:space:]]*//')
TrimRight_RemoveTrailingWhiteSpace=$(echo -e "${string}" | sed -e 's/[[:space:]]*$//')
reverseStringCharacters=$(echo -e "${string}" | rev)
randomString=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 8 ; echo '')
concatenateTwoStrings="${string1}${string2}"

# ✅️ check whether string contains substring
if [[ "${string}" == *"${substring}"* ]]; then
echo "${string} contains: ${substring}"
fi

# ✅️ get length of a variable that is a string
behrooz=123456
echo "${#behrooz}" output:6


# ✅️ Structure
${variable-name-here:index-of-character:number-of-characters-from-index-onwards-to-return}

MyString="behroozMohammadiNasabSahzabi" #Example
echo "${MyString:0:5}"   #[output] → behro
echo "${MyString:20:6}"  #[output] → bSahza
echo "${MyString:0:5}"   #[output] → behro


# ✅️ Contain SubString

if [[ "\({string}" == *"\){substring}"* ]]; then
echo "\({string} contains: \){substring}"
fi

```

```shell
# ✅️ assign default value to variable if variable is empty otherwise assign null
#اگر متغیر مقدار داشته باشد هیچ کاری نمیکند
#اگر متغیر مقدار نداشته باشد آنگاه مقدار پیش‌فرض تعیین شده را در آن میریزد
: "${variable:=defaultValue}"




#✅️ حذف کاراکتر از ابتدای یک متغیر
Name=behroozbehrooz
echo  "${Name#b}"    # ehroozbehrooz
echo  "${Name#be}"   # hroozbehrooz
echo  "${Name#b*r}"  # oozbehrooz(Remove b until r) → حذف پیشامد اول
echo  "${Name##b*r}" # ooz(Remove b until r)        → حذف بزرگترین  پیشامد
path="/home/Files/Documents/salam.txt"
echo ${path##*[/]}      #→ show only BaseName(FileName) # حذف بزرگترین پیشامدی که آخر آن اسلش است و قبل آن هرجیزی می‌تواند باشد

#✅️ حذف کاراکتر از آخر یک متغیر
Name=behroozbehrooz
echo  "${Name%z}"   # behroozbehroo
echo  "${Name%ooz}" # behroozbehr
echo  "${Name%h*z}" # behroozbe
echo  "${Name%%h*z}" # be            → حذف بزرگترین  پیشامد
Filename=salam.txt
echo "${Filename%.*}" 

#✅️ تبدیل یک کاراکتر به کاراکتر دیگر از محتویات یک متغیر
Name=behroozbehrooz
echo  "${Name/o/t}"   #once change: o → t     (behrtozbehrooz)
echo  "${Name//o/t}"  #All change : o → t     (behrttzbehrttz) 

#✅️ نمایش از اندیس شروع تا اندیس اتمام
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


#✅️ variable indirect expansion
  #تعریف متغیرها
  var1="Hello"
  var2="var1"
  # گسترش غیرمستقیم
  echo ${!var2}  # این خط "Hello" را چاپ می‌کند



# ✅️ bold
echo -e "\e[1mbold\e[0m"

# ✅️ italic
echo -e "\e[3mitalic\e[0m"

# ✅️ bold italic
echo -e "\e[3m\e[1mbold italic\e[0m"

# ✅️ underline
echo -e "\e[4munderline\e[0m"

# ✅️ strikethrough
echo -e "\e[9mstrikethrough\e[0m"

echo "$(tput setaf 0)"black text")(tput sgr0)"
echo "$(tput setaf 1)"red text")(tput sgr0)"
echo "$(tput setaf 2)"green text")(tput sgr0)"
echo "$(tput setaf 3)"yellow text")(tput sgr0)"
echo "$(tput setaf 4)"blue text")(tput sgr0)"
echo "$(tput setaf 5)"magenta text")(tput sgr0)"
echo "$(tput setaf 6)"cyan text")(tput sgr0)"
echo "$(tput setaf 7)"white text")(tput sgr0)"


```

## 🅱️ differentStarAndAtsign

```shell
echo "Using \"\$*\":"
for a in "$*"; do
    echo $a;
done

echo -e "\nUsing \$*:"
for a in $*; do
    echo $a;
done

echo -e "\nUsing \"\$@\":"
for a in "$@"; do
    echo $a;
done

echo -e "\nUsing \$@:"
for a in $@; do
    echo $a;
done

# ussing format
#./script.sh  one two "three four"
# نکته: همواره اگر از دابل کوت استفاده شود سبب می‌شود که اسپیس دیتِکت شود

```

# 🅰️ Function

```shell
# ✅️Parameters:
name () {
    # Body
    echo "$@" # function all arguments array
    echo $# # number of function arguments
    echo "$?" # last function/command return code
}

#✅️ Local/Global
# بعضی متغیر ها مثل x و y بسیار پراستفاده هستند و ممکن است این نام‌ها را قبلآ بعنوان تغیر سراسری استفاده کرده‌باشد
# برای رفع تداخل این دو متغیر سراسری و لوکال(داخل تابع) همنام از دستور local در درون تابع استفاده نمایید.
#!/bin/bash 
x=100 
func () { local x=1; echo $x;} 
echo $x; #out:100 
func #out: 1
#local x=1



# ✅️در صورتی که بخواهید یک تابع نوشته شده را محفاظت کنید, و جلوی آپدیت شدن آن را بگیرید از دستور زیر استفاده نمایید
readonly -f Func

# ✅️استفاده از تابع مِین
#!/usr/bin/env bash
main() {

    exit 0
}
main "$@"


# ✅️EqualArgsAndName
# اگر بخواهیم آرگومان‌های مجاز ورودی یک اسکریپت را نام توابع قرار بدهیم(هیچ متنی خارج از تابع نباید نوشته شود) در این صورت: 
# تمامی توابع و بدنه‌های آن را نوشته و در انتها کُل اسکریپت، عبارت زیر را قرار بدهید. در این صورت فقط آن تابع به اجرا در خواهد آمد
func1 () {...} 
func2 () {...} 
${1}

# بررسی وجود آرگومان✅️
if [ -z $1 ];then
    echo Please provide an argument
fi
echo Your argument was $ARG


```

# 🅰️ condition

* `[ condition ] || command` if condition is false then run command
* `[ condition ] && command` if condition is true then run command

| #         | title                            | sample                                                                  | Description                                                  |
|-----------|----------------------------------|-------------------------------------------------------------------------|--------------------------------------------------------------|
| -s        | Condition.File.Notempty          |                                                                         |                                                              |
| -r        | Condition.File.Readalbe          |                                                                         |                                                              |
| -w        | Condition.File.writealbe         |                                                                         |                                                              |
| -ot       | Condition.if.File1OlderThanFile2 | `[ "/path/to/file1" -ot "/path/to/file2" ]`                             |                                                              |
| -nt       | Condition.if.File1NewerThanFile2 | `[ "/path/to/file1" -nt "/path/to/file2" ]`                             | check if file1 is newer than file2                           |                         
| =         | Condition.if.evaluating          | `[ "${NAME}" = "Kevin" ]`                                               | از دو علامت مستاوی استفاده نکنید                             |                        
| !=        | Condition.if.NOTevaluating       | `[[ "${string1}" != "${string2}" ]]`                                    | if strings are not equal                                     |
| (( ... )) | Condition.if.evaluating_Integers |                                                                         | Use (( ... )) rather than [[ ... ]] when evaluating integers |
| -z        | condition.Arguments.zeroArgument | ` if [ -z $1 ];then echo ThereIs no argument; read ARG; else ARG=$1 fi` | بررسی برای وجود آرگومان ورودی                                |
| -z        | condition.String.isEmpty         | `if [[ -z "${string}" ]]; then echo "empty string" fi`                  |                                                              |
| -n        | condition.String.NotEmpty        | `if [[ -n "${string}" ]]; then echo "string is not empty" fi`           |                                                              |

```shell
# Compaire
man test
man bash


test -e $VAR                #Check Exist
test -d "$VAR"              #A test to check if a FILE exists and is a directory.
test -x "$VAR"              #A test to check if FILE exists and execute (or search) permission is granted
test -e "$VAR"              #A test to check if FILE exists
test -h "$VAR"              #A test to check if FILE exists and is a symbolic link (same as -L)
test -r "$VAR"              #A test to check if FILE exists and read permission is granted.
test -f "$VAR"              #test exist readable
test -w "$VAR"              #A test to check if FILE exists and write permission is granted.
test "$VAR" -ef "$VAR"      #A test to check if FILE1 and FILE2 have the same device and inode numbers.
test "$VAR" -nt "$VAR"      #A test to check if FILE1 is newer (modification date) than FILE2.
test "$VAR" -ot "$VAR"      #A test to check if FILE1 is older than FILE2.
test "$VAR1" -eq "$VAR2"    #[intEqual]A test to compare two different INTEGERS. Returns TRUE if they are of equal value.
test "$VAR1" -ge "$VAR2"    #[intGreatEqual]A test to compare two different INTEGERS. Returns TRUE if INTEGER1 is of equal or greater value than INTEGER2.
test "$VAR1" -gt "$VAR2"    #[intGreatThan]A test to compare two different INTEGERS. Returns TRUE if INTEGER1 is greater than INTEGER2 in value
test "$VAR1" -le "$VAR2"    #[intLessEqual]A test to compare two different INTEGERS. Returns TRUE if INTEGER1 is less than or equal to INTEGER2 in value.
test "$VAR1" -lt "$VAR2"    #[intLessThan]A test to compare two different INTEGERS. Returns TRUE if INTEGER1 is less than INTEGER2 in value.
test "$VAR1" -ne "$VAR2"    #[intNotEqual]A test to compare two different INTEGERS. Returns TRUE if INTEGER1 is NOT equal to INTEGER2 in value.
test -z "$VAR"              #[string Empty] A test to check the lengh of VAR is zero (i.e. it is empty) and returns TRUE if so.
test "$VAR1" = "$VAR2"      #[string Equal] A test to compare two different STRINGS and returns TRUE if they are of equal value
test -n "$VAR"              #[string NotEmpty] A test that checks the length of a STRING is greater than zero and returns TRUE if so
test "$VAR1" != "$VAR2"     #[string NotEqual] A test to compare two different STRINGS. Returns TRUE if they are NOT of equal value






if [ -d "/../dir/.." ]   # → If Dir  Exist
if [ -f "/../file.txt" ] # → If file Exist
if [ -z "$variable" ]    # → وقتی متغیر تهی باشد
```

## 🅱️ CommandSwitch Conditional

```shell
#!/bin/bash
while getopts "a:f:n:v:z:" options; do
    case "${options}" in
    a)
        valueA="$OPTARG"
        ;;
    f)
        valueF="$OPTARG"
        ;;
    n)
        valueN="$OPTARG"
        ;;
    v)
        valueV="$OPTARG"
        ;;
    z)
        valueZ="$OPTARG"
        ;;
    *)
        :
        ;;
    esac
done

echo "valueA:${valueA}"
echo "valueF:${valueF}"
echo "valueN:${valueN}"
echo "valueV:${valueV}"
echo "valueZ:${valueZ} "


# output:
# ./CommandSwitch.sh  -z 1 -n2  -v 3 -a 4  -f 5
# valueA:4
# valueF:5
# valueN:2
# valueV:3
# valueZ:1
```

## 🅱️ Select

```shell
echo "choose one of them"
select x in one two three; do
    if [ -n "$x" ]; then
        echo "Have you selected :$x"
        break
    else
        echo 'invalid choice'
    fi
done

```

# 🅰️ List

## 🅱️ Array

نکته:اگر یک آرایه سه عضو داشته باشد و مستقیما عضو هشتم را مقدار دهی نماییم آنگه عضو مابین تهی خواهد بود و عضو هشت همچنان هشتم باقی خواهد ماند یعنی اگر بگوییم همه را نمایش بده پشت سر هم نمایش در می‌آید ولی عضو تهی نمایش نمی‌شود

```shell
myArray=""
newArray=""

# Declare : declare an array
declareArray() {
    myArray=('constant' "${variable}" 'another constant')
}

#Push new Item to the end of arrayadd
appendToEnd() {
    myArray+=('newItem') 
}

#access all array element
getAll() {
    echo "${myArray[@]}"
}

#For: iterate array elements
getAllByFor() {
    for item in "${myArray[@]}"; do
        echo "${item}"
    done
}

#GetIndex: retrieve element from array at specified index (zero based)
getOneByIndex() {
    echo "${myArray[index]}" # مثلا ایندکس شماره ۳ یعنی عضو چهارم
}

#Get Index: n elements of an array from specified index (zero based)
getSomeFromZeroUntilIndex() {
    newArray="${myArray[*]:fromIndex:n}"
}

#filter elements of an array based on given grep pattern
checkExistElementByPattern() {
    readarray -t Var_filteredData < <(for i in "\({myArray[@]}"; do echo "\){i}"; done | grep 'pattern')
}

#Contains: check if the array contains an element
checkExistElement() {
    if [[ "${myArray[*]}" =~ 'element' ]]; then
        echo 'array contains element'
    fi
}

#Concat: concatenate two arrays
ConcatTwoArrays() {
    newArray=("\({array1[@]}" "\){array2[@]}")
}

#Delete: delete entire array
delete() {
    unset myArray
}

#Delete: delete element at index from array
deleteIndex() {
    unset "myArray[index]"
}

#Index: set array element at specified index
setonIndex() {
    myArray[index]="value"
}

#FindOrReplace: find and replace elements in array using regex
findAndReplace() {
    newArray=${myArray[*]//find/replace}
}

#Length: length of an array
lenght() {
    length=${#myArray[@]}
}

#Reverse: reverse order of array elements
reverse() {
    for ((i = ${#myArray[@]} - 1; i >= 0; i--)); do
        reversed+=("${myArray[i]}")
    done
    unset "myArray" # optional
    echo "${reversed[@]}"
}

echo "${myArray[@]:2:4}" # نمایش عضو دوم تا چهارم
echo "${myArray[@]:1}" # نمایش عضو اول تا آخر
```

## 🅱️ Expand variable names dynamically

```shell
Problematic code: # ❌️ این شیوه غلط است و فقط برای راهنمایی آورده شده است
        var_1="hello world"
        n=1
        echo "${var_$n}"


Correct code:
        # Use arrays instead of dynamic names
        declare -a var
        var[1]="hello world"
        n=1
        echo "${var[n]}"

OR
        # Expand variable names dynamically
        var_1="hello world"
        n=1
        name="var_$n"
        echo "${!name}"
```

# 🅰️ DataBase

```shell
mysql -u root -p1234567890  -h localhost -e "USE MyDatabaseName;SELECT * FROM raiddisk;"
mysql -u root -p1234567890 "MyDatabaseName" -h localhost -e "SELECT * FROM raiddisk;"
/usr/local/mysql/bin/mysql -u root -p123456789 "MyDatabaseName" -h localhost -Bse "SELECT * FROM raiddisk INTO OUTFILE '/tmp/myfilename.csv' FIELDS TERMINATED BY ','  ENCLOSED BY '\"' LINES TERMINATED BY '\n'"

echo "select * from resyncrate;" > /tmp/behrooz.sql
mysql --user=root --password=123456789 MyDatabaseName < /tmp/behrooz.sql

```

```shell
set -f        # disable globbing
IFS=$'\n'     # set field separator to NL (only)
arr=($(mysql -u root -p123456789 "MyDatabaseName" -h localhost -Bse "SELECT * FROM raiddisk;"))
 
for i in "${arr[@]}"
do
   echo "$i"
done



```

# 🅰️ Graphical commands

## 🅱️ yad

نمایش یک پنجره به سبک برنامه نویسی ویژوال:

```shell
echo My text | yad --text-info --width=400 --height=200
```

```shell
yad \
--title="Desktop entry editor" \
--text="Simple desktop entry editor" \
--form \
--field="Type:CB" \
--field="Name" \
--field="Generic name" \
--field="Comment" \
--field="Command:FL" \
--field="Icon" \
--field="Date of birth":DT \
--field="In terminal:CHK" \
--field="Startup notify:CHK" 'Application!behrooz mohammadi!yazahra' "Name" "Generic name" "This is the comment" "/usr/bin/yad" "yad" "Click calendar icon" FALSE TRUE \
--button="WebUpd8:2" \
--button="gtk-ok:0" \
--button="gtk-cancel:1"
```

## 🅱️ Whiptail

اگر بخواهیم در یک متن با خاصیت بلی ویا خیر در قلب ترمینال نمایش شود (همانند ok و Cancell در حین نصب آپاچی) از دستور زیر استفاده می‌نماییم:

```shell
whiptail --title "<message box title>" --msgbox "<text to show>" <height> <width>
```

[url1](https://unix.stackexchange.com/questions/144924/how-to-create-a-message-box-from-the-command-line)
[url2](https://stackoverflow.com/questions/7035/how-to-show-a-gui-message-box-from-a-bash-script-in-linux)
[url3](http://linux.byexamples.com/archives/265/a-complete-zenity-dialog-examples-2)
[url4](https://www.howtogeek.com/107537/how-to-make-simple-graphical-shell-scripts-with-zenity-on-linux)
[url5](http://jamesslocum.com/post/55694754191)
[url6](http://xmodulo.com/create-dialog-boxes-interactive-shell-script.html)

### ✅️ [Yes/No]Box

```shell
whiptail --title "<dialog box title>" --yesno "<text to show>" <height> <width>
```

```shell
#!/bin/bash
if (whiptail --title "Test Yes/No Box" --yesno "Choose between Yes and No." 10 60); then
    echo "You chose Yes. Exit status was $?."
else
    echo "You chose No. Exit status was $?."
fi

```

```shell
#!/bin/bash
if (whiptail --title "Test Yes/No Box" --yes-button "Skittles" --no-button "M&M's" --yesno "Which do you like better?" 10 60); then
    echo "You chose Skittles Exit status was $?."
else
    echo "You chose M&M's. Exit status was $?."
fi

```

### ✅️ ChecklistDialog

```shell
whiptail --title "<checklist title>" --checklist "<text to show>" <height> <width> <list height> [ <tag> <item> <status> ] . . .
```

```shell
#!/bin/bash
DISTROS=$(whiptail --title "Test Checklist Dialog" --checklist \
"Choose preferred Linux distros" 15 60 4 \
"debian" "Venerable Debian" ON \
"ubuntu" "Popular Ubuntu" OFF \
"centos" "Stable CentOS" ON \
"mint" "Rising Star Mint" OFF 3>&1 1>&2 2>&3)
exitstatus=$?
if [ $exitstatus = 0 ]; then
    echo "Your favorite distros are:" $DISTROS
else
    echo "You chose Cancel."
fi

```

### ✅️ FormInput

```shell
whiptail --title "<input box title>" --inputbox "<text to show>" <height> <width> <default-text>
```

```shell
#!/bin/bash
PET=$(whiptail --title "Test Free-form Input Box" --inputbox "What is your pet's name?" 10 60 Wigglebutt 3>&1 1>&2 2>&3)
 
exitstatus=$?
if [ $exitstatus = 0 ]; then
    echo "Your pet name is:" $PET
else
    echo "You chose Cancel."
fi
```

### ✅️ MenuBox

```shell
whiptail --title "<menu title>" --menu "<text to show>" <height> <width> <menu height> [ <tag> <item> ] . . .
```

```shell
#!/bin/bash
OPTION=$(whiptail --title "Test Menu Dialog" --menu "Choose your option" 15 60 4 \
    "1" "Grilled Spicy Sausage" \
    "2" "Grilled Halloumi Cheese" \
    "3" "Charcoaled Chicken Wings" \
    "4" "Fried Aubergine" 3>&1 1>&2 2>&3)

exitstatus=$?
if [ $exitstatus = 0 ]; then
    echo "Your chosen option:" $OPTION
else
    echo "You chose Cancel."
fi

```

### ✅️ MessageBox

```shell
whiptail --title "<message box title>" --msgbox "<text to show>" <height> <width>
```

```shell
#!/bin/bash
whiptail --title "Test Message Box" --msgbox "Create a message box with whiptail. Choose Ok to continue." 10 60
```

### ✅️ PasswordBox

```shell
whiptail --title "<password box title>" --passwordbox "<text to show>" <height> <width>
```

```shell
#!/bin/bash
PASSWORD=$(whiptail --title "Test Password Box" --passwordbox "Enter your password and choose Ok to continue." 10 60 3>&1 1>&2 2>&3)
 
exitstatus=$?
if [ $exitstatus = 0 ]; then
    echo "Your password is:" $PASSWORD
else
    echo "You chose Cancel."
fi
```

### ✅️ ProgressBar

```shell
whiptail --gauge "<test to show>" <height> <width> <inital percent>
```

```shell
#!/bin/bash
{
    for ((i = 0 ; i <= 100 ; i+=20)); do
        sleep 1
        echo $i
    done
} | whiptail --gauge "Please wait while installing" 6 60 0
```

### ✅️ RadiolistDialog

```shell
whiptail --title "<radiolist title>" --radiolist "<text to show>" <height> <width> <list height> [ <tag> <item> <status> ] . . .
```

```shell
#!/bin/bash
DISTROS=$(whiptail --title "Test Checklist Dialog" --radiolist \
"What is the Linux distro of your choice?" 15 60 4 \
"debian" "Venerable Debian" ON \
"ubuntu" "Popular Ubuntu" OFF \
"centos" "Stable CentOS" OFF \
"mint" "Rising Star Mint" OFF 3>&1 1>&2 2>&3)
exitstatus=$?
if [ $exitstatus = 0 ]; then
    echo "The chosen distro is:" $DISTROS
else
    echo "You chose Cancel."
fi
```

## 🅱️ zenity

```shell
zenity --timeout=180 --notification --text "salam behrooooooooooooooz"
```

```shell
zenity --error --text="An error occurred\!" --title="Warning\!"
```

```shell
find /usr | zenity --progress --pulsate --auto-close --auto-kill --text="Working..."
```

```shell
zenity --question --text="Do you wish to continue/?"
```

```shell
zenity \
--info \
--text="<span size=\"xx-large\">Time is $(date +%Hh%M).</span>\n\nGet your <b>coffee</b>." \
--title="Coffee time" \
--ok-label="Sip"
```

```shell
my_variable=$(zenity --entry --text="What's my variable:")
echo $my_variable
```

```shell
zenity --calendar
```

## 🅱️ dialog

```shell
#!/bin/bash

HEIGHT=20
WIDTH=40
CHOICE_HEIGHT=10
BACKTITLE="Backtitle here"
TITLE="Title here"
MENU="Choose one of the following options:"

OPTIONS=(1 "Option 1"
         2 "Option 2"
         3 "Option 3")

CHOICE=$(dialog --clear \
                --backtitle "$BACKTITLE" \
                --title "$TITLE" \
                --menu "$MENU" \
                $HEIGHT $WIDTH $CHOICE_HEIGHT \
                "${OPTIONS[@]}" \
                2>&1 >/dev/tty)
clear
case $CHOICE in
        1)
            echo "You chose Option 1"
            ;;
        2)
            echo "You chose Option 2"
            ;;
        3)
            echo "You chose Option 3"
            ;;
esac
```

## 🅱️ Menu-DialogBlue

```shell
#/bin/bash
# by oToGamez
# www.pro-toolz.net

      E='echo -e';e='echo -en';trap "R;exit" 2
    ESC=$( $e "\e")
   TPUT(){ $e "\e[${1};${2}H";}
  CLEAR(){ $e "\ec";}
  CIVIS(){ $e "\e[?25l";}
   DRAW(){ $e "\e%@\e(0";}
  WRITE(){ $e "\e(B";}
   MARK(){ $e "\e[7m";}
 UNMARK(){ $e "\e[27m";}
      R(){ CLEAR ;stty sane;$e "\ec\e[37;44m\e[J";};
   HEAD(){ DRAW
           for each in $(seq 1 13);do
           $E "   x                                          x"
           done
           WRITE;MARK;TPUT 1 5
           $E "BASH SELECTION MENU                       ";UNMARK;}
           i=0; CLEAR; CIVIS;NULL=/dev/null
   FOOT(){ MARK;TPUT 13 5
           printf "ENTER - SELECT,NEXT                       ";UNMARK;}
  ARROW(){ read -s -n3 key 2>/dev/null >&2
           if [[ $key = $ESC[A ]];then echo up;fi
           if [[ $key = $ESC[B ]];then echo dn;fi;}
     M0(){ TPUT  4 20; $e "Login info";}
     M1(){ TPUT  5 20; $e "Network";}
     M2(){ TPUT  6 20; $e "Disk";}
     M3(){ TPUT  7 20; $e "Routing";}
     M4(){ TPUT  8 20; $e "Time";}
     M5(){ TPUT  9 20; $e "ABOUT  ";}
     M6(){ TPUT 10 20; $e "EXIT   ";}
      LM=6
   MENU(){ for each in $(seq 0 $LM);do M${each};done;}
    POS(){ if [[ $cur == up ]];then ((i--));fi
           if [[ $cur == dn ]];then ((i++));fi
           if [[ $i -lt 0   ]];then i=$LM;fi
           if [[ $i -gt $LM ]];then i=0;fi;}
REFRESH(){ after=$((i+1)); before=$((i-1))
           if [[ $before -lt 0  ]];then before=$LM;fi
           if [[ $after -gt $LM ]];then after=0;fi
           if [[ $j -lt $i      ]];then UNMARK;M$before;else UNMARK;M$after;fi
           if [[ $after -eq 0 ]] || [ $before -eq $LM ];then
           UNMARK; M$before; M$after;fi;j=$i;UNMARK;M$before;M$after;}
   INIT(){ R;HEAD;FOOT;MENU;}
     SC(){ REFRESH;MARK;$S;$b;cur=`ARROW`;}
     ES(){ MARK;$e "ENTER = main menu ";$b;read;INIT;};INIT
  while [[ "$O" != " " ]]; do case $i in
        0) S=M0;SC;if [[ $cur == "" ]];then R;$e "\n$(w        )\n";ES;fi;;
        1) S=M1;SC;if [[ $cur == "" ]];then R;$e "\n$(ifconfig )\n";ES;fi;;
        2) S=M2;SC;if [[ $cur == "" ]];then R;$e "\n$(df -h    )\n";ES;fi;;
        3) S=M3;SC;if [[ $cur == "" ]];then R;$e "\n$(route -n )\n";ES;fi;;
        4) S=M4;SC;if [[ $cur == "" ]];then R;$e "\n$(date     )\n";ES;fi;;
        5) S=M5;SC;if [[ $cur == "" ]];then R;$e "\n$($e by oTo)\n";ES;fi;;
        6) S=M6;SC;if [[ $cur == "" ]];then R;exit 0;fi;;
 esac;POS;done
```

# 🅰️ User

```shell
# ✅️Am I Root
if (( $(id -u) == 0 )); then
    echo "I'm root"
fi

# ✅️Get data from user
read -rep "Question here? " -i "Default answer" answer
echo "${answer}"
```

# 🅰️ JSON

```shell
cat test.json
#{"title":"Person","type":"object","properties":{"firstName":{"type":"string"},"lastName":{"type":"string"},"age":{"description":"Age in years","type":"integer","minimum":0}},"required":["firstName","lastName"]}

cat test.json | python -m json.tool
cat test.json | jq

```

# 🅰️ Shebang

```shell
# -*- coding: utf-8 -*-

# Or

#!/usr/bin/bash
# -*- coding: ascii -*-

# Or

#!/usr/bin/bash
# -*- coding: latin-1 -*-



#!/usr/bin/env
#!/bin/bash

#Notice
#1-[/usr/bin/env] bash is more portable than [/bin/bash]

#2-Avoid using #!/usr/bin/env bash -e (vs set -e),
#  because when someone runs your script as bash ./script.sh,
#  the exit on error will be ignored.

```

# 🅰️ Socket

```shell
# ✅️ Send
echo "behrooz" | socat - TCP4:127.0.0.1:1234
echo "behrooz" | socat - TCP:127.0.0.1:1234
echo "behrooz" | socat - TCP:127.0.0.1:1234

# ✅️ Listen.Recieve
socat - TCP-LISTEN:1234,reuseaddr,fork
socat - TCP4-LISTEN:1234,reuseaddr,fork
socat TCP-LISTEN:1234,reuseaddr,fork EXEC:"/tmp/salam/myscript.sh"
socat tcp-l:1234,reuseaddr,fork system:'cat >> /tmp/log.txt',nofork
socat - TCP-LISTEN:1234,reuseaddr,fork | tee -a /tmp/log.txt #سوکت TIME_WAIT بوجود میآورد و بعد از یک دقیقه آن را می‌بندد

# ✅️ ################################################LOCAL###########################
export Port="55055"
export ScriptName="02-Script.sh"

# ✅️ Listen
/usr/bin/nohup /usr/bin/socat TCP4-LISTEN:"$Port",reuseaddr,fork,ignoreeof,keepalive EXEC:$(/usr/bin/dirname "$0")/"$ScriptName" &
/usr/bin/nohup /usr/bin/socat TCP4-LISTEN:"$Port",reuseaddr,fork,ignoreeof,keepalive EXEC:/bin/MyScript.sh &

# ✅️ MyScript
read MESSAGE

peerServer="$SOCAT_PEERADDR"
peerSendServerIP=$PeerServer
peerSendServerIP=$SOCAT_PEERPORT

localRecieveServerIP=$SOCAT_SOCKADDR
localRecieveServerPort=$SOCAT_SOCKPORT
localParentPid=$SOCAT_PPID
localScriptPid:$$

# ✅️ ################################################LOCAL###########################

# ✅️ ################################################PEER###########################
#send
echo "check" | socat -t 3 - TCP:127.0.0.1:55055,connect-timeout=3
echo "$2" | socat -t $timeOut - TCP:$1:$Port,connect-timeout=$timeOut
# ✅️ ############################################PEER###########################

```


```shell
# sending:
echo "salam"|socat - TCP4:127.0.0.1:1234

listening:
socat tcp-l:1234,reuseaddr,fork system:'cat >> /tmp/log.txt',nofork
or
socat - TCP-LISTEN:1234,reuseaddr,fork |tee -a /tmp/log.txt
سوکت TIME_WAIT بوجود میآورد و بعد از یک دقیقه آن را می‌بندد



# listen:
socat - TCP-LISTEN:1234,reuseaddr,fork
socat - TCP4-LISTEN:1234,reuseaddr,fork


echo "behrooz"| socat -  TCP:localhost:1234
socat TCP-LISTEN:1234,reuseaddr,fork   EXEC:"/tmp/salam/myscript.sh"


# ###########################################
socat  TCP4-LISTEN:1234,reuseaddr,fork EXEC:/tmp/13980215/myscript.sh 
echo "behrooz"| socat -  TCP:localhost:1234

#!/bin/bash
read MESSAGE

if [[   "$MESSAGE" == "behrooz"  ]];then
	echo "I see behrooz";
else
	echo "Data:  $MESSAGE";
fi


```


```shell
####script summary
# Title: title
# Description: description
# Author: author <email>
# Date: yyyy-mm-dd
# Version: 1.0.0

# Exit codes
# ==========
# 0 no error
# 1 script interrupted
# 2 error description

# >>>>>>>>>>>>>>>>>>>>>>>> ExecuteOnRecieveDataFromSocket >>>>>>>>>>>>>>>>
read MESSAGE

if [[   "$MESSAGE" == "behrooz"  ]];then
    echo "I see behrooz";
else
    echo "Data:  $MESSAGE";
fi
# <<<<<<<<<<<<<<<<<<<<<<<< ExecuteOnRecieveDataFromSocket <<<<<<<<<<<<<<<<<<<<<<<<

# Listening
socat  TCP4-LISTEN:1234,reuseaddr,fork EXEC:/tmp/13980215/myscript.sh


```

# 🅰️ File

```shell
__dirname="$(cd "\)(dirname "${BASH_SOURCE[0]}")" && pwd)"
__filename="$(${__dirname})(basename "${BASH_SOURCE[0]}")"
__basename=$(basename "){BASH_SOURCE[0]}")

echo "DireName: $__dirname"
echo "BaseName: $__basename"
echo "FileName: $__filename"

# ✅️ Rename all files in a directory
ls | xargs -i mv {} {}.old

# ✅️ File.ReadLines
while read line; do
    # ← put the command that you want to run on each line here
done < <() # ← put the command that generates the lines you want to process inside the parentheses

# ✅️ Read line by line From text file
{
    while IFS= read -r "lineNum"; do
        echo "${lineNum}"
    done
} <"FILE_NAME"

# ✅️ File.write.multipleLines
#!/bin/bash
cat >"/path/to/file" <<EOF
first line
second line
...
EOF

# ✅️ File.write.multipleLines.sudoPermissionRequired
#!/bin/bash
cat <<EOF | sudo tee "/path/to/file" >/dev/null
first line
second line
...
EOF

# ✅️ File.CompressionOrDecompression
zip -rq /path/to/archive.zip /path/to/directory-or-file
tar -czvf /path/to/archive.tar.gz /path/to/directory-or-file
tar -cJf /path/to/archive.tar.xz /path/to/directory-or-file

unzip -q /path/to/archive.zip -d /extract/to/path
tar -C /extract/to/path -xzvf /path/to/archive.tar.gz
tar -C /extract/to/path -xf /path/to/archive.tar.xz


# ✅️ دستوری برای حذف کاراکترهای اضافی انتهای خط در اسکریپت‌های شل‌اسکریپت
# File.RemoveExtraCharacter
dos2unix <FileName>
```

# 🅰️ Exit

## 🅱️ Command.Exit.WhenFailed.EvenPipeline

```shell
set -o pipefail

#EXAMPLE
# >>>>>>>>>>>>>>>>>>>>>>>> Before >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
set -e
foo | echo "a"
echo "bar"

# [output]
# →
# → a
# → line 5: foo: command not found
# → bar


# >>>>>>>>>>>>>>>>>>>>>>>> After >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
set -eo pipefail
foo | echo "a"
echo "bar"

# [output]
# → a
# → line 5: foo: command not found
```

## 🅱️ Command.Exit.WhenFailed

```shell

set -o errexit
[or]
set -e


#EXAMPLE
# >>>>>>>>>>>>>>>>>>>>>>>> Before >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
foo
echo "bar"

#[output]
# → line 4: foo: command not found
# → bar

# >>>>>>>>>>>>>>>>>>>>>>>> After >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
set -e
foo
echo "bar"

#[output]
# → line 5: foo: command not found

# >>>>>>>>>>>>>>>>>>>>>>>> PreventImmediateExit >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
set -e
foo || true
echo "bar"

#[output]
# → line 5: foo: command not found
# → bar
````

## 🅱️ Exit.WhenUseUndeclaredVariables

```shell
set -o nounset
[or]
set -u

#EXAMPLE
# >>>>>>>>>>>>>>>>>>>>>>>> Before >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
set -e
echo $a
echo "bar"

# [output]
# →
# → bar


# >>>>>>>>>>>>>>>>>>>>>>>> After >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
set -eu
echo $a
echo "bar"

# [output]
# → line 5: a: unbound variable
```

## 🅱️ Exit event handler

```shell
function on_exit() {
    tput cnorm          # Show cursor. You need this if animation is used.
                        # i.e. clean-up code here
    exit 0              # Exit gracefully.
}

# Put this line at the beginning of your script (after functions used by event handlers).
# Register exit event handler.
trap on_exit EXIT

```

# 🅰️ Math

```shell
# add two variables
result=$((int1 + int2))

# increment integer variable by 1
((int++)) #→  such as ((x++))
((++int))
((x+=5))  #→  افزودن عدد ۵ به عدد
# add int1 and int2 and assign the result to int1
((int1 += int2))

# exponentiate base to power
result=$((base ** power)) [or] echo $RANDOM



# EXPR
result=\((expr \){int1} + ${int2})
result=expr 1 + 1 #result: 2
```

# 🅰️ Code and Decode

```shell
# -*- coding: utf-8 -*-
# Or
# -*- coding: ascii -*-
# Or
# -*- coding: latin-1 -*-

# Encod.Hash
hash=\((echo -n "\)variableToHash" | md5sum | cut -f1 -d ' ')

# Encode.base64
base64Encoded=$(echo -n "String" | base64)

#  Decode.base64
base64Encoded=$(echo -n "String" | base64)
base64Decoded=$(echo -n "<Hash>" | base64 -d)

Decode_CodeToString() {
    Code=$1
    local msg=\((base64 -d <<<"\)Code")
}
```

# 🅰️ Debugging

```shell
set -o xtrace
[or]
set -x

#EXAMPLE
# >>>>>>>>>>>>>>>>>>>>>>>> Before >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
set -x
a=5
echo $a
echo "bar"

# [output]
# → + a=5
# → + echo 5
# → 5
# → + echo bar
# → bar

```

# 🅰️ mapfile

```shell
diskGetAllDisksWWN() {
    # [https://github.com/koalaman/shellcheck/wiki/SC2207]
    # روش اول
    mapfile -t Disks < <(find /dev/disk/by-id/wwn* -print0 | xargs -0 -n1 basename | awk -F '-part' '{print $1}' | sort | uniq) # خروجی دستورات توسط خط جدید از هم جدا شده است
    echo "${Disks[@]}"

    # روش دوم
    # cd "/dev/disk/by-id" || exit 1
    # Disks=($(find ./wwn* | tr -d './' | awk -F '-part' '{print $1}' | sort | uniq))
    # echo "${Disks[@]}"
}

#دو دستور زیر یکسان هستند
IFS=" " read -r -a all <<<"$(diskGetAllDisksWWN)" #آرایه با فاصله از هم جدا شده اند
all=($(diskGetAllDisksWWN))

```

# 🅰️ Event.Handler.CTRL_C

```shell
#!/bin/bash
# register a function (handler) to run on script termination (CTRL+C)
# CTRL+C event handler
function on_ctrl_c() {
    echo                # Set cursor to the next line of '^C'
    tput cnorm          # show cursor. You need this if animation is used.
                        # i.e. clean-up code here
    exit 1              # Don't remove. Use a number (1-255) for error code.
}

# Put this line at the beginning of your script (after functions used by event handlers).
# Register CTRL+C event handler
trap on_ctrl_c SIGINT
```

# 🅰️ time

```shell
# ✅️ system uptime. -p: --pretty, -s: since
systemUptime=$(uptime -p)
echo "${systemUptime}"

# ✅️ system uptime in seconds.
systemUptime=$(awk '{print $1}' /proc/uptime)
echo "${systemUptime}"

# ✅️ Convert time
timeNowSecondsEpoch=$(date +%s) #seconds since epoch (1970-01-01 00:00:00)
timeNowLocal=$(date +%R)        #current local time (R: 24hrs, r: 12hrs)
timeNowUTC=$(date -u +%R)       #current UTC time

# ✅️ Usage: formatSeconds 70 -> 1m 10s
# Credit: https://unix.stackexchange.com/a/27014
function formatSeconds {
    local T=$1
    local D=$((T / 60 / 60 / 24))
    local H=$((T / 60 / 60 % 24))
    local M=$((T / 60 % 60))
    local S=$((T % 60))
    local result=""

    ((D > 0)) && result="${D}d "
    ((H > 0)) && result="\({result}\){H}h "
    ((M > 0)) && result="\({result}\){M}m "
    ((S > 0)) && result="\({result}\){S}s "
    echo -e "\({result}" | sed -e 's/[[:space:]]*\)//'
}

```

# 🅰️

# 🅰️

# 🅰️

# 🅰️ 