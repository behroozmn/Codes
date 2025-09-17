<div dir="rtl">

# 1. 🅰️BasicRenderingMethods

## 1.1. 🅱️django.http.HttpResponse

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

## 1.2. 🅱️HttpResponse+template(context)

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
    <li>{{ activity }}</li>
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
    template = loader.get_template('welcome.html')  # ۱. بارگذاری فایل تمپلیت
    context = {  # ۲. تعریف داده‌هایی که به تمپلیت داده می‌شوند
        'name': 'علی',
        'age': 28,
        'hobbies': ['فوتبال', 'کتاب', 'سفر']
    }
    html = template.render(context, request)  # ۳. پر کردن تمپلیت با داده‌ها (render کردن)
    return HttpResponse(html)  # ۴. ارسال به مرورگر
```

File: `url.py`

```python
from django.urls import path
from .views import welcome_view

urlpatterns = [
    path('', welcome_view, name='welcome'),
]
```

## 1.3. 🅱️django.shortcuts.render()

* render() یک تابع کمکی (helper function) است که در جنگو برای ساده‌سازی نمایش صفحات HTML طراحی شده است.

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
    {% for activity in activities %}
    <li>{{ hobby }}</li>
    {% endfor %}
</ul>
{% endif %}
</body>
</html>
```

File: `views.py`

```python
from django.shortcuts import render


def welcome_view(request):
    context = {
        'name': 'محمد',
        'age': 30,
        'activities': ['دویدن', 'شنا', 'گیتار']
    }
    return render(request, 'welcome.html', context)
```

File: `url.py`

```python
from django.urls import path
from .views import welcome_view

urlpatterns = [
    path('', welcome_view, name='welcome'),
]
```

نکته حالت های متفاوت ممکن است به صورت زیر باشد

```python
render(request, template_name, context=None, content_type=None, status=200, using=None)  # content_type default is text/html
render(request, 'welcome.html', context=None)
render(request, 'feed.xml', context, content_type='application/xml')
```

## 1.4. 🅱️Http404

```python

from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string

days = {'saturday': 'شنبه', 'sunday': 'یکشنبه', 'monday': 'دوشنبه', 'tuesday': 'سه‌شنبه', 'wednesday': 'چهارشنبه', 'thursday': 'پنج‌شنبه', 'friday': 'جمعه'}


def func(reqeust, day):
    day_data = days.get(day)

    if day_data is None:  # if not some_condition:
        # روش اول
        raise Http404  # اتوماتیک در پوشه تمپلیت دنبال فایل با نام ۴۰۴ می‌گردد

        # روش دوم
        response_data = render_to_string('404.html')
        return HttpResponseNotFound(response_data)

        # روش سوم
        return render(request, '404.html', status=404)

    context = {
        "day": f'selected DAY is {day}',
        "data": day_data
    }
    return render(reqeust, 'page.html', context)
```

# 2. 🅰️TemplateTag

جنگو از یک Template Engine مبتنی بر HTML + متغیرها + تگ‌ها + فیلترها استفاده می‌کند. این ماشین، فایل `.html` را پردازش می‌کند، متغیرها را جایگزین می‌کند، و دستورات تگ‌ها را اجرا می‌نماید(و نهایتاً HTML خالص تولید می‌کند).

## 2.1. 🅱️Tag

| دسته                 | تگ‌های ضروری                                        | کاربرد                                     |
|----------------------|-----------------------------------------------------|--------------------------------------------|
| **شرطی**             | `{% if %}`, `{% else %}`, `{% elif %}`              | نمایش محتوا بر اساس شرط                    |
| **حلقه**             | `{% for %}`, `{% empty %}`                          | پیمایش لیست‌ها و مدیریت حالت خالی          |
| **متغیرها**          | `{% with %}`, `{% get_current_time ... as today %}` | ذخیره مقدار موقت برای بهینه‌سازی           |
| **قالب‌بندی**        | `{% now %}`                                         | نمایش زمان فعلی                            |
| **توابع تکرارپذیر**  | `{% include %}`, `{% extends %}`, `{% block %}`     | ساخت قالب‌های قابل بازاستفاده و مادر-فرزند |
| **امنیت و فرم‌ها**   | `{% csrf_token %}`                                  | امنیت فرم‌های POST                         |
| **فایل‌های استاتیک** | `{% load static %}`, `{% static %}`                 | لینک به CSS/JS/تصاویر                      |
| **آدرس‌ها**          | `{% url %}`                                         | ایجاد لینک‌های پویا بدون Hardcode          |
| **کش**               | `{% cache %}`                                       | بهبود عملکرد با کش کردن قطعات سنگین        |
| **کامنت / خطایابی**  | `{% comment %}`, `{% debug %}`                      | نوت‌نویسی و رفع اشکال در توسعه             |
| **فضای سفید**        | `{% spaceless %}`                                   | کاهش حجم HTML با حذف فاصله‌های اضافی       |

