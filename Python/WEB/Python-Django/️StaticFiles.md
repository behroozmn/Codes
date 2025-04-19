1. مسیر فایل‌های استاتیک پروژه باید درفایل تنظیمات تعریف شده باشد
    `INSTALLED_APPS = [ ...'django.contrib.staticfiles' ... ]`
2. File: `settings.py`
> * `STATICFILES_DIRS = [BASE_DIR / 'static' ]`
3. بالای فایل اچ تی ام ال عبارت زیر را درج نمایید
    `{% load static %}`
4.  اگر بخوایم فایلی از فایل‌های استاتیک را به پروژه وصل نمایید باید از روش زیر استفاده نمایید

    ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{% block title %}{% endblock %}</title>
        <link rel="stylesheet" href="{% static 'CustomCSS.css' %}">
        {% block header_reference %}{% endblock %}
    </head>
    <body>
    {% block content %}{% endblock %}
    {% block footer_references %}{% endblock %}
    </body>
    </html>
    ```
>  اگر اپلیکیشن بالا بود و با ارور ۴۰۴ مواجه شدیم باید سرویس جنگو را ریست نماییم