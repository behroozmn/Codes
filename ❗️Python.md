<div dir="rtl">

# 1. 🅰️ Commands

* پایتون و تعامل با زبان‌های دیگر
    * CPython: تعامل با تمام کدهایC
        * کد را در پایتون می‌نویسیم و روی cpython اجرای می‌کنیم و خروجی C می‌گیریم
    * IronPython: قابلیت کار کردن در فضای نت
    * Jthon: تعامل باتمام کدهای جاوا
        * کد را در پایتون می‌نویسیم و روی Jthon اجرای می‌کنیم و خروجی java می‌گیریم
    * Pyobjc:استفاده از فضای شیءگرایی
* نصب
    * همواره برای نصب تیک گزینه "add python to path" را بزنید
    * تابع پرینت از نسخه شماره ۳ به بعد در پایتون اضافه شده است

## 1.1. 🅱️ pip

- ریپوزیتوری pypi یا Python Package Index مخزن رسمی بسته‌های نرم‌افزاری پایتون می‌باشد که با دستور pip می‌توان از آن
  استفاده کرد
- در پایتون در pip3 منظور از آرگومان -m این است که یک ماژول را به عنوان یک برنامه اجرایی، اجرا کن!
    - pip
- موارد مشابه pip وجود دارد نظیر: Pipenv - Conda - Poetry

> pip commnad options

```shell
pip list # لیستی از بسته‌های نصب شده با ورژن
pip list

pip freeze # لیستی از بسته‌های نصب شده با ورژن
pip freeze
pip freeze > requirements.txt

pip install #دانلود و نصب بسته
pip install PyYAML==6.0
pip install --upgrade pip بروزرسانی مخرن PYPI
python -m pip install Django==3.0.3 --user
pip install --upgrade -r requirements.txt

pip download #دانلود بسته

pip check #بررسی سلامت سازگاری و وابستگی‌های یک بسته

pip uninstall #حذف بسته

pip show #نمایش اطلاعات یک بسته نصب شده
pip show drf-spectacular`

pip search #Search PyPI for packages

pip inspect #show Details about Environment

pip config #Manage local and global configuration

#################
#### Options #### 
#################
# -r filename.txt  خواندن از یک فایل که حاوی وابستگی‌های ماژول یا برنامه است
pip download -r ./requirements.txt

# --upgrade
pip install --upgrade PyYAML
pip install --upgrade pip # بروز رسانی ماژول‌های پیپ
```

## 1.2. 🅱️ python3

```shell
python3 --version
python3 -m pip --version

python3 manage.py #[Django]show help and SubCommands 
python3 manage.py runserver #[Django]Boot and startup Django project on Default port 8000
python3 manage.py runserver 8001
python3 manage.py startapp myNewApp #[Django]: add new application to django main project
python3 manage.py makemigrations #[Django]: جستجوی تغییرات مدل
python3 manage.py migrate #[Django]: اعمال تغییرات مدل در دیتابیس
python3 manage.py shell #[Django] دسترسی به شل یا همان پایتون کنسول
python3 manage.py createsuperuser` #[Django] ایجاد یوزر ادمین جنگو

#################
#### Options #### 
#################
-m module-name #Searches sys.path for the named module and runs the corresponding .py file as a script

```

## 1.3. 🅱️ django-admin

```shell
django-admin #اگر بدون پارامتر باشد نمایش لیستی از دستورات در دسترس از جنگو
django-admin startproject MyProject <Director> #Create DjangoTemplate
```

## 1.4. 🅱️ apt

```shell
sudo apt install python3-PackageName #نصب بسته در محدوده سیستمی و نه یک پروژه یعنی همه جای سیستم عامل دسترس خواهد بود
```

## 1.5. 🅱️ pipdeptree

```shell
pipdeptree | nl #نمایش وابستگی‌ها در فرمت فایل نیازمندی‌ها
```

# 2. 🅰️ Name Conventions

* جدولNaming Conventions برای نامگذاری عناصر استفاده شونده در کدنویسی

| نوع نامگذاری              | فرمت نام                       | قوانین و قراردادها                                        | مثال                                   | توضیحات                                        |
|---------------------------|--------------------------------|-----------------------------------------------------------|----------------------------------------|------------------------------------------------|
| متغیرهای معمولی           | `snake_case`                   | حروف کوچک، جداکننده با `_`                                | `user_name`, `total_price`             | برای متغیرهای محلی و عمومی                     |
| توابع                     | `snake_case`                   | مشابه متغیرها، حروف کوچک و جداکننده با `_`                | `calculate_tax()`, `load_data()`       | همواره از فعل استفاده کنید                     |
| کلاس‌ها                   | `UpperCamelCase`               | تمام کلمات با حرف بزرگ شروع می‌شوند (UpperCamelCase)      | `UserProfile`, `DatabaseManager`       | اسم‌ها هستند، نه فعل                           |
| ثابت‌ها                   | `UPPER_SNAKE_CASE`             | تمام حروف بزرگ، جداکننده با `_`                           | `MAX_USERS`, `DEFAULT_TIMEOUT`         | مقدارهای غیرقابل تغییر                         |
| ماژول‌ها                  | `snake_case`                   | نام فایل‌های `.py` باید کوچک و بدون خطوط تیره (`-`) باشد  | `utils.py`, `data_parser.py`           | اجتناب از حروف بزرگ                            |
| پکیج‌ها                   | `snake_case`                   | مشابه ماژول‌ها، نام پکیج‌ها نیز باید کوچک باشد            | `mypackage/`, `app_helpers/`           | از `_` در صورت نیاز استفاده کنید               |
| متغیرهای خصوصی            | `_single_leading_underscore`   | یک `_` در ابتدای نام(قراردادی برای خصوصی بودن)            | `_internal_value`                      | فقط درون ماژول/کلاس استفاده شود                |
| متغیرهای خصوصی قوی        | `__double_leading_underscore`  | دو `_` در ابتدای نام = Name Mangling در کلاس‌ها           | `__secret_key`                         | برای جلوگیری از تداخل در کلاس‌های فرزند        |
| متغیرهای خصوصی و داخلی    | `_single_trailing_underscore_` | یک `_` در انتهای نام(حل تداخل با کلمات کلیدی پایتون)      | `class_`, `type_`                      | مثل وقتی که نمی‌توانید از `class` استفاده کنید |
| متغیرهای موقت / لوپ       | `i`, `j`, `k`                  | برای شمارنده‌های ساده حلقه                                | `for i in range(10):`                  | فقط در حلقه‌های کوتاه                          |
| متغیرهای محاسباتی         | `x`, `y`, `z`                  | برای مقادیر عددی ساده و محاسباتی                          | `x = 5`, `coordinates = (x, y)`        | مخصوص متغیرهای ریاضی                           |
| متغیرهای بولی             | `is_`, `has_`, `should_`       | ابتدا با افعال منفی/مثبت شروع می‌شوند                     | `is_valid`, `has_permission`           | جواب بله/خیر دارند                             |
| متغیرهای توابع lambda     | `func`, `lambda_func`          | نام‌های کوتاه و معنادار برای توابع lambda                 | `func = lambda x: x*2`                 | از نام‌های غیرمعنادار مانند `f` اجتناب کنید    |
| متغیرهای مرتبط با تست     | `test_`, `fixture_`            | برای توابع تست در فریم‌ورک‌هایی مانند `pytest`            | `test_login()`, `fixture_user()`       | تشخیص آسان توابع تست                           |
| متغیرهای مرتبط با GUI     | `on_`, `btn_`, `lbl_`          | نام‌ها براساس نوع المان UI                                | `on_submit()`, `btn_save`, `lbl_title` | خوانایی بالا در برنامه‌های گرافیکی             |
| متغیرهای اشاره‌گر به تابع | `callback`, `handler`          | نام‌های استاندارد برای متغیرهایی که به تابع اشاره می‌کنند | `event_handler`, `success_callback`    | مخصوص callback ها                              |
| متغیرهای دیتابیس          | `db_`, `cursor`, `conn`        | نام‌های استاندارد برای متغیرهای دیتابیس                   | `db_connection`, `cursor.execute()`    | واضح‌سازی منبع داده                            |
| متغیرهای JSON / API       | `payload`, `response`, `data`  | نام‌های استاندارد برای مدیریت داده‌های JSON و API         | `payload = {'name': 'Ali'}`            | سازگاری با API ها                              |

# 3. 🅰️ Persian Tools

* برای استفاده از کاراکترهای «یونیکد فارسی» یا هر زبانی در سورس کدهای پایتون، باید از این هدر در بالای کد استفاده شود
    * `-*- coding: utf-8 -*-`
    * در این حالت مفسر کد را به صورت یونی کد می‌خواند و می تواند فارسی در آن بنویسید
* برای اینکه تمام رشته‌های STR در پایتون به صورت UNICODE تعریف شوند باید در ابتدای فایل این کلاس را ایمپورت کنیم
    ```python
    from __future__ import unicode_literals
    ```

# 4. 🅰️ VirtualEnvironment

* محیط مجازی (Virtual Environment): امکان ایجاد فضا مستقل و جداگانه پروژه‌ها از هم(جلوگیری از تداخل) در وابستگی‌های نصب
  بسته‌ها و کتابخانه‌ها را فراهم می‌آورد
