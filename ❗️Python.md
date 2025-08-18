<div dir="rtl">

# 🅰️ Name Conventions

* جدولNaming Conventions برای نامگذاری عناصر استفاده شونده در کدنویسی

| نوع نامگذاری              | فرمت نام                       | قوانین و قراردادها                                        | مثال                                   | توضیحات                                        |
|---------------------------|--------------------------------|-----------------------------------------------------------|----------------------------------------|------------------------------------------------|
| متغیرهای معمولی           | `snake_case`                   | حروف کوچک، جداکننده با `_`                                | `user_name`, `total_price`             | برای متغیرهای محلی و عمومی                     |
| توابع                     | `snake_case`                   | مشابه متغیرها، حروف کوچک و جداکننده با `_`                | `calculate_tax()`, `load_data()`       | همواره از فعل استفاده کنید                     |
| کلاس‌ها                   | `CamelCase`                    | تمام کلمات با حرف بزرگ شروع می‌شوند (UpperCamelCase)      | `UserProfile`, `DatabaseManager`       | اسم‌ها هستند، نه فعل                           |
| ثابت‌ها                   | `UPPER_SNAKE_CASE`             | تمام حروف بزرگ، جداکننده با `_`                           | `MAX_USERS`, `DEFAULT_TIMEOUT`         | مقدارهای غیرقابل تغییر                         |
| ماژول‌ها                  | `snake_case`                   | نام فایل‌های `.py` باید کوچک و بدون خطوط تیره (`-`) باشد  | `utils.py`, `data_parser.py`           | اجتناب از حروف بزرگ                            |
| پکیج‌ها                   | `snake_case`                   | مشابه ماژول‌ها، نام پکیج‌ها نیز باید کوچک باشد            | `mypackage/`, `app_helpers/`           | از `_` در صورت نیاز استفاده کنید               |
| متغیرهای خصوصی            | `_single_leading_underscore`   | یک `_` در ابتدای نام = قرارداد خصوصی بودن                 | `_internal_value`                      | فقط درون ماژول/کلاس استفاده شود                |
| متغیرهای خصوصی قوی        | `__double_leading_underscore`  | دو `_` در ابتدای نام = Name Mangling در کلاس‌ها           | `__secret_key`                         | برای جلوگیری از تداخل در کلاس‌های فرزند        |
| متغیرهای خصوصی و داخلی    | `_single_trailing_underscore_` | یک `_` در انتهای نام = حل تداخل با کلمات کلیدی پایتون     | `class_`, `type_`                      | مثل وقتی که نمی‌توانید از `class` استفاده کنید |
| متغیرهای موقت / لوپ       | `i`, `j`, `k`                  | برای شمارنده‌های ساده حلقه                                | `for i in range(10):`                  | فقط در حلقه‌های کوتاه                          |
| متغیرهای محاسباتی         | `x`, `y`, `z`                  | برای مقادیر عددی ساده و محاسباتی                          | `x = 5`, `coordinates = (x, y)`        | مخصوص متغیرهای ریاضی                           |
| متغیرهای بولی             | `is_`, `has_`, `should_`       | ابتدا با افعال منفی/مثبت شروع می‌شوند                     | `is_valid`, `has_permission`           | جواب بله/خیر دارند                             |
| متغیرهای توابع lambda     | `func`, `lambda_func`          | نام‌های کوتاه و معنادار برای توابع lambda                 | `func = lambda x: x*2`                 | از نام‌های غیرمعنادار مانند `f` اجتناب کنید    |
| متغیرهای مرتبط با تست     | `test_`, `fixture_`            | برای توابع تست در فریم‌ورک‌هایی مانند `pytest`            | `test_login()`, `fixture_user()`       | تشخیص آسان توابع تست                           |
| متغیرهای مرتبط با GUI     | `on_`, `btn_`, `lbl_`          | نام‌ها براساس نوع المان UI                                | `on_submit()`, `btn_save`, `lbl_title` | خوانایی بالا در برنامه‌های گرافیکی             |
| متغیرهای اشاره‌گر به تابع | `callback`, `handler`          | نام‌های استاندارد برای متغیرهایی که به تابع اشاره می‌کنند | `event_handler`, `success_callback`    | مخصوص callback ها                              |
| متغیرهای دیتابیس          | `db_`, `cursor`, `conn`        | نام‌های استاندارد برای متغیرهای دیتابیس                   | `db_connection`, `cursor.execute()`    | واضح‌سازی منبع داده                            |
| متغیرهای JSON / API       | `payload`, `response`, `data`  | نام‌های استاندارد برای مدیریت داده‌های JSON و API         | `payload = {'name': 'Ali'}`            | سازگاری با API ها                              |

