<div dir="rtl">

# 1. 🅰️ Fundamentals

* داکرهاست: همان سیستم عامل خودمان است که برنامه داکر در آن نصب شده است
* داکرهاب: مسیر hub.docker.com در مرورگر که درآنجا official image های زیادی وجود دارد و می‌توان آن را دانلود کرد و استفاده کرد
* اجاره میدهد تا نرم‌افزارهای بر پایه معماری Micro Service ایجاد نماییم و هر کدام از ماژول‌ها مستقل عمل کرده و توسط داکر راه‌اندازی شوند
* قابلیت اجرای ایمیج یک سیستم‌عامل با کرنل متفاوت(ویندوز و مک) بر روی سیستم لوکال(داکرهاست) لینوکسی وجود ندارد(در سیستم‌عامل لینوکس نمی‌توان ایمیج ویندوزی اجرا کرد)
* برنامه kitematics رابط گرافیکی داکر است که در ویندوز نصب می‌شود
* نام hostname های کانتینرهای داکر همان DockerId است
* داکر با زبان go نوشته شده است
* داکر نصب شده در سیستم عامل ویندوز به‌خوبی با کانتینر لینوکس compatible هست ولی داکر نصب شده در سیستم‌عامل لینوکس(بخاطر close بودن ویندوز) خیلی خیلی خوب نمیتونه با کانتینر ویندوز compatible باشد
* بک آپ یکی از الزامات داکر است که از کانتینرها حتما باید بک آپ داشت(بک آپی که حتما قبلا ریستور کرده باشی و خیالت راحت باشد)
* نسخه rancherLinux یک توزیع لینوکسی compatible با داکر و کانتینرها است

![Docker-Concept.jpg](_srcFiles/Images/Docker-Concept.jpg "Docker-Concept.jpg")

# 2. 🅰️ Docker CLI

## 2.1. 📍️ Options

* [-it]: Interactive --> اجازه استفاده مستقیم و تعاملی به ایمیج می‌دهد. گویا پشت کانتینر نشسته ایم و کامند وارد می‌کنیم
    * [-i]: open stdin as interactive connection
    * [-t]: define new TTY as Terminal
* [-p]: <portOnLocalHost>:<portOnImage>مَپ کردن پورت داخلی یک ایمیج روی سیستم لوکال
* [-d]: اجرای ایمیج در بک‌گراند
* [-e]: define a new EnvironmentVariable
* [-H]:ریموت روی سرور داکر در آی‌پی خاص و اجرای دستور
* [-u userName]: تعیین نام یوزر برای اجرای دستور
* [--name NAME]: دادن نام خاص به کانتینر بجای نام تصادفی
* [-v VolumeName:DirectoryOnContainer]
    * نکته:اگر از قبل توسط دستور داکر والیوم ایجاد نکرده باشیم، به محض قرار دادن نام جدید بعنوان والیوم در دستور «داکر ران» آن را میسازد
    * نکته۲:مسیر داده شده در کانتینر که قرار است به والیوم متصل شود خودکار ایجاد می‌شود ونیاز به از قبل ساخته شدن نیست
* HotFix[توجه به توضیحات]
    * docker run ... -v DirOnLocal:DirOnContainer imageName
    * مثال۱: docker run -d -p 3001:3000 -v $(pwd):/app imageName

## 2.2. 📍️docker

اجرای دستور در سرور ریموت

```shell
docker -H=<RemoteIP>:2222 <COMMAND> <OPTIONS> <ARGS> # connect to «DockerDaemon» on remote
docker -H=10.10.0.10:2222 run <IMAGE>
docker -H=tcp://<RemoteIP>:2222
docker -H=ssh://user@<RemoteIP>:2222
docker -H=192.168.1.50:2222            ps       # لیست کانتینرهای در حال اجرا روی سرور راه دور
docker -H=tcp://192.168.1.50:2222      ps       # over TCP
docker -H=ssh://user@192.168.1.50:2222 ps       # over SSH
docker -H=192.168.1.50:2222            images   # لیست همه ایمیج‌ها روی سرور راه دور
docker -H=192.168.1.50:2222 \
        run -d --name web -p 8080:80 nginx      # اجرای یک کانتینر روی سرور راه دور
docker -H=192.168.1.50:2222            logs web # دیدن لاگ‌های یک کانتینر روی سرور راه دور
docker -H=192.168.1.50:2222            stop web # توقف یک کانتینر روی سرور راه دور
docker -H=192.168.1.50:2222 \
       -H=192.168.1.60:2222            ps       # Multiple Host ---> در این حالت داکر دستور را روی هر دو سرور اجرا می‌کند
```

#### 2.2.1. ❇️ Set Default Host

تنظیم Host پیش‌فرض: اگر مدام می‌خواهید به یک سرور راه دور وصل شوید، می‌توانید متغیر محیطی تنظیم کنید تا هر بار -H ننویسید:

```shell
export DOCKER_HOST=tcp://192.168.1.50:2222
docker ps          # خودکار به سرور راه دور وصل می‌شود
unset DOCKER_HOST  # برگشتن به حالت عادی
```

#### 2.2.2. ❇️ open Remotes port

داکر Daemon روی سرور راه دور باید TCP را گوش دهد.به طور پیش‌فرض، داکر فقط روی Unix socket محلی (/var/run/docker.sock) گوش می‌دهد. برای اتصال راه دور باید روی سرور مقصد در فایل /etc/docker/daemon.json تنظیم کنید:

```json
{
  "hosts": [
    "tcp://0.0.0.0:2222",
    "unix:///var/run/docker.sock"
  ]
}
```

سپس ریستارت

```shell
sudo systemctl restart docker
sudo ufw allow 2222/tcp
```

```shell
docker --tlsverify --tlscacert=ca.pem --tlscert=cert.pem --tlskey=key.pem -H=192.168.1.50:2222 ps # اتصال امن از پروتکل TLS
docker -H=ssh://user@192.168.1.50 ps # اتصال امن از پروتکل ssh
```

## 2.3. 📍️docker build

* برای build کردن نیاز به یک داکرفایل است
* تمام Step های ران شده در build یک ایمج کش می‌شود تا در نوبت بعدی از این استفاده شود
* پس از اتمام بیلد بعنوان گزارش پارامتر Build context یک معیار خوب برای فهم کارایی ایمیج هست که حجم آن چقدر شده است
* در محیط عملیاتی هنگامی که بخواهیم یک ایمیج را ورژن بدهیم از تگ استفاده می‌کنیم که معمولاً عدد استفاده می‌شود(مدیریت نسخه‌ها) و برای اینکار باید در سوییچ«تی» که نام ایمیج را مشخص می‌کنیم سپس دو نقطه بگذاریم و شماره نسخه را بدهیم
*


* [-t]: تعیین نام برای ایمیج جدید حاصله از داکر فایل
    * نکته: اگر اسم داکرفایل را پیشفرض بگذاریم نیاز به تعیین نام نیست و نام پیش‌فرض Dockerfile است
    * docker build -t <ImageName> <Dir>
* [--no-cache=true|false]
    * docker build --no-cache=true -t <TagName> <Dir>

## 2.9. 📍️docker commit

ذخیره اطلاعات یک کانتینر و تبدیل به یک ایمیج

```shell
docker commit <ContainerID> <repository:[Tag]>
```

## 2.14. 📍️docker Container

نکته: در توزیع لینوکس alpine دستور apt نداریم بلکه معادل آن apk است

```shell
docker container exec -it <ExistContainerID> bash # اجرای دستور در یک کانتینر موجود
docker container ls -a # show Execute commands history on containers
docker container ls    # list running containers
docker container stop <ExistContainerID>
docker container prune #حذف کانتینرهای اضافی که مثلا لایه‌های آنها کش شده است. همواره ابتدا کانتینر رو هرس کنید و سپس ایمیج‌ها را هرس کنید
```

## 2.8. 📍️docker cp

کپی اطلاعات کانتینر درحال اجرا برروی سیستم فیزیکی ولوکال خودمان و برعکس

```shell
docker cp <ContainerID>:fullFileName <localHostSystem> #کپی از کانتینر به سیستم
docker cp f39a65:/app/My_file.txt /home/user/Document
docker cp <localHostSystem> <ContainerID>:fullFileName #کپی از سیستم به کانتینر
```

## 2.7. 📍️docker exec

اجرای یک دستور جدید در یک کانتینر موجود که هم‌اکنون درحال اجرای دستور است

```shell
docker exec -it <NameContiner> <Commnads>
docker exec -it <NameContiner> /bin/bash
```

## 2.16. 📍️docker history

```shell
docker history [ImageName] #نمایش تاریخچه دستورات
```

