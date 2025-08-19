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

# 🅰️ VirtualEnvironment

* محیط مجازی (Virtual Environment): امکان ایجاد فضا مستقل و جداگانه پروژه‌ها از هم(جلوگیری از تداخل) در وابستگی‌های نصب بسته‌ها و کتابخانه‌ها را فراهم می‌آورد
* هر پروژه می‌تواند نسخه‌های خاص خود از کتابخانه‌ها را داشته باشد بدون اینکه بر روی پروژه‌های دیگر تأثیر بگذارد.
* نکته: در محیط venv نیاز به زدن دستور `python3 -m pip install requests` نیست و تنها نوشتن `pip install` کار میکند
* حتما باید بسته virtualenv در سیستم نصب باشد تا بتوانین مجیط مجازی virtualEnvironment بوجود بیاورید(یعنی در خروجی دستور `pip freeze` این بسته موجود باشد)

## 🅱️ تفاوت virtualenv  و  venv

| ویژگی           | virtualenv                   | venv                                                                                     |
|-----------------|------------------------------|------------------------------------------------------------------------------------------|
| **ابزار**       | ابزار مستقل                  | ماژول داخلی پایتون(built-in)                                                             |
| **نسخه پایتون** | پایتون 2.x و 3.x             | فقط پایتون 3.3 به بعد                                                                    |
| **سرعت**        | کمی کندتر                    | سریع‌تر                                                                                  |
| **قابلیت‌ها**   | قابلیت‌های پیشرفته‌تر        | ساده و کم‌حجم                                                                            |
| **نصب**         | `pip install virtualenv`     | `apt install python3.11-venv` or `apt install python3-venv` یا به صورت پیش‌فرض موجود است |
| **استفاده**     | `python3 -m virtualenv venv` | `python3 -m venv venv`                                                                   |

```shell
apt install python3.11-virtualenv #معمولا در پایتون نسخه۳ نصب می‌شود

# پس از زدن دستور زیر یک فولدر در مسیر کنونی ایجاد می‌شود که حاوی زیرفولدرهایی برای نگهداری ساختار بسته‌های نصبی خواهد بود
python3 -m venv myenv # Alternative(windows): python3 -m vitrualenv venv #ایجاد محیط مجازی با نام دلخواه

# فعال‌سازی محیط مجازی مختص به پروژه‌خاص
source myenv/bin/activate # Alternatives(windows): .\MyVenv\Scripts\activate 
 
pip install package_name

deactivate #غیر فعال سازی و خروج از محیط مجازی
```

# 🅰️ Variable 

```python
# CaseSensitive
# Can insert many type of data into one variable
# string can use one or double qoute

# MyAge = 23      → upper camel case - Use for Classes

x, y = 400, 500
personChild = None  # None Means EMPTY
BoolData = True  # first char must uppercase

username = "behrooz"
# username = input("Insert username: ")

print(f"the BoolData is {BoolData}")
print("the BoolData is {BoolData}")
print(f"sum is : {x + y}")
print(f"multiply 2 and 6 is : {2 * 6}")
print(username[2])
print("Name: " + username)
print(round(12.2565856, 5))

print(list(range(4, 10)))  # [4, 5, 6, 7, 8, 9]
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]

userRank = 1
print("you got GOLD medal") if userRank == 1 else print("no medal")

```

# 🅰️ Loop

```python

for variable in iterable:
    if condition1:
        # کد برای condition1
        if condition2:
        # کد برای condition2
        else:
    # کد برای حالت دیگر condition2
    else:


# کد برای حالت دیگر condition1


class loop:

    def forLoop1(self):
        listOfNumbers = [23, 54, 67, 89, 34, 9]
        for number in listOfNumbers:
            print(number * 2)

    def forLoop2(self):
        [print(x) for x in [1, 2, 3, 4, 5, 6, 11]]

    def forLoop3(self):
        for num in range(1, 10):
            if num % 2 == 1:
                for star in range(1, 6):  # [1, 2, 3, 4, 5]
                    print("*" * star)
            else:
                for star in range(5, 0, -1):  # [5, 4, 3, 2, 1]
                    print("*" * star)

    def whileLoop1(self):
        password = input("what is your password : ")
        while password != "1234":
            print("your password is wrong!!!")
            password = input("what is your password : ")
            print("your password is correct !!!!")

    def whileLoop2(self):
        num = 1
        while num < 30:
            # if(num == 5):
            #     break

            print("\U0001f600" * num)
            print("*" * num)
            num += 1


behrooz = loop()
# behrooz.forLoop1()
# behrooz.forLoop2()
# behrooz.forLoop3()
# behrooz.whileLoop1()
behrooz.whileLoop2()
```