* هر پروژه می‌تواند نسخه‌های خاص خود از کتابخانه‌ها را داشته باشد بدون اینکه بر روی پروژه‌های دیگر تأثیر بگذارد.
* نکته: در محیط venv نیاز به زدن دستور `python3 -m pip install requests` نیست و تنها نوشتن `pip install` کار میکند
* حتما باید بسته virtualenv در سیستم نصب باشد تا بتوانین مجیط مجازی virtualEnvironment بوجود بیاورید(یعنی در خروجی دستور
  `pip freeze` این بسته موجود باشد)

## 4.1. 🅱️ تفاوت virtualenv  و  venv

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

# 2. پس از زدن دستور زیر یک فولدر در مسیر کنونی ایجاد می‌شود که حاوی زیرفولدرهایی برای نگهداری ساختار بسته‌های نصبی خواهد بود
python3 -m venv myenv # Alternative(windows): python3 -m vitrualenv venv #ایجاد محیط مجازی با نام دلخواه

# 3. فعال‌سازی محیط مجازی مختص به پروژه‌خاص
source myenv/bin/activate # Alternatives(windows): .\MyVenv\Scripts\activate 
 
pip install package_name

deactivate #غیر فعال سازی و خروج از محیط مجازی
```

# 5. 🅰️ Variable

* متغیرها در پایتون CaseSensitive هستند
* این قابلیت در پایتون وجود دارد که انواع نوع را در یک متغیر وارد نماییم
* مقدار None برابر است با Empty یعنی اگر مقدار `myCount = None` را دیدیم یعنی مقدار myCount برابر است با Empty
* توسط دستور input می‌توان مقدار اولیه برای یک متغیر قرار داد
   ```python
   username = "behrooz"
   username = input("Insert username: ")
   ```
* اگر در تابع print یک fقبل از علامت کوتیشن قرار دهید آنگاه مقادیر قابلیت تفکیک پیدا می‌کنند
   ```python
   # 1️⃣️
   BoolData = True
   print(f"the BoolData is {BoolData}") # the BoolData is True
   print("the BoolData is {BoolData}")  # the BoolData is {BoolData}
   # 2️⃣️
   x, y = 400, 500
   print(f"sum is : {x + y}")
   print(f"multiply 2 and 6 is : {2 * 6}")
   ```
* می‌توان در خروجی چند متغیر را الحاق کرد
   ```python
   username = "behrooz"
   print("Name: " + username) # Name: behrooz
   ```

```python

print(round(12.2565856, 5))  # 12.25659

print(list(range(4, 10)))  # [4, 5, 6, 7, 8, 9]
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]

userRank = 1
print("you got GOLD medal") if userRank == 1 else print("no medal")

```

# 6. 🅰️ Loop

```python

for variable in iterable:
    if condition1:
        # کد برای condition1
        if condition2:
        # کد برای condition2
        else:
    # کد برای حالت دیگر condition2
    else:


# 9. کد برای حالت دیگر condition1


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
# 10. behrooz.forLoop1()
# 11. behrooz.forLoop2()
# 12. behrooz.forLoop3()
# 13. behrooz.whileLoop1()
behrooz.whileLoop2()
```

# 7. 🅰️ Operation

## 7.1. 🅱️ OperatorsComparison

```python
# 14. Return Boolean Value
number_1 = -100
number_2 = -200

# 15. == : returns true if the value of number_1 is equal to number_2
print(f'{number_1} == {number_2} : {number_1 == number_2}')

# 16. != : returns true if the value of number_1 is not equal to number_2
print(f'{number_1} != {number_2} : {number_1 != number_2}')

# 17. > : returns true if the value of number_1 is greater than number_2
print(f'{number_1} > {number_2} : {number_1 > number_2}')

# 18. >= : = or >
print(f'{number_1} >= {number_2} : {number_1 >= number_2}')

# 19. < : returns true if the value of number_1 is less than number_2
print(f'{number_1} < {number_2} : {number_1 < number_2}')

# 20. <= : = or <
print(f'{number_1} <= {number_2} : {number_1 <= number_2}')

# 21. is → check By ماهیت و مقدار
# 22. == → check By مقدار

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

## 7.2. 🅱️ Logical Operand

```python
# 23. AND
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

# 24. OR
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

# 25. NOT
print("--------NOT-----------")
print(f"not True : {not True}")
print(f"not False : {not False}")

isBrotherComming = False
if not isBrotherComming:
    print("my sister said : i wont come")

# 26. Combine
print("-------Combine------------")
age = 50
if (0 <= age <= 2) or (8 <= age < 65):
    print("you should pay 10 dollars")
if not ((2 < age < 8) or age >= 65):
    print("you should pay 10 dollars")

```

## 7.3. 🅱️ Ternary Operator

```python
# 27. ternary:A ternary operator exists in some programming languages, and it allows you to shorten a simple If-Else block. It takes in 3 or more operands:
# 28. syntax: [value_if_true] if [condition] else [value_if_false]
# 29. │                  │              │
# 30. │                  │              └──> A value that's returned if the condition evaluates to False.
# 31. │                  │
# 32. │                  └─> A boolean condition that has to be satisfied to return value if true.
# 33. │
# 34. └──> A value that's returned if the condition evaluates to True.

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


# 35. ⇉ a if condition  else b
condition1()
condition6()

print("---------Step 2------------")
# 36. ⇉ a if condition1 else b if condition2 else c
condition2()

# 37. ⇉ print({True: a, False: b} [a < b])
condition3()

# 38. ⇉ Lambda
condition4()

# 39. ⇉ nested ternary operator
condition5()
condition5_Alternative()

```

# 8. 🅰️ exception

## 8.1. 🅱️ Error

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

## 8.2. 🅱️ Error-Raise

```python
# 40. print(test)
# 41. None = 1

# 42. raise IndexError('throw index error')
# 43. raise ValueError('invalid value')


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

## 8.3. 🅱️ Debug(pdb)

```python
# 44. import pdb

# 45. pdb.set_trace()

# 46. number1 = int(input('please enter a number: '))
# 47. number2 = int(input('please enter a number: '))
# 48. result = number1 + number2
# 49. print(f"result is {result}")


# 50. common pdb commands
# 51. l -> your commands list
# 52. n -> next line
# 53. c -> continue -> finished debugging
# 54. p -> print

def add_numbers(a, b, c, d):
    import pdb;
    pdb.set_trace()
    return a + b + c + d


res = add_numbers(1, 2, 3, 4)
print(res)

```

# 9. 🅰️ Function

* اگر یک تابع در داخل یک کلاس تعریف گردد آنگاه برای اینکه به مقادیر کلاس دسترسی داشته باشد باید آرگومان اول آن را کلمه کلیدی self قرار دهید

بدنه یک تابع به فرم زیر می‌باشد

```python
def exponent(num, power=2):
    return num ** power

print(exponent(5))  # output: 25
```

```python
def showFullName(first, last):
    return f"{first} {last}"


print(showFullName("MohammadiNasab", "Behrooz"))
print(showFullName(last="MohammadiNasab", first="Behrooz"))  # تغییر در ترتیب پارامتر ورودی
```

## 9.1. 🅱️ Lambda

* لامبدا در اصل یک تابع است(نوعی از تعریف تابع است) که تنها در یک خط تعریف می‌شود
* به «توابع یک خطی» یا «Annonymous function» معروف هستند

```python
# Syntax is:
# lambda arg1, arg2: arg1 * arg2 + 10
# lambda arg1      : value_if_true if condition  else  value_if_false
# lambda arg1      : value_if_true if condition1 else  (value_if_true2 if condition2 else value_if_false)
```

```python
# 1️⃣️
function1 = lambda arg1, arg2: arg1 * arg2 + 10
print(function1(5, 2)) # output: 20

# 2️⃣️
function2 = lambda x: "Positive" if x > 0 else ("Zero" if x == 0 else "Negative")
print(function2(-5)) # Output: Negative
print(function2(0)) # Output: Zero
print(function2(4)) # Output: Positive

```

## 9.2. 🅱️ Agmuments

* اگر در هنگام تعریف بدنه یک تابع همه موارد parameters و args و defaultParameters و kwargs داشته باشیم ترتیب اولویت به شکل زیر است
   * 1️⃣️ `parameters`
   * 2️⃣️ `*args` یعنی Tuple ◄  متغیر ازنوع غیرقابل تغییرخواهد بود
   * 3️⃣️ `default parameters` یعنی تعیین مقدار پیش‌فرض برای متغیر 
     * اگر درهنگام فراخوانی تابع مقدار متغیر تعیین نشود آنگاه مقدارپیش‌فرض بعنوان مقدار متغیر لحاظ می‌گردد
   * 4️⃣️ `**kwargs` یعنی Dictionary ◄ متغیر دارای محتوی کلید و مقدار است
* وقتی `*args` در بدنه تابع وجود داشت یعنی آن متغیرها همگی از نوع Tuple خواهند بود یعنی اینکه Immutable و غیرقابل تغییر خواهند بود 
* 
```python
class Functions:
    def func1(self, num, power=2):
        print(f"func1: {num ** power}")

    def func2(self, first, last):
        print(f"func2: {first} {last}")

    # تبدیل می‌شود به یک تاپل
    def func3_holico(self, *args):
        total = 0
        for num in args:
            total += num
        print(f"func3: {args}------> {total}")

    # آرگومان ورودی تبدیل می‌شود به یک دیکشنری
    def func4(self, **kwargs):
        my_string = ""
        for key, value in kwargs.items():
            my_string = f"{my_string} {key}:{value} - "
        print(f"func4: {my_string}")

    def func5(self, a, b, *args, define_parameter="defalut", **kwargs):
        print(f"func5: {a}, {b} {args}, {define_parameter}, {kwargs}")


