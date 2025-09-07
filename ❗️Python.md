<div dir="rtl">

# 1. 🅰️ Concept

## 1.1. 🅱️ Name Conventions

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

## 1.2. 🅱️ LocalVariable: `_name`

* در پایتون هیچ قلمرویی تحت عنوان private نداریم و پیرو قرارداد به این متغیرهای محلی گفته می‌شود اما در هرکجابه private می‌توان دسترسی داشت
* در پیشنهادهای IDE نمایش داده نمی‌شود
* این عضو برای استفاده داخلی کلاس یا ماژول طراحی شده و نباید توسط کاربران خارجی مستقیماً استفاده شود
* مفسر پایتون به هیچ وجه دسترسی به آن را مسدود نمی‌کند.
* فقط یک اخطار معنایی برای توسعه‌دهندگان است
* در پایتون، هیچ سیستم دسترسی سفت و سختی (مانند private, protected در جاوا) وجود ندارد.
  ش

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Convention: Local variable

    def get_age(self):
        return self._age

    def _private_method(self):  # Convention: Local Function
        print("این متد فقط برای استفاده داخلی است")


p = Person("Ali", 25)

print(p.name)  # دسترسی مجاز
print(p._age)  # دسترسی مجاز از نظر زبان، اما نقض قرارداد است زیرا بصورت پاپلیک استفاده شده است
p._private_method()  # کار می‌کند، اما نباید فراخوانی شود
```

## 1.3. 🅱️ NameMangling: `__name`

NameMangling: available only with _classname__variable in use time

* وقتی از دو خط زیرین قبل از نام یک عضو کلاس استفاده می‌شود، پایتون عملی به نام `Name Mangling` انجام می‌دهد. این عمل:
    1. نام عضو را به صورت خودکار تغییر می‌دهد تا دسترسی به آن از خارج کلاس دشوارتر شود.
    2. نام جدید به صورت `_ClassName__name` خواهد بود.
* هدف: جلوگیری از تداخل نام در کلاس‌های پایه و فرزند.
* در پایتون همه نامگذاری‌ها قراردادی است ولی تنها نِیم‌مَنگِلینگ است که سبب تغییر در نام آیتم می‌شود

```python
# Example1️⃣️: 
class Person:
    def __init__(self, name):
        self.__name = name  # Name Mangling اعمال می‌شود


p = Person("Ali")

# print(p.__name)  # ❌️ AttributeError: 'Person' object has no attribute '__name'
print(p._Person__name)  # Ali — دسترسی مستقیم اما غیرمستقیم


# Example2️⃣️: 
class User:
    _mobile = "0919XXXXXXX"  # Convention: Local variable
    __password = "myPassword"  # only available by _User__password

    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    @property
    def get_mobile(self):
        return self._mobile


obj = User("behrooz", 33)
print(obj.name)
print("❌️:" + obj._mobile)  # استفاده از پارامتر محلی داخل یک کلاس به‌صورت مستقیم توصیه نمی‌شود
print("✅️:" + obj.get_mobile)
print(obj._User__password)  # وقتی یک پارامتر را با دوتا آندرلاین تعریف کنیم و توسط شکل فوق به آن دسترسی داشته باشیم را nameMangling می‌گویند


# Example3️⃣️:  Name Mangling در وراثت
class A:
    def __init__(self):
        self.__value = 10


class B(A):
    def __init__(self):
        super().__init__()
        self.__value = 20  # conflict prevention


b = B()
print(b._A__value)  # 10
print(b._B__value)  # 20
```

## 1.4. 🅱️ DunderMethod

* نام‌هایی که با دو خط زیرین شروع و به دو خط زیرین ختم می‌شوند (مانند __name__)
    * Special Methods
    * DunderMethods: Double Underscore Methods
* این متدها:
    * توسط مفسر پایتون به صورت خودکار فراخوانی می‌شوند.
    * رفتار اشیاء را در عملیات استاندارد تعریف می‌کنند (مثل +, len(), print و غیره).
    * بخشی از پروتکل‌های پایتون هستند (مانند iteration, context manager, و غیره).

<div dir="ltr">

| نام متد             | توضیحات                                           | مثال                             |
|---------------------|---------------------------------------------------|----------------------------------|
| `__init__`          | سازنده شیء: هنگام ساخت شیء فراخوانی می‌شود        | `obj = MyClass()`                |
| `__new__`           | ایجاد شیء قبل از `__init__`                       | (کمتر استفاده می‌شود)            |
| `__del__`           | تخریب شیء (هنگام حذف)                             | `del obj`                        |
| `__str__`           | نمایش رشته‌ای قابل خواندن برای کاربر              | `str(obj)`, `print(obj)`         |
| `__repr__`          | نمایش رسمی و دقیق شیء (برای دیباگ)                | `repr(obj)`                      |
| `__len__`           | طول شیء                                           | `len(obj)`                       |
| `__getitem__`       | دسترسی به آیتم با `[]`                            | `obj[key]`                       |
| `__setitem__`       | تنظیم آیتم با `[]`                                | `obj[key] = value`               |
| `__delitem__`       | حذف آیتم با `del`                                 | `del obj[key]`                   |
| `__iter__`          | بازگرداندن یک ایتراتور                            | `iter(obj)`                      |
| `__next__`          | بازگرداندن عنصر بعدی در حلقه                      | `next(obj)`                      |
| `__contains__`      | بررسی عضویت با `in`                               | `'x' in obj`                     |
| `__call__`          | امکان فراخوانی شیء مثل تابع                       | `obj()`                          |
| `__getattr__`       | وقتی صفتی پیدا نشد فراخوانی می‌شود                | `obj.missing_attr`               |
| `__getattribute__`  | هر دسترسی به صفت                                  | `obj.attr`                       |
| `__setattr__`       | تنظیم یک صفت                                      | `obj.attr = 5`                   |
| `__delattr__`       | حذف یک صفت                                        | `del obj.attr`                   |
| `__dir__`           | لیست صفات و متدهای شیء                            | `dir(obj)`                       |
| `__dict__`          | دیکشنری حاوی صفات شیء                             | `obj.__dict__`                   |
| `__class__`         | کلاس شیء                                          | `obj.__class__`                  |
| `__doc__`           | رشته توضیحات کلاس یا تابع                         | `obj.__doc__`                    |
| `__module__`        | نام ماژولی که کلاس تعریف شده                      | `obj.__module__`                 |
| `__bases__`         | والدین کلاس (برای کلاس‌ها)                        | `MyClass.__bases__`              |
| `__name__`          | نام کلاس یا تابع                                  | `MyClass.__name__`               |
| `__qualname__`      | نام کیفیت‌دار (با مسیر کامل)                      | `MyClass.__qualname__`           |
| `__mro__`           | ترتیب حل روش (Method Resolution Order)            | `MyClass.__mro__`                |
| `__subclasses__`    | زیرکلاس‌های مستقیم                                | `MyClass.__subclasses__()`       |
| `__add__`           | جمع (`+`)                                         | `obj1 + obj2`                    |
| `__sub__`           | تفریق (`-`)                                       | `obj1 - obj2`                    |
| `__mul__`           | ضرب (`*`)                                         | `obj1 * obj2`                    |
| `__truediv__`       | تقسیم (`/`)                                       | `obj1 / obj2`                    |
| `__floordiv__`      | تقسیم صحیح (`//`)                                 | `obj1 // obj2`                   |
| `__mod__`           | باقیمانده (`%`)                                   | `obj1 % obj2`                    |
| `__divmod__`        | `(a // b, a % b)`                                 | `divmod(obj1, obj2)`             |
| `__pow__`           | توان (`**`)                                       | `obj1 ** obj2`                   |
| `__lshift__`        | شیفت چپ (`<<`)                                    | `obj1 << obj2`                   |
| `__rshift__`        | شیفت راست (`>>`)                                  | `obj1 >> obj2`                   |
| `__and__`           | AND بیتی (`&`)                                    | `obj1 & obj2`                    |
| `__or__`            | OR بیتی (`\|`)                                    | `obj1 \| obj2`                   |
| `__xor__`           | XOR بیتی (`^`)                                    | `obj1 ^ obj2`                    |
| `__invert__`        | NOT بیتی (`~`)                                    | `~obj`                           |
| `__radd__`          | جمع معکوس (`+` وقتی سمت چپ ناهمگون است)           | `int + obj`                      |
| `__rsub__`          | تفریق معکوس                                       | `2 - obj`                        |
| `__rmul__`          | ضرب معکوس                                         | `2 * obj`                        |
| `__rtruediv__`      | تقسیم معکوس                                       | `2 / obj`                        |
| `__rfloordiv__`     | تقسیم صحیح معکوس                                  | `2 // obj`                       |
| `__rmod__`          | باقیمانده معکوس                                   | `2 % obj`                        |
| `__rpow__`          | توان معکوس                                        | `2 ** obj`                       |
| `__rlshift__`       | شیفت چپ معکوس                                     | `1 << obj`                       |
| `__rrshift__`       | شیفت راست معکوس                                   | `1 >> obj`                       |
| `__rand__`          | AND معکوس                                         | `1 & obj`                        |
| `__ror__`           | OR معکوس                                          | `1 \| obj`                       |
| `__rxor__`          | XOR معکوس                                         | `1 ^ obj`                        |
| `__iadd__`          | جمع درجا (`+=`)                                   | `obj += x`                       |
| `__isub__`          | تفریق درجا (`-=`)                                 | `obj -= x`                       |
| `__imul__`          | ضرب درجا (`*=`)                                   | `obj *= x`                       |
| `__itruediv__`      | تقسیم درجا (`/=`)                                 | `obj /= x`                       |
| `__ifloordiv__`     | تقسیم صحیح درجا (`//=`)                           | `obj //= x`                      |
| `__imod__`          | باقیمانده درجا (`%=`)                             | `obj %= x`                       |
| `__ipow__`          | توان درجا (`**=`)                                 | `obj **= x`                      |
| `__ilshift__`       | شیفت چپ درجا (`<<=`)                              | `obj <<= x`                      |
| `__irshift__`       | شیفت راست درجا (`>>=`)                            | `obj >>= x`                      |
| `__iand__`          | AND درجا (`&=`)                                   | `obj &= x`                       |
| `__ior__`           | OR درجا (`\|=`)                                   | `obj \|= x`                      |
| `__ixor__`          | XOR درجا (`^=`)                                   | `obj ^= x`                       |
| `__eq__`            | برابری (`==`)                                     | `obj1 == obj2`                   |
| `__ne__`            | نامساوی (`!=`)                                    | `obj1 != obj2`                   |
| `__lt__`            | کوچکتر (`<`)                                      | `obj1 < obj2`                    |
| `__le__`            | کوچکتر یا مساوی (`<=`)                            | `obj1 <= obj2`                   |
| `__gt__`            | بزرگتر (`>`)                                      | `obj1 > obj2`                    |
| `__ge__`            | بزرگتر یا مساوی (`>=`)                            | `obj1 >= obj2`                   |
| `__hash__`          | محاسبه کلید هش (برای دیکشنری و مجموعه)            | `hash(obj)`                      |
| `__bool__`          | مقدار بولی شیء (`bool()`)                         | `if obj:`                        |
| `__format__`        | فرمت رشته (`format()`)                            | `format(obj, 'fmt')`             |
| `__sizeof__`        | حجم شیء در حافظه                                  | `sys.getsizeof(obj)`             |
| `__instancecheck__` | بررسی نمونه بودن (`isinstance`)                   | `isinstance(obj, Class)`         |
| `__subclasscheck__` | بررسی زیرکلاس بودن (`issubclass`)                 | `issubclass(A, B)`               |
| `__enter__`         | ورود به بلاک `with`                               | `with obj:`                      |
| `__exit__`          | خروج از بلاک `with`                               | `with obj:`                      |
| `__get__`           | دسترسی به دیسکریپتور                              | `obj.attr`                       |
| `__set__`           | تنظیم دیسکریپتور                                  | `obj.attr = x`                   |
| `__delete__`        | حذف دیسکریپتور                                    | `del obj.attr`                   |
| `__set_name__`      | تنظیم نام دیسکریپتور در کلاس                      | (در تعریف کلاس)                  |
| `__prepare__`       | آماده‌سازی namespace کلاس                         | `class MyClass(metaclass=Meta):` |
| `__init_subclass__` | هنگام ساخت زیرکلاس                                | `class Child(Parent):`           |
| `__class_getitem__` | زمان استفاده از `[]` روی کلاس (مثلاً `List[int]`) | `MyClass[int]`                   |
| `__missing__`       | وقتی کلید در دیکشنری پیدا نشد                     | `dict[key]`                      |
| `__reduce__`        | برای `pickle` — سریال‌سازی                        | `pickle.dumps(obj)`              |
| `__reduce_ex__`     | نسخه گسترده `__reduce__`                          | `pickle.dumps(obj)`              |
| `__fspath__`        | تبدیل به مسیر فایل سیستم                          | `os.fspath(obj)`                 |
| `__index__`         | تبدیل به عدد صحیح (برای ایندکس)                   | `obj[1:obj]`                     |
| `__await__`         | امکان استفاده در `await`                          | `await obj`                      |
| `__aiter__`         | ایتراتور ناهمزمان                                 | `async for`                      |
| `__anext__`         | عنصر بعدی ناهمزمان                                | `async for`                      |
| `__aenter__`        | ورود به بلاک `async with`                         | `async with obj:`                |
| `__aexit__`         | خروج از بلاک `async with`                         | `async with obj:`                |
| `__length_hint__`   | حدس طول یک ایترابل                                | `operator.length_hint(iterable)` |
| `__round__`         | گرد کردن                                          | `round(obj)`                     |
| `__trunc__`         | قطع کردن (truncation)                             | `math.trunc(obj)`                |
| `__floor__`         | کف عدد                                            | `math.floor(obj)`                |
| `__ceil__`          | سقف عدد                                           | `math.ceil(obj)`                 |

</div>

### 1.4.1. ✅️ `__init__`

نقش تابع سازنده در هر کلاس را ایفا می‌کند

```python
class User:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def show_data(self):
        print(self.name, self.age)


obj = User("behrooz", 33)
obj.show_data()

```

### 1.4.2. ✅️ `__len__`

تنها درصورتی می‌توان از تابع len استفاده کرد که تابع `__len__` از طریق برنامه‌نویس یا ارث‌بری در کلاس تعریف شده باشد

```python
class Behrooz:
    def __init__(self, _name):  # Constructor
        self.name = _name

    def __len__(self):
        return 20


obj = Behrooz("Ali")
print(len(obj))
```

### 1.4.3. ✅️ `__str__`

* برای خوانایی بیشتر EndUser از یک شیء مورد استفاده قرار می‌گیرد
* این متد زمانی فراخوانی می‌شود که توابعی مانند print یا str برای نمایش یک شیء استفاده شود
* این متد باید یک رشته (str) برگرداند که نماینده‌ی شیء باشد.
* اگر __str__ تعریف نشده باشد، پایتون به جای آن از متد __repr__ استفاده می‌کند.

```python
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


person = Person("علی", 25)
print(person)  # output: Person(name=علی, age=25)
```

### 1.4.4. ✅️  `__repr__`

* باتعریف این تابع سبب می‌شویم در هنگام پرینت آبجکت تهیه شده از یک کلاس تابع اجرا شود وگرنه آدرس شیء در حافظه نمایش
  می‌شود
* تابع `__str__` دیتای خوانا به کاربر ارائه میدهد درحالی که تابع `__repr__` جنبه دیباگ داشته و دیتای فنی تر و جامع و کلیدی ارائه میدهد

```python
class Person:
    def __init__(self, _name):  # Constructor
        self.name = _name

    def __repr__(self) -> str:
        return f"behroooz class attribute is [{self.name}]"


obj = Person("Ali")
print(obj)

```

* می‌توانید رفتار repr() را در کلاس‌های خود با تعریف متد __repr__() تنظیم کنید

```python
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


p = Person("Ali", 25)
print(repr(p))  # Person(name='Ali', age=25)
print(p)  # Person(name='Ali', age=25)
# نکته: `print(p)` و `print(repr(p))` خروجی یکسان دارند زیرا print از str استفاده می‌کند، اما str وقتی `__str__` نباشد از repr استفاده می‌کند)
```

### 1.4.5. ✅️  `__add__`

```python
class Person:
    def __init__(self, _name):  # Constructor
        self.name = _name

    # when ussing +
    def __add__(self, other):
        return f"{self.name} Plus {other}"


obj = Person("Ali")
print(obj)  # --------------> Output: <__main__.Person object at 0x7f5f43c13890>
print(obj + "behrooz")  # --> Output: Ali Plus behrooz
```

### 1.4.6. ✅️   `__mul__`

```python
class Person:
    def __init__(self, _name):  # Constructor
        self.name = _name

    # when ussing *
    def __mul__(self, other):
        return f"{self.name} multiplier {other}"


obj = Person("Ali")
print(obj)  # --------------> Output: <__main__.Person object at 0x7f5f43c13050>   
print(obj * "behrooz")  # --> Output:  Ali multiplier behrooz
```

### 1.4.7. ✅️  `__truediv__`

```python
class Person:
    def __init__(self, _name):  # Constructor
        self.name = _name

    # when ussing /
    def __truediv__(self, other):
        return f"{self.name} division {other}"


obj = Person("Ali")
print(obj)  # --------------> Output: <__main__.Person object at 0x7f5f43c31c10>    
print(obj / "behrooz")  # --> Output: Ali division behrooz
```

### 1.4.8. ✅️   `__sub__`

```python
class Person:
    def __init__(self, _name):  # Constructor
        self.name = _name

    # when ussing -
    def __sub__(self, other):
        return f"{self.name} minus {other}"


obj = Person("Ali")
print(obj)  # --------------> Output:  <__main__.Person object at 0x7f5f43c31e90>          
print(obj - "behrooz")  # --> Output: Ali minus behrooz
```

# 2. 🅰️ Tools

## 2.1. 🅱️ Commands

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

### 2.1.1. ✅️ pip

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

### 2.1.2. ✅️ python3

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

### 2.1.3. ✅️ django-admin

```shell
django-admin #اگر بدون پارامتر باشد نمایش لیستی از دستورات در دسترس از جنگو
django-admin startproject MyProject <Director> #Create DjangoTemplate
```

### 2.1.4. ✅️ apt

```shell
sudo apt install python3-PackageName #نصب بسته در محدوده سیستمی و نه یک پروژه یعنی همه جای سیستم عامل دسترس خواهد بود
```

### 2.1.5. ✅️ pipdeptree

```shell
pipdeptree | nl #نمایش وابستگی‌ها در فرمت فایل نیازمندی‌ها
```

## 2.2. 🅱️ VirtualEnvironment

* محیط مجازی (Virtual Environment): امکان ایجاد فضا مستقل و جداگانه پروژه‌ها از هم(جلوگیری از تداخل) در وابستگی‌های نصب
  بسته‌ها و کتابخانه‌ها را فراهم می‌آورد
* هر پروژه می‌تواند نسخه‌های خاص خود از کتابخانه‌ها را داشته باشد بدون اینکه بر روی پروژه‌های دیگر تأثیر بگذارد.
* نکته: در محیط venv نیاز به زدن دستور `python3 -m pip install requests` نیست و تنها نوشتن `pip install` کار میکند
* حتما باید بسته virtualenv در سیستم نصب باشد تا بتوانین مجیط مجازی virtualEnvironment بوجود بیاورید(یعنی در خروجی دستور
  `pip freeze` این بسته موجود باشد)

### 2.2.1. ✅️ Different (virtualenv, venv)

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

## 2.3. 🅱️ Persian Tools

* برای استفاده از کاراکترهای «یونیکد فارسی» یا هر زبانی در سورس کدهای پایتون، باید از این هدر در بالای کد استفاده شود
    * `-*- coding: utf-8 -*-`
    * در این حالت مفسر کد را به صورت یونی کد می‌خواند و می تواند فارسی در آن بنویسید
* برای اینکه تمام رشته‌های STR در پایتون به صورت UNICODE تعریف شوند باید در ابتدای فایل این کلاس را ایمپورت کنیم

```python
from __future__ import unicode_literals
```

# 3. 🅰️ Basic Syntax

## 3.1. 🅱️ Variables

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

## 3.2. 🅱️ if

```python
# Example1️⃣️: 
userRank = 1
print("you got GOLD medal") if userRank == 1 else print("no medal")
```

### 3.2.1. ✅️ TernaryOperator(اپراتورهای‌سه‌گانه)

* در برخی زبان‌های برنامه‌نویسی هستند
* به شما امکان میدهد که یک بلوک را ساده نمایید

```python
# syntax: [value_if_true] if [condition] else [value_if_false]
## value_if_true: مقداری که اگر شرط True باشد باید برگردانده شود
## value_if_false: مقداری که اگر شرط False باشد باید برگردانده شود
## condition: شرط
```

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

# Example7️⃣️:
score = 85
grade = (
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
)
print(grade)  # B
```

## 3.3. 🅱️ for

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
[print(x) for x in [1, 2, 3, 4]]
# 1
# 2
# 3
# 4
# [None, None, None, None]


# Example4️⃣️: 
for num in range(1, 10):
    if num % 2 == 1:
        for star in range(1, 6):  # [1, 2, 3, 4, 5]
            print("*" * star)
    else:
        for star in range(5, 0, -1):  # [5, 4, 3, 2, 1]
            print("*" * star)

# Example5️⃣️:
print([num % 2 == 0 for num in [1, 2, 3, 4, 5]])  # Output: [False, True, False, True, False]

# Example6️⃣️:

# Example7️⃣️: 
```

## 3.4. 🅱️ while

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

## 3.5. 🅱️ Operation

### 3.5.1. ✅️ Operators Comparison

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

### 3.5.2. ✅️ Logical Operand

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

# 4. 🅰️ exception

## 4.1. 🅱️ Error

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

## 4.2. 🅱️ Error-Raise

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

## 4.3. 🅱️ Debug(pdb)

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

# 5. 🅰️ Function

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

## 5.1. 🅱️ Lambda

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

## 5.2. 🅱️ Agmuments

* اگر در هنگام تعریف بدنه یک تابع همه موارد parameters و args و defaultParameters و kwargs داشته باشیم ترتیب اولویت به
  شکل زیر است
    * 1️⃣️ `Positional Parameters` پارامترهای عادی
    * 2️⃣️ `*args` یعنی متغیرهای نام‌گذاری‌نشده
        * ◄ متغیرها ازنوع Tuple و غیرقابل تغییرخواهدبود(Immutable یا غیرقابل تغییر)
    * 3️⃣️ `default parameters` یعنی تعیین مقدار پیش‌فرض برای متغیر
        * اگر درهنگام فراخوانی تابع مقدار متغیر تعیین نشود آنگاه مقدارپیش‌فرض بعنوان مقدار متغیر لحاظ می‌گردد
    * 4️⃣️ `**kwargs` یعنی Dictionary ◄ متغیر دارای محتوی کلید و مقدار است
* توجه: ترتیب *args قبل از default و **kwargs الزامی است.

### 5.2.1. ✅️ PositionalParameters

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

### 5.2.2. ✅️ `*args`

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

### 5.2.3. ✅️ DefaultParameters

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

### 5.2.4. ✅️ `**kwargs`

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

### 5.2.5. ✅️ Combine

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

## 5.3. 🅱️ Function as Object

* توابع در پایتون شیء هستند
* توابع در پایتون می‌توانند
    * همانند متغیرها منتقل شوند
    * به یک متغیر نسبت‌داده‌شوند
    * به تابع دیگر داده شوند
    * داخل لیست و دیکشنری و موارد مشابه ذخیره شوند

مثال:

```python
def greet():
    return "Hello!"


func = greet  # تابع رو به یک متغیر نسبت دادیم
print(func())  # Hello!
```

## 5.4. 🅱️ Higher-Order Functions

* یک تابع مرتبه‌بالا(Higher-Order Function) به تابعی گفته می‌شه که: یکی از موارد زیر باشد
    * 1️⃣️یک تابع دیگر را به عنوان ورودی بگیرد،
    * 2️⃣️ یک تابع را به عنوان خروجی برگرداند.
* پیش‌نیاز این موضوع آن است که توابع در پایتون شیء باشند

```python
def greet():
    return "Hello!"


def caller(func):
    return func()


caller(greet)  # "Hello!"
```

### 5.4.1. 1️⃣️ Function as input

* تابعی که تابع دیگری را به عنوان ورودی می‌گیرد
* Example: map(), filter(), sorted(), sum()

```python
# Example1️⃣️: map(func, iterable)
def square(x):
    return x ** 2


numbers = [1, 2, 3, 4]
squared = list(map(square, numbers))
print(squared)  # [1, 4, 9, 16]


# Example2️⃣️: filter(func, iterable)
def is_even(x):
    return x % 2 == 0


evens = list(filter(is_even, numbers))
print(evens)  # [2, 4]

# Example3️⃣️: sorted(iterable, key=func)
words = ['banana', 'kiwi', 'apple']
sorted_by_len = sorted(words, key=len)
print(sorted_by_len)  # ['kiwi', 'apple', 'banana']

# Example4️⃣️: 
from functools import reduce


def add(x, y):
    return x + y


numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)
print(total)  # Output: 15

# Example5️⃣️:
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(squared)  # [1, 4, 9, 16, 25]
print(evens)  # [2, 4]

```

### 5.4.2. 2️⃣️ Function return Function

* این نوع معمولاً در دکوراتورها یا ** Closureها** دیده می‌شه.
* مثال: تابعی که یک تابع جدید بسازد

```python
# Example1️⃣️:  
def make_multiplier(n):
    def multiplier(x):
        return x * n

    return multiplier  # تابع را برمی‌گرداند!


double = make_multiplier(2)
triple = make_multiplier(3)

# نکته: make_multiplier یک تابع مرتبه بالا است چون یک تابع (multiplier) را برمی‌گرداند.
print(double(5))  # 10
print(triple(5))  # 15
```

### 5.4.3. 3️⃣️ Combine

```python
def add_logger(func):
    def wrapper(x):
        print(f"Calling function with input: {x}")
        result = func(x)
        print(f"Result: {result}")
        return result

    return wrapper  # تابع جدید را برمی‌گرداند


def square(x):
    return x ** 2


logged_square = add_logger(square)
logged_square(4)

# Output: Calling function with input: 4
########: Result: 16
```

## 5.5. 🅱️ Function Inside Function

توابع می‌توانند در داخل تابع دیگر تعریف شوند (توابع تو در تو)

```python
# Example1️⃣️: 
def outer():
    def inner():
        print("Inside inner")

    return inner


# Example2️⃣️: return value
from random import choice


def state():
    def get_state():
        msg = choice(('Good', 'Bad!', 'Fine'))
        return msg

    return get_state()  # 📌️ به علامت پرانتز باز و بسته توجه شود


print(state())

# Example3️⃣️: Return func
from random import choice


def state():
    def get_state():
        msg = choice(('Good', 'Bad!', 'Fine'))
        return msg

    return get_state  # 📌️ به عدم وجود پرانتز باز و بسته توجه شود


result = state()
print(result())


# Example4️⃣️: with Args
def func1_square(number):
    return number * number


def func2_sum(number, func):
    total = 0
    for num in range(1, number + 1):
        total += func(num)
    return total


print(func2_sum(5, func1_square))  # Output: 55
```

## 5.6. 🅱️ Decorator

دِکوراتور یک تابع است که یک تابع دیگر را می‌گیرد، رفتار آن را تغییر می‌دهد و یک تابع جدید را برمی‌گرداند

```python
my_function = decorator(my_function)


# معادل است با
@decorator
def my_function():
    pass
```

* بادرک صحیح از سه مفهوم زیر مبحث Decorator درک خواهد شد
    * Function as Object
    * High-Order Functions
    * Function inside functions
* تکنیک Decorator یک DesignePattern است که یک تابع را درون تابع دیگر فراخوانی میکنیم
* امکان تغییر یا گسترش رفتار یک تابع یا کلاس بدون تغییر در کد اصلی آن
* یک تابع دیگر را بعنوان آرگومان ورودی می‌پذیرند و یک تابع جدید را برمی‌گردانند
* این تابع جدید می‌تواند قبل یا بعد از اجرای تابع اصلی، کارهای اضافی انجام دهد
* معمولا همراه با کاراکتر @ در بالای توابع ظاهر می‌شوند

ساختار کلی یک دکوراتور به شکل زیراست. همچنین `*args, **kwargs` باعث می‌شود تا دکوراتور با هر تابعی(فارغ از تعداد آرگومان ورودی) کار کند

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # کار قبل از اجرای تابع (مثلاً لاگ، زمان، اجازه دسترسی)
        result = func(*args, **kwargs)  # اجرای تابع اصلی
        # کار بعد از اجرای تابع (مثلاً پاک‌کردن، چک نتیجه)
        return result

    return wrapper
