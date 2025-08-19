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



```python
from rest_framework.request import Request
```

* نسخه کامل شده HttpRequest است که برای DRF سفارشی‌سازی شده است
* ماژول Request (دربستهrest_framework.request) بصورت عمومی در جنگو مورد استفاده قرار نمیگرد و معمولا در DRF مورد استفاده قرار می‌گیرد

### ✅️ rest_framework.response

```python
from rest_framework.response import Response
```

* نسخه کامل شده HttpResponse است که برای DRF سفارشی‌سازی شده است
* ماژول Response (دربستهrest_framework.request) بصورت عمومی در جنگو مورد استفاده قرار نمیگرد و معمولا در DRF مورد استفاده قرار می‌گیرد




## 🅱️ Swagger

* `pip install drf-spectacular`
* Setting.py
    * `INSTALL_APPS=[... , 'drf_spectacular' ,...]` # Swagger
    * `REST_FRAMEWORK = {... , 'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema' , ...}`
    * Add this line
      ```python
      SPECTACULAR_SETTINGS = {
      'TITLE': 'Your Project API',
      'DESCRIPTION': 'Your project description',
      'VERSION': '1.0.0',
      'SERVE_INCLUDE_SCHEMA': False,
      # OTHER SETTINGS
      }
      ```
* urls.py
  ```python
  from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('home.urls')),
      path('todos/', include('todo.urls')),
      ...
      # YOUR PATTERNS
      path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
      # Optional UI:
      path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
  ]
  ```

### ✅️ Appendix

> اگر بخواهیم مواردی که در صفحه سوئگر هست را تغییر بدهید به روش زیر امکان پذیر خواهد بود

File: `/todo/views.py`

```python
from drf_spectacular.utils import extend_schema


class TodosListApiView(APIView):
    @extend_schema(  # ✅️
        request=TodoSerializer,  # ✅️
        responses={201: TodoSerializer},  # ✅️
        description='this api is used for get all todos list',  # ✅️
    )  # ✅️


def get(self, request: Request):
    todos = Todo.objects.order_by('priority').all()
    todo_serializer = TodoSerializer(todos, many=True)
    return Response(todo_serializer.data, status.HTTP_200_OK)


def post(self, request: Request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    else:
        return Response(None, status.HTTP_400_BAD_REQUEST)


class TodosDetailApiView(APIView):
    def get_object(self, todo_id: int):
        try:
            todo = Todo.objects.get(pk=todo_id)
            return todo

    except Todo.DoesNotExist:
    return Response(None, status.HTTP_404_NOT_FOUND)


def get(self, request: Request, todo_id: int):
    todo = self.get_object(todo_id)
    serializer = TodoSerializer(todo)
    return Response(serializer.data, status.HTTP_200_OK)


def put(self, request: Request, todo_id: int):
    todo = self.get_object(todo_id)
    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)
    return Response(None, status.HTTP_400_BAD_REQUEST)


def delete(self, request: Request, todo_id: int):
    todo = self.get_object(todo_id)
    todo.delete()
    return Response(None, status.HTTP_204_NO_CONTENT)
```

## 🅱️ Validation

* در حین وارد کردن دیتای جدید یا ادیت، مقادیر وارد شده مطابق با نوع دیتای مدل و جدول باشد
* یا بخواهیم فیلتر برای وارد کردن دیتا قرار بدهیم یعنی مثلا کاربر باید یک پارامتر را اعداد بین یک تا بیست وارد نماید وگرنه نتواند و خطا بدهد
* مثلا یک عنوان نباید بیشتر از ۳۰۰ کاراکتر باشد و گرنه پیعام خطا بدهد
* یا دیتا را نباید خالی قرا دهیم وگرنه پیعام خطا بدهد

### ✅️ Implement

#### ❇️ رول اول[بررسی هر پارامتر توسط تابع مستقل]

