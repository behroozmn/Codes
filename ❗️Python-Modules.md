<div dir="rtl">

# 1. 🅰️ `__init__.py`

* یک فولدر(دایرکتوری) حاوی فایل __init__.py بعنوان یک package(بسته) شناخته می‌شود و بدون این فایل پایتون نمی‌تواند دایرکتوری را به‌عنوان یک بسته شناسایی کند
* هرگاه یک بسته(ماژول) import شود، آنگاه کد داخل این فایل به منظور راه‌انداز(پیکربندی ماژول‌ها) اجرا می‌شود
* وقتی یک package ایمپورت می‌شود، فایل __init__.py اولین چیزی است که اجرا می‌شود

## 1.1. 🅱️ مزیت‌های Package بودن یک دایرکتوری

* فولدر می‌تواند شامل ماژول‌های دیگر یعنی FileName.py های دیگر باشد
* فولدر می‌تواند حاوی sub-packageهای دیگر باشد
* می‌توانید از importهای نسبی (relative imports) و ساختارهای پیچیده‌تر استفاده کنید
* سازماندهی و مدیریت ماژول‌ها و زیر بسته‌ها
* می‌توان initialization code را به اجرا درآورد تا در هنگام استفاده بصورت پیش‌فرض به اجرا درآید

**اگر یک دایرکتوری بسته یا Package نباشد**

* یک فولدر حتی بدون __init__.py هم می‌تواند package باشد (implicit namespace package) که در پایتون 3.3 به بعد ممکن شده است اما در این صورت import نسبی (from . import ...) کار نمی‌کند.
* نمی‌توانید از __all__ کدهای اولیه‌سازی استفاده کنید.

## 1.2. 🅱️ Example

فرض کنید دایرکتوری حاوی نظام و ساختارفایل زیر است

```
myproject/
│
├── main.py
└── mypackage/
    ├── __init__.py
    ├── module_a.py
    └── module_b.py
``` 

باوجود `__init__.py` در `main.py` می‌توانید بنویسید:

```python
from mypackage import module_a
``` 

و در فایل `module_a.py` می‌توانید بنویسید

```python
from . import module_b  # import نسبی
```

💡 بدون __init__.py، این . (نقطه) در import نسبی کار نمی‌کند.

## 1.3. 🅱️ کدنویسی دراین فایل

* هر بار این بسته مورد استفاده قرار بگیرد آنگاه لاگ بیاندازد که فلان بسته مورد استفاده قرار گرفته است

```python
print("Package is being imported!")
```

# 2. 🅰️ `__all__`

* یک لیست از رشته‌ها (strings)  است که نام متغیرها، توابع، یا کلاس‌هایی هستند که وقتی از یک ماژول یا package از طریق import * استفاده می‌کنید، وارد می‌شوند
* قابلیت تعریف کردن در ۱-فایل‌های .py (ماژول) و ۲-در فایل __init__.py (package)

**دلایل استفاده**

* کنترل دقیق بر روی آنچه قابل ایمپورت است
    * هنگام عدم استفاده از __all__ درهنگام import * تمام نام‌های عمومی یا PublicNames داخل ماژول ایمپورت می‌شوند
    * منظور از PublicNames ها مواردی است که با آندرلاین شروع **نمی‌شوند** (توابع یا کلاس‌ها و متغیرها)
* عدم آلودگی namespace
    * وقتی import * می‌کنید، تمام نام‌ها به scope فعلی وارد می‌شوند. این می‌تونه باعث تداخل نام‌ها بشه.
    * با استفاده از __all__ می‌تونی دقیق مشخص کنی که چه چیزهایی قراره وارد بشن.

## 2.1. 🅱️ نحوه تعریف

* عبارت __all__ حتما باید در انتها تعریف شود

فرض کنید یک بسته با محتوی زیر دارد

```python
# mymodule.py

def greet():
    print("Hello")


def goodbye():
    print("Goodbye")


class Person:
    pass


__all__ = ['greet', 'Person']
```

حالا وقتی بنویسید:

```python
from mymodule import *
```

فقط greet و Person ایمپورت می‌شوند.

# 3. 🅰️ mathGraph

```python
import matplotlib.pyplot as plot

xs = [2, 4, 6, 8, 20, 21, 22, 28, 4]
ys = [1, 3, 5, 8, 9, 12, 20, 30, 4]
plot.plot(xs, ys)
plot.show()
```

# 4. 🅰️ pyfiglet

- نمایش متن بصورت AsciiArt یعنی همانند خروجی دستور cowsay در لینوکس
- ترکیب آن با termcolor بسیار مفید خواهد شد

```python
import pyfiglet

print(pyfiglet.figlet_format(message))
```

