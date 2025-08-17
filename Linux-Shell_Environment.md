# 🅰️ Desktop Environments

* GTK: فریم‌ورک برای توسعه رابط کاربری گرافیکی (GUI) در برنامه‌های نرم‌افزاری هستند
    * عمدتاً با زبان C توسعه یافته است
    * بیشتر بر روی لینوکس و سیستم‌عامل‌های مبتنی بر UNIX متمرکز است، از طراحی متریال و GNOME پیروی می‌کند و بیشتر برای برنامه‌های دسکتاپ GNOME استفاده می‌شود.
    * نیز دارای ابزار طراحی گرافیکی به نام Glade است که به توسعه‌دهندگان کمک می‌کند تا رابط‌های کاربری را طراحی کنند.
    * تحت مجوز LGPL منتشر شده است.
    * کتابخانه‌های PyGTK و PyGObject برای زبان پایتون و کتابخانه PHP-GTK برای زبان PHP و کتابخانه gtkmm برای زبان ++C و غیره در دسترس است


# 🅰️ Environment or Variables

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

## 🅱️ IFS

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

## 🅱️ @|*

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

## 🅱️ HISTORY

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

### ✅️ TTY|PTS

- TTY: شخصی مستقیم بصورت interactive بر سر سیستم لاگین کرده است
- PTS: تریمنال باز شده در محیط گرافیکی
- برنامه tmux هماننده اسکرین است و در هر بش می‌توان ویندوز خود را مشاهده نمود

```shell
tty #output:/dev/pts/4
write <username> <[pts/0] or [pts/1]> #Ending with CTRL+D #ارسال نوشته به یک ترمینال دیگر
# Example: write user /dev/pts/0
who -a #فهمیدن کاربران و ترمینال‌ها
```

## 🅱️ tput

- Tput: دستوری که دیتا پیرامون بش به ما میدهد
- initialize a terminal or query terminfo database

```shell
tput lines # نمایش تعداد خط‌های یک شل که هم‌اکنون باز است
tput cols # نمایش تعداد ستون‌های(اشاره به کاراکتر دارد) یک شل که هم‌اکنون باز است
```

## 🅱️ Clipboard

ارسال خروجی به حافظه clipBoard

```shell
[MicrosoftWindows] ipconfig | clip
Terminal: Command | xclip -selection clipboard

```

# 🅰️ Files

## 📁️ ~/.bash_aliases

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




# 🅰️ Terminal Shortcuts


* [Ctrl+A]:jump to start of the line
* [Ctrl+E:]:jump to end of the line
* [Escape+B][Alt+B]:jump Backward by a word(left word)
* [Escape+F]+[Alt+F]:jump Forward by a word(right word)
* [CTRL+B]:move backward by a char
* [CTRL+F]:move forward by a char
* [CTRL+W]:remove the word backwards from cursor position
* [CTRL+Y]:paste text from the kill buffer
* [CTRL+R]:reverse search for commands you typed in the past from your history.
* [CTRL+S]:forward search (works in ZSH for me but not bash)
* [Ctrl+D]: حذف کاراکتر در موقعیت مکان نما
* [Ctrl+T]: جابجا کردن و مبادله کاراکتر در موقعیت مکان نما با کاراکتر قبلی
* [Alt+T]: جابجا کردن کلمه در موقعیت مکان نما به کلمه قبلی
* [Alt+L]: تبدیل کاراکترها از موقعیت مکان نما تا آخر کلمه
* [Alt+U]: تبدیل کاراکترها از موقعیت مکان نما تا آخر کلمه به حروف بزرگ
* برش وچسباندن
* [CTRL+K]:kill the line starting from the cursor position
* [CTRL+U]: حذف متن از موقعیت مکان نما تا اول خط
* [ALT+D]:delete a word starting from the current cursor position
* [Alt+Backspace]: حذف متن از موقعیت مکان نما تا ابتدای کلمه اخیر. اگر مکان نما در اول یک کلمه باشد کلمه قبلی حذف خواهد شد
* [Ctrl+Y]: برش متن از کلیپ‌بورد و درج در موقعیت مکان نما