# 🅰️ Persian Tools

* برای استفاده از کاراکترهای «یونیکد فارسی» یا هر زبانی در سورس کدهای پایتون، باید از این هدر در بالای کد استفاده شود
    * `-*- coding: utf-8 -*-`
    * در این حالت مفسر کد را به صورت یونی کد می‌خواند و می تواند فارسی در آن بنویسید
* برای اینکه تمام رشته‌های STR در پایتون به صورت UNICODE تعریف شوند باید در ابتدای فایل این کلاس را ایمپورت کنیم
    ```python
    from __future__ import unicode_literals
    ```

# 🅰️Database

## 🅱️ SQLlight

```python
import sqlite3

connection = sqlite3.connect("/tmp//my-database.db")
cursor = connection.cursor()

# 1️⃣️
sql = """
    CREATE TABLE IF NOT EXISTS user (
        userId INTEGER ,
        name VARCHAR (60),
        family VARCHAR (60),
        email VARCHAR (60)
    );
"""

cursor.execute(sql)
connection.commit()
connection.close()

# 2️⃣️ Multiple sql command

sql = """
    INSERT INTO Product VALUES (2,'kotlin course',3000,'this is kotlin course');
    INSERT INTO Product VALUES (3,'vue course',4000,'this is vue course');

"""
cursor.execute(sql)
cursor.executescript(sql)

# 3️⃣️

sql = """
    SELECT * FROM Product WHERE description LIKE "%python%"
"""
cursor.execute(sql)
for product in cursor:
    print(product)
```

# 🅰️ GUI

## 🅱️ tkinter

### ✅️ Lable

```python
from tkinter import *

root = Tk()

root.title("new python Desktop-GUI")

label = Label(root, text='this is test label')
label.place(x=10, y=50)

label_2 = Label(root, text='this is second test label')
label_2.place(x=10, y=70)

root.mainloop()

```

### ✅️ Button

```python
from tkinter import *
import tkinter.font as font

from matplotlib.ft2font import ITALIC

tkWnd = Tk()
tkWnd.title("button")
tkWnd.geometry('400x300')
tkWnd.resizable(width=False, height=False)
# tkWnd.configure(bg='white')
# tkWnd['bg']='green'
tkWnd['bg'] = '#FFFFFF'

my_name = StringVar()


def print_my_name():
    my_name.set('my name is Mohammad')


myFont = font.Font(family='Vazir', size=10, weight='bold')
btn = Button(tkWnd, text="show my name!", bg='blue', fg='red', width=20, height=1, font=myFont, command=lambda: print_my_name())
btn.place(x=10, y=10)

label = Label(tkWnd, textvariable=my_name)
label.place(x=10, y=50)

tkWnd.mainloop()

```

### ✅️ Calculator پوسته