behrooz = Functions()

behrooz.func1(2, 3)  # output:8
behrooz.func1(3)  # output:9

behrooz.func2("behrooz", "mohammad")
behrooz.func2(last="mohammad", first="behrooz")

person = {"first": "behrooz", "last": "Mohamadi"}
behrooz.func2(**person)
behrooz.func2(*person)

behrooz.func3_holico(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

numbers = [1, 2, 3, 4, 5, 6]  # لیست است و میخواهیم بعنوان آرگومان ورودی به تابع بدهیم
behrooz.func3_holico(*numbers)  # اگر ستاره نباشد ارور میدهد

behrooz.func4(name="behrooz", FamilyName="Mohammadi")
behrooz.func4(name="behrooz", FamilyName="Mohammadi", born=1369, mobile="09191671085")

behrooz.func5(1, 2, 6, first_name="Behrooz", last_name="MohamadiNasab")

```

## 9.3. 🅱️ __NAME__

### 9.3.1. ✅️ `__init__`

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

### 9.3.2. ✅️ `__len__`

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

### 9.3.3. ✅️  `__add__` و `__mul__` و `__truediv__` و `__sub__`

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

### 9.3.4. ✅️  `__repr__`

* باتعریف این تابع سبب می‌شویم در هنگام پرینت آبجکت تهیه شده از یک کلاس تابع اجرا شود وگرنه آدرس شیء در حافظه نمایش
  می‌شود
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

### 9.3.5. ✅️ `__str__`

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

## 9.4. 🅱️ MATH

```python
from math import *  # در پایتون اگر بخواهیم دیگر مثل کلاس ریاضی نام مَت را ننویسیم و تنها نام تابع را بنویسیم

input  # گرفتن ورودی از کاربر
raw_input  #
abs(x)  # قدرمطلق یعنی اگر منفی باشد مثبت می‌کند
cmath.sqrt(x)  # محاسبه ریشه دوم صحیح
math.sqrt(x)  # محاسبه ریشه دوم طبیعی
math.floor(x)  # اگر ایکس اعشاری باشد مقدار صحیح برا برمی‌گرداند
math.ceil(x)  # کوچکترین عدد بزرگترمساوی‌یک عدد
pow(x, y, z)  # عدد ایکس به توان وای و بعد نتیجه تقسیم بر زد و نمایش باقیمانده
repr(obj)  # نمایش رشته‌ای
round(x[, ndigits])  # زند یک عدد با دقت دلخواه
ceil(x)  # وقتی ایکس عدد اعشار باشد آنگاه مقدار صحیح بالاتر را برمی‌گرداند
degrees(x)  # اگر ایکس رادیان باشد مقدار زاویه را به درجه برمی‌گرداند
```

![Fibonatchi](./_srcFiles/Images/07.gif "07.gif")

### 9.4.1. ✅️ Min_Max

```python
list1 = [3, 6, 8, 13, 4, 90]
list2 = ['a', 't', 'z']
list3 = "mostafa"
list4 = ['mohammad', 'milad', 'akbar', 'sara', 'iman', 'ali']

# 71. Step 1️⃣️ - روش اول
result = [len(name) for name in list4]
print(f"Character lenght {list(list4)} ---> {result}")

# 72. Step 1️⃣️ - روش دوم
print(f"Character lenght {list(list4)} ---> {[len(name) for name in list4]}")
print("----------End1-------------")

# 73. Step 2️⃣️
print(f"max in {list(list1)} ---> {max(list1)}")
print(f"min in {list(list1)} ---> {min(list1)}")
print(
    f"max lenght in {list(list4)} ---> {max(list4, key=lambda n: len(n))}")  # ماکزیمم را برحسب تعداد کاراکتر درنظر بگیر
print(
    f"max lenght in {list(list4)} ---> {min(list4, key=lambda n: len(n))}")  # مینیمم را برحسب تعداد کاراکتر درنظر بگیر

```

## 9.5. 🅱️ Reversed

```python
numbers = [1, 2, 3, 4, 5, 6]

# 74. numbers.reverse() #در لیست تغییر ایجاد میکند

print(f"reversed in [{numbers}] ---> {list(reversed(numbers))}")

chars = "hello"
print(f"reversed in {chars} ---> {list(reversed(chars))}")
print(f"reversed in {chars} ---> {chars[::-1]}")

nameRes = ''
print(nameRes.join(list(reversed("hello"))))

for num in reversed(range(0, 10)):
    print(num)
print("----")
for num in range(9, -1, -1):
    print(num)

```

## 9.6. 🅱️ Sort

```python
def func2sort_NoChange():
    numbers = [1, 5, 8, 4, 6, 2]
    print(f"func2(befor): {list(numbers)}")
    result = sorted(numbers, reverse=False)
    print(f"func2(sorted result): {result}")
    print(f"func2(after): {list(numbers)}")


def func4sort_Change():
    numbers = [1, 5, 8, 4, 6, 2]
    print(f"func4(befor): {list(numbers)}")
    numbers.sort(reverse=False)
    print(f"func4(after): {list(numbers)}")


# 75. لیست ها برای مرتب سازی نیاز به کلید دارند


def func5():
    users = [
        {'name': 'taha', 'family': 'MohammadiNasab', 'age': 40},
        {'name': 'mohammad', 'family': 'ketabi', 'age': 23},
        {'name': 'sara', 'family': 'nadery', 'age': 80},
        {'name': 'ali', 'family': 'Mohamadi', 'age': 30}
    ]
    print(users)
    print(sorted(users, key=lambda user: user['age'], reverse=False))


func2sort_NoChange()
print("")
func4sort_Change()
print("")
func5()

```

## 9.7. 🅱️ Length

```python
users = [{'name': 'Behrooz', 'family': 'nadery', 'born': 1369, 'shopCart': []},
         {'name': 'Alireza', 'family': 'saberi', 'born': 1400, 'shopCart': []},
         {'name': 'Attefeh', 'family': 'Rezaie', 'born': 1372, 'shopCart': ['kotlin', 'vue']}]


def func1():
    print(f"func1:{len(users)}")


def func2():
    result = filter(lambda user: len(user['shopCart']) == 0, users)
    print(f"func2(filter):{list(result)}")


func1()
func2()

```

## 9.8. 🅱️ TruthinessFalsiness_All

```python
# 84. بررسی درستی یا نادرستی یا همان تروسینس یا فالسینس
# 85. اگر تمام آیتم‌های داده شده به این تابع درست باشد مقدار ترو را برمی‌گرداند
# 86. عدد صفر بطور پیش‌فرض در پایتون مقدار فالس در نظر گرفته شده است

print(all([2, 3, 4, 8]))
print("")

print("-----Step2-----")
print(all([]))  # اگر خالی باشد ترو برمی‌گرداند
print("")

print("-----Step3-----")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(num for num in numbers if num % 2 == 0))
print("")

print("-----Step4-----")
print([num % 2 == 0 for num in numbers])
print("")

print("-----Step5-----")

# 87. همه آیتم هایی که در نامبر هستند بر دو بخش پذیر هستند یا خیر
print(all([num % 2 == 0 for num in numbers]))

```

## 9.9. 🅱️ TruthinessFalsiness_Any

```python
# 88. بررسی درستی یا نادرستی یا همان تروسینس یا فالسینس
# 89. اگر تنها حتی یک آیتم از مواردی که به این تابع داده شده است ترو باشد مقدار ترو را برمی‌گرداند

def func1():
    numbers = [0, 0, 0, 0]
    print(f"{numbers} --> {any(numbers)}")


def func2():
    numbers = [0, 0, 0, 1]
    print(f"{numbers} --> {any(numbers)}")


def func3():
    data = [False, False, False, False]
    print(f"{data} --> {any(data)}")


def func4():
    data = [False, False, False, True]
    print(f"{data} --> {any(data)}")


def func5():
    print(any([]))


def func5():
    numbers = [2, 4, 6, 8]
    result = (any([num % 2 != 0 for num in numbers]))
    print(f"{numbers} --> {result}")


def func6():
    numbers = [2, 4, 6, 7]
    result = (any([num % 2 != 0 for num in numbers]))
    print(f"{numbers} --> {result}")


func1()
func2()
func3()
func4()
func5()
func6()
```

# 10. 🅰️ Decorator

## 10.1. 🅱️ function into function

استفاده از تابع درون تابع دیگر به روش های متفاوت انجام می‌شود که نمونه‌های آن در ذیل آمده است

### 10.1.1. ✅️ Traditional

```python
from random import choice


def state():
    def get_state():
        msg = choice(('Good', 'Bad!', 'Fine'))
        return msg

    return get_state()


print(f"-----> {state()}")
print("\n")

```

### 10.1.2. ✅️ Traditional-ByReturnValue

```python
from random import choice


def state():
    def get_state():
        msg = choice(('Good', 'Bad!', 'Fine'))
        return msg

    return get_state


result = state()
print("=====> ", result())
```

### 10.1.3. ✅️ Traditional-ByArgs

```python
def sum_func(number, func):
    total = 0
    for num in range(1, number + 1):
        total += func(num)
    return total


def square_func(number):
    return number * number


