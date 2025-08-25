<div dir="rtl">

# 1. 🅰️ Django

File: `main_urls.py`

```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainindex),
]
```

File: `main_views.py`

```python
from django.http import HttpResponse


def mainindex(request):
    return HttpResponse("index page(صفحه اصلی)")
```

## 1.1. 🅱️ pages

### 1.1.1. ✅️ 404

> نام فایل باید دقیقا ۴۰۴ باشد و اگر نام دیگری باشد مورد پذیرش نیست و باید داخل مسیر تمپلیت باشد

```python
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string

days = {
    'saturday': 'this is satureday in dictionary',
    'sunday': 'this is sunday in dictionary',
    'monday': 'this is monday in dictionary',
    'tuesday': 'this is tuesday in dictionary',
    'wednesday': 'this is wednesday in dictionary',
    'thursday': 'this is thursday in dictionary',
    'friday': 'this is friday in dictionary'
}


def dynamic_days(reqeust, day):
    day_data = days.get(day)

    if day_data is None:
        # روش اول
        raise Http404  # اتوماتیک در پوشه تمپلیت دنبال فایل با نام ۴۰۴ می‌گردد

        # روش دوم
        # response_data = render_to_string('404.html') 
        # return HttpResponseNotFound(response_data)

    context = {
        "data": day_data,
        "day": f'selected DAY is {day}'
    }
    return render(reqeust, 'challenges/challenge.html', context)
```

### 1.1.2. ✅️ masterPage or MainPage or BasePage or LayoutePage

با هدف ایجاد یک صفحه اصلی که بعنوان صفحه پیش‌فرض مد نظر قرار گیرد و بقیه صفحات از آن مشتق شده و هر صفحه بتواند تگ های سفارشی خود را داشته باشد

1. create `base.html` in `template` Directory
   > Note: دایرکتوری «تمپلیت» باید در فایل ستینگ بعنوان مسیر پیش‌فرض تمپلیت‌های پروژه لحاظ شده باشد

3. File: `base.html`
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>{% block title %}{% endblock %}</title>
       {% block header_reference %}{% endblock %}
   </head>
   <body>
   {% block content %}{% endblock %}
   {% block footer_references %}{% endblock %}
   </body>
   </html>
   ```
   > در هرصفحه‌ای که ازاین صفحه ارث‌بری نماید، بااستفاده از نام بلاک‌های بالا، می‌توان دیتای سفارشی همان صفحه را در محتوی بلاک‌ها درج نمود
4. File: `subPage1.html`
   ```html
     {% extends 'base.html' %}      #✅️ برای ارث بری باید این خط در ابتدا باشد
     {% block title %}My Blog{% endblock %}
     {% block content %}
         <header id="main-navigation">
             <h1><a href="">Toplearn Blog</a></h1>
             <nav>
                 <a href="">All Posts</a>
             </nav>
         </header>
       <section id="welcome">
       <header>
              <img src="{% static 'blog/images/master.jpg' %}" alt="Toplearn - Author Of This blog">
              <h2>Toplearn blog project</h2>
          </header>
          <p>Hi, My name is mohammad, Im a Teacher in Toplearn</p>
      </section>
     {% endblock %}
         ```
5. File: `view.py`
   ```
   from django.shortcuts import render
   def index(request):
       return render(request, 'subPage1.html')
   ```

Note: [URL](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#block)

### 1.1.3. ✅️ Include

تهیه بخش های متفاوت از تکه‌ها صفحه و استفاده در صفحه اصلی

> note: `include` tag must use in `Content` block\
> یعنی معمولا در بدنه مورد استفاده قرار میگیرید

در بخش زیر یک تکه کد را خواهید دید که قرار است به بدنه صفحه ای متصل گردد\
File: `topic.html`

```html

<header>
    <nav>
        <a href="http://itsee.ir">روزهای هفته</a>
    </nav>
</header>
```

صفحه ای که تکه کد بالا باید به آن وصل گردد\
File: `index.html`

```html
{% extends 'base.html' %}
{% block content %}
{% include "topic.html"%}✅️
{% endblock %}
```

### 1.1.4. ✅️ Include by `send Parameter`

تهیه بخش های متفاوت از تکه‌ها صفحه و استفاده در صفحه اصلی

File: `topic.html`

```html

<header>
    <nav>
        <a href="{% url 'days_list' %}">روزهای هفته</a>
    </nav>
    <p>{{ active_page|title }}</p>
</header>
```

صفحه ای که تکه کد بالا باید به آن وصل گردد\
File: `index.html`

```html
{% extends 'base.html' %}
{% block content %}
{% include "topic.html" with active_page="daysIndex" %}✅️
<ul>
    {% for item in days %}
    <li><a href="{% url 'days-of-week' item %}"> {{item}} </a></li>  <!--  {% url 'days-of-week' day %}: USSING Reverse URL -->
    {% endfor %}
</ul>
{% endblock %}
```

File: `page2.html`

```html
{% extends 'base.html' %}

{% block page_title %}days info{% endblock  %}

{% block content %}
{% include "topic.html" with active_page="dayDetail" %}✅️
{% if data is not None %}
<h2>{{ data }}</h2> <!-- متغیر دیتا چیزی است که در تابع پایتون استفاده شد است و در آن فایل پایتون به این صفحه اشاره شده است-->
{% else %}
<p>there is no data</p>
{% endif %}
{% endblock  %}
```

### 1.1.5. ✅️ استفاده از جاوااسکریپ در برخی از صفحات

```python
{ % block
footer_references %}
< script >
console.log('hello')
< / script >
{ % endblock %}

```

> Note: میتوان در تکه صفحه‌ها تگ اسکریپت یعنی جاوا اسکریپت را هم درج نماییم

## 1.2. 🅱️ StaticFiles

1. مسیر فایل‌های استاتیک پروژه باید درفایل تنظیمات تعریف شده باشد
   `INSTALLED_APPS = [ ...'django.contrib.staticfiles' ... ]`
2. File: `settings.py`

> * `STATICFILES_DIRS = [BASE_DIR / 'static' ]`

3. بالای فایل اچ تی ام ال عبارت زیر را درج نمایید
   `{% load static %}`
4. اگر بخوایم فایلی از فایل‌های استاتیک را به پروژه وصل نمایید باید از روش زیر استفاده نمایید

   ```html
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>{% block title %}{% endblock %}</title>
       <link rel="stylesheet" href="{% static 'CustomCSS.css' %}">
       {% block header_reference %}{% endblock %}
   </head>
   <body>
   {% block content %}{% endblock %}
   {% block footer_references %}{% endblock %}
   </body>
   </html>
   ```

> اگر اپلیکیشن بالا بود و با ارور ۴۰۴ مواجه شدیم باید سرویس جنگو را ریست نماییم

## 1.3. 🅱️ File

### 1.3.1. ✅️ Upload

#### 1.3.1.1. ❇️ Legacy

Files: `views.py`

```python
from django.shortcuts import render, redirect
from django.views import View


def store_file(file):
    with open('temp/image.jpg', "wb+") as dest:  # نکته: مسیر تمپ باید در مسیر اصلی پروژه باشد
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):  # ✅️
    def get(self, request):
        return render(request, 'contact_module/create_profile_page.html')

    def post(self, request):
        # print(request.FILES)
        store_file(request.FILES['profile'])  # این نام پروفایل در تگ فرم بعنوان نام است
        return redirect('/contact-us/create-profile') 
```

Files: `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('create-profile/', views.CreateProfileView.as_view(), name='create_profile_page'),  # ✅️
]
```

Files: `create_profile_page.html`

```html
{% extends 'shared/_layout.html' %}
{% block content %}
<div id="contact-page" class="container">
    <div class="bg">
        <div class="row">
            <div class="col-sm-8">
                <div class="contact-form">
                    <h2 class="title text-center">ثبت پروفایل</h2>
                    <div class="status alert alert-success" style="display: none"></div>
                    <form id="main-contact-form" class="contact-form row" action="{% url 'create_profile_page' %}" # ✅️
                          method="post" enctype="multipart/form-data"> # ✅️ enctype
                        {% csrf_token %}
                        <input type="file" name="profile"> # ✅️
                        <div class="form-group col-md-12">
                            <button type="submit" class="btn btn-primary pull-right">ارسال</button>
                            # ✅️
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

#### 1.3.1.2. ❇️ Upload [By Class]]

#### 1.3.1.3. ❇️ Upload [By Class]]

save name in Database and save in custome dir

Files: `forms.py`

```python
class ProfileForm(forms.Form):
    user_image = forms.FileField()
```

Files: `models.py`

```python
class UserProfile(models.Model):
    image = models.FileField(upload_to='images')  # درفایل تنظیمات تصریح شده است که این فولدر «ایمیچ» باید در داخل کدام مسیر ایجاد شود و سبب نگهداری فایل‌ها گردد
```

Files: `views.py`

```python
from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactUsModelForm, ProfileForm
from django.views.generic.edit import FormView, CreateView
from .models import ContactUs, UserProfile  # ✅️


def store_file(file):
    with open('temp/image.jpg', "wb+") as dest:  # نکته: مسیر تمپ باید در مسیر اصلی پروژه باشد
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'contact_module/create_profile_page.html', {
            'form': form
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            return redirect('/contact-us/create-profile')

        return render(request, 'contact_module/create_profile_page.html', {
            'form': submitted_form
        })
```

