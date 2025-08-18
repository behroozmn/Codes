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