```

| دکوراتور          | کاربرد                                  |
|-------------------|-----------------------------------------|
| `@timer`          | اندازه‌گیری زمان اجرا                   |
| `@debug`          | لاگ کردن فراخوانی توابع                 |
| `@cache`          | ذخیره نتایج برای جلوگیری از محاسبه مجدد |
| `@login_required` | بررسی اینکه کاربر وارد شده باشد (در وب) |
| `@retry`          | اجرای مجدد تابع در صورت خطا             |
| `@property`       | تبدیل متد به ویژگی (در کلاس‌ها)         |

### 5.6.1. ✅️ Custom

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

### 5.6.2. ✅️ `@timer`

اگر بخواهیم قبل و بعد از اجرای تابع، زمان رو چک کنه

```python
import time


def timer(function_job):
    def wrapper():
        start = time.time()
        function_job()  # اجرای تابع اصلی
        end = time.time()
        print(f"Time taken: {end - start:.2f} seconds")

    return wrapper


# نحوه استفاده
@timer
def behrooz():
    time.sleep(2)  # عملیات دلخواه که میخواهیم مقدار زمان آن را اندازه گیری کنیم
    print("Job Done!")


behrooz()

# Output: 
### Job Done!!
### Time taken: 2.00 seconds
```

توضیحات

* تابع behrooz به عنوان ورودی به timer داده شد.
* timer یک تابع جدید (wrapper) ساخت و برگرداند.
* حالا behrooz دیگه تابع اصلی نیست، بلکه تابع پیچ‌شده (wrapped) است که قبل و بعدش کار اضافه انجام می‌ده.

```python
@timer
def behrooz():
    ...


# قطعه کد بالا در پایتون معادل زیر تلقی می‌شود
slow_function = timer(behrooz)
```

### 5.6.3. ✅️ `@debug`

```python
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function:{func.__name__}, args:{args}, kwargs:{kwargs}")
        result = func(*args, **kwargs)
        print(f"function:{func.__name__}, returned:{result}")
        return result

    return wrapper


@debug
def add(a, b):
    return a + b


add(3, 5)
# Output:
## Calling function:add, args:(3, 5), kwargs:{}
## function:add ,returned:8
## 8
```

### 5.6.4. ✅️ `@wraps`

* وقتی از یک دکوراتور استفاده می‌کنیم، در واقع تابع اصلی رو با یک تابع جدید (معمولاً wrapper) جایگزین می‌کنیم.
* اما مشکل جایگزینی این است که اطلاعات متاداده تابع اصلی (مثل نام، توضیحات، مستندات) از بین می‌رود و به جای آن اطلاعات تابع wrapper نمایش داده می‌شود
    * `__name__`
    * `__doc__`
    * `__module__`
* ذیل ماژول functools می‌باشد

```python
# Example1️⃣️: Without @wraps
def my_decorator(func):
    def wrapper():
        return func()

    return wrapper


@my_decorator
def hello():
    """Says hello"""
    print("Hello!")


print(hello.__name__)  # Output: wrapper ← اشتباه!
print(hello.__doc__)  # Output: None ← اشتباه!

# Example1️⃣️: with @wraps
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper():
        return func()

    return wrapper


@my_decorator
def hello():
    """Says hello"""
    print("Hello!")


print(hello.__name__)  # Output: hello ✅
print(hello.__doc__)  # Output: Says hello ✅
```

### 5.6.5. ✅️ `@lru_cache`

* ذخیره نتایج برای جلوگیری از محاسبه مجدد
* در پایتون از نسخه 3.9 به بعد، یک دکوراتور جدید به نام @cache به ماژول functools اضافه شد که نسخه ساده‌شده و پیش‌فرض از @lru_cache است.
    * پس دکوریتور `@cache` در نسخه های بالاتر از 3.9 معادل است با `@lru_cache(maxsize=None)`
* در موارد زیر می‌توان از cache استفاده کرد
    * فقط وابسته به ورودی‌هاست (pure function): توابعی که ورودی یکسان، همیشه خروجی یکسان دارند
    * ورودی و خروجی به زمان و گزاره‌های تصادفی و متغیرهای سراسری وابسته نباشد
        * وگرنه زمان را کش میکند و هربار یک زمان را نشان میدهد
        * وگرنه عدد رندم را کش میکند و هربار یک عدد رندم ثابت را نمایش میدهد
    * محاسبات تکراری دارد
    * ورودی‌های تکراری زیادی دارد
    * زمان اجرا زیاد است
* مثال
    * توابع بازگشتی (فیبوناچی، فاکتوریل)
    * پردازش داده‌های تکراری
    * APIهای شبیه‌سازی‌شده
* اگر پایتونت قدیمی‌تر از 3.9 است، از @lru_cache(maxsize=None) استفاده کن.
* اگر 3.9+ داری، @cache انتخاب تمیزتر و مدرن‌تریه

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    print(f"Calculating fibonacci({n})...")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# اولین بار: محاسبه می‌شه
print(fibonacci(5))
# خروجی:
# Calculating fibonacci(5)...
# Calculating fibonacci(4)...
# Calculating fibonacci(3)...
# Calculating fibonacci(2)...
# Calculating fibonacci(1)...
# Calculating fibonacci(0)...
# 5

# دومین بار: از کش استفاده می‌شه — هیچ پیامی چاپ نمی‌شه!
print(fibonacci(5))  # 5 ← بدون محاسبه دوباره
```

* بدون کش، fibonacci(35) ممکنه چند ثانیه طول بکشه. با کش، لحظه‌ای اجرا می‌شه.

### 5.6.6. ✅️ `@cache`

```python
# Example1️⃣️: فرض کنیم یک تابع کند داریم که جمع اعداد تا n رو حساب می‌کنه 
from functools import cache


@cache
def slow_sum(n):
    print(f"process sum until {n}...")
    total = 0
    for i in range(n):
        total += i
    return total


# try1: process
print(slow_sum(10))  # Output: process sum until 10... \n 45

# try2: From Cache
print(slow_sum(10))  # Output: 45 (بدون محاسبه مجدد)

# Example2️⃣️: محاسبه فاکتوریل (بازگشتی)
from functools import cache


@cache
def factorial(n):
    print(f"processing factorial({n})")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# try1: process
print(factorial(5))
# Output:
# ------> processing factorial(5)
# ------> processing factorial(4)
# ------> processing factorial(3)
# ------> processing factorial(2)
# ------> processing factorial(1)
# ------> 120 

# try2: From Cache
print(factorial(5))
# Output:
# ------> processing factorial(5)
# ------> 120

```

### 5.6.7. ✅️ `@retry`

* اجرای مجدد تابع در صورت خطا
* اگر تابعی به دلیل خطا (مثلاً شبکه قطع شد) شکست خورد، چند بار دوباره امتحان کن.

```python
import time
import random


def retry(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"تلاش {attempt + 1} شکست خورد: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay)  # کمی صبر کن
                    else:
                        print("همه تلاش‌ها شکست خورد.")
                        raise

        return wrapper

    return decorator


@retry(max_attempts=3, delay=0.5)
def unstable_function():
    if random.random() < 0.7:  # 70% احتمال خطا
        raise ConnectionError("اتصال شبکه قطع شد!")
    print("عملیات با موفقیت انجام شد.")
    return True


# اجرا
unstable_function()
# Output: 
##### تلاش 1 شکست خورد: اتصال شبکه قطع شد!
##### تلاش 2 شکست خورد: اتصال شبکه قطع شد!
##### عملیات با موفقیت انجام شد.
```

### 5.6.8. ✅️ `@login_required`

* قبل از اجرای یک تابع (مثل دسترسی به پروفایل)، بررسی کن که کاربر وارد شده (logged in) باشد.
* این دکوراتور معمولاً در فریم‌ورک‌هایی مثل Flask یا Django وجود داره. اینجا یک نسخه ساده‌شده می‌زنیم.

```python
def login_required(func):
    def wrapper(*args, **kwargs):
        # فرض می‌کنیم کاربر وارد شده یا نه
        is_logged_in = True  # فرض کن کاربر وارد شده
        if not is_logged_in:
            print("AccessDenied! Please login")
            return None
        return func(*args, **kwargs)

    return wrapper


@login_required
def view_profile():
    print("profile is loading")


view_profile()
# Output: profile is loading ------------------> if `is_logged_in = True`
# Output: AccessDenied! Please login ----------> if `is_logged_in = False`

```

### 5.6.9. ✅️ `@property`

* property: تبدیل تابع به ویزگی(property) یا صفت(attribute)
* برای دسترسی به متد باید حتما پرانتز باز و بسته گذاشته بشود ولی برای حالت property نباید پرانتز گذاشت

```python
# Example1️⃣️: 
class Behrooz:
    def __init__(self, name, family):  # Constructor
        self.name = name
        self.family = family

    @property
    def fullname(self):
        return f"{self.name} {self.family}"

    def show_fullname(self):
        return f"{self.name} {self.family}"


obj1 = Behrooz("behrooz", "MohamadiNasab")
print(obj1.show_fullname())  # --> Output: behrooz MohamadiNasab  
print(obj1.fullname)  # ---------> Output: behrooz MohamadiNasab


# Example2️⃣️: 
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @property
    def age(self):
        from datetime import datetime
        return datetime.now().year - self.birth_year


p = Person("Ali", 1990)
print(p.age)  # Output: مثلاً 34
```

### 5.6.10. ✅️ PropertyGetterSetter

* getter: یک تابع که برای استفاده می‌بایست همراه پرانتز باشد ولی هنگامیکه با `@property` آمده‌باشد نیاز به استفاده از پرانتز نیست

```python
class behrooz:
    def __init__(self, _name, _family, _age):  # Constructor
        self.name = _name
        self.family = _family
        self.age = _age

    @property
    def age(self):  # تبدیل یک تابع به یک پراپرتی و نه متد
        return self._age

    @property
    def fullName(self):  # تبدیل یک تابع به یک پراپرتی و نه متد
        return f"{self.name} {self.family}"

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            self._age = 0


obj1 = behrooz("behrooz", "MohamadiNasab", -18)
print(obj1.age)

obj1.age = 40
print(obj1.age)

obj1.age = -15
print(obj1.age)

obj1.age = 18
print(obj1.age)
print(obj1.fullName)
```

### 5.6.11. ✅️ ClassMethod

* تغییر عملکرد یک تابع بطوریکه به‌جای استفاده از منابع نمونه از منابع کلاس استفاده می‌کند
* دسترسی مستقیم به دیتای کلاس بدون ساخت شیء نمونه

```python
class User:
    activeUsers = 0

    @classmethod
    def func1(cls):
        return cls.activeUsers


# Method1️⃣️: بدون نیاز ساخت شیء از کلاس
print(User.func1())

# Method2️⃣️: الزام بر ساختن شیء از کلاس"

obj1 = User()
print(obj1.func1())

```

### 5.6.12. ✅️ Comprehensive Advance Examples

```python
def before_after(func):
    def wrapper():
        print(f"Before={0}")
        func()
        print(f"After={1}")

    return wrapper


# Example1️⃣️: Legacy❗️ Return function
def say_hello():
    print("hello")


tempFunc = before_after(say_hello)
tempFunc()


# Output:
## -----> Before=0
## -----> hello
## -----> After=1

# Example2️⃣️: Zero args
@before_after
def say_hello():
    print("hello")


say_hello()


# Output:
## -----> Before=0
## -----> hello
## -----> After=1

# Example3️⃣️: 1 args
def one_arg_before_after(func):
    def wrapper(x):
        print(f"Before={x - 1}")
        func(x)
        print(f"After={x + 1}")

    return wrapper


@one_arg_before_after
def say_hello(x):
    print(f"hi {x}")
    print(f"hi")


say_hello(256)


# Output: 
## ------> Before=255
## ------> hi 256
## ------> hi
## ------> After=257


# Example4️⃣️: 2 Args
def two_args_before_after(func):
    def wrapper(arg1, arg2):
        print(f"Before:[arg1:{arg1}] - [arg2:{arg2}]")
        func(arg1, arg2)
        print(f"After:[arg1:{arg1}] - [arg2:{arg2}]")

    return wrapper


@two_args_before_after
def show_name(name, family):
    print(f"{name} {family}")


show_name('behrooz', 'Mohamadinasab')


# Output:
## -----> Before:[arg1:behrooz] - [arg2:Mohamadinasab]
## -----> behrooz Mohamadinasab
## -----> After:[arg1:behrooz] - [arg2:Mohamadinasab]


# Example5️⃣️: *Arg
def many_args_before_after(func):
    def wrapper(*args):
        print(f"Before [{args}]")
        func(args)
        print(f"After [{args}]")

    return wrapper


@many_args_before_after
def show_data(*args):
    print(f"*args: {args}")


show_data('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address')
# Output:
## -----> Before [('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address')]
## -----> *args: (('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address'),)
## -----> After [('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address')]

show_data('Behrooz', 'male')


# Output:
## -----> Before [('Behrooz', 'male')]
## -----> *args: (('Behrooz', 'male'),)
## -----> After [('Behrooz', 'male')]


# Example6️⃣️: *Arg and **kwargs
def exec_before_after(func):
    def wrapper(*args, **kwargs):
        print(f"Before[args:{args}]")
        func(*args, **kwargs)
        print(f"After[kwargs:{kwargs}]")

    return wrapper


@exec_before_after
def show_data(*args, **kwargs):
    print(f"{args} - {kwargs}")


show_data('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address', Fname="Behi", Lname="Mohamadi")
# Output:
## -----> Before[args:('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address')]
## -----> ('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address') - {'Fname': 'Behi', 'Lname': 'Mohamadi'}
## -----> After[kwargs:{'Fname': 'Behi', 'Lname': 'Mohamadi'}]

show_data('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address', Fname="Behi")
# Output:
## -----> Before[args:('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address')]
## -----> ('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address') - {'Fname': 'Behi'}
## -----> After[kwargs:{'Fname': 'Behi'}]


show_data('Behrooz', 'MohamadiNasab', 'phone')
# Output:
## -----> Before[args:('Behrooz', 'MohamadiNasab', 'phone')]
## -----> ('Behrooz', 'MohamadiNasab', 'phone') - {}
## -----> After[kwargs:{}]


show_data(Fname="Behi", Lname="Mohamadi")
# Output:
## -----> Before[args:()]
## -----> () - {'Fname': 'Behi', 'Lname': 'Mohamadi'}
## -----> After[kwargs:{'Fname': 'Behi', 'Lname': 'Mohamadi'}]


show_data('male')
# Output:
## -----> Before[args:('male',)]
## -----> ('male',) - {}
## -----> After[kwargs:{}]


show_data(Fname="Behi")
# Output:
## -----> Before[args:()]
## -----> () - {'Fname': 'Behi'}
## -----> After[kwargs:{'Fname': 'Behi'}]
```

# 6. 🅰️ Iterate

* Iterate(فعل پیمایش): فرآیند «چرخیدن روی عناصر یک مجموعه» گفته می‌شود
    * Iterate کردن یعنی پیمایش یک مجموعه داده، عنصر به عنصر.
    * کاربردهای iterate:
        * حلقه‌های for
        * تابع‌هایی که روی داده پیمایش می‌کنند: sum(), list(), tuple(), max(), min()
        * توابع map(), filter(), zip()
        * ساختارهای داده‌ای جدید از روی داده‌های موجود
        * پردازش فایل‌ها خط به خط
* Iterable(Object): `__iter__()`
    * شیء‌ای که می‌توان روی آن حلقه زد مثل : List,Tuple,String,Dictionary,Set,Range,File,...
    * هر شیء پایتونی که دارای متد `__iter__()` باشد، یک iterable است
    * هر شیء Iterable را می‌توان توسط مکانیزم Iterator پیمایش کرد
    * هر شیء iterable را می‌توان با `for` یا توابعی مثل `iter()` و `next()` پیمایش(iterate) کرد.
    * موضوع توالی و پشت سر هم بودن، جزء مهمترین مولفه در این ساختار است
    * به صورت عادی نمی‌توان روی یک iterableObjects عمل iterate انجام داد. ابتدا باید تبدیل کنیم به iterator و سپس آن را پیمایش یا iterate کنیم
    * یک iterableObject به صورت پیش‌فرض iterator نیست بلکه باید توسط افزودن توابع تظیر `__next__()` به آن قابلیت مکانیزم Iterator را اضافه کنیم
* Iterator(Object): `__iter__()` و `__next__()`
    * شیء‌ای که وضعیت پیمایش را نگه می‌دارد و می‌توان با `next()` عنصر بعدی را بگیرد.
    * شیئی که دارای `__iter__()` و `__next__()` است.
        * `__iter__()` سبب افزودن  `obj.iter()` می‌شود
        * `__next__()`  سبب افزودن  `obj.next()` می‌شود
    * پایتون از مکانیسم ایتریتور (iterator) برای پیمایش استفاده می‌کند.
        * وقتی یک for روی یک iterable اجرا می‌شود، پایتون متد `__iter__()` را فراخوانی می‌کند تا یک ایتریتور ایجاد شود.
        * سپس متد `__next__()` فراخوانی می‌شود تا هر بار عنصر بعدی را بگیرد.
        * وقتی عناصر تمام شوند، Exception با نام StopIteration رخ می‌دهد و حلقه پایان می‌یابد.
    * an object that can iterate on items by itself, and It can sequentially access the elements of an iterable
    * `iterator=iterableObjects.iter()`

```python
lst = [1, 2, 3]  # lst: iterable
it = iter(lst)  # it: iterator

# Example1️⃣️: لیست را پیمایش می‌کند. یعنی هر عنصر را یکی یکی برمی‌دارد و پردازش می‌کند
for item in [1, 2, 3, 4]:
    print(item)

# Example2️⃣️: پیمایش روی رشته
for char in "hello":
    print(char)

# Example3️⃣️: پیمایش روی دیکشنری (کلیدها)
for key in {"a": 1, "b": 2}:
    print(key)

# Example4️⃣️: manual iterate یا پیمایش دستی ----> iter() + next()
data = "abc"
it = iter(data)

while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break
# Output: 
## -----> a
## -----> b
## -----> c

# Example5️⃣️: پیمایش فایل
with open("file.txt") as f:
    for line in f:  # iterate روی خطوط فایل
        print(line.strip())

# Example6️⃣️: Tuple
tup = (10, 20, 30)  # iterable
it = iter(tup)  # تبدیل به iterator

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# print(next(it))  # StopIteration (خطا — عناصر تمام شده‌اند)

# Example7️⃣️: String
text = "abc"  # iterable
it = iter(text)  # iterator

print(next(it))  # 'a'
print(next(it))  # 'b'
print(next(it))  # 'c'

# Example8️⃣️: Set --> عناصر «سِت» مرتب نیستند، بنابراین ترتیب خروجی ممکن است در اجراهای مختلف متفاوت باشد
s = {5, 10, 15}  # iterable (ترتیب تضمین نشده)
it = iter(s)

print(next(it))  # مثلاً 10
print(next(it))  # مثلاً 5
print(next(it))  # مثلاً 15

# Example9️⃣️: Dictionary
d = {'x': 1, 'y': 2, 'z': 3}  # iterable — به طور پیش‌فرض روی کلیدها پیمایش می‌شود
it = iter(d)

print(next(it))  # 'x'
print(next(it))  # 'y'
print(next(it))  # 'z'

# Example1️⃣️0️⃣️: pair
it_keys = iter(d.keys())  # کلیدها
it_values = iter(d.values())  # مقادیر
it_items = iter(d.items())  # جفت‌های (کلید، مقدار)

print(next(it_items))  # ('x', 1)

# Example1️⃣️1️⃣️: range
r = range(1, 4)  # iterable: 1, 2, 3
it = iter(r)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

# Example1️⃣️2️⃣️: File: sample.txt
file = open("sample.txt", "r")
it = iter(file)

print(next(it).strip())  # "Line 1"
print(next(it).strip())  # "Line 2"
print(next(it).strip())  # "Line 3"

file.close()


# Example1️⃣️3️⃣️: generator
def my_gen():
    yield 1
    yield 2
    yield 3


g = my_gen()  # generator object (هم iterable و هم iterator)
it = iter(g)  # ایجاد iterator (هرچند خودش از قبل iterator است)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

# Example1️⃣️4️⃣️:  لیست ترکیبی (انواع داده مختلف) 
mixed = [100, "hello", True, 3.14]
it = iter(mixed)

print(next(it))  # 100
print(next(it))  # "hello"
print(next(it))  # True
print(next(it))  # 3.14


# Example1️⃣️5️⃣️: Custom
class CountUp:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        value = self.start
        self.start += 1
        return value


# استفاده:
counter = CountUp(1, 4)
it = iter(counter)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # StopIteration

# Example1️⃣️6️⃣️: رزرو برای بعدی
```

## 6.1. 🅱️ Dictionary `{key1:value1}`

```python
# syntax: { key1: value1, key2: value2 }
```

* پایتون فقط اجازه می‌ده اشیاء غیرقابل تغییر (immutable) رو به عنوان کلید دیکشنری استفاده کنی.
    * Immutable(غیرقابل‌تغییر)
        * str → "hello"
        * int → 100
        * float → 3.14
        * tuple → (1, 2)
        * bool → True
        * frozenset → نوع خاصی از مجموعه که تغییرناپذیره
    * mutable(تغییرپذیر)
        * list → [1, 2]
            * سعی کنی یک لیست رو به عنوان کلید استفاده کنی، خطای `TypeError: unhashable type: 'list'` می‌ده
            * اگر لیست می‌تونست کلید باشه، بعد از تغییرش(چون تغییر پذیره)، دیکشنری نمی‌دونست کجا بره و کلید گم می‌شد
        * dict → {"a": 1}
        * set → {1, 2}

```python
dic1 = {"name": "Behrooz", "family": "Mohammadi Nasab", "age": 34}
dic2 = dict(first=1, second=2, third=3)  # {'first': 1, 'second': 2, 'third': 3}
dic3 = {}  # {}
dic4 = {num: num for num in [1, 2, 3, 4, 5]}  # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
dic5 = {key: value ** 2 for key, value in dic4.items()}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
dic6 = {num: ("even" if num % 2 == 0 else "odd") for num in [1, 2, 3, 4, 5]}  # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
dic7 = {num: num ** num for num in [1, 2, 3, 4, 5]}  # {1: 1, 2: 4, 3: 27, 4: 256, 5: 3125}

# Example1️⃣️: 
dic1 = {"name": "Behrooz", "family": "Mohammadi Nasab", "age": 34}
print(dic1["family"])  # Output: Mohammadi Nasab

# Example2️⃣️: .values()
print(dic1.values())  # Output: dict_values(['Behrooz', 'Mohammadi Nasab', 34])
for value in dic1.values():
    print(value)
# Output:
## -----> Behrooz
## -----> Mohammadi Nasab  
## -----> 34 

# Example3️⃣️: .keys()
print(dic1.keys())  # Output: dict_keys(['name', 'family', 'age'])

# Example4️⃣️: .get(key)
print(dic1.get("name"))  # output: Behrooz
print(dic1.get("age"))  # output: 34

# Example5️⃣️:
for key, value in dic1.items():
    print(f"{key}: {value}")
# Output:
## -----> name: Behrooz
## -----> family: Mohammadi Nasab
## -----> age: 34

# Example6️⃣️:
x = "name"
if x in dic1:
    print(dic1[x])
else:
    print(f"there is no {x} key in me")

# Example7️⃣️: .clear()
dic1.clear()  # dic1 is cleared

# Example8️⃣️: copy()
dic1 = {num: num for num in [1, 2, 3, 4, 5]}  # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
dic2 = dic1.copy()
print(dic2)  # Output: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

# Example9️⃣️: .pop(key) کلید و مقدار را باهم پاک میکند
dic1 = {'first': 1, 'second': 2, 'third': 3}  # {'first': 1, 'second': 2, 'third': 3}
dic1.pop("second")
print(dic1)  # Output: {'first': 1, 'third': 3}

# Example1️⃣️0️⃣️: .popitem() حذف آخرین آیتم از دیکشنری
dic1 = {'first': 1, 'second': 2, 'third': 3}  # {'first': 1, 'second': 2, 'third': 3}
dic1.popitem()
print(dic1)  # Output: {'first': 1, 'second': 2}

# Example1️⃣️1️⃣️: .update(dictionary) دیکشنری را به دیکنشری موجود می‌افراید
dic1 = {"name": "Behrooz", "family": "Mohammadi Nasab", "age": 34}
dic2 = dict(first=1, second=2, third=3)  # {'first': 1, 'second': 2, 'third': 3}
dic1.update(dic2)
print(dic1)  # Output: {'name': 'Behrooz', 'family': 'Mohammadi Nasab', 'age': 34, 'first': 1, 'second': 2, 'third': 3}

# Example1️⃣️2️⃣️: RaedOnly DICTIONARY by types.MappingProxyType
from types import MappingProxyType

d = {'a': 1, 'b': 2}
readonly = MappingProxyType(d)

print(readonly['a'])  # 1
# readonly['a'] = 3 # ❌️ TypeError: cannot be modified

# Example1️⃣️3️⃣️: nested dictionaries
data = {
    'user': {
        'profile': {
            'name': 'Ali'
        }
    }
}
name = data['user']['profile']['name']  # ❗️ توصیه نمی‌شود
name = data.get('user', {}).get('profile', {}).get('name', 'Unknown')  # ✅️ توصیه می‌شود
print(name)  # Ali

# Example1️⃣️4️⃣️: convert Dictionary to Object
from types import SimpleNamespace

config = SimpleNamespace(
    host="localhost",
    port=8000,
    debug=True
)

print(config.host)  # Output: localhost

# Example1️⃣️5️⃣️: Convert Dictionary to namespace
from types import SimpleNamespace

d = {'name': 'Ali', 'age': 25}
ns = SimpleNamespace(**d)
print(ns.name)  # Ali

# Example1️⃣️6️⃣️: ادغام دیکشنری با `|` و `|=` (پایتون ۳.۹+)
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

merged = d1 | d2
print(merged)  # {'a': 1, 'b': 3, 'c': 4} — b از d2 جایگزین شد

d1 |= d2  # update in-place
print(d1)  # {'a': 1, 'b': 3, 'c': 4}

# Example1️⃣️7️⃣️: استفاده از تاپل به عنوان کلید
locations = {  # مختصات شهرها
    (35.7, 51.4): "Tehran",
    (30.3, 48.3): "Isfahan",
    (25.2, 51.5): "Shiraz"
}

print(locations[(35.7, 51.4)])  # خروجی: Tehran

```

اگر از کلاس dict ارث بری نماییم و تابع `__missing__` تعریف شده باشد آنگاه اگر کلیدی یافت نشد آنگاه تابع فراخوانی می‌شود

```python
class DefaultDict(dict):
    def __missing__(self, key):
        return f"Key '{key}' not found, but I'm helping!"


d = DefaultDict()
print(d['name'])  # Key 'name' not found, but I'm helping!
```

## 6.2. 🅱️ Set `{}`

* NoRepeat(uniq): مجموعه‌ای که محتوی آن بدون شک تکراری نخواهند شد
* در آن مرتب سازی معنی ندارد
* در آن اندیس جایگاه ندارد(اندیس ناپذیر)
* درآن قابلیت فراخوانی (Call) وجود ندارد
* از نسخه `۳.۷` به بعد ترتیب درج نگه‌داری می‌شود
* فقط اشیاء قابل هش (hashable) می‌تونن عضو set باشن.
    * قابل هش (hashable)
        * موارد int, str, tuple البته اگر اگر عناصرش قابل هش باشن
        * frozenset
        * bool
    * غیرقابل هش (unhashable)
        * list
        * dict
        * set
        * bytearray

```python
set1 = {3, 5, 't', 'z', 2, 7, 1, 1, 1, 5, 5, 5, 5}
set2 = {"ali", "milad", "mohammad", "sara"}
set3 = {"mohammad", "ahmad", "reza", "ali"}
set4 = {x ** 2 for x in range(20)}
set5 = {char for char in "Behrooz Mohammadi Nasab Sahzabi"}
set6 = set([1, 2, 2, 3])  # {1, 2, 3}
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Example1️⃣️: 
print(set1)  # {'z', 1, 2, 3, 5, 7, 't'}

# Example2️⃣️: .add(element)
set6.add(4)
set6.add(2)  # تاثیری نداره
print(set6)  # {1, 2, 3, 4}

# Example3️⃣️: .remove(element) عضو رو حذف می‌کنه. اگر وجود نداشته باشه، خطا می‌ده
set6.remove(4)
# s.remove(10) → ❌️ KeyError!

# Example4️⃣️: .discard(element) حذف میکند و اما اگر عضو وجود نداشته باشه، خطا نمی‌ده
set6.discard(10)  # OK، بدون خطا

# Example5️⃣️: .pop() یک عضو تصادفی رو حذف و برمی‌گردونه (چون set مرتب نیست).
item = set6.pop()  # حذف یک عضو به صورت تصادفی

# Example6️⃣️: .clear()
set6.clear()

# Example7️⃣️: `|` اجتماع union
A | B  # {1, 2, 3, 4, 5, 6} # معادل: A.union(B)
# حافظه کمتر ازlist(set(A + B))

# Example8️⃣️: `&` اشتراک Intersection
A & B  # {3, 4} # معادل: A.intersection(B)

# Example9️⃣️: `-` تفاضل Difference

A - B  # {1, 2}

# Example1️⃣️0️⃣️: `^` تفاضل‌متقارن SymmetricDifference
A ^ B  # {1, 2, 5, 6}

# Example1️⃣️1️⃣️: unhashable
s = set()
# s.add([1, 2]) → ❌ TypeError
s.add((1, 2))  # ✅ OK

# Example1️⃣️2️⃣️: تبدیل به حالت های متفاوت
list(set([1, 2, 2, 3]))  # [1, 2, 3] — حذف تکراری
set("hello")  # {'h', 'e', 'l', 'o'} — تکراری 'l' حذف شد
set(range(5))  # {0, 1, 2, 3, 4}

# Example1️⃣️3️⃣️: بررسی وجود مشترک بودن عناصر
if set(A) & set(B):
    print("حداقل یک عضو مشترک دارند")

# Example1️⃣️4️⃣️: پیدا کردن عناصر منحصر به فرد در دو لیست
print(set(A) - set(B))  # Output: {1, 2}
print(set(B) - set(A))  # Output: {5, 6}
```