## 2.17. 📍️docker inspect|info

```shell
docker info # show environments
docker inspect <CoutainerID|Name>
```

## 2.20. 📍️docker image

* برای تولید یک ایمیج Custom باید ابتدا یک DockerFile ایجاد کنیم و دستورالعمل‌هایمان را داخل آن قرار دهیم. سپس داکر فایل را بیلد نماییم یعنی داکر فایل خط به خط خوانده شود و پس از اتمام آن خروجی حاصله را توسط دستور build به یک ایمیج تبدیل کنیم
* نکته: توزیع alpine یک توزیع بسیار سبک از لینوکس است که بجای دانلود ایمیج لینوکس با حجم زیاد بهتر است این را استفاده نمایید
* نکته۲: نمونه ایمیج‌های مفید و stable را می‌توان از مسیر URL استخراج کرد که ایمیج هر برنامه بصورت تفکیک شده موجود است
* نکته۳: وقتی یک ایمیج رو اکسپورت می‌کنیم و سپس در سیستم دوم ایمپورت می‌کنیم باید آی دی تغییر نکرده باشد
* [prune]: (Remove unused images) هرس و حذف اضافات یا اصطلاحاً «کلین‌آپ» کردن
    * هرس کردن و حذف ایمیج‌های که با ایمیج اصلی ارتباط ندارند و اضافی یا خطرناک هستند مثل لایه‌های کش شده
    * مثلا مواردی که در دستور «لیست ایمیج‌ها»ستون ریپوزیتوری یا ستون تگ در آن عبارت «نان» درج شده است
* [rm]: حذف یک ایمیج و به تَبَع آن تمام کانتینرهای آن نیز پاک خواهند شد
    * [-f]: تمام کانتینرهای مشتق شده از ایمیج(مثلا در ریپوزیتوری) را نیز پاک کن

```shell
docker images     # show images list
docker images ls  # show images list
docker image build -f <DockerFile> -t <NewName>            # ساخت ایمیج جدید
docker image build                 -t <NewName> .          # ساخت ایمیج جدید
docker image tag <ExistName>:<ExistTag> <NewName>:<NewTag> # Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE ---> ایجاد یک ایمیج جدید با نام و تگ جدید اما با هش کد مشابه اگر نام موجود باشد «اُوِررایت» می‌شود
docker image save -o <FullFileName> <IMAGE>                # ذخیره ایمیج در قالب فایل برای انتقال به سیستم دوم جهت استفاده مجدد
docker image load -i <ImageFile>                           # Load an image from a tar archive or STDIN ---->  اگر بخواهیم دستی یه ایمیج رو به سیستم خود اضافه کنیم
docker images rm     <ImageID>
docker images rm -f  <ImageID>
docker image prune
```

## 2.11. 📍️docker load

دریافت ورودی و یک ایمیج را در ایمیج های داکر لود میکند

```shell
docker load -i <PATH.tar.gz>
```

## 2.12. 📍️docker rmi

```shell
docker rmi [<Container ID>|<NAME>]
```

## 2.4. 📍️docker run

* اجرای یک دستور بر پایه یک ایمیج که سبب تولید یک کانتینر می‌شود و هرگاه دستور تمام شود آنگاه کانتینر ازبین می‌رود
* نکته۱:کانتینرها درواقع پروسس هستند که در قالب ایمیج ایجاد می‌شوند و پس از اجرا تمام و از بین می‌روند
* نکته۲: هر ایمیج که توسط دستور run سبب ایجاد یک کانتینر می‌شود یک کاری را باید انجام دهد. هنگامی که دستور مورد نظر برای آن ایمیج تمام شد بصورت خودکار از بین می‌روند
* نکته۳: اگر دستور ران شده سبب باز کردن پورت و ارائه سرویس باشد آنگاه آن کانتینر همچنان دردسترس است و در دستور docker ps آن ایمیج نمایش داده می‌شود که در حال ران است. اگر سرویس مد نظر crash کند آنگاه کانتینر از بین می‌رود
* نکته۴: وظیفه کانتینرها این نیست که بیایند و یک سیستم عامل بر پایه ایمیج ایجاد نمایند
* نکته۵(خیلی‌مهم): وظیفه‌ی کانتینرها اجرای «دستور» یا «جاب» یا «محاسبه» یا ا«جرای‌یک‌پردازه» و از این قبیل است و هنگامی که پردازش آنها تمام شد، بطور خودکار از بین می‌شوند
* نکته۶: به ازای هر کانتینر که برای اجرای یک دستور خاص توسط «داکر ران» ایجاد می‌شود یک محیط ایزوله و مستقل است و درصورت اجرای مجدد همان دستور یک کانتینر در محیط ایزوله و مستقل و با آی‌دی دیگر برایش ایجاد خواهد شد
* HotFix: همزمان که در سیستم خودتان درحال اصلاح کد هستید این تغییرات در داخل کانتینر هم لحاظ بشود. اگر چه این فایل‌ها در لایه readonlyداکر فایل(در وضعیت غیرقابل تغییر) قرار گرفته باشد
* برای ایمیج‌های رایج که شل پیشفرض دارند مثل ubuntu بصورت پیش‌فرض از دستور `/bin/bash` استفاده می‌شود زیرا در داکر فایل رسمی آن `CMD ["/bin/bash"]` آمده است. یعنی اگر دستوری نزنید این دستور به اجرا در میاید ولی اگر دستوری بزنین دستور نادیده گرفته می‌شود

```shell
Docker run <IMAGE> [Commands]        # Run a command in a new container
docker run <IMAGE> # اجرای دستور «هیچی» روی ایمیج اوبونتو(بدون دستور و آرگومان) و جون کامند ندادیم پس کاری انجام نمی‌شود و خودکار بسته می‌شود
docker run <IMAGE> sleep ۱۰ # به کانتینر بالا آمده از ایمیج اوبونتو می‌گوید که دستور توقف زمانی۱۰ثانه را در بش اجرا کن و پس ازاتمام کانتینر را از بین ببر-یعنی اگر در مدت ۱۰ثانیه در ترمینال دیگر دستور «داکر پی‌‌اِس» را بزنیم کانتینر را خواهیم دید
docker run <IMAGE> # جستجو در ایمیح‌های داکرهاست(سیستم‌لوکال) و درصورت عدم وجود، جستجو در ریپوزیتوری پیش‌فرض(داکرهاب) و سپس دانلود و نهایتا استفاده از آن
docker run -it node:16.5.0-alpine3.14    # ورود به کنسول ریَکت
docker run -it <Repo:Tag>                # ورود به کنسول ریَکت
docker run -it   node:16.5.0-alpine3.14 sh # ورود به شل ایمیج
docker run -it ubuntu bash # خط فرمان بش داخل ایمیج را در بصورت اینتراکتیو در اختیار کاربر قرار میدهد و صفحه ترمینال سیستم‌عامل لوکال به بش داخل ایمیج تغییر می‌کند
docker run -p 5001:5000 <IMAGE> # 5001(PhysicalServer or Localhost) TO 5000(virtual container)
docker run <IMAGE> -p 5001:5000 # ❌️  غلط است
docker run -d <IMAGE>   # یک کانینر را در بک‌گراند بالا می‌آورد و هش آن را نمایش می‌دهد
docker run -d --name <NAME> <IMAGE>
docker run -it -u root face4 sh
docker run -d -p 3001:3000 -v myShareVolume:/Dir1/subdir imageName

docker run -i -t <Repo:Tag> #run and go to bash of OS(if shell exist)
docker run -it   <Repo:Tag> #run and go to bash of OS(if shell exist)
docker run -i -t --name <NAME> <Repo:Tag>   #run and go to bash of OS 
docker run -d    --name <NAME> -v <VolumeName>:Path <Image>
docker run       --name <NAME> -v BehroozData:/data/db -p 28001:27017 -d <Image>
docker run -d    --name <NAME> -e APP_PORT=7070 -p 8081:7070 <Image>
docker run --rm ...   # run after kill after delete
```

## 2.5. 📍️docker stop

```shell
docker stop Name #استاپ کردن یک کانتینر
docker stop [Hash | Name] # نکته۱: کانتینر رو از بین نمی‌برد بلکه استاپ میکند و بعدا با دستور استارت می‌توانیم از وضعیت استاپ خارج نماییم
docker container prune #  اگر کانتینرهای استاپ شده زیاد داریم با این دستور می‌توانیم آنها را از بین ببریم

```

## 2.6. 📍️docker save

ذخیره یک ایمیج

```shell
docker save -o <Name>.tar.gz Repository:Tag
```

## 2.10. 📍️docker volume

