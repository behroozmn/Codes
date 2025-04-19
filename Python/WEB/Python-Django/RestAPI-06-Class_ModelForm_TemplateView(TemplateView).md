# 1.Intro

<div style="direction: rtl">

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

</div>

# 2.Files

## 2.1.Forms.py

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
## 2.2.HtmlFile

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

## 2.3.models.py

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

## 2.4.urls.py

File: `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
]
```



# 3.TemplateView

## 3.1.views.py

Files: `views.py`

```python
from django.views.generic.base import TemplateView  # ✅️ 


# class HomeView(View): # 📌️ Without TemplateView
#     def get(self, request):
#         return render(request, 'home_module/index_page.html')


class HomeView(TemplateView):  # ✅️ 
    template_name = 'home_module/index_page.html'

```



# 4.TemplateView with Context

## 4.1.views.py
 Files: `views.py`

```python
from django.views.generic.base import TemplateView  # ✅️ 


# class HomeView(View): # 📌️ Without TemplateView
#     def get(self, request):
#         context = {
#             'data': 'this is data'
#         }
#         return render(request, 'home_module/index_page.html', context)


class HomeView(TemplateView):  # ✅️ 
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'this is data in home page'
        context['message'] = 'this is message in home page'
        return context  # قابل دسترسی در فایل اچ تی ام ال
```