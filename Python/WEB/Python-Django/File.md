# 1.Upload

## 1.1.Legacy

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

## 1.2.Upload [By Class]]

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
>
> * `setting.py`
    >
* `MEDIA_ROOT = BASE_DIR / 'uploads'` مدیاهای ارسالی کاربر بصورت پیش‌فرض کجا ذخیره گردد
> * بدلیل تغییرات در دیتابیس باید دستورات تغییرات در دیتابیس زده شود

## 1.3.Filter[Upload Only Image]

> install pillow: `python -m pip install pillow`
>
> Files: `forms.py`
>  ```python
>  class ProfileForm(forms.Form):
>     user_image = forms.ImageField()
>  ```
> Files: `models.py`
>  ```python
> class UserProfile(models.Model):
>     image = models.ImageField(upload_to='images') # درفایل تنظیمات تصریح شده است که این فولدر «ایمیچ» باید در داخل کدام مسیر ایجاد شود و سبب نگهداری فایل‌ها گردد
>  ```

## 1.4.Upload [By CreateView]

> Files: `views.py`
>  ```python
> from django.views.generic.edit import CreateView
> from .models import UserProfile
> 
> class CreateProfileView(CreateView):
>     template_name = 'contact_module/create_profile_page.html'
>     model = UserProfile
>     fields = '__all__'
>     success_url = '/contact-us/create-profile'
>  ```
>
> Files: `models.py`
>  ```python
> class UserProfile(models.Model):
>     image = models.FileField(upload_to='images') # درفایل تنظیمات تصریح شده است که این فولدر «ایمیچ» باید در داخل کدام مسیر ایجاد شود و سبب نگهداری فایل‌ها گردد
>  ```
> Files: `forms.py`
>  ```python
>  class ProfileForm(forms.Form):     # ❌ به این نیازی نخواهد بود
>     user_image = forms.ImageField() # ❌ به این نیازی نخواهد بود
>  ```

# 2.Show

> Files: `views.py`
>  ```python
> from django.shortcuts import render, redirect
> from django.views import View
> from .forms import ContactUsModelForm, ProfileForm
> from django.views.generic.edit import FormView, CreateView
> from .models import ContactUs
> 
>   class ProfilesView(ListView):# ✅️
>       model = UserProfile
>       template_name = 'contact_module/profiles_list_page.html'
>       context_object_name = 'profiles' # change name «object_list» to «products» for use in html files
>  ```
> Files: `profiles_list_page.html`
> ```html
> 
> {% extends 'shared/_layout.html' %}
> {% block title %}
>     لیست پروفایل ها
> {% endblock %}
> {% block content %}
>     <div class="container">
>         <div class="row">
>             <div class="col-md-12">
>                 <ul>
>                     {% for profile in profiles %}
>                         <li>
>                             <img src="{{ profile.image.url }}" alt="" width="150"> # ✅️
>                         </li>
>                     {% endfor %}
>                 </ul>
>             </div>
>         </div>
>     </div>
> {% endblock %}
> ```
>
>
> Files: `urls.py`
> ```python
> from django.urls import path
> from . import views
> 
> urlpatterns = [
>     path('', views.ContactUsView.as_view(), name='contact_us_page'),
>     path('create-profile/', views.CreateProfileView.as_view(), name='create_profile_page'),
>     path('profiles/', views.ProfilesView.as_view(), name='profiles_page'),
> ]
> ```
>
> Files: `settings.py`
> > MEDIA_URL = '/medias/'
>
> Files: `main_urls.py`
> ```python
> from django.contrib import admin
> from django.urls import path, include
> from django.conf.urls.static import static
> from django.conf import settings
> urlpatterns = [
>     path('', include('home_module.urls')),
>     path('contact-us/', include('contact_module.urls')),
>     path('products/', include('product_module.urls')),
>     path('admin/', admin.site.urls),
> ]
> urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
> ```
