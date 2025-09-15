<div dir="rtl">

# 1. 🅰️Django

## 1.1. 🅱️‌BasicRenderingMethods

### 1.1.1. ✅️django.http.HttpResponse

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

### 1.1.2. ✅️HttpResponse+template(context)

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

### 1.1.3. ✅️django.shortcuts.render()

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

### 1.1.4. ✅️Http404

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

## 1.2. 🅱️‌Page

### 1.2.1. ✅️BasePage(block)

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

### 1.2.2. ✅️subPage(extends)

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

#### 1.2.2.1. ❇️block.super

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

### 1.2.3. ✅️Include

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

#### 1.2.3.1. ❇️context(with)

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

#### 1.2.3.2. ❇️contextWith(only)

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

</div>