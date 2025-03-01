# 1.Command migration

* `python3 manage.py makemigrations` # جستجوی تغییرات مدل
    + [ ]   نکته: به هیچ عنوان به محتویات پوشه «ماگریشن» دستکاری نکنید و این موارد باید اتوماتیک ساخته شوند
* `python3 manage.py migrate` # اعمال تغییرات مدل در دیتابیس .
    + [ ]    تمامی ماگریشن های ایجاد شده را در دیتابیس اعمال نماییم
* `python3 manage.py shell` # دسترسی به شل یا همان پایتون کنسول

اگر تغییراتی در مدل داده شد نیاز به بازسازی است و گرنه اگر در بدنه و دستورات پایتون بود نیازی نیست

# 2.MODEL

## example1

File: `models.py`

```python
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
```

## example2

File: `models.py`

```python
from django.db import models
from django.core.validators import MinValueValidator, maxValueValidator


class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), maxValueValidator(5)], default=0)
    short_description = models.CharField(max_length=360, null=True)
    is_active = models.BooleanFiled(default=False)
```

# 3.PythonConsole OR PythonShell

> دستورات زیر در شل پایتون باید زده شود تا تغییرات در دیتابیس لحاظ گردد

```
from product_module.models(اپلیکیشن جنگو) import Product(کلاس مدل شده از اپلیکیشن)
new_product = Product(title='عنوان محصول', price=23000)
new_product.save()
new_product.all()
new_product.all()[0].title
new_product.all()[0].price
```

# 4.validator

توابعی که صحت‌ستجی می‌نمایند و اگر مقادیر موردنظر از نطر صحت آن صحیح نبود آنگاه ارور برمی‌گردانند
 
