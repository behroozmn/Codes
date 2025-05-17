# افزودن یک اپلیکیشن(ماژول)جدید به پروژه اصلی

## 1-General

> * افزودن یک ماژول یا به‌اصلاح یک اپلیکیشن(یک پوشه)جدید به‌پروژه ولی همچنان مدیریت اصلی برنامه با پوشه اصلی است
> * شکستن پروژه بزرگ به ماژول یا برنامه کوچک‌تر تا بتوانیم هر کدام از قسمت‌ها را مستقل مدیریت کنیم

1. Execute: `python manage.py startapp myNewApp`

2. Edit `myNewApp>views.py > settings.py`

    ```
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',️
        'myNewApp'✅️
    ]
    ```
3. Edit `mainProject > main_urls.py`
   > * add `, inclule` in `from django.urls import path` line
   > * for mainPage add `from . import views`

    ```
    from django.contrib import admin
    from django.urls import path, include
    from . import views
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.mainindex),
        
    ]

4. Edit(or create) `mainProject > main_views.py`
    ```
   from django.http import HttpResponse
   def mainindex(request):
       return HttpResponse("index page(صفحه اصلی)")
    ```

## 2-Appication

### 2-1 Example1

1. Edit `mainProject > main_urls.py`

   add `urls` of myNewApp into `urls.py` of main project

   ```
   urlpatterns = [
       ...
       path('Example1/', include('myNewApp1.urls'))
       ...
   ]

   ```

2. Create `myNewApp1 > urls.py`

    ```
    from django.urls import path
    from . import views
    urlpatterns = [
        path('', views.madulewithouturl),
        path('show', views.usershow),
        path('edit', views.useredit)
    ]
    ```

3. Edit(or create) `myNewApp1 > views.py`
    * مجموعه توابع و کلاس که هنگام فراخوانی آدرس خاص توسط جنگو اجرا می‌شوند
    * این موارد تنها توسط جنگو فراخوانی و اجرا می‌شود و به هیچ عنوان توسط برنماه نویس ایجاد شیء یا فراخوانی نمی‌شود

    ```
    from django.shortcuts import render
    from django.http import HttpResponse
    # Create your views here.
    def madulewithouturl(request):
        return HttpResponse('صفحه اصلی  زیر برنامه یا ماژول') 
    def usershow(request):
        return HttpResponse('صفحه نمایش کاربران')
    def useredit(request):
        return HttpResponse('صفحه ادیت کاربران')
    ```

### available urls

* 127.0.0.1:8080 #function madulewithouturl
* 127.0.0.1:8080/Example1/show #function usershow
* 127.0.0.1:8080/Example1/edit #function useredit
    