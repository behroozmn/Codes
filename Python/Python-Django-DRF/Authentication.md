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
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class TodosGenericDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
```

# TokenAuthentication

<div style="direction: rtl">

* ابتدا به یک آدرس دلخواه نظیر «auth-token» با مقادیر username و password در body ارسال می‌کنیم

</div>

```
{
   "username":"USERNAME",
   "password":"PASS"
}
```

<div style="direction: rtl">
* سپس یک token برای کاربر ساخته شده و در دیتابیس برای همان کاربر با نگهداری زمان ایجاد توکن ذخیره می‌شود و بعنوان response برمیگرداند تا کدنویس آن را نگهداری نماید
* از آن پس هرگاه بخواهیم دیتا در آدرس‌های دیگر ارسال کنیم باید در header درخواست‌هایمان مقدار زیر را نیز وارد نمایید

</div>

```Authentication: Token <TOKEN>```

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
   ```python
   from rest_framework.authtoken.views import obtain_auth_token # ✅️
   
   urlpatterns = [
   ...
   path('auth-token/', obtain_auth_token, name='generate_auth_token')# ✅️
   ...
