# 1.معرفی

* از دو ماژول زیر استفاده خواهد شد

```python
from rest_framework.pagination import PageNumberPagination  # use «page=۱|۲|۳|......» for pagenumber
from rest_framework.pagination import LimitOffsetPagination  # use «limit» for X record in one page and «offset» for begin at X record 
```

<div style="direction: rtl">

* سبب می‌شود خروجی «جی‌سان» تماما تغییر کند و عبارت‌های زیر را به صفحه اضافه نماید

1. عبارت count که حاوی تعداد کل آیتم‌های موجود است
2. رکورد next که شامل لینک آدرس صفحه بعدی است که ادامه آیتم‌ها را به نمایش گذارد
3. رکورد previous که شامل لینک آدرس صفحه قبلی است که آیتم‌های صفحه گذشته را به نمایش گذارد
2. رکورد result که حاوی دیتای آیتم‌های است که باید تعداد را تعیین کرد که چند آیتم در یک صفحه باید قرار بگیرد

</div>

# 2.پیاده‌سازی

## 2.1.Global Setting File

File: `settingd.py`

```python
...

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
}
```

## 2.2.Config in Views

### 2.2.1.PageNumberPagination

#### 2.2.1.1.genericsView

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

#### 2.2.1.2.viewsets

File: `/todo/views.py`

```python
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination  # ✅️


class TodosViewSetApiView(viewsets.ModelViewSet):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    pagination_class = PageNumberPagination  # ✅️
```

### 2.2.2.LimitOffsetPagination

#### 2.2.2.1.genericsView

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

#### 2.2.2.12.viewsets

File: `/todo/views.py`

```python
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination  # ✅️


class TodosViewSetApiView(viewsets.ModelViewSet):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    pagination_class = LimitOffsetPagination  # ✅️
```

## 2.3.Config by Class

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