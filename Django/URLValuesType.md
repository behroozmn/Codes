در «یوآر اِل» می‌توان دیتای از نوع اینتیجر یا استرینگ ارسال کرد که در نمونه زیر می‌بینید

```
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
```python

def dynamic_id(request, ids):
    # call when  url is integer 
    redirect_url = reverse('UniqName1_behrooz')
    return HttpResponseRedirect(redirect_url)


def dynamic_name(request, name):
    pass #کدهایی که در هنگام ارسال رشته باید فراخوانی شوند
```