# 🅰️ Operation

## 🅱️ OperatorsComparison

```python
# Return Boolean Value
number_1 = -100
number_2 = -200

# == : returns true if the value of number_1 is equal to number_2
print(f'{number_1} == {number_2} : {number_1 == number_2}')

# != : returns true if the value of number_1 is not equal to number_2
print(f'{number_1} != {number_2} : {number_1 != number_2}')

# > : returns true if the value of number_1 is greater than number_2
print(f'{number_1} > {number_2} : {number_1 > number_2}')

# >= : = or >
print(f'{number_1} >= {number_2} : {number_1 >= number_2}')

# < : returns true if the value of number_1 is less than number_2
print(f'{number_1} < {number_2} : {number_1 < number_2}')

# <= : = or <
print(f'{number_1} <= {number_2} : {number_1 <= number_2}')

# is → check By ماهیت و مقدار
# == → check By مقدار

list1 = ['a', 'b', 'c']
list2 = list1
list3 = list(list1)
print(list1)
print(list2)
print(list3)
print(list1 == list2)
print(list1 == list3)
print(list1 is list2)
print(list1 is list3)

```

## 🅱️ Logical Operand

```python
# AND
print("---------AND----------")

print(f"True and True : {True and True}")
print(f"False and True : {False and True}")
print(f"True and False : {True and False}")
print(f"False and False : {False and False}")

userAge = 17
userGender = "female"
if userAge >= 18 and userGender == "male":
    print("you have to go to soldiery")
else:
    print("you can stay at home")

# OR
print("---------OR----------")
print(f"True or True : {True or True}")
print(f"False or True : {False or True}")
print(f"True or False : {True or False}")
print(f"False or False : {False or False}")

weather = "sunny"
if weather == "sunny" or weather == "cloudy":
    print("we can travel")
else:
    print("we can not travel")

# NOT
print("--------NOT-----------")
print(f"not True : {not True}")
print(f"not False : {not False}")

isBrotherComming = False
if not isBrotherComming:
    print("my sister said : i wont come")

# Combine
print("-------Combine------------")
age = 50
if (0 <= age <= 2) or (8 <= age < 65):
    print("you should pay 10 dollars")
if not ((2 < age < 8) or age >= 65):
    print("you should pay 10 dollars")

```

## 🅱️ Ternary Operator

```python
# ternary:A ternary operator exists in some programming languages, and it allows you to shorten a simple If-Else block. It takes in 3 or more operands:
#  syntax: [value_if_true] if [condition] else [value_if_false]
#               │                  │              │
#               │                  │              └──> A value that's returned if the condition evaluates to False.
#               │                  │
#               │                  └─> A boolean condition that has to be satisfied to return value if true.
#               │
#               └──> A value that's returned if the condition evaluates to True.

def condition1():
    a, b = 10, 20
    min = a if a < b else b
    print(min)


def condition2():
    age = 17
    outcome = 'Go home.' if age < 16 else 'Not sure...' if 16 <= age < 18 else 'Welcome'
    print(outcome)


def condition3():
    a, b = 100, 20
    print((b, a)[a < b])


def condition4():
    a, b = 10, 20
    print((lambda: b, lambda: a)[a < b]())


def condition5():
    a, b = 10, 20
    print("Both a and b are equal" if a == b else "a is greater than b"
    if a > b else "b is greater than a")


def condition5_Alternative():
    a, b = 10, 20
    if a != b:
        if a > b:
            print("a is greater than b")
        else:
            print("b is greater than a")
    else:
        print("Both a and b are equal")


def condition6():
    a, b = 5, 7
    print(a, "is greater") if (a > b) else print(b, "is Greater")


# ⇉ a if condition  else b
condition1()
condition6()

print("---------Step 2------------")
# ⇉ a if condition1 else b if condition2 else c
condition2()

# ⇉ print({True: a, False: b} [a < b])
condition3()

# ⇉ Lambda
condition4()

# ⇉ nested ternary operator
condition5()
condition5_Alternative()

```

# 🅰️ exception

## 🅱️ Error

```python
try:
    pass
    # Code
except NameError as NameE:  # Handle NameError Error
    print(NameE)
    print(NameE.message)
    pass
    # مدیریت ارور NameEror در این بلاک صورت می‌گیرد
except IOError as IOE:  # Handle NameError Error
    print(IOE)
    print(IOE.message)
    # مدیریت ارور IOError در این بلاک صورت می‌گیرد

except:  # ErrorHandler of each other error type
    pass
    # مدیریت ارور IOError در این بلاک صورت می‌گیرد
else:
    pass
    # اگر قسمت ترای بدون ارور اجرا شود این بلاک اجرا می‌شود
finally:
    pass
    # در هر صورت این بلاک اجرا خواهد شد

```