* edit file `serialize.py` For Item: `priority

```python
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    def validate_priority(self, priority):
        if priority < 10 or priority > 20:
            raise serializers.ValidationError('priority is not ok')
        return priority

    class Meta:
        model = Todo
        fields = '__all__'
````

#### ❇️ رول دوم[یک تابع برای همه ورودی ها]

* edit file `serialize.py` For Item: `priority

```python
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        print(attrs)
        return super().validate(attrs)

    class Meta:
        model = Todo
        fields = '__all__'
````

## 🅱️ Serialize

* مفهوم Serialize: به فرایند تبدیل Data به فرمت نظیر JSON یا XML یا CSV که در API مورد استفاده قرار بگیرد می‌گویند
* مفهوم DeSerialize: به فرایند تبدیل Json به دیتا برای استفاده در مدل(یا درچ در دیتابیس)
* عبارت request.data: مقدار(مثلا)جی‌سان که هم اکنون Serialize است و باید برای ذخیره در دیتابیس Deserialize شود
* عبارت request.instance: مقدار دیتا(مثلا دیتابیس) که هم اکنون DeSerialize است و باید برای مورد استفاده قرار گرفتن درقالب(مثلا)جی‌سان Serialize شود

### ✅️ FunctionBase view

#### ❇️ /home/url.py

File: `url.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('index_page', views.index_page),
    path('second_page', views.second_page),
    path('legacy', views.todos_json),
]
```

#### ❇️ models.py

File: `/Todo/models.py`

```python
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.title} / Is Done: {self.is_done}'

    class Meta:
        db_table = 'todos'  # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
```

#### ❇️ view.py

file: `/home/view.py`

```python
from django.shortcuts import render
from todo.models import Todo
from django.http import HttpRequest, JsonResponse


def index_page(request):
    context = {
        'todos': Todo.objects.order_by('priority').all()
    }
    return render(request, 'home/index.html', context)


def todos_json(request: HttpRequest):  # module "request" is newer --> def todos_json(request: request)
    todos = list(Todo.objects.order_by('priority').all().values('title', 'is_done'))
    return JsonResponse({'todos': todos})


def second_page(myrequest):
    colors = ["red", "blue", "green", "gray", "yellow", "orange"]
    return JsonResponse({'colors': colors})

```

### ✅️ Legacy Serialize[FunctionBaseView]

#### ❇️ url.py

File: `/home/url.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('index_page', views.index_page)
    path('legacy', views.todos_json)
]
```

#### ❇️ models.py

File: `/Todo/models.py`

```python
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.title} / Is Done: {self.is_done}'

    class Meta:
        db_table = 'todos'  # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
```

#### ❇️ view.py

file: `/home/view.py`

```python
from django.shortcuts import render
from todo.models import Todo
from django.http import HttpRequest, JsonResponse, HttpResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


def index_page(request):
    context = {
        'todos': Todo.objects.order_by('priority').all()
    }
    return render(request, 'home/index.html', context)


@api_view(['GET'])
def todos_json(request: Request):
    todos = list(Todo.objects.order_by('priority').all().values('title', 'is_done'))
    return Response({'todos': todos}, status.HTTP_200_OK)
```

### ✅️ Serializers.ModelSerializer

#### ❇️ FunctionBaseView

> تبدیل دیتای داخل دیتابیس بصورت اتوماتیک به قالب جی‌سان برای ارسال به سمت کلاینت

```python
from rest_framework import serializers
```

##### Ⓜ️ models.py

File: `/todo/models.py`

```python
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.title} / Is Done: {self.is_done}'

    class Meta:
        db_table = 'todos'  # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
```

##### Ⓜ️ serializer.py

File: `/todo/serializers.py

```python
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = ['id', 'title', 'content']
        fields = '__all__'
````

##### Ⓜ️ view.py

File: `/todo/views.py`

