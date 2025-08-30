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

# 5. 🅰️ Basic Syntax

## 5.1. 🅱️ Variables

* متغیرها در پایتون CaseSensitive هستند
* این قابلیت در پایتون وجود دارد که انواع نوع را در یک متغیر وارد نماییم
* مقدار None برابر است با Empty یعنی اگر مقدار `myCount = None` را دیدیم یعنی مقدار myCount برابر است با Empty
* توسط دستور input می‌توان مقدار اولیه برای یک متغیر قرار داد.تابع raw_input در نسخه پایتون۲ بود که منسوخ شد

```python
username = "behrooz"
username = input("Insert username: ")
```

* اگر در تابع print یک fقبل از علامت کوتیشن قرار دهید آنگاه مقادیر قابلیت تفکیک پیدا می‌کنند

```python
# 1️⃣️
BoolData = True
print(f"the BoolData is {BoolData}")  # the BoolData is True
print("the BoolData is {BoolData}")  # the BoolData is {BoolData}
# 2️⃣️
x, y = 400, 500
print(f"sum is : {x + y}")
print(f"multiply 2 and 6 is : {2 * 6}")
```

* می‌توان در خروجی چند متغیر را الحاق کرد

```python
username = "behrooz"
print("Name: " + username)  # Name: behrooz
```

## 5.2. 🅱️ if

```python
# Example1️⃣️: 
userRank = 1
print("you got GOLD medal") if userRank == 1 else print("no medal")
```

## 5.3. 🅱️ for

```python
# Syntax:
for variable in iterable:
    if condition1:
        pass
        if condition2:
            pass
        else:
            pass
    else:
        pass
```

```python
# Example1️⃣️: 
print(sum([x for x in range(40000000)]))

# Example2️⃣️: 
listOfNumbers = [23, 54, 67, 89, 34, 9]
for number in listOfNumbers:
    print(number * 2)

# Example3️⃣️:
[print(x) for x in [1, 2, 3, 4, 5, 6, 11]]

# Example4️⃣️: 
for num in range(1, 10):
    if num % 2 == 1:
        for star in range(1, 6):  # [1, 2, 3, 4, 5]
            print("*" * star)
    else:
        for star in range(5, 0, -1):  # [5, 4, 3, 2, 1]
            print("*" * star)

# Example5️⃣️:

# Example6️⃣️:

# Example7️⃣️: 
```

## 5.4. 🅱️ while

```python
# Example1️⃣️:
password = input("what is your password : ")
while password != "1234":
    print("your password is wrong!!!")
    password = input("what is your password : ")
    print("your password is correct !!!!")

# Example2️⃣️:
num = 1
while num < 30:
    # if(num == 5):
    #     break

    print("\U0001f600" * num)
    print("*" * num)
    num += 1
```

## 5.5. 🅱️ Operation

### 5.5.1. ✅️ OperatorsComparison

<div dir="ltr">

| Operator        | descriptions                                                   |
|-----------------|----------------------------------------------------------------|
| `==`            | returns true if the value of number_1 is equal to number_2     |
| `!=`            | returns true if the value of number_1 is not equal to number_2 |
| `>`             | returns true if the value of number_1 is greater than number_2 |
| `>=` ⇄ `= or >` |                                                                |
| `<`             | returns true if the value of number_1 is less than number_2    |
| `<=` : `= or <` |                                                                |
| `is`            | بررسی مقدار و ماهیت                                            |
| `==`            | بررسی فقط مقدار                                                |

</div>

```python
# Example1️⃣️: 
number_1 = -100
number_2 = -200
print(f"{number_1} == {number_2} : {number_1 == number_2}")  # -> Output:  -100 == -200 : False   
print(f"{number_1} != {number_2} : {number_1 != number_2}")  # -> Output:  -100 != -200 : True  
print(f"{number_1} > {number_2} : {number_1 > number_2}")  # ---> Output:  -100 >  -200 : True  
print(f"{number_1} >= {number_2} : {number_1 >= number_2}")  # -> Output:  -100 >= -200 : True
print(f"{number_1} < {number_2} : {number_1 < number_2}")  # ---> Output:  -100 <  -200 : False
print(f"{number_1} <= {number_2} : {number_1 <= number_2}")  # -> Output:  -100 <= -200 : False  

# Example2️⃣️: 
list1 = ['a', 'b', 'c']
list2 = list1
list3 = list(list1)

print(list1)  # ----------> Output: ['a', 'b', 'c']
print(list2)  # ----------> Output: ['a', 'b', 'c']
print(list3)  # ----------> Output: ['a', 'b', 'c']
print(list1 == list2)  # -> Output: True
print(list1 == list3)  # -> Output: True
print(list1 is list2)  # -> Output: True
print(list1 is list3)  # -> Output: False

```

### 5.5.2. ✅️ Logical Operand

