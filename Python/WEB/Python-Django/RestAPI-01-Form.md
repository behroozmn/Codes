# BasicForm

## 1.1Intro

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

## 1.1.Sample

## 1.1.1.Htmlfile.html

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

## 1.2.Error

* CSRF Token:ممنوعیت دسترسی برای هنگامی که از توکن زیر در خلال فرم استفاده نشده باشد
    * `{% csrf_token %}`

# 2.ClassForm

جنگو قابلیت مدیرت پارامترهای فرم را در قالب کلاس مهیا نموده است تا تمامی موارد را توسط کلاس پارامتردهی نمود

## 2.1.form.py

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

## 2.2.view.py

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

## 2.3.HtmlFile.html

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

# 3.Modelform[Database]

## 3.1.Forms.py

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

## 3.2.models.py

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

## 3.3.HtmlFile.html

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

## 3.4.views.py

Files: `views.py`

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
