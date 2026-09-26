<div style="direction: rtl">

# 1. 🅰️ Desktop Environments

* GTK: فریم‌ورک برای توسعه رابط کاربری گرافیکی (GUI) در برنامه‌های نرم‌افزاری هستند
    * عمدتاً با زبان C توسعه یافته است
    * بیشتر بر روی لینوکس و سیستم‌عامل‌های مبتنی بر UNIX متمرکز است، از طراحی متریال و GNOME پیروی می‌کند و بیشتر برای برنامه‌های دسکتاپ GNOME استفاده می‌شود.
    * نیز دارای ابزار طراحی گرافیکی به نام Glade است که به توسعه‌دهندگان کمک می‌کند تا رابط‌های کاربری را طراحی کنند.
    * تحت مجوز LGPL منتشر شده است.
    * کتابخانه‌های PyGTK و PyGObject برای زبان پایتون و کتابخانه PHP-GTK برای زبان PHP و کتابخانه gtkmm برای زبان ++C و غیره در دسترس است

# 2. 🅰️ Environment or Variables

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

## 2.1. 🅱️ IFS

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

## 2.2. 🅱️ @|*

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

## 2.3. 🅱️ HISTORY

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

### 2.3.1. ✅️ TTY|PTS

- TTY: شخصی مستقیم بصورت interactive بر سر سیستم لاگین کرده است
- PTS: تریمنال باز شده در محیط گرافیکی
- برنامه tmux هماننده اسکرین است و در هر بش می‌توان ویندوز خود را مشاهده نمود

```shell
tty #output:/dev/pts/4
write <username> <[pts/0] or [pts/1]> #Ending with CTRL+D #ارسال نوشته به یک ترمینال دیگر
# Example: write user /dev/pts/0
who -a #فهمیدن کاربران و ترمینال‌ها
```

## 2.4. 🅱️ tput

- Tput: دستوری که دیتا پیرامون بش به ما میدهد
- initialize a terminal or query terminfo database

```shell
tput lines # نمایش تعداد خط‌های یک شل که هم‌اکنون باز است
tput cols # نمایش تعداد ستون‌های(اشاره به کاراکتر دارد) یک شل که هم‌اکنون باز است
```

## 2.5. 🅱️ Clipboard

ارسال خروجی به حافظه clipBoard

```shell
[MicrosoftWindows] ipconfig | clip
Terminal: Command | xclip -selection clipboard

```

## 2.6. 🅱️ eval

یک دستور داخلی (Builtin) است که مکانیسم اجرای آن بر پایه «پردازش دو مرحله‌ای» (Two-Pass Execution) بنا شده است. وقتی شما دستوری را در شل اجرا می‌کنید، شل معمولاً یک بار آن را تجزیه (Parse) و اجرا می‌کند. اما وقتی از eval استفاده می‌کنید، شل مراحل زیر را طی می‌کند:

1. مرحله اول (بسط اولیه):
    * گام اول: eval تمام آرگومان‌های ورودی خود را با یک فاصله (Space) به هم می‌چسباند تا یک رشته واحد بسازد.
    * گام اول: بسط‌های استاندارد شل (مانند بسط متغیرها `$VAR`، جایگزینی دستور `$(cmd)`، و بسط حسابی) را روی این رشته انجام می‌دهد.
2. . مرحله دوم (تجزیه و اجرای نهایی): رشته حاصل از مرحله اول، مجدداً به عنوان یک خط دستور کامل شل به موتور تجزیه‌کننده (Parser) شل فرستاده می‌شود.
    * در این مرحله،مواردی که درون رشته بودند و نیاز به تجزیه و تحلیل دارند شناسایی و اجرا می‌شوند نظیر موارد زیر
        * لوله‌کشی‌ها یا همان پایپ‌ها (Pipes |)
        * تغییر مسیرها (Redirections >)
        * عملگرهای منطقی (&&, ||)

کاربرد فنی: eval زمانی استفاده می‌شود که شما نیاز دارید یک رشته متنی که حاوی ساختارهای کنترلی شل (مثل |, >, &&) یا بسط‌های تودرتو است را اجرا کنید، زیرا اجرای مستقیم یک متغیر حاوی دستور (مثلاً $CMD) توسط شل، ساختارهای کنترلی درون آن را به عنوان متن ساده در نظر می‌گیرد و آن‌ها را Parse نمی‌کند.