```python
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def all_todos(request: Request):  # برای نمایش همه یا ایجاد یک دیتای جدید
    if request.method == 'GET':  # Ussing for get all items
        todos = Todo.objects.order_by('priority').all()
        todo_serializer = TodoSerializer(todos, many=True)  # Instance(for serialize)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':  # Ussing for add one item
        serializer = TodoSerializer(data=request.data)  # Data [NotInstance]
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

    return Response(None, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail_view(request: Request, todo_id: int):  # نیازمند کلید هست تا برمبنای یک کلید اقدام انجام شود
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':  # Ussing for get one item
        serializer = TodoSerializer(todo)  # Instance(for serialize)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method == 'PUT':  # Ussing for Edit one item(ویرایش)
        serializer = TodoSerializer(todo, data=request.data)  # Instance and data(for Deserialize) دیتا را داخل اینستنس میریزد
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':  # Ussing for delete one item
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
````

##### Ⓜ️ urls.py

File: `/todo/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.todo_detail_view),
]
```

##### Ⓜ️ url[global]

File: `/urls.py` #main urls

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('todos/', include('todo.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
```

#### ❇️ ClassBaseView

```python
from rest_framework import serializers
```

##### Ⓜ️ models.py

File: `/todo/models.py`

```python
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.title} / Is Done: {self.is_done}'

    class Meta:
        db_table = 'todos'  # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
```

##### Ⓜ️ serializer.py

File: `/todo/serializers.py

```python
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = ['id', 'title', 'content']
        fields = '__all__'
````

##### Ⓜ️ view.py

File: `/todo/views.py`

```python
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.decorators import api_view  # ✅️
from rest_framework.views import APIView  # ✅️


class TodosListApiView(APIView):  # برای نمایش همه یا ایجاد یک دیتای جدید# ✅️
    def get(self, request: Request):
        todos = Todo.objects.order_by('priority').all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)


class TodosDetailApiView(APIView):  # نیازمند کلید هست تا برمبنای یک کلید اقدام انجام شود# ✅️
    def get_object(self, todo_id: int):
        try:
            todo = Todo.objects.get(pk=todo_id)
            return todo
        except Todo.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self, request: Request, todo_id: int):
        todo = self.get_object(todo_id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request: Request, todo_id: int):
        todo = self.get_object(todo_id)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, todo_id: int):
        todo = self.get_object(todo_id)
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
````

##### Ⓜ️ url.py

File: `/todo/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.todo_detail_view),
    path('classbaseview/', views.TodosListApiView.as_view()),  # ✅️
    path('classbaseview/<int:todo_id>', views.TodosDetailApiView.as_view()),  # ✅️
]
```

##### Ⓜ️ urls.py[global]

File: `/urls.py` #main urls

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('todos/', include('todo.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
```

#### ❇️ Mixin

```python
from rest_framework import serializers
```

##### Ⓜ️ models.py

File: `/todo/models.py`

```python
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.title} / Is Done: {self.is_done}'

    class Meta:
        db_table = 'todos'  # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
```

##### Ⓜ️ serializer.py

File: `/todo/serializers.py

```python
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = ['id', 'title', 'content']
        fields = '__all__'
````

##### Ⓜ️ view.py

File: `/todo/views.py`

```python
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins  # ✅️


class TodosListMixinApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):  # ✅️
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)


class TodosDetailMixinApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):  # ✅️
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk):
        return self.update(request, pk)

    def delete(self, request: Request, pk):
        return self.destroy(request, pk)

````

##### Ⓜ️ urls.py

File: `/todo/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.todo_detail_view),
    path('classbaseview/', views.TodosListApiView.as_view()),
    path('classbaseview/<int:todo_id>', views.TodosDetailApiView.as_view()),
    path('mixins/', views.TodosListMixinApiView.as_view()),  # ✅️
    path('mixins/<pk>', views.TodosDetailMixinApiView.as_view()),  # ✅️
]
```

##### Ⓜ️ urls.py[global]

File: `/urls.py` #main urls

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('todos/', include('todo.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
```

