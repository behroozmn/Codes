# 1.slug from dictionary

اسلاگ(slug) کد شناسایی یک پست خاص که در دیتابیس نگه‌داری می‌شود
> نوعی دیتا که نشانگر آدرس منحصر به فرد برای یک مجموعه عناوین(مثلا پست) است

File: `urls.py`

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='starting-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.single_post, name='post-detail-page')✅️  # toplearn.com/posts/second-post
]
]
```

File: `view.py`

```    
from django.shortcuts import render
from datetime import date

# Create your views here.

posts_database = [
    {
        'slug': 'poos0001',✅️
        'title': '۰۰۰۱',
        'author': 'بهروز محمدی نسب ',
        'image': '001.jpg',
        'date': date(2021, 4, 5),
        'shortDescription': 'توضیحات اختصاری از پست شماره یکم',
        'content': 'محتویات پست اول'},
    { ... },
    { ... },
    {
        'slug': 'poos0004',✅️
        'title': '۰۰۰۴',
        'author': 'بهروز محمدی نسب ',
        'image': '010.jpg',
        'date': date(2025, 2, 27),
        'shortDescription': 'توضیحات اختصاری از پست شماره چهارم',
        'content': 'محتویات پست چهارم'
    },
]

def single_post(request, slug):
    post = next(post for post in posts_database if post['slug'] == slug)✅️ 
    # نکته: تابع next این است که اولین آیتم که با شرط مطابقت دارد را برگرداند
    # پست را برای من بیاور به ازای تمام پست هایی که درون پست‌دیتابیس هست به شرط اینکه کلید اسلاگ برابر با اسلاگ باشد
    return render(request, 'yazahra/postDetails.html', {'post': post})
    
```

File: `base.html`

```
<!DOCTYPE html>
<html lang="en">
    <body>
        <a href="{% url 'post-detail-page' slug='learning-django' %}">✅️
    </body>
</html>
```

# 2.slug from Database

File: `models.py`

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
    slug = models.SlugField(default="", null=False, db_index=True)  # samsung galaxy s10 => samsung-galaxy-s10✅️

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # حذف فاصله و تبدیل به خط تیره✅️
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('device_details', args=[self.slug]) #✅️
    
    def __str__(self):
        return f"{self.title}: {self.price}\n"

```

* گزینه db_index را وقتی در ورودی تابع قرار می‌دهیم یعین آن مشخصه مورد ایندکس گذاری قرار گیرد
* تابع slugify برای تبدیل خط فاصله به خط تیره در اسلاگ کاربرد دارد
* تابع save را به گونه‌ای تغییر دادیم که مضاعف بر کار قبلی خود اقدامات slugify را نیز انجام دهد و انحرافی از کار قبلی خود ندارد 