```python
from tkinter import *

# ========================== settings ========================
root = Tk()
root.geometry('400x200')
root.title('calculator')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# ========================== frames ==========================
top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)

# ========================== Buttons ==========================

btn_plus = Button(top_third, text="+", width=10, highlightbackground=color)
btn_plus.pack(side=LEFT, padx=10, pady=10)

btn_minus = Button(top_third, text="-", width=10, highlightbackground=color)
btn_minus.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_third, text="*", width=10, highlightbackground=color)
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_third, text="/", width=10, highlightbackground=color)
btn_div.pack(side=LEFT, padx=10, pady=10)

# ========================== Entries and Labels ==========================

label_first_num = Label(top_first, text='Input Number 1: ', bg=color)
label_first_num.pack(side=LEFT, pady=10, padx=10)

first_num = Entry(top_first, highlightbackground=color)
first_num.pack(side=LEFT)

label_second_num = Label(top_second, text='Input Number 2: ', bg=color)
label_second_num.pack(side=LEFT, pady=10, padx=10)

second_num = Entry(top_second, highlightbackground=color)
second_num.pack(side=LEFT)

res = Label(top_forth, text='Result: ', bg=color)
res.pack(side=LEFT, pady=10, padx=10)

res_num = Entry(top_forth, highlightbackground=color)
res_num.pack(side=LEFT)

root.mainloop()

```

### ✅️ Calculator

```python
from tkinter import *
import tkinter.messagebox

# ========================== settings ========================
root = Tk()
root.geometry('400x200')
root.title('calculator')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# ========================== variables ==========================

num1 = StringVar()
num2 = StringVar()
res_value = StringVar()

# ========================== frames ==========================
top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)


# ========================== Functions ==========================

def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'something went wrong')
    elif ms == 'division zero error':
        tkinter.messagebox.showerror('Division Error', 'Can Not Divide By 0')


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')


def div():
    if num2.get() == '0':
        errorMsg('division zero error')
    elif num2.get() != '0':
        try:
            value = float(num1.get()) / float(num2.get())
            res_value.set(value)
        except:
            errorMsg('error')


# ========================== Buttons ==========================

btn_plus = Button(top_third, text="+", width=10,
                  highlightbackground=color, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=10, pady=10)

btn_minus = Button(top_third, text="-", width=10,
                   highlightbackground=color, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_third, text="*", width=10,
                 highlightbackground=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_third, text="/", width=10,
                 highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=10, pady=10)

# ========================== Entries and Labels ==========================

label_first_num = Label(top_first, text='Input Number 1: ', bg=color)
label_first_num.pack(side=LEFT, pady=10, padx=10)

first_num = Entry(top_first, highlightbackground=color, textvariable=num1)
first_num.pack(side=LEFT)

label_second_num = Label(top_second, text='Input Number 2: ', bg=color)
label_second_num.pack(side=LEFT, pady=10, padx=10)

second_num = Entry(top_second, highlightbackground=color, textvariable=num2)
second_num.pack(side=LEFT)

res = Label(top_forth, text='Result: ', bg=color)
res.pack(side=LEFT, pady=10, padx=10)

res_num = Entry(top_forth, highlightbackground=color, textvariable=res_value)
res_num.pack(side=LEFT)

root.mainloop()

```


### ✅️ Entry

```python
from tkinter import *

root = Tk()
root.title("Entry")
root.geometry('400x300')
root.resizable(width=False, height=False)

nameLabel = Label(root, text="please enter your name :")
nameLabel.place(x=8, y=10)

nameInput = Entry(root)
nameInput.insert(END, 'First')
nameInput.place(x=10, y=30)

nameInput2 = Entry(root)
nameInput2.insert(END, 'Second')
nameInput2.place(x=10, y=80)


def get_name():
    print(f"{nameInput.get()} \n{nameInput2.get()}")


btn = Button(root, text="Get Name", command=lambda: get_name())
btn.place(x=10, y=100)

root.mainloop()

```

### ✅️ Frame

```python
from tkinter import *

# ========================== settings ========================
root = Tk()
root.geometry('800x500')
root.title('calculator')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# ========================== frames ==========================
top_first = Frame(root, width=400, height=50, bg='red')
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg='purple')
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg='yellow')
top_third.pack(side=BOTTOM)

top_forth = Frame(root, width=400, height=50, bg='green')
top_forth.pack(side=LEFT)

top_fifth = Frame(root, width=400, height=50, bg='blue')
top_fifth.pack(side=RIGHT)

root.mainloop()

```

# 🅰️

# 🅰️

# 🅰️

# 🅰️

# 🅰️

</div>