print("☰☰☰☰☰> ", sum_func(5, square_func))
```

### 10.1.4. ✅️ Modern-ByDecorator

* تکنیک Decorator یک DesignePatternاست که یک تابع را درون تابع دیگر فراخوانی میکنیم
* امکان تغییر یا گسترش رفتار یک تابع یا کلاس بدون تغییر در کد اصلی آن
* معمولاً به صورت یک تابع تعریف می‌شوند
* یک تابع دیگر را بعنوان آرگومان ورودی می‌پذیرند و یک تابع جدید را برمی‌گردانند
* این تابع جدید می‌تواند قبل یا بعد از اجرای تابع اصلی، کارهای اضافی انجام دهد
* معمولا همراه با کاراکتر @ در بالای توابع ظاهر می‌شوند

```python
def exec_after_before(func):
    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


@exec_after_before
def say_hello():
    print("Hi")


say_hello()

```

## 10.2. 🅱️ Classmethod

* تغییر عملکرد یک تابع بطوریکه به‌جای استفاده از منابع نمونه از منابع کلاس استفاده می‌کند
* دسترسی مستقیم به دیتای کلاس بدون ساخت شیء نمونه

```python
class User:
    activeUsers = 0

    @classmethod
    def func1(cls):
        return cls.activeUsers


# 90. روش 1️⃣️: بدون نیاز ساخت شیء از کلاس
print(User.func1())

# 91. روش 2️⃣️: الزام بر ساختن شیء از کلاس"

obj1 = User()
print(obj1.func1())

```

## 10.3. 🅱️ Property

* property: تبدیل تابع به ویزگی(property) یا صفت(attribute)
* برای دسترسی به متد باید حتما پرانتز باز و بسته گذاشته بشود ولی برای پراپرتی نباید پرانتز گذاشت

```python

class Behrooz:

    def __init__(self, name, family):
        self.name = name
        self.family = family

    @property
    def fullname(self):
        return f"{self.name} {self.family}"

    def show_fullname(self):
        return f"{self.name} {self.family}"


obj1 = Behrooz("behrooz", "MohamadiNasab")

print(obj1.show_fullname())
print(obj1.fullname)

```

## 10.4. 🅱️ PropertyGetterSetter

* تغییر رفتارِ تابع به متغیر
* getter: یک تابع است و برای استفاده باید حتما همراه پرانتز باشد ولی هنگامیکه با @property بیاید آنگاه نیاز به استفاده
  از پرانتز نیست

```python
class behrooz:

    def __init__(self, _name, _family, _age):
        self.name = _name
        self.family = _family
        self.age = _age

    # برای دسترسی به متد باید حتما پرانتز باز و بسته گذاشته بشود
    # ولی وقتی از تابع getter استفاده می‌کنیم با گذاشتن Decorator تحت عنوان property نباید پرانتز گذاشت
    # اگر پراپرتی را قرار ندهیم آنگاه برای فراخوانی مقدار باید حتما پرانتز باز و بسته رو قرار دهیم
    @property
    def age(self):  # # تبدیل یک تابع به یک پراپرتی و نه متد
        return self._age

    @property
    def fullName(self):  # تبدیل یک تابع به یک پراپرتی و نه متد
        return f"{self.name} {self.family}"

    # توابعی که Decorator تحت عنوان property و setter قرار دارد سبب می‌شود تا رفتارِ تابع تغییر کند و در حالت متغیر استفاده گردد
    # نکته: کلمه age که در خط زیر است از تابع بالایی که همراه property است آمده است و باید هم‌نام آن باشد
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            self._age = 0


obj1 = behrooz("behrooz", "MohamadiNasab", -18)
print(obj1.age)  # اگر پراپرتی را در بالای گِتِر متغیر قرار نمی‌دادیم باید در اینجا پرانتز باز و بسته قرار می‌دادیم

obj1.age = 40
print(obj1.age)

obj1.age = -15
print(obj1.age)

obj1.age = 18
print(obj1.age)

print(obj1.fullName)  # به حالت متد فراخوانی نمیکنیم بلکه به حالت پراپرتی(خصیصه) فراخوانی می‌کنیم

```

## 10.5. 🅱️ Advanced

```python
def before_after(func):
    def wrapper():
        print(f"Before={0}")
        func()
        print(f"After={1}")

    return wrapper


print("#########################################")
print("######## روش اول:برگرداندن یک تابع ######")
print("#########################################")


def say_hello():
    print("hello")


tempFunc = before_after(say_hello)
tempFunc()

print("\n#################################")
print("###  Decorator #### 0 Argument ###")
print("##################################")


@before_after
def say_hello():
    print("hello")


say_hello()

print("\n##################################")
print("###  Decorator #### 1 Argument ###")
print("##################################")


# 92. x only sent to wrapper[not sent to num_before_after]
def one_arg_before_after(func):
    def wrapper(x):
        print(f"Before={x - 1}")
        func(x)
        print(f"After={x + 1}")

    return wrapper


@one_arg_before_after
def say_hello(x):
    print(f"----1arg---->hi {x}")
    print(f"----1arg---->hi")


say_hello(256)

print("\n##################################")
print("###  Decorator #### 2 Argument ###")
print("##################################")


def two_args_before_after(func):
    def wrapper(arg1, arg2):
        print(f"Before:      [arg1:{arg1}] - [arg2:{arg2}]")
        func(arg1, arg2)
        print(f"After:       [arg1:{arg1}] - [arg2:{arg2}]")

    return wrapper


@two_args_before_after
def show_name(name, family):
    print(f"---2arg--->  {name} {family}")


show_name('behrooz', 'Mohamadinasab')

print("\n###############################")
print("###  Decorator ##### (*Arg) ###")
print("###############################")


def many_args_before_after(func):
    def wrapper(*args):
        print(f"Before      [{args}]")
        func(args)
        print(f"After       [{args}]")

    return wrapper


@many_args_before_after
def show_data(*args):
    print(f"---*arg---> {args}")


show_data('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address')

print("\n##########################################")
print("###  Decorator with(*Arg and **kwargs) ###")
print("##########################################")


def exec_before_after(func):
    def wrapper(*args, **kwargs):
        print(f"Before      [args:{args}]")
        func(*args, **kwargs)
        print(f"After       [kwargs:{kwargs}]")

    return wrapper


@exec_before_after
def show_data(*args, **kwargs):
    print(f"==========> {args} - {kwargs}")


show_data('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address', Fname="Behi", Lname="Mohamadi")
print("\n\n")
show_data('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address', Fname="Behi")
print("\n\n")
show_data('Behrooz', 'MohamadiNasab', 'phone')
print("\n\n")
show_data(Fname="Behi", Lname="Mohamadi")
print("\n\n")
show_data('male')
print("\n\n")
show_data(Fname="Behi")

```

## 10.6. 🅱️ Example

```python
from time import time