اپراتورهای منطقی

| اپراتور | مفهوم             | مثال                        |
|---------|-------------------|-----------------------------|
| `==`    | برابری            | `{1,2} == {2,1}` → `True`   |
| `<`     | زیرمجموعه سره     | `{1} < {1,2}` → `True`      |
| `<=`    | زیرمجموعه         | `{1,2} <= {1,2}` → `True`   |
| `>`     | مجموعه سره بزرگتر | `{1,2,3} > {1,2}` → `True`  |
| `>=`    | شامل بودن         | `{1,2,3} >= {1,2}` → `True` |

### 6.2.1. ✅️ frozenset

نوعی مجموعه(set)است که غیرقابل تغییر (immutable) و فقط-خواندنی (read-only) است.

* set غیرقابل هش(unhashable)است. پس نمی‌تونه کلید دیکشنری باشه. اما frozenset قابل هش است پس می‌تونه کلید باشه
* frozenset غیرقابل تغییر است

```python
# Example1️⃣️: Create
fs = frozenset([1, 2, 3, 2])  # تکراری‌ها حذف می‌شن
print(fs)  # frozenset({1, 2, 3})

# Example2️⃣️: Create رشته
frozenset("hello")  # frozenset({'h', 'e', 'l', 'o'})

# Example3️⃣️: Create
s = {1, 2, 3}
fs = frozenset(s)

# Example4️⃣️(مهم): استفاده به عنوان کلید دیکشنری
d = {
    frozenset([1, 2]): "group A",
    frozenset([3, 4]): "group B"
}
print(d[frozenset([1, 2])])  # Output: group A
# d = {[1, 2]: "error"} # TypeError: unhashable type: 'list' - با ست امکان‌پذیر نیست
# d = {{1, 2}: "error"} # TypeError: unhashable type: 'set' - با ست امکان‌پذیر نیست

# Example5️⃣️:
A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])
print(A | B)  # frozenset({1, 2, 3, 4, 5}) → اجتماع
print(A & B)  # frozenset({3}) → اشتراک
print(A - B)  # frozenset({1, 2}) → تفاضل
print(A ^ B)  # frozenset({1, 2, 4, 5}) → تفاضل متقارن

# Example6️⃣️:
A = frozenset([1, 2])
B = frozenset([1, 2, 3])
print(A < B)  # True → A زیرمجموعه سره B است
print(A <= B)  # True

# Example7️⃣️: استفاده در setها (چون قابل هش است)
collection = {
    frozenset([1, 2]),
    frozenset([3, 4])
}
# می‌تونی frozenset رو عضو یک set کنی!

print(collection)  # {frozenset({1, 2}), frozenset({3, 4})}

# { {1, 2}, {3, 4} } # TypeError: unhashable type: 'set' - با ست امکان‌پذیر نیست

# Example8️⃣️: غیر قابل تغییر
fs = frozenset([1, 2])
# fs.add(3) → AttributeError
# fs.remove(1) → AttributeError
```

## 6.3. 🅱️ Tupple`()`

* تاپل (tuple) یک ساختار داده غیرقابل تغییر (immutable) و مرتب (ordered) در پایتون است
* ثبات داده بدلیل عدم تغییر
* استفاده به عنوان کلید در دیکشنری
* مناسب برای داده‌های ثابت مثل مکان، رنگ RGB و ...
* چون تاپل غیرقابل تغییره، فقط دو متد داره
    * `.count(item)`: شمارش تکرار
    * `.index(item)`: پیدا کردن اندیس اولین مقدار

```python
tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3  # بدون پرانتز هم می‌شه!
tuple3_empty = ()
tuple4 = (5,)  # تاپل یک عضوی حتماً کاما داشته باشه
tuple5_1to15 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
tuple6 = (1, 2, 2, 3, 4, 5, 2, (4, 5, 3), 3, 3)  # immutable list
tuple7 = (1, 2, {2}, (3, 4), [2, 5], 2, (4, 5, 3), 3, 3)
tuple8 = tuple([1, 2, 3, 4, 5])

# Example1️⃣️: ذخیره مختصات نقطه
point = (3, 4)
x, y = point
print(f"Point: ({x}, {y})")  # Point: (3, 4)


# Example2️⃣️: بازگشت چند مقدار از یک تابع
def divide_remainder(a, b):
    return a // b, a % b  # Output: بازگشت به صورت تاپل


quotient, remainder = divide_remainder(10, 3)
print(quotient, remainder)  # Output: 3 1

# Example3️⃣️:  استفاده به عنوان کلید در دیکشنری
scores = {  # ذخیره امتیاز تیم‌ها در یک تورنمنت
    ("Iran", "Spain"): (2, 1),
    ("Iran", "Portugal"): (1, 1),
    ("Spain", "Portugal"): (3, 3)
}

print(scores[("Iran", "Spain")])  # (2, 1)

# Example4️⃣️:  Color RGB (چون تغییر نمی‌کنه، تاپل انتخاب مناسبیه) 
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)
}

print(colors["red"])  # (255, 0, 0)

# Example5️⃣️: ذخیره تاریخ و زمان به صورت تاپل
event = ("Conference", (2024, 5, 15), "Tehran")
name, date, city = event
year, month, day = date

print(f"{name} in {city} on {year}-{month}-{day}")  # Output: Conference in Tehran on 2024-5-15

# Example6️⃣️: 
points = [(1, 2), (3, 4), (5, 6)]

for x, y in points:
    print(f"({x}, {y})")
# (1, 2)
# (3, 4)
# (5, 6)

# Example7️⃣️: تبدیل لیست به تاپل (برای حفظ ثبات)
my_list = [1, 2, 3]
my_tuple = tuple(my_list)


# my_tuple[0] = 99  → ❌️ TypeError عدم امکان تغییر 

# Example8️⃣️: استفاده در تابع با `*args`
def print_names(*names):
    # names یک تاپل است
    for name in names:
        print(name)


print_names("Ali", "Sara", "Reza")
# Output:
## ---> Ali
## ---> Sara
## ---> Reza

# Example9️⃣️: ذخیره اطلاعات دانشجو — رکورد ثابت
student = ("Ali", 20, "Computer Science", 19.5)

name, age, major, avg = student
print(f"{name} studies {major}, average: {avg}")

# Example1️⃣️0️⃣️:  استفاده در کتابخانه‌ها — مثلاً `zip()`
names = ["Ali", "Sara", "Reza"]
ages = [20, 19, 21]

pairs = list(zip(names, ages))
print(pairs)  # [('Ali', 20), ('Sara', 19), ('Reza', 21)]

for name, age in pairs:  # هر عنصر یک تاپل است
    print(f"{name} is {age} years old")

# Example1️⃣️1️⃣️:  Ussing in dict.items()
grades = {"Ali": 20, "Sara": 18}
for item in grades.items():
    print(item)  # ('Ali', 20) — یک تاپل
# Every item in dict.items() is pair tuple ---> (key، value)

# Example1️⃣️2️⃣️: تغییر نام متغیرها (Swapping) با تاپل
a = 10
b = 20

a, b = b, a  # (a, b) = (b, a)
print(a, b)  # 20 10

# Example1️⃣️3️⃣️: .count(item) شمارش تکرار
t = (1, 2, 2, 3, 2)
print(t.count(2))  # 3

# Example1️⃣️5️⃣️: .index(item) .index(item)
print(t.index(3))  # Output: 3    ---> if notFound: ValueError 

# Example1️⃣️4️⃣️: 
# Example1️⃣️6️⃣️:
# Example1️⃣️7️⃣️:
# Example1️⃣️8️⃣️:
# Example1️⃣️9️⃣️:
# Example2️⃣️0️⃣️:
```

کاربردهای رایج استفاده از تاپل به عنوان کلید

```python
grid = {  # مختصات (x, y)
    (0, 0): "start",
    (1, 2): "treasure",
    (3, 4): "enemy"
}
phone_book = {  # نام و نام‌خانوادگی
    ("Ali", "Rezaei"): "0912-111-2222",
    ("Sara", "Ahmadi"): "0912-333-4444"
}
student_scores = {  # ترکیپ چندویژگی
    ("Math", "Quiz1", "Easy"): 95,
    ("Math", "Midterm", "Hard"): 78
}
```

```python
class TuppleClass:

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

## 6.4. 🅱️ List `[]`

* مرتب (ordered) است عناصر ترتیب خاصی دارند.
* تغییرپذیر (mutable) است می‌تونی عناصرش رو تغییر بدی.
* قابل تکرار (iterable) است.
* می‌تونه تکراری داشته باشه.
* می‌تونه انواع مختلف داده رو داشته باشه (عدد، رشته، لیست دیگر، تابع و ...).

```python
list1 = [1, 2, 3, 4, 5, 6]
list2 = ["Python", True, 5, [4, 5, 6], 1, "hello", 3.14, [1, 2], True, "red", "blue", "green", "gray", "yellow", 3.6]
list3 = ['apple', 'banana', 'cherry']
list4 = []
list5 = [num * 2 for num in list1]
list6 = [num ** 2 for num in range(1, 6)]
list7 = [char.upper() for char in "behrooz"]
list8_even = [num for num in list1 if num % 2 == 0]
list9_odd = [num for num in list1 if num % 2 != 0]
list10 = [num * 2 if num % 2 == 0 else num * 3 for num in list1]
list12_nestedList = [[1, 2, 3], [4, 5, 6]]

# Example1️⃣️: 


# Example2️⃣️: len(list)
list2 = ["Python", True, 5, [4, 5, 6], 1, "hello", 3.14, [1, 2], True, "red", "blue", "green", "gray", "yellow", 3.6]
print(len(list2))  # Output: 15

# Example3️⃣️: .append(item)
list4 = []
list4.append("one")
list4.append(['grape', 'melon'])
print(list4)  # Output: ['one', ['grape', 'melon']]
print(len(list4))  # Output: 2

# Example4️⃣️: .extend(iterable) اضافه کردن چند آیتم 
list4 = []
list4.extend(['grape', 'melon'])
print(list4)  # ['grape', 'melon']

# Example5️⃣️: .insert(index, item) درج در موقعیت خاص
list3 = ['apple', 'banana', 'cherry']
list3.insert(1, 'kiwi')
print(list3)  # ['apple', 'kiwi', 'banana', 'cherry']

# Example6️⃣️: .remove(item)
list3.remove('banana')
print(list3)  # Output: ['apple', 'cherry']

# Example7️⃣️: .pop(index) حذف و بازگردانی آیتم
list3 = ['apple', 'banana', 'cherry']
last = list3.pop()  # Last item
print(last)  # Output: cherry
second = list3.pop(1)  # index1
print(second)  # Output: banana

# Example8️⃣️: .clear()
list3.clear()

# Example9️⃣️: .reverse() معکوس کردن لیست در جا
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
# نکته: reversed_nums = numbers.reverse() آنگاه reversed_nums برابر None خواهد شد 

# Example1️⃣️0️⃣️: `+`
a = [1, 2]
b = [3, 4]
c = a + b
print(c)  # [1, 2, 3, 4]

# Example1️⃣️1️⃣️: `*`
[0] * 5  # [0, 0, 0, 0, 0]
['hi'] * 3  # ['hi', 'hi', 'hi']

# Example1️⃣️2️⃣️: `in`
print('apple' in fruits)  # True یا False
print(99 in numbers)  # False

# Example1️⃣️3️⃣️: Slicing
lst = ['a', 'b', 'c', 'd', 'e']

print(lst[0])  # 'a' — اولین
print(lst[-1])  # 'e' — آخرین
print(lst[1:4])  # ['b', 'c', 'd'] — برش
print(lst[::-1])  # ['e', 'd', 'c', 'b', 'a'] — معکوس (بدون تغییر لیست اصلی)

# Example1️⃣️4️⃣️: .index(item) - ValueError if not Exist
list3 = ['apple', 'banana', 'cherry']
print(list3.index('cherry'))  # 2 

# Example1️⃣️5️⃣️: .count(item)
nums = [1, 2, 2, 3, 2]
print(nums.count(2))  # 3

# Example1️⃣️6️⃣️: کپی کردن
lst_original = [1, 2, 3]
lst_copy = lst_original  # ❌️ فقط ارجاع
lst_copy.append(4)
print(lst_original)  # [1, 2, 3, 4] ← تغییر کرد!

# راه‌های درست کپی:
safe1 = lst_original[:]  # slice
safe2 = list(lst_original)  # constructor
safe3 = lst_original.copy()  # method
safe4 = [x for x in lst_original]  # list comprehension

# Example1️⃣️7️⃣️: حذف تکراری‌ها (با حفظ ترتیب — پایتون 3.7+)
lst = [1, 2, 2, 3, 1, 4]
unique = list(dict.fromkeys(lst))  # [1, 2, 3, 4]

# Example1️⃣️8️⃣️: رزرو برای بعد

# Example1️⃣️9️⃣️: رزرو برای بعد

```

## 6.5. 🅱️ List Comprehension ► `[]`

* روش کوتاه، خوانا برای ساخت لیست جدید از یک ایترابل (مثل لیست، رشته، دیکشنری و ...) است
* تمام عناصر رو فوراً ایجاد می‌کنه و در حافظه نگه می‌دارد
* به جای نوشتن یک حلقه for بلند، فقط با یک خط کد، لیست مورد نظرساخته می‌شود
* مواردی که می‌توانند جایگزین ListComprehension شوند
    * generatorExpression: وقتی داده‌ها بزرگ هستند و نمی‌خوای همه رو یک‌جا در حافظه بگیری: `(x**2 for x in range(1000000))`
    * مورد `()filter()`+`map`: وقتی منطق پیچیده است
    * حلقه عادی: وقتی کد خیلی پیچیده یا چند خطی هست
* نکته مهم: اگر به جای `[]` از `()` استفاده شود آنگاه دیگر `ListComprehension` نخواهد بود بلکه  `GeneratorExpression` خواهد شد

```python
# Syntax: [expression for item in iterable if condition]
# ----> expression: چه چیزی به لیست اضافه بشه (مثلاً item, item * 2, item.upper())
# ----> item: هر عنصر در مجموعه
# ----> iterable: لیست، رشته، تاپل، و غیره
# ----> if condition (اختیاری): فقط اگر شرط درست بود، آیتم اضافه می‌شه
```

<div dir="ltr">

| کار            | نحوه نوشتن                                   |
|----------------|----------------------------------------------|
| ساخت لیست ساده | `[x*2 for x in lst]`                         |
| با شرط         | `[x for x in lst if x > 0]`                  |
| با if-else     | `["even" if x%2==0 else "odd" for x in lst]` |
| روی دیکشنری    | `[k for k, v in d.items() if v > 10]`        |
| ترکیب دو حلقه  | `[f"{a}{b}" for a in A for b in B]`          |

</div>

```python
# Example1️⃣️: squares[Traditional]
squares = []
for n in [1, 2, 3, 4, 5]:
    squares.append(n ** 2)
print(squares)  # Output: [1, 4, 9, 16, 25]

# Example1️⃣️: squares[List Comprehension]
squares = [n ** 2 for n in [1, 2, 3, 4, 5]]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Example2️⃣️: even
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Example3️⃣️: تبدیل رشته به لیست حروف بزرگ
text = "hello"
upper_chars = [char.upper() for char in text]
print(upper_chars)  # ['H', 'E', 'L', 'L', 'O']

# Example4️⃣️:  استخراج ایمیل‌های گیمیل
emails = ["ali@yahoo.com", "sara@gmail.com", "reza@gmail.com", "taha@outlook.com"]
gmails = [email for email in emails if email.endswith("@gmail.com")]
print(gmails)  # ['sara@gmail.com', 'reza@gmail.com']

# Example5️⃣️: حذف مقادیر خالی یا None
data = ["Ali", "", "Sara", None, "Reza", "   ", "Leyla"]
cleaned = [item for item in data if item]  # فقط truthy ها
print(cleaned)  # ['Ali', 'Sara', 'Reza', 'Leyla']

# Example6️⃣️: ایجاد لیست از دیکشنری‌ها (با شرط)
people = [
    {"name": "Ali", "age": 20},
    {"name": "Sara", "age": 17},
    {"name": "Reza", "age": 25}
]

adults = [p["name"] for p in people if p["age"] >= 18]
print(adults)  # ['Ali', 'Reza']

# Example7️⃣️: ایجاد ماتریس (لیست دو بعدی)
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
# خروجی:
# [
#  [1, 2, 3],
#  [2, 4, 6],
#  [3, 6, 9]
# ]

# Example8️⃣️: استخراج کلیدها یا مقادیر از دیکشنری
grades = {"ali": 20, "sara": 18, "reza": 15}

# فقط نام‌هایی که نمره‌شون بالای 17 است
top_students = [name for name, grade in grades.items() if grade > 17]
print(top_students)  # ['ali', 'sara']

# Example9️⃣️: تبدیل لیست از رشته به عدد (با فیلتر کردن ورودی‌های معتبر)
strings = ["1", "2", "abc", "3", "xyz", "4"]
numbers = [int(s) for s in strings if s.isdigit()]
print(numbers)  # [1, 2, 3, 4]

# Example1️⃣️0️⃣️: ترکیب دو لیست (مثل دکارتی)
colors = ["red", "blue"]
items = ["shirt", "hat"]
combinations = [f"{color} {item}" for color in colors for item in items]
print(combinations)
# ['red shirt', 'red hat', 'blue shirt', 'blue hat']


# Example1️⃣️1️⃣️: if-else
numbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']

# Example1️⃣️2️⃣️: رزرو برای بعد
# Example1️⃣️3️⃣️: رزرو برای بعد
```

## 6.6. 🅱️ Filter

* تابع filter() یک "فیلتر" هوشمند است که روی یک لیست (یا هر چیز قابل پیمایش) اجرا می‌شه و فقط عناصری که شرط ما رو دارن، نگه می‌داره.
* فیلتر تغییری در لیست اصلی نمی‌دهد
* می‌تواند روی هر ایتریبل کار کند

```python
# Syntax: filter(function, iterable)
# ------> function: a function that return True or False for ech item
# ------> iterable: لیست، تاپل، رشته، و غیره — چیزی که می‌تونیم رویش حلقه بزنیم.
# ------> return: IterableObject ==> list(IterableObject) or Tuple(IterableObject)
```

```python
# Example1️⃣️: EvenNumbers
evens = []
for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if num % 2 == 0:
        evens.append(num)
print(evens)  # Output: [2, 4, 6, 8, 10]

# Example1️⃣️: EvenNumbers By Filter
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(evens)  # Output: [2, 4, 6, 8, 10]

# Example2️⃣️: فیلتر رشته‌های غیرخالی
texts = ["hello", "", "world", " ", "python", None]
valid_texts = list(filter(None, texts))
# وقتی function = None باشه، filter فقط عناصری رو نگه می‌داره که درست (True) باشند
print(valid_texts)  # ['hello', 'world', ' ', 'python']

# Example3️⃣️: کلمات بلندتر از ۵ حرف
long_words = list(filter(lambda w: len(w) > 5, ["cat", "python", "elephant", "dog", "butterfly"]))
print(long_words)  # ['python', 'elephant', 'butterfly']

# Example4️⃣️: افراد بالای۱۸سال
people = [
    {"name": "Ali", "age": 20},
    {"name": "Sara", "age": 17},
    {"name": "Reza", "age": 25},
    {"name": "Leyla", "age": 16}
]

adults = list(filter(lambda p: p["age"] >= 18, people))
print(adults)  # Output: [{'name': 'Ali', 'age': 20}, {'name': 'Reza', 'age': 25}]

# Example5️⃣️: اعداد مثبت
positives = list(filter(lambda x: x > 0, [-3, -1, 0, 2, 5, -7, 8]))
print(positives)  # [2, 5, 8]

# Example6️⃣️: فیلتر ایمیل‌های دامنه
emails = ["ali@yahoo.com", "sara@gmail.com", "reza@outlook.com", "leyla@gmail.com"]
gmails = list(filter(lambda e: e.endswith("@gmail.com"), emails))
print(gmails)  # ['sara@gmail.com', 'leyla@gmail.com']


# Example7️⃣️: اعداد اول بدون لامبدا
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True


primes = list(filter(is_prime, range(1, 100)))
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Example8️⃣️: 
users = [{'name': 'Behrooz', 'family': 'nadery', 'born': 1369, 'shopCart': []},
         {'name': 'Alireza', 'family': 'saberi', 'born': 1400, 'shopCart': []},
         {'name': 'Attefeh', 'family': 'Rezaie', 'born': 1372, 'shopCart': ['kotlin', 'vue']}]
result = filter(lambda user: not user['shopCart'], users)  # معادل result = filter(lambda user: len(user['shopCart']) == 0, users)
print(list(result))
# Output: [
# {'name': 'Behrooz', 'family': 'nadery', 'born': 1369, 'shopCart': []}, 
# {'name': 'Alireza', 'family': 'saberi', 'born': 1400, 'shopCart': []}]


# Example9️⃣️: رزرو برای بعد
# Example1️⃣️0️⃣️: رزرو برای بعد
```

* همه کارهای filter() رو می‌شه با لیست درک (list comprehension) هم انجام داد
* استفاده از فیلتر هنگامی خوب است که تنها قصد فیلتر کردن داشته‌باشیم ولی اگر همزمان قصد تغییر در دیتا نیز داشته باشیم آنگاه بهتر است از list comprehension استفاده شود

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens_f = list(filter(lambda x: x % 2 == 0, numbers))  # filter 
evens_l = [x for x in numbers if x % 2 == 0]  # list comprehension
```

## 6.7. 🅱️ map

* هر عنصر از یک لیست (یا هر ایترابل) رو به یک تابع می‌ده و خروجی یک "نگاشت" جدید ایجاد می‌کنه
    * زبان ساده: به ازای هر چیز در این لیست، این کار رو انجام بده
* همه کارهای map() رو می‌شه با List Comprehension هم انجام داد
* تنها یکبار روی لیست یا غیره می‌تواند پیمایش صورت بپذیرد و در پیمایش دوم با لیست خالی مواجه می‌شود
* به صورت «Lazy» عمل می‌کند، به این معنی که محاسبات تنها زمانی انجام می‌شود که به نتایج آن نیاز باشد

```python
# Syntax: map(function, iterable)
# ----> function: تابعی که می‌خوای روی هر عنصر اعمال کنی
# ----> iterable: لیست، رشته، تاپل، دیکشنری و غیره
# ----> return: IterableObject ==> list(IterableObject) or Tuple(IterableObject)
```

```python
# Example1️⃣️: square(Traditional)
numbers = [1, 2, 3, 4]
squares = []
for n in numbers:
    squares.append(n ** 2)

# Example1️⃣️: square(map)
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))  # معادل ListComprehension ----> [x**2 for x in numbers]
print(squares)  # [1, 4, 9, 16]

# Example2️⃣️: تبدیل رشته به عدد
str_nums = ["1", "2", "3", "4"]
int_nums = list(map(int, str_nums))
print(int_nums)  # [1, 2, 3, 4]

# Example3️⃣️: تبدیل اعداد به رشته
nums = [10, 20, 30]
str_nums = list(map(str, nums))
print(str_nums)  # ['10', '20', '30']

# Example4️⃣️: تبدیل حروف به بزرگ (Upper Case)
words = ["hello", "world", "python"]
upper_words = list(map(str.upper, words))
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# Example5️⃣️: طول هر رشته در لیست
fruits = ["apple", "banana", "cherry"]
lengths = list(map(len, fruits))
print(lengths)  # [5, 6, 6]

# Example6️⃣️: گرد کردن اعداد اعشاری
floats = [3.1415, 2.718, 1.414]
rounded = list(map(lambda x: round(x, 2), floats))
print(rounded)  # [3.14, 2.72, 1.41]

# Example7️⃣️:  حذف فاصله از انتهای رشته‌ها (strip)
texts = ["  hello  ", " python ", "  world  "]
cleaned = list(map(str.strip, texts))
print(cleaned)  # ['hello', 'python', 'world']


# Example8️⃣️: اعمال تابع مشخص
def add_tax(price):
    return price * 1.09  # اضافه کردن ۹٪ مالیات


prices = [100, 200, 300]
with_tax = list(map(add_tax, prices))
print(with_tax)  # [109.0, 218.0, 327.0]

# Example9️⃣️: تبدیل دمای سانتیگراد به فارنهایت
celsius = [0, 20, 30, 40]


def c_to_f(c):
    return (c * 9 / 5) + 32


fahrenheit = list(map(c_to_f, celsius))
print(fahrenheit)  # [32.0, 68.0, 86.0, 104.0]

# Example1️⃣️0️⃣️: استخراج کلیدهای دیکشنری
people = [
    {"name": "Ali", "age": 20},
    {"name": "Sara", "age": 18},
    {"name": "Reza", "age": 25}
]

names = list(map(lambda p: p["name"], people))
print(names)  # ['Ali', 'Sara', 'Reza']

# Example1️⃣️1️⃣️: استخراج مقادیر دیکشنری
grades = {"ali": 20, "sara": 18, "reza": 15}
values = list(map(lambda x: x * 10, grades.values()))  # مثلاً تبدیل به نمره از 200
print(values)  # [200, 180, 150]

# Example1️⃣️2️⃣️: تبدیل تاریخ‌ها به فرمت خاص
from datetime import date

dates = [date(2024, 1, 1), date(2024, 2, 15), date(2024, 3, 10)]

formatted = list(map(lambda d: d.strftime("%Y-%m-%d"), dates))
print(formatted)  # ['2024-01-01', '2024-02-15', '2024-03-10']

# Example1️⃣️3️⃣️: تبدیل باینری به دسیمال
binary_list = ["1010", "1111", "1001"]

decimals = list(map(lambda b: int(b, 2), binary_list))
print(decimals)  # [10, 15, 9]

# Example1️⃣️4️⃣️: zip + map ---> استفاده از تابع مپ همراه چند لیست
names = ["Ali", "Sara", "Reza"]
scores = [85, 92, 78]

# می‌تونه روی چند ایترابل کار کنه، به شرطی که تابع همون تعداد ورودی داشته باشه که در اینجا کار با دوتا لیست(ایتریبل) می‌باشد
messages = list(map(lambda n, s: f"{n}: {s}%", names, scores))
print(messages)  # ['Ali: 85%', 'Sara: 92%', 'Reza: 78%']

# Example1️⃣️5️⃣️:  تبدیل مسیرهای فایل به نام فایل
paths = [
    "/home/user/docs/file1.txt",
    "/home/user/pics/photo.jpg",
    "/home/user/music/song.mp3"
]

# فقط نام فایل رو بگیر
import os

filenames = list(map(os.path.basename, paths))
print(filenames)  # ['file1.txt', 'photo.jpg', 'song.mp3']

# Example1️⃣️6️⃣️:  اعمال تابع روی کلیدها و مقادیر دیکشنری
data = {"  ALI  ": 20.5, "  SARA  ": 18.2}

# تمیز کردن کلیدها و گرد کردن مقادیر
cleaned = dict(zip(
    map(str.strip, map(str.title, data.keys())),  # تمیز + حروف اول بزرگ
    map(round, data.values())  # گرد کردن
))

print(cleaned)  # {'Ali': 20, 'Sara': 18}

# Example1️⃣️7️⃣️: map() + filter() + sum()
numbers = ["10", "abc", "20", "xyz", "30"]

# فقط رشته‌های عددی رو تبدیل به عدد کن و جمع بزن
total = sum(
    map(int, filter(str.isdigit, numbers))
)
print(total)  # 60


# Example1️⃣️8️⃣️:
def add(x, y):
    return x + y


list1 = [1, 2, 3]
list2 = [4, 5, 6]
added_numbers = map(add, list1, list2)  # معادل:  added_numbers = map(lambda x, y: x + y, list1, list2)

result_list = list(added_numbers)  # تبدیل به لیست
print(result_list)  # خروجی: [5, 7, 9]

# Example1️⃣️9️⃣️: در پیمایش دوم لیست خالی خواهد بود
names = ["akbar", "natasha", "zeinab", "maryam", "Kobra"]
upper_names = map(lambda name: name.upper(), names)
print(list(upper_names))  # Output: ['AKBAR', 'NATASHA', 'ZEINAB', 'MARYAM', 'KOBRA']
print(list(upper_names))  # Output: []

# Example2️⃣️0️⃣️:
users = [{'name': 'amirali', 'family': 'ojaghi', 'born': 1369, 'shopCart': []},
         {'name': 'mahmood', 'family': 'sabeti', 'born': 1400, 'shopCart': []},
         {'name': 'hossein', 'family': 'taheri', 'born': 1372, 'shopCart': ['kotlin', 'vue']}]

result_user = filter(lambda user: not user['shopCart'], users)
result_user_name = lambda user: user['name']
result = map(result_user_name, result_user)  # معادل: result = [user['name'] for user in users if len(user['shopCart']) == 0]
print(list(result))  # Output: ['amirali', 'mahmood']

```

