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