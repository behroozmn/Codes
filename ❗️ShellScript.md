# 🅰️ String



```shell
myCustomString="  Behrooz Mohammadi Nasab Sahzabi  "

lowercase="${myCustomString,,}"  # behrooz mohammadi nasab sahzabi
uppercase="${myCustomString^^}"  # BEHROOZ MOHAMMADI NASAB SAHZABI
```





# 🅰️ condition

* `[ condition ] || command` if condition is false then run command
* `[ condition ] && command` if condition is true then run command

| #         | title                            | sample                                      | Description                                                  |
|-----------|----------------------------------|---------------------------------------------|--------------------------------------------------------------|
| -s        | Condition.File.Notempty          |                                             |                                                              |
| -r        | Condition.File.Readalbe          |                                             |                                                              |
| -w        | Condition.File.writealbe         |                                             |                                                              |
| -ot       | Condition.if.File1OlderThanFile2 | `[ "/path/to/file1" -ot "/path/to/file2" ]` |                                                              |
| -nt       | Condition.if.File1NewerThanFile2 | `[ "/path/to/file1" -nt "/path/to/file2" ]` | check if file1 is newer than file2                           |                         
| =         | Condition.if.evaluating          | `[ "${NAME}" = "Kevin" ]`                   | از دو علامت مستاوی استفاده نکنید                             |                        
| (( ... )) | Condition.if.evaluating_Integers |                                             | Use (( ... )) rather than [[ ... ]] when evaluating integers |

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

# 🅰️ DataBase

```shell
mysql -u root -p1234567890  -h localhost -e "USE sadrsds;SELECT * FROM raiddisk;"
mysql -u root -p1234567890 "sadrsds" -h localhost -e "SELECT * FROM raiddisk;"
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