def speed_test(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Time Elapsed : {end_time - start_time}")
        return result

    return wrapper


@speed_test
def sum_list():
    return sum([x for x in range(40000000)])


@speed_test
def sum_gen():
    return sum(x for x in range(40000000))


sum_gen()
sum_list()

```

# 11. 🅰️ Iterate

```python
# 93. iterate: پیمایش یا تکرار کردن
# 94. 
# 95. iterable: Objects which can iterate and can convert to iterator
# 96. ---> iterableObjects: Lists, Tuples, Dictionaryes, Sets, Strings
# 97. ---------> iterableObject is not a iterator[but by function it can chage to iterator]
# 98. ---> Note: we can not iterate on iterableObjects first. It should be converted to iterator and then iterate on it
# 99. ---> Note: موضوع توالی و پشت سر هم بودن، جزء مهمترین مولفه در این ساختار است
# 100. ---> Generally ussing with loops(for and ...)
# 101. ---> next(): ussing next function for access to next item
# 102. 
# 103. iterator: object that can iterate on items by itself, and It can sequentially access the elements of an iterable
# 104. ---> iterator=iterableObjects.iter();
# 105. ---> class who must define __iter__() to  return iterator [Obj.iter()]
# 106. ---> class who must define __next__() to  return next item and if nextItem is not available, return [StopIteration exception]) [Obj.next()]


numbers = [1, 2, 3]  # iterableObjects
colors = ('red', 'green', 'blue')  # iterableObjects
name = "Behrooz"  # iterableObjects

iterator = iter(numbers)

print(iterator)  # output: <list_iterator object at 0x7fb1fd78e8f0>
print(next(iterator))  # output: 1
print(next(iterator))  # output: 2
print(next(iterator))  # output: 3
# 107. print(next(iterator)) # output: Exception(StopIteration) [only 3 items is Exist in iterableObjects]


iterName = iter(name)
print(next(iterName))
print(next(iterName))
print(next(iterName))
print(next(iterName))

```

## 11.1. 🅱️ Dictionary

```python
# 108. List       → []
# 109. Dictionary → { key1: value1, key2: value2 }
# 110. Set        → {} 1-All Items must be uniq (No repeat)
# 111. 2-without sort
# 112. 3-without index #اندیس ناپذیر
# 113. 4-without call # نمی‌توانیم فراخوانی داشته باشیم
# 114. 
# 115. Tuple      → () 1-Items cannot change(immutable)

class DictionaryClass:
    Dic1 = {
        "name": "Behrooz",
        "family": "Mohammadi Nasab",
        "age": 31
    }

    Dic2 = {
        "mobile": "09191671085"
    }

    Dic3 = dict(first=1, second=2, third=3)

    Dic4 = {num: num for num in [1, 2, 3, 4, 5]}  # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

    Dic5 = {key: value ** 2 for key, value in Dic3.items()}  # {'first': 1, 'second': 4, 'third': 9}

    _Dic6 = {num: ("even" if num % 2 == 0 else "odd")  # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
             for num in [1, 2, 3, 4, 5]}

    __Dic7 = {num: num ** num for num in [1, 2, 3, 4, 5]}

    def __init__(self) -> None:
        pass

    def showValue(self):
        print(DictionaryClass.Dic1["name"])  # Behrooz
        print(DictionaryClass.Dic1["family"])  # MohammadiNasab
        print(DictionaryClass.Dic1["age"])  # 31
        # dict_values(['Behrooz', 'MohammadiNasab', 31])
        print(DictionaryClass.Dic1.values())
        print(DictionaryClass.Dic1.keys())  # dict_keys(['name', 'family', 'age'])

    def returnValue(self):
        return DictionaryClass.Dic1.get("name"), DictionaryClass.Dic1["family"], DictionaryClass.Dic1["age"]

    def printValuesByFor(self):
        for value in DictionaryClass.Dic1.values():
            print(value)

    def printKeysByFor(self):
        for key in DictionaryClass.Dic1.keys():
            print(DictionaryClass.Dic1[key])

    def printKeyValuesByFor(self):
        for key, value in DictionaryClass.Dic1.items():
            print(f"{key}: --> {value}")

    def printAll(self):
        print(DictionaryClass.Dic1)

    def isExist(self, x):
        if x in DictionaryClass.Dic1:
            print(DictionaryClass.Dic1[x])
        else:
            print(f"there is no {x} key in me")

    def clearData(self):
        DictionaryClass.Dic1.clear()

    def copyData(self):
        two = DictionaryClass.Dic1.copy()  # یک دیکشنری را دقیقا در دیگری می‌ریزد یعنی کپی میکند
        return two

    def popData(self):
        # one.pop("name") #کلید و مقدار را باهم پاک میکند
        # or
        # مقدار را اول داخل متغیر میریزد و سپس از دیکشنری حذف میکد
        result = DictionaryClass.Dic1.pop("name")

    def popLastItem(self):
        DictionaryClass.Dic1.popitem()  # آخرین کلید و مقدار را حذف میکند

    def concatenateDictionary(self):
        DictionaryClass.Dic1.update(DictionaryClass.Dic2)  # دیکشنری را به دیکنشری موجود می‌افراید

    # آرگومان ورودی تبدیل می‌شود به یک دیکشنری
    def func4(self, **kwargs):
        my_string = ""
        for key, value in kwargs.items():
            my_string = f"{my_string} {key}:{value} - "
        print(f"func4: {my_string}")


behrooz = DictionaryClass()
# 116. behrooz.printValuesByFor()
# 117. behrooz.printKeysByFor()
# 118. behrooz.printKeyValuesByFor()
# 119. behrooz.isExist("name")
# 120. behrooz.clearData()

# 121. print(behrooz.copyData().get("age"))
# 122. print(behrooz.copyData() == one)
# 123. print(behrooz.copyData() is one)

# 124. behrooz.popLastItem()
# 125. behrooz.printKeyValuesByFor()

# 126. behrooz.concatenateDictionary()
# 127. behrooz.printKeyValuesByFor()

# 128. value1, value2, value3 = behrooz.returnValue()
# 129. print(f"name:{value1}\n\nfamily:{value2}\n\nage:{value3}")

behrooz.printAll()

behrooz.func4(name="behrooz")
behrooz.func4(name="behrooz", FamilyName="Mohammadi")
behrooz.func4(name="behrooz", FamilyName="Mohammadi", born=1369, mobile="09191671085")

```

## 11.2. 🅱️ Set

```python
# 130. List       → []
# 131. Dictionary → { key1: value1, key2: value2 }
# 132. Set        → {} 1-All Items must be uniq (No repeat)
# 133. 2-without sort
# 134. 3-without index #اندیس ناپذیر
# 135. 4-without call # نمی‌توانیم فراخوانی داشته باشیم
# 136. 
# 137. Tuple      → () 1-Items cannot change(immutable)


class SetClass:
    _set1 = {3, 5, 't', 'z', 2, 7, 1, 1, 1, 5, 5, 5, 5}
    _set2 = {"ali", "milad", "mohammad", "sara"}
    _set3 = {"mohammad", "ahmad", "reza", "ali"}
    _set4 = {x ** 2 for x in range(20)}
    _set5 = {char for char in "Behrooz Mohammadi Nasab Sahzabi"}

    def showData(self):
        for item in self._set1:
            print(item)
        print(self._set1)

    def functions(self, mySet):
        mySet.add(8)

        if 4 in mySet:
            mySet.remove(2)

        mySet.discard(4)  # اگر عدد بود آن را پاک میکند و اگر نبود ارور نمیدهد و دستور بدون ارور رد می‌شود
        print(mySet)


behrooz = SetClass()

behrooz.showData()

behrooz.functions(SetClass._set1)

print(
    SetClass._set2 | SetClass._set3)  # {'ahmad', 'mohammad', 'reza', 'milad', 'sara', 'ali'}  # نمایش اجتماع بدون تکرار

print(SetClass._set2 & SetClass._set3)  # {'ali', 'mohammad'}  #نمایش اشتراک بدون تکرار

print(SetClass._set4)

print(SetClass._set5)

```

## 11.3. 🅱️ Tupple

```python
# 138. List       → []
# 139. Dictionary → { key1: value1, key2: value2 }
# 140. Set        → {} 1-All Items must be uniq (No repeat)
# 141. 2-without sort
# 142. 3-without index #اندیس ناپذیر
# 143. 4-without call # نمی‌توانیم فراخوانی داشته باشیم
# 144. 
# 145. Tuple      → () 1-Items cannot change(immutable)


class TuppleClass:
    _tuple1_1to50 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50)
    _tuple2 = (1, 2, 2, 3, 4, 5, 2, (4, 5, 3), 3, 3)  # immutable list
    _tuple3 = (1, 2, {2}, (3, 4), [2, 5], 2, (4, 5, 3), 3, 3)
    _tuple4 = tuple([1, 2, 3, 4, 5])

    def show_tuple_withfor(self, localtuple=_tuple2):
        for num in localtuple:
            print(num)

    # آرگومان ورودی تبدیل می‌شود به یک تاپل
    def func1(self, *args):
        total = 0
        for num in args:
            total += num
        print(f"func3: {args}------> {total}")


obj = TuppleClass()
obj.show_tuple_withfor()

obj.func1(1, 2, 3, 4)
obj.func1(12)

numbers = [1, 2, 3, 4, 5, 6]  # لیست است و میخواهیم بعنوان آرگومان ورودی به تابع بدهیم
obj.func1(*numbers)  # اگر ستاره نباشد ارور میدهد

```

## 11.4. 🅱️ List

```python
# 146. List       → []
# 147. Dictionary → { key1: value1, key2: value2 }
# 148. Set        → {} 1-All Items must be uniq (No repeat)
# 149. 2-without sort
# 150. 3-without index #اندیس ناپذیر
# 151. 4-without call # نمی‌توانیم فراخوانی داشته باشیم
# 152. 
# 153. Tuple      → () 1-Items cannot change(immutable)

class ListClass:
    def __init__(self):
        _list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        _list2 = ["Python", True, 5, [4, 5, 6]]
        _list3 = ["red", "blue", "green", "gray", "yellow", "orange", 3.6]
        _list4 = []
        _list5 = [num * 2 for num in _list1]
        _list6 = [char.upper() for char in "behrooz"]
        _list7_even = [num for num in _list1 if num % 2 == 0]
        _list7_odd = [num for num in _list1 if num % 2 != 0]
        _list8 = [num * 2 if num % 2 == 0 else num * 3 for num in _list1]
        _list9 = "BehroozMohammadiNasab"
        _list10_nestedList = [[1, 2, 3], [4, 5, 6]]
        _list11 = [num ** 2 for num in range(1, 11)]

    def getDataAll(self, myList):
        for x in myList:
            print(f"the value is : {x}")

    def getDataAllByCount(self, mylist):
        indexCount = len(mylist)
        index = 0
        while index < indexCount:
            x = mylist[index]
            print(f"the value is : {x}")
            index += 1

    def fill_list(self):
        for num in self._list1:
            self._list4.append(num ** 2)

    def get_alldata_revese(self, mylist):
        mylist.reverse()
        print(mylist)

    def get_select_item(self, mylist):
        # List[start:end:step]

        value1 = mylist[1]  # output: 2
        value2 = mylist[-5:]  # output: [12, 13, 14, 15, 16]
        value3 = mylist[::2]  # output: [1, 3, 5, 7, 9, 11, 13, 15]
        value4 = mylist[0:]  # output: All items [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        value5 = mylist[:]  # output: All items [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        value6 = mylist[
                 ::-1]  # List[start:end:step] output: Reverse [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        value7 = mylist[:3]
        print(f"value1:{value1}")
        print(f"value2:{value2}")
        print(f"value3:{value3}")
        print(f"value4:{value4}")
        print(f"value5:{value5}")
        print(mylist == value5)
        print(mylist is value5)
        print(f"value6:{value6}")
        print(f"value7:{value7}")


def list_functions(self, mylist):
    first_item = mylist.pop(0)
    last_item = mylist.pop()
    length = {len(mylist)}
    mylist.extend(["ali", "hassan", "hossein"])
    mylist.append(["alii", "hassann", "hosseinn"])
    mylist.insert(-1, "Behrooz")
    mylist.remove(13)
    # mylist.clear()  # remove all elements
    # mylist.sort()  # only number
    print(f"length: {length}")
    print(f"firstItem:{first_item}")
    print(f"lastItem:{last_item}")
    print(mylist)