```python
# Example1:🇦 🇳 🇩 
print(f"True and True : {True and True}")  # -------> True and True : True 
print(f"False and True : {False and True}")  # -----> False and True : False  
print(f"True and False : {True and False}")  # -----> True and False : False 
print(f"False and False : {False and False}")  # ---> False and False : False  

# Example2: 
userAge = 17
userGender = "female"
if userAge >= 18 and userGender == "male":
    print("you have to go to soldiery")
else:
    print("you can stay at home")

# Example3:🇴 🇷
print(f"True or True : {True or True}")  # -----------> True or True : True         
print(f"False or True : {False or True}")  # ---------> False or True : True          
print(f"True or False : {True or False}")  # ---------> True or False : True            
print(f"False or False : {False or False}")  # -------> False or False : False          

# Example4: 
weather = "sunny"
if weather == "sunny" or weather == "cloudy":
    print("we can travel")
else:
    print("we can not travel")

# Example5:🇳 🇴 🇹 
print(f"not True : {not True}")  # -----> not True : False       
print(f"not False : {not False}")  # ---> not False : True     

isBrotherComming = False
if not isBrotherComming:
    print("my sister said : i wont come")

# Example6:🇨 🇴 🇲 🇧 🇮 🇳 🇪 
age = 50
if (0 <= age <= 2) or (8 <= age < 65):
    print("you should pay 10 dollars")
if not ((2 < age < 8) or age >= 65):
    print("you should pay 10 dollars")
```

### 5.5.3. ✅️ TernaryOperator(اپراتورهای‌سه‌گانه)

* در برخی زبان‌های برنامه‌نویسی هستند
* به شما امکان میدهد که یک بلوک را ساده نمایید
* `syntax: [value_if_true] if [condition] else [value_if_false]`
    * قسمت value_if_true: مقداری که اگر شرط True باشد باید برگردانده شود
    * فسمت condition: شرط
    * قسمت value_if_false: مقداری که اگر شرط False باشد باید برگردانده شود

```python
# Example1️⃣️: 
a, b = 10, 20
min = a if a < b else b
print(min)  # Output: 10

# Example2️⃣️: True:[Go home], condition1:[age<16], False:[{'Not sure...' if 16 <= age < 18 else 'Welcome'} ---> {True:[Not sure],condition:[16<=age<18],False:[Welcome]}] 
age = 17
result = 'Go home.' if age < 16 else 'Not sure' if 16 <= age < 18 else 'Welcome'
print(result)  # Output: Not sure

# Example3️⃣️: Python: [False=0], [True=1]
a, b = 100, 20

print((a, b)[a < b])  # 1️⃣️(a,b):Tuple 2️⃣️[a < b]:condition --> [a < b]=False --> (a, b)[False] --> (a, b)[0]=a --> (100, 20)[0]=100 --> Output:100
print((a, b)[a > b])  # 1️⃣️(a,b):Tuple 2️⃣️[a > b]:condition --> [a > b]=True ---> (a, b)[True] ---> (a, b)[1]=b --> (100, 20)[1]=20 ---> Output:20
print((b, a)[a < b])  # 1️⃣️(b,a):Tuple 2️⃣️[a < b]:condition --> [a < b]=False --> (b, a)[False] --> (b, a)[0]=b --> (20, 100)[0]=20 ---> Output:20
print((b, a)[a > b])  # 1️⃣️(b,a):Tuple 2️⃣️[a > b]:condition --> [a > b]=True ---> (b, a)[True] ---> (b, a)[1]=a --> (20, 100)[1]=100 --> Output:100

# Example4️⃣️: Python: [False=0], [True=1]
a, b = 10, 20
print((lambda: b, lambda: a)[a < b]())  # (lambda:b, lambda:a)[True=1] -->  function: lambda:a ---> Output: 10

# Example5️⃣️:
a, b = 10, 20
print("Both a and b are equal" if a == b else "a is greater than b"
if a > b else "b is greater than a")
# Output: b is greater than a

# Example5️⃣️: هردو مثال یکسان هستند
a, b = 10, 20
if a != b:
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")
else:
    print("Both a and b are equal")
# Output: b is greater than a

# Example6️⃣️:
a, b = 5, 7
print(a, "is greater") if (a > b) else print(b, "is Greater")  # output: 7 is Greater
```

# 6. 🅰️ exception

## 6.1. 🅱️ Error

```python
# Syntax
try:
    pass
except NameError as NameE:  # Handle NameError
    print(NameE)
    print(NameE.message)
    pass
except IOError as IOE:  # Handle IOError
    print(IOE)
    print(IOE.message)
except:  # ErrorHandler of each other error type
    pass
else:
    pass  # ExecuteCode if tryBlock run without Error
finally:
    pass  # در هر صورت این بلاک اجرا خواهد شد

```

## 6.2. 🅱️ Error-Raise

```python
def print_with_custom_color(text, color, indx):
    colors = ('red', 'green', 'blue')
    if type(text) is not str:
        raise TypeError("text must be a string")
    elif color not in colors:
        raise ValueError(f"{color} is not in colors")
    elif indx >= len(colors):
        raise IndexError('index out of range')
    elif colors[indx] != color:  # بررسی تطابق اندیس و رنگ
        raise ValueError('invalid value')
    else:
        print(f"printed {text} in {color}")


print_with_custom_color("hello", "red", 0)  # printed hello in red
print_with_custom_color("hello", "red", 1)  # raises ValueError: invalid value
```

