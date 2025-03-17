
Files: `Forms.py`
```python
from django import forms

class ContactUsForm(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی')
    email = forms.EmailField()
    subject = forms.CharField()
    text = forms.CharField() # or -> forms.CharField(widget=forms.Textarea)
```

Files: `views.py`

```python
from .Forms import ContactUsForm


def contact_us_page(request):
if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():  # اگر همه پارامترهای داخل فرم دیتای صحیح داشت و مناسب بود
        print(contact_form.cleaned_data) #چاپ تمامی اطلاعات فرم
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
    {{ contact_form }}
    <div class="form-group col-md-12">
        <button type="submit" class="btn btn-primary pull-right">ارسال</button>
    </div>
</form>
```