## 🅱️ Error-Raise

```python
# print(test)
# None = 1

# raise IndexError('throw index error')
# raise ValueError('invalid value')


def print_with_custom_color(text, color):
    colors = ('red', 'green', 'blue')
    if type(text) is not str:
        raise TypeError("text must be a string")
    elif color not in colors:
        raise ValueError(f"{color} is not in colors")
    else:
        print(f"printed {text} in {color}")


print_with_custom_color("Behrooz", 'red')
print_with_custom_color(2, 'red')
print_with_custom_color("Behrooz", 'redd')

```

## 🅱️ Debug(pdb)

```python
# import pdb

# pdb.set_trace()

# number1 = int(input('please enter a number: '))
# number2 = int(input('please enter a number: '))
# result = number1 + number2
# print(f"result is {result}")


# common pdb commands
# l -> your commands list
# n -> next line
# c -> continue -> finished debugging
# p -> print

def add_numbers(a, b, c, d):
    import pdb;
    pdb.set_trace()
    return a + b + c + d


res = add_numbers(1, 2, 3, 4)
print(res)

```

# 🅰️ Function

## 🅱️ __NAME__

### ✅️ `__init__`

نقش تابع سازنده در هر کلاس را ایفا می‌کند

```python
class User:
    def __init__(self, name, age):  # تابع سازنده
        self.name = name
        self.age = age

    def show_data(self):
        print(self.name, self.age)


obj = User("behrooz", 33)
obj.show_data()

```

### ✅️ `__len__`

فقط زمانی می‌شود از این تابع استفاده کرد که فانکشن آن تعریف شده باشد یا خودمان یا ارث‌بری

```python
class Behrooz:
    def __init__(self, _name):
        self.name = _name

    def __len__(self):
        return 20


obj = Behrooz("Alii")
print(len(obj))
```

### ✅️  `__add__` و `__mul__` و `__truediv__` و `__sub__`

```python
class Behrooz:
    def __init__(self, _name):
        self.name = _name

    # بجای عملگر  + استفاده می‌شود
    def __add__(self, other):
        return f"Need to plus with {self.name} or {other}"

    # بجای عملگر *استفاده می‌شود
    def __mul__(self, other):
        return f"Need to multiplier with {self.name} or {other}"

    # بجای عملگر / استفاده می‌شود
    def __truediv__(self, other):
        return f"Need to division with {self.name} or {other}"

    # بجای عملگر - استفاده می‌شود
    def __sub__(self, other):
        return f"Need to minus with {self.name} or {other}"


obj = Behrooz("Alii")

print(obj)
print(obj + "salam")
print(obj - "salam")
print(obj * "salam")
print(obj / "salam")

```

| Function               | Oprator |
|------------------------|---------|
| __isub__(self,p2)      | -=      | 
| __imul__(self,p2)      | *=      | 
| __itruediv__(self,p2)  | \=      | 
| __floordiv__(self,p2)  | \\      | 
| __ifloordiv__(self,p2) | \=      | 

### ✅️  `__repr__`

* باتعریف این تابع سبب می‌شویم در هنگام پرینت آبجکت تهیه شده از یک کلاس تابع اجرا شود وگرنه آدرس شیء در حافظه نمایش می‌شود
* یعنی اگر بخواهیم که بچای نمایش دیتای فنی دیتای خوانا به کاربر نمایش داده شود
* برای نمایش "رسمی" و دقیق‌تر شیء استفاده می‌شود (معمولاً برای دیباگ یا لاگ‌گیری).

```python
class Behrooz:
    def __init__(self, _name):
        self.name = _name

    def __repr__(self) -> str:
        return f"behroooz class attribute is [{self.name}]"


obj = Behrooz("Alii")
print(obj)

```

### ✅️ `__str__`

* برای خوانایی بیشتر EndUser از یک شیء مورد استفاده قرار می‌گیرد
* این متد زمانی فراخوانی می‌شود که توابعی مانند print یا str برای نمایش یک شیء استفاده شود
* این متد باید یک رشته (str) برگرداند که نماینده‌ی شیء باشد.
* اگر __str__ تعریف نشده باشد، پایتون به جای آن از متد __repr__ استفاده می‌کند.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


person = Person("علی", 25)
print(person)  # output: Person(name=علی, age=25)
```

# 🅰️ JSON

```python
import json
from json2html import *