## 6.3. 🅱️ Debug(pdb)

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

# 7. 🅰️ Function

* اگر یک تابع در داخل یک کلاس تعریف گردد آنگاه برای اینکه به مقادیر کلاس دسترسی داشته باشد باید آرگومان اول آن را کلمه کلیدی self قرار دهید
* کاراکترهای پرانتز باز و بسته  `()` عملگر فراخوانی تابع یا call operator است.

بدنه یک تابع به فرم زیر می‌باشد

```python
# Example1️⃣️: 
def exponent(num, power=2):
    return num ** power


print(exponent(5))  # output: 25


# Example2️⃣️: 
def showFullName(first, last):
    return f"{first} {last}"


print(showFullName("MohammadiNasab", "Behrooz"))
print(showFullName(last="MohammadiNasab", first="Behrooz"))  # تغییر در ترتیب پارامتر ورودی

# Example3️⃣️:
a = 10


def f():
    return a


f()  # Output: 10
f  # Output: <function f at 0x7f89357a5580>
print(f)  # Output: <function f at 0x7f89357a5580>
print(f())  # Output: 10

# lambda
(lambda: a)()  # Output: 10
(lambda: a)  # Output: <function <lambda> at 0x7f89357677e0>
print((lambda: a))  # Output: <function <lambda> at 0x7f892fe12c00>
print((lambda: a)())  # Output: 10
```

## 7.1. 🅱️ Lambda

* لامبدا در اصل یک تابع است(نوعی از تعریف تابع است) که تنها در یک خط تعریف می‌شود
* به «توابع یک خطی» یا «Annonymous function» معروف هستند

```python
# Syntax is:
# lambda arg1, arg2: arg1 * arg2 + 10
# lambda arg1      : value_if_true if condition  else  value_if_false
# lambda arg1      : value_if_true if condition1 else  (value_if_true2 if condition2 else value_if_false)
```

```python
# Example1️⃣️: 
function1 = lambda arg1, arg2: arg1 * arg2 + 10
print(function1(5, 2))  # output: 20

# Example2️⃣️: 
function2 = lambda x: "Positive" if x > 0 else ("Zero" if x == 0 else "Negative")
print(function2(-5))  # Output: Negative
print(function2(0))  # Output: Zero
print(function2(4))  # Output: Positive

```

## 7.2. 🅱️ Agmuments

* اگر در هنگام تعریف بدنه یک تابع همه موارد parameters و args و defaultParameters و kwargs داشته باشیم ترتیب اولویت به
  شکل زیر است
    * 1️⃣️ `Positional Parameters` پارامترهای عادی
    * 2️⃣️ `*args` یعنی متغیرهای نام‌گذاری‌نشده
        * ◄ متغیرها ازنوع Tuple و غیرقابل تغییرخواهدبود(Immutable یا غیرقابل تغییر)
    * 3️⃣️ `default parameters` یعنی تعیین مقدار پیش‌فرض برای متغیر
        * اگر درهنگام فراخوانی تابع مقدار متغیر تعیین نشود آنگاه مقدارپیش‌فرض بعنوان مقدار متغیر لحاظ می‌گردد
    * 4️⃣️ `**kwargs` یعنی Dictionary ◄ متغیر دارای محتوی کلید و مقدار است
* توجه: ترتیب *args قبل از default و **kwargs الزامی است.

### 7.2.1. ✅️ PositionalParameters

```python
# Example1️⃣️
def greet(name, age):
    print(f"Hi {name}، you are {age} years old")


greet("Ali", 25)  # Output: Hi Ali، you are 25 years old


# Example2️⃣️
def add_numbers(a, b, c):
    return a + b + c


result = add_numbers(10, 20, 30)
print(result)  # Output: 60

```

### 7.2.2. ✅️ `*args`

* با استفاده از *args می‌توان تعداد نامشخصی از ورودی‌ها را به صورت یک Tuple (غیرقابل تغییر) دریافت کرد.
* args یک تاپل است و Immutable (غیرقابل تغییر) است

```python
# Example1️⃣️
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all(1, 2, 3, 4))  # Output: 10
print(sum_all(5, 10))  # Output: 15


# Example2️⃣️
def print_names(*names):
    for name in names:
        print(f"ٔName: {name}")


print_names("Zeinab", "Mohadeseh", "Tasnim")
# Output:
# Name: Zeinab
# Name: Mohadeseh
# Name: Tasnim
```

### 7.2.3. ✅️ DefaultParameters

اگر مقداری به پارامتر داده نشود، از مقدار پیش‌فرض استفاده می‌شود

