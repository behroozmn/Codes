Files: `Forms.py`

```python
from django import forms


class ContactUsForm(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی',
                                max_length=50,
                                error_messages={'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                                                'max_length': 'نام و نام خانوادگی نمی تواند بیشتر از 50 کاراکتر باشد'},
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'نام و نام خانوادگی'}))
    email = forms.EmailField(label='ایمیل ', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))
    subject = forms.CharField(label='عنوان', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان'}))
    text = forms.CharField(label='متن پیام', widget=forms.Textarea(attrs={'class': 'form-control',
                                                                          'placeholder': 'متن پیام',
                                                                          'rows': '5',
                                                                          'id': 'message'
                                                                          }))
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
