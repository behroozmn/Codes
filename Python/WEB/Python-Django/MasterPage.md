# 1. [masterPage] or [MainPage] or [BasePage] or [LayoutePage]

با هدف ایجاد یک صفحه اصلی که بعنوان صفحه پیش‌فرض مد نظر قرار گیرد و بقیه صفحات از آن مشتق شده و هر صفحه بتواند تگ های سفارشی خود را داشته باشد

1. create `base.html` in `template` Directory
   > Note: دایرکتوری «تمپلیت» باید در فایل ستینگ بعنوان مسیر پیش‌فرض تمپلیت‌های پروژه لحاظ شده باشد

3. File: `base.html`
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>{% block title %}{% endblock %}</title>
       {% block header_reference %}{% endblock %}
   </head>
   <body>
   {% block content %}{% endblock %}
   {% block footer_references %}{% endblock %}
   </body>
   </html>
   ```
   > در هرصفحه‌ای که ازاین صفحه ارث‌بری نماید، بااستفاده از نام بلاک‌های بالا، می‌توان دیتای سفارشی همان صفحه را در محتوی بلاک‌ها درج نمود
4. File: `subPage1.html`
   ```html
     {% extends 'base.html' %}      #✅️ برای ارث بری باید این خط در ابتدا باشد
     {% block title %}My Blog{% endblock %}
     {% block content %}
         <header id="main-navigation">
             <h1><a href="">Toplearn Blog</a></h1>
             <nav>
                 <a href="">All Posts</a>
             </nav>
         </header>
       <section id="welcome">
       <header>
              <img src="{% static 'blog/images/master.jpg' %}" alt="Toplearn - Author Of This blog">
              <h2>Toplearn blog project</h2>
          </header>
          <p>Hi, My name is mohammad, Im a Teacher in Toplearn</p>
      </section>
     {% endblock %}
         ```
5. File: `view.py`
   ```
   from django.shortcuts import render
   def index(request):
       return render(request, 'subPage1.html')
   ```

Note: [URL](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#block)

# 2.Include

تهیه بخش های متفاوت از تکه‌ها صفحه و استفاده در صفحه اصلی

> note: `include` tag must use in `Content` block\
> یعنی معمولا در بدنه مورد استفاده قرار میگیرید

در بخش زیر یک تکه کد را خواهید دید که قرار است به بدنه صفحه ای متصل گردد\
File: `topic.html`

```html
<header>
  <nav>
    <a href="http://itsee.ir">روزهای هفته</a>
  </nav>
</header>
```

صفحه ای که تکه کد بالا باید به آن وصل گردد\
File: `index.html`

```html
{% extends 'base.html' %} 
{% block content %}
{% include "topic.html"%}✅️
{% endblock %}
```

# 3 Include by `send Parameter`

تهیه بخش های متفاوت از تکه‌ها صفحه و استفاده در صفحه اصلی

File: `topic.html`

```html
<header>
  <nav>
    <a href="{% url 'days_list' %}">روزهای هفته</a>
  </nav>
  <p>{{ active_page|title }}</p>
</header>
```

صفحه ای که تکه کد بالا باید به آن وصل گردد\
File: `index.html`

```html
{% extends 'base.html' %} 
{% block content %}
{% include "topic.html" with active_page="daysIndex" %}✅️
<ul>
  {% for item in days %}
  <li><a href="{% url 'days-of-week' item %}"> {{item}} </a></li>  <!--  {% url 'days-of-week' day %}: USSING Reverse URL -->
  {% endfor %}
</ul>
{% endblock %}
```

File: `page2.html`

```html
{% extends 'base.html' %}

  {% block page_title %}days info{% endblock  %}

{% block content %}
  {% include "topic.html" with active_page="dayDetail" %}✅️
    {% if data is not None %}
    <h2>{{ data }}</h2> <!-- متغیر دیتا چیزی است که در تابع پایتون استفاده شد است و در آن فایل پایتون به این صفحه اشاره شده است-->
    {% else %}
    <p>there is no data</p>
    {% endif %}
{% endblock  %}
```

# 4. استفاده از جاوااسکریپ در برخی از صفحات

{% block footer_references %}
  <script>
  console.log('hello')
  </script>
{% endblock %}

```
> Note: میتوان در تکه صفحه‌ها تگ اسکریپت یعنی جاوا اسکریپت را هم درج نماییم