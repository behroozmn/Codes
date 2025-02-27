# Render

## 1.render_to_string

دریافت آدرس یک فایل «اچ‌تی‌اِم‌آِل» و تبدیل به رشته و استفاده از آن

```
from django.template.loader import render_to_string✅️
def dynamic_name(request, name):
    dic_keys = list(dic_id.keys())
    dic_values = list(dic_id.values())

    data = None
    for key, val in dic_id.items():
        if val == name:
            data = key
    if data is not None:
        return HttpResponse(f'input from url is : {name} and data is : {data}<br><br>'
                            f'<a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>')
    else:
        response_data = render_to_string('NotResponse.html')✅️
        return HttpResponse(response_data)
```

## 2. render

```
from django.shortcuts import render✅️
def dynamic_name(request, name):
    dic_keys = list(dic_id.keys())
    dic_values = list(dic_id.values())

    data = None
    for key, val in dic_id.items():
        if val == name:
            data = key
    if data is not None:
        return HttpResponse(f'input from url is : {name} and data is : {data}<br><br>'
                            f'<a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>')
    else:
        return render(request, 'NotResponse.html')✅️
```

## 3.Render(Reverse)

File: `View.py`

```
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

days = {
    'saturday': 'this is satureday in dictionary',
    'sunday': 'this is sunday in dictionary',
    'monday': 'this is monday in dictionary',
    'tuesday': 'this is tuesday in dictionary',
    'wednesday': 'this is wednesday in dictionary',
    'thursday': 'this is thursday in dictionary',
    'friday': 'this is friday in dictionary',
}


def dynamic_days(reqeust, day):
    day_data = days.get(day)
    if day_data is not None:
        context = {
            "data": day_data,
            "day": f'selected DAY is {day}'
        }
        return render(reqeust, 'challenges/challenge.html', context)
    return HttpResponseNotFound('day does not exists')

def days_list(request):
    days_list = list(days.keys())
    context = {'days': days_list}
    return render(request, "challenges/index.html", context)

def dynamic_days_by_number(request, day):
    days_names = list(days.keys())
    if day > len(days_names):
        return HttpResponseNotFound('day does not exists')
    redirect_day = days_names[day - 1]
    redirect_url = reverse('days-of-week', args=[redirect_day])✅️
    return HttpResponseRedirect(redirect_url)
```

File: `urls.py`

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.days_list),
    path('<int:day>', views.dynamic_days_by_number),
    path('<str:day>', views.dynamic_days, name='days-of-week'),
]
```

File: `index.html` in Templates Folder

```html
<!DOCTYPE html>
<html lang="en">
<body>
<ul>
    {% for day in days %}
    <li><a href="{% url 'days-of-week' day %}"> {{day | title}} </a></li>
    {% endfor %}
</ul>
</body>
</html>
```

## 4.DTL(Django Template Language) with CONTEXT

به استفاده از قعطه کد پایتون در داخل صفحات «اچ‌تی‌ام‌ال» که سیتنکس آن مشابه خطوط زیر است
> `{% PYTHON_SYNTAX_CODE %}`

### 4.1 basic

File: `View.py`

```
days = {
    'saturday': 'this is satureday in dictionary',
    'sunday': 'this is sunday in dictionary',
    'monday': 'this is monday in dictionary',
    'tuesday': 'this is tuesday in dictionary',
    'wednesday': 'this is wednesday in dictionary',
    'thursday': 'this is thursday in dictionary',
    'friday': 'this is friday in dictionary',
}


def days_list(request):
    days_list = list(days.keys())
    context = {'days': days_list }
    return render(request, "challenges/index.html", context)
```

File: `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<body>
<ul>
    {% for day in days %}
    <li><a href="/days/{{day}}"> {{day | title}} </a></li>
    # به این علامت «|» فیلتر گفته می‌شود
    {% endfor %}
</ul>
</body>
</html>
```

### 4.2 Modules

```html
...
<div class="post_content">
    <h3>{{ post.title }}</h3>
    <p>{{ post.content }}</p>
</div>
...
```

#### url

میتوان برای رفرنس و آدرس ها از کانتکس ارسالی به صفحه استفاده کرد به نحو زیر

```html
{% load static %}
...
<a href="{% url 'urlPost' slug=post.slug %}"></a>
<img src="{% static 'yazahra/images/001.jpg' %}" alt="بهروز محمدی نسب">
<img src="{% static 'yazahra/images'|add:'/'|add:post.image %}" alt="{{ post.title }}">
...
```

#### for

```html

