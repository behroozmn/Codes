## پیش‌فرض

فرض شود که فایل «یوآراِل» و «ویو» ساختار اصلی پروژه به صورت زیر باشد
> main_url: `urls.py`
>
> ```python
> from django.contrib import admin
> from django.urls import path, include
> from . import views
> urlpatterns = [
>     path('admin/', admin.site.urls),
>     path('', views.mainindex),
>     path('users/', include('users.urls')),
> ]
> 
> ```
> main_view: view.py
>
> ```python
> from django.http import HttpResponse
> from django.shortcuts import render
> def mainindex(request):
>    # return HttpResponse("این صفحه اصلی است")
>    return render(request, 'URLs.html')
>  ```
همچنین فایل «یوآراِل» و «ویو» اپلیکیش «کاربران» بصورت زیر باشد
> --- 
> Users: `urls.py`
> ```python
> from django.urls import path
> from . import views
> urlpatterns = [
>     path('show', views.usershow),
>     path('edit', views.useredit),
>     path('<int:ids>', views.dynamic_id),  # ترتیب مهم است
>     path('<str:name>', views.dynamic_name),  # ترتیب مهم است
> ] 
> ```
> Users:`view.py`
>
> ```python
> from django.shortcuts import render
> from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
> dic_id = {
>     '0': 'بهروز',
>     '1': 'Behrooz',
>     '2': 'سبحان',
>     '3': 'Sobhan',
>     '4': 'مهدی',
>     '5': 'Mahdi',
>     '6': 'علی',
>     '7': 'Ali'
> }
> def usershow(request):
>     return HttpResponse('<html lang="en"><head><meta charset="UTF-8"></head><body><ul><li>صفحه نمایش کاربران و برای ورود به صفحه اصلی لینک زیر را کلیک نمایید</li><a href="http://127.0.0.1:8000"><li>127.0.0.1:8000</li></a></ul></body></html>')
> def useredit(request):
>     return HttpResponse('<html lang="en"><head><meta charset="UTF-8"></head><body><ul><li>صفحه ادیت کاربران </li><a href="http://127.0.0.1:8000"><li>127.0.0.1:8000</li></a></ul></body></html>')
> def dynamic_id(request, ids):
>     dic_values = list(dic_id.values())
>     data = dic_values[ids]
>     if data is not None:
>         return HttpResponseRedirect(f'/users/{data}')
>     return HttpResponseNotFound('ids does not exists')
> def dynamic_name(request, name):
>     dic_keys = list(dic_id.keys())
>     dic_values = list(dic_id.values())
>     data = None
>     for key, val in dic_id.items():
>         if val == name:
>             data = key
>     if data is not None:
>         return HttpResponse(f'input from url is : {name} and data is : {data}')
>     return HttpResponseNotFound('name does not exists')
>  ```

## Reverse

هنگامیکه صفحات زیادی داشته باشیم آنگاه اصلاح عبارت و کلمات «یوآراِل» کار دشواری خواهد بود بنابراین توصیه می‌شود که<br>
برای هر مجموعه صفحاتِ «یوآراِل»، یک نام منحصربفرد اختصاص بدهیم تا بااستفاده از آن نام، بصورت خوکار تمام مسیرهای زیرین در دسترس قرار بگیرد<br>
برای این کار فایل `«یوآراِل»` اپلیکیش بصورت زیر تغییر میکند<br>

```python
...
urlpatterns = [
    ...
    path('<str:name>', views.dynamic_name, name='UniqName1_behrooz'),
    ...
]
...
```

همچننی فایل «ویو» اپلیکیشن به صورت زیر تغییر می‌کند

```python
...
from django.urls import reverse

...


def dynamic_id(request, ids):
    dic_values = list(dic_id.values())
    data = dic_values[ids]
    if data is not None:
        redirect_url = reverse('UniqName1_behrooz', args=[data])
        return HttpResponseRedirect(redirect_url)
    return HttpResponseNotFound('ids does not exists')


...

```

در صورتی که قطعه کد بالا را تنظیم نماییم آنگاه در فایل زیر بجای عبارت«یوزر» در یوآراِل هرچیزی میتوانید قرار بدهید

```python
...
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainindex),
    path('userssssssssssssssss/', include('users.urls')),
]
...
```
