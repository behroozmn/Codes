####  افزودن جداول در داشتبورد مدیریت ادمین
```python
from . import models
admin.site.register(models.Product)
```

#### تغییر زبان داشبورد از انگلیسی به فارسی
File: setting.py
`LANGUAGE_CODE = 'fa-ir'`

تنظیمات  مدل پیرامون صفحه ادمین چنگو
file: `admin.py`

```python
from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):  # تنظیمات مدل پروداکت در پنل ادمین جنگو
    # readonly_fields = ['slug', 'rating'] # هیچگاه در پنل ادمین نمی‌توانیم اسلاگ را تغییر بدهیم
    prepopulated_fields = {
        'slug': ['title']  # خودش از نوشته عنوان عبارت اسلاگ را کامل می‌کند(در پنل مدیریت جنگو) 
    }

    list_display = ['__str__', 'price', 'rating', 'is_active', 'short_description', 'title']
    list_filter = ['rating', 'is_active', 'short_description', 'title']
    list_editable = ['rating', 'is_active', 'short_description', 'title']


admin.site.register(models.Product, ProductAdmin)


```