Files: `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('create-profile/', views.CreateProfileView.as_view(), name='create_profile_page')
]
```

Files: `create_profile_page.html`

```html
{% extends 'shared/_layout.html' %}
{% block content %}
<div id="contact-page" class="container">
    <div class="bg">
        <div class="row">
            <div class="col-sm-8">
                <div class="contact-form">
                    <h2 class="title text-center">ثبت پروفایل</h2>
                    <div class="status alert alert-success" style="display: none"></div>
                    <form id="main-contact-form" class="contact-form row" action="{% url 'create_profile_page' %}"
                          method="post" enctype="multipart/form-data">
                        {% csrf_token %}
                        {{ form }} # ✅️
                        <div class="form-group col-md-12">
                            <button type="submit" class="btn btn-primary pull-right">ارسال</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

File: `setting.py`

`MEDIA_ROOT = BASE_DIR / 'uploads'  #مدیاهای ارسالی کاربر بصورت پیش‌فرض کجا ذخیره گردد`

* بدلیل تغییرات در دیتابیس باید دستورات تغییرات در دیتابیس زده شود

#### 1.3.1.4. ❇️ Filter[Upload Only Image]

1. `python -m pip install pillow`
2. Files: `forms.py`
    ```python
   class ProfileForm(forms.Form):
      user_image = forms.ImageField()
   ```
3. Files: `models.py`
   ```python
   class UserProfile(models.Model):
      image = models.ImageField(upload_to='images')  # درفایل تنظیمات تصریح شده است که این فولدر «ایمیچ» باید در داخل کدام مسیر ایجاد شود و سبب نگهداری فایل‌ها گردد
   ```

#### 1.3.1.5. ❇️ Upload [By CreateView]

1. Files: `views.py`
   ```python
   from django.views.generic.edit import CreateView
   from .models import UserProfile
   
   class CreateProfileView(CreateView):
      template_name = 'contact_module/create_profile_page.html'
      model = UserProfile
      fields = '__all__'
      success_url = '/contact-us/create-profile'
   ```
2. Files: `models.py`
   ```python
   class UserProfile(models.Model):
      image = models.FileField(upload_to='images') # درفایل تنظیمات تصریح شده است که این فولدر «ایمیچ» باید در داخل کدام مسیر ایجاد شود و سبب نگهداری فایل‌ها گردد
   ```
3. Files: `forms.p
   ```python
   class ProfileForm(forms.Form):     # ❌ به این نیازی نخواهد بود
      user_image = forms.ImageField() # ❌ به این نیازی نخواهد بود
   ```

### 1.3.2. ✅️ Show

1. Files: `views.py`
   ```python
   from django.shortcuts import render, redirect
   from django.views import View
   from .forms import ContactUsModelForm, ProfileForm
   from django.views.generic.edit import FormView, CreateView
   from .models import ContactUs
   
   class ProfilesView(ListView):# ✅️
      model = UserProfile
      template_name = 'contact_module/profiles_list_page.html'
      context_object_name = 'profiles' # change name «object_list» to «products» for use in html files
   ```   
2. Files: `profiles_list_page.html`
   ```html
   {% extends 'shared/_layout.html' %}
   {% block title %}
       لیست پروفایل ها
   {% endblock %}
   {% block content %}
       <div class="container">
           <div class="row">
               <div class="col-md-12">
                   <ul>
                       {% for profile in profiles %}
                           <li>
                               <img src="{{ profile.image.url }}" alt="" width="150"> # ✅️
                           </li>
                       {% endfor %}
                   </ul>
               </div>
           </div>
       </div>
   {% endblock %}
   ```
3. Files: `urls.py`
   ```python
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('', views.ContactUsView.as_view(), name='contact_us_page'),
       path('create-profile/', views.CreateProfileView.as_view(), name='create_profile_page'),
       path('profiles/', views.ProfilesView.as_view(), name='profiles_page'),
   ]
   ```
4. Files: `settings.py`
   ```python
   MEDIA_URL = '/medias/'
   ```
5. Files: `main_urls.py`
   ```python
   from django.contrib import admin
   from django.urls import path, include
   from django.conf.urls.static import static
   from django.conf import settings
   urlpatterns = [
       path('', include('home_module.urls')),
       path('contact-us/', include('contact_module.urls')),
       path('products/', include('product_module.urls')),
       path('admin/', admin.site.urls),
   ]
   urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

## 1.4. 🅱️ Database Model

### 1.4.1. ✅️ Info

* نکته: به هیچ عنوان به محتویات پوشه «ماگریشن» دستکاری نکنید و این موارد باید اتوماتیک ساخته شوند
* اگر تغییراتی در مدل داده شد نیاز به بازسازی است و گرنه اگر در بدنه و دستورات پایتون بود نیازی نیست
* گزینه db_index را وقتی در ورودی تابع قرار می‌دهیم یعنی آن مشخصه مورد ایندکس گذاری قرار گیرد

```shell
python3 manage.py makemigrations # جستجوی تغییرات مدل
python3 manage.py migrate # اعمال تغییرات مدل در دیتابیس
python3 manage.py shell # دسترسی به شل یا همان پایتون کنسول

```

### 1.4.2. ✅️ Models

Example1️⃣️: File: `models.py`

```python
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
   ```

Example2️⃣️:File: `models.py`

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

Example3️⃣️: File: `models.py`

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
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, editable=False)  # samsung galaxy s10 => samsung-galaxy-s10✅️

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # حذف فاصله و تبدیل به خط تیره✅️
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('device_details', args=[self.slug])  # ✅️

    def __str__(self):
        return f"{self.title}: {self.price}\n"
```

### ✅️ PythonConsole OR PythonShell

> دستورات زیر در شل پایتون باید زده شود تا تغییرات در دیتابیس لحاظ گردد

```python
>> from < Appname >.models
import Product

>> from dbehrooz.models import Product

>> from product_module.models import Product

>> new_product = Product(title='عنوان محصول', price=23000)
new_product.save()

>> new_product.all()
new_product.all()[0].title
new_product.all()[0].price

>> secondRow = product.objects.all()[1]  # حذف ستون دوم
secondRow.delete()

>> product.objects.get(id=4)  # برگرداندن ردیف با آی‌دی۴ همچنین توجه شود که این دستورالزاما باید یک ردیف باشد و اگر چند ردیف باشد ارور میدهد 

>> Product.objects.create(title='عنوان محصول', price=5000)  # در ج مستقیم در دیتابیس   
```

### ✅️ validator

توابعی که صحت‌ستجی می‌نمایند و اگر مقادیر موردنظر از نطر صحت آن صحیح نبود آنگاه ارور برمی‌گردانند

### ✅️ get() و filter()

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

# 2. OR
>> from django.db.models import Q

product.objects.filter(Q(is_active=True) | Q(rating__gte=4))
product.objects.filter(Q(is_active=True) | Q(rating__gte=4), rating__lt=5)

# 3. کاهش کانکشن به دیتابیس در فیلترهای متعدد
>> active_products = Product.objects.filter(is_active=True)  # کوئری ایجاد می‌شود
>> active_products = Product.objects.filter(price__gt=50000)  # کوئری آپدیت مي‌شود
>> active_products = Product.objects.filter(rating__gt=4)  # کوئری آپدیت مي‌شود
>> print(active_products)  # فقط یک بار کانکشن میزند
# 4. اگر دوباره پرینت کنیم دیتا کش می‌شود و مجدد کوئری نخواهد زد


products = list(Product.objects.all().order_by('-price')[:5])
products = list(Product.objects.order_by('price').allS().values('title', 'is_active'))  # مرتب‌سازی برحسب قیمت و تنها برگردداندن دو ستون
```

### ✅️ Internal Parameter

* `editable=False` سبب می‌شود که پارامتر جدول هنگام افزودن در پنل مدیریت جنگو نمایش داده نشود
* `related_name='product_set'` واکشی تمام روابط برعکس درصورتی که از کلید خارجی استفاده نماییم

file:`model.py`

```python
class Product(models.Model):
    # ...
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, related_name='BEHROOOZ')  # ✅️
    # ...
```

file:`view.py`

```
from [نام‌ماژول].models import Product,ProductCategory
   # ...
   categoryname=ProductCategory.objects.get(title='دسته‌بندی۱')
   categoryname.BEHROOOZ.all() # در جدول محصولات همه مواردی که دارای نام «دسته‌بندی۱» است را نمایش می‌دهد
```

### ✅️ class meta

این قابلیت وجود دارد که داخل کلاس مدل یک کلاس دیگر تعریف کنیم تا به بیان خصوصیات در تنظیمات ادمین بپردازد

```python
class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        db_table = 'نام دلحواه برای اسم جدول دردیتابیس'  # default: "AppName_ModelName"

```

### ✅️ UserModel(Custom)

1. اگر در ابتدای کار هستید یک اپلیکیشن استارت نمایید
   `python manage.py startapp account_module`
2. File: `account_module/models.py`
   ```python
    from django.contrib.auth.models import AbstractUser
    from django.db import models
    
    
    # Create your models here.
    
    class User(AbstractUser):
        mobile = models.CharField(max_length=20, verbose_name='تلفن همراه')
        email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    
        class Meta:
            verbose_name = 'کاربر'
            verbose_name_plural = 'کاربران'
    
        def __str__(self):
            return self.get_full_name()
   ```
