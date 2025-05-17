from gettext import install

# 1.BasicAuthentications

## 1.1.Global Setting File

* با این کار شما درسراسر کد نیازبه احراز هویت خواهید داشت

File: `settingd.py`

```python
...

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.BasicAuthentication'],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated']
}
```

## 1.2.Config in Views

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

# 2.TokenAuthentication[ذخیره توکن در دیتابیس]

## 2.1.Configure

1. File: `setting.py`
    ```python
    ...
   INSTALL_APPS = [... ,'rest_framework.authtoken', ... ]
   
   REST_FRAMEWORK = {...
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
   ...

## 2.2.Intro

<div style="direction: rtl">

* ابتدا به یک آدرس دلخواه نظیر «auth-token» با مقادیر username و password در body ارسال می‌کنیم

</div>

```
URL: http://127.0.0.1:8000/auth-token[POST]
{
   "username":"USERNAME",
   "password":"PASS"
}
```

<div style="direction: rtl">

* سپس یک token برای کاربر ساخته می‌شود و در دیتابیس برای همان کاربر با نگهداری زمان ایجاد token ذخیره می‌شود و بعنوان response برمیگرداند تا کدنویس آن را نگهداری و استفاده نماید

</div>

```
#response
{
    "token": "<Token>", 
}
```

<div style="direction: rtl">

* از آن پس هرگاه بخواهیم دیتا در آدرس‌های دیگر ارسال کنیم باید در header درخواست‌هایمان مقدار زیر را نیز وارد نمایید

</div>

```Authentication: Token <TOKEN>```# ✅️

# 3.JWT(JsonWebToken)[عدم ذخیره توکن در دیتابیس]

## 3.1.Intro

<div style="direction: rtl">

* ابتدا به یک آدرس دلخواه نظیر «api/token» با مقادیر username و password در body ارسال می‌کنیم

</div>

```
URL: http://127.0.0.1:8000/api/token[POST]
{
   "username":"USERNAME",
   "password":"PASS"
}
```

<div style="direction: rtl">

* سپس دو token برای کاربر ساخته می‌شود و بعنوان response آنها را به کدنویس برمیگرداند تا کدنویس توکن access را نگهداری و در هر ارسال دیتا از آن استفاده نماید

</div>

```
#response
{
    "refresh": "<Token>", 
    "access" : "<Token>"
}
```

<div style="direction: rtl">

* توکن access: باید در هدر هر درخواست ارسال گردد بصورت پیش‌فرض تا ۱ روز معتبر است
* توکن refresh: بصورت پیش‌فرض ۵ دقیقه معتبر است. هرگاه توکن access منقضی شد آنگاه این توکن را به آدرس «api/token/refresh/» ارسال می‌کنیم تا توکن بروز رسانی شود و سپس آن را در هر انتقال دیتا در آدرس استفاده می‌کنیم
* از آن پس هرگاه بخواهیم دیتا در آدرس‌های دیگر ارسال کنیم باید در header درخواست‌هایمان مقدار هش access را نیز وارد نمایید

</div>

```Authentication: Bearer <AccessToken>```

<div style="direction: rtl">

* هرگاه توکن در تایم پیش‌فرض تعیین شده منقضی شد آنگاه می‌توانیم توسط درج در Body درخواست به آدرس زیر، آن را مجدد فعال کنیم.

</div>

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

## 3.2.Requirements

* python
* Django
* Django REST framework

## 3.3.installation

```
pip install djangorestframework-simplejwt
```

## 3.4.Configure

1. File: `setting.py`
   ```python
   ...
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