```python
# Example1️⃣️
def introduce(name, job="Unknown"):
    print(f"I am {name}، my job is {job}.")


introduce("Zahra")  # Output: I am Zahra ، my job is Unknown.
introduce("Hassan", "Engineer")  # Output: I am Hassan، my job is Engineer.


# Example2️⃣️
def power(base, exponent=2):
    return base ** exponent


print(power(3))  # Output: 3^2 = 9
print(power(3, 3))  # Output: 3^3 = 27
```

### 7.2.4. ✅️ `**kwargs`

با `**kwargs` می‌توان ورودی‌های نام‌دار متغیر را به صورت دیکشنری دریافت کرد.

```python
# Example1️⃣️
def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


user_info(name="Behrooz", age=30, city="Tehran")


# Output:
# name: Behrooz
# age: 30
# city: Tehran

# Example2️⃣️
def create_profile(**details):
    profile = {}
    for key, value in details.items():
        profile[key] = value
    return profile


profile = create_profile(username="ali123", email="ali@example.com", role="admin")
print(profile)  # Output: {'username': 'ali123', 'email': 'ali@example.com', 'role': 'admin'}
```

### 7.2.5. ✅️ Combine

```python
def full_function(a, b, *args, c=10, **kwargs):
    print("a:", a)
    print("b:", b)
    print("*args:", args)
    print("c (default):", c)
    print("**kwargs:", kwargs)


full_function(1, 2, 3, 4, 5, c=50, name="Sarah", age=25)

# Output:
# a: 1
# b: 2
# *args: (3, 4, 5)
# c (default): 50
# **kwargs: {'name': 'Sarah', 'age': 25}
```

## 7.3. 🅱️ __NAME__

### 7.3.1. ✅️ `__init__`

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

### 7.3.2. ✅️ `__len__`

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

### 7.3.3. ✅️  `__add__` و `__mul__` و `__truediv__` و `__sub__`

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

### 7.3.4. ✅️  `__repr__`

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

* می‌توانید رفتار repr() را در کلاس‌های خود با تعریف متد __repr__() تنظیم کنید

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


p = Person("Ali", 25)
print(repr(p))  # Person(name='Ali', age=25)
print(p)  # Person(name='Ali', age=25)
# نکته: `print(p)` و `print(repr(p))` خروجی یکسان دارند زیرا print از str استفاده می‌کند، اما str وقتی `__str__` نباشد از repr استفاده می‌کند)
```

### 7.3.5. ✅️ `__str__`

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

### 7.3.6. ✅️ `__all__`

* یک لیست از رشته‌ها (strings)  است که نام متغیرها، توابع، یا کلاس‌هایی هستند که وقتی از یک ماژول یا package از طریق import * استفاده می‌کنید، وارد می‌شوند
* قابلیت تعریف کردن در ۱-فایل‌های .py (ماژول) و ۲-در فایل __init__.py (package)

📌️ **دلایل استفاده**

* کنترل دقیق بر روی آنچه قابل ایمپورت است
    * هنگام عدم استفاده از __all__ درهنگام import * تمام نام‌های عمومی یا PublicNames داخل ماژول ایمپورت می‌شوند
    * منظور از PublicNames ها مواردی است که با آندرلاین شروع **نمی‌شوند** (توابع یا کلاس‌ها و متغیرها)
* عدم آلودگی namespace
    * وقتی import * می‌کنید، تمام نام‌ها به scope فعلی وارد می‌شوند. این می‌تونه باعث تداخل نام‌ها بشه.
    * با استفاده از __all__ می‌تونی دقیق مشخص کنی که چه چیزهایی قراره وارد بشن.

📌️ **نحوه تعریف:**: * عبارت __all__ حتما باید در انتها تعریف شود

فرض کنید بسته mymodule.py با محتوی زیر دارد

```python
def func1():
    print("func1")

def func2():
    print("func2")

class func3:
    print("func3")

__all__ = ['func1', 'func3']
```

حالا وقتی بنویسید:

```python
from mymodule import *
```

فقط func1 و func3 ایمپورت می‌شوند.

## 7.4. 🅱️ Reversed

```python
numbers = [1, 2, 3, 4, 5, 6]

# 118. numbers.reverse() #در لیست تغییر ایجاد میکند

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

## 7.5. 🅱️ Sort

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


# 119. لیست ها برای مرتب سازی نیاز به کلید دارند


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

## 7.6. 🅱️ Length

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

## 7.7. 🅱️ TruthinessFalsiness_All

### 7.7.1. ✅️ ALL

```python
# 120. بررسی درستی یا نادرستی یا همان تروسینس یا فالسینس
# 121. اگر تمام آیتم‌های داده شده به این تابع درست باشد مقدار ترو را برمی‌گرداند
# 122. عدد صفر بطور پیش‌فرض در پایتون مقدار فالس در نظر گرفته شده است

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

# 123. همه آیتم هایی که در نامبر هستند بر دو بخش پذیر هستند یا خیر
print(all([num % 2 == 0 for num in numbers]))

```

### 7.7.2. ✅️ Any

