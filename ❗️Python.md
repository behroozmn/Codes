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

# Example1️⃣️6️⃣️:
# Example1️⃣️7️⃣️:
# Example1️⃣️8️⃣️:
# Example1️⃣️9️⃣️:
# Example2️⃣️0️⃣️:
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

calc = Calculator() # حتی اگر شیء بسازید کار میکند ولی نیاز نیست
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
        return cls(first, last)  # 👈 cls همان Person است


p1 = Person("Ali", "Rezaei")
p2 = Person.from_full_name("Sara Ahmadi")  # ← روش جایگزین ساخت شیء

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

## 8.1. 🅱️ Read

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

## 8.2. 🅱️ Write

```python
# 242. mode:
# 243. a: append
# 244. w: read
# 245. r: write


with open("/tmp/salam.txt", encoding='UTF-8', mode="w") as bFile:
    bFile.write("STRIIIIIIIIIIIIIIIIIIIIIIIIIIING\n")

```

## 8.3. 🅱️ module os

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

## 8.4. 🅱️ Module Pathlib

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

## 8.5. 🅱️ Module shutil

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

# 9. 🅰️ JSON

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

# 10. 🅰️Database

## 10.1. 🅱️ SQLlight

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

* Need to`import re`

## 12.1. 🅱️ dot

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

## 12.2. 🅱️ ^

```shell
# 293. text = 'Toplearn'
# 294. 
# 295. if re.search('^Top', text):
# 296. print('this is ok')
```

## 12.3. 🅱️  $

```shell
# 297. text = 'Toplearn'
# 298. 
# 299. if re.search('rn$', text):
# 300. print('this is ok')
```

## 12.4. 🅱️ escape

```shell
# 301. text = 'this is a book.'
# 302. 
# 303. if re.search('book\.', text):
# 304. print('this is ok')
```

## 12.5. 🅱️ set

```shell
# 305. text = 'site'
# 306. 
# 307. if re.search('si[tdz]e', text):
# 308. print('this is ok')
```

## 12.6. 🅱️ range

```shell
# 309. text = 'c'
# 310. 
# 311. if re.search('[a-f]', text):
# 312. print('this is ok')
```

## 12.7. 🅱️ exclude

```shell
# 313. text = 'siue'
# 314. 
# 315. if re.search('si[^tdz]e', text):
# 316. print('this is ok')
```

## 12.8. 🅱️ repeat

```shell
# 317. text = '09123456789'
# 318. 
# 319. if re.match('[0-9]{11}', text):
# 320. print('this is ok')
```

## 12.9. 🅱️ other characters

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

## 12.10. 🅱️ email regex

```python
text = '787jhjkj@test.com'
if re.match('^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print('email is valid')
```

## 12.11. 🅱️ Search

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