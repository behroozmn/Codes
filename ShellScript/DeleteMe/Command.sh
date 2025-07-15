
- Indention: در شل اسکریپت به هیچ عنوان از تب استفاده نشود و تنها از اسپیس استفاده شود و اگر بخواهیم بحث indentation را رعایت نماییم از دو اسپیس استفاده مینماییم
- Note: فرق sh و bash این است که گاهی ممکن است لینوکس آنقدر کوچک شده باشد که برنامه bash را نداشته باشد و تنها یک شل Customشده کوچک داشته باشد و این شل توسط دستور sh شناخته می شود و در این صورت اگر بجای /bin/sh عبارت /bin/bash قرار بدید ممکن است اسکریپت نتواند شل را اجرا نماید.(معمولا sh به bash اشاره دارد)


# Command.returnCode.Check.success
#!/bin/bash
if command >/dev/null 2>&1; then
    echo "succeed"
else
    echo "failed"
fi

# Command.returnCode.Check.failed
#!/bin/bash
# check if last command failed
if ! command >/dev/null 2>&1; then
    echo "failed"
else
    echo "succeed"
fi

# Command.ReturnCode
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


# Command.output
#!/bin/bash
cd /tmp;
result="$(pwd)"
echo "$result"   #[output] → /tmp



# Command.GetPassword
# get text as input from user without showing
echo "Please enter your password: "
read -rs password
echo "${password}"


# Port Scan
host=$1
port_first=1
port_last=65535
echo >/dev/tcp/$host/$port >/dev/null 2>&1 && echo "$port open"