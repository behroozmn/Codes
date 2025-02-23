در «یوآر اِل» می‌توان دیتای از نوع اسلاگ که در نمونه زیر می‌بینید

File: `urls.py`
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='starting-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.single_post, name='post-detail-page')  # toplearn.com/posts/second-post
]
]

```

File: `base.html`
```
<!DOCTYPE html>
<html lang="en">
    <body>
        <a href="{% url 'post-detail-page' slug='learning-django' %}">
    </body>
</html>
```

File: `view.py`
```
def single_post(request, slug):
    return render(request, 'base.html')
```