## Upload

> Files: `views.py`
> 
>  ```python
> from django.shortcuts import render, redirect
> from django.views import View
> 
> def store_file(file):
>     with open('temp/image.jpg', "wb+") as dest: # نکته: مسیر تمپ باید در مسیر اصلی پروژه باشد
>     for chunk in file.chunks():
>         dest.write(chunk)
> 
> class CreateProfileView(View): # ✅️
>     def get(self, request):
>         return render(request, 'contact_module/create_profile_page.html') 
> 
>     def post(self, request):
>         # print(request.FILES)
>         store_file(request.FILES['profile']) # این نام پروفایل در تگ فرم بعنوان نام است
>         return redirect('/contact-us/create-profile') 
>  ```
> 
> Files: `urls.py`
> ```python
> from django.urls import path
> from . import views
> 
> urlpatterns = [
>     path('create-profile/', views.CreateProfileView.as_view(), name='create_profile_page'), # ✅️
> ]
> ```
> 
> Files: `create_profile_page.html`
> ```html
> {% extends 'shared/_layout.html' %}
> {% block content %}
>     <div id="contact-page" class="container">
>         <div class="bg">
>             <div class="row">
>                 <div class="col-sm-8">
>                     <div class="contact-form">
>                         <h2 class="title text-center">ثبت پروفایل</h2>
>                         <div class="status alert alert-success" style="display: none"></div>
>                         <form id="main-contact-form" class="contact-form row" action="{% url 'create_profile_page' %}" # ✅️
>                               method="post" enctype="multipart/form-data"> # ✅️ enctype
>                             {% csrf_token %}
>                             <input type="file" name="profile"> # ✅️
>                             <div class="form-group col-md-12">
>                                 <button type="submit" class="btn btn-primary pull-right">ارسال</button>  # ✅️
>                             </div>
>                         </form>
>                     </div>
>                 </div>
>             </div>
>         </div>
>     </div>
> {% endblock %}
> ```

## Upload[Class base]
[save name in Database] and [save in custome dir]

> Files: `forms.py`
>  ```python
>  class ProfileForm(forms.Form):
>     user_image = forms.FileField()
>  ```
> Files: `models.py`
>  ```python
> class UserProfile(models.Model):
>     image = models.FileField(upload_to='images') # درفایل تنظیمات تصریح شده است که این فولدر «ایمیچ» باید در داخل کدام مسیر ایجاد شود و سبب نگهداری فایل‌ها گردد
>  ```
> Files: `views.py`
>  ```python
> from django.shortcuts import render, redirect
> from django.views import View
> from .forms import ContactUsModelForm, ProfileForm
> from django.views.generic.edit import FormView, CreateView
> from .models import ContactUs, UserProfile # ✅️
> 
> def store_file(file):
>     with open('temp/image.jpg', "wb+") as dest: # نکته: مسیر تمپ باید در مسیر اصلی پروژه باشد
>     for chunk in file.chunks():
>         dest.write(chunk)
> 
> class CreateProfileView(View):
>     def get(self, request):
>         form = ProfileForm()
>         return render(request, 'contact_module/create_profile_page.html', {
>             'form': form
>         })
> 
>     def post(self, request):
>         submitted_form = ProfileForm(request.POST, request.FILES)
> 
>         if submitted_form.is_valid():
>             profile = UserProfile(image=request.FILES["user_image"])
>             profile.save()
>             return redirect('/contact-us/create-profile')
> 
>         return render(request, 'contact_module/create_profile_page.html', {
>             'form': submitted_form
>         })
>  ```
> 
> Files: `urls.py`
> ```python
> from django.urls import path
> from . import views
> 
> urlpatterns = [
>     path('create-profile/', views.CreateProfileView.as_view(), name='create_profile_page')
> ]
> ```
> 
> Files: `create_profile_page.html`
> ```html
> {% extends 'shared/_layout.html' %}
> {% block content %}
>     <div id="contact-page" class="container">
>         <div class="bg">
>             <div class="row">
>                 <div class="col-sm-8">
>                     <div class="contact-form">
>                         <h2 class="title text-center">ثبت پروفایل</h2>
>                         <div class="status alert alert-success" style="display: none"></div>
>                         <form id="main-contact-form" class="contact-form row" action="{% url 'create_profile_page' %}" 
>                               method="post" enctype="multipart/form-data"> 
>                             {% csrf_token %}
>                             {{ form }} # ✅️
>                             <div class="form-group col-md-12">
>                                 <button type="submit" class="btn btn-primary pull-right">ارسال</button>
>                             </div>
>                         </form>
>                     </div>
>                 </div>
>             </div>
>         </div>
>     </div>
> {% endblock %}
> ```
> 
* `setting.py`
    *  `MEDIA_ROOT = BASE_DIR / 'uploads'` مدیاهای ارسالی کاربر بصورت پیش‌فرض کجا ذخیره گردد
* بدلیل تغییرات در دیتابیس باید دستورات تغییرات در دیتابیس زده شود
    