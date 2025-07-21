# awk

## Concepts

* [$0] → print all column
* [OFS] → Output field separator
    * awk -F ":" 'OFS="-" {print $1,$7}' /etc/passwd #نمایش تنها ستون اول و هفتم و یک خط تیره بین این دو ستون
    * awk -F ":" ‘{print $1 "→" $3}’ /etc/passwd ⇄ awk -F ':' 'OFS="→" {print $1,$3}' /etc/passwd ⇄ awk -F ':' 'BEGIN{OFS="→";}{print $1,$3}' /etc/passwd #کاراکتر خاص بین ستون‌ها
* && → AND
* || → OR
* [!] → NOT (!= Means not equal)
* [-F '<Pattern>'] or [--field-separator '<Pattern>'] → splitter
    * echo "192.168.1.1"| awk -F '.' '{ print $1" "$2" "$3" "$4;}'
* [$NF] → prints the last columns
    * awk -F ':' '{print $NF}' /etc/passwd #نمایش ستون آخر
    * awk 'NF>=3' #نمایش خطوطی که محتوی ۳ستون و بیشتر باشند
* [NR] → prints the line number(NumberRecord)
    * cat /etc/passwd | awk 'NR%2==1' #تمام خطوط فرد
    * cat /etc/passwd | awk 'NR%2==0' #تمام خطوط زوج
    * awk '$0 ~ "user" {print NR}' /etc/passwd #نمایش خطی که کلمه یوزر در آن وجود دارد
    * awk '{print NR"-"$0}' /etc/passwd #نمایش تمام خطوط به همراه شماره خط و یک خط تیره
    * awk 'NR==6 {print$1}' ⇄ awk '{if(NR==6) print$1}' #نمایش فقط خط۶
    * awk '/user/ {print$0;x=NR+2;next}(NR<=x) {print$0}' /etc/passwd #نمایش الگو و ۲ خط پس از الگو(حتی اگر چند الگو داشته باشیم)

## spliter

* awk -F ':' '{print $1}' /etc/passwd #نمایش ستون‌دوم با جداکننده دو نقطه

## [PATTERN]

* `awk '/PATTERN/ {print}'`  #نمایش خطوط حاولی الگو
* `awk '/PATTERN1/&&/PATTERN2/ {print$0}'`
* `awk '$0 ~ "PATTERN" {print$0}'`
* `awk '/^PATTERN$/ {print}'` #خطوطی که دقیقا حاوی الگو باشند و کاراکتر اضافی نداشته باشند
* `awk '! /PATTERN/'` #عدم نمایش الگو
* `awk '$0 !~ "PATTERN1|PATTERN2" {print$0}'` #عدم نمایش الگوها
* `awk '/PATTERN/{found=1} found'`  #نمایش الگو تا انتهای خروجی
    * {found=1}: وقتی الگو پیدا شد، متغیر را به ۱ تنظیم می‌کند
    * found: هر خط بعد از الگو چاپ شود
* `awk '/startPattern/{found=1} /endPattern/{print; found=0} found' file.txt` #نمایش از الگو اول تا الگوی دوم
    * `awk /startPattern/{found=1}`: وقتی الگوی "شروع شونده" پیدا شد، متغیر را به ۱ تنظیم می‌کند
    * `awk /endPattern/{print; found=0}`: وقتی الگوی "پایان‌پذیر" پیدا شد، خط را چاپ می‌کند و متغیر را به تنظیم می‌کند (یعنی از این به بعد هیچ خطی چاپ نخواهد شد)
    * found: هر خطی را که بین "الگوی استارت" و "الگوی پایان" است، چاپ کند
* `awk -v pattern="$PATTERN" -F ":" '$1 ~ pattern {print$0}' /etc/passwd` #[Behroooz: PATTERN=user]

## [PATTERN Eexactly]

* `awk ‘/\<PATTERN\>/ {print$0}’ File.txt` #match whole words only
* `awk -F ":" 'match($1,/\<....\>/) {print$0}'` ⇄ `awk '/^\<....\>/ {print$0}'` #ستون اول دقیقا ۴کاراکتر باشد
* `awk -v EID="$enclosure" -v SLT="$slot" '-F[:\t]' '$1 == EID && $2 == SLT {print$4}'`

## Trim

* `awk 'gsub("^[ \t]*","") {print $0}'` #حذف تمام خط‌فاصله‌های ابتدایی هر سطر
* `awk 'gsub("[ \t]*$" ,"") {print$0}'` #حذف تمام خط‌فاصله‌های انتهایی هر سطر
* `awk  '!/^$/'` ⇄ `awk '/./'`  #حذف خط خالی

## Functions

* [getline]: به ازای هر «گِت‌لاین» یک خط را نادیده می‌گیرد و به خط بعد می‌رود
    * `awk '/PATTERN/ {getline;print$0}'` #نمایش خط بعد از خطی که الگو یافت شده است
    * `awk '/PATTERN/ {print$0;getline;print$0}'` #خط الگو و خط بعد از الگو
* [sqrt]
    * `awk '{ print sqrt(625)}'` ⇄ `echo 625|awk '{print sqrt($0)}'`
* [match]
    * `awk -F ":" 'match($1,/\<....\>/) {print$0}'` ⇄ `awk '/^\<....\>/ {print$0}'` #ستون اول دقیقا ۴کاراکتر باشد
