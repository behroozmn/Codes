# 1.Linux Command

- sudo apt install python3-PackageName #نصب بسته در محدوده سیستمی و نه یک پروژه یعنی همه جای سیستم عامل دسترس خواهد بود

----

# 2.python Command

- python3 --version
- python3 -m pip --version

---

# 3.Django

* `python3 manage.py` # show help and SubCommands
* `python3 manage.py runserver` #Boot and startup Django project on port 8000
* `python3 manage.py runserver 8001` # change port
*
* `python manage.py startapp myNewApp` # افزودن یک ماژول یا به‌اصلاح یک اپلیکیشن(یک پوشه)جدید به‌پروژه ولی همچنان مدیریت اصلی برنامه با پوشه اصلی است\
  شکستن پروژه بزرگ به ماژول یا برنامه کوچک‌تر تا بتوانیم هر کدام از قسمت‌ها را مستقل مدیریت کنیم
*
* `python3 manage.py makemigrations` # جستجوی تغییرات مدل\
  #نکته: به هیچ عنوان به محتویات پوشه «ماگریشن» دستکاری نکنید و این موارد باید اتوماتیک ساخته شوند
*
* `python3 manage.py migrate` # اعمال تغییرات مدل در دیتابیس
  # تمامی ماگریشن های ایجاد شده را در دیتابیس اعمال نماییم

* `python3 manage.py shell` # دسترسی به شل یا همان پایتون کنسول
---

# 4.Other Command

- pipdeptree|nl #نمایش وابستگی‌ها در فرمت فایل نیازمندی‌ها