```python
# 124. بررسی درستی یا نادرستی یا همان تروسینس یا فالسینس
# 125. اگر تنها حتی یک آیتم از مواردی که به این تابع داده شده است ترو باشد مقدار ترو را برمی‌گرداند

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

# 8. 🅰️ Decorator

## 8.1. 🅱️ function into function

استفاده از تابع درون تابع دیگر به روش های متفاوت انجام می‌شود که نمونه‌های آن در ذیل آمده است

### 8.1.1. ✅️ Traditional

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

### 8.1.2. ✅️ Traditional-ByReturnValue

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

### 8.1.3. ✅️ Traditional-ByArgs

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

### 8.1.4. ✅️ Modern-ByDecorator

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

## 8.2. 🅱️ Classmethod

* تغییر عملکرد یک تابع بطوریکه به‌جای استفاده از منابع نمونه از منابع کلاس استفاده می‌کند
* دسترسی مستقیم به دیتای کلاس بدون ساخت شیء نمونه

```python
class User:
    activeUsers = 0

    @classmethod
    def func1(cls):
        return cls.activeUsers


# 126. روش 1️⃣️: بدون نیاز ساخت شیء از کلاس
print(User.func1())

# 127. روش 2️⃣️: الزام بر ساختن شیء از کلاس"

obj1 = User()
print(obj1.func1())

```

## 8.3. 🅱️ Property

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

## 8.4. 🅱️ PropertyGetterSetter

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

## 8.5. 🅱️ Advanced

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


# 128. x only sent to wrapper[not sent to num_before_after]
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

## 8.6. 🅱️ Example

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

# 9. 🅰️ Iterate

```python
# 129. iterate: پیمایش یا تکرار کردن
# 130. 
# 131. iterable: Objects which can iterate and can convert to iterator
# 132. ---> iterableObjects: Lists, Tuples, Dictionaryes, Sets, Strings
# 133. ---------> iterableObject is not a iterator[but by function it can chage to iterator]
# 134. ---> Note: we can not iterate on iterableObjects first. It should be converted to iterator and then iterate on it
# 135. ---> Note: موضوع توالی و پشت سر هم بودن، جزء مهمترین مولفه در این ساختار است
# 136. ---> Generally ussing with loops(for and ...)
# 137. ---> next(): ussing next function for access to next item
# 138. 
# 139. iterator: object that can iterate on items by itself, and It can sequentially access the elements of an iterable
# 140. ---> iterator=iterableObjects.iter();
# 141. ---> class who must define __iter__() to  return iterator [Obj.iter()]
# 142. ---> class who must define __next__() to  return next item and if nextItem is not available, return [StopIteration exception]) [Obj.next()]


numbers = [1, 2, 3]  # iterableObjects
colors = ('red', 'green', 'blue')  # iterableObjects
name = "Behrooz"  # iterableObjects

iterator = iter(numbers)

print(iterator)  # output: <list_iterator object at 0x7fb1fd78e8f0>
print(next(iterator))  # output: 1
print(next(iterator))  # output: 2
print(next(iterator))  # output: 3
# 143. print(next(iterator)) # output: Exception(StopIteration) [only 3 items is Exist in iterableObjects]


iterName = iter(name)
print(next(iterName))
print(next(iterName))
print(next(iterName))
print(next(iterName))

```

## 9.1. 🅱️ Dictionary

```python
# 144. List       → []
# 145. Dictionary → { key1: value1, key2: value2 }
# 146. Set        → {} 1-All Items must be uniq (No repeat)
# 147. 2-without sort
# 148. 3-without index #اندیس ناپذیر
# 149. 4-without call # نمی‌توانیم فراخوانی داشته باشیم
# 150. 
# 151. Tuple      → () 1-Items cannot change(immutable)

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
# 152. behrooz.printValuesByFor()
# 153. behrooz.printKeysByFor()
# 154. behrooz.printKeyValuesByFor()
# 155. behrooz.isExist("name")
# 156. behrooz.clearData()

# 157. print(behrooz.copyData().get("age"))
# 158. print(behrooz.copyData() == one)
# 159. print(behrooz.copyData() is one)

# 160. behrooz.popLastItem()
# 161. behrooz.printKeyValuesByFor()

# 162. behrooz.concatenateDictionary()
# 163. behrooz.printKeyValuesByFor()

# 164. value1, value2, value3 = behrooz.returnValue()
# 165. print(f"name:{value1}\n\nfamily:{value2}\n\nage:{value3}")

behrooz.printAll()

behrooz.func4(name="behrooz")
behrooz.func4(name="behrooz", FamilyName="Mohammadi")
behrooz.func4(name="behrooz", FamilyName="Mohammadi", born=1369, mobile="09191671085")

```

## 9.2. 🅱️ Set

```python
# 166. List       → []
# 167. Dictionary → { key1: value1, key2: value2 }
# 168. Set        → {} 1-All Items must be uniq (No repeat)
# 169. 2-without sort
# 170. 3-without index #اندیس ناپذیر
# 171. 4-without call # نمی‌توانیم فراخوانی داشته باشیم
# 172. 
# 173. Tuple      → () 1-Items cannot change(immutable)


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