3. File: `setting.py`
   ```python
   AUTH_USER_MODEL = 'account_module.user' # نام مآژول و یک نقطه و نانم کلاس مدل یعنی نیاز به آوردن نام فایل نیست
   ``` 
4. change on database
    * `python3 manage.py makemigrations`
    * `python3 manage.py migrate`
5. اگر در وسط پروژه هستید و کلی تغییرات در دیتابیس دادید
    * غیر فعال سازی اپلیکیشن‌های گذشته درفایل ستینگ
    * غیرفعال سازی یوآراِل در فایل `urls.py`
    * حذف محتوی پوشه account_module/migrations
        * نکته: فایل `__init__.py` پاک نشود
6. change on database
    * `python3 manage.py makemigrations`
    * `python3 manage.py migrate`

## 🅱️ URL valueType

### ✅️ int, string

در «یوآر اِل» می‌توان دیتای از نوع اینتیجر یا استرینگ ارسال کرد که در نمونه زیر می‌بینید

File: `url.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    # ترتیب مهم است
    path('', views.showItems),
    path('show', views.usershow),
    path('edit', views.useredit),
    path('<int:ids>', views.dynamic_id),  # ترتیب مهم است ✅️
    path('<str:name>', views.dynamic_name, name='UniqName1_behrooz'),  # ترتیب مهم است✅️
]

```

File: `view.py`

```python
def dynamic_id(request, ids):
    # call when  url is integer 
    redirect_url = reverse('UniqName1_behrooz')
    return HttpResponseRedirect(redirect_url)


def dynamic_name(request, name):
    pass  # کدهایی که در هنگام ارسال رشته باید فراخوانی شوند
```

### ✅️ slug from dictionary

* اسلاگ(slug) کد شناسایی یک پست خاص که در دیتابیس نگه‌داری می‌شود
* نوعی دیتا که نشانگر آدرس منحصر به فرد برای یک مجموعه عناوین(مثلا پست) است

File: `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='starting-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.single_post, name='post-detail-page')  # toplearn.com/posts/second-post
]
```

File: `view.py`

```python
from django.shortcuts import render
from datetime import date

# 5. Create your views here.

posts_database = [
    {
        'slug': 'poos0001',  # ✅️
        'title': '۰۰۰۱',
        'author': 'بهروز محمدی نسب ',
        'image': '001.jpg',
        'date': date(2021, 4, 5),
        'shortDescription': 'توضیحات اختصاری از پست شماره یکم',
        'content': 'محتویات پست اول'},
    {...},
    {...},
    {
        'slug': 'poos0004',  # ✅️
        'title': '۰۰۰۴',
        'author': 'بهروز محمدی نسب ',
        'image': '010.jpg',
        'date': date(2025, 2, 27),
        'shortDescription': 'توضیحات اختصاری از پست شماره چهارم',
        'content': 'محتویات پست چهارم'
    },
]


def single_post(request, slug):
    post = next(post for post in posts_database if post['slug'] == slug)  # ✅️
    # نکته: تابع next این است که اولین آیتم که با شرط مطابقت دارد را برگرداند
    # پست را برای من بیاور به ازای تمام پست هایی که درون پست‌دیتابیس هست به شرط اینکه کلید اسلاگ برابر با اسلاگ باشد
    return render(request, 'yazahra/postDetails.html', {'post': post})

```

File: `base.html`

```html
<!DOCTYPE html>
<html lang="en">
<body>
<a href="{% url 'post-detail-page' slug='learning-django' %}">
</body>
</html>
```

### ✅️ slug from Database

* گزینه db_index را وقتی در ورودی تابع قرار می‌دهیم یعین آن مشخصه مورد ایندکس گذاری قرار گیرد
* تابع slugify برای تبدیل خط فاصله به خط تیره در اسلاگ کاربرد دارد
* تابع save را به گونه‌ای تغییر دادیم که مضاعف بر کار قبلی خود اقدامات slugify را نیز انجام دهد و انحرافی از کار قبلی خود ندارد

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
        return reverse('device_details', args=[self.slug])  # ✅️

    def __str__(self):
        return f"{self.title}: {self.price}\n"

```

## 🅱️ Admin

* افزودن جداول در داشتبورد مدیریت ادمین

```python
from . import models

admin.site.register(models.Product)
```

* تنظیمات مدل پیرامون صفحه ادمین چنگو

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

## 🅱️ Session

* برای ذخیره اطلاعات ازنوع آبجکت از سشن استفاده نکنید
* برای ذخیره اطلاعات سبک نظیر آی دی یا رشته متنی یا بولین یامشابه استفاده شود

```python
request.session["Key"] = Value  # Suyntax Create
Value = request.session["Key"]  # Syntax Read[1] اگر پیدا نکند ارور برمیگرداند 
Value = request.session.get('Key')  # Syntax Read[2] اگر پیدا نکند مقدار هیچی برمیگرداند و ارور نمی‌دهد
```

## 🅱️ Paging

* اگر تعداد آیتم‌ها زیاد باشد آنگاه برای نمایش تعداد زیاد نیاز به صفحه بندی داریم

File: `product_module/views.py`

```python
class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product  # تعیین این که از کدام جدول دیتا باید استخراج کند و به صفحه اچ تی ام ال بفرستد 
    context_object_name = 'products'  # change name «object_list» to «products» for use in html files
    ordering = ['-price']  # مرتب‌سازی بر پایه یک پارامتر برحسب نزولی یا سعودی 
    paginate_by = 6  # تعداد چند پارامتر در یک صفحه نمایش داده شود
```

File: `/product_module/templates/product_module/product_list.html`

```html
<!-- ... -->
<div class="col-sm-9 padding-right">
    <div class="features_items"><!--features_items-->
        <h2 class="title text-center">محصولات عمده</h2>
        {% for product in products %}
        {% include 'includes/product_item_partial.html' with product=product %}
        {% endfor %}
        <div class="clearfix"></div>
        <ul class="pagination">
            {% if page_obj.has_previous %}# ✅️
            <li><a href="?page={{ page_obj.previous_page_number }}">قبلی</a></li>
            {% endif %}
            {% for pageNumber in paginator.page_range %}# ✅️
            <li class="{% if page_obj.number == pageNumber %} active {% endif %}">
                <a href="?page={{ pageNumber }}">{{ pageNumber }}</a># ✅️
            </li>
            {% endfor %}
            {% if page_obj.has_next %}# ✅️
            <li><a href="?page={{ page_obj.next_page_number }}">بعدی</a></li>
            # ✅️
            {% endif %}

        </ul>
    </div><!--features_items-->
</div>
<!-- ... -->
```

## 🅱️ Application

* افزودن یک ماژول یا به‌اصلاح یک اپلیکیشن(یک پوشه)جدید به‌پروژه ولی همچنان مدیریت اصلی برنامه با پوشه اصلی است
* شکستن پروژه بزرگ به ماژول یا برنامه کوچک‌تر تا بتوانیم هر کدام از قسمت‌ها را مستقل مدیریت کنیم

### ✅️ Add new application

1. Execute: `python manage.py startapp myNewApp`
2. Edit `myNewApp>settings.py`
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',️
       'myNewApp' , # ✅️
   ]
   ```
3. Edit file: `mainProject > main_urls.py`
   ```python
   from django.urls import path, include
   urlpatterns = [
      # ...
      path('Example1/', include('myNewApp1.urls'))
      # ...
   ]
   ```

4. Create `myNewApp1>urls.py`
   ```python
   from django.urls import path
   from . import views
   urlpatterns = [
      path('', views.madulewithouturl),
      path('show', views.usershow),
      path('edit', views.useredit)
   ]
   ```
5. File: `myNewApp1>views.py`
    ```python
   from django.http import HttpResponse
   # Create your views here.
   def madulewithouturl(request):
       return HttpResponse('صفحه اصلی  زیر برنامه یا ماژول') 
   def usershow(request):
       return HttpResponse('صفحه نمایش کاربران')
   def useredit(request):
       return HttpResponse('صفحه ادیت کاربران')
   ```

### available urls

* 127.0.0.1:8080 #function madulewithouturl
* 127.0.0.1:8080/Example1/show #function usershow
* 127.0.0.1:8080/Example1/edit #function useredit

## 🅱️ Rest API

### ✅️ BasicForm

* Method: تعیین نوع درخواست که از نوع گت باشد یا پست
    * GET
        * بصورت پیش‌فرض همه درخواست‌ها گت هست مگر اینکه تغییر داده شود
        * ارسال دیتا در «یوآراِل»
        * استفاده معمول در هنگام فیلتر کردن
    * POST
        * ارسال دیتا در هِدِر
        * ```python
          if request.method == 'POST'
             print(request.POST)
             return redirect(reverse('URL_NAME'))
          ```
* Action: ارسال فرم به کدام آدرس از «یوآراِل»ها
    * اگر قرار داده نشود به همان «یوآراِل» که فرم درآن ارسال شده است ارسال می‌شود(هرصفحه که باشیم)
    * `<form action="javascript:alert('sent');" id="form">...</form>`
