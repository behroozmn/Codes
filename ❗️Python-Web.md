<div dir="rtl">

# 1. 🅰️ Django

## 🅱️ django.http.HttpResponse

* نمایش صفحه `HTML` با تولید دستی رشته‌های `HTML` در کد پایتون
* این روش هیچ تمپلیتی ندارد. شما کل `HTML` را به صورت رشته‌ای (string) در کد پایتون می‌نویسید و با `HttpResponse` آن را به مرورگر می‌فرستید.
* هرگز در پروژه واقعی استفاده نشود(زیرا نگهداری آن غیرممکن است)
*     سریع برای تست یک خطی
* نیازی به فایل تمپلیت ندارد

```python
from django.http import HttpResponse


def home_view(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head><title>صفحه اصلی</title></head>
    <body>
        <h1>سلام دنیا!</h1>
        <p>این صفحه کاملاً دستی نوشته شده است.</p>
        <footer>© 2025</footer>
    </body>
    </html>
    """
    return HttpResponse(html)
```

## 🅱️ HttpResponse+template

* نمایش صفحه با استفاده از فایل تمپلیت (.html) و پردازش دستی آن در پایتون
* قبل از `render()` اولین روش صحیح برای نماش صفحات در جنگو بود
* از قابلیت‌های تمپلیت جنگو(مثلا `{% for %}` یا `{{ variable }}`یا `{% if %}`) استفاده می‌کند
* منسوخ شده و با render() جایگزین شده است
* روش کار:
    1. یک فایل `HTML` جداگانه(تمپلیت) داریم
    2. از طریق `loader.get_template()` تمپلیت خوانده می‌شود
    3. داده های کد به آن داده می‌شود
    4. خروجی را در `HttpResponse` قرار میدهیم

ساختار پروژه به صورت زیر است

```
myproject/
├── myapp/
│   ├── views.py
│   ├── templates/
│   │   └── welcome.html
│   └── urls.py
└── settings.py
```

File: `welcome.html`

```html
<!DOCTYPE html>
<html>
<head><title>خوش آمدید</title></head>
<body>
<h1>سلام {{ name }}!</h1>
<p>سن شما: {{ age }} سال</p>
{% if hobbies %}
<ul>
    {% for hobby in hobbies %}
    <li>{{ hobby }}</li>
    {% endfor %}
</ul>
{% endif %}
</body>
</html>
```

File: `views.py`

```python
from django.http import HttpResponse
from django.template import loader


def welcome_view(request):
    # ۱. بارگذاری فایل تمپلیت
    template = loader.get_template('welcome.html')

    # ۲. تعریف داده‌هایی که به تمپلیت داده می‌شوند
    context = {
        'name': 'علی',
        'age': 28,
        'hobbies': ['فوتبال', 'کتاب', 'سفر']
    }

    # ۳. پر کردن تمپلیت با داده‌ها (render کردن)
    html = template.render(context, request)

    # ۴. ارسال به مرورگر
    return HttpResponse(html)
```

File: `url.py`

```python
from django.urls import path
from .views import welcome_view

urlpatterns = [
    path('', welcome_view, name='welcome'),
]
```

## 🅱️render()

</div>