* با توجه به خطرات eval، صنعت نرم‌افزار تا حد امکان از آن اجتناب می‌کند
* در شل اسکریپت بهتر است بجای استفاده از eval با استفاده از آرایه نیاز خود را کفایت کنید
    * ❌ `eval rsync $FLAGS`
    * ✅ استفاده زا دو دستور زیر پشت‌سر هم
        * `CMD=(rsync "${FLAGS[@]}")`
        * `"${CMD[@]}"`
* اگر یک دستور شامل لوله `|` یا تغییر مسیر `>` را در یک متغیر ذخیره کنید، اجرای مستقیم آن `$CMD` کار نمی‌کند. eval آن را Parse می‌کند.
* خواندن فایل‌های تنظیمات `.env` که شامل خطوط KEY=VALUE هستند و تبدیل آن‌ها به متغیرهای شل.

### 2.6.1. ✅️example1: Dynamic Variable Assignment

در اسکریپت‌های شل، گاهی اوقات نیاز دارید متغیرهایی با نام‌های پویا بسازید (مثلاً در یک حلقه). eval تنها راه مستقیم و ساده برای این کار بدون استفاده از آرایه‌های پیچیده است. در مثال زیر می‌خواهیم ۳ متغیر به نام‌های server1_ip, server2_ip, server3_ip بسازیم

```shell
for i in 1 2 3; do
    # استفاده از eval برای ساخت پویای نام متغیر و مقداردهی به آن
    eval "server${i}_ip='192.168.1.${i}0'"
done

# حالا متغیرها ساخته شده‌اند
echo $server1_ip  # خروجی: 192.168.1.10
echo $server2_ip  # خروجی: 192.168.1.20
```

### 2.6.2. ✅️example2: Nested Quotes on SSH commands

وقتی می‌خواهید یک دستور را از طریق SSH روی سرور راه دور اجرا کنید و آن دستور خودش دارای آرگومان‌هایی با فاصله (Space) و نقل‌قول است. در این هنگام اگر مستقیم دستور دارای فاصله را اجرا کنید، به دلیل فاصله‌ها و نقل‌قول‌های تودرتو خطا می‌دهد. پس باید توسط eval استفاده گردد که در این صورت دستور eval رشته را یک بار دیگر Parse می‌کند و نقل‌قول‌ها را به
درستی برای SSH و grep تفسیر می‌کند

```shell
REMOTE_HOST="admin@server.com"
FILE_PATH="/var/log/my app logs/app.log" # دارای فاصله است
GREP_PATTERN="Error: Connection failed"   # دارای فاصله است

CMD="ssh $REMOTE_HOST \"grep '$GREP_PATTERN' '$FILE_PATH'\"" # ❌ : سبب بروز خطا می‌شود
eval $CMD # ✅️
```

### 2.6.3. ✅️example3: Environment ► .env

فرض کنید فایل .env شامل خطوطی مثل DB_PASS=12345 است. این دستور خطوط کامنت شده را حذف کرده و بقیه را به عنوان متغیر شل اجرا می‌کند

```shell
eval $(grep -v '^#' .env | xargs)
echo "Database password is: $DB_PASS"
```

### 2.6.4. ✅️example4: ساخت پویای دستورهای پیچیده

```shell
CMD="rsync -avz"
if [ "$COMPRESS" = "true" ]; then
    CMD="$CMD --compress"
fi

eval $CMD /source/ /destination/ # اجرای دستور ساخته شده با حفظ ساختار آرگومان‌ها
```

### 2.6.5. ✅️example5: جایگذاری متغیرها در قالب‌ها

فرض کنید داخل فایل `welcome_template.txt` رشته `Welcome $USER_NAME to $SERVER_IP` قرار دارد. در اینصورت اجرای eval برای جایگذاری متغیرهای واقعی شل در رشته کاربرد پیدا خواهد کرد

```shell
USER_NAME="Admin"
SERVER_IP="192.168.1.1"


TEMPLATE=$(cat welcome_template.txt) # خواندن تمپلیت از فایل
eval echo \"$TEMPLATE\"

# OUTPUT: Welcome Admin to 192.168.1.1
```

### 2.6.6. ✅️example6:

```shell
#!/bin/bash
CMD="ps aux | grep 'sshd' | grep -v grep > /tmp/sshd_procs.txt"

# $CMD ❌
 
eval "$CMD" # ✅️ use eval for analize  Pipe و Redirection
echo "Processes saved to /tmp/sshd_procs.txt"
```

### 2.6.7. ✅️example7:  Parsing .env

