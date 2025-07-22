# 📍️ Environment or Variables

```shell
printenv # نمایش
printenv NAME # نمایش یک موردخاص
set # نمایش
env # متغیرهایی که بصورت پیش‌فرض شل آنها را مقدار دهی می‌کند با این دستور قابل نمایش است
echo $NAME
echo $FUNCNAME # نام تابع که در خط کنونی در حال اجرا است
echo $HOSTNAME # نام هاست
echo $$ # PID
echo $_ # Note: آرگومان ورودی دستور قبل
```

## IFS

مواردی که شل بعنوان جداکننده در نظر خواهد گرفت

- نکته: اگر بخواهیم که بش تنها خط جدید را بعنوان جدا کننده در نظر بگیرد باید حتما یک دالر قبل عبارت قرار دهیم

```shell
#!/bin/bash
IFS=':'
name="Behroox:Ali:Reza:Zeinab:Mohamad"
for i in $name; do #به هیچ عنوان داخل کوتیشن نگذارید # Qoute
echo "Hello $i"
done
```

## @|*

- هردوی کاراکترهای @ یا * تمامی آرگومان‌های ورودی یک اسکریپت را برمی‌گرداند
- تفاوت: در حلقه @ به دفعات اجرا می‌شود ولی در * حلقه تنها یکبار اجرا می‌شود

**حالت استفاده از @**: در زمان استفاده عناصر حلقه به دفعات تکرار می‌شود

```shell
vim /tmp/test1.sh
#!/bin/bash
for x in "$@";do # 
echo "Hello $x"
done

/tmp/test1.sh Mohamad Ali Fatemeh Hassan Hossein

output:
Hello Mohamad
Hello Ali
Hello Fatemeh
Hello Hassan
Hello Hossein
```

حالت استفاده از *: در زمان استفاده عناصر حلقه تنها یک بار برای همه تکرار می‌شود

```shell
vim /tmp/test2.sh
#!/bin/bash
for x in "$*";do
 echo "Hello $x"
done

/tmp/test2.sh Mohamad Ali Fatemeh Hassan Hossein
output:
 Hello Mohamad Ali Fatemeh Hassan Hossein
```

## HISTORY

* HISTSIZE: is the number of lines or commands that are stored in memory in a history list while your bash session is ongoing.
* HISTFILESIZE: is the number of lines or commands that (a) are allowed in the history file at startup time of a session, and (b) are stored in the history file at the end of your bash session for use in future sessions.

- Example 1: HISTFILESIZE=10 and HISTSIZE=10
    1. You start your session
    2. Your HISTFILE (file that stores your bash command history), is truncated to contain HISTFILESIZE=10 lines
    3. You write 50 lines
    4. At the end of your 50 commands, only commands 41 to 50 are in your history list, whose size is determined by HISTSIZE=10
    5. You end your session
    6. Assuming histappend is not enabled, commands 41 to 50 are saved to your HISTFILE which now has the 10 commands it held at the beginning plus the 10 newly written commands
    7. Your HISTFILE is truncated to contain HISTFILESIZE=10 lines
    8. You now have 10 commands in your history - the last 10 that you just typed in the session you just finished
    9. When you start a new session, you start over at step 1 with a HISTFILE of HISTFILESIZE=10
- Example 2: HISTFILESIZE=10 and HISTSIZE=5
    1. You start your session
    2. Your HISTFILE (file that stores your bash command history), is truncated to contain at most HISTFILESIZE=10 lines
    3. You write 50 lines
    4. At the end of your 50 commands, only commands 46 to 50 are in your history list, whose size is determined by HISTSIZE=5
    5. You end your session
    6. Assuming histappend is not enabled, commands 46 to 50 are saved to your HISTFILE which now has the 10 commands it held at the beginning plus the 5 newly written commands
    7. Your HISTFILE is truncated to contain HISTFILESIZE=10 lines
    8. You now have 10 commands in your history - 5 from a previous session and the last 5 that you just typed in the session you just finished
    9. When you start a new session, you start over at step 1 with a HISTFILE of HISTFILESIZE=10
- Example 3: HISTFILESIZE=5 and HISTSIZE=10
    1. You start your session
  2. Your HISTFILE (file that stores your bash command history), is truncated to contain at most HISTFILESIZE=5 lines
  3. You write 50 lines
  4. At the end of your 50 commands, only commands 41 to 50 are in your history list, whose size is determined by HISTSIZE=10
  5. You end your session
  6. Assuming histappend is not enabled, commands 41 to 50 are saved to your HISTFILE which now has the 5 commands it held at the beginning plus the 10 newly written commands
  7. Your HISTFILE is truncated to contain HISTFILESIZE=5 lines
  8. You now have 5 commands in your history - the last 5 that you just typed in the session you just finished
  9. When you start a new session, you start over at step 1 with a HISTFILE of HISTFILESIZE=5

