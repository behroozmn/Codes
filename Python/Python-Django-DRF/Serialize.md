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
        db_table = 'todos' # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
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

# 2.Legacy Serialize[FunctionBaseView]

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
        db_table = 'todos' # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
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

# 3.Serializers.ModelSerializer

# 3.1.FunctionBaseView

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
        db_table = 'todos' # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
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

File: `/todo/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.todo_detail_view),
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

# 3.2.ClassBaseView

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
        db_table = 'todos' # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
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

# 3.3.Mixin

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
        db_table = 'todos' # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
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

# 3.4.GenericView

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
        db_table = 'todos' # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
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
from rest_framework.views import APIView
from rest_framework import generics, mixins  # ✅️


class TodosGenericApiView(generics.ListCreateAPIView):  # ✅️
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer


class TodosGenericDetailView(generics.RetrieveUpdateDestroyAPIView):  # ✅️
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

````

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

# 3.4.ViewSet

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
        db_table = 'todos' # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
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
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets  # ✅️


class TodosViewSetApiView(viewsets.ModelViewSet):  # ✅️
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

````

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

# 3.5.NestedSerialize

* اگر دو مدل بخواهند رابطه داشته باشند یعنی یکی از پارامترهای مدل(جدول) اول ارتباط مستقیم با مدل دیگر داشته باشند(یک به یک یا یک به چند یا یک به چند)
* Nested such as [1, 2, 3, 4, [14, 15, 16, 120 ,5]]

```python
from rest_framework import serializers
```

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
        db_table = 'todos' # 'نام دلحواه برای اسم جدول دردیتابیس' # default: "AppName_ModelName"
```

File: `/todo/serializers.py

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

File: `/todo/views.py`

```python
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from .serializers import UserSerialzier# ✅️
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.contrib.auth import get_user_model# ✅️

User = get_user_model() # ✅️


class UsersGenericApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialzier

````

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