**MountPoint**: ‌مسیری که در دستور inspect نمایش داده می‌شود و نشان می‌دهد که والیوم در کدام مسیر لینوکس اصلی قرار دارد

```shell
docker volume create <VolumeName>     #ایجاد یک والیوم جدید
docker volume rm     <VolumeName>     # Remove one or more volumes
docker volume prune                   # Remove unused local volumes
docker volume ls                      # List   volumes
docker volume inspec <VolumeName>     # Display detailed information on one or more volumes ---> نمایش جزییات والیوم ساخته شده از قبل
docker volume update                  # Update a volume (cluster volumes only)
```

## 2.13. 📍️docekr ps

* نمایش کانینرهای درحال اجرای دستور در سیستم عامل کنونی را نشان می‌دهد که درحال اجرای چه دستوری است
* نکته۱:کانتینرها درواقع پروسس هستند که در قالب ایمیج اجرا می‌شوند و پس از اجرا تمام و از بین می‌روند


* [-a]: تاریخچه دستورات و وضعیت کانتینرهای فعال و غیرفعال
    * doccker ps -a
* [-q]
    * docker ps -a -q #show ContainerID of all containers

## 2.15. 📍️docker volume

```shell
docker volume create --name Behrooz
docker volume ls
docker volume inspect behrooz
```

## 2.18. 📍️docker logs

```shell
docker logs [ContainerID | NAME] #Fetch the logs of a container منظور خطوط خروجی دستورات داکر است اگر در حالت بک‌گراند اجرا بگیریم
```

* [--details] #Show extra details provided to logs
* [-f] or [--follow] : # Follow log output یعنی ته فایل رو باز می‌گذارد که خروجی جدید مشاهده شود
* [-n] or [--tail string] #Number of lines to show from the end of the logs (default "all")
    * docker logs ContainerName -n 5 #نمایش تعدا خط خروجی
* [-t]: نمایش تایم برای هر خط
    * docker logs -t -n 100 ImageName # نمایش صد خط از خروجی دستورات داکر به همراه نمایش تایم آن دستورات که به اجرا درآمده است




## 2.19. 📍️docker tag

یک نام یا برچسب اضافی (alias) به یک ایمیج موجود اختصاص می‌دهد. این دستور ایمیج جدید نمی‌سازد و کپی هم نمی‌کند — فقط یک ارجاع (reference) جدید به همان لایه‌های ایمیج اضافه می‌کند. یعنی بعد از اجرا، دو نام مختلف دارید که هر دو به یک ایمیج یکسان (با همان IMAGE ID) اشاره می‌کنند.اگر تگ را ننویسید، به طور پیش‌فرض latest در نظر گرفته می‌شود.

* docker tag ایمیج جدید نمی‌سازد — فقط یک نام جدید اضافه می‌کند. اگر می‌خواهید ایمیج جدید بسازید، از docker build یا docker commit استفاده کنید.
* حذف یک تگ، ایمیج را حذف نمی‌کند — اگر ایمیجی چند تگ داشته باشد، با `docker rmi tag` فقط همان تگ حذف می‌شود. ایمیج اصلی تا وقتی آخرین تگ حذف نشود، باقی می‌ماند:فقط تگ حذف می‌شود، nginx:latest باقی است
    * `docker rmi my-nginx:v1`
* تگ latest یک قرارداد است، نه یک قانون — داکر latest را به عنوان "آخرین نسخه" نمی‌شناسد؛ فقط یک تگ پیش‌فرض است. اگر تگ ننویسید، داکر latest را فرض می‌کند

```shell
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
docker tag nginx:latest my-nginx:v1   # حالا my-nginx:v1 و nginx:latest هر دو به یک ایمیج اشاره می‌کنند (ایمیج آی دی یکسان).
docker tag 174c8c134b2a my-app:prod   # اگر ایمیج آی دی را بدانید، می‌توانید مستقیماً از آن استفاده کنید (نیازی به نام فعلی نیست).

# Versioning
docker tag my-app:latest my-app:1.0.0
docker tag my-app:latest my-app:1.0
docker tag my-app:latest my-app:stable

# تغییر نام یک ایمیج
docker tag old-name:latest new-name:latest
docker rmi old-name:latest
```

# 3. 🅰️ Images

* نسخه برنامه یا سرویس یا سیستم‌عامل یا هرچیزی که برپایه داکر ارائه شده است و کانتینرها بر پایه آن به اجرا درخواهند آمد
* شامل تمامی مواردی که یک اپلیکیشن برای اجرا نیاز دارد شامل :[PieceOfOS] [ThirdPartyLibraries] [ApplicationsFiles] [EnvironmentsVariables]

## 3.1. 🅱️ Dockerfile

* یک فایل متنی بر پایه سینتکس خاص که در آن دستورالعمل می‌نویسیم
* نام پیش‌فرض داکر فایل Dockerfile است که اگر فایل را به این نام ساختیم و اگر در آن مسیر باشیم خودکار این فایل شناخته می‌شود
* همواره برای داکرفایل یک دایرکتوری مستقل به خود قرار دهید
* همواره از داکر ایمیج های استیبل و Base اقدام به ساخت ایمیج جدید نمایید
* هر خط از داکر فایل بعنوان یک لایه ReadOnly روی ایمیج پایه قرار می‌گیرد و پس از اجرای دستور نمی‌توان آن دستور را دستکاری کرد
* پس از اتمام اجرای خط به خط دستورات داکر فایل و بالا آمدن کانتینر یک لایه Read/Write روی کانتینر بوجود می‌آید تا بتوانیم از این کانتینر استفاده کنیم و دستور بزنیم(البته اگر بخواهیم بش بگیریم)
* بهینه‌گی در داکرفایل:
    * هنگام بیلد مجدد یک ایمیج دستورات(لایه‌ها) cache می‌شوند تا نوبت بعدی زمان صرف نشود(مگر در بیلد مجدد دستور تغییرکند) پس حتی‌المقدور دستوراتی که ثابت است را در ابتدای داکرفایل بگذارید تا تغییر نکند
    * دستور کپی همواره سبب تغییر در لایه‌ها و مانع کش نمودن است پس حتی‌المقدور کپی را در لایه‌های انتهایی داکرفایل قرار دهید تا لایه‌های قبل بتواند از کش بهره‌مند گردد

![Docker-DockerFile.jpg](_srcFiles/Images/Docker-DockerFile.jpg "Docker-DockerFile.jpg")

### 3.1.1. ✅️ FROM

:تعیین ایمیج پایه که قرار است دستورها بر روی آن اجرا شود و باید اولین خط در داکرفایل باشد

```dockerfile
FROM baseImage
FROM baseImage:tag
```

### 3.1.2. ✅️ WORKDIR

این مورد optional است و میتواند مورد استفاده واقع نگردد. سبب تغییر مسیر کنونی دایرکتوری می‌شود که قرار است ادامه فرآیند در آن واقع گردد

```dockerfile
WORKDIR /Behrooz/salam
```

### 3.1.3. ✅️ RUN

دستور هنگام ساخت Image اجرا می‌شود؛ مثلاً نصب پکیج‌ها

Execute command inside shell(When build the image)

* نکته۱:اجرای دستور جهت ایجاد یک ایمیج جدید(حین بیلد تا ایمیج پایه مد نظر تولید شود)
* نکته۲:هر دستور مستقل از دیگری است و مسیر «پی‌دبلیو دی» هر دستور / است مگر اینکه توسط دستور «وُرک‌دایر» مسیررا تغییر بدهیم
* نکته۳:دستور «سی‌اِم‌دی» برای زمانی است که ساخت ایمیج پایان یافته و قصد داریم دستور را در کانتینر ران شده اجرا می‌کنیم

```dockerfile
RUN apt-get update && apt-get install -y curl
RUN mkdir -p /behrooz/salam
```

دو دستور زیر یکسان هستند

```dockerfile
1️⃣️ docker run [imageName] npm start
2️⃣️ docker run [imageName] # if «CMD [ "npm", "start" ]» exist at end of DockeeFile
```

### 3.1.4. ✅️ CMD ► Execute command in container

دستور پیش‌فرضی است که هنگام اجرای Container اجرا می‌شود و به‌راحتی با آرگومان جایگزین می‌شود.

* نکته۱:هنگامیکه ساخت ایمیج پایان یافته است سپس قصد اجرای دستور در ایمیج ساخته شده داریم تا هربار هنگام ران گرفتن کانتینر جدید(از ایمیج ساخته شده)، دستور موردنظر به اجرا درآید و در خط فرمان آن را ندهیم
* نکته۲: تنها یک دستور «CMD» می‌توان در هر داکرفایل اجرا کرد(معمولا لایه‌های آخر[دستورآخر] از داکر فایل) و اگر چندین «سی‌اِم‌دی» داشته باشیم تنها آخرین آن به اجرا درخواهد آمد
* نکته۳یادآوری: کامند «ران»: دستوراتی بود برای ایجاد یک ایمیج جدید