## 6.8. 🅱️ Generator

در پایتون، گاهی با داده‌های بسیار بزرگ سروکار داریم (مثلاً یک فایل ۱۰ گیگابایتی یا یک سری عددی بی‌نهایت) اگر تمام داده‌ها را در حافظه ذخیره کنیم (مثلاً در یک لیست)، ممکن است با مشکل مصرف بالای حافظه مواجه شویم.

**generator**: یک تابع یا عبارت که به جای بازگرداندن تمام مقادیر یک‌جا (مثل لیست)، مقادیر را یکی یکی و در زمان واقعی تولید می‌کند

**هدف generator**: مصرف بسیار کم حافظه به دلیل استفاده از داده‌های پویا و lazy(یعنی تولید فقط در هنکام نیاز) تا تمام دیتا یکباره در حافظه ذخیره نگردد

* بدلیل اینکه generatorها از نوع iterator هستند پس نیاز به تعریف تابع `next()` ندارند و فقط یک بار قابل پیمایش هستند
* اگر یک ماژول یک generator برگرداند آنگاه ناگزیر باید روی آن پیمایش کرد تا به محتوی آن دست یافت
* با کلمه کلیدی `yield` یا علامت `()` پیاده‌سازی می‌شود.
* ۲نوع Generator در پایتون داریم
    1. Generator Function با کلمه کلیدی `yield`
    2. Generator Expression با علامت `()`
        * شبیه List Comprehension با علامت `[]`
* کاربرد
    * پردازش داده‌های بزرگ»:مثل فایل‌های بزرگ، لاگ‌ها» و CSV بدون بارگذاری کل داده
    * «جریان داده (DataStreaming)»: شبیه‌سازی داده‌های زنده (مانند سنسورها)
    * «پایپلاین پردازش داده»:`filter` → `map` → `reduce` با حافظه کم
    * «تولید دنباله‌های بی‌نهایت»: اعداد فیبوناچی، اعداد اول، دنباله‌های ریاضی
    * «کاهش مصرف حافظه»:وقتی نیازی به نگه‌داری تمام داده‌ها نیست

### 6.8.1. ✅️ GeneratorFunction ► `yield`

**GeneratorFunction**: تابعی که در آن از yield استفاده شده است

* مهم: فراخوانی این تابع، مقدار را برنمی‌گرداند، بلکه یک `GeneratorObject` ایجاد می‌کند.
* نحوه کار yield
    * وقتی yield اجرا می‌شود، تابع موقتاً متوقف می‌شود و مقدار را برمی‌گرداند.
    * وضعیت تابع (متغیرها، محل اجرا و ...) در حافظه نگه داشته می‌شود.
    * در فراخوانی بعدی `next()`، اجرا از همان نقطه ادامه می‌یابد.
* وضعیت تابع(شامل مقادیر متغیرها و موقعیت اجرای تابع) حفظ می‌شود
* قابلیت ادامه تابع از همان نقطه توقف
* عدم محاسبه و برگرداندن یکباره تمام مقادیر بلکه محاسبه و تولیدیکی پس از دیگری

```python
def my_generator():
    yield 1
    yield 2
    yield 3
```

### 6.8.2. ✅️ GeneratorExpression ► `()`

* شبیه `list comprehension` است، اما به جای `[]` از `()` استفاده می‌کند و یک generator ایجاد می‌کند.

```python
# Syntax: (expression for item in iterable if condition)
```

تفاوت Generator با List Comprehension

| مورد          | List Comprehension               | Generator Expression                                 |
|---------------|----------------------------------|------------------------------------------------------|
| نحوه نوشتن    | `[x**2 for x in range(5)]`       | `(x**2 for x in range(5))`                           |
| نوع خروجی     | لیست                             | generator object                                     |
| ایجاد         | تمام عناصر رو فوراً ایجاد می‌کند | عناصر رو به صورت lazy(تنبل:درهنگام‌نیاز)تولید می‌کنه |
| حافظه         | تمام عناصر در حافظه              | فقط یک عنصر در هر لحظه                               |
| قابلیت پیمایش | چندباره                          | فقط یک‌بار                                           |
| سرعت اولیه    | سریع (اما ممکن است کند باشد)     | فوری (چون هنوز تولید نشده)                           |

### 6.8.3. ✅️ Examples

مثال1️⃣️: تولید اعداد یک تا سه

```python
# ╔═════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔽𝕦𝕟𝕔𝕥𝕚𝕠𝕟 ║
# ╚═════════════════════╝
def count_up():
    yield 1
    yield 2
    yield 3


# ==> by for
gen = count_up()
for n in gen:
    print(n)  # Output: 1, 2, 3

# ==> Manual
gen = count_up()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# print(next(gen))  # StopIteration

# ╔═══════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕚𝕠𝕟 ║
# ╚═══════════════════════╝
# ==> by for
gen_expr = (x for x in [1, 2, 3])
for n in gen_expr:
    print(n)  # Output: 1, 2, 3

# ==> Manual
gen_expr = (x for x in [1, 2, 3])
print(next(gen_expr))  # Output: 1
print(next(gen_expr))  # Output: 2
print(next(gen_expr))  # Output: 3
# print(next(gen_expr))  # StopIteration

# ╔═════════════════════╗
# ║ 𝕃𝕚𝕤𝕥 ℂ𝕠𝕞𝕡𝕣𝕖𝕙𝕖𝕟𝕤𝕚𝕠𝕟 ║
# ╚═════════════════════╝
# ==> by for
gen_list_comp = iter([x for x in [1, 2, 3]])
for n in gen_list_comp:
    print(n)  # Output: 1, 2, 3

# ==> Manual
gen_list_comp = iter([x for x in [1, 2, 3]])
print(next(gen_list_comp))  # Output: 1
print(next(gen_list_comp))  # Output: 2
print(next(gen_list_comp))  # Output: 3
# print(next(gen_list_comp))  # StopIteration
```

مثال2️⃣️: تولید اعداد زوج تا یک حد مشخص

```python
# ╔═════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔽𝕦𝕟𝕔𝕥𝕚𝕠𝕟 ║
# ╚═════════════════════╝
def even_numbers(limit):
    num = 0
    while num <= limit:
        yield num
        num += 2


gen = even_numbers(10)
for n in gen:
    print(n)  # Output: 0, 2, 4, 6, 8, 10

# ╔═══════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕚𝕠𝕟 ║
# ╚═══════════════════════╝
limit = 10
gen_expr = (num for num in range(0, limit + 1, 2))

for n in gen_expr:
    print(n)  # Output: 0, 2, 4, 6, 8, 10

# ╔═════════════════════╗
# ║ 𝕃𝕚𝕤𝕥 ℂ𝕠𝕞𝕡𝕣𝕖𝕙𝕖𝕟𝕤𝕚𝕠𝕟 ║
# ╚═════════════════════╝
limit = 10
gen_list_comp = [num for num in range(0, limit + 1, 2)]

for n in gen_list_comp:
    print(n)  # Output: 0, 2, 4, 6, 8, 10

```

مثال3️⃣️: تولید مربع اعداد زوج تا یک حد مشخص

```python
# ╔═════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔽𝕦𝕟𝕔𝕥𝕚𝕠𝕟 ║
# ╚═════════════════════╝
def even_numbers_squared(limit):
    num = 0
    while num <= limit:
        yield num ** 2  # مربع عدد زوج
        num += 2


limit = 10
gen = even_numbers_squared(limit)
for n in gen:
    print(n)  # Output: 0, 4, 16, 36, 64, 100

# ╔═══════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕚𝕠𝕟 ║
# ╚═══════════════════════╝
limit = 10
gen_expr = (num ** 2 for num in range(0, limit + 1, 2))
for n in gen_expr:
    print(n)  # Output: 0, 4, 16, 36, 64, 100

# ╔═════════════════════╗
# ║ 𝕃𝕚𝕤𝕥 ℂ𝕠𝕞𝕡𝕣𝕖𝕙𝕖𝕟𝕤𝕚𝕠𝕟 ║
# ╚═════════════════════╝
limit = 10
gen_list_comp = [num ** 2 for num in range(0, limit + 1, 2)]
for n in gen_list_comp:
    print(n)  # Output: 0, 4, 16, 36, 64, 100
```

مثال4️⃣️: تولید بی‌نهایت اعداد فیبوناچی

```python
# ╔═════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔽𝕦𝕟𝕔𝕥𝕚𝕠𝕟 ║
# ╚═════════════════════╝
def fibonacci(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


limit = 10
fib = fibonacci(limit)
for n in fib:
    print(n)  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


# ╔═══════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕚𝕠𝕟 ║
# ╚═══════════════════════╝
def fib_gen(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


limit = 10
gen_expr = (x for x in fib_gen(limit))

for n in gen_expr:
    print(n)  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


# ╔═════════════════════╗
# ║ 𝕃𝕚𝕤𝕥 ℂ𝕠𝕞𝕡𝕣𝕖𝕙𝕖𝕟𝕤𝕚𝕠𝕟 ║
# ╚═════════════════════╝
def fib_gen(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


limit = 10
gen_list_comp = [x for x in fib_gen(limit)]

for n in gen_list_comp:
    print(n)  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

مثال5️⃣️: پردازش خطوط یک فایل بدون بارگذاری کل فایل

```python
# ╔═════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔽𝕦𝕟𝕔𝕥𝕚𝕠𝕟 ║
# ╚═════════════════════╝
def read_large_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


for line in read_large_file("huge_log.txt"):
    if "ERROR" in line:
        print(line)

# ╔═══════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕚𝕠𝕟 ║
# ╚═══════════════════════╝
filename = "huge_log.txt"

with open(filename, 'r') as file:
    gen_expr = (line.strip() for line in file)
    for line in gen_expr:
        if "ERROR" in line:
            print(line)

# ╔═════════════════════╗
# ║ 𝕃𝕚𝕤𝕥 ℂ𝕠𝕞𝕡𝕣𝕖𝕙𝕖𝕟𝕤𝕚𝕠𝕟 ║
# ╚═════════════════════╝
filename = "huge_log.txt"

print("List Comprehension (NOT RECOMMENDED for large files):")
with open(filename, 'r') as file:
    lines = [line.strip() for line in file]  # ❌ تمام فایل در حافظه
for line in lines:
    if "ERROR" in line:
        print(line)
```

مثال6️⃣️: تولید داده‌های شبیه‌سازی شده (مثلاً دما)

```python
# ╔═════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔽𝕦𝕟𝕔𝕥𝕚𝕠𝕟 ║
# ╚═════════════════════╝
import random


def sensor_data():
    while True:
        temp = random.uniform(20, 30)
        yield round(temp, 2)


sensor = sensor_data()
for _ in range(5):
    print(f"دمای فعلی: {next(sensor)}°C")  # Output: 25.34, 27.12, 22.89, ...

# ╔═══════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕚𝕠𝕟 ║
# ╚═══════════════════════╝
import random

# Generator Expression شبیه‌سازی شده با iter + lambda
sensor_gen = (round(random.uniform(20, 30), 2) for _ in iter(int, 1))  # int, 1 → همیشه False → بی‌نهایت
for _ in range(5):
    print(f"دمای فعلی: {next(sensor_gen)}°C")  # Output: 24.67, 28.01, 21.95, ...
# ╔═════════════════════╗
# ║ 𝕃𝕚𝕤𝕥 ℂ𝕠𝕞𝕡𝕣𝕖𝕙𝕖𝕟𝕤𝕚𝕠𝕟 ║
# ╚═════════════════════╝
import random

data_buffer = [round(random.uniform(20, 30), 2) for _ in range(100)]  # تولید ۱۰۰ عدد تصادفی (به عنوان بافر)
for i in range(5):
    print(f"دمای فعلی: {data_buffer[i]}°C")
```

مثال7️⃣️: نمایش وضعیت متغیرها

```python
# ╔═════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔽𝕦𝕟𝕔𝕥𝕚𝕠𝕟 ║
# ╚═════════════════════╝
def counter_with_state():
    count = 0
    while count < 3:
        print(f"Before yield: count = {count}")
        yield count
        count += 1
        print(f"Ⓜ️After yield: count = {count}")


gen = counter_with_state()
print("Start:")
print(next(gen))
print("❗️After first next")
print(next(gen))
print(next(gen))

# Output:
## -----> Start:
## -----> Before yield: count = 0
## -----> 0
## -----> ❗️After first next
## -----> Ⓜ️After yield: count = 1
## -----> Before yield: count = 1
## -----> 1
## -----> Ⓜ️After yield: count = 2
## -----> Before yield: count = 2
## -----> 2


# ╔═══════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕚𝕠𝕟 ║
# ╚═══════════════════════╝
print("بدلیل عدم توانایی استفاده از لاگ این امکان وجود ندارد")

# ╔═════════════════════╗
# ║ 𝕃𝕚𝕤𝕥 ℂ𝕠𝕞𝕡𝕣𝕖𝕙𝕖𝕟𝕤𝕚𝕠𝕟 ║
# ╚═════════════════════╝
print("بدلیل عدم توانایی استفاده از لاگ این امکان وجود ندارد")
```

مثال8️⃣️: وقتی یک generator پیمایش شود آنگاه محتوای آن خالی خواهد شد

```python
# ╔═════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔽𝕦𝕟𝕔𝕥𝕚𝕠𝕟 ║
# ╚═════════════════════╝
def gen_func():
    for x in [1, 2, 3]:
        yield x


print("\nGenerator Function:")
gen = gen_func()
print(list(gen))  # Output: [1, 2, 3]
print(list(gen))  # Output: []

# ╔═══════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕚𝕠𝕟 ║
# ╚═══════════════════════╝
print("Generator Expression:")
gen = (x for x in [1, 2, 3])
print(list(gen))  # Output: [1, 2, 3]
print(list(gen))  # Output: []

# ╔═════════════════════╗
# ║ 𝕃𝕚𝕤𝕥 ℂ𝕠𝕞𝕡𝕣𝕖𝕙𝕖𝕟𝕤𝕚𝕠𝕟 ║
# ╚═════════════════════╝
# تولید لیست با list comprehension، سپس تبدیل به iterator
gen = iter([x for x in [1, 2, 3]])

print("\nList Comprehension (as iterator):")
print(list(gen))  # Output: [1, 2, 3]
print(list(gen))  # Output: []
```

مثال9️⃣️: Generator + itertools.islice - دریافت ۵ عدد اول از اعداد زوج

```python
import itertools

n = 5


# ╔═════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔽𝕦𝕟𝕔𝕥𝕚𝕠𝕟 ║
# ╚═════════════════════╝
def infinite_evens():
    num = 0
    while True:
        yield num
        num += 2


for value in itertools.islice(infinite_evens(), n):
    print(value)  # Output: 0, 2, 4, 6, 8

# ╔═══════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕚𝕠𝕟 ║
# ╚═══════════════════════╝
for value in itertools.islice((x for x in itertools.count(0, 2)), n):
    print(value)  # Output: 0, 2, 4, 6, 8

# ╔═════════════════════╗
# ║ 𝕃𝕚𝕤𝕥 ℂ𝕠𝕞𝕡𝕣𝕖𝕙𝕖𝕟𝕤𝕚𝕠𝕟 ║
# ╚═════════════════════╝
# تولید n عدد اول اعداد زوج با list comprehension
even_numbers = [2 * i for i in range(n)]  # [0, 2, 4, 6, 8]
for value in itertools.islice(iter(even_numbers), n):
    print(value)  # Output: 0, 2, 4, 6, 8
```

مثال1️⃣️0️⃣️: نمایش اعداد زوج در یک لیست داده شده

```python
source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ╔═════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔽𝕦𝕟𝕔𝕥𝕚𝕠𝕟 ║
# ╚═════════════════════╝
def even_generator(lst):
    for num in lst:
        if num % 2 == 0:
            yield num


result = list(even_generator(source))
print("Generator Function:", result)  # Output: [2, 4, 6, 8, 10]

# ╔═══════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕚𝕠𝕟 ║
# ╚═══════════════════════╝
print(list(num for num in source if num % 2 == 0))  # Output: [2, 4, 6, 8, 10]

# ╔═════════════════════╗
# ║ 𝕃𝕚𝕤𝕥 ℂ𝕠𝕞𝕡𝕣𝕖𝕙𝕖𝕟𝕤𝕚𝕠𝕟 ║
# ╚═════════════════════╝
print([num for num in source if num % 2 == 0])  # Output: [2, 4, 6, 8, 10]
```

مثال1️⃣️1️⃣️: مربع اعداد زوج یک تا ده

```python
# ╔═════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔽𝕦𝕟𝕔𝕥𝕚𝕠𝕟 ║
# ╚═════════════════════╝
def even_squares_generator():
    for x in range(1, 10):
        if x % 2 == 0:
            yield x ** 2


squares = even_squares_generator()
for sq in squares:
    print(sq)  # Output: 4, 16, 36, 64
# ╔═══════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕚𝕠𝕟 ║
# ╚═══════════════════════╝
squares = (x ** 2 for x in range(1, 10) if x % 2 == 0)
for sq in squares:
    print(sq)  # Output: 4, 16, 36, 64
# ╔═════════════════════╗
# ║ 𝕃𝕚𝕤𝕥 ℂ𝕠𝕞𝕡𝕣𝕖𝕙𝕖𝕟𝕤𝕚𝕠𝕟 ║
# ╚═════════════════════╝
squares = [x ** 2 for x in range(1, 10) if x % 2 == 0]
for sq in squares:
    print(sq)  # Output: 4, 16, 36, 64
```

مثال1️⃣️2️⃣️: تبدیل رشته به حروف بزرگ

```python
# ╔═════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔽𝕦𝕟𝕔𝕥𝕚𝕠𝕟 ║
# ╚═════════════════════╝
def clean_upper_generator(word_list):
    for word in word_list:
        stripped = word.strip()
        if stripped:  # فقط اگر غیرخالی باشد
            yield stripped.upper()


words = ["hello", "", "world", "  ", "python"]
for w in clean_upper_generator(words):
    print(w)  # Output: HELLO, WORLD, PYTHON

# ╔═══════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕚𝕠𝕟 ║
# ╚═══════════════════════╝
words = ["hello", "", "world", "  ", "python"]
clean_upper = (word.strip().upper() for word in words if word.strip())
for w in clean_upper:
    print(w)  # Output: HELLO, WORLD, PYTHON

# ╔═════════════════════╗
# ║ 𝕃𝕚𝕤𝕥 ℂ𝕠𝕞𝕡𝕣𝕖𝕙𝕖𝕟𝕤𝕚𝕠𝕟 ║
# ╚═════════════════════╝
words = ["hello", "", "world", "  ", "python"]
clean_upper = [word.strip().upper() for word in words if word.strip()]
for w in clean_upper:
    print(w)  # Output: HELLO, WORLD, PYTHON
```

مثال1️⃣️3️⃣️: خواندن و پردازش خط‌به‌خط فایل data.txt

```
Hello World
# This is a comment
Python is great
   # Another comment with spaces
Keep coding
```

```python
# ╔═════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔽𝕦𝕟𝕔𝕥𝕚𝕠𝕟 ║
# ╚═════════════════════╝
def read_clean_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            cleaned = line.strip()
            if cleaned and not cleaned.startswith("#"):
                yield cleaned


for line in read_clean_lines("data.txt"):
    print(line)  # Output: Hello World, Python is great, Keep coding

# ╔═══════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕚𝕠𝕟 ║
# ╚═══════════════════════╝
line_gen = (line.strip() for line in open("data.txt", "r"))

for line in line_gen:
    if line.startswith("#"):
        continue
    if line:  # اطمینان از اینکه خط خالی نیست
        print(line)  # Output: Hello World, Python is great, Keep coding

# ╔═════════════════════╗
# ║ 𝕃𝕚𝕤𝕥 ℂ𝕠𝕞𝕡𝕣𝕖𝕙𝕖𝕟𝕤𝕚𝕠𝕟 ║
# ╚═════════════════════╝
# خواندن فایل و پردازش با list comprehension
with open("data.txt", "r") as file:
    lines = [line.strip() for line in file]
for line in lines:
    if line and not line.startswith("#"):
        print(line)  # Output: Hello World, Python is great, Keep coding
```

مثال1️⃣️4️⃣️: محاسبه تفاوت سرعت اجرا در مقایسه جمع اعداد بین 0 تا 99,999,999

```python
from time import time


# ╔═════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔽𝕦𝕟𝕔𝕥𝕚𝕠𝕟 ║
# ╚═════════════════════╝
def number_generator(n):
    """یک تابع مولد که اعداد 0 تا n-1 را تولید می‌کند."""
    for num in range(n):
        yield num


start_time = time()
print(f"GeneratorFunction: {sum(number_generator(100000000))}")
end_time = time()
print(f"----------> duration: {end_time - start_time:.6f} second")
# Output:
## GeneratorFunction: 4999999950000000
## ----------> duration: 2.902747 second

# ╔═══════════════════════╗
# ║ 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤𝕚𝕠𝕟 ║
# ╚═══════════════════════╝
start_time = time()
print(f"GeneratorExprerssion: {sum(num for num in range(100000000))}")  # --> GeneratorExprerssion
end_time = time()
print(f"----------> duration: {end_time - start_time} second")
# Output:
## GeneratorExprerssion: 4999999950000000 
## ----------> duration: 3.010427236557007 second

# ╔═════════════════════╗
# ║ 𝕃𝕚𝕤𝕥 ℂ𝕠𝕞𝕡𝕣𝕖𝕙𝕖𝕟𝕤𝕚𝕠𝕟 ║
# ╚═════════════════════╝
start_time = time()
print(f"ListComprehension: {sum([num for num in range(100000000)])}")  # --> ListComprehension
end_time = time()
print(f"-------> duration: {end_time - start_time} second")
# Output:
## ListComprehension: 4999999950000000 
## -------> duration: 3.480952739715576 second

```

## 6.9. 🅱️ Zip

* برای ادغام عناصر چندین مجموعه قابل پیمایش (iterable) به صورت موازی به کار می‌رود.
* این تابع یک ایتراتور (iterator) از چندتایی‌ها (tuples) برمی‌گرداند که هر کدام شامل عناصر متناظر از ورودی‌ها هستند.
* کاربردهای رایج
    * ساخت دیکشنری از دو لیست: `dict(zip(keys, values))`
    * پیمایش موازی چند لیست: `for x, y in zip(list1, list2)`
    * ترانهاده ماتریس: `list(zip(*matrix))`
    * مقایسه عناصر:‌تشخیص تفاوت‌ها در دو لیست
    * پردازش داده‌های موازی: داده‌های دانشجو، محصولات، و غیره
    * تبدیل داده‌های عمودی به افقی: مثلا در پردازش CSV
* نکات مهم:
    * خروجی `zip()` یک `zip object` است پس باید با `list()` یا `tuple()` تبدیل شود
    * فقط تا کوتاه‌ترین لیست ادامه می‌یابد: عناصر اضافی نادیده گرفته می‌شوند
    * قابل استفاده با هر iterable نظیر لیست و تاپل و رشته و دیکشنری و غیره
    * غیرقابل پیمایش مجدد: مثل generatorها، فقط یک بار قابل استفاده است
    * برای بازگرداندن به حالت اولیه از `unzip()` استفاده می‌شود

```python
# Syntac: zip(iterable1, iterable2, ...)
## --> Input:  iterable2 ==> Such as: List, Tuple, Dictionary, String, ...
## --> Return: ZipObject ==> Iterator
```

```python
# Example1️⃣️: 
names = ['Ali', 'Sara', 'Reza']
ages = [20, 19, 21]
print(list(zip(names, ages)))  # Output: [('Ali', 20), ('Sara', 19), ('Reza', 21)]

# Example2️⃣️: ترکیب دو لیست
names = ['Ali', 'Sara', 'Reza']
scores = [85, 92, 78]
print(list(zip(names, scores)))  # Output: [('Ali', 85), ('Sara', 92), ('Reza', 78)]

# Example3️⃣️: ترکیب ۳ لیست
names = ['Ali', 'Sara', 'Reza']
ages = [20, 19, 21]
cities = ['Tehran', 'Shiraz', 'Mashhad']
print(list(zip(names, ages, cities)))  # Output: [('Ali', 20, 'Tehran'), ('Sara', 19, 'Shiraz'), ('Reza', 21, 'Mashhad')]

# Example4️⃣️: استفاده در حلقه for
names = ['Ali', 'Sara']
scores = [85, 92]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Output:
# Ali: 85
# Sara: 92

# Example5️⃣️: تبدلی داده‌های سطری به ستونی (Transpose)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = list(zip(*matrix))
print(transposed)  # Output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# Example6️⃣️: ترکیب کلید و مقدار برای ساخت دیکشنری
keys = ['name', 'age', 'city']
values = ['Ali', 20, 'Tehran']
print(dict(zip(keys, values)))  # Output: {'name': 'Ali', 'age': 20, 'city': 'Tehran'}

# Example7️⃣️: ترکیب با رشته‌ها
s1 = "abc"
s2 = "123"
print(list(zip(s1, s2)))  # Output: [('a', '1'), ('b', '2'), ('c', '3')]

# Example8️⃣️: استفاده با range
items = ['apple', 'banana', 'cherry']
indexed = list(zip(range(len(items)), items))

for index, item in indexed:
    print(f"{index}: {item}")
# Output: 0: apple
# Output: 1: banana
# Output: 2: cherry

# Example9️⃣️: مقایسه دو لیست عنصر به عنصر
list1 = [1, 2, 3]
list2 = [1, 4, 3]

differences = [(i, a, b) for i, (a, b) in enumerate(zip(list1, list2)) if a != b]
print(differences)  # [(1, 2, 4)] → فقط عنصر اندیس ۱ متفاوت است

# Example1️⃣️0️⃣️: ترکیب دیکشنری‌ها (کلیدها و مقادیر)
d1 = {'a': 1, 'b': 2}
d2 = {'a': 3, 'b': 4}

# ترکیب مقادیر با کلیدهای مشترک
result = {k: (v1, v2) for k, v1, v2 in zip(d1.keys(), d1.values(), d2.values())}
print(result)  # Output: {'a': (1, 3), 'b': (2, 4)}

# Example1️⃣️1️⃣️: پردازش داده‌های موازی
names = ['Ali', 'Sara', 'Reza']
midterm = [80, 90, 75]
final = [85, 88, 80]

for name, mid, final in zip(names, midterm, final):
    average = (mid + final) / 2
    print(f"{name}: میانگین = {average}")
# Output:
## Ali: میانگین = 82.5
## Sara: میانگین = 89.0
## Reza: میانگین = 77.5

# Example1️⃣️2️⃣️: ترکیب fitler و  map
numbers = [1, 2, 3]
powers = [2, 3, 4]

# محاسبهٔ عدد اول به توان عدد دوم
results = list(map(pow, numbers, powers))  # print(results)  # [1**2, 2**3, 3**4] → [1, 8, 81]
#  توجه: map و zip می‌توانند با هم کار کنند، اما در اینجا map به‌صورت خودکار zip را شبیه‌سازی می‌کند. 


# Example1️⃣️3️⃣️:  تشخیص تفاوت طول لیست‌ها
a = [1, 2, 3, 4]
b = [10, 20]
print(list(zip(a, b)))  # Output: [(1, 10), (2, 20)] — فقط دو عنصر، چون b کوتاه‌تر است

# Example1️⃣️4️⃣️: ussing itertools.zip_longest
from itertools import zip_longest

a = [1, 2, 3, 4]
b = [10, 20]
print(list(zip_longest(a, b, fillvalue=0)))
# Output: [(1, 10), (2, 20), (3, 0), (4, 0)]

# Example1️⃣️5️⃣️: باز کردن (unzip) داده‌ها
pairs = [('Ali', 20), ('Sara', 19), ('Reza', 21)]
names, ages = zip(*pairs)

print(names)  # Output: ('Ali', 'Sara', 'Reza')
print(ages)  # Output: (20, 19, 21)
```

# 7. 🅰️ OOP(Object Oriented Programming)

* در کلاس‌ها درحین تعریف یک تابع در داخل آن تابع اگر از کلمه کلیدی self استفاده نشود آنگاه متغیرهای کلاس همراه آورده
  نمی‌شود
* کلمه پارامتر بعنوان ورودی در وقت استفاده از تابع است و کلمه آرگومان بعنوان ورودی‌های یک تابع در بدنه یک فانکشن است

```python
class User:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def show_data(self):
        print(self.name, self.age)


