# 📍️ group:PackageManagements

## Debian

### source.list

```shell
part1 part2 part3 part4
```

* part1
    * deb: دانلود فایل‌های اجرایی
    * deb-src: دانلود سورس پکیج‌شده که برای دِوِلُپ یا دیباگ استفاده می‌شود
* part2
    * URL
* part3
    * bullseye → Debian11
* part4
    * Main:بطور کامل توسط شرکت سازنده پشتیبانی می‌شود
    * Restricted: پشتیبانی می‌شود ولی بطور کامل پشتیبانی نمیشود مثل درایور های شرکت ان ویدیا
    * Universe: توسط کامیونتی‌ها پشتیبانی می‌شود و برنامه های رسمی نیستند
    * Multiverse: رایگان نیستنتد
    * partner: [بهروز: باید بررسی شود]
    * می‌تواند چندین قسمت باشد یعنی هم شامل main و هم شامل Universe و هم شامل موارد دیگر باشد

☑️ **Examples:**

```shell
# 1️⃣️ Debian11:
  cat /etc/apt/sources.list|grep -v -E '#|$^'|grep . 
  deb http://deb.debian.org/debian/ bullseye main contrib non-free 
  deb-src http://deb.debian.org/debian/ bullseye main contrib non-free 
  deb http://security.debian.org/debian-security bullseye-security main contrib non-free 
  deb-src http://security.debian.org/debian-security bullseye-security main contrib non-free 
  deb http://deb.debian.org/debian/ bullseye-updates main contrib non-free 
  deb-src http://deb.debian.org/debian/ bullseye-updates main contrib non-free 

# ✅ Debian11: HOME
  deb http://deb.debian.org/debian/ bullseye main
  deb-src http://deb.debian.org/debian/ bullseye main
  deb http://security.debian.org/debian-security bullseye-security main contrib
  deb-src http://security.debian.org/debian-security bullseye-security main contrib
  deb http://deb.debian.org/debian/ bullseye-updates main contrib
  deb-src http://deb.debian.org/debian/ bullseye-updates main contrib
  deb http://security.debian.org/ bullseye-security main

```

### ✅️ apt

* [install] PackageName
    * install --fix-broken
* [remove] PackageName
* [purge] PackageName
* [show] PackageName
* [list] PackageName
* [search] PackageName

☑️ **Examples:****

* sudo apt download $(sudo apt-cache depends php7.0 | awk '{print$2}'|grep -v ">"|grep -v "<") # DownloadAllDependency
* apt --option Acquire::HTTP::Proxy="socks5h://127.0.0.1:9150" update

### ✅️ apt-get

* [install] PackageName #نصب بسته
    * [install] PackageName --print-urls #نمایش آدرس دانلود بسته‌ها
        * بجای نصب فقط آدرس «یوآرال» نمایش خواهد داد
* [update] #بروزرسانی لیست همه بسته‌های موجود در مخازن
* [upgrade] #آپگرید همه بسته‌ّای نصب شده به نسخه جدیدتر
* [remove] PackageName #حذف یک بسته با پسوند دب از روی سیستم توسط ابزار اَپْت
* [check] # بررسی وضعیت پیش‌نیاز‌ها یا همان دیپندنسی
* [clean] #پاک کردن کش که شامل بسته‌های پسوند دب دانلود شده است
    * [clean] all #حذف تمام کش مدیریت بسته

☑️ **Examples:**

* sudo apt-get download php && apt-cache depends -i php |awk '/Depends:/ {print $2}' | xargs apt-get download # DownloadAllDependency

### ✅️ apt-cache

* apt-cache search PackageName #جستجوی بسته موردنظر

### ✅️ ap-cdrom

ap-cdrom install PackageName #نصب یا آپگرید یک بسته باپسوند دب از روی سی‌دی‌رام

### ✅️ dpkg

* [-i PackageName.deb] # نصب آپگرید یک بسته
* [-r <Package>] #حذف یک بسته نصب شده
* [-l] # نمایش همه بسته‌های با پسوند دِب نصب شده در سیستم
* [-s PackageName] # نمایش اطلاعات مربوط به یک بسته خاص نصب شده در سیستم
* [-L PackageName] # نمایش لیست فایل‌ّای مربوط به یک بسته نصب شده
* [-L PackageName] # لیست تمام فایل‌های یک برنامه
    * dpkg -L vim
* [--contents PackageName.deb] # نمایش لیست فایل‌های مربوط به یک بسته که هنوز نصب نشده
* [-S /bin/ping] # بررسی اینکه فایل موردنظر به کدام بسته تعلق دارد

### ✅️ dpkg-query

* dpkg-query -L <PackageName> # نمایش تمام فایل‌ها و فولدرهای نصب شده از یک بسته
* dpkg-query --list # نمایش لیست تمام برنامه‌های نصب شده با جزئیات آن

### ✅️ dpkg-deb

* dpkg-deb -c <PackageName>.deb # تمام فایل‌هایی که قرار است با این بسته در سیستم نصب شود
* dpkg-deb -I FileName.deb # دریافت اطلاعات فایل به همراه تمامی دیپندنسی های این بسته(آی بزرگ)

### LocalRepository[DVD]

1. download DVD From Debian website
2. sudo vim /etc/apt/sources.list
3. mount file to specific directory with next line command:
    1. [temporary]:sudo mount -o loop /home/behrooz/App/DVD/debian-9.3.0-amd64-DVD-1.iso /media/repo_1
    2. [Permanently]:
        1. sudo vim /etc/fstab
        2. edit: /home/behrooz/App/DVD/debian-9.3.0-amd64-DVD-1.iso /media/repo_1 iso9660 defaults 0 0
4. sudo vim /etc/apt/sources.list
5. add:  deb [trusted=yes] file:///media/repo_1 stretch main contrib
6. sudo mount -a
7. lsblk
   dpkg -S /bin/ping # بررسی اینکه فایل موردنظر به کدام بسته تعلق دارد

### LocalRepository[WEB]

1. apt-get install build-essential apache2
2. mkdir /var/www/html/packages /var/www/html/packages/amd64
3. mount /dev/cdrom /media/cdrom
4. DVD1:find /media/cdrom/pool/ -name "*.deb" -exec cp {} /var/www/html/packages/amd64 \;
5. DVD2:find /media/cdrom/pool/ -name "*.deb" -exec cp {} /var/www/html/packages/amd64 \;
6. DVD3:find /media/cdrom/pool/ -name "*.deb" -exec cp {} /var/www/html/packages/amd64 \;
7. cd /var/www/html/packages/amd64/
8. dpkg-scanpackages . /dev/null | gzip -9c > Packages.gz

* SERVER:
    * vim /etc/apt/sources.list: `deb file:/var/www/html/packages/amd64/ /`
* CLIENT
    * vim /etc/apt/sources.list: `deb <http://192.168.1.150/packages/amd64/> /`

## CentOS

### ✅️ yum

* yum whatprovides "*CA.pl" #چه بسته‌هایی این نام را درون خود دارند
* yum -y install PackageName #دانلود و نصب یک بسته «آرپی‌ام»از مخازن
* yum localinstall PackageName #نصب یک بسته «آرپی‌ام» و تلاش برای حل پیش‌نیازها با استفاده از مخازن
* yum -y update #آپدیت همه بسته های «آرپی‌ام» نصب شده در سیستم
* yum update PackageName #آپگرید یک سته «آرپی‌ام» به نسخه جدیدتر
* yum remove PackageName #حذف یک بسته «آرپی‌ام» با استفاده از ابزار یام
* yum list #نمایش لیست همه بسته‌های نصب شده در سیستم
* yum search PackageName #پیدا کردن یک بسته از مخازن
* yum clean PackageName #پاک کردن کش که شمال بسته‌های «آرپی‌ام» دانلود شده توسط یام است
* yum clean headers #پاک کردن همه فایل‌های هِدِر که سیستم برای حل پیش‌نیازها از آنها استفاده می‌کند
* yum clean all #پاک کردن همه فایل‌های هِدِر و کش