* Name: در هِدِر پارامتر به همین نام به سمت سرور ارسال خواهد شد
* required:‌اگر بخواهیم فرم به سمت سرور ارسال بشود باید حتما پارامتر مورد نظر پر شده باشد
* placeholder: مقدار پیشفرض برای نمایش مقدار خالی چه باشد
* value: مقداری که بصورت پیشفرض ارسال شود
    * `<input type="submit" name="submit" class="" value="ارسـال">`
    * `<button type="submit" class="">ارسال</button`
* inputType
    * type=text
    * type=email
    * type=submit
    * type=color
    * type=time
    * type=date
    * type=button
    * type=checkbox
    * type=datetime-local
    * type=file
    * type=hidden
    * type=image
    * type=month
    * type=number
    * type=password
    * type=radio
    * type=range
    * type=reset
    * type=search
    * type=tel
    * type=url
    * type=week

* csrf_token: برای اطمینان ازاینکه مبدا ارسال کننده صحیح می‌باشد
* نکته: ارور CSRF Token Error زمانی رخ می‌دهد که از توکن زیر در خلال فرم استفاده نشده باشد و ممنوعیت دسترسی ایجاد شده باشد
    * `{% csrf_token %}`

File: `Htmlfile.html`

```html

<form id="main-contact-form" class="contact-form row" name="contact-form" method="post">
    <div class="form-group col-md-6">
        <input type="text" name="name" class="form-control" required="required"
               placeholder="نام">
    </div>
    {% csrf_token %}
    <div class="form-group col-md-6">
        <input type="email" name="email" class="form-control" required="required"
               placeholder="ایمیـل">
    </div>
    <div class="form-group col-md-12">
        <input type="text" name="subject" class="form-control" required="required"
               placeholder="موضـوع">
    </div>
    <div class="form-group col-md-12">
        <textarea name="message" id="message" required="" class="form-control" rows="8" placeholder="پیغـام شمـا"></textarea>
    </div>
    <div class="form-group col-md-12">
        <button type="submit" class="">ارسال</button
    </div>
</form>
```

### ✅️ ClassForm

جنگو قابلیت مدیرت پارامترهای فرم را در قالب کلاس مهیا نموده است تا تمامی موارد را توسط کلاس پارامتردهی نمود

Files: `Forms.py`

```python
from django import forms


class ContactUsForm(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی'
                                , max_length=50
                                , error_messages={'required': 'لطفا نام و نام خانوادگی خود را وارد کنید', 'max_length': 'نام و نام خانوادگی نمی تواند بیشتر از 50 کاراکتر باشد'}
                                , widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'})
                                )
    email = forms.EmailField(label='ایمیل ', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))
    subject = forms.CharField(label='عنوان', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان'}))
    text = forms.CharField(label='متن پیام', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن پیام', 'rows': '5', 'id': 'message'}))
```

Files: `views.py`

```python
from .Forms import ContactUsForm


def contact_us_page(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)  # or -> contact_form = ContactUsForm(request.POST or None)
        if contact_form.is_valid():  # اگر همه پارامترهای داخل فرم دیتای صحیح داشت و مناسب بود
            print(contact_form.cleaned_data)  # چاپ تمامی اطلاعات فرم
            return redirect('home_page')
    else:
        contact_form = ContactUsForm()
    return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})
```

Files: `ContactUsage.html`

```html

<form id="main-contact-form" class="contact-form row" action="{% url 'contact_us_page' %}"
      method="post">
    {% csrf_token %}

    {% for item in contact_form %}
    <div class="col-md-12 form-group">
        {{ item.label_tag }}
        {{ item }}
        {{ item.errors }}
    </div>
    {% endfor %}
    <hr>

    {% comment %}{{ contact_form }}{% endcomment %}
    {% comment %}
    <div class="form-group col-md-6"><input type="text" name="fullname" class="form-control" placeholder="نام"></div>
    <div class="form-group col-md-6"><input type="email" name="email" class="form-control" placeholder="ایمیـل"></div>
    <div class="form-group col-md-12"><input type="text" name="subject" class="form-control" placeholder="موضـوع"></div>
    <div class="form-group col-md-12"><textarea name="message" id="message" class="form-control" rows="8" placeholder="پیغـام شمـا"></textarea></div>
    {% endcomment %}
    <div class="form-group col-md-12">
        {% comment %}<input type="submit" name="submit" class="btn btn-primary pull-right" value="ارسـال">{% endcomment %}
        <button type="submit" class="btn btn-primary pull-right">ارسال</button>
    </div>
</form>
```

### ✅️ Modelform[Database]

Files: `Forms.py`

```python
from django import forms


class ContactUsForm(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی',
                                max_length=50,
                                error_messages={'required': 'لطفانام‌و‌نام‌خانوادگی خودرا واردکنید', 'max_length': 'نام‌و‌نام‌خانوادگی نباید بیش‌از۵۰کاراکتر باشد'},
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'}))
    email = forms.EmailField(label='ایمیل ', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))
    subject = forms.CharField(label='عنوان', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان'}))
    text = forms.CharField(label='متن پیام', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن پیام', 'rows': '5', 'id': 'message'}))
```

Files: `models.py`

```python
from django.db import models


class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    message = models.TextField(verbose_name='متن تماس با ما')
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    response = models.TextField(verbose_name='متن پاسخ تماس با ما', null=True, blank=True)
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)

    class Meta:  # پارامتر صفحه ادمین جنگو
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.title
```

Files: `ContactUsage.html`

```html

<form id="main-contact-form" class="contact-form row" action="{% url 'contact_us_page' %}"
      method="post">
    {% csrf_token %}

    <div class="col-md-6 form-group">
        {{ contact_form.email.label_tag }}
        {{ contact_form.email }}
        {{ contact_form.email.errors }}
    </div>

    <div class="col-md-6 form-group {% if contact_form.full_name.errors %} text-danger  {% endif %}">
        {{ contact_form.full_name.label_tag }}
        {{ contact_form.full_name }}
        {{ contact_form.full_name.errors }}
    </div>

    <div class="col-md-12 form-group">
        {{ contact_form.subject.label_tag }}
        {{ contact_form.subject }}
        {{ contact_form.subject.errors }}
    </div>

    <div class="col-md-12 form-group">
        {{ contact_form.text.label_tag }}
        {{ contact_form.text }}
        {{ contact_form.text.errors }}
    </div>
    <div class="form-group col-md-12">
        <button type="submit" class="btn btn-primary pull-right">ارسال</button>
    </div>
</form>
```

File: `views.py`

```python
from django.shortcuts import render, redirect
from .forms import ContactUsForm, ContactUsModelForm
from .models import ContactUs


def contact_us_page(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            contact = ContactUs(
                title=contact_form.cleaned_data.get('subject'),
                full_name=contact_form.cleaned_data.get('full_name'),
                email=contact_form.cleaned_data.get('email'),
                message=contact_form.cleaned_data.get('text'),
            )

            contact.save()  # ذخیره در دیتابیس
            return redirect('home_page')
    else:
        contact_form = ContactUsForm()

    return render(request, 'contact_module/contact_us_page.html', {
        'contact_form': contact_form
    })
```

### ✅️ FunctionBaseViews

Files: `views.py`

```python
from django.shortcuts import render, redirect
from .forms import ContactUsForm, ContactUsModelForm
from .models import ContactUs
from django.urls import reverse


def contact_us_page(request):
    if request.method == 'POST':
        # contact_form = ContactUsForm(request.POST)
        contact_form = ContactUsModelForm(request.POST)  # ✅️
        if contact_form.is_valid():
            contact_form.save()  # ✅️بخاطر استفاده از مدل فُرم و تعریف فیلدها درون آن
            return redirect('home_page')
    else:
        # contact_form = ContactUsForm()
        contact_form = ContactUsModelForm()  # ✅️

    return render(request, 'contact_module/contact_us_page.html', {
        'contact_form': contact_form
    })


def product_list(request):
    products = Product.objects.all().order_by('-price')[:5]
    return render(request, 'product_module/product_list.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_module/product_detail.html', {'product': product})
```

File: `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cotact_us_page, name='cotact_us_page'),  # ✅️
    path('', views.product_list, name='product-list'),
    path('<slug:slug>', views.product_detail, name='product-detail'),
]
```

Files: `Forms.py`

```python
from django import forms
from .models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی',
                                max_length=50,
                                error_messages={'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                                                'max_length': 'نام و نام خانوادگی نمی تواند بیشتر از 50 کاراکتر باشد'},
                                widget=forms.TextInput(attrs={'class': 'form-control',  # کلاس سی اس اس می‌شود تخصیص داد
                                                              'placeholder': 'نام و نام خانوادگی'}))
    email = forms.EmailField(label='ایمیل ', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))
    title = forms.CharField(label='عنوان', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان'}))
    message = forms.CharField(label='متن پیام', widget=forms.Textarea(attrs={'class': 'form-control',
                                                                             'placeholder': 'متن پیام',
                                                                             'rows': '5',
                                                                             'id': 'message'
                                                                             }))


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        # fields = '__all__'
        # exclude = ['response']
        widgets = {  # فابلیت کانفیگ روی کلیدهای تعریفی در فیلدز
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'id': 'message'})
        }
        labels = {'full_name': 'نام و نام خانوادگی شما', 'email': 'ایمیل شما'}
        error_messages = {'full_name': {'required': 'نام و نام خانوادگی اجباری می باشد. لطفا وارد کنید'}}
```

Files: `models.py`