* [gsub]
    * `awk '{gsub(";",""); print $2}'` #حذف کاراکتر سمیکالون
    * `awk 'gsub("^[ \t]*","") {print $0}'` #حذف تمام خط‌فاصله‌های ابتدایی هر سطر
    * `awk 'gsub("[ \t]*$" ,"") {print$0}'` #حذف تمام خط‌فاصله‌های انتهایی هر سطر
* [substr]
    * `echo "hello, how are you?" | awk '{ print substr( $0, 3 ) }'` #حذف دو کاراکتر اول یک عبارت
* [lenght]
    * `echo "hello, how are you?" | awk '{ print substr( $0, 1, length($0)-1 ) }'` #حذف آخرین کاراکتر
    * `echo "hello, how are you?" | awk '{ print substr( $0, 2, length($0) - 2)}'`
* [tolower]
    * `awk '{print tolower($0)}'`

## کدنویسی

* `awk '{if(Condition1){action} else if(Condition2){action} else {action}}'`
* `awk -F":" '{if($1=="user") print "====> " $1; else if($1 == "root") print $1 " =====> " $7; else print "[" $0 "]"}' /etc/passwd`
* `awk -F ":" '$3>=1000 {print $1,$3,$NF}' /etc/passwd`
* `awk '{<CONDITION> print$1}'`
* `awk 'BEGIN{print "salam";}{print $0}'` #دقیقا ورودی را به خروجی هدایت میکند و تنها در اولین خط یک سلام اضافه میکند
* `awk -F ':' 'BEGIN{OFS="→";}{print $1,$3}' /etc/passwd ⇄ awk -F ":" ‘{print $1 "→" $3}’ /etc/passwd ⇄ awk -F ':' 'OFS="→" {print $1,$3}' /etc/passwd` #OFS کاراکتر خاص بین ستون‌ها