obj = User("behrooz", 33)
obj.show_data()
print("آیا شیء یک نمونه از کلاس است؟", isinstance(obj, User))

```

## 7.1. 🅱️ `self`

* مربوط به نمونه (Instance)
* هر self فقط به همان شیء اشاره می‌کند که متد روی آن فراخوانی شده است
* اولین پارامتر در متدهای عادی کلاس است و به شیء ایجاد شده اشاره می‌کند

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} is barking!")


dog1 = Dog("Rex")
dog2 = Dog("Buddy")

dog1.bark()  # Output: Rex is barking!
dog2.bark()  # Output: Buddy is barking!
```

## 7.2. 🅱️ `cls`

* مربوط به کلاس (Class)
* اولین پارامتر در متدهای کلاسی (@classmethod) است و به خود کلاس اشاره می‌کند
    * نه به یک شیء خاص
* همیشه به کلاس اشاره می‌کند(حتی اگر از روی یک شیء فراخوانی شود)

مثال1️⃣️:

```python
class Dog:
    species = "Canis lupus"  # متغیر استاتیک — متعلق به کلاس
    total_dogs = 0

    def __init__(self, name):
        self.name = name
        Dog.total_dogs += 1  # یا self.__class__.total_dogs += 1

    @classmethod
    def get_species(cls):  # cls ---> Dog(یعنی خود کلاس داگ)
        return cls.species  # معادل Dog.species

    @classmethod
    def create_anonymous(cls):  # cls ---> Dog(یعنی خود کلاس داگ)
        return cls("Anonymous")  # معادل: Dog("Anonymous")


print(Dog.get_species())  # Output: Canis lupus -----> call from CLASS

dog1 = Dog.create_anonymous()  # ceate object by cls
dog2 = Dog("Rex")

print(dog1.name)  # Output: Anonymous
print(dog2.get_species())  # Output: "Canis lupus"
```

تصویر ذهنی

```
کلاس Dog (cls → Dog)
│
├── species = "Canis lupus" ← cls.species
├── total_dogs = 3          ← cls.total_dogs
│
├── dog1 (self → dog1)
├── dog2 (self → dog2)
└── dog3 (self → dog3)
```

مثال2️⃣️:

```python
class Car:
    brand = "Generic"  # StaticVariable
    count = 0

    def __init__(self, model):
        self.model = model
        Car.count += 1  # یا self.__class__.count += 1

    def show_model(self):
        return f"Model: {self.model}"

    @classmethod
    def show_brand(cls):
        return f"Brand: {cls.brand}"

    @classmethod
    def total_cars(cls):
        return f"Total: {cls.count}"


car1 = Car("Model S")
print(car1.show_model())  # Model: Model S ← self

car2 = Car("Model X")
print(car2.show_model())  # Model: Model X ← self

print(Car.show_brand())  # Brand: Generic ← cls
print(Car.total_cars())  # Total: 2 ← cls

print(car1.show_brand())  # Brand: Generic --> حتی از روی شیء هم می‌شود فراخوانی کرد
# Output:
## ---> Model: Model S
## ---> Model: Model X
## ---> Brand: Generic
## ---> Total: 2
## ---> Brand: Generic
```

فرض کنید یک کلاس فرزند دارید

```python
class Tesla(Car):
    brand = "Tesla"


car = Tesla("Model Y")
print(car.show_brand())  # Output: Tesla ----> Because: cls is Tesla
```

اگر در `show_brand` به جای `cls.brand` بنویسید `Car.brand`، همیشه "Generic" چاپ می‌شد(حتی برای Tesla) اما cls هوشمندانه به کلاس واقعی شیء اشاره می‌کند(حتی اگر فرزند باشد).

این رفتار به چندشکلی (Polymorphism) و وراثت (Inheritance) کمک می‌کند.

مثال3️⃣️:

```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    def introduce(self):
        return f"Hi, I'm {self.name}"

    @classmethod
    def get_population(cls):
        return f"Population: {cls.population}"

    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous")

    @staticmethod
    def is_valid_name(name):  # متد استاتیک — هیچ!
        return isinstance(name, str) and len(name) > 0


p1 = Person("Ali")
p2 = Person.create_anonymous()

print(p1.introduce())  # Hi, I'm Ali ← self
print(Person.get_population())  # Population: 2 ← cls
print(Person.is_valid_name("Ali"))  # True ← static

# Output:
## ---> Hi, I'm Ali
## ---> Population: 2
## ---> True
```

چه زمانی چه چیزی استفاده نماییم

| موقعیت                                                                               | استفاده کنید از                        |
|--------------------------------------------------------------------------------------|----------------------------------------|
| می‌خواهید به **داده‌های یک شیء خاص** دسترسی داشته باشید (مثل `name`, `age`, `model`) | `self` → متد عادی                      |
| می‌خواهید **شیء جدیدی بسازید** با روش جایگزین (مثل `from_string`, `create_default`)  | `cls` → `@classmethod`                 |
| می‌خواهید به **متغیرهای کلاسی** دسترسی داشته باشید (مثل `total_count`, `species`)    | `cls` → `@classmethod`                 |
| می‌خواهید **منطقی مستقل** داشته باشید که نه به شیء و نه به کلاس وابسته است           | `@staticmethod` (نه `self` و نه `cls`) |

## 7.3. 🅱️ Override

تعریف مجدد یک متد یا ویژگی در یک کلاس فرزند (زیرکلاس) است که قبلاً در کلاس والد (Superclass) تعریف شده است. هدف از بازنویسی، تغییر یا گسترش رفتار یک متد بدون تغییر نام آن است

برایOverride کردن یک متد، کافی است در کلاس فرزند، متدی با همان نام و همان پارامترها (هرچند پارامترها می‌توانند متفاوت باشند، اما بهتر است سازگار باشند) تعریف شود. مفسر پایتون به طور خودکار متد فرزند را در صورت فراخوانی از طریق یک نمونه از کلاس فرزند، اجرا می‌کند.

* در پایتون، مکانیسم `Override` به صورت پویا (dynamic) انجام می‌شود و در زمان اجرا (runtime) تعیین می‌گردد که کدام نسخه از متد فراخوانی شود.
* عدم نیاز به کلیدواژه خاص: برخلاف زبان‌هایی مانند Java، پایتون نیازی به کلیدواژه‌ای مانند `@Override` ندارد. بازنویسی به صورت ضمنی انجام می‌شود.
* استفاده از super(): برای دسترسی به رفتار کلاس والد، از تابع `super()` استفاده می‌شود.
* موضوع `Override` امکان چندشکلی (Polymorphism) را فراهم می‌کند. یعنی یک متغیر می‌تواند نمونه‌های مختلفی از کلاس‌های فرزند را نگه دارد و متد مناسب را فراخوانی کند.
* نام و پارامترها: برای رعایت قرارداد، بهتر است نام و تعداد پارامترهای متد بازنویسی‌شده با کلاس والد یکسان باشد.

مثال1️⃣️: `Override` متد `speak()` در کلاس‌های حیوانات

```python
class Animal:
    def speak(self):
        return "An animal makes a sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# استفاده
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

# Output:
## ----> Woof!
## ----> Meow!
```

مثال2️⃣️:متد `__str__` برای نمایش سفارشی

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, {self.age} years old"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.name}, ID: {self.student_id}"


# استفاده
p = Person("Ali", 30)
s = Student("Sara", 20, "12345")
print(p)  # Person: Ali, 30 years old
print(s)  # Student: Sara, ID: 12345
```

مثال3️⃣️: استفاده از `super()` برای گسترش رفتار

```python
class Vehicle:
    def start(self):
        return "Vehicle engine started"


class Car(Vehicle):
    def start(self):
        parent_result = super().start()
        return f"{parent_result} and car is ready to drive."


# استفاده
car = Car()
print(car.start())  # Output: Vehicle engine started and car is ready to drive.
```

مثال4️⃣️:متد `area()` در اشکال هندسی

```python
class Shape:
    def area(self):  # این متد از نوع Abstract خواهد بود زیرا دربدنه اصلی تعریف نشده است و اگر در زیر کلاس تعریف نشود ارور میدهد
        raise NotImplementedError("Subclass must implement abstract method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# استفاده
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())
# Output:
## ---> 78.53975 
## ---> 24
```

```python
class Animal:
    def makeSound(self):
        raise NotImplementedError  # بدنه کلاس را در زیر کلاس باید تعریف کنیم وگرنه به ارور برخورد خواهیم کرد


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

## 7.4. 🅱️ Overload

درپایتون موضوع `Overload` نداریم. یعنی شما نمی‌توانید چندین تابع با نام یکسان در یک حوزه(مثلا در یک کلاس) تعریف کنید و اگر این کار را انجام دهید، آخرین تعریف، تعاریف قبلی را بازنویسی (override) می‌کند.

موارد زیر پایتون را از موضوع `overload` بی‌نیاز کرده است

1. Default Arguments

```python
def add(a, b):
    return a + b


def add(a, b, c):
    return a + b + c


# فقط نسخه دوم وجود دارد
# print(add(1, 2))        # ❌ TypeError: missing 1 required argument
print(add(1, 2, 3))  # 6 ✅
```

2. `**kwargs` و `*args`

```python
def add(*args):
    return sum(args)


print(add(1, 2))  # 3
print(add(1, 2, 3, 4))  # 10
```

3. چک کردن نوع و تعداد آرگومان‌ها در بدنه تابع

```python
def process(data):
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, list):
        return [x.upper() for x in data]
    else:
        raise TypeError("Unsupported type")


print(process("hello"))  # HELLO
print(process(["a", "b"]))  # ['A', 'B']
```

4. استفاده از functools.singledispatch (Overload بر اساس نوع اولین آرگومان)

```python
from functools import singledispatch


@singledispatch
def process(data):
    print(f"Unknown type: {type(data)}")


@process.register
def _(data: str):
    print(f"String: {data.upper()}")


@process.register
def _(data: int):
    print(f"Integer: {data * 2}")


process("hello")  # String: HELLO
process(5)  # Integer: 10
process(3.14)  # Unknown type: <class 'float'>
```

5. استفاده از کتابخانه multipledispatch (برای Overload کامل)

```python
# pip install multipledispatch
from multipledispatch import dispatch


@dispatch(int, int)
def add(a, b):
    return a + b


@dispatch(str, str)
def add(a, b):
    return a + " " + b


@dispatch(int, str)
def add(a, b):
    return str(a) + b


print(add(2, 3))  # 5
print(add("Hello", "World"))  # Hello World
print(add(5, " apples"))  # 5 apples
```

6. انجام Overload عملگرها (Operator Overloading) با متدهای خاص (`__add__`, `__str__`, ...)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # (4, 6)
```

## 7.5. 🅱️ Static

* مفهوم Static به صورت ذاتی در زبان پایتون تعریف نشده است.
* اما توسط مفهوم شی‌گرایی و مفهوم Decorator می‌توان این مفهوم و رفتارهای «استاتیک» را شبیه‌سازی و پیاده‌سازی کرد.
* اگر یک متغیر را در داخل کلاس و خارج توابع تعریف کنیم آنگاه آن را استاتیک درنظر می‌گیرد
* برای درک بهتر از زمان استفاده ۱-متغیراستاتیک ۲-متداستاتیک ۳-متدکلاسی
    * **متد عادی**: آیا این متد نیاز دارد اطلاعات یک شیء خاص (مثل self.name) را ببیند؟
    * `@classmethod`: آیا نیاز دارد اطلاعات کلاس (مثل cls.total) را ببیند یا شیء جدیدی بسازد؟
    * `@staticmethod`:  آیا فقط یک تابع منطقی است که هیچ state ای نمی‌خواهد؟

| مورد                | توصیه                                                                                                         |
|---------------------|---------------------------------------------------------------------------------------------------------------|
| 📌 `@staticmethod`  | فقط وقتی استفاده کنید که متد **هیچ ارتباطی با `self` یا `cls` ندارد** — مثلاً یک تابع کمکی منطقی.             |
| 📌 `@classmethod`   | برای Factoryها، متدهای جایگزین سازنده، یا دستکاری کلاس.                                                       |
| 📌 متغیرهای استاتیک | در بدنه کلاس تعریف می‌شوند — اما با `cls.variable` دسترسی داشته باشید، نه `self.variable` (مگر در موارد خاص). |
| 📌 Private Static   | با `_` یا `__` پیشوند بزنید و در `__setattr__` کنترل کنید.                                                    |
| 📌 Caching          | از `@lru_cache` یا `@cache` روی متدهای استاتیک برای بهینه‌سازی استفاده کنید.                                  |
| 📌 Type Hints       | حتی در متدهای استاتیک، حتماً از تایپ‌هینت استفاده کنید — به خصوص در پروژه‌های بزرگ.                           |

### 7.5.1. ✅️ StaticVariable

متغیری که متعلق به کلاس است، نه به هر شیء (نمونه) از آن کلاس. یعنی اگر ۱۰۰ تا شیء از یک کلاس بسازید، این متغیر فقط یک عدد است و بین همه شیءها مشترک است.

* متغیری است که به کلاس تعلق دارد، نه به نمونه(instance)
* بین تمام instance ها مشترک است

مثال1️⃣️:

```python
# Translate: ---> species: گونه
class Dog:
    species = "Canis lupus"  # StaticVariable

    def __init__(self, name):
        self.name = name  # این یک متغیر نمونه (instance variable) است


dog1 = Dog("Rex")
dog2 = Dog("Buddy")

print(dog1.species)  # Output: Canis lupus
print(dog2.species)  # Output: Canis lupus

Dog.species = "Wolf"  # Change by CLASS

print(dog1.species)  # Output: Wolf  تغییر کرد
print(dog2.species)  # Output: Wolf  تغییر کرد
```

مثال2️⃣️

```python
class User:
    staticData = 100  # static data for class(access by [ClassName].Variable)


one = User()
two = User()

print("--------Initial value---------------")  # تابع آی‌دی شماره هر متغیر را که در حافظه دارد را نشان می‌دهد
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

# Output:
## ---> --------Initial value---------------
## ---> staticData in User[id: 10864392] ==========> 100
## ---> staticData in one [id: 10864392 ] ---> 100
## ---> staticData in two [id: 10864392 ] ---> 100
## ---> --------change in class---------------
## ---> staticData in User[id: 10861192] ==========> 0
## ---> staticData in one [id: 10861192 ] ---> 0
## ---> staticData in two [id: 10861192 ] ---> 0
## ---> --------Change objects---------------
## ---> staticData in User[id: 10861192] ==========> 0
## ---> staticData in one [id: 10861224 ] ---> 1
## ---> staticData in two [id: 10861256 ] ---> 2
## ---> --------change in class---------------
## ---> staticData in User[id: 10861288] ==========> 3
## ---> staticData in one [id: 10861224 ] ---> 1
## ---> staticData in two [id: 10861256 ] ---> 2
```

مثال3️⃣️: فرض کنید می‌خواهید تعداد کل سگ‌هایی که ساخته‌اید را بشمارید

نکته: اگر self.total_dogs += 1 می‌نوشتید، هر شیء یک کپی جداگانه می‌ساخت — و جواب اشتباه می‌شد!

```python
class Dog:
    total_dogs = 0

    def __init__(self, name):
        self.name = name
        Dog.total_dogs += 1  # هر بار که شیء جدید می‌سازیم، یکی اضافه می‌کنیم


dog1 = Dog("Rex")
dog2 = Dog("Buddy")
dog3 = Dog("Max")

print(Dog.total_dogs)  # 3 ← همه شیءها یک متغیر مشترک دارند
```

مثال4️⃣️:متغیر استاتیک برای شمارش تعداد اشیاء ساخته شده

کاربرد: برای آمار، لاگ، محدودیت تعداد instanceها و...

```python
class Car:
    total_cars = 0  # متغیر استاتیک — متعلق به کلاس

    def __init__(self, name):
        self.name = name
        Car.total_cars += 1  # یا self.__class__.total_cars += 1


# ساخت چند شیء:
car1 = Car("BMW")
car2 = Car("Tesla")
car3 = Car("Benz")

print(Car.total_cars)  # 3
```

مثال4️⃣️: ساخت "استاتیک ReadOnly" با `@classmethod` + `@property`

دراین مثال این یک متغیر استاتیک فقط-خواندنی است(کاملاً شبیه `StaticFinal` در جاوا). همچنین `@classmethod` + `@property` فقط از پایتون `3.9` پشتیبانی م‌شود

```python
class MathConstants:
    _PI = 3.1415926535

    @classmethod
    @property
    def PI(cls):
        return cls._PI


print(MathConstants.PI)  # 3.1415926535

# خطا در هنگام تلاش برای تغییر:
# MathConstants.PI = 3.14 # ❌️ AttributeError: can't set attribute
```

### 7.5.2. ✅️ StaticMethod ► `@staticmethod`

متدی که هیچ ارتباطی با شیء یا کلاس ندارد(فقط منطقاً داخل کلاس گذاشته شده) یعنی نه self بعنوان آرگومان ورودی می‌گیرد، نه cls. مثل یک تابع معمولی است که داخل کلاس قرار گرفته

* متدی که نیازی به `self` یا `cls` ندارد و مستقل از نمونه یا کلاس اجرا می‌شود
* دلایل قرارگرفتن این گونه توابع در داخل کلاس:
    * توابع مرتبط با کلاس هستند وبرای پیاده‌سازی منطق کد نیاز هست در کلاس از آنها استفاده شود
    * برای سازماندهی کد درون کلاس تعریف می‌شوند(مثلا تمام توابع ماشین حساب داخل کلاس ماشین‌حساب قرار داده شود)
    * همانند یک ابزار کمکی(Utility)
* چه زمانی از توابع از نوع StaticMethod استفاده نکنیم
    * استفاده از متدعادی: هنگامی که متد نیاز به دسترسی به `self` یا ویژگی‌های `instance` دارد
    * استفاده از `@classmethod`:اگر متد نیاز به `cls` یا تغییر در کلاس یا دسترسی به کلاس دارد
    * اگر منطق کاملاً مستقل است و جای دیگر هم می‌تواند باشد
        * شاید بهتر است در ماژول سطح بالا تعریف شود، نه درون کلاس

مثال1️⃣️:

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(number):
        return number % 2 == 0


# فراخوانی بدون ساخت شیء:
print(Calculator.add(5, 3))  # 8
print(Calculator.is_even(4))  # True

calc = Calculator()  # حتی اگر شیء بسازید کار میکند ولی نیاز نیست
print(calc.add(10, 20))  # Output: 30
```

مثال2️⃣️ [اشتباه رایج❌️] این قطعه کد تولید خطا میکند زیرا متد استاتیک، self ندارد

```python
class Dog:
    @staticmethod
    def bark():
        print(self.name + " is barking!")  # ❌️ خطا! self تعریف نشده
```

مثال 3️⃣️:فرض کنید می‌خواهید یک کلاس برای محاسبات ریاضی داشته باشید که نیازی به ساخت شیء ندارد

چرا استاتیک؟ چون این توابع به داده‌های داخل شیء (self) یا کلاس (cls) وابسته نیستند — فقط منطق ریاضی هستند.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


# فراخوانی بدون نیاز به ساخت instance:
print(MathUtils.add(5, 3))  # 8
print(MathUtils.multiply(4, 6))  # 24
```

مثال4️⃣️: متد استاتیک برای اعتبارسنجی (Validation)

فرض کنید می‌خواهید قبل از ساخت شیء، ورودی‌ها را چک کنید

```python
class User:
    def __init__(self, email):
        if not User.is_valid_email(email):
            raise ValueError("Invalid email!")
        self.email = email

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email


# استفاده:
user1 = User("ali@gmail.com")  # ✅ OK
# user2 = User("invalid-email") # ❌ Error!
```

مثال5️⃣️: متد استاتیک برای تبدیل واحد (Unit Conversion)

```python
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9


print(Temperature.celsius_to_fahrenheit(0))  # 32.0
print(Temperature.fahrenheit_to_celsius(32))  # 0.0
```

مثال6️⃣️: متد استاتیک برای فرمت‌دهی متن (String Formatting)

کاربرد: پیش‌پردازش متن در سیستم‌های چت، وب‌سایت‌ها، یا پایگاه داده

```python
class TextFormatter:
    @staticmethod
    def clean_spaces(text):
        return " ".join(text.split())

    @staticmethod
    def to_title_case(text):
        return text.title()


# استفاده:
dirty_text = "   hello    world   "
clean = TextFormatter.clean_spaces(dirty_text)
title = TextFormatter.to_title_case(clean)

print(clean)  # "hello world"
print(title)  # "Hello World"
```

### 7.5.3. ✅️ ClassMethod ► `@classmethod`

متدی که به جای شیء، به کلاس دسترسی دارد

* اِلِمان `cls` را به عنوان اولین ورودی می‌گیرد
* برای ساخت شیءهای جایگزین، دستکاری کلاس، یا دسترسی به متغیرهای استاتیک استفاده می‌شود

مثال1️⃣️: ساخت شیء با فرمت جایگزین

```python
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name):
        first, last = full_name.split(" ", 1)
        return cls(first, last)  # cls is Person


p1 = Person("Ali", "Rezaei")
p2 = Person.from_full_name("Sara Ahmadi")  # روش جایگزین ساخت شیء

print(p2.first_name)  # Sara
print(p2.last_name)  # Ahmadi
```

مثال2️⃣️: دسترسی به متغیر استاتیک

```python
class Student:
    school_name = "PySchool"
    total_students = 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1

    @classmethod
    def get_school_info(cls):
        return f"{cls.school_name} has {cls.total_students} students."


s1 = Student("Ali")
s2 = Student("Sara")

print(Student.get_school_info())  # PySchool has 2 students.
```

مثال3️⃣️: در این مثال ۱-متغیراستاتیک ۲-متداستاتیک ۳-متدکلاسی استفاده شده است

```python
class Car:
    brand = "Generic"  # متغیر استاتیک — متعلق به کلاس
    total_cars = 0  # متغیر استاتیک — شمارنده

    def __init__(self, model):
        self.model = model  # متغیر نمونه — متعلق به هر شیء
        Car.total_cars += 1  # یا self.__class__.total_cars += 1

    @staticmethod
    def is_valid_model(model):  # فقط چک می‌کند — وابسته به چیزی نیست
        return len(model) > 0

    @classmethod
    def get_brand_info(cls):  # به کلاس دسترسی دارد — cls.brand
        return f"Brand: {cls.brand}, Total Cars: {cls.total_cars}"

    @classmethod
    def create_default(cls):  # یک شیء پیش‌فرض می‌سازد
        return cls("DefaultModel")


# ✅ متغیر استاتیک:
print(Car.brand)  # Generic

# ✅ متد استاتیک:
print(Car.is_valid_model("Tesla"))  # True

# ✅ متد کلاسی:
car1 = Car.create_default()  # ← با متد کلاسی شیء ساختیم
print(Car.get_brand_info())  # Brand: Generic, Total Cars: 1
```

مثال4️⃣️:

```python
class BankAccount:
    bank_name = "PyBank"  # متغیر استاتیک
    accounts_count = 0  # متغیر استاتیک

    def __init__(self, owner, balance=0):
        if not BankAccount.is_valid_owner(owner):  # ← متد استاتیک
            raise ValueError("Invalid owner name!")
        self.owner = owner
        self.balance = balance
        BankAccount.accounts_count += 1

    @staticmethod
    def is_valid_owner(name):
        return isinstance(name, str) and len(name.strip()) > 0

    @classmethod
    def get_bank_status(cls):  # ← متد کلاسی
        return f"{cls.bank_name} has {cls.accounts_count} accounts."

    @classmethod
    def create_empty_account(cls, owner):
        return cls(owner, 0)  # ← متد کلاسی برای ساخت سریع


# --- استفاده ---
acc1 = BankAccount.create_empty_account("Ali")
print(BankAccount.get_bank_status())  # PyBank has 1 accounts.
```

مثال5️⃣️: ترکیب متغیر استاتیک + متد کلاسی + متد استاتیک

```python
class BankAccount:
    bank_name = "PyBank"  # متغیر استاتیک
    total_accounts = 0  # متغیر استاتیک برای شمارش

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    @classmethod
    def get_bank_info(cls):
        return f"{cls.bank_name} - Total Accounts: {cls.total_accounts}"


# استفاده:
acc1 = BankAccount("Ali", 1000)
acc2 = BankAccount("Sara", 2000)

print(BankAccount.is_valid_amount(50))  # True
print(BankAccount.get_bank_info())  # PyBank - Total Accounts: 2
```

مثال6️⃣️:متغیر استاتیک با کنترل دسترسی و اعتبارسنجی

در این مثال _`count` یک متغیر استاتیک کنترل‌شده است که فقط از طریق متدهای کلاسی قابل دستکاری است

```python
class Counter:
    _count = 0  # متغیر استاتیک "private"

    @classmethod
    def increment(cls):
        cls._count += 1

    @classmethod
    def get_count(cls):
        return cls._count

    @classmethod
    def reset(cls):
        cls._count = 0

    # جلوگیری از تغییر مستقیم با setattr
    def __setattr__(self, name, value):
        if name == '_count':
            raise AttributeError("Cannot modify private static variable directly")
        super().__setattr__(name, value)


c1 = Counter()
c2 = Counter()

Counter.increment()
Counter.increment()
print(Counter.get_count())  # 2

# c1._count = 10  # ❌️ خطا: Cannot modify private static variable directly
```

مثال7️⃣️:متد استاتیک به عنوان Factory Method با اعتبارسنجی

در این مثال from_config یک factory method است که از یک دیکشنری، instance می‌سازد — و validate_db_type یک متد استاتیک برای منطق اعتبارسنجی.

```python
from typing import Literal, Union


class DatabaseConnection:
    def __init__(self, host: str, port: int, db_type: str):
        self.host = host
        self.port = port
        self.db_type = db_type

    @staticmethod
    def validate_db_type(db_type: str) -> bool:
        return db_type in ("mysql", "postgresql", "sqlite")

    @classmethod
    def from_config(cls, config: dict):
        db_type = config.get("type")
        if not cls.validate_db_type(db_type):
            raise ValueError(f"Unsupported database type: {db_type}")
        return cls(config["host"], config["port"], db_type)


# استفاده:
config = {"host": "localhost", "port": 5432, "type": "postgresql"}
conn = DatabaseConnection.from_config(config)
print(conn.db_type)  # postgresql
```

مثال8️⃣️: کَش کردن نتیجه متد استاتیک (Static Method Caching)

در این مثال `@lru_cache` روی متد استاتیک، نتیجه را کَش می‌کند — حتی اگر از instance ها یا کلاس فراخوانی شود، کش مشترک است.

```python
from functools import lru_cache
import time


class MathUtils:

    @staticmethod
    @lru_cache(maxsize=128)
    def fibonacci(n: int) -> int:
        if n < 2:
            return n
        return MathUtils.fibonacci(n - 1) + MathUtils.fibonacci(n - 2)

    @staticmethod
    def cached_fib_with_timer(n: int) -> int:
        start = time.perf_counter()
        result = MathUtils.fibonacci(n)
        end = time.perf_counter()
        print(f"Computed fib({n}) in {end - start:.6f} seconds")
        return result


# تست:
print(MathUtils.cached_fib_with_timer(35))  # اولی کند
print(MathUtils.cached_fib_with_timer(35))  # دومی فوری (کش شده)
```

مثال9️⃣️: متد استاتیک Async

در این مثال متد استاتیک `fetch_data` مستقل از instance است و می‌تواند async باشد(حتی در کلاس‌های معمولی)

```python
import asyncio


class APIClient:
    BASE_URL = "https://api.example.com"

    @staticmethod
    async def fetch_data(endpoint: str) -> dict:
        # شبیه‌سازی درخواست async
        await asyncio.sleep(1)
        return {"data": f"Response from {endpoint}"}

    @classmethod
    async def get_user(cls, user_id: int):
        return await cls.fetch_data(f"/user/{user_id}")


# استفاده:
async def main():
    client = APIClient()
    result = await APIClient.get_user(123)
    print(result)  # {'data': 'Response from /user/123'}


asyncio.run(main())
```

مثال1️⃣️0️⃣️: استفاده از متدهای استاتیک در متاکلاس (MetaClass)

در این مثال متد استاتیک `get_instance_key` در متاکلاس، منطق تولید کلید را جدا کرده — بدون نیاز به `cls` یا `self`

```python
class SingletonMeta(type):
    _instances = {}

    @staticmethod
    def get_instance_key(cls):
        return cls.__name__

    def __call__(cls, *args, **kwargs):
        key = SingletonMeta.get_instance_key(cls)
        if key not in cls._instances:
            cls._instances[key] = super().__call__(*args, **kwargs)
        return cls._instances[key]


class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Connected"


