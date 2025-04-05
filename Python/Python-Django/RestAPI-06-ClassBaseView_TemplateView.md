Files: `views.py`

```python
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic.base import TemplateView # ✅️ 


# class HomeView(View): # 📌️ Without TemplateView
#     def get(self, request):
#         context = {
#             'data': 'this is data'
#         }
#         return render(request, 'home_module/index_page.html', context)


class HomeView(TemplateView):  # ✅️ 
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'this is data in home page'
        context['message'] = 'this is message in home page'
        return context # قابل دسترسی در فایل اچ تی ام ال


```