def search(self, mylist):
    index1 = mylist.index(5)
    index2 = mylist.index(7, 3, 10)  # از اندیس ۴ تا اندیس ۱۱ جستجو نماید
    print(index1)
    print(index2)

    tmp = '.'.join(['ab', 'pq', 'rs'])
    print(tmp)

# 154. behrooz.getDataAll(list._list8)
# 155. behrooz.getDataAllByCount(list._list2)
# 156. behrooz.fillList()
# 157. behrooz.getDataAll(list._list4)
# 158. behrooz.getDataAll_Revese(list._list1)
# 159. behrooz.get_select_item(list.list1)
# 160. print(list._list10_nestedList[1][2])  # output: 6
# 161. [[print(x) for x in y] for y in list._list10_nestedList] # output: 1 NewLine 2 NewLine 3 NewLine 4 NewLine 5 NewLine 6
# 162. behrooz.listFunctions(list._list1)
# 163. behrooz.search(list._list1)
# 164. print(list._list11)

# 165. behrooz = list()

```

## 11.5. 🅱️ Filter

* برای یاد گیری سه مفهوم ۱-لامبدا ۲-فیلتر ۳-مَپ ،باید به ترتیب نام برده شده مطالعه شود

* انتخاب یک المان تحت شرایط
* فیلتر روی یک ایتریبل اگر در شرط بگنجد
    * Filter a iterable by condition(only apply to items which true condition on it)
* itarate: پیمایش

```python
# 59. Syntax:                        filter(function, iterable)
# 60. return:                        IterableObject
# 61. How ussing IterableObject:     list(IterableObject) or  Tuple(IterableObject)
```

```python
numbers = [1, 2, 3, 4, 5, 6]
names = ["akbar", "fatemeh", "zeinab", "maryam", "Kobra"]
users = [{'name': 'Behrooz', 'family': 'nadery', 'born': 1369, 'shopCart': []},
         {'name': 'Alireza', 'family': 'saberi', 'born': 1400, 'shopCart': []},
         {'name': 'Attefeh', 'family': 'Rezaie', 'born': 1372, 'shopCart': ['kotlin', 'vue']}]


def func1_get_even():
    evens = filter(lambda num: num % 2 == 0, numbers)
    print(f"func1:{list(evens)}")


def func3():  # Use with Falsiness Or Truthiness
    result = filter(lambda user: not user['shopCart'], users)  # [not user['shopCart']] OR [len(user['shopCart']) == 0]
    # result = filter(lambda user: len(user['shopCart']) == 0, users)
    print(f"func3(alt):{list(result)}")


def func4_map_filter():
    result_user = filter(lambda user: not user['shopCart'], users)
    result_user_name = lambda user: user['name']
    result = map(result_user_name, result_user)
    # ALTERNATIVE =====> result = [user['name'] for user in users if len(user['shopCart']) == 0]
    print(f"func4(filterAndMap):{list(result)}")


func1_get_even()
print()

func3()
print()

func4_map_filter()

```

## 11.6. 🅱️ map

```python
# 64. map: calls a function for all its members of iterable
# 65. ---> Syntax: map(function, iterable) ==> Return: an iterable mapObject
# 66. ==> Ussing: list(mapObject) or Tuple(mapObject) or ...
# 67. ---> Note: تنها یکبار روی لیست یا غیره می‌تواند پیمایش صورت بپذیرد و در پیمایش دوم با لیست خالی مواجه می‌شود
# 68. ---> itarate: پیمایش
# 69. ---> iterable: هر چیزی که روی آیتم‌های آن قابلیت پیمایش وچود داشته باشد
# 70. ---> Note:  به صورت «لِیزی» عمل می‌کند، به این معنی که محاسبات تنها زمانی انجام می‌شود که به نتایج آن نیاز باشد


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["akbar", "natasha", "zeinab", "maryam", "Kobra"]
users = [{'name': 'amirali', 'family': 'ojaghi', 'born': 1369, 'shopCart': []},
         {'name': 'mahmood', 'family': 'sabeti', 'born': 1400, 'shopCart': []},
         {'name': 'hossein', 'family': 'taheri', 'born': 1372, 'shopCart': ['kotlin', 'vue']}]


def func1():
    def square(x):
        return x ** 2

    squared_numbers = map(square, numbers)
    # Alternatives: squared_numbers = map(lambda x: x ** 2, numbers)

    # تبدیل به لیست
    squared_list = list(squared_numbers)
    print(squared_list)  # خروجی: [1, 4, 9, 16, 25]


def func2_map_filter():
    result_user = filter(lambda user: not user['shopCart'], users)
    result_user_name = lambda user: user['name']
    result = map(result_user_name, result_user)
    # ALTERNATIVE =====> result = [user['name'] for user in users if len(user['shopCart']) == 0]
    print(f"func4(filterAndMap):{list(result)}")


def func3():
    upper_names = map(lambda name: name.upper(), names)
    print(f"func5{list(upper_names)}")
    print(
        f"func5(خالی خواهد بود زیرا یک بار پیمایش شده است){list(upper_names)}")  # خالی خواهد بود زیرا پیمایش سبب تخلیه می‌گردد


def func4():
    result = map(lambda person: person['family'], users)
    print(f"func3:{list(result)}")
    # Alternatives:
    #           families = []
    #           for person in users: families.append(person['family'])
    #           print(f"{families}")


def func5():
    def add(x, y):
        return x + y

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    added_numbers = map(add, list1, list2)
    # ALTERNATIVE =====> added_numbers = map(lambda x, y: x + y, list1, list2)

    # تبدیل به لیست
    result_list = list(added_numbers)
    print(result_list)  # خروجی: [5, 7, 9]


func1()
print()
func2_map_filter()
print()

func3()
print()

func4()
print()

func5()

```

## 11.7. 🅱️ Generator_Expression

* Generator: create function as sequentional lazy items
    * create or generate items only when ussing
    * Generate values incrementally when need
    * اگر کار با دیتای زیادی صورت می‌گیرد بهتر است از جنریتور استفاده شود
    * دیتا یکباره لود نمی‌شود و یک به یک انجام می‌شود
    * روشی برای ایجاد ایتریتور
    * اگر دستورات را داخل یک پرانتز قرار بدهیم(در مثال تصریح شده است)
    * بطور پیش‌فرض ایتریتور هستند و نیاز به تعریف تابع نکست ندارند
    * اگر یک ماژول یک جنریتور برگرداند آنگاه ناگزیر باید روی آن پیمایش کرد تا به محتوی آن دست یافت
* yield
    * وضعیت تابع(شامل مقادیر متغیرها و موقعیت اجرای تابع) حفظ می‌شود
    * قابلیت ادامه تابع از همان نقطه توقف
    * عدم محاسبه و برگرداندن یکباره تمام مقادیر بلکه محاسبه و تولیدیکی پس از دیگری

### 11.7.1. ✅️ Example 1️⃣️: yield

```python
def nums():
    for num in range(20):
        yield num


g = nums()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
```

### 11.7.2. ✅️ Example 2️⃣️: Generator

```python
myGenerator = (num for num in range(20))
print(myGenerator)
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
```

### 11.7.3. ✅️ Example 3️⃣️: yield

```python
def func_generator(maximom):
    count = 1
    while count <= maximom:
        yield count
        count += 1


counter = func_generator(3)  # استفاده از حالت جنریتور
print(next(counter))  # -> 1
print(next(counter))  # -> 2
print(next(counter))  # -> 3
# 166. print(next(counter))  # if run error
```

### 11.7.4. ✅️ Example4️⃣️: Fibunachi()

```python
print("--------------------byList----------------------")


def fib_list(maximom):  # 10
    numbers = []  # [1,1]
    a, b = 0, 1
    while len(numbers) <= maximom:
        numbers.append(b)
        a, b = b, a + b
    return numbers


print(f"By List ===> {fib_list(10)}")
for num in fib_list(10):
    print(f"------> {num}")


def fib_generator(maximom):
    count = 0
    a, b = 0, 1

    while count < maximom:
        a, b = b, a + b
        yield b
        count += 1


print("-----------------byGenerator--------------------")

print(f"By Generator ===> {fib_list(10)}")
for num in fib_generator(10):  # استفاده از حالت جنریتور
    print(f"------> {num}")
```

### 11.7.5. ✅️ Example 5️⃣️

```python
from time import time

start_time = time()
print(f"byGenerator: {sum(num for num in range(100000000))}")  # --> GeneratorExprerssion
end_time = time()
print(f"--------->  Time(s): {end_time - start_time}")

start_time = time()
print(
    f"ussing list: {sum([num for num in range(100000000)])}")  # Not GeneratorExprerssion, only send list to sum function
end_time = time()
print(f"---------->  Time(s): {end_time - start_time}\n")

```

## 11.8. 🅱️ Zip

```python
# 167. تلفیق دو ایتِرِیت با یکدیگر تبدیل به یک ایتریت جدید که شامل هردوی آن‌ها می‌باشد
# 168. اگر یک بار پیمایش شود خالی خواهد شد

from unittest import result

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9, 10]
students = ["mohammad", "iman", "sara"]
midterm = [78, 80, 94]
final = [91, 84, 97]


def func1_CreateZip():
    result = zip(list1, list2)
    print(f"[func1]=> combine {list1} and {list2}: -------> {list(result)}")
    print(f"[func1]=> combine {list1} and {list2}: --2th--> {list(result)}\n")  # یکبار پیمایش سبب تخلیه می‌گردد