# تست:
db1 = Database()
db2 = Database()
print(db1 is db2)  # True — چون متاکلاس از متد استاتیک برای کلید استفاده کرده
```

مثال1️⃣️1️⃣️: متد استاتیک با Type Dispatch (شبیه Overload استاتیک)

توجه: در `singledispatch`، ترکیب با `@staticmethod` در نسخه‌های پایین‌تر پایتون ممکن است با خطا مواجه شود. در `python 3.9+` پشتیبانی می‌شود. برای نسخه‌های قدیمی‌تر، بهتر است `@classmethod` یا تابع معمولی خارج از کلاس استفاده شود.

```python
from functools import singledispatch


class DataProcessor:

    @staticmethod
    @singledispatch
    def process(data):
        raise NotImplementedError("Unsupported type")

    @process.register
    @staticmethod
    def _(str):
        return data.upper()

    @process.register
    @staticmethod
    def _(int):
        return data * 2

    @process.register
    @staticmethod
    def _(list):
        return [DataProcessor.process(item) for item in data]


# استفاده:
print(DataProcessor.process("hello"))  # HELLO
print(DataProcessor.process(5))  # 10
print(DataProcessor.process(["a", 2]))  # ['A', 4]
```

مثال1️⃣️2️⃣️:متغیر استاتیک با مدیریت Thread-Safe

در این مثال متغیر استاتیک `_count` با قفل، در محیط چند(thread ایمن است).

```python
import threading


class ThreadSafeCounter:
    _count = 0
    _lock = threading.Lock()

    @classmethod
    def increment(cls):
        with cls._lock:
            cls._count += 1

    @classmethod
    def get_count(cls):
        with cls._lock:
            return cls._count


# تست چند-thread:
def worker():
    for _ in range(1000):
        ThreadSafeCounter.increment()


threads = [threading.Thread(target=worker) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()

print(ThreadSafeCounter.get_count())  # 10000 — دقیق و thread-safe
```

مثال1️⃣️3️⃣️:

```python

```

# 8. 🅰️ File

* mode:
    * a: append
    * w: read
    * r: write

```python

# Example1️⃣️: 
file_passwd = open("/etc/passwd")
print(file_passwd.read())
file_passwd.seek(2)  # دو کاراکتر را نادیده بگیر و بقیه را لحاظ کن
print(file_passwd.read())

# Example2️⃣️: 
file_passwd = open("/etc/passwd")
textLines = file_passwd.readlines()  # یک لیست از خطوط که آخر هر خط یک \ قرار میدهد
print(textLines)  # Output: ['root:x:0:0:root:/root:/bin/bash\n', 'daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\n', ...]
print(f"----> {textLines[5]}")  # Output: games:x:5:60:games:/usr/games:/usr/sbin/nologin ---> خط ششم از فایل

# Example3️⃣️:

with open("/etc/passwd", encoding='UTF-8', mode="r") as bFile:
    for l in bFile:
        line = l.strip()
        # mylist = lines.rsplit(",")
        print(line)

# Example4️⃣️: 
with open("/tmp/salam.txt", encoding='UTF-8', mode="w") as bFile:
    bFile.write("STRIIIIIIIIIIIIIIIIIIIIIIIIIIING\n")
```

نکات:

* در درجه اول سعی کنید از ماژول pathlib استفاده نمایید
    * خوانایی بالاتر
    * `CrossPlatform` (خودش `/` یا `\` را مدیریت می‌کند)
    * شیءگرا و زنجیره‌ای (`path.parent / "file.txt"`)
* از ماژول `shutil`برای عملیات‌های "سیستمی" و "مدیریتی" استفاده شود
    * برای `copy`, `move`, `copytree`, `rmtree`, `disk_usage`
* از ماژول `os` برای موارد زیر استفاده نمایید
    * دسترسی به متغیرهای محیطی (os.getenv)
    * ایجاد/حذف دایرکتوری (`os.mkdir`, `os.rmdir`)
    * اجرا دستورات سیستمی (`os.system` — اما ترجیحاً از `subprocess` استفاده کنید)
    * وقتی نیاز به سطح پایین‌تر دارید
* بصورت خلاصه
    * `pathlib`: برای همه کارهای مربوط به مسیر و فایل‌های منفرد(مدرن، خوانا، توصیه‌شده).
    * `os`: برای بررسی وجود، اطلاعات فایل، حذف یا تغییر نام، و کارهای سیستمی.
    * `shutil`: برای کپی یا جابجایی یا حذف در سطح بالا(به خصوص برای پوشه‌ها و متادیتا).

| عملیات       | `pathlib` (شیءگرا)      | `os` (سنتی)         | `shutil` (کمکی برای os)    |
|--------------|-------------------------|---------------------|----------------------------|
| خواندن       | `.read_text()`          | `open().read()`     | ❌ ندارد                    |
| نوشتن        | `.write_text()`         | `open('w')`         | ❌ ندارد                    |
| الحاق        | `.open('a')`            | `open('a')`         | ❌ ندارد                    |
| جستجو        | `.read_text() + filter` | `open() + filter`   | ❌ ندارد                    |
| کپی          | ندارد                   | ندارد               | ✅ `copy()`, `copy2()`      |
| جابجایی      | `.rename()`             | `os.rename()`       | ✅ `move()`                 |
| تغییر نام    | `.rename()`             | `os.rename()`       | ❌ (اما `move` جایگزین است) |
| حذف          | `.unlink()`             | `os.remove()`       | `rmtree` (فقط پوشه)        |
| وجود دارد؟   | `.exists()`             | `os.path.exists()`  | ❌                          |
| اطلاعات فایل | `.stat()`               | `os.stat()`         | ❌                          |
| کپی پوشه     | ❌                       | ❌                   | ✅ `copytree()`             |
| حذف پوشه     | `.rmdir()` (خالی)       | `os.rmdir()` (خالی) | ✅ `rmtree()` (با محتوا)    |
| فضای دیسک    | ❌                       | ❌                   | ✅ `disk_usage()`           |

## 8.1. 🅱️ module glob

ابزار پایتون برای جستجوی فایل‌ها و پوشه‌ها بر اساس الگوی نام است. ماژول glob (مخفف global) در پایتون برای پیدا کردن مسیرهای فایل/پوشه با استفاده از الگوهای وایلدکارت (wildcard) استفاده می‌شود

* دو تابع اصلی دارد
    * `glob.glob()`: لیست تمام موارد مطابق الگو را برمی‌گرداند
    * `glob.iglob()`: یک Generator برمی‌گرداند (برای فایل‌های زیاد — حافظه‌بهینه)
* همیشه از `recursive=True` برای `**` استفاده کنید
* جمع‌آوری تمام فایل‌های تست: `tests/**/test_*.py`
* پیدا کردن فایل‌های لاگ قدیمی: `logs/*2023*.log`
* پیدا کردن فایل‌های پیکربندی: `**/*.conf`
* پیدا کردن تصاویر: `images/**/*.jpg`

```python
# Example1️⃣️: 
import glob

py_files = glob.glob("*.py")  # پیدا کردن تمام فایل‌های .py در پوشه فعلی
print(py_files)  # ['main.py', 'utils.py', 'test_script.py']

# Example2️⃣️: `**` جستجوی بازگشتی (Recursive)
import glob

# پیدا کردن تمام فایل‌های .py در تمام زیرپوشه‌ها
all_py_files = glob.glob("**/*.py", recursive=True)  # الگوی `**` بدون recursive=True کار نمیکند 
for f in all_py_files:
    print(f)  # main.py, src/utils.py, tests/test_main.py, docs/conf.py

# Example3️⃣️: فایل‌های دارای دو رقم در نام
# تمام فایل‌هایی که شامل دو رقم متوالی هستند
digit_files = glob.glob("*[0-9][0-9]*")
print(digit_files)  # ['report2024.txt', 'log_05_backup.log', 'data12.csv']

# Example4️⃣️: فایل‌های log با یک حرف در پسوند
log_files = glob.glob("*.log?")
print(log_files)  # ['app.log1', 'error.logA']

# Example5️⃣️:
from pathlib import Path
import glob

# تبدیل خروجی glob به Path برای کارهای پیشرفته‌تر
for path_str in glob.glob("**/*.py", recursive=True):
    path = Path(path_str)
    print(f"{path.name} → size: {path.stat().st_size} bytes")

# Example6️⃣️:برای فایل‌های زیاد (حافظه‌بهینه)
import glob

# به جای لود کردن تمام مسیرها در حافظه، یکی یکی برمی‌گرداند
for file_path in glob.iglob("**/*.log", recursive=True):
    print("Processing:", file_path)
    # پردازش سنگین روی فایل — بدون اشغال حافظه
# Example7️⃣️:
import glob
from pathlib import Path

# glob.glob
files1 = glob.glob("*.py")

# Path.glob
files2 = list(Path(".").glob("*.py"))

# هر دو یک نتیجه می‌دهند — اما files2 از نوع Path است

# Example8️⃣️:مثال عملی با فایل‌های: /etc/passwd و /tmp/salam.txt
import glob

# جستجوی فایل‌هایی که با "pass" شروع می‌شوند در /etc
passwd_matches = glob.glob("/etc/pass*")
print("🔍 Found in /etc:", passwd_matches)  # Output: ['/etc/passwd', '/etc/passwd-'] (اگر وجود داشته باشند)

# جستجوی فایل‌های txt در /tmp
tmp_txt = glob.glob("/tmp/*.txt")
print("📄 .txt files in /tmp:", tmp_txt)  # Output: ['/tmp/salam.txt', '/tmp/test.txt', ...]

# Example9️⃣️:
# ❌️ اشتباه — بدون recursive=True، ** کار نمی‌کند
glob.glob("**/*.py")

# ✅ درست
glob.glob("**/*.py", recursive=True)

# Example1️⃣️0️⃣️:برای فایل‌های زیاد از iglob استفاده کنید
# بهینه از نظر حافظه
for file in glob.iglob("huge_dir/**/*.log", recursive=True):
    process(file)

# Example1️⃣️1️⃣️:اگر می‌خواهید فقط فایل‌ها را فیلتر کنید — با Path.is_file() ترکیب کنید
from pathlib import Path
import glob

for path_str in glob.glob("**/*", recursive=True):
    path = Path(path_str)
    if path.is_file() and path.suffix == ".py":
        print(path)

# Example1️⃣️2️⃣️:برای الگوهای پیچیده‌تر از fnmatch یا re استفاده کنید
import fnmatch
import os

# جستجوی پیچیده‌تر
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, 'data_??_*.csv'):
        print(file)

# Example1️⃣️3️⃣️:  اگر بخواهید یک دستور find لینوکسی در پایتون بنویسید — glob اولین انتخاب شماست
import glob

# معادل: find . -name "*.py"
python_files = glob.glob("**/*.py", recursive=True)
for f in python_files:
    print(f)

# Example1️⃣️4️⃣️:
# Example1️⃣️5️⃣️:
# Example1️⃣️6️⃣️:
# Example1️⃣️7️⃣️:
# Example1️⃣️8️⃣️:
# Example1️⃣️9️⃣️:
# Example2️⃣️0️⃣️:

```

## 8.2. 🅱️ module pathlib

ماژول pathlib (مدرن‌ترین و شیءگرا — توصیه می‌شود)

```python
from pathlib import Path

# تعریف مسیرها
passwd_path = Path("/etc/passwd")
output_path = Path("/tmp/salam.txt")

# Example1️⃣️: Read(خواندن کامل فایل)
if passwd_path.exists():
    content = passwd_path.read_text(encoding='utf-8')
    print("✅ Read from /etc/passwd (first 100 chars):")
    print(content[:100] + "...")

# Example2️⃣️:  write(جایگزین محتوای قبلی)
output_path.write_text("Hello from pathlib!\n", encoding='utf-8')
print(f"✅ Wrote to {output_path}")

# Example3️⃣️: الحاق (append)
with output_path.open('a', encoding='utf-8') as f:
    f.write("Appended line via pathlib.\n")
print("✅ Appended to file")

# Example4️⃣️:  جستجو در محتوا (search)
lines = passwd_path.read_text().splitlines()
users_with_bin = [line for line in lines if "/bin/bash" in line]
print(f"✅ Found {len(users_with_bin)} users with /bin/bash")

# Example5️⃣️: 

# Example6️⃣️: rename
renamed_path = Path("/tmp/hello.txt")
output_path.rename(renamed_path)
print(f"✅ Renamed {output_path} → {renamed_path}")
output_path = renamed_path  # آپدیت مسیر

# Example7️⃣️: move
moved_path = Path("/tmp/moved_hello.txt")
output_path.rename(moved_path)
print(f"✅ Moved {output_path} → {moved_path}")
output_path = moved_path

# Example8️⃣️: delete
if output_path.exists():
    output_path.unlink()  # حذف فایل
    print(f"✅ Deleted {output_path}")

# Example9️⃣️: بررسی وجود فایل
if not output_path.exists():
    print("✅ File deleted successfully.")

# Example1️⃣️0️⃣️: دریافت اطلاعات فایل
if passwd_path.exists():
    stat = passwd_path.stat()
    print(f"📄 Size: {stat.st_size} bytes")
    print(f"🕒 Modified: {stat.st_mtime}")

# Example1️⃣️1️⃣️: حذف پوشه خالی ---> اگر خالی نباشد باید با کد پایتون پوشه را خالی نمایید
test_dir = Path("/tmp/empty_test_dir")
test_dir.rmdir()
print(f"✅ {test_dir} deleted (was empty).")
```

## 8.3. 🅱️ module os

ماژول os (سطوح پایین‌تر — قدیمی‌تر اما قدرتمند)

```python
import os
from pathlib import Path

passwd_file = "/etc/passwd"
output_file = "/tmp/salam_os.txt"

# Example1️⃣️: read
if os.path.exists(passwd_file):
    with open(passwd_file, 'r', encoding='utf-8') as f:
        content = f.read(100)  # فقط 100 کاراکتر اول
        print("✅ Read via os (first 100 chars):", content + "...")

# Example2️⃣️: write
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("Hello from os module!\n")
print(f"✅ Wrote to {output_file}")

# Example3️⃣️:append
with open(output_file, 'a', encoding='utf-8') as f:
    f.write("Appended line via os.\n")
print("✅ Appended via os")

# Example4️⃣️: search
with open(passwd_file, 'r') as f:
    lines = f.readlines()
    filtered = [line for line in lines if "root" in line]
    print(f"✅ Found {len(filtered)} lines containing 'root'")

# Example5️⃣️:

# Example6️⃣️:تغییر نام (rename)
os.rename(output_file, "/tmp/hello_os.txt")
output_file = "/tmp/hello_os.txt"
print("✅ Renamed via os.rename")

# Example7️⃣️:جابجایی (move) — همان os.rename است
os.rename(output_file, "/tmp/moved_hello_os.txt")
output_file = "/tmp/moved_hello_os.txt"
print("✅ Moved via os.rename")

# Example8️⃣️:حذف (delete)
if os.path.exists(output_file):
    os.remove(output_file)
    print("✅ Deleted via os.remove")

# Example9️⃣️:بررسی وجود
if not os.path.exists(output_file):
    print("✅ File no longer exists.")

# Example1️⃣️0️⃣️:اطلاعات فایل
if os.path.exists("/etc/passwd"):
    stat = os.stat("/etc/passwd")
    print(f"📄 Size: {stat.st_size} bytes")
    print(f"🕒 Modified: {stat.st_mtime}")

# Example1️⃣️1️⃣️: حذف فایل
output_path = Path("/tmp/salam.txt")
os.unlink(output_path)
print(f"🗑️ Deleted {output_path} using os.unlink()")

# Example1️⃣️2️⃣️: ایجاد یک درخت پوشه (حتی اگر والدین وجود نداشته باشند)
os.makedirs("/tmp/demo/subdir1/subdir2", exist_ok=True)  # اگر قبلا موجود بود خطا ندهد و عبور کند
print("✅ Created nested directories with os.makedirs()")

# Example1️⃣️3️⃣️: حذف یک پوشه خالی os.rmdir()
os.rmdir("/tmp/demo/subdir1/subdir2")
os.rmdir("/tmp/demo/subdir1")
os.rmdir("/tmp/demo")
print("✅ Removed empty directories with os.rmdir()")

# Example1️⃣️4️⃣️: WALK: Search all directories and subdirectories
for root, dirs, files in os.walk('/tmp'):
    print(f"\n📁 Root: {root}")
    print(f"📂 Directories: {dirs}")
    print(f"📄 Files: {files}")

# Example1️⃣️5️⃣️: WALK with topdown=False (bottom-up)
for root, dirs, files in os.walk('/tmp', topdown=False):
    print(f"➡️  {root}")
```

## 8.4. 🅱️ Module shutil

ماژول shutil (برای عملیات سطح بالا: کپی، جابجایی، حذف درختی و ...)

```python
import shutil
import os
from pathlib import Path

passwd_file = "/etc/passwd"
tmp_dir = Path("/tmp/demo_shutil")
tmp_dir.mkdir(exist_ok=True)  # اگر قبلا موجود بود خطا ندهد و عبور کند

source_file = tmp_dir / "source.txt"
target_file = tmp_dir / "target.txt"
backup_file = tmp_dir / "backup.txt"

# ایجاد فایل نمونه
source_file.write_text("Sample content for shutil demo.\nLine with keyword: python\n", encoding='utf-8')

# Example1️⃣️:خواندن — shutil خودش read ندارد، پس از open یا pathlib استفاده می‌کنیم
with open(source_file, 'r') as f:
    print("✅ Read via open (for shutil context):")
    print(f.read())

# Example2️⃣️: write
# ماژول shutil نوشتن ندارد

# Example3️⃣️: append
# ماژول shutil الحاق ندارد

# Example4️⃣️: جستجو — shutil search ندارد → با open + خواندن

# Example5️⃣️:کپی (copy)
shutil.copy(source_file, target_file)
print(f"✅ Copied {source_file} → {target_file}")

# Example6️⃣️:کپی با مجوزها و متادیتا (copy2)
shutil.copy2(source_file, backup_file)
print(f"✅ Copied with metadata → {backup_file}")

# Example7️⃣️: جابجایی (move)
moved_file = tmp_dir / "moved.txt"
shutil.move(target_file, moved_file)
print(f"✅ Moved {target_file} → {moved_file}")

# Example8️⃣️:Rename — shutil rename ندارد → از os.rename یا pathlib.rename

# Example9️⃣️: Remove — shutil برای فایل‌های تکی remove ندارد → از os.remove یا pathlib.unlink
# اما برای پوشه‌ها: shutil.rmtree

# Example1️⃣️0️⃣️:کپی کل پوشه (مثال اضافه)
demo_src = Path("/tmp/src_demo")
demo_dst = Path("/tmp/dst_demo")
demo_src.mkdir(exist_ok=True)  # اگر قبلا موجود بود خطا ندهد و عبور کند
(demo_src / "file1.txt").write_text("Hello")
(demo_src / "file2.txt").write_text("World")

shutil.copytree(demo_src, demo_dst, dirs_exist_ok=True)  # exist_ok=True ---> # اگر قبلا موجود بود خطا ندهد و عبور کند
print(f"✅ Copied directory {demo_src} → {demo_dst}")

# Example1️⃣️1️⃣️:حذف پوشه با محتوا
shutil.rmtree(demo_src)
shutil.rmtree(demo_dst)
print("✅ Removed demo directories")

# Example1️⃣️2️⃣️:بررسی فضای دیسک (عملیات سیستمی)
total, used, free = shutil.disk_usage("/")
print(f"💾 Disk Usage — Total: {total // (2 ** 30)} GB, Free: {free // (2 ** 30)} GB")
```

# 9. 🅰️ JSON

* به صورت پیش‌فرض، `json.dumps()` تمام کاراکترهای غیر `ASCII` (مثل فارسی، عربی، چینی) را به `\uXXXX` تبدیل می‌کند.
* با` ensure_ascii=False`، این تبدیل انجام نمی‌شود و کاراکترهای اصلی (مثلاً "علی") در خروجی باقی می‌مانند
* `encode('utf-8').decode()`: در برخی محیط‌های قدیمی یا وب (مثل بعضی سرورها یا مرورگرها) ممکن است نیاز باشد رشته را به بایت‌های UTF-8 تبدیل و دوباره به رشته برگردانید تا کدگذاری به درستی اعمال شود.
* مثال از متن

```python
# در پایتون مدرن و فایل‌های محلی معمولاً نیازی نیست — اما اگر مشکل داشتید
text = "سلام دنیا"
safe_text = text.encode('utf-8').decode('utf-8')  # فقط برای اطمینان از کدگذاری
```

* در JSON، کافی است از ensure_ascii=False و encoding='utf-8' استفاده کنید — نیازی به encode().decode() نیست

| موقعیت       | راه‌حل                                                                       |
|--------------|------------------------------------------------------------------------------|
| نوشتن JSON   | `json.dumps(data, ensure_ascii=False)` + `file.write(..., encoding='utf-8')` |
| خواندن JSON  | `open(file, encoding='utf-8')` + `json.load(f)`                              |
| چاپ در کنسول | `print(json.dumps(data, ensure_ascii=False, indent=2))`                      |
| API / وب     | همیشه هدر `Content-Type: application/json; charset=utf-8` را تنظیم کنید      |
| دیتابیس      | مطمئن شوید ستون‌ها از `utf8mb4` (در MySQL) یا معادل پشتیبانی می‌کنند         |

```python
import json
import os
from pathlib import Path
from datetime import datetime
from typing import Any

# ────────────────────────────────────────────────────────
# ✅ ۱. تعریف مسیرهای فایل‌های JSON — با پشتیبانی UTF-8
# ────────────────────────────────────────────────────────
input_json = Path("/tmp/data_fa.json")  # تغییر نام برای شفافیت
output_json = Path("/tmp/output_fa.json")

# 🌍 داده نمونه با متن فارسی — نام، شهر و پیام‌ها به فارسی
sample_data = {
    "شرکت": "فناوران پیشرو",  # Persian key & value
    "تاسیس": 1394,  # Persian year
    "کارمندان": [
        {"نام": "علی", "سن": 30, "شهر": "تهران", "فعال": True},
        {"نام": "سارا", "سن": 27, "شهر": "شیراز", "فعال": True},
        {"نام": "رضا", "سن": 35, "شهر": "مشهد", "فعال": False}
    ],
    "متادیتا": {
        "آخرین_به‌روزرسانی": "۱۴۰۳-۰۳-۱۲",  # Persian date string
        "نسخه": 1.1
    },
    "پیام_سیستم": "✅ داده‌های اولیه با موفقیت بارگذاری شدند."
}

# ────────────────────────────────────────────────────────
# ✅ ۲. نوشتن JSON در فایل — با ensure_ascii=False برای پشتیبانی فارسی
# ────────────────────────────────────────────────────────
print("📝 در حال نوشتن داده‌های نمونه به فایل ورودی...")
# ⚠️ نکته: `ensure_ascii=False` باعث می‌شود کاراکترهای غیر-ASCII (مثل فارسی) به صورت اصلی ذخیره شوند
# ⚠️ نکته: `encoding='utf-8'` برای ذخیره صحیح در فایل ضروری است
input_json.write_text(
    json.dumps(sample_data, indent=2, ensure_ascii=False),
    encoding='utf-8'
)
print(f"✅ داده‌ها در {input_json} ذخیره شدند.")

# 🧪 تست: خواندن فایل و چاپ محتوا برای اطمینان از صحت فارسی
print("\n🧪 تست خواندن فایل نوشته شده (برای اطمینان از صحت فارسی):")
print(input_json.read_text(encoding='utf-8')[:200] + "...")

# ────────────────────────────────────────────────────────
# ✅ ۳. خواندن JSON از فایل — با encoding='utf-8'
# ────────────────────────────────────────────────────────
print("\n📂 در حال خواندن JSON از فایل...")
with open(input_json, 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)

print("✅ داده‌ها با موفقیت بارگذاری شدند:")
# ⚠️ دوباره ensure_ascii=False برای چاپ صحیح فارسی در کنسول
print(json.dumps(loaded_data, indent=2, ensure_ascii=False))

# ────────────────────────────────────────────────────────
# ✅ ۴. جستجو (Search) — پیدا کردن کارمند با نام فارسی
# ────────────────────────────────────────────────────────
target_name = "سارا"  # نام فارسی
found = None
for emp in loaded_data["کارمندان"]:
    if emp["نام"] == target_name:
        found = emp
        break

if found:
    print(f"\n🔍 کارمند پیدا شد: {json.dumps(found, ensure_ascii=False)}")
else:
    print(f"\n❌ کارمند '{target_name}' یافت نشد.")

# ────────────────────────────────────────────────────────
# ✅ ۵. به‌روزرسانی (Update) — تغییر سن و افزودن تاریخ به‌روزرسانی
# ────────────────────────────────────────────────────────
for emp in loaded_data["کارمندان"]:
    if emp["نام"] == "علی":
        emp["سن"] = 31
        emp["آخرین_تغییر"] = str(datetime.now().date())
        print(f"🔄 سن علی به {emp['سن']} به‌روزرسانی شد.")

# ────────────────────────────────────────────────────────
# ✅ ۶. اضافه کردن (Append) — افزودن کارمند جدید با نام فارسی
# ────────────────────────────────────────────────────────
new_employee = {
    "نام": "نرگس",
    "سن": 29,
    "شهر": "اصفهان",
    "فعال": True
}
loaded_data["کارمندان"].append(new_employee)
print(f"➕ کارمند جدید اضافه شد: {new_employee['نام']}")

# ────────────────────────────────────────────────────────
# ✅ ۷. حذف (Delete) — حذف کارمندان غیرفعال
# ────────────────────────────────────────────────────────
before_count = len(loaded_data["کارمندان"])
loaded_data["کارمندان"] = [emp for emp in loaded_data["کارمندان"] if emp["فعال"]]
after_count = len(loaded_data["کارمندان"])
print(f"🗑️ {before_count - after_count} کارمند غیرفعال حذف شدند.")

# ────────────────────────────────────────────────────────
# ✅ ۸. نوشتن با فرمت زیبا — ensure_ascii=False برای حفظ فارسی
# ────────────────────────────────────────────────────────
print(f"\n💾 در حال نوشتن داده‌های به‌روز شده در {output_json}...")
with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(loaded_data, f, indent=4, ensure_ascii=False, sort_keys=False)

print("✅ فایل JSON با فرمت زیبا و پشتیبانی فارسی ذخیره شد.")

# ────────────────────────────────────────────────────────
# ✅ ۹. خواندن و پارس کردن رشته JSON فارسی (String Parsing)
# ────────────────────────────────────────────────────────
json_string_fa = '''
{
    "وضعیت": "موفق",
    "پیام": "✅ پردازش داده‌ها با موفقیت انجام شد.",
    "تعداد": 42
}
'''

# ⚠️ حتی برای رشته‌های JSON فارسی هم باید ensure_ascii=False استفاده کنیم
parsed_from_string = json.loads(json_string_fa)
print(f"\n💬 پیام پردازش: {parsed_from_string['پیام']} (تعداد: {parsed_from_string['تعداد']})")

# ────────────────────────────────────────────────────────
# ✅ ۱۰. مدیریت خطا — حتی برای JSON فارسی
# ────────────────────────────────────────────────────────
invalid_json_fa = '{"نام": "علی", "سن": }'  # ❌ ناقص — حتی با فارسی!

try:
    broken = json.loads(invalid_json_fa)
except json.JSONDecodeError as e:
    print(f"\n❌ خطای پارس JSON: {e.msg} در خط {e.lineno}، ستون {e.colno}")


# ────────────────────────────────────────────────────────
# ✅ ۱۱. اعتبارسنجی ساختار — برای داده‌های فارسی
# ────────────────────────────────────────────────────────
def validate_employee_fa(emp: dict) -> bool:
    # کلیدهای فارسی را چک می‌کنیم
    required_keys = {"نام", "سن", "شهر", "فعال"}
    return required_keys.issubset(emp.keys()) and isinstance(emp["سن"], int)


print("\n✅ اعتبارسنجی کارمندان:")
for emp in loaded_data["کارمندان"]:
    is_valid = validate_employee_fa(emp)
    status = "✅ معتبر" if is_valid else "❌ نامعتبر"
    print(f"   {emp['نام']}: {status}")


# ────────────────────────────────────────────────────────
# ✅ ۱۲. تبدیل شیء سفارشی به JSON — با پشتیبانی فارسی
# ────────────────────────────────────────────────────────
class UserFa:
    def __init__(self, name: str, signup_date: datetime):
        self.نام = name  # Persian attribute name!
        self.تاریخ_عضویت = signup_date


