## 0.without TemplateView

> Files: `views.py`
>
>```python
>def HomeView(request)
>    return render(request, 'home_module/index_page.html')
>```
>
>File: `urls.py`
>
>```python
>from django.urls import path
>from . import views
>
>urlpatterns = [
>    path('', views.HomeView, name='home_page'),
>]
>```

## 1.TemplateView

### 1.2.TemplateView

> Files: `views.py`
>
>```python
>from django.views.generic.base import TemplateView  # ✅️ 
>
>
># class HomeView(View): # 📌️ Without TemplateView
>#     def get(self, request):
>#         return render(request, 'home_module/index_page.html')
>
>
>class HomeView(TemplateView):  # ✅️ 
>    template_name = 'home_module/index_page.html'
>
>```
>
>File: `urls.py`
>
>```python
>from django.urls import path
>from . import views
>
>urlpatterns = [
>    path('', views.HomeView.as_view(), name='home_page'),
>]
>```

### 1.3.TemplateView with Context data

> Files: `views.py`
>
>```python
>from django.views.generic.base import TemplateView  # ✅️ 
>
>
># class HomeView(View): # 📌️ Without TemplateView
>#     def get(self, request):
>#         context = {
>#             'data': 'this is data'
>#         }
>#         return render(request, 'home_module/index_page.html', context)
>
>
>class HomeView(TemplateView):  # ✅️ 
>    template_name = 'home_module/index_page.html'
>
>    def get_context_data(self, **kwargs):
>        context = super().get_context_data(**kwargs)
>        context['data'] = 'this is data in home page'
>        context['message'] = 'this is message in home page'
>        return context  # قابل دسترسی در فایل اچ تی ام ال
>```
> File: `urls.py`
>```python
>from django.urls import path
>from . import views
>urlpatterns = [
>    path('', views.HomeView.as_view(), name='home_page'),
>]
>```

## 2.ListView