## 9.3. 🅱️ Tupple

```python
# 174. List       → []
# 175. Dictionary → { key1: value1, key2: value2 }
# 176. Set        → {} 1-All Items must be uniq (No repeat)
# 177. 2-without sort
# 178. 3-without index #اندیس ناپذیر
# 179. 4-without call # نمی‌توانیم فراخوانی داشته باشیم
# 180. 
# 181. Tuple      → () 1-Items cannot change(immutable)


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

## 9.4. 🅱️ List

```python
# 182. List       → []
# 183. Dictionary → { key1: value1, key2: value2 }
# 184. Set        → {} 1-All Items must be uniq (No repeat)
# 185. 2-without sort
# 186. 3-without index #اندیس ناپذیر
# 187. 4-without call # نمی‌توانیم فراخوانی داشته باشیم
# 188. 
# 189. Tuple      → () 1-Items cannot change(immutable)

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

# 190. behrooz.getDataAll(list._list8)
# 191. behrooz.getDataAllByCount(list._list2)
# 192. behrooz.fillList()
# 193. behrooz.getDataAll(list._list4)
# 194. behrooz.getDataAll_Revese(list._list1)
# 195. behrooz.get_select_item(list.list1)
# 196. print(list._list10_nestedList[1][2])  # output: 6
# 197. [[print(x) for x in y] for y in list._list10_nestedList] # output: 1 NewLine 2 NewLine 3 NewLine 4 NewLine 5 NewLine 6
# 198. behrooz.listFunctions(list._list1)
# 199. behrooz.search(list._list1)
# 200. print(list._list11)

# 201. behrooz = list()

```

## 9.5. 🅱️ Filter

* برای یاد گیری سه مفهوم ۱-لامبدا ۲-فیلتر ۳-مَپ ،باید به ترتیب نام برده شده مطالعه شود

* انتخاب یک المان تحت شرایط
* فیلتر روی یک ایتریبل اگر در شرط بگنجد
    * Filter a iterable by condition(only apply to items which true condition on it)
* itarate: پیمایش

```python
# 202. Syntax:                        filter(function, iterable)
# 203. return:                        IterableObject
# 204. How ussing IterableObject:     list(IterableObject) or  Tuple(IterableObject)
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

## 9.6. 🅱️ map

```python
# 205. map: calls a function for all its members of iterable
# 206. ---> Syntax: map(function, iterable) ==> Return: an iterable mapObject
# 207. ==> Ussing: list(mapObject) or Tuple(mapObject) or ...
# 208. ---> Note: تنها یکبار روی لیست یا غیره می‌تواند پیمایش صورت بپذیرد و در پیمایش دوم با لیست خالی مواجه می‌شود
# 209. ---> itarate: پیمایش
# 210. ---> iterable: هر چیزی که روی آیتم‌های آن قابلیت پیمایش وچود داشته باشد
# 211. ---> Note:  به صورت «لِیزی» عمل می‌کند، به این معنی که محاسبات تنها زمانی انجام می‌شود که به نتایج آن نیاز باشد


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

## 9.7. 🅱️ Generator_Expression

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

### 9.7.1. ✅️ Example 1️⃣️: yield

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

### 9.7.2. ✅️ Example 2️⃣️: Generator

```python
myGenerator = (num for num in range(20))
print(myGenerator)
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
```

### 9.7.3. ✅️ Example 3️⃣️: yield

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
# 212. print(next(counter))  # if run error
```

### 9.7.4. ✅️ Example4️⃣️: Fibunachi()

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

### 9.7.5. ✅️ Example 5️⃣️

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

## 9.8. 🅱️ Zip

```python
# 213. تلفیق دو ایتِرِیت با یکدیگر تبدیل به یک ایتریت جدید که شامل هردوی آن‌ها می‌باشد
# 214. اگر یک بار پیمایش شود خالی خواهد شد

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

## 9.9. 🅱️ Iterate_class_example

```python
# example 1️⃣️
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


# 216. استفاده از iterator
my_iter = MyIterator(5)
for number in my_iter:
    print(number)


# example 2️⃣️
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


# example 3️⃣️
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

# 10. 🅰️ OOP(Object Oriented Programming)

* در کلاس‌ها درحین تعریف یک تابع در داخل آن تابع اگر از کلمه کلیدی self استفاده نشود آنگاه متغیرهای کلاس همراه آورده
  نمی‌شود
* کلمه پارامتر بعنوان ورودی در وقت استفاده از تابع است و کلمه آرگومان بعنوان ورودی‌های یک تابع در بدنه یک فانکشن است