```python
from django.db import models


class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    message = models.TextField(verbose_name='متن تماس با ما')
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    response = models.TextField(verbose_name='متن پاسخ تماس با ما', null=True, blank=True)
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)

    class Meta:  # پارامتر صفحه ادمین جنگو
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.title
```

Files: `ContactUsage.html`

```html

<form id="main-contact-form" class="contact-form row" action="{% url 'contact_us_page' %}"
      method="post">
    {% csrf_token %}

    <div class="col-md-6 form-group">
        {{ contact_form.email.label_tag }}
        {{ contact_form.email }}
        {{ contact_form.email.errors }}
    </div>

    <div class="col-md-6 form-group {% if contact_form.full_name.errors %} text-danger  {% endif %}">
        {{ contact_form.full_name.label_tag }}
        {{ contact_form.full_name }}
        {{ contact_form.full_name.errors }}
    </div>

    <div class="col-md-12 form-group">
        {{ contact_form.title.label_tag }}
        {{ contact_form.title }}
        {{ contact_form.title.errors }}
    </div>

    <div class="col-md-12 form-group">
        {{ contact_form.message.label_tag }}
        {{ contact_form.message }}
        {{ contact_form.message.errors }}
    </div>
    <hr>
    <div class="form-group col-md-12">
        <button type="submit" class="btn btn-primary pull-right">ارسال</button>
    </div>
</form>
```

### ✅️ CBV[ClassBaseView]

#### ❇️ BasicView(view)

* تنها یک کلاس پایه است که تمام منطق را به شما واگذار می‌کند. شما باید خودتان متدهای HTTP (get, post, و غیره) را پیاده‌سازی کنید.
* استفاده از View خالی زمانی مناسب است که نیاز به انعطاف‌پذیری کامل دارید،
* اگر نیاز دارید که منطق کاملاً سفارشی برای پاسخ‌دهی به درخواست‌ها پیاده‌سازی کنید.
* عدم نیاز به ویوهای پیش‌ساخته (مثل ListView، DetailView، CreateView و غیره) بذلیل اینکه به اندازه کافی قابل انعطاف نیستند.
* اگر بخواهید خودتان بصورت مستقیم مدیریت متد‌های HTTP مانند GET، POST، PUT، DELETE و غیره را برعهده بگیرید.
* اگر می‌خواهید تمپلیت‌ها، کانتکست‌ها، فرم‌ها و سایر اجزا را به طور کامل شخصی‌سازی کنید.


* **مواقع عدم استفاده از view خالی**
    1. تکرار کد:  باید تمام منطق مربوط به مدل‌ها، فرم‌ها، تمپلیت‌ها و دیگر اجزا را خودتان بنویسید
    2. خطاهای احتمالی:  به دلیل نبود منطق پیش‌فرض، احتمال بروز خطاهای منطقی یا امنیتی بیشتر است
    3. در بیشتر مواقع استفاده از ویوهای پیش‌ساخته Django (مثل ListView, DetailView, CreateView و غیره) سریع‌تر و کاراتر است
    4. سایر ClassBaseViewsها (مثل ListView, DetailView, و غیره) منطق پیش‌فرضی دارند که گاهی برای سناریوهای رایج مورد استفاده قرار می‌گیرند

##### Ⓜ️ ViewsClass

Files: `views.py`

```python
from django.shortcuts import render, redirect
from .forms import ContactUsForm, ContactUsModelForm
from .models import ContactUs
from django.urls import reverse


class ContactUsView(View):
    def get(self, request):
        contact_form = ContactUsModelForm()
        return render(request, 'contact_module/contact_us_page.html', {
            'form': contact_form
        })

    def post(self, request):
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('home_page')

        return render(request, 'contact_module/contact_us_page.html', {'form': contact_form})


class HomeView(View):
    def get(self, request):
        context = {
            'data': 'this is data'
        }
        return render(request, 'home_module/index_page.html', context)
```

##### Ⓜ️ Files

File: `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Cotact_us_page , name='cotact_us_page'),
    path('', views.HomeView.as_view(), name='home_page'),
    path('', views.ContactUsView.as_view(), name='cotact_us_page'),  # ✅️
]
```

Files: `Forms.py`

```python
from django import forms
from .models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی',
                                max_length=50,
                                error_messages={'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                                                'max_length': 'نام و نام خانوادگی نمی تواند بیشتر از 50 کاراکتر باشد'},
                                widget=forms.TextInput(attrs={'class': 'form-control',  # کلاس سی اس اس می‌شود تخصیص داد
                                                              'placeholder': 'نام و نام خانوادگی'}))
    email = forms.EmailField(label='ایمیل ', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))
    title = forms.CharField(label='عنوان', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان'}))
    message = forms.CharField(label='متن پیام', widget=forms.Textarea(attrs={'class': 'form-control',
                                                                             'placeholder': 'متن پیام',
                                                                             'rows': '5',
                                                                             'id': 'message'
                                                                             }))


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        # fields = '__all__'
        # exclude = ['response']
        widgets = {  # فابلیت کانفیگ روی کلیدهای تعریفی در فیلدز
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'id': 'message'})
        }
        labels = {'full_name': 'نام و نام خانوادگی شما', 'email': 'ایمیل شما'}
        error_messages = {'full_name': {'required': 'نام و نام خانوادگی اجباری می باشد. لطفا وارد کنید'}}
```

Files: `ContactUsage.html`

```html

<form id="main-contact-form" class="contact-form row" action="{% url 'contact_us_page' %}"
      method="post">
    {% csrf_token %}

    <div class="col-md-6 form-group">
        {{ form.email.label_tag }}# حتما باید کلمه کلیدی فرم باشد✅️
        {{ form.email }}# ✅️
        {{ form.email.errors }}# ✅️
    </div>

    <div class="col-md-6 form-group {% if contact_form.full_name.errors %} text-danger  {% endif %}">
        {{ form.full_name.label_tag }}# ✅️
        {{ form.full_name }}# ✅️
        {{ form.full_name.errors }}# ✅️
    </div>

    <div class="col-md-12 form-group">
        {{ form.title.label_tag }}# ✅️
        {{ form.title }}# ✅️
        {{ form.title.errors }}# ✅️
    </div>

    <div class="col-md-12 form-group">
        {{ form.message.label_tag }}# ✅️
        {{ form.message }}# ✅️
        {{ form.message.errors }}# ✅️
    </div>
    <hr>
    <div class="form-group col-md-12">
        <button type="submit" class="btn btn-primary pull-right">ارسال</button>
    </div>
</form>
```

Files: `models.py`

```python
from django.db import models


class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    message = models.TextField(verbose_name='متن تماس با ما')
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    response = models.TextField(verbose_name='متن پاسخ تماس با ما', null=True, blank=True)
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)

    class Meta:  # پارامتر صفحه ادمین جنگو
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.title

```

#### ❇️ TemlateBaseView(TemplateView)

* وقتی می‌خواهید صفحات ساده یا ثابت را نمایش دهید و نیازی به منطق پیچیده ندارید از TemplateView استفاده کنید
* به طور پیش‌فرض فقط برای درخواست‌های GET طراحی شده است.
* اگر نیاز به مدیریت درخواست‌های POST دارید، باید از کلاس View یا سایر CBVs استفاده کنید
* اگر نیاز دارید داده‌های اضافی به تمپلیت ارسال کنید، می‌توانید تابع get_context_data را override کنید.
* اما اگر نیاز به کار با مدل‌ها دارید، بهتر است از ویوهایی مانند ListView یا DetailView استفاده کنید


* **شرایط استفاده**
    * نمایش صفحات ساده(StaticPages)که نیاز به عملیات پیچیده مانند کوئری در دیتابیس و مدیریت فرم‌ها ندارد
    * ارسال داده ساده به تمپلیت
    * صفحاتی مانند HomePage یا AboutUs یا ContactUs و موارد مشابه
    * نیاز به مدیریت درخواست‌های POST و اعتبارسنجی فرم‌ها یا انجام عملیات روی دیتابیس ندارید


* **عدم استفاده**
    * اگر با دیتابیس ارتباط می‌گیرید از TemplateView استفاده نکنید
    * اگر می‌خواهید فرم را نمایش بدهید یا اعتبارسنجی نمایید از TemplateView استفاده ننمایید
    * اگر می‌خواهید عملیات ساده انجام دهید از TemplateView استفاده ننمایید

##### Ⓜ️ TemplateBaseView without context

Files: `views.py`

```python
from django.views.generic.base import TemplateView  # ✅️ 


# 6. class HomeView(View): # 📌️ Without TemplateView
# 7. def get(self, request):
# 8. return render(request, 'home_module/index_page.html')


class HomeView(TemplateView):  # ✅️ 
    template_name = 'home_module/index_page.html'

```

##### Ⓜ️ TemplateBaseView with Context

Files: `views.py`

```python
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'this is data in home page'
        context['message'] = 'this is message in home page'
        return context  # قابل دسترسی در فایل اچ تی ام ال


class ProductListView(TemplateView):
    template_name = 'product_module/product_list.html'

    def get_context_data(self, **kwargs):
        products = Product.objects.all().order_by('-price')[:5]
        context = super(ProductListView, self).get_context_data()
        context['products'] = products
        return context


class ProductDetailView(TemplateView):
    template_name = 'product_module/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        slug = kwargs['slug']
        product = get_object_or_404(Product, slug=slug)
        context['product'] = product
        return context
```