<section id="latestPost">
    <h2>پست‌های‌آخر</h2>
    <ul>
        {% for post in 2latestPosts %}
        {% include 'yazahra/includes/include_post.html' %} #نکته: اینکلود معمولا در مسیر تمپلیت قرار داده می‌شود(مسیر تمپلیت به پروزه باید افزوده شود)
        {% endfor %}
    </ul>
</section>
```

#### time

```html

<time>{{ post.date|date:'d M Y' }}</time>
```

#### linebreaks

تبدیل خطوط جدید (\n) در متن post.content به تگ‌های HTML مناسب برای نمایش در مرورگر
> نکته« معمولا وقتی از علامت پایت یا «|» استفاده می‌کنیم اصطلاحا کلمه فیلتر شدن معنی پیدا میکند

```html
{{ post.content| linebreaks }} #
```

## 5.مثال‌ها

### مثال۱

> منظور همان دو آکولاد باز و بسته است که در داخل کد «اچ‌تی‌ام‌ال» مشاهده می‌شود

```
from django.shortcuts import render
days = {
    'saturday': 'this is satureday in disctionary',
    'sunday': 'this is sunday in disctionary',
    'monday': 'this is monday in disctionary',
    'tuesday': 'this is tuesday in disctionary',
    'wednesday': 'this is wednesday in disctionary',
    'thursday': 'this is thursday in disctionary',
    'friday': 'this is friday in disctionary',
}


def dynamic_days(reqeust, day):
    day_data = days.get(day)
    if day_data is not None:
        context = {"data": day_data}
        # DTL -> Django Template Language

        return render(reqeust, 'challenges/challenge.html', context)✅️ # این اسم مهم نیست مهم ارسال دیکشنری است که به صفحخه دیکشنری ارسال بشود
        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
    return HttpResponseNotFound('day does not exists')

```

### مثال۲

File: `*.html`

```html
...
<div class="post_content">
    <h3>{{ post.title }}</h3>
    <p>{{ post.content }}</p>
</div>
...
```

File: `view.py`

```python
from django.shortcuts import render
from datetime import date

# Create your views here.

posts_database = [
    {
        'slug': 'poos0001',
        'title': '۰۰۰۱',
        'author': 'بهروز محمدی نسب ',
        'image': '001.jpg',
        'date': date(2021, 4, 5),
        'shortDescription': 'توضیحات اختصاری از پست شماره یکم',
        'content': 'محتویات پست اول'},
    {
        'slug': 'poos0002',
        'title': '۰۰۰۲',
        'author': 'بهروز محمدی نسب ',
        'image': '009.jpg',
        'date': date(2021, 6, 3),
        'shortDescription': 'توضیحات اختصاری از پست شماره دوم',
        'content': 'محتویات پست دوم'
    },
    {
        'slug': 'poos0003',
        'title': '۰۰۰۳',
        'author': 'بهروز محمدی نسب ',
        'image': '003.jpg',
        'date': date(2021, 3, 1),
        'shortDescription': 'توضیحات اختصاری از پست شماره سوم',
        'content': 'محتویات پست سوم'
    },
    {
        'slug': 'poos0004',
        'title': '۰۰۰۴',
        'author': 'بهروز محمدی نسب ',
        'image': '010.jpg',
        'date': date(2025, 2, 27),
        'shortDescription': 'توضیحات اختصاری از پست شماره چهارم',
        'content': 'محتویات پست چهارم'
    },
]


def get_date(post):
    return post['title']


def index(request):
    sorted_posts = sorted(posts_database, key=get_date)
    two_latest_post = sorted_posts[-2:]
    return render(request, 'yazahra/index.html', {'2latestPosts': two_latest_post})


def posts(request):
    all_posts = sorted(posts_database, key=get_date)
    return render(request, 'yazahra/posts.html', {'allPosts': all_posts})


def single_post(request, slug):
    # return render(request, 'yazahra/post.html')
    post = next(post for post in posts_database if post['slug'] == slug)
    return render(request, 'yazahra/post.html', {'post': post})
```

> Note: [built-In Templates](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/)
> Note: [URL]               (https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#url)