def func2_CreateZip():
    finalGrades = [pair for pair in zip(students, midterm, final)]
    # finalGrades = [pair for pair in zip(students,midterm)]
    print(f"[func2]=> {list(finalGrades)}\n")


def func3_Extract():
    myList = [(1, 5), (3, 7), (6, 4), (7, 9)]
    print(f"[func3]=> extract from {myList}: ----> {list(zip(*myList))}\n")


def func4():
    result = zip(midterm, final)
    print(f"[func4]=> {list(result)}\n")


def func5_max():
    result = map(
        lambda pair: max(pair),
        zip(midterm, final)
    )
    print(f"[func5(max)]=> {list(result)}\n")


def func6_MaxZip():
    finalGrades = zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterm, final)
        )
    )
    print(f"[func6(Max_Zip)]=> {dict(finalGrades)}")


def func6_MaxZip_WithIndex():  # use index
    finalGrades = {t[0]: max(t[1], t[2]) for t in zip(students, midterm, final)}
    print(f"[func6(Max_Zip)]=> {finalGrades}")


def func7_avg():
    result = map(
        lambda pair: (pair[0] + pair[1]) / 2,
        zip(midterm, final)
    )
    print(f"[func7(avg)]=> {list(result)}")


def func7_avg_WithIndex():
    average = zip(
        students,
        map(
            lambda pair: (pair[0] + pair[1]) / 2,
            zip(midterm, final)
        )
    )
    print(f"[func7(avg)]=> {dict(average)}")


func1_CreateZip()
func2_CreateZip()
func3_Extract()
func4()
func5_max()
func6_MaxZip()
func6_MaxZip_WithIndex()
func7_avg()
func7_avg_WithIndex()

```

## 11.9. 🅱️ Iterate_class_example

```python
# 169. example 1️⃣️
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration


# 170. استفاده از iterator
my_iter = MyIterator(5)
for number in my_iter:
    print(number)


# 171. example 2️⃣️
class Counter:
    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += self.step
            return num
        raise StopIteration  # حلقه فور نسبت به این ارور حساس است و خودکار از حلقه خارج می‌شود # auto Break


for num in Counter(10, 20, 3): print(num)
print("------")
for num in Counter(10, 20): print(num)


# 172. example 3️⃣️
class User:
    ActiveUsers = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.index = 0
        User.ActiveUsers.append({'name': name, 'age': age})

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(User.ActiveUsers):
            person = User.ActiveUsers[self.index]
            self.index += 1
            return person
        raise StopIteration


person_1 = User('mohammad', 24)
person_2 = User('sara', 20)

print(f"ActiveUsers:{User.ActiveUsers}\n\n")

for item in User('ali', 60):
    print(item)

```

# 12. 🅰️ OOP(Object Oriented Programming)

* در کلاس‌ها درحین تعریف یک تابع در داخل آن تابع اگر از کلمه کلیدی self استفاده نشود آنگاه متغیرهای کلاس همراه آورده
  نمی‌شود
* کلمه پارامتر بعنوان ورودی در وقت استفاده از تابع است و کلمه آرگومان بعنوان ورودی‌های یک تابع در بدنه یک فانکشن است

```python
# 173. import random
# 174. import random as rand
# 175. from random import *
# 176. from random import randint, choice
# 177. from random import randint as r_i, choice as r_ch

# 178. vsCode--> python: select interpreter #تغییر در ورژن‌های پایتون در ویژوآل استودیو کد
# 179. encapsulation: توابع و متغیرها و موارد را در یک کلاس قرار بدهیم
# 180. __name__ --> name of the module(file)


class User:
    def __init__(self, name, age):  # تابع سازنده
        self.name = name
        self.age = age

    def show_data(self):
        print(self.name, self.age)


obj = User("behrooz", 33)
obj.show_data()
print("آیا شیء یک نمونه از کلاس است؟", isinstance(obj, User))

```

## 12.1. 🅱️ NameMangling

```python
# 181. _name    => define local variable
# 182. Note: در پایتون هیچ قلمرویی تحت عنوان پرایویت نداریم
# 183. Note: استفاده از یک آندرلاین قبل متغیر تنها یک قرارداد است ولی باز در هرکجا به پرایویت می‌توان دسترسی داشت

# 184. __name   => name mangling: available only with _classname__variable in use time
# 185. Note: در پایتون همه نامگذاری‌ها قراردادی است ولی تنها نِیم‌مَنگِلینگ است که سبب تغییر در نام آیتم می‌شود

# 186. __name__ => in python special function define in this form such as __init__ as construction


class User:
    _mobile = "09191671085"  # بعنوان پیشنهاد در لیست intelliSence نمایش داده نمی‌شود و تلویحاً بعنوان متغیر محلی تلفی‌می‌شود
    __password = "myPassword"  # Generally __password is not available. only available by _User__password

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def get_mobile(self):
        return self._mobile


obj = User("behrooz", 33)
print(obj.name)
print("☓️:" + obj._mobile)  # استفاده از پارامتر محلی داخل یک کلاس بصورت مستقیم توصیه نمی‌شود
print("✓:" + obj.get_mobile)
print(
    obj._User__password)  # وقتی یک پارامتر را با دوتا آندرلاین تعریف کنیم و توسط شکل فوق به آن دسترسی داشته باشیم را nameMangling می‌گویند

```

## 12.2. 🅱️ Override

```python
class Animal:
    def makeSound(
            self): raise NotImplementedError  # بدنه کلاس را در زیر کلاس باید تعریف کنیم وگرنه به ارور برخورد خواهیم کرد


class Dog(Animal):
    def makeSound(self):
        return "cat is making sound"


class Worm(Animal):
    def makeSound(self):
        return "worm does not make any sound"


dog = Dog()
worm = Worm()

print(dog.makeSound())
print(worm.makeSound())

```

## 12.3. 🅱️ Static

* اگر یک متغیر را در داخل کلاس و خارج توابع تعریف کنیم آنگاه آن را استاتیک خواندنی درنظر می‌گیرد
* یعنی با تغییر در شیء‌نمونه‌ها ازین پس مقادیر آنها مستقل خواهند شد
* تابع آی‌دی شماره هر متغیر را که در حافظه دارد را نشان می‌دهد

```python
class User:
    staticData = 100  # static data for class(access by [ClassName].Variable)


one = User()
two = User()

print("--------Initial value---------------")
print(f"staticData in User[id: {id(User.staticData)}] ==========> {User.staticData}")
print(f"staticData in one [id: {id(one.staticData)} ] ---> {one.staticData}")
print(f"staticData in two [id: {id(two.staticData)} ] ---> {two.staticData}")

print("--------change in class---------------")
User.staticData = 0
print(f"staticData in User[id: {id(User.staticData)}] ==========> {User.staticData}")
print(f"staticData in one [id: {id(one.staticData)} ] ---> {one.staticData}")
print(f"staticData in two [id: {id(two.staticData)} ] ---> {two.staticData}")

print("--------Change objects---------------")
one.staticData = 1
two.staticData = 2

print(f"staticData in User[id: {id(User.staticData)}] ==========> {User.staticData}")
print(f"staticData in one [id: {id(one.staticData)} ] ---> {one.staticData}")
print(f"staticData in two [id: {id(two.staticData)} ] ---> {two.staticData}")

print("--------change in class---------------")
User.staticData = 3
print(f"staticData in User[id: {id(User.staticData)}] ==========> {User.staticData}")
print(f"staticData in one [id: {id(one.staticData)} ] ---> {one.staticData}")
print(f"staticData in two [id: {id(two.staticData)} ] ---> {two.staticData}")

```

# 13. 🅰️ File

## 13.1. 🅱️ Read

```python
data = open("/etc/passwd")

# 187. 1)
# 188. print(data.read())
# 189. data.seek(2) # جابجایی کرسر به نقطه خاص از فایل
# 190. print(data.read())

# 191. 2)
# 192. textLines = data.readlines() # یک لیست از خطوط که آخر هر خط یک بک‌اسلش‌اِن قرار میدهد
# 193. print(textLines)
# 194. print(f"----> {textLines[5]}")


# 195. 3)
with open("/etc/passwd", encoding='UTF-8', mode="r") as bFile:
    for l in bFile:
        line = l.strip()
        # mylist = lines.rsplit(",")
        print(line)

```

## 13.2. 🅱️ Write

```python
# 196. mode:
# 197. a: append
# 198. w: read
# 199. r: write


with open("/tmp/salam.txt", encoding='UTF-8', mode="w") as bFile:
    bFile.write("STRIIIIIIIIIIIIIIIIIIIIIIIIIIING\n")

```

## 13.3. 🅱️ module os

```python
import os
import time
import fnmatch
import glob

print(os.listdir('/'))
print(os.path.isdir('/'))

print("---------------")

result = os.scandir('/home/Files')
for item in result:
    if item.is_file():  # if item.is_file():
        print(f'File {item.name}: {time.ctime(item.stat().st_mtime)}')

# 200. result = os.stat('./my_files/doc.txt')
# 201. print(time.ctime(result.st_mtime))

# 202. os.mkdir('test')  # 1-Error if exist 2-Error with subDirectory
# 203. os.makedirs('/tmp/test/sub_ddsfdsfdsfsirectory1')  # 1-Error if exist


print('################')
print('#### Delete ####')
print('################')

# 204. os.remove("/tmp/test/sub_ddsfdsfdsfdsfsirectory1"); # اگر فایل موجود نباشد خطا برمی‌گرداند
# 205. os.unlink("/tmp/test/sub_ddsfdsfdsfsdfsdfsdfsdfdsfdsfsirectory1"); # اگر فایل موجود نباشد خطا برمی‌گرداند