#### ❇️ GenericView

```python
from rest_framework import serializers
```

##### Ⓜ️ models.py

File: `/todo/models.py`

```python
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.title} / Is Done: {self.is_done}'

    class Meta:
        db_table = 'todos'  # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
```

##### Ⓜ️ serializer.py

File: `/todo/serializers.py

```python
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = ['id', 'title', 'content']
        fields = '__all__'
````

##### Ⓜ️ view.py

File: `/todo/views.py`

```python
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins  # ✅️


class TodosGenericApiView(generics.ListCreateAPIView):  # ✅️
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer


class TodosGenericDetailView(generics.RetrieveUpdateDestroyAPIView):  # ✅️
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

````

##### Ⓜ️ urls.py

File: `/todo/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.todo_detail_view),
    path('classbaseview/', views.TodosListApiView.as_view()),
    path('classbaseview/<int:todo_id>', views.TodosDetailApiView.as_view()),
    path('mixins/', views.TodosListMixinApiView.as_view()),
    path('mixins/<pk>', views.TodosDetailMixinApiView.as_view()),
    path('generics/', views.TodosGenericApiView.as_view()),  # ✅️
    path('generics/<pk>', views.TodosGenericDetailView.as_view()),  # ✅️
]
```

##### Ⓜ️3.4.5.urls.py[global]

File: `/urls.py` #main urls

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('todos/', include('todo.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
```

#### ❇️ ViewSet

```python
from rest_framework import serializers
```

##### Ⓜ️ models.py

File: `/todo/models.py`

```python
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.title} / Is Done: {self.is_done}'

    class Meta:
        db_table = 'todos'  # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
```

##### Ⓜ️3.4.2.serializer.py

File: `/todo/serializers.py

```python
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = ['id', 'title', 'content']
        fields = '__all__'
````

##### Ⓜ️ view.py

File: `/todo/views.py`

```python
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets  # ✅️


class TodosViewSetApiView(viewsets.ModelViewSet):  # ✅️
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

````

##### Ⓜ️ urls.py

File: `/todo/urls.py`

```python
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter  # ✅️

router = DefaultRouter()  # ✅️
router.register('', views.TodosViewSetApiView)  # ✅️

urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.todo_detail_view),
    path('classbaseview/', views.TodosListApiView.as_view()),
    path('classbaseview/<int:todo_id>', views.TodosDetailApiView.as_view()),
    path('mixins/', views.TodosListMixinApiView.as_view()),
    path('mixins/<pk>', views.TodosDetailMixinApiView.as_view()),
    path('generics/', views.TodosGenericApiView.as_view()),
    path('generics/<pk>', views.TodosGenericDetailView.as_view()),
    path('viewsets/', include(router.urls)),  # ✅️
]
```

##### Ⓜ️ urls.py[global]

File: `/urls.py` #main urls

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('todos/', include('todo.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
```

#### ❇️ NestedSerialize

* اگر دو مدل بخواهند رابطه داشته باشند یعنی یکی از پارامترهای مدل(جدول) اول ارتباط مستقیم با مدل دیگر داشته باشند(یک به یک یا یک به چند یا یک به چند)
* Nested such as [1, 2, 3, 4, [14, 15, 16, 120 ,5]]

```python
from rest_framework import serializers
```

##### Ⓜ️ models.py

File: `/todo/models.py`

* IF Changing must to execute `migrations` command

```python
from django.db import models
from django.contrib.auth import get_user_model  # ✅️

user = get_user_model()  # ✅️


class Todo(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField()
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='todos')  # ✅️

    def __str__(self) -> str:
        return f'{self.title} / Is Done: {self.is_done}'

    class Meta:
        db_table = 'todos'  # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
```

##### Ⓜ️ serializzer.py

File: `/todo/serializers.py`