```dockerfile
CMD [ "npm", "start" ] # 1️⃣️ (✅️) --> Execute Form: use current shell
CMD npm start          # 2️⃣️ (❌️) --> Shell   Form: run in new shell(/bin/sh npm start)
```

### 3.1.5. ✅️ ENTRYPOINT

بسیار شبیه دستور `CMD` است. برنامهٔ اصلی Container را مشخص می‌کند و معمولاً با آرگومان‌های CMD ترکیب می‌شود.

| ویژگی                                      | `RUN`                                 | `CMD`                                 | `ENTRYPOINT`                          |
|--------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
| **زمان اجرا**                              | هنگام `docker build`                  | هنگام `docker run`                    | هنگام `docker run`                    |
| **هدف اصلی**                               | ساخت و آماده‌سازی Image               | تعیین رفتار/آرگومان پیش‌فرض Container | تعیین برنامهٔ اصلی Container          |
| **روی Image اثر می‌گذارد؟**                | بله؛ یک Layer جدید می‌سازد            | به metadata Image اضافه می‌شود        | به metadata Image اضافه می‌شود        |
| **روی Container اثر مستقیم دارد؟**         | خیر، نتیجه‌اش داخل Image باقی می‌ماند | بله                                   | بله                                   |
| **قابل Override با `docker run`؟**         | ❌ خیر                                 | ✅ بله                                 | بستگی دارد؛ معمولاً با `--entrypoint` |
| **برای نصب Package مناسب است؟**            | ✅                                     | ❌                                     | ❌                                     |
| **برای اجرای Application اصلی مناسب است؟** | ❌                                     | ⚠️ در موارد ساده                      | ✅                                     |
| **می‌تواند آرگومان پیش‌فرض بدهد؟**         | ❌                                     | ✅                                     | ✅، ولی کاربرد متفاوت است              |
| **تعداد در Dockerfile**                    | می‌تواند چندتا باشد                   | معمولاً آخرین `CMD` مؤثر است          | معمولاً آخرین `ENTRYPOINT` مؤثر است   |
| **تأثیر روی Cache**                        | بسیار مهم؛ Layer می‌سازد              | ندارد                                 | ندارد                                 |
| **نمونه کاربرد**                           | `RUN apt install nginx`               | `CMD ["nginx", "-g", "daemon off;"]`  | `ENTRYPOINT ["nginx"]`                |

```dockerfile
ENTRYPOINT ["executable", "param1", "param2"] # 1️⃣️ (✅️) --> Execute Form: use current shell
ENTRYPOINT command param1 param2              # 2️⃣️ (❌️) --> Shell   Form: run in new shell
```

### 3.1.6. 📍️ Different CMD And ENTRYPOINT

[//]: # (Todo: بررسی مثال و مثالهای مشابه بیارم)

با فرض گزاره زیر:

```dockerfile
# //TODO بررسی مجدد این عنوان
ENTRYPOINT ["python"]
CMD ["app.py"]
```

اگر بنویسیم `docker run myimage` آنگاه داکر عملاً `python app.py` را اجرا می‌کند ولی اگر بنویسیم `docker run myimage test.py` می‌شود `python test.py` یعنی:

```text
# ENTRYPOINT +  CMD
#    ↓           ↓
#  python   +  app.py

# پس می‌توان گفت:
#    ENTRYPOINT = برنامهٔ اصلی
#    CMD = آرگومان/مقدار پیش‌فرض
```

### 3.1.7. ✅️ COPY

کپی دیتا از سیستم اصلی لینوکس به یک کانتینر و اگر دایرکتوری مقصد موجود نباشد داکر خودش آن مسیر را می‌سازد

```dockerfile
COPY [LocalMachine] [ContainerDir]
COPY /tmp/salam2 /salam2
COPY *package* /<DirectoryInDockerImages>
COPY . /[DirectoryInDockerImages]
COPY /home/FIles/Data/salam.txt /[DirectoryInDockerImages]
```

### 3.1.8. ✅️ ADD

* همانند کپی است با برخی ویژگی‌ها
* مثلا از یک «یوآراِل»استفاده شود
* یا فایل زیپ استفاده کنیم که خودکار آنزیپ کند

### 3.1.9. ✅️ ENV

Create a new EnviromnebtVariable

```dockerfile
ENV Key=Value
ENV API_URL=https://myapi.api.com/
ENV APP_PORT=8000
```

### 3.1.10. ✅️ EXPOSE port

Define the network port[s] that this container will listen on at runtime

تقریبا بابت داکیومنت کردن این رو می‌گذاریم که بگوییم این کانینترروی پورت فلان باید لیسن کند ولی باید هنگام ران کردن عمل مپ کردن پورت صورت بگیرد
اگر از داکر کامپوز استفاده شود این خط کاربرد دارد

```dockerfile
EXPOSE 8080
EXPOSE 80 443 22
EXPOSE 7000-8000
```

* [EXPOSE port]:
* USER: The user name to use درداخل کانتینر از این خط به بعد دستورات توسط کدام یوزر انجام شود
    * یوزر پیش‌فرض روت است
    * USER user #منوط به این است که نام یوزر در کانتینر موجود باشد
        * RUN addgroup user && adduser -S -G user user # ایجاد یوزر اگر یوزر موجود نبود
* MAINTAINER: نام سازنده و اطلاعات
    * MAINTAINER "behroozmn@chmail.ir"

### 3.1.11. ✅️ Example

```dockerfile
1-CreateDockerFile
   FROM python:3.9-alpine3.13
   RUN pip install flask
   CMD [ "python" , "app2.py" ]
   COPY app2.py /app2.py
2.BuildImage
   sudo docker image build -t <NewNameForNewImage> .
3.Run
   sudo docker run -p 5001:5000 <name>
```

# 4. 🅰️ Containers

* یک پردازه از اجرای یک دستور بر پایه یک ایمیج است که هرگاه دستور تمام شود آنگاه کانتینر ازبین می‌رود
* محیط‌های ایزوله که برنامه ها و پردازه‌های مستقل بخود را دارند و همه ازیک کرنل و سیستم عامل برای اجرا استفاده می‌کنند
* از نگاه سیستم عامل کانتینر یک پروسس هست
* وقتی یک ایمیج آماده باشد می‌توانیم کانتینر را روی آن اجرا نماییم


* EnginDocker:سروری که در روی آن داکر نصب شده است
    * DockerDaemon: پروسه‌اصلی داکر که در بک گراند کار می‌کند و مدیریت شبکه داکر و کانتینرها و ایمیج‌ها و غیره
    * REST API: قابلیت ارتباط برنامه‌ها با کانتینرها در بستر این سکو میسر است
    * Docker CLI: رابط فط فرمان

* cgroup یا ControlGroup: إعمال محدودیت برای کانتینرها جهت استفاده از منابع(گروهی برای محدود کردن منابع)
    * docker run--cpu=1.5 ImageName
    * docker run --memory=100m imageName

# 5. 🅰️ Network

آی پی در کانتیرها تفاوت می‌کند و هربار آی پی ممکن است تغییر کند پس اگر بخواهیم با یک کانتینر ارتباط بگیریم توصیه می‌شود که از نام استفاده نماییم تغییرات آی پی سبب بروز اشکال نشود

* Bridge:  پورت باز بصورت مجازی به کانتینر اختصاص داشته و برای هاست اصلی و دیگر کانتینرها اعمال نمی‌شود
    * docker run myImage
* None
    * docker run myImage --network=none
* Host: پورت باز دقیقا روی هاست فیزیکی باز می‌شود و در سرور فیزیکی درحال لیستِن می باشد
    * docker run myImage --network=host


* [ls]: List networks
    * docker network ls
* [connect]: Connect a container to a network
* [create]: Create a network
    * docker network create --driver bridge --subnet X.Y.W.Z/16 custom-isolated-network # Change subnet for some container
* [disconnect]: Disconnect a container from a network
* [inspect]: Display detailed information on one or more networks
    * docker network inspect bridge
* [prune]: Remove all unused networks
* [rm]: Remove one or more networks

# 6. 🅰️ Repository

نکته: عمل ارسال به ریپوزیتوری(پوش کردن) لایه به لایه انجام می‌شود یعنی اگر تنها یک لایه تغییر نماید آنگاه تنها یک لایه ارسال می‌شود

* برای آپلود به Docker Hub، نام ایمیج باید با نام کاربری شما شروع شود. docker tag این کار را انجام می‌دهد.
* برای رجیستری خصوصی، نام باید شامل آدرس رجیستری و پورت باشد.

```shell
docker login #enter user and password
docker tag <ImagNameOrID> [IdOnDockerHub]/[NewNameForVisibleOnDockerHub] #
docker push [id]/[name]
docker pull [NameOfImageOnDockerHub] #دانلود یک ایمیج داکر از روی داکرهاب
docker pull docker/whalesay #دانلود ایمیج مدنظر با حجم تقریبا۷۰مگابایت
docker run docker/whalesay cowsay salam # 

# آماده‌سازی برای push به Docker Hub
docker tag my-app:latest yourusername/my-app:1.0
docker push yourusername/my-app:1.0

# آماده‌سازی برای push به رجیستری خصوصی
docker tag my-app:latest registry.example.com:5000/my-app:v2
docker push registry.example.com:5000/my-app:v2
```

# 7. 🅰️ Deployment

* مجموعه فرآیند و اقداماتی که سبب استقرار ماشین‌های داکر می‌شود و در دو حالت استقرار تکی و کلاستر(اورکستریشن) صورت می‌پذیرد
* در دو حالت استقرار به‌صورت تکی و به‌صورت کلاستر می‌باشد
* در حالت استقرار کلاستر(Orchestration or Cluster)) شامل ابزارهایی نظیر **dockerSwarm** یا **Kubernetes** می‌باشد
    * Docker Orchestration:فرآیند مدیریت و ایجاد هماهنگی چندین کانتینر داکر
    * فرآیند شامل استقرار، مقیاس‌گذاری، و مدیریت چرخه عمر کانتینرها در یک محیط توزیع‌شده و ...