```python
# 219. import random
# 220. import random as rand
# 221. from random import *
# 222. from random import randint, choice
# 223. from random import randint as r_i, choice as r_ch

# 224. vsCode--> python: select interpreter #تغییر در ورژن‌های پایتون در ویژوآل استودیو کد
# 225. encapsulation: توابع و متغیرها و موارد را در یک کلاس قرار بدهیم
# 226. __name__ --> name of the module(file)


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

## 10.1. 🅱️ NameMangling

```python
# 227. _name    => define local variable
# 228. Note: در پایتون هیچ قلمرویی تحت عنوان پرایویت نداریم
# 229. Note: استفاده از یک آندرلاین قبل متغیر تنها یک قرارداد است ولی باز در هرکجا به پرایویت می‌توان دسترسی داشت

# 230. __name   => name mangling: available only with _classname__variable in use time
# 231. Note: در پایتون همه نامگذاری‌ها قراردادی است ولی تنها نِیم‌مَنگِلینگ است که سبب تغییر در نام آیتم می‌شود

# 232. __name__ => in python special function define in this form such as __init__ as construction


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

## 10.2. 🅱️ Override

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

## 10.3. 🅱️ Static

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

# 11. 🅰️ File

## 11.1. 🅱️ Read

```python
data = open("/etc/passwd")

# 233. 1)
# 234. print(data.read())
# 235. data.seek(2) # جابجایی کرسر به نقطه خاص از فایل
# 236. print(data.read())

# 237. 2)
# 238. textLines = data.readlines() # یک لیست از خطوط که آخر هر خط یک بک‌اسلش‌اِن قرار میدهد
# 239. print(textLines)
# 240. print(f"----> {textLines[5]}")


# 241. 3)
with open("/etc/passwd", encoding='UTF-8', mode="r") as bFile:
    for l in bFile:
        line = l.strip()
        # mylist = lines.rsplit(",")
        print(line)

```

## 11.2. 🅱️ Write

```python
# 242. mode:
# 243. a: append
# 244. w: read
# 245. r: write


with open("/tmp/salam.txt", encoding='UTF-8', mode="w") as bFile:
    bFile.write("STRIIIIIIIIIIIIIIIIIIIIIIIIIIING\n")

```

## 11.3. 🅱️ module os

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

# 246. result = os.stat('./my_files/doc.txt')
# 247. print(time.ctime(result.st_mtime))

# 248. os.mkdir('test')  # 1-Error if exist 2-Error with subDirectory
# 249. os.makedirs('/tmp/test/sub_ddsfdsfdsfsirectory1')  # 1-Error if exist


print('################')
print('#### Delete ####')
print('################')

# 250. os.remove("/tmp/test/sub_ddsfdsfdsfdsfsirectory1"); # اگر فایل موجود نباشد خطا برمی‌گرداند
# 251. os.unlink("/tmp/test/sub_ddsfdsfdsfsdfsdfsdfsdfdsfdsfsirectory1"); # اگر فایل موجود نباشد خطا برمی‌گرداند

# 252. os.rmdir("/tmp/test/sub_ddsfdsfdsfsdfsdfsdfsdfdsfdsfsirectory1"); # فقط پوشه های خالی رو پاک میکنه


# 253. ---------------------------------------------------------------------------------------------------------

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

## 11.4. 🅱️ Module Pathlib

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
# 254. file_path.unlink() # حذف فایل
# 255. file_path.rmdir() # حذف فولدر خالی

print('################')
print('#### Search ####')
print('################')

shutil.rmtree('./test', ignore_errors=True)

path = Path('')  # root of projects
data = path.glob('**/*.py')
print(list(data))

```

## 11.5. 🅱️ Module shutil

```python
import os
import shutil

# 256. shutil.copy('src', 'Des') # Only copy file
# 257. print(os.stat('./my_files/data-1.txt'))
# 258. print(os.stat('./new_my_files/new-data-1.txt'))

# 259. shutil.copy2('./my_files/data-2.txt', 'Des') # copy file with metadata
# 260. print(os.stat('./my_files/data-2.txt'))
# 261. print(os.stat('./new_my_files/new-data-2.txt'))

# 262. shutil.copytree('src', 'Des') #create Backup[all _SRCFiles and subDir and Subfiles]

# 263. shutil.move('src', 'Des')

# 264. os.rename('src', 'Des')

```

# 12. 🅰️ JSON

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


# 265. toHtml("/tmp/All.json", "/tmp/All.html")


def showData():
    json_string = '{ "1":"Red", "2":"Blue", "3":"Green"}'
    parsed_json = json.loads(json_string)
    print(parsed_json['2'])

```

# 13. 🅰️Database

## 13.1. 🅱️ SQLlight

```python
import sqlite3

connection = sqlite3.connect("/tmp//my-database.db")
cursor = connection.cursor()

# 266. 1️⃣️
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

# 267. 2️⃣️ Multiple sql command

sql = """
    INSERT INTO Product VALUES (2,'kotlin course',3000,'this is kotlin course');
    INSERT INTO Product VALUES (3,'vue course',4000,'this is vue course');

"""
cursor.execute(sql)
cursor.executescript(sql)

# 268. 3️⃣️

sql = """
    SELECT * FROM Product WHERE description LIKE "%python%"
"""
cursor.execute(sql)
for product in cursor:
    print(product)
```

# 14. 🅰️ GUI

