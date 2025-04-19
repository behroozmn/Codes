# 1.Commands

## 1.1.pip

> pip commnad options

* [Command]
    * list # لیستی از بسته‌های نصب شده با ورژن
        * `pip list`
    * freeze # لیستی از بسته‌های نصب شده با ورژن
        * `pip freeze`
        * `pip freeze > requirements.txt`
    * install #دانلود و نصب بسته
        * `pip install PyYAML==6.0`
        * `python -m pip install Django==3.0.3 --user`
        * `pip install --upgrade -r requirements.txt`
    * download #دانلود بسته
    * check #بررسی سلامت سازگاری و وابستگی‌های یک بسته
    * uninstall #حذف بسته
    * show #نمایش اطلاعات یک بسته نصب شده
    * search #Search PyPI for packages
    * inspect #show Details about Environment
    * config #Manage local and global configuration
* [Optional]
    * [-r filename.txt] # خواندن از یک فایل که حاوی وابستگی‌های ماژول یا برنامه است
        * `pip download -r ./requirements.txt`
    * [--upgrade]
        * `pip install --upgrade PyYAML`

<div style="direction:rtl;">

- ریپوزیتوری pypi یا Python Package Index مخزن رسمی بسته‌های نرم‌افزاری پایتون می‌باشد که با دستور pip می‌توان از آن استفاده کرد
- در پایتون در pip3 منظور از آرگومان -m این است که یک ماژول را به عنوان یک برنامه اجرایی، اجرا کن!
    - pip
- موارد مشابه pip وجود دارد نظیر: Pipenv - Conda - Poetry

</div>

## 1.2.python

> python Command option

* [command]
    * version
        * `python3 --version`
* [optional]
    * [-m pipe]
        * `python3 -m pip --version`

## 1.3.pythom3

> python3 Command option

* [command]
    * manage.py #Django commands
        * `python3 manage.py` [Django]show help and SubCommands
        * `python3 manage.py runserver` [Django]Boot and startup Django project on port 8000
            * `python3 manage.py runserver 8001`  [Django] change port
            * `python manage.py startapp myNewApp` [Django]
                * افزودن یک ماژول یا به‌اصلاح یک اپلیکیشن(یک پوشه)جدید به‌پروژه
                * ولی همچنان مدیریت اصلی برنامه با پوشه اصلی است
                * شکستن پروژه بزرگ به ماژول یا برنامه کوچک‌تر تا بتوانیم هر کدام از قسمت‌ها را مستقل مدیریت کنیم
            * `python3 manage.py makemigrations` [Django]  جستجوی تغییرات مدل
              #نکته: به هیچ عنوان به محتویات پوشه «ماگریشن» دستکاری نکنید و این موارد باید اتوماتیک ساخته شوند
                * `python3 manage.py migrate` [Django]  اعمال تغییرات مدل در دیتابیس
                    * تمامی ماگریشن های ایجاد شده را در دیتابیس اعمال نماییم
            * `python3 manage.py shell` [Django]  دسترسی به شل یا همان پایتون کنسول
            * `python manage.py createsuperuser` [Django] ایجاد یوزر ادمین جنگو

## 1.4.django-admin

* [Command]
    * [] اگر خالی باشد نمایش لیستی از دستورات در دسترس از جنگو
        * `django-admin`
    * [startproject name]
        * ```django-admin startproject MyProject < Director >``` Create DjangoTemplate

## 1.5.apt

> apt command options

* [commands]
    * install # نصب
        * `sudo apt install python3-PackageName` #نصب بسته در محدوده سیستمی و نه یک پروژه یعنی همه جای سیستم عامل دسترس خواهد بود

## 1.6.pipdeptree

> pipdeptree|nl #نمایش وابستگی‌ها در فرمت فایل نیازمندی‌ها

---

# 2.Install Offline

## 2.1.[install from local Archive](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-local-archives)

### 2.1.1.روش اول

1. mkdir <span style="color:red;">/tmp/</span><span style="color:purple;">download</span>
2. vim <span style="color:red;">/tmp/</span><span style="color:lightgreen;">requirements.txt</span>
    - wadllib==1.3.6
    - webcolors==1.11.1
    - webencodings==0.5.1
    - websocket-client==1.2.3
    - Werkzeug==2.2.2
3. cd download
4. pip download -r <span style="color:red;">/tmp/</span><span style="color:lightgreen;">requirements.txt</span>
5. python3 -m pip install --no-index --find-links=file://<span style="color:red;">/tmp/</span><span style="color:purple;">download</span> wadllib webcolors webencodings websocket-client Werkzeug

### 2.1.2.روش دوم

- python3 -m pip install <span style="color:lightgreen;">./downloads/SomeProject-1.0.4.tar.gz</span>
- python3 -m pip install --no-index --find-links=<span style="color:lightgreen;">file:///local/dir/ </span><span style="color:purple;">SomeProject</span>
- python3 -m pip install --no-index --find-links=<span style="color:lightgreen;">/local/dir/ </span><span style="color:purple;">SomeProject</span>
- python3 -m pip install --no-index --find-links=<span style="color:lightgreen;">relative/dir/ </span><span style="color:purple;">SomeProject</span>