* در حالت استقرار تکی(SingleHost or ApplicationStack) نیز شامل ابزارهایی نظیر **Terraform** یا **dockerMachine** یا **ApacheMesos** می‌باشد
* در پروژه‌های کوچک ممکن است واقعاً به هر ۶ فایل نیاز نداشته باشید. مثلاً یک پروژه کوچک می‌تواند فقط `local`، `test` و `prod` داشته باشد؛ اما در پروژه‌های سازمانی، جدا کردن `dev`، `staging` و `demo` می‌تواند مرزهای عملیاتی واضح‌تری ایجاد کند.
  یک نکته بسیار مهم: Image را بین Environmentها Build نکنیم

```text
                 SOURCE CODE
                      │
                      ▼
                 Docker Build
                      │
                      ▼
                Docker Image
                      │
     ┌────────────────┼────────────────┐
     │                │                │
     ▼                ▼                ▼
  LOCAL              DEV             TEST
     │                │                │
     │                │                │
     └────────────────┼────────────────┘
                      │
                      ▼
                   STAGING
                      │
             ┌────────┴────────┐
             │                 │
             ▼                 ▼
           Check            FinalTest
             │                 │
             └────────┬────────┘
                      │
                      ▼
                    PROD                       ┌─────────────────┐
                      │                        │      DEMO       │
                      ▼                        │                 │
                  Real Users                   │ Customer / Sales│
                                               │ Presentation    │
                                               └─────────────────┘


Order: Local ► Dev ► Test ► Demo ► Staging ► Prod
```

## 7.1. 🅱️ DockerCompose

* داکر Compose بیشتر برای تعریف و اجرای چند کانتینر به‌صورت یک application stack است، نه Deployment به معنای production deployment.
* اگر بخواهیم چندین سرویس همزمان در یک ایمیج قرار داده شود تا این سرویس‌ها یکدیگر را ببینند
* باید docker-compose جداگانه نصب شود و پس از نصب می‌توان دستور docker-compose --version از صحت نصب مطلع شویم
* برای اجرای داکر کامپوز باید به مسیری برویم که فایل YML در آن موجود است
* فایل داکر کامپوز :‌همه کارها را به داکر کامپوز میدهیم و خودکار همه چیز بالا می‌آید و کاربر نقشی نخواهد داشت
* فایل باید با پسوند yml یا yaml باشد و حروف کوچک باشد
* برای هر سرویس باید داکر فایل مستقل داشت(ایمیج مستقل که در داکر فایل مختص همان سرویس مورد استفاده قرار بگیرد. یعنی دانلود کنیم یا خود داکر توسط کامپوزر دانلود نماید)

* پسوند برخی فایل‌های داکر ved مخفف develop است که حاوی تنظیماتی برای توسعه (دیباگ، reload خودکار، ابزارهای توسعه) می‌باشد
    *

**docker-compos COMMAND**

* [up]: create and start containers اگر ایمیج نباشد میرود و دانلود میکند و اگر موجود باشد آن را استارت و دستورات را اجرا میکند
    * docker-compose up
* [--build]: Build images before starting containers
* [-d]: اجرا کردن در وضعیت بک گراند
* [down]: Stop and remove containers
* [build]: Build or rebuild services
* [--no-cache]: Do not use cache when building the image
    * docker-compose build --no-cache
* [--pull]: Always attempt to pull a newer version of the image
* [-f]:‌تعیین فایل داکرکامپوز
    * docker-compose -f docker-compose1.yaml build -d
    * docker-compose -f docker-compose1.yaml up -d --build
    * docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d # Override environment variable in prod file
* [ps]: List containers
    * docker-compose ps

### 7.1.1. ✅️ DockerCompose Files Type

در Docker Compose، این نام‌گذاری‌ها معمولاً Convention پروژه هستند و خود Docker معنای رسمی و اجباری برای `dev`، `test`، `staging`، `prod`، `local` و `demo` تعریف نکرده است؛ تیم تعیین می‌کند هر فایل چه تفاوتی داشته باشد.

```text
      Local
        │
        ▼
Developer(On Laptop)
        │
        ▼
LOCAL Environment
        │
        │ git push
        ▼
DEV Environment
        │
        ▼
Automated Tests
        │
        ▼
TEST Environment
        │
        ▼
STAGING Environment
        │
        ▼
Production Approval
        │               ┌─────────────┐
        ▼               │    DEMO     │
PROD Environment        │             │
                        │ Presentation│
                        └─────────────┘
```

| محیط      | هدف اصلی             | داده واقعی         | Debug    | مقیاس/شبکه       | ریسک تغییر |
|-----------|----------------------|--------------------|----------|------------------|------------|
| `local`   | توسعه روی لپ‌تاپ     | معمولاً خیر        | زیاد     | ساده             | پایین      |
| `dev`     | توسعه مشترک تیم      | معمولاً Mock/تست   | زیاد     | متوسط            | پایین      |
| `test`    | اجرای تست خودکار     | خیر                | متوسط    | شبیه CI          | پایین      |
| `staging` | شبیه‌سازی Production | گاهی Sanitized     | کم       | بسیار شبیه Prod  | متوسط      |
| `prod`    | سرویس واقعی کاربران  | بله                | بسیار کم | واقعی/مقیاس‌پذیر | بسیار بالا |
| `demo`    | نمایش محصول          | معمولاً داده نمونه | متوسط    | کنترل‌شده        | متوسط      |

```text
project/
├── src/                         # Source Code برنامه را نگه می‌دارد
├── tests/                       # تست‌های پروژه را نگه می‌دارد
├── nginx/                       # Configurationهای Nginx را نگه می‌دارد
├── docker/                      # فایل‌ها و تنظیمات Docker را نگه می‌دارد
├── Dockerfile                   # Image اصلی برنامه را تعریف می‌کند
├── docker-compose.local.yml     # محیط شخصی Developer را تعریف می‌کند
├── docker-compose.dev.yml       # محیط توسعه مشترک را تعریف می‌کند
├── docker-compose.test.yml      # محیط تست خودکار را تعریف می‌کند
├── docker-compose.demo.yml      # محیط Demo را تعریف می‌کند
├── docker-compose.staging.yml   # محیط پیش‌تولید را تعریف می‌کند
└── docker-compose.prod.yml      # محیط Production را تعریف می‌کند

```