##### Ⓜ️ Files

File: `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('', views.ProductListView.as_view(), name='product-list'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
]
```

Files: `Forms.py`

```python
from django import forms
from .models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی',
                                max_length=50,
                                error_messages={'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                                                'max_length': 'نام و نام خانوادگی نمی تواند بیشتر از 50 کاراکتر باشد'},
                                widget=forms.TextInput(attrs={'class': 'form-control',  # کلاس سی اس اس می‌شود تخصیص داد
                                                              'placeholder': 'نام و نام خانوادگی'}))
    email = forms.EmailField(label='ایمیل ', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))
    title = forms.CharField(label='عنوان', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان'}))
    message = forms.CharField(label='متن پیام', widget=forms.Textarea(attrs={'class': 'form-control',
                                                                             'placeholder': 'متن پیام',
                                                                             'rows': '5',
                                                                             'id': 'message'
                                                                             }))


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        # fields = '__all__'
        # exclude = ['response']
        widgets = {  # فابلیت کانفیگ روی کلیدهای تعریفی در فیلدز
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'id': 'message'})
        }
        labels = {'full_name': 'نام و نام خانوادگی شما', 'email': 'ایمیل شما'}
        error_messages = {'full_name': {'required': 'نام و نام خانوادگی اجباری می باشد. لطفا وارد کنید'}}
```

Files: `ContactUsage.html`

```html

<form id="main-contact-form" class="contact-form row" action="{% url 'contact_us_page' %}"
      method="post">
    {% csrf_token %}

    <div class="col-md-6 form-group">
        {{ contact_form.email.label_tag }}
        {{ contact_form.email }}
        {{ contact_form.email.errors }}
    </div>

    <div class="col-md-6 form-group {% if contact_form.full_name.errors %} text-danger  {% endif %}">
        {{ contact_form.full_name.label_tag }}
        {{ contact_form.full_name }}
        {{ contact_form.full_name.errors }}
    </div>

    <div class="col-md-12 form-group">
        {{ contact_form.title.label_tag }}
        {{ contact_form.title }}
        {{ contact_form.title.errors }}
    </div>

    <div class="col-md-12 form-group">
        {{ contact_form.message.label_tag }}
        {{ contact_form.message }}
        {{ contact_form.message.errors }}
    </div>
    <hr>
    <div class="form-group col-md-12">
        <button type="submit" class="btn btn-primary pull-right">ارسال</button>
    </div>
</form>
```

Files: `models.py`

```python
from django.db import models


class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    message = models.TextField(verbose_name='متن تماس با ما')
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    response = models.TextField(verbose_name='متن پاسخ تماس با ما', null=True, blank=True)
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)

    class Meta:  # پارامتر صفحه ادمین جنگو
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.title
```

#### ❇️ PredefinedGenericViews(ListView_Detailview_More)

* یکی از روش‌های ساختارمند و قابل توسعه در Class-Based Viewsها روش ارث‌بری از ویوکلاس‌های پایه چنگو است که هرکدام وظیفه خاصی دارند
* سبب سهولت در کد نویسی و کوتاه شدن کد می‌شود
* اگرنیاز به سفارشی‌سازی منطق خاصی باشد امکان Override کردن متدها وجود دارد تا نیازمندی محقق گردد
* سبب کاهش خطای احتمالی خواهد شد
* وقتی استفاده کنید که می‌خواهید عملکردهای رایج مانند نمایش لیست اشیاء، جزئیات یک شیء، ایجاد یا ویرایش شیء، و حذف شیء را به سرعت و با کمترین کد پیاده‌سازی کنید.
* جلوگیری از کد تکراری برای منطق‌های مشابه

**عدم استفاده دز زمان‌های زیر**

* نیاز به منطق پیچیده برای پیاده‌سازی
* مدیریت درخواست‌های غیر معمول متدهایHTTP (مثل PUT, PATCH, DELETE)
* مدیریت مستقیم APT ها(یا سرویس‌های) خارجی
* می‌خواهید صفحاتی مانند "درباره ما" یا "تماس با ما" بسازید که هیچ ارتباطی با دیتابیس ندارند (در این مواقع از TemplateView استفاده کنید)

نکته:

* این ویوها داده‌های پیش‌فرضی (مثل اشیاء مدل یا فرم‌ها) به تمپلیت ارسال می‌کنند.
* اگر می‌خواهید داده‌های اضافی به کانتکست اضافه کنید، باید از get_context_data استفاده کنید.

**معرفی برخی از زیر موارد**

* هنگام نمایش لیست اشیاء مدل خود از ListView استفاده نمایید.مثل لیست محصولات یک فروشگاه آنلاین
* هنگام نمایش جزییات و اطلاعات دقیق یک شیء خاص از DetailView استفاده نمایید. مثل نمایش جزییات یک محصول یا یک پست وبلاگ
* هنگام نمایش یک فرم برای ایجاد یک شیء جدید و ذخیره در دیتابیس از CreateView استفاده نمایید.مثل صفحه‌ای برای ایجاد یک پست جدید در وبلاگ
* هنگام نمایش یک فرم برای ویرایش یک شیء موجود و اعمال تغییرات در دیتابیس از UpdateView استفاده نمایید.مثل صفحه ویرایش اطلاعات یک محصول
* هنگام حذف شیء موجود(پس از دریافت تایید) و سپس حذف از دیتابیس از DeleteView استفاده کنید.مثل حذف یک پست یا محصول
* هنگام نیاز به اعمال عملیات ساده مانند فیلتر کردن و مرتب‌سازی یا جستجوی اشیاء در دیتابیس

##### Ⓜ️ ListView

Files: `views.py`

 ```python
from django.views.generic import ListView  # ✅️


class ProductListView(ListView):  # ✅️
    template_name = 'product_module/product_list.html'
    model = Product  # تعیین این که از کدام جدول دیتا باید استخراج کند و به صفحه اچ تی ام ال بفرستد 
    # همیشه با نام object_list در صفحات اچ تی ام ال شناخته می‌شود 
    context_object_name = 'products'  # change name «object_list» to «products» for use in html files

    # اگر بخش زیر نباشد همه رکوردها نمایش خواهد شد و فیلتر اعمال نمیگردد
    def get_queryset(self):  # ایجاد قابلیت فیلتر برای لیست مد نظر
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(is_active=True)  # فیلتر در اینجا لحاظ می‌گردد
        return data
```

File: `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
]
```

##### 8.1. Ⓜ️ DetailView

File: `views.py`

```python
from django.views.generic import DetailView


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product  # تعیین این که از کدام جدول دیتا باید استخراج کند و به صفحه اچ تی ام ال بفرستد 
```

File: `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
]
```

File: `models.py`

```python
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ManyToManyField(
        ProductCategory,
        related_name='product_categories',
        verbose_name='دسته بندی ها')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند', null=True, blank=True)
    price = models.IntegerField(verbose_name='قیمت')
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
```

##### 8.2. Ⓜ️ FormView

Files: `views.py`

```python
from .forms import ContactUsForm, ContactUsModelForm
from django.views.generic.edit import FormView


class ContactUsView(FormView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contac-us'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
```

##### 8.3. Ⓜ️ CreateView

Files: `views.py`

```python
from .forms import ContactUsForm, ContactUsModelForm
from django.views.generic.edit import FormView, CreateView
from .models import ContactUs


class ContactUsView(CreateView):  # ✅️
    model = contactUs
    form_class = ContactUsModelForm  # حتما باید مدل فرم باشد
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/contact-us/'
```

## 🅱️ Render

* اگر بخواهیم نوع رکوئست رو مشخص کنیم از روش زیر استفاده میکنیم تا به IntelliSence کمک کرده باشیم

```python
def FunctionName(request: HTTPRequest):
    print(request.body)
```

### ✅️ render_to_string

دریافت آدرس یک فایل «اچ‌تی‌اِم‌آِل» و تبدیل به رشته و استفاده از آن

File: `View.py`

```python
from django.template.loader import render_to_string  # ✅️


def dynamic_name(request, name):
    dic_keys = list(dic_id.keys())
    dic_values = list(dic_id.values())

    data = None
    for key, val in dic_id.items():
        if val == name:
            data = key
    if data is not None:
        return HttpResponse(f'input from url is : {name} and data is : {data}<br><br>'
                            f'<a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>')
    else:
        response_data = render_to_string('NotResponse.html')✅️
        return HttpResponse(response_data)
```

### ✅️ render

File: `View.py`

```python
from django.shortcuts import render  # ✅️


def dynamic_name(request, name):
    dic_keys = list(dic_id.keys())
    dic_values = list(dic_id.values())

    data = None
    for key, val in dic_id.items():
        if val == name:
            data = key
    if data is not None:
        return HttpResponse(f'input from url is : {name} and data is : {data}<br><br>'
                            f'<a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>')
    else:
        return render(request, 'NotResponse.html')  # ✅️
```

### ✅️ Reverse

#### ❇️ Basic(NonReverse)

نمونه زیر وضعیت بدون Reverse را نشان میدهد تا در ادامه تغییرات قابل درک باشد

فرض شود که فایل «یوآراِل» و «ویو» ساختار اصلی پروژه به صورت زیر باشد

File: (main_url) `urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainindex),
    path('users/', include('users.urls')),
]

```

