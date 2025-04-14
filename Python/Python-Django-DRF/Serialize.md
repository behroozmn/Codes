<div style="direction: rtl">

* مفهوم Serialize: به فرایند تبدیل Data به فرمت نظیر JSON یا XML یا CSV که در API مورد استفاده قرار بگیرد می‌گویند
* مفهوم DeSerialize: به فرایند تبدیل Json به دیتا برای استفاده در مدل(یا درچ در دیتابیس)
* عبارت request.data: مقدار(مثلا)جی‌سان که هم اکنون Serialize است و باید برای ذخیره در دیتابیس Deserialize شود
* عبارت request.instance: مقدار دیتا(مثلا دیتابیس) که هم اکنون DeSerialize است و باید برای مورد استفاده قرار گرفتن درقالب(مثلا)جی‌سان Serialize شود

</div> 

# 1.FunctionBase view

File: `/home/url.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('index_page', views.index_page)
    path('legacy', views.todos_json)
]
```

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
        db_table = 'todos'
```

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


def todos_json(request: HttpRequest):
    todos = list(Todo.objects.order_by('priority').all().values('title', 'is_done'))
    return JsonResponse({'todos': todos})
```

# 2.Legacy Serialize

File: `/home/url.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('index_page', views.index_page)
    path('legacy', views.todos_json)
]
```

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
        db_table = 'todos'
```

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

# 3.Serialize by [serializers.ModelSerializer]

> تبدیل دیتای داخل دیتابیس بصورت اتوماتیک به قالب جی‌سان برای ارسال به سمت کلاینت

```python
from rest_framework import serializers
```

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
        db_table = 'todos'
```

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
def all_todos(request: Request):
    if request.method == 'GET':
        todos = Todo.objects.order_by('priority').all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

    return Response(None, status.HTTP_400_BAD_REQUEST)
````

File: `/todo/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_todos)
]
```

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