## 14.1. 🅱️ tkinter

### 14.1.1. ✅️ Lable

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

### 14.1.2. ✅️ Button

```python
from tkinter import *
import tkinter.font as font

from matplotlib.ft2font import ITALIC

tkWnd = Tk()
tkWnd.title("button")
tkWnd.geometry('400x300')
tkWnd.resizable(width=False, height=False)
# 269. tkWnd.configure(bg='white')
# 270. tkWnd['bg']='green'
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

### 14.1.3. ✅️ Calculator پوسته

```python
from tkinter import *

# 271. ========================== settings ========================
root = Tk()
root.geometry('400x200')
root.title('calculator')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# 272. ========================== frames ==========================
top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)

# 273. ========================== Buttons ==========================

btn_plus = Button(top_third, text="+", width=10, highlightbackground=color)
btn_plus.pack(side=LEFT, padx=10, pady=10)

btn_minus = Button(top_third, text="-", width=10, highlightbackground=color)
btn_minus.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_third, text="*", width=10, highlightbackground=color)
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_third, text="/", width=10, highlightbackground=color)
btn_div.pack(side=LEFT, padx=10, pady=10)

# 274. ========================== Entries and Labels ==========================

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

### 14.1.4. ✅️ Calculator

```python
from tkinter import *
import tkinter.messagebox

# 275. ========================== settings ========================
root = Tk()
root.geometry('400x200')
root.title('calculator')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# 276. ========================== variables ==========================

num1 = StringVar()
num2 = StringVar()
res_value = StringVar()

# 277. ========================== frames ==========================
top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)


# 278. ========================== Functions ==========================

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


# 279. ========================== Buttons ==========================

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

# 280. ========================== Entries and Labels ==========================

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

### 14.1.5. ✅️ Entry

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

### 14.1.6. ✅️ Frame

```python
from tkinter import *

# 281. ========================== settings ========================
root = Tk()
root.geometry('800x500')
root.title('calculator')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# 282. ========================== frames ==========================
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

# 15. 🅰️ Regex

* Need to`import re`

## 15.1. 🅱️ dot

```shell
# 283. (.) -> Note: یک کاراکتر
# 284. (f.n) --> کاراکتر اول «اِف» و کاراکتر دوم هر چیزی می‌تونه باشه و کاراکتر سوم «اِن» باید باشد
# 285. (f..n) --> کاراکتر اول «اِف» و کاراکتر دوم و سوم هر چیزی می‌تونه باشه و کاراکتر چهارم «اِن» باید باشد
# 286. 
# 287. dot (.)
# 288. text = 'this is fun'
# 289. if re.search('f.n', text):
# 290. print('this is ok')
# 291. 
# 292. 
```

## 15.2. 🅱️ ^

```shell
# 293. text = 'Toplearn'
# 294. 
# 295. if re.search('^Top', text):
# 296. print('this is ok')
```

## 15.3. 🅱️  $

```shell
# 297. text = 'Toplearn'
# 298. 
# 299. if re.search('rn$', text):
# 300. print('this is ok')
```

## 15.4. 🅱️ escape

```shell
# 301. text = 'this is a book.'
# 302. 
# 303. if re.search('book\.', text):
# 304. print('this is ok')
```

## 15.5. 🅱️ set

```shell
# 305. text = 'site'
# 306. 
# 307. if re.search('si[tdz]e', text):
# 308. print('this is ok')
```

## 15.6. 🅱️ range

```shell
# 309. text = 'c'
# 310. 
# 311. if re.search('[a-f]', text):
# 312. print('this is ok')
```

## 15.7. 🅱️ exclude

```shell
# 313. text = 'siue'
# 314. 
# 315. if re.search('si[^tdz]e', text):
# 316. print('this is ok')
```

## 15.8. 🅱️ repeat

```shell
# 317. text = '09123456789'
# 318. 
# 319. if re.match('[0-9]{11}', text):
# 320. print('this is ok')
```

## 15.9. 🅱️ other characters

```shell
# 321. decimal digits => \d
# 322. non decimal digits => \D
# 323. white space => \s
# 324. non white space => \S
# 325. word => \w
# 326. non word => \W

# 327. text = 'abcdef'
# 328. if re.match('(abc|cde)', text):
# 329. print('this is ok')
```

## 15.10. 🅱️ email regex

```python
text = '787jhjkj@test.com'
if re.match('^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print('email is valid')
```

## 15.11. 🅱️ Search

```python
import re

# 330. Behrooz: regexr.com

names = [
    'data.png', 'memory.txt', 'data.txt', 'image.png', 'momy.png'
]

for item in names:
    if re.search('m.m', item):
        print(item)

# 331. re.search('m.m', item): #اگر در این رشته موجود بود
# 332. re.match('m.m', item): # باید دقیقا این رشته مساوی الگو باشد

```

```python
import re
import os

for item in os.walk('/Learning-Concept'):
    for file in item[2]:
        if re.search('\.py', file):
            print(file)

```

# 16. 🅰️ Thread

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

</div>