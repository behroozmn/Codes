# fun Comamnds

```shell
1-while true; do echo "$(date '+%D %T' | toilet -f term -F border --gay)"; sleep 1; done #نمایش زمان در حالت ترمینال
2- :(){ :|: & };:   #ForkBomb
3-rev behrooz #برگرداندن متن
4-cowsay
```

# sleep

انتظار در خط فرمان

```shell
sleep 1000 #توقف یک ثانیه
sleep 10m  #توقف ده دقیقه

```

# paste

```shell
```

# ImageMagic|convert

برنامه‌ای برای ادیت عکس توسط خط فرمان

```shell
convert <input.png> <output.jpg>
convert <input.png> -resize 50% <output.jpg> #کاهش ۵۰درصدی طول و عرض عکس
```

# Mplayer

برنامه‌ای برای اجرای فایل صوتی در خط فرمان


# WINOWS

## yad

نمایش یک پنجره به سبک برنامه نویسی ویژوال:

`echo My text | yad --text-info --width=400 --height=200 `

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

## Whiptail

اگر بخواهیم در یک متن با خاصیت بلی ویا خیر در قلب ترمینال نمایش شود (همانند ok و Cancell در حین نصب آپاچی) از دستور زیر استفاده می‌نماییم:

`whiptail --title "<message box title>" --msgbox "<text to show>" <height> <width>`

[url1](https://unix.stackexchange.com/questions/144924/how-to-create-a-message-box-from-the-command-line)
[url2](https://stackoverflow.com/questions/7035/how-to-show-a-gui-message-box-from-a-bash-script-in-linux)
[url3](http://linux.byexamples.com/archives/265/a-complete-zenity-dialog-examples-2)
[url4](https://www.howtogeek.com/107537/how-to-make-simple-graphical-shell-scripts-with-zenity-on-linux)
[url5](http://jamesslocum.com/post/55694754191)
[url6](http://xmodulo.com/create-dialog-boxes-interactive-shell-script.html)

### [Yes/No]Box

`whiptail --title "<dialog box title>" --yesno "<text to show>" <height> <width>`

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

`whiptail --title "<checklist title>" --checklist "<text to show>" <height> <width> <list height> [ <tag> <item> <status> ] . . .`

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

`whiptail --title "<input box title>" --inputbox "<text to show>" <height> <width> <default-text>`

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

`whiptail --title "<menu title>" --menu "<text to show>" <height> <width> <menu height> [ <tag> <item> ] . . .`

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

`whiptail --title "<message box title>" --msgbox "<text to show>" <height> <width>`

```shell
#!/bin/bash
whiptail --title "Test Message Box" --msgbox "Create a message box with whiptail. Choose Ok to continue." 10 60
```

### PasswordBox

`whiptail --title "<password box title>" --passwordbox "<text to show>" <height> <width>`

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

`whiptail --gauge "<test to show>" <height> <width> <inital percent>`

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

`whiptail --title "<radiolist title>" --radiolist "<text to show>" <height> <width> <list height> [ <tag> <item> <status> ] . . .`

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

## zenity

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