### ✅️ rpm

* rpm -ivh Package.rpm #نصب یک بسته جدید
* rpm -ivh nodeeps Package.rpm #نصب یک بسته بدون درنظر گرفتن بسته‌های پیش‌نیاز
* rpm -U Package.rpm # آپگرید یک بسته بدون تغییر فایل‌های تنظیماتی مربوط به آن بسته
* rpm -F Package.rpm #آپگرید یک بسته فقط در حالتی که آن بسته نصب شده باشد
* rpm -e PackageName #حذف یک بسته از سیستم
* rpm -qa #نمایش همه بسته‌هایی که در سیستم نصب شده است
* rpm -qi PackageName #نمایش اطلاعات مربوط به یک بسته نصب شده
* rpm -qg "System Environment/Daemons" #نمایش بسته‌های «آرپی‌ام» مربوط به یک گروه نرم‌افزاری
* rpm -ql PackageName #نمایش لیست فایل‌های مربوط به یک بسته «آرپی‌ام» نصب شده
* rpm -qc PackageName #نمایش لیست فایل‌های تنظیماتی مربوط به یک بسته «آرپی‌ام» نصب شده
* rpm -q PackageName -whatrequires #نمایش لیست پیش‌نیازهای یک بسته «آرپی‌ام» نصب شده
* rpm -q PackageName -whatprovides #نمایش قابلیت‌های یک بسته «آرپی‌ام» مدنظر
* rpm -q PackageName -scripts #نمایش اسکریپت‌های اجرا شده در حین عمل نصب یا حذف یک بسته «آرپی‌ام» مدنظر
* rpm -q PackageName -changelog #نمایش تغییر اتیک بسته «آرپی‌ام» نسبت به نسخه‌ی قبلی
* rpm -qf /etc/httpd/conf/httpd.conf #بررسی اینکه فایل مورد نظر به کدلم بسته‌ی «آرپی‌ام» تعلق دارد
* rpm -qp PackageName -l #نمایش لیست فایل‌های مربوط به یک بسته «آرپی‌ام» که هنوز نصب نشده است
* rpm -import /media/cdrom/RPM-GPG-KEY #وارد کردن کلید
* rpm -cheksig Package.rpm #بررسی سالم بودن یک بسته «آرپی‌ام» مدنظر
* rpm -qa gpg-pubkey #بررسی سالم بودن همه بسته‌های نصب شده
* rpm -V PackageName #چک کردن حجم و هش «ام‌دی‌فایو» و مجوز و سایر مشخصات یک بسته «آرپی‌ام» مدنظر
* rpm -Va #چک کردن حجم و کد هش «ام‌دی‌فایو» و مجوز و سایر مشخصات همه بسته‌های «آرپی‌ام» مدنظر
* rpm -Vp PackageName.rpm #جک کردن حجم و هش «ام‌دی‌فایو» و سایر مشخصات یک بسته «آرپی‌ام» نصب نشده
* rpm -ivh /usr/src/redhat/RPMS/`arch`/PackageName.rpm #نصب یک بسته ساخته‌شده از سورس یک‌بسته «آرپی‌ام» مدنظر

### EPEL

Epel: Extra Packages for Enterprise Linux

* install
    * Cenots 7 64bit : rpm -ivh <http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-7.noarch.rpm>
    * Cenots 6 64bit :rpm -ivh <http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm>
    * Cenots 6 32bit :rpm -ivh <http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm>
    * Cenots 5 64bit :rpm -ivh <http://download.fedoraproject.org/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm>
    * Cenots 5 32bit :rpm -ivh <http://download.fedoraproject.org/pub/epel/5/i386/epel-release-5-4.noarch.rpm>
* configFile
    * /etc/yum.repos.d/epel.repo

### ✅️ rpmbuld

* rpmbuild -rebuild PackageName.src.rpm #ساختن یک فایل «آرپی‌ام» از روی سورس یک بسته «آرپی‌ام»

### ✅️ rpm2cpio

```shell
rpm2cpio PackageName | cpio -extract -make directories *bin* #استخراج فایل‌های اجرایی از یک بسته «آرپی‌ام»
```

# 📍️ group:UserManagements

## ✅️ adduser

- در نسخه لینوکس‌های کوچک دستور adduser وجود دارد(توزیع لینوکس alpine) و دستور useradd دستور بزرگتری و با ابزارهای بیشتری است.

## ✅️ groups

```shell
groups <name> #نمایش تمام گروه‌های یوزر فعلی
```

# 📍️ group:Process

## ✅️ fuser

```shell
fuser #پروسس‌هایی که دارد از یک فایل استفاده میکنند

```

# 📍️ group:Network

## ✅️ arp

* پروتکل arp: چه مک‌آدرس به چه آی‌پی متصل است
* بسته‌های پروتکل ARP از روتر عبور نمی‌کنند


* [-e]: display (all) hosts in default (Linux) style
    * `sudo arp -e`
* [-n|--numeric]:don't resolve names
    * `sudo arp -n`

## ✅️ethtool

```shell
sudo ethtool enp5s0 # اطلاعات فوق‌العاده زیاد بابت کارت شبکه

```

## ✅️ fping

`fping -g 192.168.10.1 192.168.10.5 #alive hosts`

## ✅️ hostname

* [-I] or [--all-ip-addresses] → All IP addresses for the host

```shell
hostname -I # show all ip address
```

## ✅️ iwlist|iwconfig

wifi|wireless|وای‌فای

```shell
iwlist <nic> scan #بررسی وایرلس‌های اطراف سیستم که بخواهیم به آن وصل شویم
iwconfig wlp4s0 essid "<Name>" key s:<Pass> #اتصال به یک وایرلس
```

## ✅️ ip

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

### [Gateway|Routr] Commands

* show
    * ip route
    * ip route show #default gateway information
* add
    * ip route add default via 192.168.200.1/24 #assign a default gateway
* remove
    * ip route del 192.168.0.150/24 #Removing a static route

## ✅️ ifconfig

```shell
ifconfig eth0:0 xxx.xxx.xxx.xxx #set [Additional ip] or [VirtualIp]
ifconfig eth0 hw ether AA:BB:CC:DD:EE:FF #MacSpoofing or تغییر مک آدرس
```

## ✅️ lsof

### Concept

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

### Switch

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

### Appendix

* [+L1] → سوکت‌های فعلی سرور که به هیچ فایلی از هارد وصل نشده است - پردازه‌های موجود در رم که ممکن است ویروس باشند
    * lsof +L1
* deletedFiles
    * sudo lsof [path] | grep deleted

## ✅️ mtr

```shell
mtr google.com
mtr -n --report IP
```

## ✅️ netstat

* [خالی و بدون پارامتر ورودی] → By default, netstat displays a list of open sockets.
* [-i] or [--interfaces,] → Display a table of all network interfaces
* [-s] or [--statistics] → Display summary statistics for each protocol
* [-r] or [--route,] ⇄ [route -e] → Display the kernel routing tables
* [-g] or [--groups,] → Display multicast group membership information for IPv4 and IPv6
* [-t] or [--tcp]→ display TCP sockets
* [-u] or [--udp] → display UDP sockets
* [-l] → display only listening sockets
* [-n] → display the socket’s port number

## ✅️ nmapt

* تعریف NullScan: بسته هیچ پرچمی(TCP، UDP، Sync، Http، ICMP و غیره) به خود نمی‌گیرد.
    * اگر یک سرور هیچ پاسخی نداد شما می‌توانید نوع اسکن را در وضعیت Null Scan قرار دهید که در آن صورت حتما بسته عبور می‌کند و حداقل می‌توان فهمید که سرور alive هست یا پایین است
