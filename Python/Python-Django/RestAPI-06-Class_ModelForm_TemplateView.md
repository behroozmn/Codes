## 1.TemplateView

### 1.1.FunctionBaseView

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

### 1.2.ClassBaseView[TemplateView]

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

### 1.3.ClassBaseView[TemplateView] with Context

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

### 2.1.functionBaseView

> Files: `views.py`
> ```python
> def product_list(request):
>    products = Product.objects.all().order_by('-price')[:5]
>    return render(request, 'product_module/product_list.html', {
>        'products': products,
>    })
>
>
> def product_detail(request, slug):
>    product = get_object_or_404(Product, slug=slug)
>    return render(request, 'product_module/product_detail.html', {
>        'product': product
>    })
>```
> File: `urls.py`
>```python
>from django.urls import path
>from . import views
>
>urlpatterns = [
>    path('', views.product_list, name='product-list'),
>    path('<slug:slug>', views.product_detail, name='product-detail'),
>]
>```

### 2.2.ClassBaseView[TemplateView]

> Files: `views.py`
> ```python
> from django.views.generic.base import TemplateView
> class ProductListView(TemplateView):# ✅️
>    template_name = 'product_module/product_list.html'
>    def get_context_data(self,**kwargs):
>        products = Product.objects.all().order_by('-price')[:5]
>        context = super(ProductListView,self).get_context_data()
>        context['products'] = products
>        return context
> 
> class ProductDetailView(TemplateView):
>    template_name = 'product_module/product_detail.html'
>    def get_context_data(self, **kwargs):
>        context = super(ProductDetailView, self).get_context_data()
>        slug = kwargs['slug']
>        product = get_object_or_404(Product, slug=slug)
>        context['product'] = product
>        return context
>```
> File: `urls.py`
>```python
>from django.urls import path
>from . import views
>
>urlpatterns = [
>    path('', views.ProductListView.as_view(), name='product-list'),
>    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
>]
>```

### 2.3.ClassBaseView[ListView]

> Files: `views.py`
> ```python
> from django.views.generic.base import TemplateView
> from django.views.generic import ListView # ✅️
> 
> class ProductListView(ListView):# ✅️
>    template_name = 'product_module/product_list.html'
>    model = Product
>    # همیشه با نام object_list در صفحات اچ تی ام ال شناخته می‌شود 
>    context_object_name = 'products' # change name «object_list» to «products» for use in html files
>    def get_queryset(self): # ایجاد قابلیت فیلتر برای لیست مد نظر
>        base_query = super(ProductListView, self).get_queryset()
>        data = base_query.filter(is_active=True) # فیلتر در اینجا لحاظ می‌گردد
>        return data
> 
> class ProductDetailView(TemplateView):
>    template_name = 'product_module/product_detail.html'
>    def get_context_data(self, **kwargs):
>        context = super(ProductDetailView, self).get_context_data()
>        slug = kwargs['slug']
>        product = get_object_or_404(Product, slug=slug)
>        context['product'] = product
>        return context
>```
> File: `urls.py`
>```python
>from django.urls import path
>from . import views
>
>urlpatterns = [
>    path('', views.ProductListView.as_view(), name='product-list'),
>    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
>]
>```