فرض کنید فایل config.env شامل خطوطی مثل DB_HOST=localhost است. در مثال زیر دستور grep کامنت‌ها را حذف کرده و eval آن‌ها را به عنوان مقداردهی متغیر اجرا می‌کند

```shell
#!/bin/bash
eval $(grep -v '^#' config.env | xargs) 
echo "Database Host is: $DB_HOST"
```

### 2.6.8. ✅️example8: Indirect Variable Expansion

دسترسی به مقدار یک متغیر، در حالی که نام آن متغیر در یک متغیر دیگر ذخیره شده است. در مثال زیر ما می‌خواهیم مقدار USER_NAME را چاپ کنیم، اما نام آن در target_var است. پس توسط دستور eval ابتدا $target_var را به USER_NAME تبدیل می‌کند، سپس \$USER_NAME را اجرا می‌کند

```shell
#!/bin/bash
target_var="USER_NAME"
USER_NAME="Administrator"
 
eval echo \$$target_var
# OUTPUT: Administrator
```

### 2.6.9. ✅️example9: Dynamic Function Generation

ساخت و اجرای پویای توابع در حلقه: تولید توابع تکراری در زمان اجرا (Runtime) بر اساس یک لیست.

```shell
#!/bin/bash
services=("nginx" "mysql" "redis")

for svc in "${services[@]}"; do
    # ساخت پویای کد تابع به صورت رشته
    func_code="check_${svc}() { systemctl status ${svc} | grep 'active (running)'; }"
    
    eval "$func_code" # رشته را تجزیه کرده و تابع را در حافظه شل ثبت می‌کند
done

check_nginx # حالا توابع ساخته شده‌اند و قابل اجرا هستند
```

### 2.6.10. ✅️example10: Dynamic Array Indexing

دسترسی پویا به اندیس‌های آرایه: خواندن مقدار یک آرایه وقتی که شماره اندیس در یک متغیر دیگر است.

```shell
#!/bin/bash
my_array=("apple" "banana" "cherry" "date")
index=2

eval val=\${my_array[$index]} # متغیر ایندکس را جایگذاری کرده و سپس آرایه را پارس می‌کند

echo "The fruit at index $index is: $val"
# OUTPUT: cherry
```

### 2.6.11. ✅️example11:

اجرای دستورات پیچیده و Quote-دار از طریق SSH: وقتی می‌خواهید دستوری را روی سرور راه دور اجرا کنید که خودش دارای آرگومان‌های Quote-دار است.

```shell
#!/bin/bash
REMOTE_HOST="admin@192.168.1.10"
REMOTE_CMD="grep 'ERROR' '/var/log/my app/server.log' | wc -l"

eval ssh "$REMOTE_HOST" "\"$REMOTE_CMD\"" # ابتدا متغیرها را بسط می‌دهد و سپس کل دستور «اس اس اچ» را با حفظ ساختار نقل‌قول‌ها اجرا می‌کند
```

### 2.6.12. ✅️example12: Interactive Shell

فرض کنید در ترمینال لینوکس هستید و می‌خواهید یک رشته که شامل && (عملگر منطقی) و > (تغییر مسیر) است را مستقیماً اجرا کنید، بدون اینکه آن را در متغیری ذخیره کنید.

```shell
eval "date '+%Y-%m-%d %H:%M:%S' > /tmp/current_time.txt && cat /tmp/current_time.txt"
```

1. شما رشته را مستقیماً به eval می‌دهید
2. eval رشته را دریافت کرده و به Parser شل می‌فرستد.
3. Parser شل، عملگر > را شناسایی کرده و خروجی date را به فایل منتقل می‌کند.
4. سپس عملگر && را شناسایی کرده و پس از موفقیت دستور اول، دستور cat را اجرا می‌کند.

نکته: اگر این رشته را بدون eval و فقط به صورت یک متغیر اجرا می‌کردید، شل > و && را به عنوان بخشی از آرگومان‌های دستور در نظر می‌گرفت و عملگرها کار نمی‌کردند. eval به تنهایی این گره را باز می‌کند

# 3. 🅰️ Files

## 3.1. 📁️ ~/.bash_aliases

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

# 4. 🅰️Shortcuts

* Shift+F10:  راست کلیک
* Alt+F8: Resize
* Alt+space: RightClick(Outer)
* super+f10: RightClick(Tray)
*
* Alt+F7: Move

## 4.1. 🅱️Terminal Shortcuts

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

## 4.2. 🅱️Gnome

* Alt+Ctrl+Shift+R: ScreenShot
* Shift+Super+<>: Workspace(Move Window Into Workspace2)

</div>