* تعریف Zombi Attach: همزمان به چندین سیستم زامبی‌شده(قربانی‌های بستر اینترنت) می‌گوییم که به یک سرور وصل شوند و کاری انجام دهند و گزارش خروجی حمله را در اختیارمان قرار دهند و ما ناشناخته خواهیم ماند

### Ping

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

### Trace

* nmap –traceroute     [target] #Traceroute
* nmap --packet-trace [target] #Trace package

### DNS

* nmap -R [target] #Force Reverse DNS Resolution
* nmap -n [target] #Disable Reverse DNS Resolution
* nmap –system-dns [target] #Alternative DNS Lookup
* nmap –dns-servers [servers] [target] #Manually Specify DNS Server(s)
* nmap -sL [targets] #Create a Host List

### Advanced Scanning Options

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

### Port Scan

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

### Version Detection

* nmap -O [target] #Operating System Detection
* nmap -O –osscan guess [target] #Attempt to Guess an Unknown OS
* nmap -sV [target] #Service Version Detection
* nmap -sV –version trace [target] #Troubleshooting Version Scans
* nmap -sR [target] #Perform a RPC Scan

### Firewall Evasion Techniques

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

### Troubleshooting And Debugging

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

### nmap Scripting Engine

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

## ✅️ nmcli

```shell
nmcli connection show
nmcli connection show -a #only the active connections
nmcli connection [down|up] <Name> #[Up|Down] connections (By connections name) 
nmcli device status
nmcli device show
nmcli device show enp3s0
nmcli device [connect|disconnect] <NCname> #enabling|disconnect] an interface
nmcli device wifi list
nmcli general status
nmcli general #status is default action
nmcli general hostname #نمایش نام هاست
nmcli general hostname <NewName>
nmcli general permission #Show caller permissions for authenticated operations
nmcli general permission #Listing NetworkManager polkit permissions 
nmcli general logging
nmcli general logging level INFO
nmcli general logging domains ETHER
nmcli general logging domains WIFI
nmcli general logging domains ALL
nmcli general logging level INFO domains ALL
```

## ✅️ tcpdump

دستور لینوکس برای گوش کردن به شبکه- سوییچ‌ها

### Switch

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

### Examples

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

## ✅️ traceroute

```shell
traceroute google.com
```

## ✅️ wget

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
    - wget -r -A.pdf

# 📍️ group:Text

## ✅️ awk

### Concepts

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

### spliter

* awk -F ':' '{print $1}' /etc/passwd #نمایش ستون‌دوم با جداکننده دو نقطه

### [PATTERN]

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

### [PATTERN Eexactly]

* `awk ‘/\<PATTERN\>/ {print$0}’ File.txt` #match whole words only
* `awk -F ":" 'match($1,/\<....\>/) {print$0}'` ⇄ `awk '/^\<....\>/ {print$0}'` #ستون اول دقیقا ۴کاراکتر باشد
* `awk -v EID="$enclosure" -v SLT="$slot" '-F[:\t]' '$1 == EID && $2 == SLT {print$4}'`

### Trim

* `awk 'gsub("^[ \t]*","") {print $0}'` #حذف تمام خط‌فاصله‌های ابتدایی هر سطر
* `awk 'gsub("[ \t]*$" ,"") {print$0}'` #حذف تمام خط‌فاصله‌های انتهایی هر سطر
* `awk  '!/^$/'` ⇄ `awk '/./'`  #حذف خط خالی

### Functions

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

### کدنویسی

* `awk '{if(Condition1){action} else if(Condition2){action} else {action}}'`
* `awk -F":" '{if($1=="user") print "====> " $1; else if($1 == "root") print $1 " =====> " $7; else print "[" $0 "]"}' /etc/passwd`
* `awk -F ":" '$3>=1000 {print $1,$3,$NF}' /etc/passwd`
* `awk '{<CONDITION> print$1}'`
* `awk 'BEGIN{print "salam";}{print $0}'` #دقیقا ورودی را به خروجی هدایت میکند و تنها در اولین خط یک سلام اضافه میکند
* `awk -F ':' 'BEGIN{OFS="→";}{print $1,$3}' /etc/passwd ⇄ awk -F ":" ‘{print $1 "→" $3}’ /etc/passwd ⇄ awk -F ':' 'OFS="→" {print $1,$3}' /etc/passwd` #OFS کاراکتر خاص بین ستون‌ها

