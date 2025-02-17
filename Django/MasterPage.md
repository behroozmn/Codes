# [masterPage] or [MainPage] or [BasePage] or [LayoutePage]

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