### 2.1.1. ✅️BasePage(block)

* همه نام‌های masterPage یا MainPage یا BasePage یا LayoutePage به یک مفهوم اشاره دارند
* ایجاد یک صفحه‌اصلی(صفحه پیش‌فرض)تا بقیه صفحات از آن مشتق شود و در ادامه بتوان توسط تگ‌های دلخواه هر صفحه قابلیت سفارشی‌سازی محقق شود
* فایل `base.html` باید در مسیر  `template` قرار گرفته باشد تا قابلیت شناخته شدن داشته باشد
* دایرکتوری template باید در فایل `setting.py` بعنوان مسیر پیش‌فرض تمپلیت‌های پروژه لحاظ شده باشد
* هرصفحه‌ای که ازاین صفحه ارث‌بری نماید، بااستفاده از نام بلاک‌های ذیل، می‌تواند دیتای سفارشی همان صفحه را در محتوی بلاک‌ها درج نمود
* یک تمپلیت پایه (base) داشته باشید، و تمام صفحات دیگر از آن وراثت ببرند(فقط بخش‌های خاص خود را جایگزین کنند)
* کاهش تکرار کد

File: `templates/basePage.html`

```html
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}وبسایت من{% endblock %}</title>  <!-- 👈️  -->

    <!-- Share CSS -->
    <link rel="stylesheet" href="{% static 'css/main.css' %}">

    <!-- Special CSS -->
    {% block extra_css %}{% endblock %}  <!-- 👈️  -->
</head>
<body>
<nav class="navbar">
    <a href="/">خانه</a>
    <a href="/about/">درباره</a>
    <a href="/contact/">تماس</a>
    {% if user.is_authenticated %}
    <span>سلام {{ user.username }}!</span>
    <a href="/logout/">خروج</a>
    {% else %}
    <a href="/login/">ورود</a>
    {% endif %}
</nav>

<main>
    {% block content %}{% endblock %} <!-- 👈️ محتوای اصلی — جایی که فرزندان جایگزین می‌کنند -->

</main>


<footer>
    <!-- Special Footer -->
    {% block footer %}{% endblock %}#  <!-- 👈️  -->

    <!-- Share Footer -->
    &copy; 2025 وبسایت من — تمامی حقوق محفوظ است.
</footer>

<!--  Share JS -->
<script src="{% static 'js/jquery.min.js' %}"></script>

<!--  Special JS -->
{% block extra_js %}{% endblock %}   <!-- 👈️  -->
</body>
</html>
```