[OnlineTools](https://awk.js.org)

## ✅️ cat

* [-E]: نمایش انتهای خط که مثلا کاراکتر دالر باشد

```shell
cat -E fileName
```

## ✅️ dos2unix

```shell
dos2unix filedos.txt fileUnix.txt #تبدیل فرمت یک فایل متنی از سیستم ام اس داس به سیتمس یونیکس
```

## ✅️ echo

* `echo -e`: Display a message containing special characters

```shell
echo -e "You know nothing, Jon Snow.\n\t- Ygritte"
# output:You know nothing, Jon Snow.
#                - Ygritte
```

```shell
echo -e 'Here \vthe \vspaces \vhave \vvertical \vtab \vspaces.'
#Here
#     the
#         spaces
#                have
#                     vertical
#                              tab
#                                  spaces.
#

```

## ✅️ find

### Time

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

### Type

* [-type d] → Directory
* [-type f] → RegularFile
* [-type l] → SymbolicLink
* [-type s] → Socket
* [-type b] → block device Or block (buffered) special

### Size

* [-size +2G] → بزرگتر از دو گیگابایت
* [-size -10k] → کمتر از ۱۰ کیلوبایت
* [-size +10M -size -20M] → بزرگتر از ۱۰مگابایت و کوچکتر از ۲۰ مگابایت

### Perm

* [-perm 777]
* [! -perm 777] → NOT(without permission)
* [-perm 2644] → Find all the SGID bit files whose permissions are set to 644
* [-perm 1551] → Find all the Sticky Bit set files whose permission is 551
* [-perm /u=s] → Find all SUID set files.
* [-perm /g=s] → Find all SGID set files
* [-perm /u=r] → Find all Read-Only files
* [-perm /a=x] → Find all Executable files

### Other

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

### Examples

* [find / -type f -perm 0777 -print -exec chmod 644 {} \;] → Find all 777 permission files and use the chmod command to set permissions to 644
* [find / -type d -perm 777 -print -exec chmod 755 {} \;]  → Find all 777 permission directories and use the chmod command to set permissions to 755
* [find . -type f -name "tecmint.txt" -exec rm -f {} \;]         → To find a single file called tecmint.txt and remove it
* [find . -type f -name "*.mp3" -exec rm -f {} \;] → To find and remove multiple files such as .mp3 then use
* [find . -type f -name "*.txt" -exec rm -f {} \;]    → To find and remove multiple files such as .txt then use
* [find ./backup -type f -print0] → show all regular file wth path
* [find path -name file_name |xargs grep string] → پیدا کردن محتوی خاص در داخل فایل‌ها
* [find . -type f | xargs grep "example"]
* [] →

## ✅️ grep

### Switchs

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

### Repetition(تکرار)

**Repetition:** A regular expression may be followed by one of several repetition operators:

* ? The preceding item is optional and matched at most once.
* \* The preceding item will be matched zero or more times.
* \+ The preceding item will be matched one or more times.
* {n} The preceding item is matched exactly n times.
* {n,} The preceding item is matched n or more times.
* {,m} The preceding item is matched at most m times. This is a GNU extension.
* {n,m} The preceding item is matched at least n times, but not more than m times.

### EXAMPLE

* grep -E "[a]{3}" File.txt ⇄ grep  "[a]\{3\}" File.txt ⇄ egrep "[a]{3}" File.txt #خطوطی که حرف a سه مرتبه تکرار شده باشد
* grep "^<PATTERN>" File → هرچیزی که شروع خط با یک الگو باشد
* grep "<PATTERN>$" File → هرچیزی که پایان خط با یک الگو باشد

## ✅️ sed

* برای Not کردن یک علامت تعجب قبل از d یا s یا غیره قرار دهید
* برای در نظر نگرفتن case sensitive تنها کنار g یک آی بزرگ قرار دهید(یا تنها فقط یک آی قرار دهید)

### [s] → substitute

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

### [d] → delete

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

### [q]

* sed '<NUM>q;d' #نمایش خط شماره خاص از فایل
    * echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" |sed '6q;d' #نمایش فقط خط شماره ۶
* sed '<NUM>q' #نمایش تعداد خط اول
    * echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" |sed '6q' #نمایش 6 خط اول

### [p] → Print twice

* sed 'p' file #Print every line twice on output
* sed '6p' #print line 6 twice(every line once)
    * echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" |sed '6p' #

### [n] → سوییچ «اِن» سبب می‌شود که هرخط فقط یک بار چاپ شود

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

### [NOT]

* sed '!s/day/night/g'

## ✅️ tail

* [-<n>]
    * نمایش تعداد خط آخر
* tail [+<n>]
    * از خط شماره «اِن» شروع کن به نمایش

```shell
echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" | tail -3
8 eight
9 nine
10 ten
```

```shell
echo -ne "1 one\n2 two\n3 three\n4 four\n5 five\n6 six\n7 seven\n8 eight\n9 nine\n10 ten\n" | tail +3
3 three
4 four
5 five
6 six
7 seven
8 eight
9 nine
10 ten
```

## ✅️ tr

‌تبدیل کاراکتر به کاراکتر دیگر

* [-d]: حذف کاراکتر هایی که معین می‌شود
* [-c]: معکوس حذف یعنی تنها این کاراکترها را نگه‌داری کن
    * `tr -dc '0-9'` #نگهداری تنها اعداد و حذف همه کاراکترها

```shell
echo behrooz | tr 'o' 'u' #--> out: behruuz
```

## ✅️ unix2dos

```shell
unix2dos fileUnix.txt filedos.txt #تبدیل فرمت یک فایل متنی از سیستم ام اس داس به سیتمس یونیکس 
```

## ✅️ vim

### C → Change

- کارهای مربوط به change و دقیقا کارهای همان d را میکند ولی با این تفاوت که وارد مود نوشتن می‌شود
- حذف کاراکتر و رفتن به مود نوشتن

| syntax: c [number] motion | Description                                                  |
|---------------------------|--------------------------------------------------------------|
| `ce`                      | حذف کلمه از مکان کرسر تا انتهای کلمه و رفتن به مود نوشتن[ce] |
| `c2w`                     | حذف کلمه از مکان کرسر تا انتهای کلمه و رفتن به مود نوشتن[ce] |
| `c$`                      | حذف تا انتهای خط                                             |
| `ce`                      | Change rest of current word                                  |
| ``                        |                                                              |

### D → Remove

- کارهای حذف توسط این کاراکتر در مود نرمال انجام می‌شود
- حذف کاراکتر و باقی ماندن در مود نرمال

| syntax: d [number] motion | Description                                                                                |
|---------------------------|--------------------------------------------------------------------------------------------|
| `dw`                      | حذف یک کلمه:در ابتدای کلمه قرار بگیرید و d و سپس w را بفشرید(Delete word)                  |
| `de`                      | حذف یک کلمه: در ابتدای کلمه قرار بگیرید و d و سپس e را بفشرید(Delete (cut) to end of word) |
| `$d`                      | حذف یک خط کامل: حالت‌اول:در ابتدای خط قرار بگیرید و d و سپس $ را بفشرید                    |
| `^d`                      | حذف یک خط کامل: حالت‌دوم:در انتهای خط قرار بگیرید و d و سپس ^ را بفشرید                    |
| `d2w`                     | Delete (cut) next two words                                                                |
| `d3w`                     | حذف سه کلمه‌ی بعد از مکان نما و رفتن به اول کلمه بعد                                       |
| `d3e`                     | حذف سه کلمه‌ی بعد از مکان نما                                                              |
| `dd`                      | Delete(removex,cut) current line                                                           |
| `4dd`                     | remove 4 line                                                                              |
| `5dd`                     | Delete 5 lines                                                                             |
| `d$`                      | Delete (cut) to end of line                                                                |
| `D`                       | Delete (cut) to end of line (one char)                                                     |

### R → Replace

- کارهای حذف توسط این کاراکتر در مود نرمال انجام می‌شود
- کارهای مربوط به replace

| syntax: r [number] motion | Description                                                                                                                            |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `r<CHAR>`                 | در مود نرمال بخواهیم یک کاراکتر را تغییر دهیم ابتدا r را میفشاریم و سپس کاراکتر را وارد می‌کنیم                                        |
| `r<CHAR>esc`              | درمود نرمال بخواهیم چند کاراکتر را تغییر دهیم آنگاه زدن r و رفتن در مود replce و فشردن کاراکترها و در انتها فشردن esc                  |
| `:r<space><FullFilename>` | وارد کردن دیتای یک فایل دیگر در مکان کرسر آنگاه کرسر را در مکان مورد نظر قرار داده و فشردن کاراکتر : سپس r و فاصله و آدرس فایل         |
| `:r !date`                | ۴-وارد کردن دیتای یک دستور در مکان کرسر‌ آنگاه کرسر را در مکان مورد نظر قرار داده و فشردن کاراکتر : سپس r و فاصله و علامت تعجب و دستور |

### S → Substitude

| syntax: s [number] motion | Description                                                |
|---------------------------|------------------------------------------------------------|
| `:%s/foo/bar/<Enter>`     | Replace first 'foo' with 'bar' on every line               |
| `:s/foo/bar<Enter>`       | Replace first 'foo' with 'bar' on line                     |
| `:%s/foo/bar/gc<Enter>`   | Confirm replace all 'foo' with 'bar' in file               |
| `:s/foo/bar/gc<Enter>`    | Confirm replace all 'foo' with 'bar' on line               |
| `:s/foo/bar/g<Enter>`     | Replace all 'foo' with 'bar' on line                       |
| `:s/foo/bar/i<Enter>`     | Ignore case replace first 'foo' with 'bar'                 |
| `:%s/foo/bar/g<Enter>`    | Replace all 'foo' with 'bar' in file                       |
| `:%s/old/new/gc`          | تغییر کلمه در همه فایل به همراه پرسش                       |
| `:s/old/new/gc`           | تغییر کلمه در همه موارد موجود در خط به همراه پرسش از کاربر |
| `:s/old/new/g`            | تغییر کلمه در همه موارد موجود در خط                        |
| `:s/old/new`              | تغییر کلمه فقط در اولین مورد پیدا شده                      |
| `:sp<Enter>`              | New window above                                           |

### w → Write

| syntax: w [number] motion | Description   |
|---------------------------|---------------|
| `:w<Enter>`               | Save changes  |
| `:wq<Enter>`              | Save and exit |

#### ذخیره بخشی از محتوی فایل

1. زدن دکمه v [در مود نرمال] تا به حالت ویژوال مود برود
2. جابجایی کلید های بالا پایین و انتخاب خطوط مورد نیاز
3. بدون زدن دکمه دیگری فشردن دکمه :
4. سپس فشردن w و فاصله و آدرس مکان ذخیره
5. زدن اینتر

- `w /tmp/Behrooz.txt`

### Y → Yunk

| syntax: y [number] motion | Description                    |
|---------------------------|--------------------------------|
| `y$`                      | Yank (copy) to end of line     |
| `ye`                      | Yank (copy) to end of word     |
| `yw`                      | Yank to beginning of next word |
| `yy`                      | Yank (copy) line               |

### Visual Mode

| Command              | Description                   |
|----------------------|-------------------------------|
| `:w filename<Enter>` | Write selection to 'filename' |
| `v`                  | Visual mode select characters |
| `V`                  | Visual mode highlight lines   |
| `~`                  | Swap case                     |
| `>`                  | Shift right                   |
| `<`                  | Shift left                    |
| `c`                  | Change highlighted text       |
| `y`                  | Yank (copy) highlighted text  |
| `d`                  | Cut highlighted text          |
| `=`                  | Re-indent selection           |

---

### Bookmarks

| Command         | Description                 |
|-----------------|-----------------------------|
| `:marks<Enter>` | Show bookmarks              |
| `ma`            | Mark position 'a'           |
| ``a``           | Go to bookmark position 'a' |
| ````            | Go to previous position     |

---

### Set

| Command            | Description                                         |
|--------------------|-----------------------------------------------------|
| `:set hls<Enter>`  | Set highlight matching phrases(های‌لایت‌کردن‌جستجو) |
| `:set ic<Enter>`   | Set ignore case                                     |
| `:set is<Enter>`   | Set incremental search                              |
| `:set nois<Enter>` | Turn off incremental search                         |
| `:set number`      | نمایش شماره خطوط                                    |

<div dir="rtl">

### General Commands

- برای اینکه در اول خط چندین خط یک متن رو اضافه کنیم: در mode کامند دکمه CTRL+V را میزنیم تا به Mode تحت عنوان VisualBlock برویم سپس با arrow پایین و بالا و چپ و راست کنیم و محدوده را انتخاب نمایید سپس CTRL+I سبب نوشتن کاراکتر می‌شود پس از اتمام وارد کردن کاراکتر های مد نظر escape را بزنید تا برای همه محدوده بلاک اعمال شود
- در مود کامند در این برنامه کاراکتر % یعنی فایل کنونی
- برای کپی بخشی از فایل متنی ابتدا در مود نرمال کلید v را بفشرید و وارد ویژوآل مود شوید و بدون زدن دکمه دیگر دکمه بالا پایین و چپ و راست را بزنید و محتوی را انتخاب کرده و در انتها y را بزنید(با اینکار در بافر قرار می‌گیرد) سپس در مکان کرسر p را بزنید
- در محیط vim هرگاه یک دونقطه و یک علامت تعجب بزنید، هر دستوری که بخواهید قابل اجرا خواهد بود  `:!ls /tmp` و `:!/tmp/behrooz.sh`

</div>

- g: Global
- c: Confirm(در هنگام پرسش از کاربر)
- /: Search after cursor
- ?: Search before cursor

| Command                  | Description                                             |
|--------------------------|---------------------------------------------------------|
| `$`                      | Move to end of line                                     |
| `0`                      | Move to beginning of line                               |
| `:10,16s/old/new/gc`     | تغییر کلمه فقط در خطوط بین 10 تا 16 به همراه پرسش       |
| `12G`                    | Go to line 12                                           |
| `12`                     | Go to line 12                                           |
| `20l`                    | Go to column 20                                         |
| `:2,9s/foo/bar/g<Enter>` | Replace all 'foo' with 'bar' between lines 2 and 9      |
| `5b`                     | Move 5 words backward                                   |
| `5j`                     | Move down 5 lines                                       |
| `5k`                     | Move up 5 lines                                         |
| `5.`                     | Repeat last change 5 times                              |
| `5w`                     | Move 5 words forward                                    |
| `a`                      | Append                                                  |
| `A`                      | Append at end of line                                   |
| `b`                      | [Move to beginning of word [OR] Move to previous word ] |
| `ctrl+b`                 | Move backward one screen                                |
| `ctrl+e`                 | Scroll down                                             |
| `ctrl+f`                 | Move forward one screen                                 |
| `ctrl+g`                 | Show file info                                          |
| `ctrl+I`                 | رفتن به مکان جستجوی صورت گرفته                          |
| `ctrl+i`                 | Move to newer position                                  |
| `ctrl+o`                 | Move language autocomplete backward                     |
| `ctrl+o`                 | Move to older position                                  |
| `ctrl+O`                 | رفتن به مکان شروع جستجو                                 |
| `ctrl+p`                 | Move autocomplete backward                              |
| `ctrl+r`                 | Redo                                                    |
| `ctrl+x`                 | Move language autocomplete forward                      |
| `ctrl+y`                 | Scroll up                                               |
| `:e<Enter>`              | Open new file                                           |
| `:e filename<Enter>`     | Set current buffer to 'filename'                        |
| `e`                      | Move to end of word(کرسر را به انتهای کلمه بعدی می‌برد) |
| `ESC`                    | Exit insert mode to normal mode                         |
| `?foo<Enter>`            | Search backwards for 'foo'                              |
| `/foo<Enter>`            | Search forwards for 'foo'                               |
| `fw`                     | Move to next 'w' on line                                |
| `Fw`                     | Move to previous 'w' on line                            |
| `ga`                     | Show character info                                     |
| `gg`                     | Go to beginning of file                                 |
| `G`                      | Go to end of file                                       |
| `%`                      | Go to matching parenthesis or bracket                   |
| `:help cmd<Enter>`       | Lookup 'cmd' in help                                    |
| `h`                      | Move left one character                                 |
| `H`                      | Move to first line of screen                            |
| `i`                      | Insert                                                  |
| `I`                      | Insert at start of line                                 |
| `j`                      | Move down one line                                      |
| `K`                      | Look up word in man pages                               |
| `k`                      | Move up one line                                        |
| `l`                      | Move right one character                                |
| `L`                      | Move to last line of screen                             |
| `:!ls<Enter>`            | Execute 'ls' command                                    |
| `:make<Enter>`           | Run make                                                |
| `M`                      | Move to middle line of screen                           |
| `^`                      | Move to first non-whitespace char                       |
| `n`                      | Search next                                             |
| `N`                      | Search previous                                         |
| `O`                      | Insert new line above                                   |
| `o`                      | Insert new line below                                   |
| `p`                      | Paste                                                   |
| `P`                      | Paste before cursor                                     |
| `:qa<Enter>`             | Close all windows                                       |
| `:q<Enter>`              | Close current window                                    |
| `:q<Enter>`              | Quit                                                    |
| `:q!<Enter>`             | Quit without saving                                     |
| `r`                      | Change char and return to cmd mode                      |
| `:r !cmd<Enter>`         | Execute and insert results of 'cmd'                     |
| `R`                      | Enter replace mode                                      |
| `.`                      | Repeat last change                                      |
| `;`                      | Repeat last f, F, t, or T                               |
| `,`                      | Repeat last f, F, t, or T reversed                      |
| `:r filename<Enter>`     | Read and insert 'filename'                              |
| `:!rm filename<Enter>`   | Delete 'filename'                                       |
| `rx`                     | Replace current char with 'x'                           |
| `#`                      | Search for current word backward                        |
| `*`                      | Search for current word forward                         |
| `tw`                     | Move before next 'w' on line                            |
| `Tw`                     | Move before previous 'w' on line                        |
| `u`                      | Undo                                                    |
| `U`                      | Undo all changes to current line                        |
| `vim -t foo<Enter>`      | Start editing where foo is defined                      |
| `:vs<Enter>`             | New window to left                                      |
| `w`                      | Move to next word(کرسر را به ابتدای کلمه بعدی می‌برد)   |
| `:x<Enter>`              | Save and exit if modified                               |
| `zt`                     | Scroll current line to top of window                    |
| `:set background=dark`   |                                                         |
| `:syntax enable`         |                                                         |
| `:syntax on`             |                                                         |
| `:syntax off`            |                                                         |

### Files

#### 📌️ [~/.vim/color](http://amirsamimi.ir/vimrc)

```shell
cat ~/.vim/colors 

" Vim color file
"
" Author: Tomas Restrepo <tomas@winterdom.com>
"
" Note: Based on the monokai theme for textmate
" by Wimer Hazenberg and its darker variant
" by Hamish Stuart Macpherson
"

hi clear

set background=dark
if version > 580
    " no guarantees for version 5.8 and below, but this makes it stop
    " complaining
    hi clear
    if exists("syntax_on")
        syntax reset
    endif
endif
let g:colors_name="molokai"

if exists("g:molokai_original")
    let s:molokai_original = g:molokai_original
else
    let s:molokai_original = 0
endif


hi Boolean         guifg=#AE81FF
hi Character       guifg=#E6DB74
hi Number          guifg=#AE81FF
hi String          guifg=#E6DB74
hi Conditional     guifg=#F92672               gui=bold
hi Constant        guifg=#AE81FF               gui=bold
hi Cursor          guifg=#000000 guibg=#F8F8F0
hi Debug           guifg=#BCA3A3               gui=bold
hi Define          guifg=#66D9EF
hi Delimiter       guifg=#8F8F8F
hi DiffAdd                       guibg=#13354A
hi DiffChange      guifg=#89807D guibg=#4C4745
hi DiffDelete      guifg=#960050 guibg=#1E0010
hi DiffText                      guibg=#4C4745 gui=italic,bold

hi Directory       guifg=#A6E22E               gui=bold
hi Error           guifg=#960050 guibg=#1E0010
hi ErrorMsg        guifg=#F92672 guibg=#232526 gui=bold
hi Exception       guifg=#A6E22E               gui=bold
hi Float           guifg=#AE81FF
hi FoldColumn      guifg=#465457 guibg=#000000
hi Folded          guifg=#465457 guibg=#000000
hi Function        guifg=#A6E22E
hi Identifier      guifg=#FD971F
hi Ignore          guifg=#808080 guibg=bg
hi IncSearch       guifg=#C4BE89 guibg=#000000

hi Keyword         guifg=#F92672               gui=bold
hi Label           guifg=#E6DB74               gui=none
hi Macro           guifg=#C4BE89               gui=italic
hi SpecialKey      guifg=#66D9EF               gui=italic

hi MatchParen      guifg=#000000 guibg=#FD971F gui=bold
hi ModeMsg         guifg=#E6DB74
hi MoreMsg         guifg=#E6DB74
hi Operator        guifg=#F92672

" complete menu
hi Pmenu           guifg=#66D9EF guibg=#000000
hi PmenuSel                      guibg=#808080
hi PmenuSbar                     guibg=#080808
hi PmenuThumb      guifg=#66D9EF

hi PreCondit       guifg=#A6E22E               gui=bold
hi PreProc         guifg=#A6E22E
hi Question        guifg=#66D9EF
hi Repeat          guifg=#F92672               gui=bold
hi Search          guifg=#FFFFFF guibg=#455354
" marks column
hi SignColumn      guifg=#A6E22E guibg=#232526
hi SpecialChar     guifg=#F92672               gui=bold
hi SpecialComment  guifg=#465457               gui=bold
hi Special         guifg=#66D9EF guibg=bg      gui=italic
hi SpecialKey      guifg=#888A85               gui=italic
if has("spell")
    hi SpellBad    guisp=#FF0000 gui=undercurl
    hi SpellCap    guisp=#7070F0 gui=undercurl
    hi SpellLocal  guisp=#70F0F0 gui=undercurl
    hi SpellRare   guisp=#FFFFFF gui=undercurl
endif
hi Statement       guifg=#F92672               gui=bold
hi StatusLine      guifg=#455354 guibg=fg
hi StatusLineNC    guifg=#808080 guibg=#080808
hi StorageClass    guifg=#FD971F               gui=italic
hi Structure       guifg=#66D9EF
hi Tag             guifg=#F92672               gui=italic
hi Title           guifg=#ef5939
hi Todo            guifg=#FFFFFF guibg=#BB0000 gui=bold

hi Typedef         guifg=#66D9EF
hi Type            guifg=#66D9EF               gui=none
hi Underlined      guifg=#808080               gui=underline

hi VertSplit       guifg=#808080 guibg=#080808 gui=bold
hi VisualNOS                     guibg=#403D3D
hi Visual                        guibg=#403D3D
hi WarningMsg      guifg=#FFFFFF guibg=#333333 gui=bold
hi WildMenu        guifg=#66D9EF guibg=#000000

if s:molokai_original == 1
   hi Normal          guifg=#F8F8F2 guibg=#272822
   hi Comment         guifg=#75715E
   hi CursorLine                    guibg=#3E3D32 gui=underline
   hi CursorColumn                  guibg=#3E3D32
   hi LineNr          guifg=#BCBCBC guibg=#3B3A32
   hi NonText         guifg=#BCBCBC guibg=#3B3A32
else
   hi Normal          guifg=#F8F8F2 guibg=#1B1D1E
   hi Comment         guifg=#465457
   hi CursorLine                    guibg=#293739
   hi CursorColumn                  guibg=#293739
   hi LineNr          guifg=#BCBCBC guibg=#232526
   hi NonText         guifg=#BCBCBC guibg=#232526
end

"
" Support for 256-color terminal
"
if &t_Co > 255
   hi Boolean         ctermfg=135
   hi Character       ctermfg=144
   hi Number          ctermfg=135
   hi String          ctermfg=144
   hi Conditional     ctermfg=161               cterm=bold
   hi Constant        ctermfg=135               cterm=bold
   hi Cursor          ctermfg=16  ctermbg=253
   hi Debug           ctermfg=225               cterm=bold
   hi Define          ctermfg=81
   hi Delimiter       ctermfg=241

   hi DiffAdd                     ctermbg=24
   hi DiffChange      ctermfg=181 ctermbg=239
   hi DiffDelete      ctermfg=162 ctermbg=53
   hi DiffText                    ctermbg=102 cterm=bold

   hi Directory       ctermfg=118               cterm=bold
   hi Error           ctermfg=219 ctermbg=89
   hi ErrorMsg        ctermfg=199 ctermbg=253    cterm=bold
   hi Exception       ctermfg=118               cterm=bold
   hi Float           ctermfg=135
   hi FoldColumn      ctermfg=67  ctermbg=16
   hi Folded          ctermfg=67  ctermbg=16
   hi Function        ctermfg=118
   hi Identifier      ctermfg=208
   hi Ignore          ctermfg=244 ctermbg=232
   hi IncSearch       ctermfg=193 ctermbg=16

   hi Keyword         ctermfg=161               cterm=bold
   hi Label           ctermfg=229               cterm=none
   hi Macro           ctermfg=193
   hi SpecialKey      ctermfg=81  

   hi MatchParen      ctermfg=16  ctermbg=208 cterm=bold
   hi ModeMsg         ctermfg=229
   hi MoreMsg         ctermfg=229
   hi Operator        ctermfg=161

   " complete menu
   hi Pmenu           ctermfg=81  ctermbg=16
   hi PmenuSel        ctermfg=208  ctermbg=236
   hi PmenuSbar                   ctermbg=232
   hi PmenuThumb      ctermfg=81

   hi PreCondit       ctermfg=118               cterm=bold
   hi PreProc         ctermfg=118
   hi Question        ctermfg=81
   hi Repeat          ctermfg=161               cterm=bold
   hi Search          ctermfg=253 ctermbg=66

   " marks column
   hi SignColumn      ctermfg=118 ctermbg=235
   hi SpecialChar     ctermfg=161               cterm=bold
   hi SpecialComment  ctermfg=245               cterm=bold
   hi Special         ctermfg=81  
   hi SpecialKey      ctermfg=245

   hi Statement       ctermfg=161               cterm=bold
   hi StatusLine      ctermfg=238 ctermbg=253
   hi StatusLineNC    ctermfg=244 ctermbg=232
   hi StorageClass    ctermfg=208
   hi Structure       ctermfg=81
   hi Tag             ctermfg=161
   hi Title           ctermfg=166
   hi Todo            ctermfg=231 ctermbg=232   cterm=bold

   hi Typedef         ctermfg=81
   hi Type            ctermfg=81                cterm=none
   hi Underlined      ctermfg=244               cterm=underline

   hi VertSplit       ctermfg=244 ctermbg=232   cterm=bold
   hi VisualNOS                   ctermbg=238
   hi Visual                      ctermbg=235
   hi WarningMsg      ctermfg=231 ctermbg=238   cterm=bold
   hi WildMenu        ctermfg=81  ctermbg=16

   hi Normal          ctermfg=252 ctermbg=233
   hi Comment         ctermfg=59
   hi CursorLine                  ctermbg=234   cterm=underline
   hi CursorColumn                ctermbg=234
   hi LineNr          ctermfg=250 ctermbg=234
   hi NonText         ctermfg=250 ctermbg=233
end
```

#### 📌️ ~/.vimrc

```shell

:set number " Display line numbers on the left side
:set ls=2 " This makes Vim show a status line even when only one window is shown
:filetype plugin on " This line enables loading the plugin files for specific file types
:set tabstop=4 " Set tabstop to tell vim how many columns a tab counts for. Linux kernel code expects each tab to be eight columns wide.
:set expandtab " When expandtab is set, hitting Tab in insert mode will produce the appropriate number of spaces.
:set softtabstop=4 " Set softtabstop to control how many columns vim uses when you hit Tab in insert mode. If softtabstop is less than tabstop and expandtab is not set, vim will use a combination of tabs and spaces to make up the desired spacing. If softtabstop equals tabstop and expandtab is not set, vim will always use tabs. When expandtab is set, vim will always use the appropriate number of spaces.
:set shiftwidth=4 " Set shiftwidth to control how many columns text is indented with the reindent operations (<< and >>) and automatic C-style indentation. 
:setlocal foldmethod=indent " Set folding method
:set t_Co=256 " makes Vim use 256 colors
:set nowrap " Don't Wrap lines!
":colorscheme molokai "Set colorScheme
:set nocp " This changes the values of a LOT of options, enabling features which are not Vi compatible but really really nice
:set clipboard=unnamed
:set clipboard=unnamedplus
:set autoindent " Automatic indentation
:set cindent " This turns on C style indentation
:set si " Smart indent
:syntax enable " syntax highlighting
:set showmatch " Show matching brackets
:set hlsearch " Highlight in search
"":set ignorecase " Ignore case in search
:set noswapfile " Avoid swap files
:set mouse=a " Mouse Integration
:set cursorline " Highlight current line

" auto complete for ( , " , ' , [ , { 
:inoremap        (  ()<Left>
:inoremap        "  ""<Left>
:inoremap        `  ``<Left>
:inoremap        '  ''<Left>
:inoremap        [  []<Left>
:inoremap      {  {}<Left>

" auto comment and uncooment with F6 and F7 key
:autocmd FileType c,cpp,java,scala let b:comment_leader = '// '
:autocmd FileType sh,ruby,python   let b:comment_leader = '# '
:autocmd FileType vim   let b:comment_leader = '" '

:noremap <silent> #6 :<C-B>silent <C-E>s/^/<C-R>=escape(b:comment_leader,'\/')<CR>/<CR>:nohlsearch<CR> " commenting line with F6
:noremap <silent> #7 :<C-B>silent <C-E>s/^\V<C-R>=escape(b:comment_leader,'\/')<CR>//e<CR>:nohlsearch<CR> " uncommenting line with F7

:noremap <silent> #3 :tabprevious<CR> " switch to previous tab with F3
:noremap <silent> #4 :tabnext<CR> " switch to next tab with F2
:map <F8> :setlocal spell! spelllang=en_us<CR> " check spelling with F8
:set pastetoggle=<F2> " Paste mode toggle with F2 Pastemode disable auto-indent and bracket auto-compelation and it helps you to paste code fro elsewhere .


" plugins
" autocomplpop setting
:set omnifunc=syntaxcomplete " This is necessary for acp plugin
:let g:acp_behaviorKeywordLength = 1 "  Length of keyword characters before the cursor, which are needed to attempt keyword completion

" airline plugin setting
:let g:airline_theme='minimalist' " set airline plugin theme
:let g:airline#extensions#tabline#enabled = 1 " showing tabs 
:let g:airline_powerline_fonts = 1
if !exists('g:airline_symbols')
    let g:airline_symbols = {}
  endif

 " unicode symbols
  let g:airline_left_sep = '»'
  let g:airline_left_sep = '▶'
  let g:airline_right_sep = '«'
  let g:airline_right_sep = '◀'

"vim-airline-clock 
:let g:airline#extensions#clock#format = '%c'

" NERDTree plugin setting

"toggle showing NERDTree with F9
:map <F9> :NERDTreeToggle<CR> 

"open a NERDTree automatically when vim starts up if no files were specified
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

" close vim if the only window left open is a NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" Open file in new tab with ctrl + t
:let NERDTreeMapOpenInTab='<c-t>'

"indentLine 
:let g:indentLine_char = '.'


" vim-plug
" Plugins will be downloaded under the specified directory.
call plug#begin('~/.vim/plugged')

Plug 'https://github.com/rakr/vim-one.git'
Plug 'https://github.com/scrooloose/nerdtree.git'
Plug 'https://github.com/Shougo/vimshell.vim.git'
"Plug 'Shougo/vimproc.vim', {'do' : 'make'}
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'https://github.com/skywind3000/asyncrun.vim.git'

" List ends here. Plugins become visible to Vim after this call.
call plug#end()


" ۲۴ bit true colors
"Use 24-bit (true-color) mode in Vim/Neovim when outside tmux.
"If you're using tmux version 2.2 or later, you can remove the outermost $TMUX check and use tmux's 24-bit color support
"(see < http://sunaku.github.io/tmux-24bit-color.html#usage > for more information.)
if (empty($TMUX))
 if (has("nvim"))
    "For Neovim 0.1.3 and 0.1.4 < https://github.com/neovim/neovim/pull/2198 >
    let $NVIM_TUI_ENABLE_TRUE_COLOR=1

 endif
  "For Neovim > 0.1.5 and Vim > patch 7.4.1799 < https://github.com/vim/vim/commit/61be73bb0f965a895bfb064ea3e55476ac175162 >
  "Based on Vim patch 7.4.1770 (`guicolors` option) < https://github.com/vim/vim/commit/8a633e3427b47286869aa4b96f2bfc1fe65b25cd >
  " < https://github.com/neovim/neovim/wiki/Following-HEAD#20160511 >

 if (has("termguicolors"))
   set termguicolors
 endif
endif

" scary colorscheme
:let g:srcery_italic = 1
:let g:srcery_bold = 1
:let g:srcery_transparent_background = 0
:let g:srcery_underline = 1
:let g:srcery_undercurl = 1
:let g:srcery_inverse = 1
:let g:srcery_inverse_matches = 1
:let g:srcery_inverse_match_paren = 1
:let g:srcery_dim_lisp_paren = 1
:color srcery
:colorscheme srcery


"set colorscheme and airline theme according to daylight time
" if strftime("%H") < 12 && strftime("%H") > 7 
"       set background=light
"       let g:airline_theme='silver'
"       colorscheme buttercream
" else
"       colorscheme srcery
"     let g:airline_theme='minimalist' " set airline plugin theme
" endif
"
function Light()
        set background=light
        let g:airline_theme='silver'
        colorscheme buttercream
endfunction

function Dark()
    let g:srcery_transparent_background = 0
    let g:airline_theme='minimalist'
    color srcery
    colorscheme srcery
endfunction


:command LightTheme call Light()
:command DarkTheme call Dark()

" show qss file ighlighting like css files 
au BufRead,BufNewFile *.qss set filetype=css

"call pylint
:autocmd FileType python :map <F10> :AsyncRun pylint ./%<CR><CR>
:map <F12> :bw!<CR> 
"asyncrun.vim
:let g:asyncrun_open = 8
:let $PYTHONUNBUFFERED=1
:autocmd FileType python :noremap <F5> :AsyncRun -raw python % <CR> 
:autocmd FileType sh  :noremap <F5> :AsyncRun bash % <CR> 

```

# 📍️ group:Kernel

## ✅️ dd

### Switchs

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

### Examples

* dd if=/dev/sda1 of=/dev/sdb1 bs=4096 conv=noerror,sync
    * Note: برای کپی یک پارتیشن رو یک پارتیشن دیگر از دستور زیر استفاده می کنیم
* dd if=/dev/cdrom of=/mycd.iso
* dd if=/dev/sda of=/tmp/sdaMBR.img bs=512 count=1 #MBR size is 512 byte
* dd if=debian.iso of=/dev/sda bs=4M conv=fdatasync status=progress # ساخت یک فلش با قابلیت بوت
* dd if=/dev/da0 conv=sync,noerror bs=128K | gzip -c | ssh behrooz@server1 dd of=centos-core-7.gz # نبودن فضا کافی و ذخیره در ریموت

## ✅️ gcc

* عبارت GCC مخفف GNU Compiler Collection می‌باشد
* توسط ریچارد استالمن توسعه داده شده است
* کامپایلر Clang که بر مبنای پروژه LLVM توسعه داده شده و بسیار شبیه به کامپایلر GCC است.
* کامپایلر MSVS که مخفف MicroSoft Visual Studio هست و توسط مایکروسافت توسعه داده شده است.
* کامپایلر GCC در سیستم‌عامل‌هایی که کرنل آنها بر مبنای UNIX نوشته شده باشد(مثل لینوکس یا مک) عملکرد بهتری دارد و عملکرد gcc در ویندوز کندتر هست
* `sudo apt install gcc`: نصب کامپایلر جی‌سی‌سی

**CommandSyntax:** gcc Options Files

### options:

* [-o Output]: ایجاد فایل باینتری خروجی
* [-D<NameofConstant>=Value]: بجای تعریف ثابت‌ها تحت عنوان «دیفاین» مقادیر را درهنگام کامپایل مقدار دهی کرد
    * gcc -D<NameOfConstant>=Value NameOfSourceCode -o NameOfOutputFile]
* [-S outFile.c]: specifies to produce assembly code, instead of object code
    * ایجاد یک «فایل‌اسمبلی» (که حاوی کداسمبلی است) بجای ایجاد «آبجکت‌فایل» توسط کامپایلر
    * gcc -S metech2.c -o assembled.s

```shell
gcc main.c -o outpu_bin_file
```

### Environment Variables

[//]: # (Todo: Need to Review)
GCC uses the following environment variables:

* **PATH**: For searching the executables and run-time shared libraries (.dll, .so)
* **CPATH**: For searching the include-paths for headers.
    * It is searched after paths specified in -I<dir> options.
    * `C_INCLUDE_PATH` and `CPLUS_INCLUDE_PATH` can be used to specify C and C++ headers if the particular language was indicated in pre-processing
* **LIBRARY_PATH**: For searching library-paths for link libraries.
    * It is searched after paths specified in -L<dir> options.

## ✅️ g++

Syntax: g++ [options] [files]

### options

* [-o]: specifies the output executable filename.
* [-g]: generates additional symbolic debuggging information for use with gdb debugger.
* [-Wall]: prints "all" warning messages. نمایش تمام هشدار ها

### Examples

```shell
g++ -o myCode.exe file.cpp  # تک فایل
g++ -o myCode file1.cpp file2.cpp # چند فایل
g++ -c file1.cpp && g++ -c file2.cpp  &&   g++ -o myprog.exe file1.o file2.o # چند فایل
```

## ✅️ udevadm

### 1.Concepts

* در سیستم‌عامل لینوکس مبحث udev عاملی برای مدیریت سیستم و دستگاه است که به طور خودکار دستگاه‌های متصل به سیستم را شناسایی و پیکربندی می‌کند.
* در سیستم‌عامل‌های لینوکسی دستور udevadm برای فعال‌سازی مجدد رویدادهای udev استفاده می‌شود
* دستور [udevadm trigger]: ارسال فرمان به «udev» جهت ایجاد رویدادهای جدید برای دستگاه‌های متصل
    * به گونه‌ای که قوانین و اسکریپت‌های مربوط به دستگاه‌ها(شامل بارگذاری ماژول‌های هسته، تنظیم مجدد مجوزها، یا اجرای اسکریپت‌های خاص) دوباره اجرا شوند
    * حاصل نمودن اطمینان از صحت إعمال تغییرات در پیکربندی دستگاه‌ها یا قوانین udev
    * تغیین کلاس خاصی از دیوایس‌ها(مثلا فقط بلاک‌ها و غیره) که بخواهیم تحت تأثیر قرار بگیرند با سوییچ subsystem-match

### 2.Switch

### trigger

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

### 3.info

Query the udev database for device information

udevadm **info** [options] [devpath(such as /dev/sda)|file|unit]

* [-t] or [--tree]: نمایش در ساختار درختی
* [-c] or [--cleanup-db]: Cleanup the udev database
    * sudo udevadm info --cleanup-db /dev/sdb
    * توصیه‌می‌شوددر ادامه دستور زیر را بزنید
    * sudo udevadm trigger /dev/sdb

### 4.Examples

* `udevadm trigger  --subsystem-match=block --action=add $disk`
* `sudo udevadm info /dev/sda`
* ```shell
  for disk in /dev/sda /dev/sdb; do
  udevadm trigger  --subsystem-match=block --action=add $disk 
  done
  ```
* `sudo udevadm info /dev/sdb`

## ✅️ uname

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

# 📍️ group:Form Or Banner

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

# 📍️ group:Fun Comamnds

```shell
1-while true; do echo "$(date '+%D %T' | toilet -f term -F border --gay)"; sleep 1; done #نمایش زمان در حالت ترمینال
2- :(){ :|: & };:   #ForkBomb
3-rev behrooz #برگرداندن متن
4-cowsay
```

# 📍️ group:File

## ✅️ fio

```shell
fio --name=Rand_RW_100_8K --rw=randrw --direct=1 --rwmixwrite=100  --ioengine=windowsaio --time_based  --runtime=1800  --size=30tib --blocksize=8k  --numjobs=8 --filesize=4tib --thread --group_reporting --filename="\\.\PhysicalDrive2"  --output="c:\1403-08-29-TestRand100Write-T2.txt"
```

## ✅️ tree

نمایش فایل‌های بصورت درختی

```shell
tree -fi #نمایش تنها لیست فایل‌ها بصورت نام کامل
```

## ✅️ ulimit

get and set user limits

```shell
ulimit --help
ulimit -n #مشاهده محدودیت تعداد فایل‌های باز برای هر پردازه
ulimit -n <new_limit> #Temprory #the maximum number of open file
vim /etc/security/limits.conf # اگر بخواهیم بصورت دائمی باشد
```

# 📍️ group:MultiMedia

## ✅️ ffmpeg

```shell
ffmpeg -ss <Second> -i input.mp3 output.mp3
```