[OnlineTools](https://awk.js.org)

# dd

## Switchs

* if: Input File
    * if=IMAGE.img
* of: Output File
    * of=/dev/sdc
* bs: BlockSize تعداد بایت هایی است که در یک زمان خوانده یا نوشته می شود
    * مطمین شین که اندازه بلوک مضربی از ۱۰۲۴ که برابر با ۱ کیلوبایت است استفاده شود.
    * bs=1M
    * bs=1K
* status:
    * progress:‌اطلاع از میزان پیشرفت
* conv:روش تبدیل فایل ورودی و نوشتن روی دیسک مقصد چگونه است
    * noerror: کپی کردن داده ها در صورت برخورد به هر گونه خطا ادامه یابد
    * sync: استفاده از همگام‌سازی بین ورودی و خروجی
    * fdatasync: بافر به درستی پاکسازی و مجدداً نوشته شود و خطایی رخ ندهد
    * ucase: تبدیل به حروف بزرگ
        * dd if=~/file1 of=~/file2 conv=ucase # برای تبدیل کل محتویات فایل به حروف بزرگ
    * lcase: تبدیل به حروف کوچک
        * dd if=~/file1 of=~/file2 conv=lcase # برای تبدیل کل محتویات فایل به حروف کوچک
    * ascii: تبدیل فایلی ازهر فرمت به فرمت اسکی
        * dd if=textfile.ebcdic of=textfile.ascii conv=ascii
    * ebcdic: تبدیل فایل از هر فرمت به فرمت «اِب‌دیک» که بیشتر از «مِین‌فِرِیم»ها بازیابی می‌شود\
        * dd if=textfile.ascii of=textfile.ebcdic conv=ebcdic
* count: تعداد انجام عملیات

## Examples

* dd if=/dev/sda1 of=/dev/sdb1 bs=4096 conv=noerror,sync
    * Note: برای کپی یک پارتیشن رو یک پارتیشن دیگر از دستور زیر استفاده می کنیم
* dd if=/dev/cdrom of=/mycd.iso
* dd if=/dev/sda of=/tmp/sdaMBR.img bs=512 count=1 #MBR size is 512 byte
* dd if=debian.iso of=/dev/sda bs=4M conv=fdatasync status=progress # ساخت یک فلش با قابلیت بوت
* dd if=/dev/da0 conv=sync,noerror bs=128K | gzip -c | ssh behrooz@server1 dd of=centos-core-7.gz # نبودن فضا کافی و ذخیره در ریموت

# find

## Time

* [-mmin n]  → File's data was last modified less than, more than or exactly n minutes ago
    * [-mmin -60] ⇉ فایل‌های تغییر یافته در ۶۰دقیقه گذشته
    * [-mmin +60] ⇉ فایل‌های تغییر یافته از ۶۰ دقیقه پیش به قبل
* [-mtime n] → File's data was last modified less than, more than or exactly n*24 hours ago
* [-amin n]   → File was last accessed less than, more than or exactly n minutes ago
* [-atime n]  → File was last accessed less than, more than or exactly n*24 hours ago
* [-cmin n]   → File's status was last changed less than, more than or exactly n minutes ago
* [-ctime n]  → File's status was last changed less than, more than or exactly n*24 hours ago
* [-newermt]
    * [-newermt '-2 seconds'] → فایل‌هایی که تا دوثانیه پیش تغییر کرده‌اند

## Type

* [-type d] → Directory
* [-type f] → RegularFile
* [-type l] → SymbolicLink
* [-type s] → Socket
* [-type b] → block device Or block (buffered) special

## Size

* [-size +2G] → بزرگتر از دو گیگابایت
* [-size -10k] → کمتر از ۱۰ کیلوبایت
* [-size +10M -size -20M] → بزرگتر از ۱۰مگابایت و کوچکتر از ۲۰ مگابایت

## Perm

* [-perm 777]
* [! -perm 777] → NOT(without permission)
* [-perm 2644] → Find all the SGID bit files whose permissions are set to 644
* [-perm 1551] → Find all the Sticky Bit set files whose permission is 551
* [-perm /u=s] → Find all SUID set files.
* [-perm /g=s] → Find all SGID set files
* [-perm /u=r] → Find all Read-Only files
* [-perm /a=x] → Find all Executable files

## Other

* [-maxdepth X] → تعداد دایرکتوری هایی که بصورت بازگشتی مشاهده شود
    * بصورت دیفالت نامحدود است و همه زیر دایرکتوری مشاهده می‌شود
* [-empty]
    * find . -type f -empty
* [-name]
    * [-name] → جستجوی برمبنای نام
    * [-iname] → نادیده گرفتن حروف بزرگ و کوچک و آوردن هردو
    * find <Dir> -name behrooz.txt
* [-user]
    * [-user root]
* [-group]
    * [-group behrooz]
* [-print0] → رکوردهای یافت شده پشت‌سرهم در یک خط چاپ شوند
* [-print] → رکوردهای یافت شده توسط خط جدید از هم تفکیک شوند

## Examples

* [find / -type f -perm 0777 -print -exec chmod 644 {} \;] → Find all 777 permission files and use the chmod command to set permissions to 644
* [find / -type d -perm 777 -print -exec chmod 755 {} \;]  → Find all 777 permission directories and use the chmod command to set permissions to 755
* [find . -type f -name "tecmint.txt" -exec rm -f {} \;]         → To find a single file called tecmint.txt and remove it
* [find . -type f -name "*.mp3" -exec rm -f {} \;] → To find and remove multiple files such as .mp3 then use
* [find . -type f -name "*.txt" -exec rm -f {} \;]    → To find and remove multiple files such as .txt then use
* [find ./backup -type f -print0] → show all regular file wth path
* [find path -name file_name |xargs grep string] → پیدا کردن محتوی خاص در داخل فایل‌ها
* [find . -type f | xargs grep "example"]
* [] →

# grep

## Switchs

* [--color=auto] →نمایش رنگی
    * grep --color=auto user /etc/passwd #کلمه جستجو شده رنگی نمایش داده خواهد شد
* [-i] → ignore any case sensitivity
* [-c] → count for the number of occurrences of the matched pattern in a file
* [-o] → Print only the matched parts of a matching line, with each such part on a separate output line.
* [-n] → لحاظ کردن حروف کوچک یا بزرگ[دقیقا دنبال عبارت روبرو بگرد اگر بزرگ است یا کوچک]
* [-v] → عدم نمایش خطوط پیدا شده
    * echo -ne "۱\n\n\n\n۲\n۳\n\n۴" | grep -v "^$" #حذف خط خالی
* [-m] → فقط چند مورد(برحسب خط) از موارد یافت شده را نشان بده
    * grep -m 5 nologin /etc/passwd #‌فقط ۵ خط از موارد یافت شده را نشان بده و بقیه را نادیده بگیر
* [-A] → نمایش تعداد خط پس از الگو
    * grep -A 3 systemd /etc/passwd
* [-B] → نمایش تعدا خط قبل از الگو
    * grep -B 3 systemd /etc/passwd
* [-C] → نمایش تعداد خط قبل و پس از الگو
    * grep -C 3 systemd /etc/passwd
* [-e] → Egrep
    * grep -E "one|two|three"   ⇄ egrep  "one|two|three" #multi flter
    * ldd /sbin/ifconfig | grep -E -o '/lib.*\.[0-9]'  ⇄ ldd /sbin/ifconfig | egrep -o '/lib.*\.[0-9]' #نمایش ماژول‌های یک برنامه

* [-w] → match whole words only #مثال توجه شود
    * cat /tmp/salam\
      behrooz mohamadi\
      behrooz1 mohama\
      behrooz123 behrooz\
      behrooz12\
      behroo\
    * cat /tmp/salam |grep -w behrooz\
      behrooz mohamadi\
      behrooz123 behrooz

## Repetition(تکرار)

**Repetition:** A regular expression may be followed by one of several repetition operators:

* ? The preceding item is optional and matched at most once.
* \* The preceding item will be matched zero or more times.
* \+ The preceding item will be matched one or more times.
* {n} The preceding item is matched exactly n times.
* {n,} The preceding item is matched n or more times.
* {,m} The preceding item is matched at most m times. This is a GNU extension.
* {n,m} The preceding item is matched at least n times, but not more than m times.

## EXAMPLE

* grep -E "[a]{3}" File.txt ⇄ grep  "[a]\{3\}" File.txt ⇄ egrep "[a]{3}" File.txt #خطوطی که حرف a سه مرتبه تکرار شده باشد
* grep "^<PATTERN>" File → هرچیزی که شروع خط با یک الگو باشد
* grep "<PATTERN>$" File → هرچیزی که پایان خط با یک الگو باشد

# ip

Usage: ip OPTIONS OBJECT COMMAND

**نکته:** به جهت سهولت اگر بخشی از کلمه دستور نگارش شود به منزله‌آن است که همه کلمه به نگارش درآمده است

**OBJECTS**:

* address
    * ip a[|ad|add|addr|addre|addres|address] [s|sh|sho|show] [dev] eth0
    * ip a sh
    * ip ad sho
    * ip add s
    * ip -4 addre sho
* addrlabel
* amt
* fou
* help
* ila
* ioam
* l2tp
* link: network device
* macsec
* maddress: multicast address
* monitor: watch for netlink messages
* mptcp
* mroute
* mrule
* neigh
* neighbor
* neighbour
* netconf
* netns
* nexthop
* ntable
* ntbl
* route: routing table entry
* rule: rule in routing policy database
* sr
* stats: manage and show interface statistics
* tap
* tcp_metrics
* token
* tunnel: tunnel over IP
* tuntap
* vrf
* xfrm

**Options:**

* -c[olor]: نمایش رنگی دستورات
    * ip -c address show
* -d[etails]: نمایش جزییات
    * ip -d address
* -s[tatistics]
    * ip -s link
* -4: ip version4
* -6: ip version6

* ip -s link #network statistics
* link
    * ip link set <NIC> up|down
    * ip link #show information for all interfaces
    * ip link show dev eth0 #Display information only for device eth0
    * ip link set eth0 promisc on #Enable promiscuous mode for eth0
    * ip link ls up #Only show running interfaces
    * ip -s link #Display interface statistics
    * ip -s link ls eth0 #get information about a particular network interface
* add
    * ip addr add x.x.x.x/Y dev <NIC> → Add IP
* remove
    * ip addr del x.x.x.x/Y dev <NIC> → del IP
    * ip link del <nic> down → up/down NIC

## [Gateway|Routr] Commands

* show
    * ip route
    * ip route show #default gateway information
* add
    * ip route add default via 192.168.200.1/24 #assign a default gateway
* remove
    * ip route del 192.168.0.150/24 #Removing a static route

# lsof

## Concept

* COMMAND: The command name
* PID: Process ID (PID) of the process
* USER: Owner of the process
* FD: is the File Descriptor number of the file or
    * cwd: current working directory
    * rtd: root directory
    * txt: program text (code and data)
    * mem: memory-mapped file
    * Lnn: library references (AIX);
    * err: FD information error (see NAME column)
    * jld: jail directory (FreeBSD)
    * ltx: shared library text (code and data)
    * Mxx: hex memory-mapped type number xx
    * m86: DOS Merge mapped file
    * mmap: memory-mapped device
    * pd: parent directory
    * tr: kernel trace file (OpenBSD)
    * v86: VP/ix mapped file;
    * others:
        * r: for read access
        * w: for write access
        * u: for read and write access
* TYPE: Type of file descriptor[type of the node associated with the file]
    * DIR: Directory
    * REG: Regular file
    * CHR: Character special file.
    * FIFO: First In First Out
    * IPv4: IPv4 socket
    * IPv6: for an open IPv6 network file - even if its address is IPv4, mapped in an IPv6 address
    * inet: for an Internet domain socket
* DEVICE: Device number or, in the case of a block device, character or other
* SIZE/OFF: Dimension(بُعد) or size of the file or offset (the suffix 0t is the offset)
* NODE: Node description of the local file; this could be the number of the local file, TCP, UDP, or STR (stream)
* NAME: The name of the mount point where the file resides

## Switch

* [-i] → List all network connecttion
    * tcp|udp:
        * lsof -i tcp
        * lsof -i udp
    * PORT
        * lsof -i :22 #open Ports on ssh
        * lsof -i :ssh
        * lsof -i TCP:22
        * lsof -i UDP:514
        * lsof -i tcp
    * PORT Range
        * lsof -i TCP:1-1024
    * 4|6 → ipv4 or ipv6
        * lsof -i 4
        * lsof -i 6
    * IP
        * lsof -i @127.0.0.1
        * lsof -i @192.168.200.2
        * lsof -i tcp@127.0.0.1
        * lsof -i tcp@192.168.200.2
        * lsof -i udp@127.0.0.1
        * lsof -i udp@127.0.0.1
* [-u] All network connecttion List User Specific Opened Files
    * lsof -u behrooz
    * ^ : Exclude User with ‘^’ Character → عدم نمایش یک یوزر خاص
        * lsof -i -u^root
* [-p] → PID
    * lsof -p 1 → Pid=1
* [/<dir>] → Display Files of a Specific Filesystem
    * lsof / sys/
    * [+d]: جلوگیری از گردشی شدن یعنی نمایش تمام زیر مسیرها
    * lsof +d /proc
* TerminalFiles →
    * lsof /dev/tty*
* [-c] → Display Files Used by a Process Name
    * lsof -c ssh
    * lsof -c firefox
* [-R] → Add Parent pid(PPID) at output as a new column
* [-d] → فیلتر بر حسب ستون اِف‌دی یعنی ستون چهارم
    * lsof -d mem → All memory map files
    * lsof -d cwd

## Appendix

* [+L1] → سوکت‌های فعلی سرور که به هیچ فایلی از هارد وصل نشده است - پردازه‌های موجود در رم که ممکن است ویروس باشند
    * lsof +L1
* deletedFiles
    * sudo lsof [path] | grep deleted

# netstat

* [خالی و بدون پارامتر ورودی] → By default, netstat displays a list of open sockets.
* [-i] or [--interfaces,] → Display a table of all network interfaces
* [-s] or [--statistics] → Display summary statistics for each protocol
* [-r] or [--route,] ⇄ [route -e] → Display the kernel routing tables
* [-g] or [--groups,] → Display multicast group membership information for IPv4 and IPv6
* [-t] or [--tcp]→ display TCP sockets
* [-u] or [--udp] → display UDP sockets
* [-l] → display only listening sockets
* [-n] → display the socket’s port number

# nmapt

* تعریف NullScan: بسته هیچ پرچمی(TCP، UDP، Sync، Http، ICMP و غیره) به خود نمی‌گیرد.
    * اگر یک سرور هیچ پاسخی نداد شما می‌توانید نوع اسکن را در وضعیت Null Scan قرار دهید که در آن صورت حتما بسته عبور می‌کند و حداقل می‌توان فهمید که سرور alive هست یا پایین است
* تعریف Zombi Attach: همزمان به چندین سیستم زامبی‌شده(قربانی‌های بستر اینترنت) می‌گوییم که به یک سرور وصل شوند و کاری انجام دهند و گزارش خروجی حمله را در اختیارمان قرار دهند و ما ناشناخته خواهیم ماند

## Ping

* nmap -Pn [target] #Dont ping
* nmap -sP [target] #perform a Ping Only Scan
* nmap -PS [target] #TCP SYN Ping
* nmap -PA [target] #TCP ACK Ping
* nmap -PU [target] #UDP Ping
* nmap -PY [target] #SCTP INIT Ping
* nmap -PE [target] #ICMP Echo Ping
* nmap -PP [target] #ICMP Timestamp Ping
* nmap -PM [target] #CMP Address Mask Ping
* nmap -PO [target] #IP Protocol Ping

## Trace

* nmap –traceroute     [target] #Traceroute
* nmap --packet-trace [target] #Trace package

## DNS

* nmap -R [target] #Force Reverse DNS Resolution
* nmap -n [target] #Disable Reverse DNS Resolution
* nmap –system-dns [target] #Alternative DNS Lookup
* nmap –dns-servers [servers] [target] #Manually Specify DNS Server(s)
* nmap -sL [targets] #Create a Host List

## Advanced Scanning Options

* nmap -sS [target] #TCP SYN Scan
* nmap -sT [target] #TCP Connect Scan
* nmap -sU [target] #UDP Scan
* nmap -sN [target] #TCP NULL Scan
* nmap -sF [target] #TCP FIN Scan
* nmap -sX [target] #Xmas Scan
* nmap -sA [target] #TCP ACK Scan
* nmap –scanflags [flags] [target] #Custom TCP Scan
    * nmap –scanflags SYNFIN 192.168.0.1
* nmap -sO [target] #IP Protocol Scan
* nmap –send-eth [target] #Send Raw Ethernet Packets
* nmap –send-ip [target] #Send IP Packets

## Port Scan

* nmap -F [target] #Perform a Fast Scan
* nmap -p [port(s)] [target] #Scan Specific Ports
    * nmap -p 21-25,80,139,8080 192.168.1.1
* nmap -p [portName(s)] [target] #Scan Ports by Name
    * nmap -p ftp,http* 192.168.0.1
* nmap -sU -sT -p U: [ports],T:[ports] [target] #Scan Ports by Protocol
    * nmap -sU -sT -p U:53,111,137,T:21- 25,80,139,8080 192.168.0.1
* nmap -p ‘*’ [target] #Scan All Ports
* nmap –top-ports [number] [target] #Scan Top Ports
* nmap -r [target] #Perform a Sequential Port Scan

## Version Detection

* nmap -O [target] #Operating System Detection
* nmap -O –osscan guess [target] #Attempt to Guess an Unknown OS
* nmap -sV [target] #Service Version Detection
* nmap -sV –version trace [target] #Troubleshooting Version Scans
* nmap -sR [target] #Perform a RPC Scan

## Firewall Evasion Techniques

* nmap -f [target] #augment Packets
* nmap –mtu [MTU] [target] #pacify a Specific MTU
    * nmap –mtu 32 192.168.0.1
* nmap -D RND:[number] [target] #Use a Decoy
* nmap -D RND:10 192.168.0.1
* nmap -sI [zombie] [target] #Zombie Scan
* nmap –source-port [port] [target] #Manually Specify a Source Port
* nmap –data-length [size] [target] #Append Random Data
    * nmap –data-length 2 192.168.0.1
* nmap –randomize-hosts [target] #Randomize Target Scan Order
    * nmap –randomize-ho 192.168.0.1-20
* nmap –spoof-mac [MAC|0|vendor] [target] #Spoof MAC Address
    * nmap –spoof-mac Cis 192.168.0.1
* nmap –badsum [target] #Send Bad Checksums

## Troubleshooting And Debugging

* nmap -h #Getting Help
* nmap -V #Display nmap Version
* nmap -v [target] #Verbose Output
* nmap -d [target] #Debugging
* nmap –reason [target] #Display Port State Reason
* nmap –open [target] #Only Display Open Ports
* nmap –packet-trace [target] #Trace Packets
* nmap –iflist #Display Host Networking
* nmap -e [interface] [target] #Specify a Network Interface
    * nmap -e eth0 192.168.0.1

## nmap Scripting Engine

* nmap –script [script.nse] [target] #Execute Individual Scripts
* nmap –script [expression] [target] #Execute Multiple Scripts
    * nmap –script ‘http-*’ 192.168.0.1
* nmap –script [category] [target] #Execute Scripts by Category
    * Script Categories: all, auth, default, discovery, external, intrusive, malware, safe, vuln
    * nmap –script ‘not intrusive’ 192.168.0.1
* nmap –script [category1,category2,etc] #Execute Multiple Script Categories
    * nmap –script ‘default or safe’ 192.168.0.1
* nmap –script [script] –script trace [target] #Troubleshoot Scripts
    * nmap –script banner.nse –script-trace 192.168.0.1
* nmap –script-updatedb #Update the Script Database

# sed

* برای Not کردن یک علامت تعجب قبل از d یا s یا غیره قرار دهید
* برای در نظر نگرفتن case sensitive تنها کنار g یک آی بزرگ قرار دهید(یا تنها فقط یک آی قرار دهید)

## [s] → substitute

* echo  "day day day day" | sed 's/day/(day)/g' #out: (day) (day) (day) (day)
* echo  "day day day day" | sed 's/day/(&)/g' → #out: (day) (day) (day) (day)
* echo  "day day day day" | sed 's/day/night/' #تغییر فقط در اولی → #out: night day day day
* echo  "day day day day" | sed 's/day/night/2' #تغییر فقط در دومی → #out: day night day day
* echo  "day day day day" | sed 's/day/night/3' #تغییر فقط در سومی → #out: day day night day
* echo  "day day day day" | sed 's/day/night/3g' #تغییر در سومی به بعد → #out: day day night night
* echo  "day day day day" | sed 's/[a-f]/r/g' → #out: rry rry rry rry #substitute [a-f]  waith r
* sed 's/^[a-d]*/r/g' → #out: اگر کاراکتر «آ» تا کاراکتر «د» هر چند بار تکرار شده بود(در ابتدای خط) بجای آن «آر» قرار بده(حتی اگر صفر بار تکرار شده بود یعنی خط خالی بود)
* sed '3 s/<X>/<Y>/g' File.txt ⇉ #Change only in Line 3
* sed '3,5 s/<X>/<Y>/g' ⇉ #Change in Line 3 until line5
* sed '3,$    s/<X>/<Y>/g' ⇉ #Change in Line 3 until End
* sed /'^/,$ s/<X>/<Y>/g' ⇉ #Change in Line 1 until End [Carrot must be between  slash]
* sed -e 's/ *$//' #كاركتر خالي در آخر هر سطر را پاك كن
* sed -e 's/00*/0/g' #صفرهاي متعدد را با يك صفر تعويض كن

## [d] → delete

* sed '<NUM>d' #حذف خط شماره خاص
    * echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" |sed '7d' #نمایش همه بجز خط شماره هفتم
* sed '5d' File.txt #حذف خط خاص[مثلا  خط ۵]
* sed '$d' File.txt #حذف خط آخر
* sed '4,$d' File.txt #حذف خط چهارم تا آخر
* sed '/<X>/d' File.txt #حذف یک الگو از فایل
* sed -i '/<td>الگو<\/td>/{n;d}' FILE.txt #حذف یک خط پس از یک الگو
* sed '/^$/ d' File.tx #پاک کردن خطی که خالی هست و چیزی در آن نیست
* sed '/ *#/d;/^$/d' File.txt @تمام خطوط خالی و همچنین خطوط شامل کامنت حذف شود
* sed '/./!d' ⇄ sed '/^$/d'#حذف خط خالی

## [q]

* sed '<NUM>q;d' #نمایش خط شماره خاص از فایل
    * echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" |sed '6q;d' #نمایش فقط خط شماره ۶
* sed '<NUM>q' #نمایش تعداد خط اول
    * echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" |sed '6q' #نمایش 6 خط اول

## [p] → Print twice

* sed 'p' file #Print every line twice on output
* sed '6p' #print line 6 twice(every line once)
    * echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" |sed '6p' #

## [n]  → سوییچ «اِن» سبب می‌شود که هرخط فقط یک بار چاپ شود

* sed -n 'p' file #print every line only once
* sed -n <NUM>p File.txt # نمایش فقط یک خط خاص
    * cat /etc/passwd|nl|sed '4q;d'
    * cat /etc/passwd|nl|sed -n 4p
    * cat /etc/passwd|nl|sed -n '4p;4q'
    * cat /etc/passwd|nl|awk '{if(NR==4) print $0}'
    * cat /etc/passwd|nl|head -n 4| tail -n +4
      هر۴تای بالا یکسان هستند
* sed -n '1,3 p' file #چاپ خط یک تا سه
* sed -n '1,8p' file #چاپ خط یک تا هشت
* sed -n '/^[a]/ p' file # خطوطی که خط اول با «آ» شروع می‌شود را چاپ کن
* sed -n '/^[a]/ !p' file #خطوطی که خط اول با «آ» شروع می‌شود را چاپ نکن
* sed -n '/string1/p' # نمایش خطوطی که شامل کلمه استرینگ۱ باشد

## [NOT]

* sed '!s/day/night/g'

# tcpdump

دستور لینوکس برای گوش کردن به شبکه- سوییچ‌ها

## Switch

* [-c] → Capture Only N Number of Packets
    * sudo tcpdump -c 5
* [-i] → Capture Packets from Specific Interface
    * sudo tcpdump -i eth0
    * sudo tcpdump -i any
* [-A] → Print Captured Packets in ASCII
    * sudo tcpdump -A
* [-w] → Capture and Save Packets in a File
    * sudo tcpdump -w /tmp/0001.pcap
* [-r] → Read Captured Packets File
    * sudo tcpdump -r 0001.pcap
* [tcp] → Capture only TCP Packets
    * sudo tcpdump tcp
* [port n] → Capture Packet from Specific Port
    * sudo tcpdump port 22
* [src] → Capture Packets from source IP
    * sudo tcpdump src 192.168.0.2
* [dst] → Capture Packets from destination IP
    * sudo tcpdump dst 50.116.66.139
* [-D] → Display available interfaces
    * sudo tcpdump -D
        1. enp3s0 [Up, Running, Connected]
        2. any (Pseudo-device that captures on all interfaces) [Up, Running]
        3. lo [Up, Running, Loopback]
        4. bluetooth-monitor (Bluetooth Linux Monitor) [Wireless]
        5. nflog (Linux netfilter log (NFLOG) interface) [none]
        6. nfqueue (Linux netfilter queue (NFQUEUE) interface) [none]
        7. dbus-system (D-Bus system bus) [none]
        8. dbus-session (D-Bus session bus) [none]
* [-n] → show IP address replace name (disable name resolution)(Only IP address packets)
    * tcpdump -n
* [-nn] → show port address replace name (disable port resolution with -nn)
* [-XX] → Display Captured Packets in HEX
* [--number] → show packet numbers in output
* [-t] → omit timestamp info from tcpdump outpu
* [-v] → show detailed output
* [icmp] → capture ICMP packets only
* [host ip] → only packets related to a specific host
    * tcpdump host 10.0.20.150
* [broadcast] → capture broadcasts
    * tcpdump broadcast
* [multicast] → capture multicast
    * tcpdump multicast
* [] →
* [] →

## Examples

* tcpdump src NUMBER && dst port NUMBER
* tcpdump dst ff:ff:ff:ff:ff:ff
* tcpdump broadcast and multicast
* tcpdump broadcast && multicast
* tcpdump tcp and host 169.144.0.1 or host 169.144.0.20
    * tcp packages between 2 hosts
* ✅ tcpdump src 169.144.0.1 and port 22 and dst 169.144.0.20 and port 22
    * Only ssh packages between 2 hosts
* tcpdump -i any -c5 -nn src 192.168.122.98 and port 80 → #filter packets from source IP address 192.168.122.98 and
  service HTTP only
* tcpdump -i any -c5 -nn "port 80 and (src 192.168.122.98 or src 54.204.39.132)" → #filtering packets for HTTP service
  only (port 80) and source IP addresses 192.168.122.98 or 54.204.39.132

# udevadm

## 1.Concepts

* در سیستم‌عامل لینوکس مبحث udev عاملی برای مدیریت سیستم و دستگاه است که به طور خودکار دستگاه‌های متصل به سیستم را شناسایی و پیکربندی می‌کند.
* در سیستم‌عامل‌های لینوکسی دستور udevadm برای فعال‌سازی مجدد رویدادهای udev استفاده می‌شود
* دستور [udevadm trigger]: ارسال فرمان به «udev» جهت ایجاد رویدادهای جدید برای دستگاه‌های متصل
    * به گونه‌ای که قوانین و اسکریپت‌های مربوط به دستگاه‌ها(شامل بارگذاری ماژول‌های هسته، تنظیم مجدد مجوزها، یا اجرای اسکریپت‌های خاص) دوباره اجرا شوند
    * حاصل نمودن اطمینان از صحت إعمال تغییرات در پیکربندی دستگاه‌ها یا قوانین udev
    * تغیین کلاس خاصی از دیوایس‌ها(مثلا فقط بلاک‌ها و غیره) که بخواهیم تحت تأثیر قرار بگیرند با سوییچ subsystem-match

## 2.Switch

## trigger

udevadm **trigger** [options] [devpath(such as /dev/sda)|file|unit]

**options**

* [--action=]:
    * add # افزودن
    * remove # حذف‌کردن
    * change # اعمال تغییر
    * move # جابه‌جایی
    * online # آنلاین‌نمودن
    * offline # آفلاین نمودن
    * bind # اتصال رویکرد در دو شیء یا دیوایس
    * unbind # خارح کردن ارتباط و اتصال دو شیء یا دیوایس از هم
* [--subsystem-match=]
    * block: برای دستگاه‌های بلاک (مانند دیسک‌های سخت و SSDها)
        * net: برای دستگاه‌های شبکه (مانند کارت‌های شبکه)
            * udevadm trigger --subsystem-match=net #فعالسازی مجدد رویدادها برای دستگاه‌های شبکه
    * usb: برای دستگاه‌های USB
    * pci: برای دستگاه‌های PCI
    * tty: برای دستگاه‌های ترمینال (مانند tty و pty)
    * input: برای دستگاه‌های ورودی (مانند کیبورد و ماوس)
    * sound: برای دستگاه‌های صوتی
    * video: برای دستگاه‌های ویدیویی (مانند دوربین‌ها)
    * char: برای دستگاه‌های کاراکتری (مانند دستگاه‌های سریال)
    * firmware: دستگاه‌های مربوط به فریمور
    * backlight: دستگاه‌های نور پس‌زمینه (مانند صفحه‌نمایش)
    * dmi: اطلاعات DMI (دستگاه‌های سخت‌افزاری)
    * gpu: دستگاه‌های گرافیکی
    * scsi: دستگاه‌های SCSI
    * md: دستگاه‌های RAID (مدیریت دیسک)
        * برای مشاهده لیست کامل(البته وابسته به توزیع لینوکس و سخت‌افزار) از دستور زیر استفاده نمایید
            * ls /sys/class/

## 3.info

Query the udev database for device information

udevadm **info** [options] [devpath(such as /dev/sda)|file|unit]

* [-t] or [--tree]: نمایش در ساختار درختی
* [-c] or [--cleanup-db]: Cleanup the udev database
    * sudo udevadm info --cleanup-db /dev/sdb
    * توصیه‌می‌شوددر ادامه دستور زیر را بزنید
    * sudo udevadm trigger /dev/sdb

## 4.Examples

* `udevadm trigger  --subsystem-match=block --action=add $disk`
* `sudo udevadm info /dev/sda`
* ```shell
  for disk in /dev/sda /dev/sdb; do
  udevadm trigger  --subsystem-match=block --action=add $disk 
  done
  ```
* `sudo udevadm info /dev/sdb`

# uname

نمایش اطلاعات کرنل و سیستمی

* [-a] OR [--all] → print all information
* [-s] OR [--kernel-name] → print the kernel name
* [-n] OR [--nodename] → print the network node hostname
* [-r] OR [--kernel-release] → print the Linux kernel release
* [-v] OR [--kernel-version] → print the kernel version
* [-m] OR [--machine] → print the machine hardware name
* [-p] OR [--processor] → print the processor type or “unknown”
* [-i] OR [--hardware-platform] → print the hardware platform or “unknown”
* [-o] OR [--operating-system] → print the operating system

# wget

- [-b] → قرار دادن پروسه دانلود در بک‌گراند و عدم نمایش و این معمولا برای فایل‌های بزرگ کاربرد دارد
- [-c] → اگر دانلود متوقف شد مجددا ادامه دانلود را از سر گیرد
- [-f]: ایجاد یک فایل برای لاگ شدن وضعیت پیشرفت دانلود
- [-i] → ذخیره چندین یو‌آر‌ال در فایل و سپس دانلود لینک‌ها از فایل
    - wget -i ./FileName.txt
- [-l]: سطح بازگشت را تعیین میکند
    - اِل است و نه آی
- [-np] or [--no-parent] عدم رجوع به مسیر بالاتر
- [-O] Name → انتخاب نام جدید به فایل دانلود شده
- [-o ./download.log] → ذخیره لاگ در یک فایل بجای نمایش در ترمینال
- [-P]: قرار دادن در یک فولدر دیگر
    - [-P /documents/websites]:تمام محتوا به فهرست مشخص شده ما می رود
- [-Q5m] → پایان دانلود وقتی سایز دانلود شده از مقدار ۵مگابایت فراتر برود
- [-r] or [--recursive] دانلود به صورت بازگشتی
- [-R] or [--reject] → عدم دانلود یک نوع فایل معین ، در هنگام دانلود
    - wget -P documents/archives/ https://wordpress.org/latest.zip
- [--limit-rate=200k] → تعیین سرعت دانلود
- [--user-agent] → برخی سایت‌ها با تشخیص اینکه شما از مرورگر برای دانلود استفاده نمی‌کنید،می‌تونن اجازه دانلود به شما ندهند و شما توسط این گزینه نقاب می‌زنید و تحت عنوان مثلا فایرفاکس متصل می‌شوید
    - wget --user-agent="Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092416 Firefox/3.0.3" <URL>
- [--tries] → تعداد پیش‌فرض تلاش مجدد برای دانلود عدد۲۰ است و می‌تونیم آنرا تغییر دهیم
    - wget --tries=75 URL
- [--spider]: قراردادن در وضعیت اسپایدر
- [-mirror]: دانلود را بازگشتی می کند
- [-convert-links]: همه لینک‌ها برای استفاده آفلاین مناسب تبدیل خواهند شد
- [-page-requisites]: موارد زیر شامل تمام فایل‌های ضروری مانند «سی‌اِس‌اِس» و «جِی‌اِس» و تصاویر می شود
- [-no-parent]:تضمین می‌کند که دایرکتوری‌های بالای سلسله مراتب دانلود نمی‌شوند


- `wget --ftp-user=USERNAME --ftp-password=PASSWORD DOWNLOAD-URL`
- `wget --spider --force-html -r -l5 htp://dl.folan.net/Movie/ 2>&1 | grep '^--' | awk '{ print $3 }' | grep -v '\.css\|js\|png\|gif\|jpg$' | grep -v '\/$'`
- `wget --mirror --convert-links --page-requisites --no-parent -P documents/websites/ URL` #می توان از دستور wget برای دانلود محتوای کل سایت استفاده کرد
- `wget -r -np -R "index.html*" https://shop.hemat-elec.ir/wp-content/themes/irankala/assets/fonts` # Note: دانلود فایل های مشخص شده
    - wget -r -A.pdf <URL>