File: (main_view) `view.py`

```python
from django.http import HttpResponse
from django.shortcuts import render


def mainindex(request):
    # return HttpResponse("این صفحه اصلی است")
    return render(request, 'URLs.html')
 ```

همچنین فایل «یوآراِل» و «ویو» اپلیکیش «کاربران» بصورت زیر باشد

File: (Users) `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('show', views.usershow),
    path('edit', views.useredit),
    path('<int:ids>', views.dynamic_id),  # ترتیب مهم است
    path('<str:name>', views.dynamic_name),  # ترتیب مهم است
] 
```

File: (Users) `view.py`

```python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

dic_id = {
    '0': 'بهروز',
    '1': 'Behrooz',
    '2': 'سبحان',
    '3': 'Sobhan',
    '4': 'مهدی',
    '5': 'Mahdi',
    '6': 'علی',
    '7': 'Ali'
}


def usershow(request):
    return HttpResponse('<html lang="en"><head><meta charset="UTF-8"></head><body><ul><li>صفحه نمایش کاربران و برای ورود به صفحه اصلی لینک زیر را کلیک نمایید</li><a href="http://127.0.0.1:8000"><li>127.0.0.1:8000</li></a></ul></body></html>')


def useredit(request):
    return HttpResponse('<html lang="en"><head><meta charset="UTF-8"></head><body><ul><li>صفحه ادیت کاربران </li><a href="http://127.0.0.1:8000"><li>127.0.0.1:8000</li></a></ul></body></html>')


def dynamic_id(request, ids):
    dic_values = list(dic_id.values())
    data = dic_values[ids]
    if data is not None:
        return HttpResponseRedirect(f'/users/{data}')
    return HttpResponseNotFound('ids does not exists')


def dynamic_name(request, name):
    dic_keys = list(dic_id.keys())
    dic_values = list(dic_id.values())
    data = None
    for key, val in dic_id.items():
        if val == name:
            data = key
    if data is not None:
        return HttpResponse(f'input from url is : {name} and data is : {data}')
    return HttpResponseNotFound('name does not exists')
```

#### ❇️ Reverse

اصلاح عبارت و کلمات «یوآراِل» هنگامی که صفحات زیاد داشته‌باشیم کار دشواری خواهد بود. بنابراین توصیه می‌شود برای هر مجموعه صفحاتِ «یوآراِل»، یک نام منحصربفرد اختصاص بدهیم تا بااستفاده از آن نام، بصورت خوکار تمام مسیرهای زیرین در دسترس قرار بگیرد

##### Ⓜ️ مثال اول

File: `View.py`

```python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

days = {
    'saturday': 'this is satureday in dictionary',
    'sunday': 'this is sunday in dictionary',
    'monday': 'this is monday in dictionary',
    'tuesday': 'this is tuesday in dictionary',
    'wednesday': 'this is wednesday in dictionary',
    'thursday': 'this is thursday in dictionary',
    'friday': 'this is friday in dictionary',
}


def dynamic_days(reqeust, day):
    day_data = days.get(day)
    if day_data is not None:
        context = {
            "data": day_data,
            "day": f'selected DAY is {day}'
        }
        return render(reqeust, 'challenges/challenge.html', context)
    return HttpResponseNotFound('day does not exists')


def days_list(request):
    days_list = list(days.keys())
    context = {'days': days_list}
    return render(request, "challenges/index.html", context)


def dynamic_days_by_number(request, day):
    days_names = list(days.keys())
    if day > len(days_names):
        return HttpResponseNotFound('day does not exists')
    redirect_day = days_names[day - 1]
    redirect_url = reverse('days-of-week', args=[redirect_day])✅️
    return HttpResponseRedirect(redirect_url)
```

File: `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.days_list),
    path('<int:day>', views.dynamic_days_by_number),
    path('<str:day>', views.dynamic_days, name='days-of-week'),
]
```

File: `index.html` in Templates Folder

```html
<!DOCTYPE html>
<html lang="en">
<body>
<ul>
    {% for day in days %}
    <li><a href="{% url 'days-of-week' day %}"> {{day | title}} </a></li>
    {% endfor %}
</ul>
</body>
</html>
```

##### Ⓜ️ مثال دوم

File: `url.py`

```python
urlpatterns = [
    # ...
    path('<str:name>', views.dynamic_name, name='UniqName1_behrooz'),
    # ...
]
...
```

File: (newApplication) `view.py`

```python
from django.urls import reverse


# ...
def dynamic_id(request, ids):
    dic_values = list(dic_id.values())
    data = dic_values[ids]
    if data is not None:
        redirect_url = reverse('UniqName1_behrooz', args=[data])
        return HttpResponseRedirect(redirect_url)
    return HttpResponseNotFound('ids does not exists')
# ...
```

در صورتی که قطعه کد بالا را تنظیم نماییم آنگاه در فایل زیر بجای عبارت«یوزر» در یوآراِل هرچیزی میتوانید قرار بدهید

```python
# ...
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainindex),
    path('userssssssssssssssss/', include('users.urls')),
]
# ...
```

#### ❇️ url reverse

File: `url.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('/<int:product_id>', views.device_details, name='device_details'),
]
```

File: `view.py`

```python
def device_details(request, product_id):
    device = get_object_or_404(Product, pk=product_id)
    return render(request, 'dbehrooz/device_details.html', {'device': device})
```

File: `device_details.html`

```html

<ul style="direction: rtl">
    {% for device in devices %}
    <li>
        <a href="{% url 'device_details' product_id=device.id %}">
            نام محصول: {{ device.title }} / قیمت محصول: {{ device.price }}
        </a>
    </li>
    {% endfor %}
</ul>
```

#### ❇️ Function reverse(get_absolute_url)

File: `url.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('/<int:product_id>', views.device_details, name='device_details')
]
```

File: `models.py`

```python
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    short_description = models.CharField(max_length=360, null=True)
    is_active = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('product-detail', args={'pk': self.pk})

    def __str__(self):
        return f"{self.title}: {self.price}\n"

```

File: `device_details.html`

```html

<ul style="direction: rtl">
    {% for device in devices %}
    <li>
        <a href="{{ device.get_absolute_url }}">
            نام محصول: {{ device.title }} / قیمت محصول: {{ device.price }}
        </a>
    </li>
    {% endfor %}
</ul>
```

### ✅️ DTL(Django Template Language) with CONTEXT