| ویژگی         | Local            | Dev             | Test         | Demo         | Staging                  | Prod             |
|---------------|------------------|-----------------|--------------|--------------|--------------------------|------------------|
| هدف           | توسعه شخصی       | توسعه تیمی      | تست          | نمایش        | پیش‌تولید                | کاربران واقعی    |
| محل اجرا      | Laptop           | Server/CI/Cloud | CI           | Server/Cloud | Server/Cloud             | Production Infra |
| Debug         | زیاد             | زیاد            | متوسط        | کم/متوسط     | کم                       | خاموش            |
| Hot Reload    | معمولاً بله      | ممکن است        | معمولاً خیر  | خیر          | خیر                      | خیر              |
| Source Mount  | معمولاً بله      | گاهی            | معمولاً خیر  | خیر          | خیر                      | خیر              |
| داده واقعی    | خیر              | خیر             | خیر          | خیر          | معمولاً خیر یا Sanitized | بله              |
| Seed Data     | گاهی             | گاهی            | معمولاً بله  | بسیار مهم    | گاهی                     | خیر              |
| Database      | Local            | Dev DB          | Ephemeral    | Demo DB      | Staging DB               | Production DB    |
| Redis         | Local            | Dev             | Test         | Demo         | Staging                  | Production       |
| SSL           | معمولاً خیر      | معمولاً خیر     | خیر          | ممکن است     | بله                      | بله              |
| Domain        | localhost        | dev.example     | test         | demo.example | staging.example          | example.com      |
| Secrets       | ساده             | Dev Secrets     | Test Secrets | Demo Secrets | Staging Secrets          | Secret Manager   |
| Logging       | بسیار زیاد       | زیاد            | متوسط        | متوسط        | کنترل‌شده                | کنترل‌شده        |
| Monitoring    | معمولاً خیر      | محدود           | CI logs      | محدود        | بله                      | کامل             |
| Backup        | معمولاً خیر      | معمولاً خیر     | خیر          | معمولاً خیر  | بله/اختیاری              | ضروری            |
| Availability  | مهم نیست         | متوسط           | مهم نیست     | متوسط        | بالا                     | بسیار بالا       |
| تغییرات دستی  | آزاد             | نسبتاً آزاد     | خودکار       | کنترل‌شده    | محدود                    | بسیار محدود      |
| Deployment    | دستی             | CI/CD           | CI           | CI/CD        | CI/CD                    | CI/CD            |
| Lifecycle     | دائمی روی Laptop | دائمی           | موقت         | تا زمان Demo | دائمی                    | دائمی            |
| سطح امنیت     | پایین‌تر         | متوسط           | متوسط        | متوسط        | بالا                     | بسیار بالا       |
| شباهت به Prod | کم               | متوسط           | متوسط        | کم/متوسط     | بسیار زیاد               | مرجع اصلی        |

#### 7.1.1.1. ❇️ Local ► استفاده محلی

محیط local یعنی محیطی که معمولاً روی سیستم شخصی Developer اجرا می‌شود.

* در این محیط Debug فعال است
* در این محیط Source code به کانتینر mount می‌شود
* در این محیط Hot reload وجود دارد
* در این محیط Database محلی است
* در این محیط Passwordها معمولاً ساده‌اند
* در این محیط SSL معمولاً وجود ندارد
* در این محیط Logging بسیار verbose است
* در این محیط Performance و security در اولویت دوم هستند
* نام فایل این محیط معمولا `docker-compose.local.yml` است
* مثلاً با دستور زیر بلافاصله API و Database روی لپ‌تاپ لوکال developer اجرا می‌شوند
    * `docker compose -f docker-compose.local.yml up

```dockerfile
NODE_ENV=development
LOG_LEVEL=debug
DATABASE_URL=postgresql://app:app@localhost:5432/app
```

#### 7.1.1.2. ❇️ Dev ► توسعه

محیط dev معمولاً یک محیط توسعه مشترک‌تر و کنترل‌شده‌تر است.

```text
local = محیط شخصی Developer

dev = محیط توسعه تیم

Developer A ─┐
Developer B ─┼──► Dev Environment
Developer C ─┘

```

* در این محیط Debug هنوز ممکن است فعال باشد
* در این محیط Logging نسبتاً زیاد است
* در این محیط Database مشترک است
* در این محیط Deployment ممکن است اتوماتیک باشد
* در این محیط Configuration نسبت به Local واقعی‌تر است
* هنگامی که تغییرات سریع و زیاد داریم دراین محیط اعمال می‌کنیم
* محیط dev می‌تواند محیط مشترک تیم یا یک محیط توسعه روی سرور/CI باشد.
* نام فایل این محیط معمولا `docker-compose.dev.yml` است
* در این محیط سرویس‌های خارجی ممکن است Sandbox باشند

```dockerfile
NODE_ENV=development
LOG_LEVEL=debug
DATABASE_URL=postgresql://...

```

#### 7.1.1.3. ❇️ Test ► آزمایش خودکار

هدف اصلی Test این است که آیا کدی که نوشته‌ایم درست کار می‌کند؟

```text
git push
   ↓
Build
   ↓
docker compose -f docker-compose.test.yml up
   ↓
Unit / Integration / E2E Tests
   ↓
PASS / FAIL
   ↓
Destroy
```

* در این محیط داده واقعی نداریم
* در این محیط Database موقت است
* این محیط بدلیل تست بودن باید قابل تکرار باشد
* در این محیط تست‌ها باید deterministic باشند
* در این محیط بعد از تست containerها حذف می‌شوند
    * محیط Test برای قابل‌تکرار بودن تست‌هاست؛ بنابراین معمولاً سرویس‌هایی مثل PostgreSQL/Redis موقت بالا می‌آیند و بعد از تست حذف می‌شوند.
* نام فایل این محیط معمولا `docker-compose.test.yml` است

```dockerfile
NODE_ENV=test
LOG_LEVEL=error
DATABASE_URL=postgresql://test:test@postgres:5432/test
```

#### 7.1.1.4. ❇️ Staging ► محیط آزمایش

یک نسخه کنترل‌شده و تقریباً مشابه Production برای اینکه قبل از انتشار، رفتار سیستم را بررسی کنیم.محیط Staging باید تا حد امکان به Production نزدیک باشد.

* محیط تست قبل از تولید
* محیط Staging باید تا حد امکان از نظر image، configuration، network و dependency شبیه Production باشد، اما معمولاً با داده، secrets و دامنه‌های جدا.
* نام فایل این محیط معمولا `docker-compose.staging.yml` است
* اگر بخواهیم قبل از Production، سیستم را تقریباً در شرایط واقعی امتحان کنیم

```dockerfile
NODE_ENV=production
LOG_LEVEL=info
DATABASE_URL=<staging database>
```

#### 7.1.1.5. ❇️ Production(Prod) ► محیط تولید

محیط Production که به اختصار prod هم معروف است محیطی است که کاربران واقعی از آن استفاده می‌کنند. در این محیط هدف شامل Availability و Security و Reliabilityو Backup و Monitoring و Logging و Recovery و Scalability و Zero/Low Downtime Deployment است

* در Production معمولاً نباید Secrets را مستقیماً داخل docker-compose.prod.yml قرار دهیم.
* حاوی تنظیماتی برای محیط تولید (بهینه‌سازی، امنیت، لاگینگ) می‌باشد
* در انین محیط برای سرویس نهایی تدابیر لازمه را درنظر می‌گیرند
* محیط کاربران واقعی
* `docker-compose.prod.yml` or `config.prod.json`
    * به‌طور مثال فایل `.env.prod` حاوی متغیرهای محیطی یا همان Environment در محیط پروداکشن است
* بهتر است Secret از Secret Manager یا CI/CD یا Environment امن یا مکانیزم مناسب زیرساخت دریافت شود.
* در سیستم‌های بزرگ معمولاً Database را هم داخل Compose نگه نمی‌دارند و از سرویس‌هایی مانند: Managed PostgreSQL یا Managed Redis یا Managed Kafka یا Cloud Load Balancer یا Kubernetes یا ECS یا Nomad استفاده می‌کنند.
* در داخل docker-compose.prod.yml نباید Password وجود داشته باشد و مقدار را از سیستم امن دریافت کنیم. زیرا ممکن است فایل وارد Git شود.
    * در معماری بزرگ‌تر اطلاعات امن DockerCompose اطلاعات نظیر `Database Password` و `JWT Secret` و  `API Key` و  `Encryption Key`  را از SecretManager دریافت می‌کند

```dockerfile
NODE_ENV=production
LOG_LEVEL=warn
DATABASE_URL=<productionDatabase>
POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
```

#### 7.1.1.6. ❇️ Demo ► نمایشی

محیط demo با staging یکی نیست. محیط Demo معمولاً برای موارد زیر استفاده می‌شود

* محصول به مشتری نمایش داده شود
* ویژگی‌های جدید یا همان Feature های جدید در آن present گردد
* تیم بازرگانی معمولا به آن متصل می‌گردد
* چیزی که در جلسات دمو از آن استفاده می‌گردد
* این محیط باید برای هر نوع پرزنت قابلیت ریست داشته باشد که در محل های متفاوت قابل ارائه باشد


* محیط نمایش سیستم برای کلاینت‌ها
* `docker-compose.demo.yml`
*

### 7.1.2. ✅️ Concent

یک داکر کامپوز شامل موارد زیر است

* اولین خط همواره باید ورژن باشد و عدد آن باید مطابق با ورژن «Docker Engine» باشد که مثلا در ورژن‌های داکر بالاتر از 19.03 می‌توان ورژن را ۳.۸ قرار داد
* هرکدام از سرویس‌ها یک سرور با آی‌پی مستقل خواهند بود یعنی اگر داخل هرکدام دیگری را پینگ کنیم پاسخ را خواهیم گرفت(دستور پینگ و نام هاست را نام سرویس می‌گذاریم یعین ping web)


* version: # اولین خط همیشه باید تعیین ورژن باشد
    * ورژن رو باید با توجه به نسخه داکر هاست تعیین کنین که در سایت داکر نیز آمده است
* services: هرکدام از سرویس‌های دلخواه که بخواهیم بالا بیاوریم
* serviceName: هر نام دلخواه می‌توان قرار داد
    * در مثال زیر کلمه دلخواه «وِب» برای «فرانت‌اِند» انتخاب کردیم و «اِی‌پی‌آی» برای «بَک‌اِند» و کلمه دلخواه «دی‌بی» برای دیتابیس است
* build: تعیین مسیر داکرفایل مختص سرویس برای بیلد کردن
* context:‌وقتی بخواهیم در بیلد یک داکر فایل خاص استفاده نماییم باید مسیر را توسط این عبارت به همراه کلیدواژه «داکرفایل»با مقدار «نام فایل» مشخص نماییم
* image: استفاده از ایمیج خاص و عدم بیلد کردن و استفاده از کانتینر
* environment #تعریف متغیرهای محلی در ایمیج
*
    - DB_URL=mongodb://db/mydb #هردو شکل صحیح است
* DB_URL: mongodb://db/mydb
* volumes #اتصال مسیر خاصی از سیستم لینوکس اصلی به کانتینر
* `- ./DireName:/app` #در مسیر کنونی با نام خاص را به مسیر «اَپ» در درون کانتینر متصل می‌کند
* command: اجرای یک دستور در کانتینر
    * میتوا ن همه کارها را درون یک شل ایجاد کرد و فقط به دستور بگوییم آن شل را اجرا بکند
* restart #وقتی یک کانتینر کرش می‌کند چه اتفاقی رخ دهد
    * always: همواره هنگام کرش کردن ریست کند
    * no: هنگام کرش کردن ریست نکند
    * unless-stopped: ریست هنگام استاپ کردن سرویس

### 7.1.3. ✅️ Commands

```shell
docker-compose -f docker-compose-prod.yaml build
```

### 7.1.4. ✅️ Example

```dockerfile
version: "3.8"
services:
    web:
        build:
            context: ./frontend
            dockerfile: Dockerfile.prod
        ports:a
            - 3000:3001
    api:
        build:./backend
        ports:
            -  3001:3001
        environment:
            - DB_URL2=mongodb://db/mydb
        volumes:
            - ./DireName:/app
        command: ./MyScript.sh
    db:
        image: mongo:4.0-xenial
        ports:
            - 27017:27017
        volumes:
            - mydb:/data/db