* `block title` می‌تواند در هر صفحه تغییر کند
* `block content` حتما در «صفحه‌لایه‌پایین‌تر» تکمیل خواهد شد
* اختیاری: `block extra_css` و  `extra_js` برای صفحات نیازمند سفارشی‌سازی
* [URL](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#block)

### 2.1.2. ✅️subPage(extends)

«صفحه‌لایه‌پایین‌تر» که از «صفحه‌اصلی» ارث‌بری میکند و تمام صفحات یک ساختار واحد خواهند داشت(ولی هر کدام محتوا، استایل و اسکریپت خاص خود را دارند)

* هرآنچه در محتوی `block` قرارمیدهید جایگزین می‌شود
* از `extends` فقط برای ساختار اصلی استفاده کنید,نه برای بخش‌های کوچک!

File: `templates/products/product_detail.html`

```html
{% extends 'basePage.html' %} <!-- 👈️  -->

{% block title %}جزئیات محصول — {{ product.name }}{% endblock %} <!-- 👈️  -->

{% block content %} <!-- 👈️  -->
<article>
    <h1>{{ product.name }}</h1>
    <p><strong>قیمت:</strong> {{ product.price }} تومان</p>
    <img src="{{ product.image.url }}" alt="{{ product.name }}">
    <p>{{ product.description }}</p>

    <button id="add-to-cart">افزودن به سبد</button>
</article>
{% endblock %}

{% block extra_css %} <!-- 👈️  -->
<link rel="stylesheet" href="{% static 'css/product-detail.css' %}">
{% endblock %}

{% block extra_js %} <!-- 👈️  -->
<script src="{% static 'js/product-detail.js' %}"></script>
<script>
    document.getElementById('add-to-cart').addEventListener('click', () => {
        alert('محصول به سبد اضافه شد!');
    });
</script>
{% endblock %}
```

* `{% extends %}`:اعلام وراثت از `basePage.html`
* `{% block title %}`:جایگزینی عنوان صفحه(بدون تأثیر روی سایر صفحات)
* `{% block content %}`:حتماً باید پر شود(اگر نشود، خطا می‌دهد در جنگو ۴.۲+)
* `{% block extra_css %}`:اختیاری(فقط وقتی نیاز دارید، پر می‌شود)
* `{% block extra_js %}`:اختیاری برای اسکریپت‌های صفحه‌محور(فقط وقتی نیاز دارید، پر می‌شود)

File: `view.py`

```python
from django.shortcuts import render


def index(request):
    return render(request, 'subPage1.html')
```

#### 2.1.2.1. ❇️block.super

اگر از کلمه کلیدی  `block.super` استفاده نمایید محتوی والد حفظ خواهد شد و تنها محتوی به بلاک «صفحه‌لایه‌پایین‌تر» افزوده خواهد شد

File: `templates/base.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}سایت من{% endblock %}</title>
    <link href="{% static 'css/global.css' %}" rel="stylesheet">
</head>
<body>
<header>...</header>
<main>{% block content %}{% endblock %}</main>
<footer>...</footer>
{% block scripts %}
<script src="{% static 'js/main.js' %}"></script>
{% endblock %}
</body>
</html>
```

File: `templates/admin/base_admin.html`

```html
{% extends "base.html" %}

{% block title %}پنل مدیریت — {% block admin_title %}{% endblock %}{% endblock %}

{% block content %}
<div class="admin-wrapper">
    <aside class="sidebar">
        {% include "admin/_sidebar.html" %}
    </aside>
    <section class="admin-content">
        {% block admin_content %}{% endblock %}
    </section>
</div>
{% endblock %}

{% block scripts %}
{{ block.super }}
<script src="{% static 'js/admin.js' %}"></script>
{% endblock %}
```

File: `templates/admin/dashboard.html`

```html
{% extends "admin/base_admin.html" %}

{% block admin_title %}داشبورد{% endblock %}
{% block admin_content %}
<h2>آمار کلی</h2>
<p>تعداد کاربران: {{ user_count }}</p>
<p>سفارشات امروز: {{ orders_today }}</p>
{% endblock %}
```

### 2.1.3. ✅️Include

* تهیه بخش های متفاوت از تکه‌ها صفحه و استفاده در صفحه اصلی یا هر صفحه دلخواه
* نکته: بلوک `include` معمولا در بدنه یعنی `Content` مورد استفاده قرار می‌گیرد
* ترکیب یک فایل تمپلیت دیگر در داخل فایل فعلی
* هدف:کاهش تکرار بخش‌های کوچک (مثل منو، فرم، کارت محصول، کامنت)
* مدیریت مستقل بخش‌ها(هر کدام یه فایل جداگانه)
* همواره یک پوشه برای `include` داشته باشید
* از `include` برای همه چیزهای تکراری استفاده کنید,فوتر، ناوبری، فرم‌ها، کارت‌ها، کامنت‌ها
* Standard Name: `*_form.html` or `*_card.html` or `*_list.html` or `*_modal.html`

File: `templates/includes/login_form.html`

```html

<form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    <div>
        <label for="username">نام کاربری:</label>
        <input type="text" name="username" id="username" required>
    </div>
    <div>
        <label for="password">رمز عبور:</label>
        <input type="password" name="password" id="password" required>
    </div>
    <button type="submit">ورود</button>
    {% if form.errors %}
    <p style="color: red;">نام کاربری یا رمز عبور اشتباه است.</p>
    {% endif %}
</form>
```

File: `templates/registration/login.html` صفحه ورود

```html
{% extends "basePage.html" %}

{% block content %}
<h1>ورود به سایت</h1>
{% include "includes/login_form.html" %}
{% endblock %}
```

File: `templates/home.html` صفحه اصلی(فرم ورود در فوتر)

```html
{% extends "basePage.html" %}

{% block content %}
<h1>خوش آمدید!</h1>
<p>برای دسترسی به بخش‌های ویژه، وارد شوید.</p>
{% endblock %}

{% block footer %}
<div class="footer-login">
    <h4>وارد شوید:</h4>
    {% include "includes/login_form.html" %}
</div>
{% endblock %}
```

#### 2.1.3.1. ❇️Context(with)

* قابلیت انتقال دیتا از طریق کلمه کلیدی `with` در سازوکار `include` وجود دارد
* همیشه از `with` استفاده کنید(حتی اگر متغیر موجود است تا از عدم شفافیت جلوگیری کنید)

File: `templates/products/list.html` (لیست محصولات)

```html
{% extends "basePage.html" %}

{% block content %}
<h1>محصولات</h1>
<div class="products-grid">
    {% for product in products %}
    {% include "includes/product_card.html" with product=product %}
    {% endfor %}
</div>
{% endblock %}
```

File: `templates/includes/product_card.html`

```html

<div class="product-card">
    <img src="{{ product.image.url }}" alt="{{ product.name }}">
    <h3>{{ product.name }}</h3>
    <p class="price">{{ product.price|default:"ناموجود" }}</p>
    {% if product.in_stock %}
    <button class="btn-buy">خرید</button>
    {% else %}
    <button class="btn-disabled" disabled>ناموجود</button>
    {% endif %}
</div>
```

توضیحات:

* `with product=product` متغیر `product` را فقط برای این `include` تعریف می‌کند.
* بدون `with` اگر `product` در کانتکست والد وجود نداشته باشد، خطا می‌دهد

#### 2.1.3.2. ❇️ContextWith(only)

* فقط متغیرهایی که با `with` به همراه `=`  و  `only` تعریف کردید در تمپلیت داخلی در دسترس هستند.
* بقیه متغیرهای والد حذف می‌شوند
* کاربرد امنیت: نمی‌خواهید یه user یا request از صفحه والد به داخل include نفوذ کند.
* کاربرد پاکیزگی: مطمئن شوید که include فقط چیزی که لازم دارد را می‌بیند.
* کاربرد تست‌پذیری: می‌توانید include را به صورت مستقل تست کنید.

File: `templates/includes/comment_list.html`

```html

<ul class="comment-list">
    {% for comment in comments %}
    <li>{{ comment.text }} — {{ comment.author }}</li>
    {% endfor %}
</ul>
```

File: `templates/post/detail.html`

```html
{% extends "basePage.html" %}

{% block content %}
<article>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
</article>

<!-- فقط کامنت‌ها را نمایش بده — بدون دسترسی به متغیرهای دیگر -->
{% include "includes/comment_list.html" with comments=post.comments.all only %}
{% endblock %}
```

## 2.2. 🅱️Filter

فیلتر(Filter) یک تابع ساده است که یک مقدار(value) را دریافت می‌کند، آن را پردازش می‌کند، و یک خروجی جدید برمی‌گرداند

* فیلترها همیشه رشته برمی‌گردانند
* اگر بخواهید HTML را رندر کنید(حتماً `|safe` را اضافه کنید.)

```
Syntax: {{ variable|filter_name:argument }}
```

| گروه                                                  | عناصر                                                                                                                                                                 |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **رشته‌ها (String Manipulation)**                     | `upper`, `lower`, `title`, `capfirst`, `slugify`, `truncatechars`, `truncatewords`, `truncatewords_html`, `escape`, `safe`, `linebreaks`, `linebreaksbr`, `striptags` |
| **اعداد (Number Operations)**                         | `floatformat`, `add`, `sub`, `multiply`, `divide`, `mod`, `abs`, `intcomma`                                                                                           |
| **لیست‌ها و آرایه‌ها (List/Array Operations)**        | `length`, `join`, `slice`, `first`, `last`, `random`, `dictsort`, `dictsortreversed`                                                                                  |
| **امنیت و HTML (Security & XSS)**                     | `escape`, `safe`, `striptags`                                                                                                                                         |
| **تاریخ و زمان (Date & Time Formatting)**             | `date`, `time`, `timesince`, `timeuntil`, `naturalday`, `naturaltime`                                                                                                 |
| **مقادیر پیش‌فرض و جایگزینی (Defaults & Fallbacks)**  | `default`, `default_if_none`, `yesno`                                                                                                                                 |
| **جمع‌بندی و صرفه‌جویی (Pluralization & Conversion)** | `pluralize`, `phone2numeric`                                                                                                                                          |
| **حذف و اصلاح تگ‌های خاص (Tag Filtering)**            | `removetags`                                                                                                                                                          |

```
## Examples:
# ╔═════════╗
# ║ STRING  ║   ← String Manipulation
# ╚═════════╝

{{ name|upper }} ← change all characters to uppercase
input:"ali reza" ▶️ "ALI REZA"

{{ name|lower }} ← change all characters to lowercase
input:"HELLO WORLD" ▶️ "hello world"

{{ name|title }} ← capitalize first letter of each word
input:"john doe" ▶️ "John Doe"

{{ name|capfirst }} ← capitalize only the first character of the string
input:"john doe" ▶️ "John doe"

{{ name|slugify }} ← convert string to URL-safe slug (replace spaces with hyphens, remove special chars)
input:"Hello, World! 2025" ▶️ "hello-world-2025"

{{ name|truncatechars:10 }} ← truncate string to 10 characters and append "…"
input:"This is a very long text" ▶️ "This is a…"

{{ name|truncatewords:3 }} ← truncate string to 3 words and append "…"
input:"The quick brown fox jumps over the lazy dog" ▶️ "The quick brown…"

{{ name|truncatewords_html:3 }} ← truncate to 3 words while preserving HTML tags
input:"<p>Hello <strong>World</strong></p>" ▶️ "<p>Hello <strong>World</strong>…</p>"

{{ name|escape }} ← escape HTML characters to prevent XSS attacks
input:"<script>alert('XSS')</script>" ▶️ "<script>alert(&#x27;XSS&#x27;)</script>"

{{ name|safe }} ← render raw HTML (use only if content is trusted)
input:"<strong>Bold Text</strong>" ▶️ "<strong>Bold Text</strong>"

{{ name|linebreaks }} ← convert newlines (\n) to <p> tags
input:"Line 1\nLine 2\nLine 3" ▶️ "<p>Line 1</p><p>Line 2</p><p>Line 3</p>"

{{ name|linebreaksbr }} ← convert newlines (\n) to <br> tags
input:"Line 1\nLine 2" ▶️ "Line 1<br>Line 2"

{{ name|striptags }} ← remove all HTML tags, keep only text
input:"<p>Hello <b>World</b></p><script>malicious()</script>" ▶️ "Hello World"


# ╔══════════╗
# ║ NUMBERS  ║   ← Number Operations
# ╚══════════╝

{{ price|floatformat:2 }} ← round number to 2 decimal places
input:3.14159 ▶️ "3.14"

{{ price|floatformat:"-2" }} ← remove trailing zeros from decimal
input:5.000 ▶️ "5"

{{ number|add:5 }} ← add the given number to the value
input:10 ▶️ 15

{{ number|sub:3 }} ← subtract the given number from the value (Django 3.2+)
input:10 ▶️ 7

{{ number|multiply:4 }} ← multiply the value by the given number
input:6 ▶️ 24

{{ number|divide:2 }} ← divide the value by the given number (Django 3.2+)
input:12 ▶️ 6

{{ number|mod:5 }} ← return remainder after division by the given number (Django 3.2+)
input:17 ▶️ 2

{{ number|abs }} ← return absolute value
input:-7 ▶️ 7

{{ price|intcomma }} ← add commas as thousands separators (e.g., for USD/EUR)
input:1000000 ▶️ "1,000,000"


# ╔════════════════╗
# ║ ARRAY or LIST  ║  ← List/Array Operations
# ╚════════════════╝

{{ items|length }} ← return number of items in list
input:["apple", "banana", "cherry"] ▶️ 3

{{ items|join:", " }} ← join list elements with specified separator
input:["a", "b", "c"] ▶️ "a, b, c"

{{ items|slice:":2" }} ← slice list from start to index 2 (like Python [0:2])
input:["a", "b", "c", "d"] ▶️ ["a", "b"]

{{ items|slice:"1:3" }} ← slice list from index 1 to 3
input:["a", "b", "c", "d"] ▶️ ["b", "c"]

{{ items|slice:"::-1" }} ← reverse the list
input:["a", "b", "c"] ▶️ ["c", "b", "a"]

{{ items|first }} ← return the first item of the list
input:["a", "b", "c"] ▶️ "a"

{{ items|last }} ← return the last item of the list
input:["a", "b", "c"] ▶️ "c"

{{ items|random }} ← return a random item from the list (Django 2.2+)
input:["red", "green", "blue"] ▶️ "green"

{{ users|dictsort:"name" }} ← sort list of dictionaries by the given key
input:[{"name":"Zahra"},{"name":"Ali"}] ▶️ [{"name":"Ali"},{"name":"Zahra"}]

{{ users|dictsortreversed:"age" }} ← sort list of dictionaries by key in descending order
input:[{"name":"Ali","age":20},{"name":"Zahra","age":25}] ▶️ [{"name":"Zahra","age":25},{"name":"Ali","age":20}]


# ╔═══════════╗
# ║ SECURITY  ║ ← Security & XSS Prevention
# ╚═══════════╝

{{ user_input|escape }} ← escape HTML to prevent XSS attacks (Django does this by default)
input:"<script>alert('XSS')</script>" ▶️ "<script>alert(&#x27;XSS&#x27;)</script>"

{{ html_content|safe }} ← render unescaped HTML (use only with trusted content)
input:"<strong>Important</strong>" ▶️ "<strong>Important</strong>"

{{ html_with_script|striptags }} ← remove all HTML tags, keep only plain text
input:"<p>Hello</p><script>evil()</script>" ▶️ "Hello"


# ╔══════════╗
# ║ DATE/TIME ║   ← Date & Time Formatting
# ╚══════════╝

{{ now|date:"Y-m-d" }} ← format date as YYYY-MM-DD
input:datetime(2025, 4, 5, 10, 30) ▶️ "2025-04-05"

{{ now|date:"j F Y" }} ← format date in human-readable form: Day Month Year
input:datetime(2025, 4, 5, 10, 30) ▶️ "5 April 2025"

{{ now|time:"H:i" }} ← format time in 24-hour format: HH:MM
input:datetime(2025, 4, 5, 10, 30) ▶️ "10:30"

{{ created_at|timesince }} ← display how long ago the datetime occurred (e.g., "1 day, 2 hours")
input:datetime(2025, 4, 4, 8, 0) ▶️ "1 day, 2 hours"

{{ event_date|timeuntil }} ← display how much time remains until the datetime (e.g., "5 days")
input:datetime(2025, 4, 10, 14, 0) ▶️ "5 days"

{{ created_at|naturalday }} ← show "today", "yesterday", or normal date (requires {% load humanize %})
input:datetime.today() ▶️ "today"

{{ created_at|naturaltime }} ← show relative time like "2 hours ago" (requires {% load humanize %})
input:datetime(2025, 4, 4, 15, 0) ▶️ "2 hours ago"


# ╔════════╗
# ║ OTHER  ║  ← Miscellaneous Filters
# ╚════════╝

{{ value|default:"N/A" }} ← return fallback value if input is falsy (None, "", 0, False, [])
input:None ▶️ "N/A"

{{ value|default_if_none:"Unknown" }} ← return fallback value only if input is exactly None
input:None ▶️ "Unknown"

{{ is_active|yesno:"فعال,غیرفعال" }} ← convert True/False to custom strings separated by comma
input:True ▶️ "فعال"

{{ is_active|yesno:"✅,❌" }} ← convert True/False to emojis or custom symbols
input:False ▶️ "❌"

{{ count|pluralize }} ← return empty string if value is 1, otherwise return "s" (for pluralization)
input:1 ▶️ ""

{{ count|pluralize:"s" }} ← return empty string if value is 1, else return suffix (e.g., "s")
input:1 ▶️ ""

{{ count|pluralize:"s" }} ← return suffix when value is not 1 (e.g., "s" for plural)
input:3 ▶️ "s"

{{ phone|phone2numeric }} ← convert phone letters to numbers (e.g., A→2, C→2, L→5)
input:"1-800-CALL-NOW" ▶️ "1-800-2255-669"

{{ html|removetags:"script style" }} ← remove specific HTML tags while keeping others
input:"<p>Hello <script>bad()</script></p><style>...</style>" ▶️ "<p>Hello </p>"
```

# 3. 🅰️Files

## 3.1. 🅱️Static

* جنگو از الگوی "اپ‌محور" استفاده می‌کند. بنابراین، بهترین روش این است که برای هر اپ، یک پوشه به نام static بسازید
    * نکته مهم: حتماً یک زیرپوشه با نام اپ (مثل myapp/) داخل static/ بسازید. این از تداخل نام فایل‌ها در اپ‌های مختلف جلوگیری می‌کند
* عبارت `{% load static %}` باید بالای هر فایل HTML که از فایل‌های استاتیک استفاده می‌کند درج گردد
* `STATIC_URL`: نشان‌دهنده URL پیش‌فرض برای دسترسی به فایل‌های استاتیک در مرورگر است.
* `STATICFILES_DIRS`:اگر فایل‌های استاتیک مشترکی دارید که در تمام اپ‌ها استفاده می‌شوند (مثلاً فایل‌های عمومی پروژه)، آنها را در یک پوشه خارج از اپ‌ها قرار دهید
* `STATIC_ROOT`:وقتی دستور `collectstatic` را اجرا می‌کنید، تمام فایل‌های استاتیک از اپ‌ها و `STATICFILES_DIRS` را در این مسیر جمع‌آوری می‌کند
    * این مسیر فقط در محیط تولید (production) استفاده می‌شود
    * این پوشه نباید در git قرار گیرد (در `.gitignore` اضافه کنید)

```
myapp/
    ├── static/
    │   └── myapp/
    │       ├── css/
    │       │   └── style.css
    │       ├── js/
    │       │   └── script.js
    │       └── images/
    │           └── logo.png
    ├── templates/
    ├── models.py
    └── views.py
```

File: `setting.py`

```python
STATIC_URL = 'static/'  # Default url on clients browser
STATIC_ROOT = BASE_DIR / "staticfiles"
# ╔═══════════════════╗
# ║ STATICFILES_DIRS ║
# ╚═══════════════════╝
# myproject/               ←  اگر ساختار شبیه ساختار ذیل بود
#     ├── static/          ← فایل‌های استاتیک عمومی پروژه
#     │   ├── css/
#     │   └── js/
#     ├── myapp/
#     │   └── static/myapp/...
#     └── settings.py
import os

STATICFILES_DIRS = [
    BASE_DIR / "static",  # پوشه استاتیک اصلی پروژه (در کنار manage.py)
]
```

```html
<!DOCTYPE html>
<html>
<head>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/main.css' %}"> <!--If ussing "STATICFILES_DIRS"-->
    <link rel="stylesheet" href="{% static 'myapp/css/style.css' %}">
    <script src="{% static 'myapp/js/script.js' %}"></script>
</head>
<body>
<img src="{% static 'myapp/images/logo.png' %}" alt="Logo">
</body>
</html>
```

**محیط Production**

در محیط توسعه (development)، جنگو به طور خودکار فایل‌های استاتیک را سرو می‌کند.اما در تولید (مثلاً روی سرور با Nginx یا Apache)، باید همه فایل‌های استاتیک را در یک مکان جمع کنید. این دستور تمام فایل‌های استاتیک از همه اپ‌ها و STATICFILES_DIRS را در STATIC_ROOT کپی می‌کند. پس از اجرای این دستور، سرور وب (مثل Nginx) باید مستقیماً از STATIC_ROOT فایل‌ها را سرو کند (نه از جنگو!).

```shell
python manage.py collectstatic

# ╔══════╗
# ║ NGINX ║
# ╚══════╝
location /static/ {
    alias /path/to/your/project/staticfiles;
}
```

* اگر می‌خواهید فایل‌های استاتیک را روی Heroku، Railway، Render یا Docker راه‌اندازی کنید، همین ساختار کافی است. فقط حتماً collectstatic را در مرحله ساخت (build) اجرا کنید.

**محیط Development**

* جنگو در تولید برای سرو فایل‌های استاتیک مناسب نیست
* در محیط توسعه، جنگو به صورت خودکار فایل‌های استاتیک را سرو می‌کند اما فقط اگر`DEBUG = True`باشد و در `urls.py` پروژه خط زیر اضافه شده باشد

```python
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # ... سایر مسیرها
]

# فقط در محیط توسعه! و هیچوقت این خطوط را در محیط تولید نگذارید!
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # اگر media هم دارید
```

**FINAL:**

جمع‌بند از فایل `settings.py`

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # فایل‌های عمومی پروژه
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# اگر از Media (آپلود فایل‌ها) هم استفاده می‌کنید:
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / "media"
```

# 4. 🅰️ClassBaseView

**FunctionBaseView**:در این حالت View ها به‌صورت تابع معمولی پایتون همانند ️BasicRenderingMethods که از django.http.HttpResponse استفاده می‌کند نوشته می‌شوند.

* مزایا:
    *     ساده و شهودی برای مبتدیان
    * کنترل کامل روی منطق
    * مناسب برای منطق‌های غیراستاندارد یا پیچیده
* معایب
    *     تکرار کد در پروژه‌های بزرگ (مثلاً برای Create/Edit/Delete)
    * نیاز به نوشتن دستی چیزهایی مثل فرم‌ها، اعتبارسنجی، redirect و ...

**Class-Based Views (CBV)**:ویوها به‌صورت کلاس پایتون نوشته می‌شوند و از وراثت و Mixinها برای استفاده مجدد کد استفاده می‌کنند.

* نکته: GenericViewها از ترکیب Mixinها + View ساخته شده‌اند
* نکته:Mixinها خودشان View نیستند، اما اجزای سازنده Viewها هستند
* در دسته‌بندی `TemplateView` (که در عمل پس از View ساده‌ترین CBV است) را ذیل Generic نیز آوردند 


```
🆑️ → Class or کلاس 
🅾️ → Object or شیء
Ⓜ️ → Method or function or تابع
p  → parent

Django Views
│
├── 1. Function-Based Views (FBV)
│    ├── my_view[Ⓜ️]
│    ├── list_view → [Ⓜ️]
│    ├── detail_view → [Ⓜ️]
│    ├── create_view → [Ⓜ️]
│    ├── update_view → [Ⓜ️]
│    ├── delete_view → [Ⓜ️]
│    └── api_view → [Ⓜ️(return JsonResponse)] )
│
└── 2. Class-Based Views (CBV)
     │
     ├── 2.1. Base Views
     │    ├── View[🆑️] → (base for all CBVs) ⟹ (handles HTTP methods)
     │    ├── TemplateView[🆑️] → (p: View) ⟹ (renders template) [پرکاربرد]
     │    └── RedirectView[🆑️] → (p: View) ⟹ (redirects to URL)
     │
     ├── 2.2. Generic Display Views
     │    ├── ListView[🆑️] → (ps: MultipleObjectMixin + TemplateResponseMixin + View)  ⟹ (handles list display) [پرکاربرد]
     │    ├── DetailView[🆑️] → (ps: SingleObjectMixin + TemplateResponseMixin + View)  ⟹ (handles single object)
     │    ├── ArchiveIndexView[🆑️] → (p: ListView) ⟹ (grouped by date)
     │    ├── YearArchiveView[🆑️] → (p: ArchiveIndexView) ⟹ (filter by year)
     │    ├── MonthArchiveView[🆑️] → (p: ArchiveIndexView) ⟹ (filter by month)
     │    ├── WeekArchiveView[🆑️] → (p: ArchiveIndexView) ⟹ (filter by week)
     │    ├── DayArchiveView[🆑️] → (p: ArchiveIndexView) ⟹ (filter by day)
     │    └── DateDetailView[🆑️] → (ps: SingleObjectMixin + TemplateResponseMixin + View) ⟹ (single object by date + slug)
     │
     ├── 2.3. Generic Editing Views
     │    ├── FormView[🆑️] → (ps: FormMixin + TemplateResponseMixin + View) ⟹ (handles forms)
     │    ├── CreateView[🆑️] → (ps: ModelFormMixin + ProcessFormView + FormMixin + TemplateResponseMixin + View) ⟹ (creates model instance)
     │    ├── UpdateView[🆑️] → (ps: ModelFormMixin + ProcessFormView + SingleObjectMixin + FormMixin + TemplateResponseMixin + View) ⟹ (edits model instance)
     │    └── DeleteView[🆑️] → (ps: DeletionMixin + SingleObjectMixin + TemplateResponseMixin + View) ⟹ (deletes object with confirmation)
     │
     ├── 2.4. Authentication Views
     │    ├── LoginView[🆑️] → (p: FormView) ⟹ (handles login)
     │    ├── LogoutView[🆑️] → (p: RedirectView)
     │    ├── PasswordChangeView[🆑️] → (p: FormView)
     │    ├── PasswordChangeDoneView[🆑️] → (p: TemplateView)
     │    ├── PasswordResetView[🆑️] → (p: FormView)
     │    ├── PasswordResetDoneView[🆑️] → (p: TemplateView)
     │    ├── PasswordResetConfirmView[🆑️] → (p: FormView)
     │    └── PasswordResetCompleteView[🆑️] → (p: TemplateView)
     │
     ├── 2.5. Mixins
     │    ├── ContextMixin[🅾️] → (adds context to template)
     │    ├── TemplateResponseMixin[🅾️] → (handles template rendering)
     │    ├── SingleObjectMixin[🅾️] → (retrieves single object)
     │    ├── MultipleObjectMixin[🅾️] → (retrieves list of objects)
     │    ├── FormMixin[🅾️] → (handles form logic)
     │    ├── ModelFormMixin[🆑️] → (p: FormMixin) ⟹ (binds ModelForm)
     │    ├── ProcessFormView[🅾️] → (process GET/POST for forms)
     │    ├── LoginRequiredMixin[🅾️] → (requires authenticated user)
     │    ├── UserPassesTestMixin[🅾️] → (custom permission logic)
     │    ├── PermissionRequiredMixin[🅾️] → (requires Django permission)
     │    └── SuccessMessageMixin[🅾️] → (adds success message after form)
     │
     ├── 2.6. API & Specialized Views
     │    ├── JSONResponseMixin[🅾️] → (provides JSON response)
     │    ├── DeletionMixin[🅾️] → (deletion helper)
     │    ├── AsyncView[🆑️] → (p: View) ⟹ (supports async HTTP)
     │    ├── APIView[🆑️] → (p: View) ⟹ (base API view)
     │    ├── GenericAPIView[🆑️] → (p: APIView) ⟹ (adds queryset/form handling)
     │    ├── ListModelMixin[🅾️] → (API list endpoint)
     │    ├── CreateModelMixin[🅾️] → (API create endpoint)
     │    ├── RetrieveModelMixin[🅾️] → (API retrieve endpoint)
     │    ├── UpdateModelMixin[🅾️] → (API update endpoint)
     │    ├── DestroyModelMixin[🅾️] → (API delete endpoint)
     │    ├── ViewSet[🅾️] → (groups API actions)
     │    └── ModelViewSet[🆑️] → (ps: ViewSet + GenericAPIView + mixins) ⟹ (full CRUD API)
     │
     └── 2.7. Advanced CBV Patterns
          ├── BaseListView[🆑️] → (p: ListView) ⟹ (customizable list view)
          ├── BaseDetailView[🆑️] → (p: DetailView) ⟹ (customizable detail view)
          ├── ModelPermissionMixin[🅾️] → (map HTTP methods to permissions)
          ├── OwnerRequiredMixin[🅾️] → (restrict object access to owner)
          └── BulkActionView[🆑️] → (p: View) ⟹ (handle bulk create/update/delete)
```
## 🅱️
## 🅱️
## 🅱️
## 🅱️
## 🅱️
## 🅱️
## 🅱️
## 🅱️
## 🅱️
## 🅱️
## 🅱️
## 🅱️

</div>