```python
#!/usr/bin/env python
import pyfiglet
from termcolor2 import colored

ascii_art = pyfiglet.figlet_format("Hello")
ascii_art = colored(ascii_art, color="red")
print(ascii_art)
```

# 5. 🅰️ termcolor

* ماژولی برای رنگ آمیزی خروجی

```python
import termcolor

# help(termcolor) 

print(termcolor.colored('python course', color="white", on_color="on_magenta", attrs=["blink"]))
print(termcolor.colored('python course', color="green"))
print(termcolor.colored('python course', color="blue"))
print(termcolor.colored('python course', color="cyan"))

```

# 6. 🅰️ JsonResponse

```
return JsonResponse(Items.to_dict(), safe=False)
```

* توضیحات safeکه بصورت پیش‌فرض True است
    * اگر safe=Trueباشد آنگاه JsonResponse فقط مجاز است یک dict را بگیرد. یعنی اگر یک لیست یا نوع دیگری بفرستید، Django یک خطا می‌ده
    * اگر safe=False باشد
        * آنگاه اجازه می‌دهیم هر نوع object قابل سریالایز شدن JSON (مثل لیست , namedtuple , custom class ) را هم برگردانیم.
        * در این حالت، JsonResponse فرض می‌کند که شما مسئول مدیریت خروجی هستید.

# 7. 🅰️ Install Offline

## 7.1. 🅱️  [install from local Archive](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-local-archives)

### 7.1.1. ✅️ روش اول

```shell
mkdir /tmp/download
vim /tmp/requirements.txt
- wadllib==1.3.6
- webcolors==1.11.1
- webencodings==0.5.1
- websocket-client==1.2.3
- Werkzeug==2.2.2
cd download
pip download -r /tmp/requirements.txt
python3 -m pip install --no-index --find-links=file:///tmp/download wadllib webcolors webencodings websocket-client Werkzeug

```

### 7.1.2. ✅️ روش دوم

```shell
python3 -m pip install ./downloads/SomeProject-1.0.4.tar.gz
python3 -m pip install --no-index --find-links=file:///local/dir/ SomeProject
python3 -m pip install --no-index --find-links=/local/dir/ SomeProject
python3 -m pip install --no-index --find-links=relative/dir/ SomeProject
```
### 7.1.3. ✅️ روش سوم

* برای نصب دستی یک بسته ابتدا آن را دانلود کرده و سپس به پوشه مورد نظر رفته و مطابق دستور زیر نصب نمایید(به فایل توضیحی همراه بسته توجه گردد)
    ```python
    python setup.py install --user --prefix=~
    ```

## 7.2. 🅱️ Installer

* تولید یک فایل اجرایی برنامه پایتون(اکسپورت فایل اجرایی از تمام پکیج‌ها و لایبرری‌ها و مشتقات برنامه نوشته شده)
    ```python
    pyinstaller --onefile --windowed <MainScript.py>
    ```

# 8. 🅰️ requests

## 8.1. 🅱️ Get

```python
import requests

res1 = requests.get("https://barnamenevisan.info/api/courses/getactivecourses")
res2 = requests.get("https://jsonplaceholder.typicode.com/comments", params={'postId': 2})

# 1)
print(f"[res1.status_code]: {res1.status_code}\n\n")

# 2)
print(f"[res1.text]:{res1.text}\n\n")  # string

# 3)
for course in res1.json():
    print(f"Curse:{course['title']} Teacher: {course['teacher']}")

# 4)
print(f"[res2.json()]: {res2.json()}")

```

## 8.2. 🅱️ Post

```python
import requests

res1 = requests.post("https://jsonplaceholder.typicode.com/posts")
res2 = requests.get("https://jsonplaceholder.typicode.com/comments", params={'postId': 2})

print(f"[res1.json()]: {res1.json()}\n")
print(f"[res2.json()]: {res2.json()}\n\n")

for data in res1.json():
    print(f"[data]: {data}")

```

# 9. 🅰️ BaseHTTPRequestHandler and HTTPServer

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # تنظیم کد وضعیت پاسخ
        self.send_response(200)
        self.send_header('Content-type', 'text/plain;charset=utf-8')  # استفاده از text/plain
        self.end_headers()

        # نوشتن محتوای پاسخ با خط جدید
        response = "Requested path: {}\n".format(self.path)
        response += "This is a new line.\n"  # اضافه کردن خط جدید
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        # تنظیم کد وضعیت پاسخ
        self.send_response(200)
        self.send_header('Content-type', 'application/json;charset=utf-8')
        self.end_headers()

        # محتوای پاسخ
        response = {
            'message': 'این یک پاسخ از سمت سرور است به درخواست POST شما'
        }
        self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):
    server_address = ('', port)  # گوش دادن به همه آدرس‌ها
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
```

</div>