[built-In Templates](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/)
[URL](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#url)

به استفاده از قعطه کد پایتون در داخل صفحات «اچ‌تی‌ام‌ال» که سیتنکس آن مشابه خطوط زیر است

```html
{% PYTHON_SYNTAX_CODE %}
```

#### ❇️ basic

File: `View.py`

```
days = {
    'saturday': 'this is satureday in dictionary',
    'sunday': 'this is sunday in dictionary',
    'monday': 'this is monday in dictionary',
    'tuesday': 'this is tuesday in dictionary',
    'wednesday': 'this is wednesday in dictionary',
    'thursday': 'this is thursday in dictionary',
    'friday': 'this is friday in dictionary',
}


def days_list(request):
    days_list = list(days.keys())
    context = {'days': days_list }
    return render(request, "challenges/index.html", context)
```

File: `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<body>
<ul>
    {% for day in days %}
    <li><a href="/days/{{day}}"> {{day | title}} </a></li>
    # به این علامت «|» فیلتر گفته می‌شود
    {% endfor %}
</ul>
</body>
</html>
```

#### ❇️ Modules

```html
<!--...-->
<div class="post_content">
    <h3>{{ post.title }}</h3>
    <p>{{ post.content }}</p>
</div>
<!--...-->
```

##### Ⓜ️ url

میتوان برای رفرنس و آدرس ها از کانتکس ارسالی به صفحه استفاده کرد به نحو زیر

```html
{% load static %}
<!--...-->
<a href="{% url 'urlPost' slug=post.slug %}"></a>✅️
<img src="{% static 'yazahra/images/001.jpg' %}" alt="بهروز محمدی نسب">
<img src="{% static 'yazahra/images'|add:'/'|add:post.image %}" alt="{{ post.title }}">
<!--...-->
```

##### Ⓜ️ for

```html

<section id="latestPost">
    <h2>پست‌های‌آخر</h2>
    <ul>
        {% for post in 2latestPosts %}
        {% include 'yazahra/includes/include_post.html' %} #نکته: اینکلود معمولا در مسیر تمپلیت قرار داده می‌شود(مسیر تمپلیت به پروزه باید افزوده شود)
        {% endfor %}
    </ul>
</section>
```

##### Ⓜ️ time

```html

<time>{{ post.date|date:'d M Y' }}</time>✅️
```

##### Ⓜ️ linebreaks

تبدیل خطوط جدید (\n) در متن post.content به تگ‌های HTML مناسب برای نمایش در مرورگر

> نکته« معمولا وقتی از علامت پایت یا «|» استفاده می‌کنیم اصطلاحا کلمه فیلتر شدن معنی پیدا میکند

```html
{{ post.content| linebreaks }} #
```

### ✅️ Examples

#### ❇️ Example 1️⃣️

> منظور همان دو آکولاد باز و بسته است که در داخل کد «اچ‌تی‌ام‌ال» مشاهده می‌شود

File: `view.py`

```python
from django.shortcuts import render

days = {
    'saturday': 'this is satureday in disctionary',
    'sunday': 'this is sunday in disctionary',
    'monday': 'this is monday in disctionary',
    'tuesday': 'this is tuesday in disctionary',
    'wednesday': 'this is wednesday in disctionary',
    'thursday': 'this is thursday in disctionary',
    'friday': 'this is friday in disctionary',
}


def dynamic_days(reqeust, day):
    day_data = days.get(day)
    if day_data is not None:
        context = {"data": day_data}
        # DTL -> Django Template Language

        return render(reqeust, 'challenges/challenge.html', context)✅️  # این اسم مهم نیست مهم ارسال دیکشنری است که به صفحخه دیکشنری ارسال بشود
        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
    return HttpResponseNotFound('day does not exists')

```

#### ❇️ Example 2️⃣️

File: `*.html`

```html
...
<div class="post_content">
    <h3>{{ post.title }}</h3>
    <p>{{ post.content }}</p>
</div>
...
```

File: `view.py`

```python
from django.shortcuts import render
from datetime import date

# Create your views here.

posts_database = [
    {
        'slug': 'poos0001',
        'title': '۰۰۰۱',
        'author': 'بهروز محمدی نسب ',
        'image': '001.jpg',
        'date': date(2021, 4, 5),
        'shortDescription': 'توضیحات اختصاری از پست شماره یکم',
        'content': 'محتویات پست اول'},
    {
        'slug': 'poos0002',
        'title': '۰۰۰۲',
        'author': 'بهروز محمدی نسب ',
        'image': '009.jpg',
        'date': date(2021, 6, 3),
        'shortDescription': 'توضیحات اختصاری از پست شماره دوم',
        'content': 'محتویات پست دوم'
    },
    {
        'slug': 'poos0003',
        'title': '۰۰۰۳',
        'author': 'بهروز محمدی نسب ',
        'image': '003.jpg',
        'date': date(2021, 3, 1),
        'shortDescription': 'توضیحات اختصاری از پست شماره سوم',
        'content': 'محتویات پست سوم'
    },
    {
        'slug': 'poos0004',
        'title': '۰۰۰۴',
        'author': 'بهروز محمدی نسب ',
        'image': '010.jpg',
        'date': date(2025, 2, 27),
        'shortDescription': 'توضیحات اختصاری از پست شماره چهارم',
        'content': 'محتویات پست چهارم'
    },
]


def get_date(post):
    return post['title']


def index(request):
    sorted_posts = sorted(posts_database, key=get_date)
    two_latest_post = sorted_posts[-2:]
    return render(request, 'yazahra/index.html', {'2latestPosts': two_latest_post})


def posts(request):
    all_posts = sorted(posts_database, key=get_date)
    return render(request, 'yazahra/posts.html', {'allPosts': all_posts})


def single_post(request, slug):
    # return render(request, 'yazahra/post.html')
    post = next(post for post in posts_database if post['slug'] == slug)  # next: اولین آیتم که با شرط مطابقت دارد را برمی‌گرداند
    # پست را برای من بیاور به ازای تمام پست هایی که درون پست‌دیتابیس هست به شرط اینکه کلید اسلاگ برابر با اسلاگ باشد
    return render(request, 'yazahra/post.html', {'post': post})
```

### ✅️

## 📁️ apps.py

* جزئیات و اطلاعات هر اپلیکیشن یا ماژول

```python
from django.apps import AppConfig


class YazahraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'yazahra'
    verbose_name = 'ماژول آزماشی که بهروز دارد کار میکند'
```

## 📁️ Setting.py

* `INSTALL_APPS`
    * `INSTALL_APPS=[... , 'rest_framework' ,...]`
    * `INSTALL_APPS=[... , 'rest_framework.authtoken' ,...]`
    * `INSTALL_APPS=[... , 'drf-spectacular' ,...]` # Swagget
* `LANGUAGE_CODE = 'fa-ir'` تغییر زبان داشبورد از انگلیسی به فارسی
* `TEMPLATES`
    * `'APP_DIRS': True`  بصورت خودکار در هر اپلیکیشن اضافه‌شده دنبال پوشه تمپلیت بگرد و آن را بخوان
* `MEDIA_ROOT = BASE_DIR / 'MyDir'` مدیاهای ارسالی کاربر بصورت پیش‌فرض کجا ذخیره گردد
    * must be absolute name
* `MEDIA_URL = 'MyDir'` باز کردن یک مسیر خاص در آدرس‌های داخلی جنگو
    * بصورت پیش‌فرض همه مسیرهای جنگو بسته است مگر که مسیر خاصی را باز نمایید که باید در فایل یوآراِل نیز این گزینه را اضافه نمایید
* `SESSION_COOKIE_AGE = 120` مقدار زمان عمر سشن را روی ۲دقیقه تنظیم می‌کند
    * بصورت پیش‌فرض مقدار آن دو هفته است
* `AUTH_USER_MODEL = 'account_module.user'` تعیین نام مدل[جدول دیتابیس] که باید بابت احراز هویت مورد استفاده قرار بگیرد
    * نام مآژول و یک نقطه و نانم کلاس مدل یعنی نیاز به آوردن نام فایل نیست
* `REST_FRAMEWORK = {...}` تنظیمات «دی‌آراِف» و رست را این قسمت قرار می‌دهیم
    * `'DEFAULT_PAGINATION_CLASS'`
        * `REST_FRAMEWORK = {...,'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',...}` # use «page=۱|۲|۳|......» for pagenumber
        * `REST_FRAMEWORK = {...,'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',...}` # use «limit» for X record in one page and «offset» for begin at X record
    * `'DEFAULT_AUTHENTICATION_CLASSES'`
        * `REST_FRAMEWORK = {...,'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.BasicAuthentication'],...}` # send user and pass for all pages
        * `REST_FRAMEWORK = {...,'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],...}` # Use Token for authenticate
    * `'DEFAULT_PERMISSION_CLASSES'`
        * `REST_FRAMEWORK = {...,'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],...}` # execute code when authenticate is valid(when user logedin)
    * `'DEFAULT_SCHEMA_CLASS'` # Swagger
        * `REST_FRAMEWORK = {...,'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',...}`
* `SIMPLE_JWT = {...}` customize JWT authentication's behavior [URL](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html)
    * `'ACCESS_TOKEN_LIFETIME'` # عمر توکن اکسس
        * `"SIMPLE_JWT = {...,ACCESS_TOKEN_LIFETIME": timedelta(minutes=5)}`
    * `'REFRESH_TOKEN_LIFETIME'` عمر توکن رفرش
        * `"SIMPLE_JWT = {...,REFRESH_TOKEN_LIFETIME": timedelta(days=1)}`
    * `'AUTH_HEADER_TYPES'`
        * `"SIMPLE_JWT = {...,AUTH_HEADER_TYPES": ("Bearer",)}` # نام ارسالی همراه توکن باید چه باشد
* `SPECTACULAR_SETTINGS = {...}` # SWAGGER  [URL](https://drf-spectacular.readthedocs.io/en/latest/readme.html)
    * `SPECTACULAR_SETTINGS = {...,'TITLE': 'Your Project API',...}`
    * `SPECTACULAR_SETTINGS = {...,'DESCRIPTION': 'Your project description',...}`
    * `SPECTACULAR_SETTINGS = {...,'VERSION': '1.0.0',...}`
    * `SPECTACULAR_SETTINGS = {...,'SERVE_INCLUDE_SCHEMA': False,...}`
* `ALLOWED_HOSTS = ['*']` # Need to run `python3 manage.py runserver 0.0.0.0:8000`
    * `ALLOWED_HOSTS = ['192.168.1.100', 'example.com', '127.0.0.1']`

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

1. File: `setting.py`
    ```python
   INSTALL_APPS = [... ,'rest_framework.authtoken', ... ]
   
   REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
    'DEFAULT_PERMISSION_CLASSES':     ['rest_framework.permissions.IsAuthenticated']
   }
   ```
2. migrations Command `python3 manage.py migrate`

3. File: `/config/urls.py` # Main urls
   ```python
   from rest_framework.authtoken.views import obtain_auth_token # ✅️
   
   urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('home.urls')),
      path('todos/', include('todo.urls')),
      path('api-auth/', include('rest_framework.urls')),
      path('auth-token/', obtain_auth_token, name='generate_auth_token'),# ✅️
   ```
4. ابتدا به یک آدرس دلخواه نظیر «auth-token» با مقادیر username و password در body بعنوان RawData ارسال می‌کنیم.[نکته:در پارامتر و در هدر ارسال نکنید]
   ```json
   "POST":"http://127.0.0.1:8000/auth-token",
   {
      "username":"USERNAME",
      "password":"PASS"
   }
   ```
5. سپس یک token برای کاربر ساخته می‌شود و در دیتابیس برای همان کاربر با نگهداری زمان ایجاد token ذخیره می‌شود و بعنوان response برمیگرداند تا کدنویس آن را نگهداری و استفاده نماید
   ```json
   {
       "token": "<Token>", 
   }
   ```

* از آن پس هرگاه بخواهیم دیتا در آدرس‌های دیگر ارسال کنیم باید در header درخواست‌هایمان مقدار زیر را نیز وارد نمایید

```http request
Authentication: Token <TOKEN>
```

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

* IF Changing must to execute `python3 manage.py migrate` command

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