class DateTimeEncoderFa(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        # برای پشتیبانی از کلیدهای فارسی در خروجی JSON
        return super().default(obj)


user_fa = UserFa("محمد", datetime(2024, 5, 20))
# ⚠️ ensure_ascii=False برای نمایش صحیح "محمد" در خروجی
user_json_fa = json.dumps(
    user_fa.__dict__,
    cls=DateTimeEncoderFa,
    indent=2,
    ensure_ascii=False
)
print(f"\n👤 تبدیل شیء سفارشی به JSON (با نام فارسی):\n{user_json_fa}")


# ────────────────────────────────────────────────────────
# ✅ ۱۳. تبدیل JSON به شیء سفارشی — با کلیدهای فارسی
# ────────────────────────────────────────────────────────
def user_decoder_fa(dct):
    # چک می‌کنیم که کلید فارسی وجود دارد
    if 'تاریخ_عضویت' in dct:
        dct['تاریخ_عضویت'] = datetime.fromisoformat(dct['تاریخ_عضویت'])
        return UserFa(dct['نام'], dct['تاریخ_عضویت'])
    return dct


user_data_str_fa = '{"نام": "لیلا", "تاریخ_عضویت": "2024-04-15T00:00:00"}'
decoded_user_fa = json.loads(user_data_str_fa, object_hook=user_decoder_fa)
print(f"\n🔄 تبدیل JSON به شیء: {decoded_user_fa.نام}، عضویت در {decoded_user_fa.تاریخ_عضویت}")

# ────────────────────────────────────────────────────────
# ✅ ۱۴. فشرده‌سازی — بدون از دست دادن فارسی
# ────────────────────────────────────────────────────────
# ⚠️ حتی در حالت فشرده، ensure_ascii=False برای حفظ فارسی ضروری است
compact_json_fa = json.dumps(loaded_data, separators=(',', ':'), ensure_ascii=False)
print(f"\n📦 طول JSON فشرده: {len(compact_json_fa)} کاراکتر")
print(f"   (در مقابل حالت زیبا: {len(json.dumps(loaded_data, indent=2, ensure_ascii=False))} کاراکتر)")


# ────────────────────────────────────────────────────────
# ✅ ۱۵. استخراج کلیدهای منحصر به فرد — شامل کلیدهای فارسی
# ────────────────────────────────────────────────────────
def extract_keys_fa(obj: Any, keys: set = None) -> set:
    if keys is None:
        keys = set()
    if isinstance(obj, dict):
        keys.update(obj.keys())  # کلیدهای فارسی هم اضافه می‌شوند
        for value in obj.values():
            extract_keys_fa(value, keys)
    elif isinstance(obj, list):
        for item in obj:
            extract_keys_fa(item, keys)
    return keys


all_keys_fa = extract_keys_fa(loaded_data)
print(f"\n🔑 تمام کلیدهای منحصر به فرد یافت شده: {sorted(all_keys_fa)}")

# ────────────────────────────────────────────────────────
# ✅ ۱۶. فیلتر کردن — بر اساس شهر فارسی
# ────────────────────────────────────────────────────────
tehran_employees_fa = [emp for emp in loaded_data["کارمندان"] if emp["شهر"] == "تهران"]
print(f"\n🏙️ کارمندان ساکن تهران: {[emp['نام'] for emp in tehran_employees_fa]}")

# ────────────────────────────────────────────────────────
# ✅ ۱۷. مرتب‌سازی — بر اساس سن
# ────────────────────────────────────────────────────────
sorted_by_age_fa = sorted(loaded_data["کارمندان"], key=lambda x: x["سن"])
ages_str = [f"{emp['نام']}({emp['سن']})" for emp in sorted_by_age_fa]
print(f"\n👴 مرتب‌سازی بر اساس سن: {ages_str}")

# ────────────────────────────────────────────────────────
# ✅ ۱۸. آمار — میانگین سن
# ────────────────────────────────────────────────────────
ages_fa = [emp["سن"] for emp in loaded_data["کارمندان"]]
avg_age_fa = sum(ages_fa) / len(ages_fa) if ages_fa else 0
print(f"\n📊 میانگین سن کارمندان: {avg_age_fa:.1f}")

# ────────────────────────────────────────────────────────
# ✅ ۱۹. مقایسه دو JSON — حتی با کلیدهای فارسی
# ────────────────────────────────────────────────────────
original_fa = {"الف": 1, "ب": 2}
modified_fa = {"الف": 1, "ب": 3, "پ": 4}


def json_diff_fa(old: dict, new: dict) -> dict:
    diff = {}
    all_keys = set(old.keys()) | set(new.keys())
    for key in all_keys:
        old_val = old.get(key, "__مفقود__")
        new_val = new.get(key, "__مفقود__")
        if old_val != new_val:
            diff[key] = {"قدیم": old_val, "جدید": new_val}
    return diff


changes_fa = json_diff_fa(original_fa, modified_fa)
# برای چاپ صحیح کلیدهای فارسی در دیکشنری
print(f"\n⚖️  تغییرات: {json.dumps(changes_fa, ensure_ascii=False, indent=2)}")

# ────────────────────────────────────────────────────────
# ✅ ۲۰. پاک‌سازی و خروجی نهایی — با تأیید فارسی
# ────────────────────────────────────────────────────────
print(f"\n✅ خروجی نهایی در: {output_json}")
print(f"📁 اندازه فایل: {output_json.stat().st_size} بایت")

# نمایش محتوای نهایی — با اطمینان از صحت فارسی
print("\n📋 محتوای نهایی فایل (۳۰۰ کاراکتر اول):")
final_content = output_json.read_text(encoding='utf-8')
print(final_content[:300] + "..." if len(final_content) > 300 else final_content)

# 🧪 تست نهایی: آیا فارسی به درستی ذخیره شده؟
if "علی" in final_content and "تهران" in final_content and "نرگس" in final_content:
    print("\n✅🎉 تبریک! تمام داده‌های فارسی به درستی ذخیره و خوانده شدند.")
else:
    print("\n❌ هشدار: مشکلی در ذخیره‌سازی داده‌های فارسی وجود دارد!")
```

## 9.1. 🅱️ ماژول json2html

* ماژول json2html یک ابزار ساده و سریع برای تبدیل داده‌های JSON به جدول HTML است.
* نکته: این ماژول فقط جدول تولید می‌کند — برای استایل‌دهی یا تعاملی بودن نیاز به CSS/JS جداگانه دارید
* چون json2html.convert() یک رشته HTML برمی‌گرداند (نه داده JSON)، نیازی به json.dumps نیست
    * (و نیازی به encode().decode() هم نیست)
    * کافی است مستقیماً با encoding='utf-8' بنویسید.
*

```python
# Install: pip install json2html
# Syntax: json2html.convert(json=..., ...)
## ---> json: داده JSON (دیکشنری یا لیست)
## ---> table_attributes: ویژگی‌های HTML جدول — مثلclass,id,border
## ---> escape(Default:True): برای امنیت وب آیا محتوی escape بشود یا خیر
## ---> clubbingDefault:True): آیا کلیدهای تکراری در ردیف‌های مجاور ادغام شوند یا خیر
```

| نکته                      | توضیح                                                                     |
|---------------------------|---------------------------------------------------------------------------|
| `escape=False`            | برای نمایش فارسی ضروری است — اما در وب‌اپلیکیشن‌های عمومی، XSS را چک کنید |
| `table_attributes`        | برای افزودن کلاس‌های Bootstrap یا استایل‌های سفارشی                       |
| `dir="rtl"` + `lang="fa"` | برای نمایش صحیح فارسی در مرورگر                                           |
| فونت‌های فارسی            | در CSS از `font-family: Tahoma, Arial, sans-serif` استفاده کنید           |
| `clubbing=False`          | اگر نمی‌خواهید کلیدهای تکراری ادغام شوند (مثلاً در لیست سرورها)           |
| خروجی تمیز                | همیشه یک هدر HTML کامل با متا charset اضافه کنید                          |

مثال1️⃣️️:تبدیل داده کارمندان به جدول HTML

📌 خروجی: یک فایل HTML با جدول زیبا که شامل نام‌های فارسی است.

```python
from json2html import json2html
import json

employees_data = {
    "شرکت": "فناوران رایانش ابری",
    "کارمندان": [
        {"نام": "علی رضایی", "سمت": "توسعه‌دهنده", "دپارتمان": "فنی", "حقوق": 15000000},
        {"نام": "سارا محمدی", "سمت": "تحلیلگر داده", "دپارتمان": "تحلیل", "حقوق": 18000000},
        {"نام": "رضا احمدی", "سمت": "مدیر پروژه", "دپارتمان": "مدیریت", "حقوق": 25000000}
    ]
}

# Convert To HTML
html_table = json2html.convert(
    json=employees_data,
    table_attributes="class='table table-striped' style='border-collapse: collapse; width: 100%;'",
    escape=False  # برای نمایش صحیح فارسی — اما در وب حتماً امنیت را چک کنید
)

# ذخیره در فایل — با پشتیبانی فارسی
with open("employees.html", "w", encoding="utf-8") as f:
    # ⚠️ نیازی به encode/decode نیست — فقط ensure_ascii=False در json.dumps کافی است
    # ولی ما مستقیماً HTML را می‌نویسیم — پس اصلاً نیازی به json.dumps نیست!
    f.write(html_table)

print("✅ جدول HTML با داده‌های فارسی ذخیره شد: employees.html")
```

مثال2️⃣️:گزارش سیستم — لاگ سرورها

📌 خروجی: یک صفحه HTML کامل با استایل RTL، فونت فارسی و رنگ‌بندی وضعیت.

```python
from json2html import json2html

servers_status = [
    {"سرور": "web-01", "آی‌پی": "192.168.1.10", "وضعیت": "🟢 سالم", "آخرین_چک": "1403-03-15"},
    {"سرور": "db-01", "آی‌پی": "192.168.1.20", "وضعیت": "🔴 خطا", "آخرین_چک": "1403-03-15"},
    {"سرور": "cache-01", "آی‌پی": "192.168.1.30", "وضعیت": "🟡 هشدار", "آخرین_چک": "1403-03-15"}
]

html = json2html.convert(
    json=servers_status,
    table_attributes="""
        border="1" 
        style="border-collapse: collapse; width: 100%; text-align: right; direction: rtl;"
    """,
    escape=False
)

# افزودن هدر HTML برای پشتیبانی RTL و فونت فارسی
full_html = f"""
<!DOCTYPE html>
<html dir="rtl" lang="fa">
<head>
    <meta charset="UTF-8">
    <title>📊 گزارش وضعیت سرورها</title>
    <style>
        body {{ font-family: Tahoma, Arial, sans-serif; margin: 20px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: right; }}
        th {{ background-color: #f2f2f2; }}
        .green {{ color: green; }}
        .red {{ color: red; }}
        .yellow {{ color: #cc9900; }}
    </style>
</head>
<body>
    <h1>📊 گزارش وضعیت سرورها — {datetime.now().strftime('%Y-%m-%d %H:%M')}</h1>
    {html}
</body>
</html>
"""

with open("server_report.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("✅ گزارش سرورها با پشتیبانی RTL و فارسی ذخیره شد.")
```

مثال3️⃣️:داده تو در تو (Nested) — اطلاعات محصول + مشخصات فنی

```python
product_data = {
    "محصول": "لپ‌تاپ گیمینگ XYZ",
    "قیمت": "۲۵,۰۰۰,۰۰۰ تومان",
    "مشخصات": {
        "پردازنده": "Intel i7-12700H",
        "رم": "32GB DDR5",
        "گرافیک": "NVIDIA RTX 4070",
        "ذخیره‌سازی": "1TB NVMe SSD",
        "ابعاد": {
            "وزن": "2.3 kg",
            "ضخامت": "20 mm"
        }
    },
    "توضیحات": "✅ مناسب برای گیم و رندرینگ — گارانتی ۲۴ ماهه"
}

html = json2html.convert(
    json=product_data,
    table_attributes="class='table' style='width: 100%; direction: rtl; text-align: right;'",
    escape=False
)

with open("product_detail.html", "w", encoding="utf-8") as f:
    f.write(f"""
    <!DOCTYPE html>
    <html dir="rtl" lang="fa">
    <head><meta charset="utf-8"><title>{product_data['محصول']}</title></head>
    <body style="font-family: Tahoma; padding: 20px;">
        <h2>{product_data['محصول']}</h2>
        <h3>قیمت: {product_data['قیمت']}</h3>
        {html}
        <p><strong>توضیحات:</strong> {product_data['توضیحات']}</p>
    </body>
    </html>
    """)

print("✅ صفحه محصول با ساختار تو در تو ایجاد شد.")
```

مثال4️⃣️: لیست دیکشنری‌ها — نتایج جستجو (مثال واقعی برای وب‌اپلیکیشن)

```python
search_results = [
    {
        "عنوان": "راهنمای خرید لپ‌تاپ",
        "خلاصه": "بهترین لپ‌تاپ‌های سال 1403 برای کاربران حرفه‌ای",
        "امتیاز": 4.8,
        "تاریخ_انتشار": "1403-02-10"
    },
    {
        "عنوان": "مقایسه موبایل‌های پرچم‌دار",
        "خلاصه": "مقایسه جامع آیفون 15 پرو و سامسونگ گلکسی S24 الترا",
        "امتیاز": 4.9,
        "تاریخ_انتشار": "1403-02-15"
    }
]

html = json2html.convert(
    json=search_results,
    table_attributes="""
        class="search-results"
        style="width: 100%; border: 1px solid #eee; direction: rtl; text-align: right;"
    """,
    escape=False
)

css = """
<style>
.search-results th { background-color: #007bff; color: white; }
.search-results td { padding: 10px; border-bottom: 1px solid #eee; }
.search-results tr:hover { background-color: #f8f9fa; }
</style>
"""

with open("search_results.html", "w", encoding="utf-8") as f:
    f.write(f"""
    <!DOCTYPE html>
    <html dir="rtl" lang="fa">
    <head>
        <meta charset="utf-8">
        <title>نتایج جستجو</title>
        {css}
    </head>
    <body style="font-family: Tahoma; padding: 20px;">
        <h2>🔍 نتایج جستجو ({len(search_results)} مورد)</h2>
        {html}
    </body>
    </html>
    """)

print("✅ نتایج جستجو به صورت جدول HTML ذخیره شد.")
```

مثال5️⃣️:خطاها و لاگ‌های سیستم — برای تیم DevOps

```python
system_logs = [
    {"زمان": "1403-03-15 10:23:45", "سطح": "ERROR", "پیام": "اتصال به دیتابیس قطع شد", "ماژول": "database.py"},
    {"زمان": "1403-03-15 10:25:12", "سطح": "WARNING", "پیام": "حافظه RAM به 85% رسید", "ماژول": "monitor.py"},
    {"زمان": "1403-03-15 10:30:00", "سطح": "INFO", "پیام": "سرویس با موفقیت ری‌استارت شد", "ماژول": "service.py"}
]


# رنگ‌بندی بر اساس سطح لاگ
def colorize_log(row):
    level = row.get('سطح', '')
    color = "red" if "ERROR" in level else "orange" if "WARNING" in level else "green"
    return f"<span style='color:{color}; font-weight:bold;'>{level}</span>"


# Convert To HTML
html = json2html.convert(json=system_logs, escape=False)

# جایگزینی سطح لاگ با نسخه رنگی
for log in system_logs:
    colored_level = colorize_log(log)
    html = html.replace(f"<td>{log['سطح']}</td>", f"<td>{colored_level}</td>")

with open("system_logs.html", "w", encoding="utf-8") as f:
    f.write(f"""
    <!DOCTYPE html>
    <html dir="rtl" lang="fa">
    <head><meta charset="utf-8"><title>📊 لاگ‌های سیستم</title></head>
    <body style="font-family: Tahoma; padding: 20px;">
        <h2>📊 لاگ‌های سیستم — {len(system_logs)} رکورد</h2>
        {html}
    </body>
    </html>
    """)

print("✅ لاگ‌های سیستم با رنگ‌بندی ذخیره شد.")
```

مثال6️⃣️:تابع toHtml شما — اصلاح شده برای پشتیبانی فارسی و بهینه‌سازی

```python
from json2html import json2html
import json


def toHtml(inputFileName, outputFileName):
    """
    تبدیل فایل JSON به فایل HTML با پشتیبانی کامل فارسی
    """
    # خواندن JSON — با encoding='utf-8'
    with open(inputFileName, 'r', encoding='utf-8') as f:
        jData = json.load(f)

    # Convert To HTML (For Farsi: escape=False)
    data = json2html.convert(
        json={"data": jData},  # بسته‌بندی در یک کلید برای جلوگیری از flat شدن
        table_attributes="class='table' style='width: 100%; direction: rtl; text-align: right;'",
        escape=False
    )

    # افزودن هدر HTML کامل برای پشتیبانی فارسی
    full_html = f"""
    <!DOCTYPE html>
    <html dir="rtl" lang="fa">
    <head>
        <meta charset="UTF-8">
        <title>📊 گزارش JSON</title>
        <style>
            body {{ font-family: Tahoma, Arial, sans-serif; padding: 20px; }}
            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: right; }}
            th {{ background-color: #f8f9fa; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>📊 گزارش داده‌ها</h1>
        {data}
    </body>
    </html>
    """

    # نوشتن مستقیم — بدون encode/decode — چون data از قبل رشته است
    with open(outputFileName, 'w', encoding='utf-8') as ff:
        ff.write(full_html)

    print(f"✅ فایل HTML ایجاد شد: {outputFileName}")


# تست تابع
if __name__ == "__main__":
    # ایجاد فایل JSON نمونه با فارسی
    sample = {
        "گزارش": "فروش ماهانه",
        "داده‌ها": [
            {"ماه": "فروردین", "فروش": "۱۲۰,۰۰۰,۰۰۰ تومان", "تعداد_سفارش": 150},
            {"ماه": "اردیبهشت", "فروش": "۱۸۰,۰۰۰,۰۰۰ تومان", "تعداد_سفارش": 220}
        ]
    }

    with open("input.json", "w", encoding="utf-8") as f:
        json.dump(sample, f, ensure_ascii=False, indent=2)

    toHtml("input.json", "output.html")
```

# 10. 🅰️Database

* CEUD
    * Create (ایجاد جدول + افزودن محصول)
    * Read (نمایش محصولات — جستجوی فارسی)
    * Update (به‌روزرسانی قیمت)
    * Delete (حذف محصول منقضی شده)

## 10.1. 🅱️ SQLlight

مثال کامل و کاربردی: مدیریت محصولات فروشگاه (با پشتیبانی فارسی)

```python
import sqlite3
from pathlib import Path


def main():
    """مثال کاربردی: مدیریت محصولات فروشگاه آنلاین با SQLite و پشتیبانی فارسی"""

    db_path = Path("/tmp/shop_products.db")

    # 🔧 اتصال به دیتابیس با context manager (اتصال خودکار + بسته شدن امن)
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # ✅ 1. CREATE TABLE — ایجاد جدول محصولات (با پشتیبانی فارسی)
        print("🔧 ایجاد جدول محصولات...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT, -- تولید آی دی خودکار
                name TEXT NOT NULL,          -- نام محصول (پشتیبانی فارسی)
                price INTEGER NOT NULL,      -- قیمت به تومان
                category TEXT,               -- دسته‌بندی
                description TEXT,            -- توضیحات (پشتیبانی فارسی)
                stock INTEGER DEFAULT 0      -- موجودی انبار
            )
        """)
        conn.commit()
        print("✅ جدول محصولات ایجاد شد.")

        # ✅ 2. INSERT — افزودن محصولات (یکی یکی + گروهی)
        print("\n📥 درج محصولات اولیه...")

        # درج تکی — شامل یک محصول فارسی
        cursor.execute("""
            INSERT INTO products (name, price, category, description, stock)
            VALUES (?, ?, ?, ?, ?)
        """, ("کتاب آموزش پایتون", 120000, "کتاب", "📚 کتاب جامع برای یادگیری پایتون — مناسب مبتدی تا پیشرفته", 50))

        # درج گروهی با executemany
        products_bulk = [
            ("دوره آنلاین React", 850000, "دوره آموزشی", "⚛️ آموزش ری‌اکت از صفر تا حرفه‌ای", 100),
            ("ماوس گیمینگ RGB", 450000, "سخت‌افزار", "🖱️ ماوس با نور RGB و DPI قابل تنظیم", 75),
            ("کیبورد مکانیکی", 950000, "سخت‌افزار", "⌨️ کیبورد مکانیکی با کلیدهای قابل تعویض", 30),
            ("دوره هوش مصنوعی", 1200000, "دوره آموزشی", "🤖 آموزش مفاهیم پایه تا پیشرفته هوش مصنوعی", 60),
            ("کوله پشتی لپ‌تاپ", 350000, "اکسسوری", "🎒 کوله پشتی مناسب برای لپ‌تاپ ۱۷ اینچی", 40),
            # ✅ مثال فارسی — فقط یک مورد کافی است طبق درخواست شما
            ("لپ‌تاپ گیمینگ ASUS", 45000000, "لپ‌تاپ", "💻 لپ‌تاپ گیمینگ با کارت گرافیک RTX 4060 — مناسب بازی‌های سنگین", 15)
        ]

        cursor.executemany("""
            INSERT INTO products (name, price, category, description, stock)
            VALUES (?, ?, ?, ?, ?)
        """, products_bulk)

        conn.commit()
        print(f"✅ {len(products_bulk) + 1} محصول با موفقیت اضافه شدند.")

        # ✅ 3. SELECT — نمایش تمام محصولات
        print("\n📋 لیست تمام محصولات:")
        cursor.execute("SELECT id, name, price, stock FROM products ORDER BY id")
        for row in cursor.fetchall():  # دریافت تمام نتایج برای نمایش
            print(f"  - #{row[0]}: {row[1]} — {row[2]:,} تومان (موجودی: {row[3]})")

        # ✅ 4. SELECT + LIKE — جستجوی فارسی در توضیحات
        print("\n🔍 جستجوی محصولات مرتبط با 'گیمینگ' (پشتیبانی فارسی):")
        search_term = "%گیمینگ%"
        cursor.execute("SELECT name, price FROM products WHERE description LIKE ?", (search_term,))
        gaming_products = cursor.fetchall()  # دریافت تمام نتایج برای نمایش
        if gaming_products:
            for prod in gaming_products:
                print(f"  - {prod[0]}: {prod[1]:,} تومان")
        else:
            print("  - ❌ محصولی یافت نشد.")

        # ✅ 5. UPDATE — به‌روزرسانی قیمت یک محصول
        print("\n🔄 به‌روزرسانی قیمت محصول...")
        product_id = 2  # فرض: دوره آنلاین React
        new_price = 799000
        cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
        if cursor.rowcount > 0:
            print(f"✅ قیمت محصول #{product_id} به {new_price:,} تومان به‌روزرسانی شد.")
        else:
            print(f"❌ محصول با ID {product_id} یافت نشد.")

        # ✅ 6. DELETE — حذف محصول با موجودی صفر
        print("\n🗑️ حذف محصولات با موجودی صفر...")
        cursor.execute("DELETE FROM products WHERE stock = 0")
        deleted_count = cursor.rowcount
        if deleted_count > 0:
            print(f"✅ {deleted_count} محصول با موجودی صفر حذف شدند.")
        else:
            print("✅ هیچ محصولی برای حذف یافت نشد.")

        # ✅ 7. SELECT بعد از تغییرات — برای تأیید
        print("\n📊 وضعیت نهایی محصولات:")
        cursor.execute("SELECT id, name, price, stock FROM products ORDER BY price DESC")
        for row in cursor.fetchall():  # دریافت تمام نتایج برای نمایش
            print(f"  - #{row[0]}: {row[1]} — {row[2]:,} تومان (موجودی: {row[3]})")

        # ✅ 8. گزارش آماری — تعداد و میانگین قیمت
        cursor.execute("SELECT COUNT(*), AVG(price), SUM(stock) FROM products")
        count, avg_price, total_stock = cursor.fetchone()
        print(f"\n📈 آمار کلی:")
        print(f"  - تعداد محصولات: {count}")
        print(f"  - میانگین قیمت: {int(avg_price):,} تومان")
        print(f"  - کل موجودی انبار: {total_stock}")

    print(f"\n✅ عملیات با موفقیت به پایان رسید. دیتابیس در {db_path} ذخیره شد.")


# اجرای مثال
if __name__ == "__main__":
    main()
```

خروجی به شکل زیر است

```
🔧 ایجاد جدول محصولات...
✅ جدول محصولات ایجاد شد.

📥 درج محصولات اولیه...
✅ 7 محصول با موفقیت اضافه شدند.

📋 لیست تمام محصولات:
  - #1: کتاب آموزش پایتون — 120,000 تومان (موجودی: 50)
  - #2: دوره آنلاین React — 850,000 تومان (موجودی: 100)
  - #3: ماوس گیمینگ RGB — 450,000 تومان (موجودی: 75)
  - #4: کیبورد مکانیکی — 950,000 تومان (موجودی: 30)
  - #5: دوره هوش مصنوعی — 1,200,000 تومان (موجودی: 60)
  - #6: کوله پشتی لپ‌تاپ — 350,000 تومان (موجودی: 40)
  - #7: لپ‌تاپ گیمینگ ASUS — 45,000,000 تومان (موجودی: 15)

🔍 جستجوی محصولات مرتبط با 'گیمینگ' (پشتیبانی فارسی):
  - ماوس گیمینگ RGB: 450,000 تومان
  - لپ‌تاپ گیمینگ ASUS: 45,000,000 تومان

🔄 به‌روزرسانی قیمت محصول...
✅ قیمت محصول #2 به 799,000 تومان به‌روزرسانی شد.

🗑️ حذف محصولات با موجودی صفر...
✅ هیچ محصولی برای حذف یافت نشد.

📊 وضعیت نهایی محصولات:
  - #7: لپ‌تاپ گیمینگ ASUS — 45,000,000 تومان (موجودی: 15)
  - #5: دوره هوش مصنوعی — 1,200,000 تومان (موجودی: 60)
  - #4: کیبورد مکانیکی — 950,000 تومان (موجودی: 30)
  - #2: دوره آنلاین React — 799,000 تومان (موجودی: 100)
  - #3: ماوس گیمینگ RGB — 450,000 تومان (موجودی: 75)
  - #6: کوله پشتی لپ‌تاپ — 350,000 تومان (موجودی: 40)
  - #1: کتاب آموزش پایتون — 120,000 تومان (موجودی: 50)

📈 آمار کلی:
  - تعداد محصولات: 7
  - میانگین قیمت: 6,695,571 تومان
  - کل موجودی انبار: 370
```

# 11. 🅰️ GUI

## 11.1. 🅱️ tkinter

### 11.1.1. ✅️ Lable

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

### 11.1.2. ✅️ Button

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

### 11.1.3. ✅️ Calculator پوسته

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

### 11.1.4. ✅️ Calculator

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

### 11.1.5. ✅️ Entry

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

### 11.1.6. ✅️ Frame

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

# 12. 🅰️ Regex

## 🅱️ Dot `.`

matches any character except newline

```python
import re

# Example 1: f.n → f + any char + n
text = "fun"
if re.search(r'f.n', text):
    print(f"Example 1: '{text}' matches 'f.n'")
# Basic pattern: . matches exactly one character

# Example 2: f..n → f + any two chars + n
text = "f12n"
if re.search(r'f..n', text):
    print(f"Example 2: '{text}' matches 'f..n'")
# Multiple dots for multiple characters

# Example 3: 3-letter filename with 3-letter extension
filename = "log.txt"
if re.search(r'^...\..{3}$', filename):
    print(f"Example 3: '{filename}' is 3-letter name with 3-letter extension")
# ^ = start, $ = end, \. = literal dot

# Example 4: Find 4-letter words
word = "book"
if re.fullmatch(r'.{4}', word):
    print(f"Example 4: '{word}' is exactly 4 characters")
# fullmatch ensures entire string matches

# Example 5: Simple IP pattern (not fully validated)
ip = "192.168.1.1"
if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip):
    print(f"Example 5: '{ip}' matches basic IP pattern")
# \d = digit, {1,3} = 1 to 3 occurrences

# Example 6: Time pattern HH:MM using dot substitution
time_str = "14:30"
if re.search(r'\d{1,2}\.\d{2}', time_str.replace(':', '.')):
    print(f"Example 6: '{time_str}' matches time pattern with dot")
# Demonstrates pattern flexibility

# Example 7: Words with specific first and last letters
word = "fan"
if re.search(r'f.n', word):
    print(f"Example 7: '{word}' starts with f, ends with n, any middle char")

# Example 8: Find all 3-letter words in text
text = "cat bat rat"
matches = re.findall(r'\w.\w', text)
print(f"Example 8: 3-letter words: {matches}")
# \w = word character (letter, digit, underscore)

# Example 9: Dot matches space too
text = "f n"
if re.search(r'f.n', text):
    print(f"Example 9: '{text}' — dot matches space character")
# Important: . matches whitespace, not just visible chars

# Example 10: Middle character is digit
word = "f5n"
if re.search(r'f.n', word):
    print(f"Example 10: '{word}' — middle character is digit")

# Example 11: Non-greedy dot matching
text = "start<middle>end<another>finish"
match = re.search(r'<.*?>', text)
print(f"Example 11: Non-greedy match: {match.group() if match else 'None'}")
# .*? matches as few characters as possible

# Example 12: Dot with multiline flag
text = "line1\nline2\nline3"
matches = re.findall(r'l.ne', text, re.DOTALL)
print(f"Example 12: With DOTALL flag: {matches}")
# Normally dot doesn't match newline, DOTALL flag changes this

```

## 🅱️ `^` Start of string

Start of string

```python
import re

# Example 1: Starts with 'Top'
text = "Toplearn"
if re.search(r'^Top', text):
    print(f"Example 1: '{text}' starts with 'Top'")
# ^ anchors pattern to beginning of string

# Example 2: Starts with digit
phone = "09123456789"
if re.match(r'^[0-9]', phone):
    print(f"Example 2: '{phone}' starts with a digit")
# re.match automatically anchors to start, so ^ is redundant here

# Example 3: Starts with http or https
url = "https://example.com"
if re.search(r'^https?://', url):
    print(f"Example 3: '{url}' starts with http(s)://")
# ? makes preceding character optional

# Example 4: Starts with uppercase letter
name = "Ali"
if re.search(r'^[A-Z]', name):
    print(f"Example 4: '{name}' starts with uppercase letter")

# Example 5: Starts with hashtag
hashtag = "#python"
if re.search(r'^#', hashtag):
    print(f"Example 5: '{hashtag}' is a hashtag")

# Example 6: Starts with double dash (long argument)
arg = "--help"
if re.search(r'^--', arg):
    print(f"Example 6: '{arg}' is a long argument")

# Example 7: Starts with whitespace (indentation detection)
line = "    print('hello')"
if re.search(r'^\s+', line):
    print(f"Example 7: '{line}' has leading whitespace")
# \s = whitespace character, + = one or more

# Example 8: Starts with minus (negative number)
number = "-42"
if re.search(r'^-', number):
    print(f"Example 8: '{number}' is negative")

# Example 9: Starts with quote
quote = '"Hello"'
if re.search(r'^"', quote):
    print(f"Example 9: '{quote}' starts with double quote")

# Example 10: Starts with <! (HTML/XML doctype)
html = "<!DOCTYPE html>"
if re.search(r'^<!(?:DOCTYPE)?', html):
    print(f"Example 10: '{html}' is HTML doctype")
# (?:...) = non-capturing group

# Example 11: Multiline mode - ^ matches start of each line
text = "first line\nsecond line\nthird line"
matches = re.findall(r'^\w+', text, re.MULTILINE)
print(f"Example 11: Start of each line: {matches}")
# MULTILINE flag makes ^ match start of each line

# Example 12: Negative lookahead at start
text = "not_allowed_start"
if re.search(r'^(?!not_)', text):
    print(f"Example 12: '{text}' — doesn't start with 'not_'")
else:
    print(f"Example 12: '{text}' — starts with forbidden prefix")
# (?!...) = negative lookahead

```

## 🅱️ `$` End of string

```python
import re

# Example 1: Ends with 'rn'
text = "Toplearn"
if re.search(r'rn$', text):
    print(f"Example 1: '{text}' ends with 'rn'")
# $ anchors pattern to end of string

# Example 2: Ends with .py
filename = "script.py"
if re.search(r'\.py$', filename):
    print(f"Example 2: '{filename}' is a Python file")

# Example 3: Ends with digit
version = "v1.0"
if re.search(r'[0-9]$', version):
    print(f"Example 3: '{version}' ends with a digit")

# Example 4: Ends with period (escaped)
sentence = "Hello."
if re.search(r'\.$', sentence):
    print(f"Example 4: '{sentence}' ends with period")

# Example 5: Ends with uppercase letter
word = "HELLO"
if re.search(r'[A-Z]$', word):
    print(f"Example 5: '{word}' ends with uppercase letter")

# Example 6: Ends with newline
text = "line1\nline2\n"
if re.search(r'\n$', text):
    print(f"Example 6: Text ends with newline")

# Example 7: Ends with closing parenthesis
expr = "calc(42)"
if re.search(r'\)$', expr):
    print(f"Example 7: '{expr}' ends with closing parenthesis")

# Example 8: Ends with emoji
text = "Hello 👋"
if re.search(r'👋$', text):
    print(f"Example 8: '{text}' ends with emoji")
# Modern regex supports Unicode characters

# Example 9: Ends with whitespace (trailing spaces)
line = "text   "
if re.search(r'\s+$', line):
    print(f"Example 9: '{line}' has trailing whitespace")

# Example 10: Ends with semicolon
code = "print('hi');"
if re.search(r';$', code):
    print(f"Example 10: '{code}' ends with semicolon")

# Example 11: Multiline mode - $ matches end of each line
text = "first line\nsecond line\nthird line"
matches = re.findall(r'\w+$', text, re.MULTILINE)
print(f"Example 11: End of each line: {matches}")

# Example 12: Positive lookahead at end
text = "password123"
if re.search(r'(?<=\d)$', text):
    print(f"Example 12: '{text}' — ends after a digit")
# (?<=...) = positive lookbehind

```

## 🅱️ Escape

escaping special characters

```python
import re

# Example 1: Escape dot to match literal dot
text = "this is a book."
if re.search(r'book\.', text):
    print(f"Example 1: '{text}' contains 'book.' literally")
# Special characters: . ^ $ * + ? { } [ ] \ | ( )

# Example 2: Escape question mark
filename = "file?.txt"
if re.search(r'file\?.txt', filename):
    print(f"Example 2: '{filename}' contains literal ?")

# Example 3: Escape parentheses
text = "math(42)"
if re.search(r'math$$42$$', text):
    print(f"Example 3: '{text}' — parentheses escaped")

# Example 4: Escape asterisk
text = "size*large"
if re.search(r'size\*large', text):
    print(f"Example 4: '{text}' — asterisk escaped")

# Example 5: Escape plus
text = "a+b"
if re.search(r'a\+b', text):
    print(f"Example 5: '{text}' — plus escaped")

# Example 6: Escape square brackets
text = "list[item]"
if re.search(r'list$$item$$', text):
    print(f"Example 6: '{text}' — square brackets escaped")

# Example 7: Escape backslash (double backslash)
path = "C:\\Windows"
if re.search(r'C:\\\\Windows', path):
    print(f"Example 7: '{path}' — backslash escaped")
# In regex, \\ represents one literal backslash

# Example 8: Escape dollar sign
text = "price$100"
if re.search(r'price\$', text):
    print(f"Example 8: '{text}' — dollar sign escaped")

# Example 9: Escape caret
text = "start^end"
if re.search(r'start\^end', text):
    print(f"Example 9: '{text}' — caret escaped")

# Example 10: Escape pipe
text = "a|b"
if re.search(r'a\|b', text):
    print(f"Example 10: '{text}' — pipe escaped")

# Example 11: Escape using re.escape() function
special_chars = ".*+?^${}()|[]\\"
escaped = re.escape(special_chars)
print(f"Example 11: Escaped: {escaped}")
# re.escape() automatically escapes all special characters

# Example 12: Raw strings vs regular strings for escaping
pattern1 = r'\d+\.\d+'  # Raw string - preferred
pattern2 = '\\d+\\.\\d+'  # Regular string - harder to read
text = "3.14"
if re.search(pattern1, text) and re.search(pattern2, text):
    print(f"Example 12: Both patterns match '{text}'")
# Always use raw strings (r'') for regex patterns

```

## 🅱️ Set `[...]`

character sets

```python
import re

# Example 1: si[tdz]e → site, side, size
text = "site"
if re.search(r'si[tdz]e', text):
    print(f"Example 1: '{text}' matches si[tdz]e")

# Example 2: Find colors
text = "red green blue"
colors = re.findall(r'\b(red|green|blue)\b', text)
print(f"Example 2: Colors found: {colors}")

# Example 3: Find vowels
word = "hello"
vowels = re.findall(r'[aeiou]', word)
print(f"Example 3: Vowels in '{word}': {vowels}")

# Example 4: Find alphanumeric characters
text = "a1b2c3"
alphanum = re.findall(r'[a-zA-Z0-9]', text)
print(f"Example 4: Alphanumeric: {alphanum}")

# Example 5: Find special symbols
text = "a!b@c#"
symbols = re.findall(r'[!@#]', text)
print(f"Example 5: Symbols: {symbols}")

# Example 6: Find Persian characters (Unicode range)
text = "سلام دنیا"
persian = re.findall(r'[\u0600-\u06FF]', text)
if persian:
    print(f"Example 6: Persian characters: {''.join(persian)}")

# Example 7: Find letters a-f
text = "c"
if re.search(r'[a-f]', text):
    print(f"Example 7: '{text}' is in range a-f")

# Example 8: Find digits 0-5
text = "3"
if re.search(r'[0-5]', text):
    print(f"Example 8: '{text}' is in range 0-5")

# Example 9: Find uppercase letters A-Z
text = "M"
if re.search(r'[A-Z]', text):
    print(f"Example 9: '{text}' is uppercase")

# Example 10: Find non-digits
text = "abc123"
non_digits = re.findall(r'[^0-9]', text)
print(f"Example 10: Non-digits: {non_digits}")

# Example 11: Character class subtraction (Python doesn't support directly)
# Workaround using negative lookahead
text = "abc123def"
# Find letters that are not vowels
consonants = re.findall(r'(?![aeiou])[a-z]', text)
print(f"Example 11: Consonants: {consonants}")

# Example 12: POSIX character classes (not directly supported in Python)
# Use equivalent patterns
text = "Hello123 World!"
# \w equivalent for letters only
letters = re.findall(r'[[:alpha:]]', text)  # This won't work in Python
# Instead use:
letters = re.findall(r'[a-zA-Z]', text)
print(f"Example 12: Letters only: {letters}")

```

## 🅱️ Exclude `[^...]`

negated character sets

```python
import re

# Example 1: si[^tdz]e → siue, sibe, etc.
text = "siue"
if re.search(r'si[^tdz]e', text):
    print(f"Example 1: '{text}' matches si[^tdz]e")

# Example 2: Find words without letter 'a'
text = "hello world"
words = re.findall(r'\b[^a\W]+\b', text)
print(f"Example 2: Words without 'a': {words}")

# Example 3: Find non-whitespace characters
text = "a b c"
non_space = re.findall(r'[^ ]', text)
print(f"Example 3: Non-space: {non_space}")

# Example 4: Find non-alphanumeric characters
text = "a1! b2@"
specials = re.findall(r'[^a-zA-Z0-9]', text)
print(f"Example 4: Special characters: {specials}")

# Example 5: Find lines without period
line = "This is a line"
if re.search(r'^[^.]*$', line):
    print(f"Example 5: '{line}' has no period")

# Example 6: Find words without vowels
text = "dry myth"
consonants = re.findall(r'\b[^aeiou\W]+\b', text, re.IGNORECASE)
print(f"Example 6: Words without vowels: {consonants}")

# Example 7: Find non-ASCII characters
text = "café naïve"
non_ascii = re.findall(r'[^\x00-\x7F]', text)
print(f"Example 7: Non-ASCII characters: {non_ascii}")

# Example 8: Find non-Persian characters
text = "Hello سلام"
non_persian = re.findall(r'[^\u0600-\u06FF]', text)
print(f"Example 8: Non-Persian: {''.join(non_persian)}")

# Example 9: Find non-digits at start
text = "abc123"
if re.match(r'[^0-9]', text):
    print(f"Example 9: '{text}' starts with non-digit")

# Example 10: Find non-letters at end
text = "hello!"
if re.search(r'[^a-zA-Z]$', text):
    print(f"Example 10: '{text}' ends with non-letter")

# Example 11: Double negation
text = "abc123"
# Find characters that are NOT non-digits (i.e., digits)
digits = re.findall(r'[^0-9]', text)  # non-digits
actual_digits = re.findall(r'[^' + re.escape(''.join(digits)) + ']', text) if digits else []
print(f"Example 11: Double negation result: {actual_digits}")

# Example 12: Negated set with ranges
text = "abc123XYZ!@#"
# Find characters that are NOT letters or digits
non_alphanum = re.findall(r'[^a-zA-Z0-9]', text)
print(f"Example 12: Non-alphanumeric: {non_alphanum}")

```

## 🅱️ Repeat

repetition {n}, *, +, ?

```python
import re

# Example 1: {11} — exactly 11 digits
phone = "09123456789"
if re.match(r'[0-9]{11}', phone):
    print(f"Example 1: '{phone}' is exactly 11 digits")

# Example 2: ? — zero or one (optional 'u' in color/colour)
text = "color"
if re.search(r'colou?r', text):
    print(f"Example 2: '{text}' matches colou?r")

# Example 3: + — one or more
text = "goood"
if re.search(r'go+d', text):
    print(f"Example 3: '{text}' has one or more 'o's")

# Example 4: * — zero or more
text = "http://example.com"
if re.search(r'https?://', text):
    print(f"Example 4: '{text}' — 's' is optional")

# Example 5: {2,4} — between 2 and 4
text = "aa"
if re.search(r'a{2,4}', text):
    print(f"Example 5: '{text}' has 2-4 'a's")

# Example 6: {3,} — at least 3
text = "aaaa"
if re.search(r'a{3,}', text):
    print(f"Example 6: '{text}' has at least 3 'a's")

# Example 7: *? — non-greedy
text = "<b>bold</b> and <i>italic</i>"
tags = re.findall(r'<.*?>', text)
print(f"Example 7: Non-greedy tags: {tags}")

# Example 8: +? — non-greedy
text = "aabbcc"
matches = re.findall(r'a.+?c', text)
print(f"Example 8: Non-greedy matches: {matches}")

# Example 9: ?? — non-greedy for optional
text = "color"
matches = re.findall(r'colou??r', text)
print(f"Example 9: Non-greedy optional: {matches}")

# Example 10: {2,5}? — non-greedy range
text = "aaaaa"
matches = re.findall(r'a{2,5}?', text)
print(f"Example 10: Non-greedy range matches: {matches}")

# Example 11: Possessive quantifiers (not directly supported in Python)
# Python doesn't support a++ or a*+ syntax
# Workaround using atomic grouping (not available in standard re)
print("Example 11: Python doesn't support possessive quantifiers directly")

# Example 12: Complex repetition with groups
text = "ababab"
pattern = r'(ab)+'
match = re.search(pattern, text)
if match:
    print(f"Example 12: Matched: {match.group()}, Group: {match.group(1)}")

```

## 🅱️ Special characters

Special characters — \d, \w, \s etc.

```python
import re

# Example 1: \d — digit
text = "123"
if re.search(r'\d+', text):
    print(f"Example 1: '{text}' contains digits")

# Example 2: \D — non-digit
text = "abc"
if re.search(r'\D+', text):
    print(f"Example 2: '{text}' contains non-digits")

# Example 3: \s — whitespace
text = "a b"
if re.search(r'\s', text):
    print(f"Example 3: '{text}' contains whitespace")

# Example 4: \S — non-whitespace
text = "a b"
non_space = re.findall(r'\S', text)
print(f"Example 4: Non-whitespace: {non_space}")

# Example 5: \w — word character
text = "user_name123"
if re.fullmatch(r'\w+', text):
    print(f"Example 5: '{text}' contains only word characters")

# Example 6: \W — non-word character
text = "user@name"
special = re.findall(r'\W', text)
print(f"Example 6: Non-word characters: {special}")

# Example 7: \b — word boundary
text = "the theory"
matches = re.findall(r'\bthe\b', text)
print(f"Example 7: Complete word 'the': {matches}")

# Example 8: \B — non-word boundary
text = "theory"
if re.search(r'the\B', text):
    print(f"Example 8: '{text}' — 'the' not at word boundary")

# Example 9: \A — absolute start of string
text = "Hello\nWorld"
if re.search(r'\AHello', text):
    print(f"Example 9: '{text}' starts with Hello")

# Example 10: \Z — absolute end of string
text = "Hello\nWorld"
if re.search(r'World\Z', text):
    print(f"Example 10: '{text}' ends with World")

# Example 11: \b with Unicode
text = "café au lait"
matches = re.findall(r'\b\w+\b', text)
print(f"Example 11: Words with Unicode: {matches}")

# Example 12: Custom word boundaries for specific cases
text = "email@example.com"
# Find email without using \b (since . and @ are non-word chars)
pattern = r'(?<!\S)[\w.-]+@[\w.-]+\.[\w]{2,4}(?!\S)'
if re.search(pattern, text):
    print(f"Example 12: Found email with custom boundaries: {text}")

```

## 🅱️ `(abc|def)`

Grouping and alternation — (abc|def)

```python
import re

# Example 1: (abc|cde)
text = "abcdef"
if re.match(r'(abc|cde)', text):
    print(f"Example 1: '{text}' starts with abc")

# Example 2: Find days of week
text = "Monday Tuesday Friday"
days = re.findall(r'\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b', text)
print(f"Example 2: Days found: {days}")

# Example 3: Find colors with grouping
text = "red car, blue sky, green grass"
colors = re.findall(r'\b(red|blue|green)\b', text)
print(f"Example 3: Colors: {colors}")

# Example 4: Grouping for extraction
text = "John: 30, Jane: 25"
matches = re.findall(r'(\w+): (\d+)', text)
print(f"Example 4: Extracted name and age: {matches}")

# Example 5: Non-capturing group
text = "https://example.com"
match = re.search(r'(?:https?://)([\w.-]+)', text)
if match:
    print(f"Example 5: Domain: {match.group(1)}")

# Example 6: Named groups
text = "John: 30"
match = re.search(r'(?P<name>\w+): (?P<age>\d+)', text)
if match:
    print(f"Example 6: Name: {match.group('name')}, Age: {match.group('age')}")

# Example 7: Substitution with groups
text = "John Doe"
new_text = re.sub(r'(\w+) (\w+)', r'\2, \1', text)
print(f"Example 7: Substituted: {new_text}")

# Example 8: Using groups in substitution
text = "price: $100"
new_text = re.sub(r'\$(\d+)', r'USD \1', text)
print(f"Example 8: Substituted: {new_text}")

# Example 9: Nested grouping
text = "((a+b)*c)"
match = re.search(r'$$([$$a-zA-Z0-9+\-*/]+)$$', text)
if match:
    print(f"Example 9: Inside parentheses: {match.group(1)}")

# Example 10: Grouping for repetition
text = "ababab"
match = re.search(r'(ab)+', text)
if match:
    print(f"Example 10: Repeated group: {match.group(1)}")

# Example 11: Atomic grouping (not supported in standard Python re)
# Python's re module doesn't support atomic groups (?>...)
print("Example 11: Atomic grouping not supported in standard Python re")

# Example 12: Conditional groups (not supported in standard Python re)
# Python's re module doesn't support conditional patterns (?(id)yes|no)
print("Example 12: Conditional groups not supported in standard Python re")

```

## 🅱️ Email

advanced pattern such Email

```python
import re

# Example 1: Standard email pattern
text = "787jhjkj@test.com"
if re.match(r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print(f"Example 1: '{text}' is a valid email")

# Example 2: Email with + (Gmail)
text = "user+tag@gmail.com"
if re.match(r'^[\w\.\+\-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print(f"Example 2: '{text}' is valid Gmail with +")

# Example 3: Email with subdomain
text = "user@sub.domain.co.uk"
if re.match(r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print(f"Example 3: '{text}' has subdomain")

# Example 4: Email with numbers
text = "user123@domain.com"
if re.match(r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print(f"Example 4: '{text}' has numbers")

# Example 5: Invalid email — no @
text = "invalid.email.com"
if not re.match(r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print(f"Example 5: '{text}' is invalid (no @)")

# Example 6: Invalid email — no domain
text = "user@"
if not re.match(r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print(f"Example 6: '{text}' is invalid (no domain)")

# Example 7: Email with emoji — invalid
text = "user👋@domain.com"
if not re.match(r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print(f"Example 7: '{text}' is invalid (has emoji)")

# Example 8: Email with hyphen
text = "user-name@domain.com"
if re.match(r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print(f"Example 8: '{text}' has hyphen")

# Example 9: Email with 2-letter domain
text = "user@ir"
if re.match(r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print(f"Example 9: '{text}' has 2-letter domain")

# Example 10: Email with 5-letter domain — invalid
text = "user@domain.toolong"
if not re.match(r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print(f"Example 10: '{text}' has too long domain")

# Example 11: More robust email validation
email_pattern = r'''
    ^                           # Start of string
    (?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*
    |  "(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]
    |  \\[\x01-\x09\x0b\x0c\x0e-\x7f])*")
    @                           # @ symbol
    (?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?
    |  \[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
    (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-zA-Z0-9-]*[a-zA-Z0-9]:
    (?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]
    |  \\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])
    $                           # End of string
'''
text = "test@example.com"
if re.match(email_pattern, text, re.VERBOSE):
    print(f"Example 11: '{text}' matches robust email pattern")

# Example 12: Email validation with compile for performance
email_regex = re.compile(r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$')
emails = ["user@example.com", "invalid.email", "another@domain.org"]
valid_emails = [email for email in emails if email_regex.match(email)]
print(f"Example 12: Valid emails: {valid_emails}")

```

## 🅱️  `Search` vs `Match`

difference between Search vs Match

```python
import re

# Example 1: re.search — anywhere in string
names = ['data.png', 'memory.txt', 'data.txt', 'image.png', 'momy.png']
print("Example 1: Files containing 'm.m':")
for item in names:
    if re.search(r'm.m', item):
        print(f"  - {item}")

# Example 2: re.match — only at start of string
print("\nExample 2: Files starting with 'm.m':")
for item in names:
    if re.match(r'm.m', item):
        print(f"  - {item}")

# Example 3: re.fullmatch — entire string
text = "abc"
if re.fullmatch(r'abc', text):
    print(f"Example 3: '{text}' fully matches pattern")

# Example 4: re.findall — all matches
text = "a1 b2 c3"
digits = re.findall(r'\d', text)
print(f"Example 4: All digits: {digits}")

# Example 5: re.finditer — iterator with positions
text = "a1 b2 c3"
for match in re.finditer(r'\d', text):
    print(f"Example 5: Digit '{match.group()}' at position {match.start()}")

# Example 6: re.sub — substitution
text = "Hello 123 World 456"
new_text = re.sub(r'\d+', '#', text)
print(f"Example 6: Substituted: {new_text}")

# Example 7: re.split — splitting
text = "a,b;c:d"
parts = re.split(r'[,;:]', text)
print(f"Example 7: Split parts: {parts}")

# Example 8: re.compile — compiled pattern
pattern = re.compile(r'\d+')
text = "There are 123 apples and 456 oranges"
matches = pattern.findall(text)
print(f"Example 8: Compiled pattern matches: {matches}")

# Example 9: re.IGNORECASE — case insensitive
text = "Hello WORLD"
if re.search(r'world', text, re.IGNORECASE):
    print(f"Example 9: '{text}' contains 'world' (case insensitive)")

# Example 10: re.MULTILINE — multiline mode
text = "line1\nline2\nline3"
matches = re.findall(r'^line\d', text, re.MULTILINE)
print(f"Example 10: Multiline matches: {matches}")

# Example 11: re.DOTALL — dot matches newline
text = "first line\nsecond line"
matches = re.findall(r'first.*second', text, re.DOTALL)
print(f"Example 11: DOTALL matches: {matches}")

# Example 12: Combining multiple flags
text = "Line1\nLINE2\nline3"
pattern = re.compile(r'^line\d$', re.MULTILINE | re.IGNORECASE)
matches = pattern.findall(text)
print(f"Example 12: Combined flags matches: {matches}")

```

## 🅱️ Real-world application

Real-world application—file searching

```python
import re
import os
from pathlib import Path

# Example 1: Search for .py files in a directory
print("Example 1: .py files in /tmp (if accessible):")
try:
    py_files = []
    for root, dirs, files in os.walk('/tmp'):
        for file in files:
            if re.search(r'\.py$', file):
                py_files.append(file)
    for file in py_files[:5]:  # Show first 5 to avoid too much output
        print(f"  - {file}")
    if len(py_files) > 5:
        print(f"  ... and {len(py_files) - 5} more files")
except PermissionError:
    print("  - Permission denied to access /tmp")
except Exception as e:
    print(f"  - Error: {e}")

# Example 2: Search for log files
print("\nExample 2: Log files (.log):")
try:
    log_files = []
    for root, dirs, files in os.walk('/tmp'):
        for file in files:
            if re.search(r'\.log$', file, re.IGNORECASE):
                log_files.append(file)
    for file in log_files[:5]:
        print(f"  - {file}")
    if len(log_files) > 5:
        print(f"  ... and {len(log_files) - 5} more files")
except:
    pass

# Example 3: Search for image files
print("\nExample 3: Image files:")
image_pattern = re.compile(r'\.(jpg|jpeg|png|gif|bmp)$', re.IGNORECASE)
try:
    image_files = []
    for root, dirs, files in os.walk('/tmp'):
        for file in files:
            if image_pattern.search(file):
                image_files.append(file)
    for file in image_files[:5]:
        print(f"  - {file}")
    if len(image_files) > 5:
        print(f"  ... and {len(image_files) - 5} more files")
except:
    pass

# Example 4: Search for files with Persian characters in name
print("\nExample 4: Files containing 'report' in name:")
try:
    report_files = []
    for root, dirs, files in os.walk('/tmp'):
        for file in files:
            if re.search(r'report', file, re.IGNORECASE):
                report_files.append(file)
    for file in report_files[:5]:
        print(f"  - {file}")
    if len(report_files) > 5:
        print(f"  ... and {len(report_files) - 5} more files")
except:
    print("  - Could not search in /tmp")

# Example 5: Search for files with numeric names
print("\nExample 5: Files with purely numeric names:")
try:
    numeric_files = []
    for root, dirs, files in os.walk('/tmp'):
        for file in files:
            name = Path(file).stem
            if re.fullmatch(r'\d+', name):
                numeric_files.append(file)
    for file in numeric_files[:5]:
        print(f"  - {file}")
    if len(numeric_files) > 5:
        print(f"  ... and {len(numeric_files) - 5} more files")
except:
    pass

# Example 6: Search for files modified today (requires os.stat)
print("\nExample 6: Files modified today (conceptual):")
# This would require combining regex with os.stat
# For demonstration, showing the concept:
print("  - Concept: Use os.stat(file).st_mtime with datetime to filter")
print("  - Then apply regex patterns to filter by name")

# Example 7: Search for files larger than 1MB with specific extension
print("\nExample 7: Large .txt files (conceptual):")
print("  - Concept: Combine os.path.getsize() with regex pattern")
print("  - Pattern: r'\\.txt$' for .txt files")
print("  - Filter: size > 1024*1024 bytes")

# Example 8: Search for files with specific naming convention
print("\nExample 8: Files with YYYY-MM-DD format in name:")
date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
try:
    date_files = []
    for root, dirs, files in os.walk('/tmp'):
        for file in files:
            if date_pattern.search(file):
                date_files.append(file)
    for file in date_files[:5]:
        print(f"  - {file}")
    if len(date_files) > 5:
        print(f"  ... and {len(date_files) - 5} more files")
except:
    pass

# Example 9: Search for files excluding certain patterns
print("\nExample 9: Files NOT containing 'temp' in name:")
try:
    non_temp_files = []
    for root, dirs, files in os.walk('/tmp'):
        for file in files:
            if not re.search(r'temp', file, re.IGNORECASE):
                non_temp_files.append(file)
    print(f"  - Found {len(non_temp_files)} files not containing 'temp'")
    for file in non_temp_files[:3]:
        print(f"  - {file}")
except:
    pass

# Example 10: Search for files with multiple extensions
print("\nExample 10: Files with .py or .pyc extensions:")
try:
    python_files = []
    pattern = re.compile(r'\.pyc?$')
    for root, dirs, files in os.walk('/tmp'):
        for file in files:
            if pattern.search(file):
                python_files.append(file)
    for file in python_files[:5]:
        print(f"  - {file}")
    if len(python_files) > 5:
        print(f"  ... and {len(python_files) - 5} more files")
except:
    pass

# Example 11: Search for files with version numbers in name
print("\nExample 11: Files with version numbers (v1.0, v2.3.1, etc.):")
version_pattern = re.compile(r'v\d+(\.\d+)*')
try:
    version_files = []
    for root, dirs, files in os.walk('/tmp'):
        for file in files:
            if version_pattern.search(file):
                version_files.append(file)
    for file in version_files[:5]:
        print(f"  - {file}")
    if len(version_files) > 5:
        print(f"  ... and {len(version_files) - 5} more files")
except:
    pass

# Example 12: Search for files and extract information from names
print("\nExample 12: Extract dates from filenames like 'report_2024-01-15.pdf':")
date_extract_pattern = re.compile(r'report_(\d{4})-(\d{2})-(\d{2})\.pdf')
try:
    reports = []
    for root, dirs, files in os.walk('/tmp'):
        for file in files:
            match = date_extract_pattern.search(file)
            if match:
                year, month, day = match.groups()
                reports.append(f"{file} -> {year}-{month}-{day}")
    for report in reports[:5]:
        print(f"  - {report}")
    if len(reports) > 5:
        print(f"  ... and {len(reports) - 5} more reports")
except:
    pass

print("\n🎉 Congratulations! 144 practical and advanced examples of Regular Expressions in Python executed.")
```

# 13. 🅰️ Thread

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