```python
from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model  # ✅️


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = ['id', 'title', 'content']
        fields = '__all__'


class UserSerialzier(serializers.ModelSerializer):  # ✅️
    todos = TodoSerializer(read_only=True, many=True)  # ✅️✅️✅️✅️

    class Meta:
        model = User
        fields = '__all__'
````

##### Ⓜ️ views.py

File: `/todo/views.py`

```python
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from .serializers import UserSerialzier  # ✅️
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.contrib.auth import get_user_model  # ✅️

User = get_user_model()  # ✅️


class UsersGenericApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialzier

````

##### Ⓜ️ urls.py

File: `/todo/urls.py`

```python
from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.TodosViewSetApiView)

urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.todo_detail_view),
    path('classbaseview/', views.TodosListApiView.as_view()),
    path('classbaseview/<int:todo_id>', views.TodosDetailApiView.as_view()),
    path('mixins/', views.TodosListMixinApiView.as_view()),
    path('mixins/<pk>', views.TodosDetailMixinApiView.as_view()),
    path('generics/', views.TodosGenericApiView.as_view()),
    path('generics/<pk>', views.TodosGenericDetailView.as_view()),
    path('viewsets/', include(router.urls)),
    path('users/', views.UsersGenericApiView.as_view()),
]
```

##### Ⓜ️ urls.py[global]

File: `/urls.py` #main urls

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('todos/', include('todo.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
```

## 🅱️ Paginations

* از دو ماژول زیر استفاده خواهد شد

```python
from rest_framework.pagination import PageNumberPagination  # use «page=۱|۲|۳|......» for pagenumber
from rest_framework.pagination import LimitOffsetPagination  # use «limit» for X record in one page and «offset» for begin at X record 
```

* سبب می‌شود خروجی «جی‌سان» تماما تغییر کند و عبارت‌های زیر را به صفحه اضافه نماید

1. عبارت count که حاوی تعداد کل آیتم‌های موجود است
2. رکورد next که شامل لینک آدرس صفحه بعدی است که ادامه آیتم‌ها را به نمایش گذارد
3. رکورد previous که شامل لینک آدرس صفحه قبلی است که آیتم‌های صفحه گذشته را به نمایش گذارد
2. رکورد result که حاوی دیتای آیتم‌های است که باید تعداد را تعیین کرد که چند آیتم در یک صفحه باید قرار بگیرد

### ✅️ پیاده‌سازی

#### ❇️ Global Setting File

File: `settingd.py`

```python
...

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
}
```

#### ❇️ Config in Views

#### ❇️ PageNumberPagination

##### Ⓜ️ genericsView

File: `/todo/views.py`

```python
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination  # ✅️


class TodosGenericApiView(generics.ListCreateAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    pagination_class = PageNumberPagination  # ✅️


class TodosGenericDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
```

##### Ⓜ️ viewsets

File: `/todo/views.py`

```python
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination  # ✅️


class TodosViewSetApiView(viewsets.ModelViewSet):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    pagination_class = PageNumberPagination  # ✅️
```

#### ❇️ LimitOffsetPagination

##### Ⓜ️ genericsView

File: `/todo/views.py`

```python
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination  # ✅️


class TodosGenericApiView(generics.ListCreateAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    pagination_class = LimitOffsetPagination  # ✅️


class TodosGenericDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
```

##### Ⓜ️ viewsets

File: `/todo/views.py`

```python
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination  # ✅️


class TodosViewSetApiView(viewsets.ModelViewSet):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    pagination_class = LimitOffsetPagination  # ✅️
```

#### ❇️ Config by Class

File: `/todo/views.py`

```python
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class TodosGenericApiViewPagination(PageNumberPagination):  # ✅️
    page_size = 3


class TodosGenericApiView(generics.ListCreateAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    pagination_class = TodosGenericApiViewPagination  # ✅️


class TodosGenericDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
```

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