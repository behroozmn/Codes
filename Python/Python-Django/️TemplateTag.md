# TemplateTag

## basic

به استفاده از قعطه کد پایتون در داخل صفحات «اچ‌تی‌ام‌ال» که سیتنکس آن مشابه خطوط زیر است

> `{% PYTHON_SYNTAX_CODE %}`


File: `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>days</title>
</head>

<body>
<ul>
    {% for day in days %}
    <li><a href="/days/{{day}}"> {{day | title}} </a></li>
    {% endfor %}
</ul>
</body>
</html>
```

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
    context = {
        'days': days_list
    }

    return render(request, "challenges/index.html", context)

```

# 2. TemplateTag[Reverse]

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
    context = {
        'days': days_list
    }
    return render(request, "challenges/index.html", context)

def dynamic_days_by_number(request, day):
    days_names = list(days.keys())
    if day > len(days_names):
        return HttpResponseNotFound('day does not exists')
    redirect_day = days_names[day - 1]
    redirect_url = reverse('days-of-week', args=[redirect_day])
    return HttpResponseRedirect(redirect_url)
    # return HttpResponse(day)
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
<head>
    <meta charset="UTF-8"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>days</title>
</head>

<body>
<ul>
    {% for day in days %}
    <li><a href="{% url 'days-of-week' day %}"> {{day | title}} </a></li>
    {% endfor %}
</ul>
</body>
</html>
```

Note: [URL](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#url)

# ماژول‌های تمپلیت‌تگ
## url
میتوان برای رفرنس و آدرس ها از کانتکس ارسالی به صفحه استفاده کرد به نحو زیر
```html
{% load static %}
... 
<a href="{% url 'urlPost' slug=post.slug %}"></a>
<img src="{% static 'yazahra/images/001.jpg' %}" alt="بهروز محمدی نسب">
<img src="{% static 'yazahra/images'|add:'/'|add:post.image %}" alt="{{ post.title }}">
...
```

# for
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

# time
```html
<time>{{ post.date|date:'d M Y' }}</time>
```
# linebreaks
تبدیل خطوط جدید (\n) در متن post.content به تگ‌های HTML مناسب برای نمایش در مرورگر 
> نکته« معمولا وقتی از علامت پایت یا «|» استفاده می‌کنیم اصطلاحا کلمه فیلتر شدن معنی پیدا میکند
```html
{{ post.content| linebreaks }} #
```

# محتویات تگ‌ها
```html
...
<div class="post_content">
    <h3>{{ post.title }}</h3>
    <p>{{ post.content }}</p>
</div>
...
```
