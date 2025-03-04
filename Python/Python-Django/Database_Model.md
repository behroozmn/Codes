from traceback import print_tb

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
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), maxValueValidator(5)], default=0)
    short_description = models.CharField(max_length=360, null=True)
    is_active = models.BooleanField(default=False)
```

# 3.PythonConsole OR PythonShell

> دستورات زیر در شل پایتون باید زده شود تا تغییرات در دیتابیس لحاظ گردد

```
>>> from <Appname>.models import Product
>>> from dbehrooz.models import Product
>>> from product_module.models import Product
>>> new_product = Product(title='عنوان محصول', price=23000)
    new_product.save()
>>> new_product.all()
    new_product.all()[0].title
    new_product.all()[0].price
>>> secondRow=product.objects.all()[1] #حذف ستون دوم
    secondRow.delete()
>>> product.objects.get(id=4) #برگرداندن ردیف با آی‌دی۴ همچنین توجه شود که این دستورالزاما باید یک ردیف باشد و اگر چند ردیف باشد ارور میدهد 
>>>   
```

# 4.در ج مستقیم در دیتابیس 

```python
>>>  Product.objects.create(title='عنوان محصول', price=5000)
```


# 5.validator

توابعی که صحت‌ستجی می‌نمایند و اگر مقادیر موردنظر از نطر صحت آن صحیح نبود آنگاه ارور برمی‌گردانند
 


# 6. get() و filter()

```python
product.objects.get(id=4)
product.objects.get(title="متن")
product.objects.filter(is_active=True)
product.objects.filter(is_active=True, rating=5)
product.objects.filter(is_active=True, rating__lt=4)  # کوچکتر از ۴
product.objects.filter(is_active=True, rating__lte=4)  # کوچکتر مساوی از ۴
product.objects.filter(is_active=True, rating__gt=4)  # بزرگتر از ۴
product.objects.filter(is_active=True, rating__gte=4)  # بزرگتر مساوی از ۴
product.objects.get(headline__exact="متن")
product.objects.filter(headline__exact="متن")
product.objects.get(id__exact=14)
product.objects.filter(id__exact=14)
product.objects.filter(title__contains='متن')
product.objects.filter(title__icontains='متن')  # ignore case sensitive

# OR
>>> from django.db.models import Q

    product.objects.filter(Q(is_active=True) | Q(rating__gte=4))
    product.objects.filter(Q(is_active=True) | Q(rating__gte=4), rating__lt=5)


# کاهش کانکشن به دیتابیس در فیلترهای متعدد
>>> active_products= Product.objects.filter(is_active=True) #کوئری ایجاد می‌شود
>>> active_products= Product.objects.filter(price__gt=50000) #کوئری آپدیت مي‌شود
>>> active_products= Product.objects.filter(rating__gt=4)  #کوئری آپدیت مي‌شود
>>> print(active_products) #فقط یک بار کانکشن میزند
#اگر دوباره پرینت کنیم دیتا کش می‌شود و مجدد کوئری نخواهد زد

```



## Example1

```python
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    short_description = models.CharField(max_length=360, null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True,blank=True,editable=False)  # samsung galaxy s10 => samsung-galaxy-s10✅️

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # حذف فاصله و تبدیل به خط تیره✅️
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('device_details', args=[self.slug]) #✅️
    
    def __str__(self):
        return f"{self.title}: {self.price}\n"
```

*  گزینه db_index را وقتی در ورودی تابع قرار می‌دهیم یعین آن مشخصه مورد ایندکس گذاری قرار گیرد
