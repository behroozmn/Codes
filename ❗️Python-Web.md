<div dir="rtl">

# 🅰️ Django

# 🅰️ DRF(Django Rest Framework)

## 🅱️ Install

```shell
pip freeze # check for "virtualenv" that must be installed
python3 -m venv myenv #ایجاد مجیط مجازی مستقل از سیستم اصلی 
source myenv/bin/activate #فعال‌سازی محیط مجازی مختص به پروژه‌خاص
pip install django
pip freeze # باید بسته جنگو نصب شده در لیست موجود باشد
           # This package is also installed: 1-asgire 2-sqlparse 3-tzdata 
```

<div style="direction:rtl;">
به مسیری که پوشه venv در آن موجود است رفته و در کنار پوشه venv ، پوشه پروژه را ایجاد نمایید
</div>

```shell
django-admin startproject config . # پروژه با نام کانفیگ در مسیر جاری ایجاد می‌کنیم
```

```
pip install djangorestframework
pip install markdown
pip install django-filter
```

File: `setting.py`

```python
INSTALL_APPS = [..., 'rest_framework', ...]
```

File: `urls.py`

```python
from django.urls import path, include

urlpatterns = [

    path('api/auth/', include('rest_framework.urls'))
]
```

## 🅱️ Authentication

### ✅️ BasicAuthentications

#### ❇️ Global Setting File

* با این کار شما درسراسر کد نیازبه احراز هویت خواهید داشت

File: `settingd.py`

```python

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.BasicAuthentication'],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated']
}
```

#### ❇️ Config in Views

File: `/todo/views.py`

```python
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class TodosGenericApiView(generics.ListCreateAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    authentication_classes = [BasicAuthentication] ✅️
    permission_classes = [IsAuthenticated] ✅️


class TodosGenericDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
```

### ✅️ TokenAuthentication[ذخیره توکن در دیتابیس]

#### ❇️ Configure

1. File: `setting.py`
    ```python
   INSTALL_APPS = [... ,'rest_framework.authtoken', ... ]
   
   REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
    'DEFAULT_PERMISSION_CLASSES':     ['rest_framework.permissions.IsAuthenticated']
   }
   ```
2. migrations Command `python manage.py migration`

3. File: `/config/urls.py` # Main urls
   ```
   from rest_framework.authtoken.views import obtain_auth_token # ✅️
   
   urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('home.urls')),
      path('todos/', include('todo.urls')),
      path('api-auth/', include('rest_framework.urls')),
      path('auth-token/', obtain_auth_token, name='generate_auth_token')# ✅️
   ```

#### ❇️ Intro

* ابتدا به یک آدرس دلخواه نظیر «auth-token» با مقادیر username و password در body ارسال می‌کنیم

```
URL: http://127.0.0.1:8000/auth-token[POST]
{
   "username":"USERNAME",
   "password":"PASS"
}
```

* سپس یک token برای کاربر ساخته می‌شود و در دیتابیس برای همان کاربر با نگهداری زمان ایجاد token ذخیره می‌شود و بعنوان response برمیگرداند تا کدنویس آن را نگهداری و استفاده نماید

```
#response
{
    "token": "<Token>", 
}
```

* از آن پس هرگاه بخواهیم دیتا در آدرس‌های دیگر ارسال کنیم باید در header درخواست‌هایمان مقدار زیر را نیز وارد نمایید

```Authentication: Token <TOKEN>```# ✅️

### ✅️ JWT(JsonWebToken)[عدم ذخیره توکن در دیتابیس]

#### ❇️ Intro

* ابتدا به یک آدرس دلخواه نظیر «api/token» با مقادیر username و password در body ارسال می‌کنیم

```
URL: http://127.0.0.1:8000/api/token[POST]
{
   "username":"USERNAME",
   "password":"PASS"
}
```

* سپس دو token برای کاربر ساخته می‌شود و بعنوان response آنها را به کدنویس برمیگرداند تا کدنویس توکن access را نگهداری و در هر ارسال دیتا از آن استفاده نماید

```
#response
{
    "refresh": "<Token>", 
    "access" : "<Token>"
}
```

* توکن access: باید در هدر هر درخواست ارسال گردد بصورت پیش‌فرض تا ۱ روز معتبر است
* توکن refresh: بصورت پیش‌فرض ۵ دقیقه معتبر است. هرگاه توکن access منقضی شد آنگاه این توکن را به آدرس «api/token/refresh/» ارسال می‌کنیم تا توکن بروز رسانی شود و سپس آن را در هر انتقال دیتا در آدرس استفاده می‌کنیم
* از آن پس هرگاه بخواهیم دیتا در آدرس‌های دیگر ارسال کنیم باید در header درخواست‌هایمان مقدار هش access را نیز وارد نمایید

```Authentication: Bearer <AccessToken>```

* هرگاه توکن در تایم پیش‌فرض تعیین شده منقضی شد آنگاه می‌توانیم توسط درج در Body درخواست به آدرس زیر، آن را مجدد فعال کنیم.

```
URL: http://127.0.0.1:8000/api/token/refresh[POST]
{
   "refresh":"<RefreshToken>",
}
```

```
#response
{
    "access" : "<Token>"
}
```

#### ❇️ Requirements

* python
* Django
* Django REST framework

#### ❇️ installation

```
pip install djangorestframework-simplejwt
```

#### ❇️ Configure

1. File: `setting.py`
   ```python
   # ...
   INSTALL_APPS = [... ,'rest_framework.authtoken','rest_framework_simpleJWT', ... ]
   REST_FRAMEWORK = {...
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.JWTAuthentication'],
    'DEFAULT_PERMISSION_CLASSES':     ['rest_framework.permissions.IsAuthenticated']
   }
   
   from datetime import timedelta # ✅️
   SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",), # نام ارسالی همراه توکن باید چه باشد
   }
   ```
   [URL](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html)

2. File: `/config/urls.py` # Main urls
   ```python
   from rest_framework.authtoken.views import obtain_auth_token
      from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
      
      urlpatterns = [
         path('admin/', admin.site.urls),
         path('', include('home.urls')),
         path('todos/', include('todo.urls')),
         path('api-auth/', include('rest_framework.urls')),
         path('auth-token/', obtain_auth_token, name='generate_auth_token'),
         path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # ✅️
         path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),# ✅️
      ```


## 🅱️ DRF_Modules

### ✅️ rest_framework.request

#### ❇️ request

```python
from rest_framework.request import Request
```

<div style="direction: rtl" >

* نسخه کامل شده HttpRequest است که برای DRF سفارشی‌سازی شده است
* ماژول Request (دربستهrest_framework.request) بصورت عمومی در جنگو مورد استفاده قرار نمیگرد و معمولا در DRF مورد استفاده قرار می‌گیرد

</div>

#### ❇️ response

```python
from rest_framework.response import Response
```

<div style="direction: rtl" >

* نسخه کامل شده HttpResponse است که برای DRF سفارشی‌سازی شده است
* ماژول Response (دربستهrest_framework.request) بصورت عمومی در جنگو مورد استفاده قرار نمیگرد و معمولا در DRF مورد استفاده قرار می‌گیرد

</div>



# 🅰️ Flask

```python
   from flask import Flask

app = Flask(___name___)


@app.route("/")
def hello()
    return "Hellow Woeld!"


if ___name___ == "___main___":
    app.run(host="0.0.0.0")
```

</div>