# 📍️ TTY|PTS

- TTY: شخصی مستقیم بصورت interactive بر سر سیستم لاگین کرده است
- PTS: تریمنال باز شده در محیط گرافیکی
- برنامه tmux هماننده اسکرین است و در هر بش می‌توان ویندوز خود را مشاهده نمود

```shell
tty #output:/dev/pts/4
write <username> <[pts/0] or [pts/1]> #Ending with CTRL+D #ارسال نوشته به یک ترمینال دیگر
# Example: write user /dev/pts/0
who -a #فهمیدن کاربران و ترمینال‌ها
```

# 📍️ tput

- Tput: دستوری که دیتا پیرامون بش به ما میدهد
- initialize a terminal or query terminfo database

```shell
tput lines # نمایش تعداد خط‌های یک شل که هم‌اکنون باز است
tput cols # نمایش تعداد ستون‌های(اشاره به کاراکتر دارد) یک شل که هم‌اکنون باز است
```

# 📍️ Clipboard

ارسال خروجی به حافظه clipBoard

```shell
[MicrosoftWindows] ipconfig | clip
Terminal: Command | xclip -selection clipboard

```

# 📍️ Files

## 📌️ bash_aliases

```shell
alias ifconfig='/sbin/ifconfig'
alias apt='sudo apt'
alias nmap='sudo nmap'
alias nmapT='sudo nmap -T5'
alias shutdown='sudo shutdown'
alias updatedb='sudo updatedb'
alias b_killOutputMessengers='kill -9 $(pidof OutputMessenger)'
alias b_Busy="cat /dev/urandom | hexdump -C | grep --color=auto -E 'aa|bb|cc|dd|ee|ff'"
alias b_GenPasswd="strings /dev/urandom | grep -o '[[:alnum:]]' | head -n 30 | tr -d '\n'; echo"
alias b_ipAll='ip addr list |column -t|grep -E "\." |awk "{print \$2}"'
alias b_ipPublic='curl -s http://ip.jsontest.com|jq .ip|tr -d "\""' #dependency: jq, curl
alias b_ipPublic2='curl -s ifconfig.me'
alias b_logDmesg='sudo dmesg -Tx  --follow'
alias b_mount="mount | column -t"
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias mv='mv -i'
alias cp='cp -i' #prompt before overwrite
alias dir='dir --color=auto'
alias grep='grep --color=auto'
alias ll="ls --color -al"
alias ls="ls --color=auto"
alias ps?="ps aux | grep"
b_backup() {
    _time=$(date +%Y%m%d-%H%M%S)
    cp "$1"{,.bak_$_time}
}
cls() {
    cd "$1"
    ls
}
mcd() {
    mkdir -p "$1"
    cd "$1"
}
b_7z() { 7z -mx9 a data.7z "$1"; }
alias chgrp='chgrp --preserve-root' # Parenting changing perms on /
alias chmod='chmod --preserve-root' # Parenting changing perms on /
alias chown='chown --preserve-root' # Parenting changing perms on /
alias rm='rm -I --preserve-root'
alias b_ScanPort_1-1000_open='nc -vv -z localhost 1-1000 2>&1 | grep open'
alias b_DeleteDirOnTMP='mkdir /tmp/DeletedFiles'
alias b_Chk_Duplicate='fdupes -R .'

alias echoColorize='echo -e "${NOCOLOR}Nocolor ${RED}Red ${GREEN}Green ${ORANGE}Orange ${BLUE}Blue ${PURPLE}Purple ${YELLOW}Yellow ${CYAN}Cyan ${LIGHTGRAY}LightGray ${DARKGRAY}DarkGray ${LIGHTRED}LightRed ${LIGHTGREEN}LightGreen ${LIGHTBLUE}LightBlue ${LIGHTPURPLE}LightPurple ${LIGHTCYAN}LightCyan ${WHITE}White ${NOCOLOR}Nocolor"'

NOCOLOR='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
LIGHTGRAY='\033[0;37m'
DARKGRAY='\033[1;30m'
LIGHTRED='\033[1;31m'
LIGHTGREEN='\033[1;32m'
YELLOW='\033[1;33m'
LIGHTBLUE='\033[1;34m'
LIGHTPURPLE='\033[1;35m'
LIGHTCYAN='\033[1;36m'
WHITE='\033[1;37m'

```



# 📍️ Commands

## ✅️ yad

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

## ✅️ Whiptail

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

### [Yes/No]Box

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

### ChecklistDialog

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

### FormInput

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

### MenuBox

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

### MessageBox

```shell
whiptail --title "<message box title>" --msgbox "<text to show>" <height> <width>
```

```shell
#!/bin/bash
whiptail --title "Test Message Box" --msgbox "Create a message box with whiptail. Choose Ok to continue." 10 60
```

### PasswordBox

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

### ProgressBar

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

### RadiolistDialog

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

## ✅️ zenity

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