def createJson(obj):
    # obj = {
    #             "word": "behroooz",
    #             "type": "behrooz"
    #         }
    jsonStr = json.dumps(obj, ensure_ascii=False).encode('utf-8').decode()
    print(jsonStr)


def importFromFile(filename):
    f = open('/tmp/json.json')
    jData = json.load(f)
    return jData


def EditJson(filename):
    f = open('/tmp/Quran/Input.json')
    jData = json.load(f)
    # print(jData)

    for x in range(0, 6236):
        if jData[x]['SuraNumber'] == "003" and jData[x]['VerseNumber'] == "003":
            jData[x]['Farsi'] = "NewData"

    json_str = json.dumps(jData, ensure_ascii=False).encode('utf-8').decode()
    with open('/tmp/Quran/Output.json', 'w') as ff:
        ff.write(json_str)
    f.close()
    ff.close()


def toHtml(inputFileName, outputFileName):
    f = open(inputFileName)
    jData = json.load(f)
    data = json2html.convert(json={"data": jData})
    with open(outputFileName, 'w') as ff:
        ff.write(json.dumps(data, ensure_ascii=False).encode('utf-8').decode())
    f.close()
    ff.close()


# toHtml("/tmp/All.json", "/tmp/All.html")


def showData():
    json_string = '{ "1":"Red", "2":"Blue", "3":"Green"}'
    parsed_json = json.loads(json_string)
    print(parsed_json['2'])

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

# 🅰️ Regex

* Need to`import re`

## 🅱️ dot

```shell
# (.) -> Note: یک کاراکتر
#     (f.n) --> کاراکتر اول «اِف» و کاراکتر دوم هر چیزی می‌تونه باشه و کاراکتر سوم «اِن» باید باشد
#     (f..n) --> کاراکتر اول «اِف» و کاراکتر دوم و سوم هر چیزی می‌تونه باشه و کاراکتر چهارم «اِن» باید باشد
#
# dot (.)
# text = 'this is fun'
# if re.search('f.n', text):
#     print('this is ok')
#
#
```

## 🅱️ ^

```shell
# text = 'Toplearn'
#
# if re.search('^Top', text):
#     print('this is ok')
```

## 🅱️  $

```shell
# text = 'Toplearn'
#
# if re.search('rn$', text):
#     print('this is ok')
```

## 🅱️ escape

```shell
# text = 'this is a book.'
#
# if re.search('book\.', text):
#     print('this is ok')
```

## 🅱️ set

```shell
# text = 'site'
#
# if re.search('si[tdz]e', text):
#     print('this is ok')
```

## 🅱️ range

```shell
# text = 'c'
#
# if re.search('[a-f]', text):
#     print('this is ok')
```

## 🅱️ exclude

```shell
# text = 'siue'
#
# if re.search('si[^tdz]e', text):
#     print('this is ok')
```

## 🅱️ repeat

```shell
# text = '09123456789'
#
# if re.match('[0-9]{11}', text):
#     print('this is ok')
```

## 🅱️ other characters

```shell
# decimal digits => \d
# non decimal digits => \D
# white space => \s
# non white space => \S
# word => \w
# non word => \W

# text = 'abcdef'
# if re.match('(abc|cde)', text):
#     print('this is ok')
```

## 🅱️ email regex

```python
text = '787jhjkj@test.com'
if re.match('^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print('email is valid')
```

## 🅱️ Search

```python
import re

# Behrooz: regexr.com

names = [
    'data.png', 'memory.txt', 'data.txt', 'image.png', 'momy.png'
]

for item in names:
    if re.search('m.m', item):
        print(item)

# re.search('m.m', item): #اگر در این رشته موجود بود
# re.match('m.m', item): # باید دقیقا این رشته مساوی الگو باشد

```

```python
import re
import os

for item in os.walk('/Learning-Concept'):
    for file in item[2]:
        if re.search('\.py', file):
            print(file)

```

# 🅰️ Thread

```python
import time
from threading import Thread


class Worker(Thread):
    def run(self):
        for x in range(0, 30):
            print(f"1 → {x}")
            time.sleep(1)


class Waiter(Thread):
    def run(self):
        for x in range(100, 110):
            print(f"2 ⇉⇉⇉{x}")
            time.sleep(5)


print("Staring Worker Thread")
Worker().start()
print("Starting Waiter Thread")
Waiter().start()
print("Done")

```

# 🅰️ Number

## 🅱️ Leading Zero

```python
number = 1
number = f"{number:03d}"
print(number)

```

</div>