volumes:
    mydb:
```

![Docker-compose.jpg](_srcFiles/Images/Docker-compose.jpg "Docker-compose.jpg")

## 7.2. 🅱️ dockerMachine(منسوخ شده)

* لایه اجرایی آن قابلیت اجرای دستور docker در هاست‌های ریموت می‌دهد
* منطق لایه زیرساختی داکر ماشین به شکل زیر است
    * 1️⃣️ سیستم میزبان (Host): کامپیوتر فیزیکی شما با ویندوز، مک یا لینوکس.
    * 2️⃣️ مجازی‌ساز (Hypervisor): نرم‌افزاری که قبلاً باید نصب شده باشد، مانند VirtualBox، VMware یا Hyper-V. این لایه مسئول مدیریت منابع سخت‌افزاری و ساخت ماشین‌های مجازی است
    * 3️⃣️ Docker Machine: یک ابزار خط فرمان (CLI) که روی سیستم میزبان نصب می‌شود. این ابزار از طریق درایورهایش (مثل virtualbox، hyperv) به مجازی‌ساز دستور می‌دهد تا یک ماشین مجازی بسازد، یک سیستم‌عامل کوچک لینوکسی (boot2docker) روی آن نصب کند و داخل آن Docker Daemon را راه‌اندازی کند
    * 4️⃣️ Docker Daemon داخل VM: این دقیقاً همان چیزی است که به آن "Docker Machine" می‌گویند؛ یعنی یک محیط Docker که جدا از Docker محلی روی سیستم میزبان شماست.
* اگر می‌خواهید از Docker Machine استفاده کنید، ابتدا باید VirtualBox، Hyper-V یا VMware را نصب کنید.سپس Docker Machine را نصب کرده و با دستور docker-machine create ماشین مجازی مورد نظر را بسازید
* وقتی برای اولین بار Docker Machine را نصب و راه‌اندازی می‌کنید این ابزار به طور خودکار یک ماشین مجازی می‌سازد و نام آن را default می‌گذارد.(پس اگر نام default را برای ماشین دیدید بدانید یک کلمه رزرو شده نیست)

```text
┌────────────────────────────────────────────────────────────────────────────────────┐
│   Layyer1: Hardware(CPU, RAM, Disk)                                                │
├────────────────────────────────────────────────────────────────────────────────────┤
│   Layyer2: Local OS(Windows / macOS / Linux)                                       │
├────────────────────────────────────────────────────────────────────────────────────┤
│   Layyer3: Hypervisor (VirtualBox | Hyper-V | VMware )                             │
│                                                                                    │
│    Docker                               VirtualBox                                 │
│   ┌──────────────────────────────┐   ┌──────────────────────────────────────────┐  │
│   │  Docker Daemon localhost     │   │  Linux: boot2docker                      │  │
│   │                              │   │  ┌────────────────────────────────────┐  │  │
│   │   ┌───────┐    ┌──────────┐  │   │  │   VM: default                      │  │  │
│   │   │  C1   │    │    C2    │  │   │  │  ┌──────────────────────────────┐  │  │  │
│   │   │ nginx │    │ Database │  │   │  │  │  DockerDaemon(DockerMachine) │  │  │  │
│   │   └───────┘    └──────────┘  │   │  │  │                              │  │  │  │
│   │                              │   │  │  │  ┌───────┐ ┌───────┐         │  │  │  │
│   │   ┌───────┐    ┌───────┐     │   │  │  │  │  X1   │ │  X2   │         │  │  │  │
│   │   │  C3   │    │  C4   │     │   │  │  │  │ mysql │ │ mongo │         │  │  │  │
│   │   │ kafka │    │  App  │     │   │  │  │  └───────┘ └───────┘         │  │  │  │
│   │   └───────┘    └───────┘     │   │  │  └──────────────────────────────┘  │  │  │
│   │                              │   │  └────────────────────────────────────┘  │  │
│   └──────────────────────────────┘   └──────────────────────────────────────────┘  │
│                                                                                    │
├────────────────────────────────────────────────────────────────────────────────────┤
│                    ┌──────► docker                                                 │
│   Layyer4: CLI  ───┤                                                               │
│                    └──────► docker-machine                                         │
└────────────────────────────────────────────────────────────────────────────────────┘
```

* از سال ۲۰۱۲ به بعد منسوخ شده است و دیگر پشتیبانی نمی‌شود
* یکی ابزارهای نصب و مدیریت داکر درهاست‌های مجازی ریموت(می‌تواند لوکال باشد یا ریموت یا کلود باشد)
* با دستور `docker-machine` می‌توان در سرور ریموت کارهایی نظیر استارت و استاپ و بررسی سرویس بروزرسانی سرویس و تنظیمات داکر را انجام داد
* ابزارهای دیگر نظیر terraform هم هست که این کار را می‌کند
* در بستر اینترنت شرکت یا سایت digitalOcean و AWS که مخفف Amazon Web Services است ماشین مجازی ارائه می‌دهند
* در digitalOcean به ماشین مجازی droplet می‌گویند که حاوی رم و سی پی یو و جزییات دیگر است که هنگام ساخته شدن باید تعریف شود
* برای ارتباط گرفتن با شرکت های ارائه دهنده خدمات کلود(مثلا ماشین مجازی) توسط کامندلاین باید در چهار چوب API ارائه شده توسط این سایت‌ها اقدام نماییم و برای ارتباط حتما باید token ایجاد نماییم و توسط آن توکن دستورات را به شرکت میزبان ارائه دهنده ماشین مجازی کلود بدهیم(معمولا در منوی API دنبال ایجاد توکن ساختن بگردید)
* توسط دستور docker-machine می‌توان یک ماشین مجازی توسط کامند لاین در سایت دیجیتال اوشن ساخت که به اصطلاح می‌گویند ماشین مجازی provision می‌کنیم

```shell
docker-machine ls
docker-machine ssh default <Command>
docker-machine ip <ContainerName>
docker-machine --version #Current version is 19.03.9
docker-machine rm machineName -f #حذف یک ماشین ساخته شده
docker-machine create --driver digitalocean --digitalocean-access-token TokenID --digitalocean-image ubuntu-18-04-x64 --engine-install-url "https://release.rancher.com/install-docker/19.03.9.sh" ServerName
docker-machine ls
docker-machine ssh MachineName #اتصال به یوزر روت ماشین مجازی کلود موجود در دیجیتال اوشن
```

### 7.2.1. ✅️ DockerMachine Environments

1️⃣️ این دستور را در داخل bash لوکال خود اجرا کنید تا متغیرهای محلی داکر ماشین(نصب شده در داخل سیستم خودمان) را نمایش دهد.سپس باتنظیم آن در bash خود(بعنوان Environment Variable) می‌توانیم به docker-machine لوکال سیستم خود متصل شویم

```shell
docker-machine env <MachineName> # show environments variable
```

2️⃣️ تنظیم متغیرهای محلی در شل سیستم خود

```shell
eval $(docker-machine env machineName)