# 206. os.rmdir("/tmp/test/sub_ddsfdsfdsfsdfsdfsdfsdfdsfdsfsirectory1"); # فقط پوشه های خالی رو پاک میکنه


# 207. ---------------------------------------------------------------------------------------------------------

import fnmatch
import glob
import os

print('################')
print('#### Search ####')
print('################')

for file_name in os.listdir(''):
    if file_name.endswith('.py'):
        print(file_name)

print('#### only content \'Read\'')
for file_name in os.listdir(''):
    if 'read' in file_name:
        print(file_name)

print('#### Search by fnmatch ####')

print(fnmatch.fnmatch('/Learning-Concept/_SRCFiles/File_Pathlib.py', '*.py'))  # ‌آیا فایل با الگو تطابق دارد یا خیر

for file_name in os.listdir(''):
    if fnmatch.fnmatch(file_name, '*_*.py'):  # *[0-9][0-9]* : وجود فایل دارای دو رقم عدد
        print(file_name)

print(glob.glob('**/*[0-9][0-9]*', recursive=True))

print('#### WALK: Search all directory and subDirectory####')
for data in os.walk(''):  # os.walk('dir',topdown=False) از تویی ترین مسیر شروع میکنه و اقدام به بررسی محتویات می‌کنه
    print(data)



```

## 13.4. 🅱️ Module Pathlib

```python
import pathlib
import shutil
from pathlib import Path

directory = Path('/home/Files')
for item in directory.iterdir():
    print(item)
print("---------------")

path = Path('/tmp/salam')
path.mkdir(exist_ok=True)  # [false: error on exist][True: not Error on exist]

print('################')
print('#### Delete ####')
print('################')

file_path = pathlib.Path('/tmp/salam/fsdfsdfsd.txt')
# 208. file_path.unlink() # حذف فایل
# 209. file_path.rmdir() # حذف فولدر خالی

print('################')
print('#### Search ####')
print('################')

shutil.rmtree('./test', ignore_errors=True)

path = Path('')  # root of projects
data = path.glob('**/*.py')
print(list(data))

```

## 13.5. 🅱️ Module shutil

```python
import os
import shutil

# 210. shutil.copy('src', 'Des') # Only copy file
# 211. print(os.stat('./my_files/data-1.txt'))
# 212. print(os.stat('./new_my_files/new-data-1.txt'))

# 213. shutil.copy2('./my_files/data-2.txt', 'Des') # copy file with metadata
# 214. print(os.stat('./my_files/data-2.txt'))
# 215. print(os.stat('./new_my_files/new-data-2.txt'))

# 216. shutil.copytree('src', 'Des') #create Backup[all _SRCFiles and subDir and Subfiles]

# 217. shutil.move('src', 'Des')

# 218. os.rename('src', 'Des')

```

# 14. 🅰️ JSON

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


# 219. toHtml("/tmp/All.json", "/tmp/All.html")


def showData():
    json_string = '{ "1":"Red", "2":"Blue", "3":"Green"}'
    parsed_json = json.loads(json_string)
    print(parsed_json['2'])

```

# 15. 🅰️Database

## 15.1. 🅱️ SQLlight

```python
import sqlite3

connection = sqlite3.connect("/tmp//my-database.db")
cursor = connection.cursor()

# 220. 1️⃣️
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

# 221. 2️⃣️ Multiple sql command

sql = """
    INSERT INTO Product VALUES (2,'kotlin course',3000,'this is kotlin course');
    INSERT INTO Product VALUES (3,'vue course',4000,'this is vue course');

"""
cursor.execute(sql)
cursor.executescript(sql)

# 222. 3️⃣️

sql = """
    SELECT * FROM Product WHERE description LIKE "%python%"
"""
cursor.execute(sql)
for product in cursor:
    print(product)
```

# 16. 🅰️ GUI

## 16.1. 🅱️ tkinter

### 16.1.1. ✅️ Lable

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

### 16.1.2. ✅️ Button

```python
from tkinter import *
import tkinter.font as font

from matplotlib.ft2font import ITALIC

tkWnd = Tk()
tkWnd.title("button")
tkWnd.geometry('400x300')
tkWnd.resizable(width=False, height=False)
# 223. tkWnd.configure(bg='white')
# 224. tkWnd['bg']='green'
tkWnd['bg'] = '#FFFFFF'

my_name = StringVar()


def print_my_name():
    my_name.set('my name is Mohammad')


myFont = font.Font(family='Vazir', size=10, weight='bold')
btn = Button(tkWnd, text="show my name!", bg='blue', fg='red', width=20, height=1, font=myFont,
             command=lambda: print_my_name())
btn.place(x=10, y=10)

label = Label(tkWnd, textvariable=my_name)
label.place(x=10, y=50)

tkWnd.mainloop()

```

### 16.1.3. ✅️ Calculator پوسته

```python
from tkinter import *

# 225. ========================== settings ========================
root = Tk()
root.geometry('400x200')
root.title('calculator')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# 226. ========================== frames ==========================
top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)

# 227. ========================== Buttons ==========================

btn_plus = Button(top_third, text="+", width=10, highlightbackground=color)
btn_plus.pack(side=LEFT, padx=10, pady=10)

btn_minus = Button(top_third, text="-", width=10, highlightbackground=color)
btn_minus.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_third, text="*", width=10, highlightbackground=color)
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_third, text="/", width=10, highlightbackground=color)
btn_div.pack(side=LEFT, padx=10, pady=10)

# 228. ========================== Entries and Labels ==========================

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

### 16.1.4. ✅️ Calculator

```python
from tkinter import *
import tkinter.messagebox

# 229. ========================== settings ========================
root = Tk()
root.geometry('400x200')
root.title('calculator')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# 230. ========================== variables ==========================

num1 = StringVar()
num2 = StringVar()
res_value = StringVar()

# 231. ========================== frames ==========================
top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)


# 232. ========================== Functions ==========================

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


# 233. ========================== Buttons ==========================

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

# 234. ========================== Entries and Labels ==========================

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

### 16.1.5. ✅️ Entry

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

### 16.1.6. ✅️ Frame

```python
from tkinter import *

# 235. ========================== settings ========================
root = Tk()
root.geometry('800x500')
root.title('calculator')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# 236. ========================== frames ==========================
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

# 17. 🅰️ Regex

* Need to`import re`

## 17.1. 🅱️ dot

```shell
# 237. (.) -> Note: یک کاراکتر
# 238. (f.n) --> کاراکتر اول «اِف» و کاراکتر دوم هر چیزی می‌تونه باشه و کاراکتر سوم «اِن» باید باشد
# 239. (f..n) --> کاراکتر اول «اِف» و کاراکتر دوم و سوم هر چیزی می‌تونه باشه و کاراکتر چهارم «اِن» باید باشد
# 240. 
# 241. dot (.)
# 242. text = 'this is fun'
# 243. if re.search('f.n', text):
# 244. print('this is ok')
# 245. 
# 246. 
```

## 17.2. 🅱️ ^

```shell
# 247. text = 'Toplearn'
# 248. 
# 249. if re.search('^Top', text):
# 250. print('this is ok')
```

## 17.3. 🅱️  $

```shell
# 251. text = 'Toplearn'
# 252. 
# 253. if re.search('rn$', text):
# 254. print('this is ok')
```

## 17.4. 🅱️ escape

```shell
# 255. text = 'this is a book.'
# 256. 
# 257. if re.search('book\.', text):
# 258. print('this is ok')
```

## 17.5. 🅱️ set

```shell
# 259. text = 'site'
# 260. 
# 261. if re.search('si[tdz]e', text):
# 262. print('this is ok')
```

## 17.6. 🅱️ range

```shell
# 263. text = 'c'
# 264. 
# 265. if re.search('[a-f]', text):
# 266. print('this is ok')
```

## 17.7. 🅱️ exclude

```shell
# 267. text = 'siue'
# 268. 
# 269. if re.search('si[^tdz]e', text):
# 270. print('this is ok')
```

## 17.8. 🅱️ repeat

```shell
# 271. text = '09123456789'
# 272. 
# 273. if re.match('[0-9]{11}', text):
# 274. print('this is ok')
```

## 17.9. 🅱️ other characters

```shell
# 275. decimal digits => \d
# 276. non decimal digits => \D
# 277. white space => \s
# 278. non white space => \S
# 279. word => \w
# 280. non word => \W

# 281. text = 'abcdef'
# 282. if re.match('(abc|cde)', text):
# 283. print('this is ok')
```

## 17.10. 🅱️ email regex

```python
text = '787jhjkj@test.com'
if re.match('^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print('email is valid')
```

## 17.11. 🅱️ Search

```python
import re

# 284. Behrooz: regexr.com

names = [
    'data.png', 'memory.txt', 'data.txt', 'image.png', 'momy.png'
]

for item in names:
    if re.search('m.m', item):
        print(item)

# 285. re.search('m.m', item): #اگر در این رشته موجود بود
# 286. re.match('m.m', item): # باید دقیقا این رشته مساوی الگو باشد

```

```python
import re
import os

for item in os.walk('/Learning-Concept'):
    for file in item[2]:
        if re.search('\.py', file):
            print(file)

```

# 18. 🅰️ Thread

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

# 19. 🅰️ Number

## 19.1. 🅱️ Leading Zero

```python
number = 1
number = f"{number:03d}"
print(number)

```

</div>