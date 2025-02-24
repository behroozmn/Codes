<div style="direction:rtl;">

## توضیحات

---

- ریپوزیتوری pypi یا Python Package Index مخزن رسمی بسته‌های نرم‌افزاری پایتون می‌باشد که با دستور pip می‌توان از آن استفاده کرد
- در پایتون در pip3 منظور از آرگومان -m این است که یک ماژول را به عنوان یک برنامه اجرایی، اجرا کن!
    - pip
- موارد مشابه pip وجود دارد نظیر: Pipenv - Conda - Poetry

</div>

# pip commnad [options]

### COMMAND

- [list] # لیستی از بسته‌های نصب شده با ورژن
    - `pip list`
- [freeze] # لیستی از بسته‌های نصب شده با ورژن
    - `pip freeze`
    - `pip freeze > requirements.txt`
- [install] #دانلود و نصب بسته
    - `pip install PyYAML==6.0`
    - `python -m pip install Django==3.0.3 --user`
    - `pip install --upgrade -r requirements.txt`
- [download] #دانلود بسته
- [check] #بررسی سلامت سازگاری و وابستگی‌های یک بسته
- [uninstall] #حذف بسته
- [show] #نمایش اطلاعات یک بسته نصب شده
- [search] #Search PyPI for packages
- [inspect] #show Details about Environment
- [config] #Manage local and global configuration

### [Options]

- [-r filename.txt] # خواندن از یک فایل که حاوی وابستگی‌های ماژول یا برنامه است
    - `pip download -r ./requirements.txt`
- [--upgrade]
    - `pip install --upgrade PyYAML`



# [install from local Archive](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-local-archives)

### روش اول

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

### روش دوم

- python3 -m pip install <span style="color:lightgreen;">./downloads/SomeProject-1.0.4.tar.gz</span>
- python3 -m pip install --no-index --find-links=<span style="color:lightgreen;">file:///local/dir/ </span><span style="color:purple;">SomeProject</span>
- python3 -m pip install --no-index --find-links=<span style="color:lightgreen;">/local/dir/ </span><span style="color:purple;">SomeProject</span>
- python3 -m pip install --no-index --find-links=<span style="color:lightgreen;">relative/dir/ </span><span style="color:purple;">SomeProject</span>