#                       ┌───► eval $(docker-machine env -u)           
# unset Environments ───┤                         
#                       └───► unset DOCKER_TLS_VERIFY DOCKER_HOST DOCKER_CERT_PATH DOCKER_MACHINE_NAME   
```

3️⃣️ از این پس هر دستوری بزنیم گویا در داخل دکر ماشین میزنیم. به‌طور مثال دستور زیر در داخل داکر ماشین اجرا میشود و نه داکر localhost خودمان

```shell
docker-compose -f docker-compose1.yaml build -d
```

![dockerMachine01.jpg](_srcFiles/Images/dockerMachine01.jpg "dockerMachine01.jpg")

## 7.3. 🅱️ swarm

* محصول شرکت داکر است یا به عنوانی Orchestration Tools از شرکت داکر است

```shell
# [--advertise-addr string] # تعیین یک نود بعنوان مستر  
docker swarm init 
docker swarm init --advertise-addr 10.116.0.2 # PrivateIp_OfContainer_From_DigitalOcean #افزودن یک نود بعنوان گره اصلی
docker swarm join --token SWMTKN-1-137q7uuogt4slnhar6b68nid7e33sgtkgkr 10.116.0.2:2377 # اضافه کردن گره اسلِیو به گره اصلی ایجاد شده
       # هر نود که میخاهیم به کلاستر اضافه شود از این دستور استفاده می‌کنیم
docker node ls #list nodes
docker swarm join-token worker # نمایش دستوری که می‌توانیم با آن یک نود جدید به کلاستر اضافه کنیم(این دستور را باید در مستر بزنیم و دستور «جوین شدن» را باید در اسلیو بزنیم)

```

## 2.19. 📍️docker stack


```shell
# cat docker-compose.yml ┐
#                        │
#                        ▼
# ╔═════════════════════════════════════════════╗
# ║ version: "3.8"
# ║ 
# ║ services:
# ║   web:
# ║     image: dblearn/web
# ║     ports:
# ║       - 80:80
# ║     restart: always
# ║   api:
# ║     image: dblearn/api
# ║     ports:
# ║       - 3001:3001
# ║     environment:
# ║       DB_URL: mongodb://db/mydb
# ║     command: ./docker-entrypoint.sh
# ║     restart: always
# ║   db:
# ║     image: mongo:4.0-xenial
# ║     ports:
# ║       - 27017:27017
# ║     volumes:
# ║       - mydb:/data/db
# ║     restart: always
# ║ volumes:
# ║   mydb:
# ╚═══════════════════════════════════════════╝

docker stack deploy --compose-file <docker-compose.yml> MyApp # دستور استقرار استک در سوآرم
docker stack services myapp # مشاهده سرویس‌های استک
docker stack ps myapp #مشاهده وضعیت تسک‌ها
docker stack rm myapp # حذف استک


# ---------- مدیریت استک (Stack) ----------
docker stack ls                                                        # لیست تمام استک‌های در حال اجرا
docker stack deploy -c docker-compose.yml MyApp                        # استقرار استک با نام MyApp
docker stack deploy -c docker-compose.yml --with-registry-auth MyApp   # استقرار با احراز هویت رجیستری
docker stack deploy -c docker-compose.yml --prune MyApp                # حذف سرویس‌های قدیمی که در فایل نیستند
docker stack deploy -c docker-compose.yml --resolve-image always MyApp # همیشه ایمیج را از رجیستری بگیر
docker stack deploy -c docker-compose.yml --detach=false MyApp         # اجرا به صورت attached (نمایش لاگ)
docker stack services MyApp                          # لیست سرویس‌های استک MyApp
docker stack services MyApp --filter name=web        # فیلتر سرویس‌ها بر اساس نام
docker stack ps MyApp                                # لیست تسک‌های استک MyApp
docker stack ps MyApp --filter desired-state=running # فیلتر تسک‌های در حال اجرا
docker stack ps MyApp --no-trunc                     # نمایش کامل اطلاعات تسک‌ها
docker stack rm MyApp                                # حذف استک MyApp
docker stack rm MyApp --detach=false                 # حذف با نمایش پیشرفت
docker stack config -c docker-compose.yml            # نمایش کانفیگ نهایی استک

# ---------- مدیریت سرویس‌ها (Service) ----------
docker service ls                                    # لیست تمام سرویس‌ها
docker service ps <service>                          # وضعیت تسک‌های یک سرویس
docker service logs <service>                        # مشاهده لاگ‌های یک سرویس
docker service scale <service>=<number>              # تغییر تعداد replicaهای یک سرویس
docker service update <service>                      # به‌روزرسانی یک سرویس
docker service rm <service>                          # حذف یک سرویس
docker service inspect <service>                     # نمایش جزئیات کامل یک سرویس

# ---------- مدیریت نودها و Swarm ----------
docker swarm init                                    # راه‌اندازی Swarm روی این نود
docker swarm join --token <token> <ip>:<port>        # پیوستن به Swarm موجود
docker node ls                                       # لیست نودهای Swarm
docker node ps                                       # لیست تسک‌های در حال اجرا روی نودها
docker node inspect <node>                           # نمایش جزئیات یک نود
docker node update --availability drain <node>       # تخلیه یک نود (خارج کردن از سرویس‌دهی)


```



## 7.4. 🅱️ terraform

* ابزار متن‌باز برای مدیریت زیرساخت به عنوان کد.
* ابزارهای دیگر نظیر DockerMachine هم هست که این کار را می‌کند
* توسط HashiCorp توسعه یافته است
* این ابزار به کاربران اجازه می‌دهد تا زیرساخت‌های خود را با استفاده از یک زبان پیکربندی(declarative)تعریف کنند
* ابزاری برای automate کردن ریسورسها و زیرساخت‌ها
* ساپورت IAC که مخفف Infrastructure as Code است
* Terraform به عنوان یک ابزار IAC عمل می‌کند.
* با استفاده از Terraform، کاربران می‌توانند زیرساخت‌های خود را به صورت کد تعریف کرده و آن‌ها را به صورت خودکار مدیریت کنند.
* از زبان HCL (HashiCorp Configuration Language) برای تعریف زیرساخت‌ها استفاده می‌کند
* می‌تواند با ارائه‌دهندگان مختلف ابری (مانند AWS، Azure، Google Cloud) و همچنین منابع محلی کار کند.

## 7.5. 🅱️ dockerSwarm

* فراهم سازی امکان مدیریت و استقرار کلاستر
* شرکت داکر برای استقرار این نسخه را توصیه می‌نماید زیرا ابزار Orchestration شرکت داکر است

## 7.6. 🅱️ Kubernetes

* پیاده سازی شده توسط شرکت گوگل
* متن‌باز یا همان OpenSource
* استفاده گسترده‌ در صنعتIT
* امکانات پیشرفته‌تر نسبت به Docker Swarm

# 8. 🅰️ dockerignore

* فایل sockerignore که شروع آن با یک نقطه است(برای شناساندن به سیستم‌عامل‌ها که این فایل از نوع مخفی است) برای نادیده گرفتن فایل‌ها و دایرکتوری‌ها می‌باشد.
* مثال: هنگام کپی تمام محتوی یک دایرکتوری که ذیل آن یک دایرکتوری ignore شده وجود دارد، دراین حالت پوشه ignore شده کپی نمی‌شود

```shell
Diretory/ #نادیده گرفتن یک دایرکتوری
```

</div>


