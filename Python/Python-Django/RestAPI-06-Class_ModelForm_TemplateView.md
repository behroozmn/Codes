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

### 1.2.ClassBaseView by [TemplateView]

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

### 1.3.ClassBaseView by [TemplateView] with Context

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

### 2.2.ClassBaseView by [TemplateView]

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

### 2.3.ClassBaseView by [ListView]

> Files: `views.py`
> ```python
> from django.views.generic.base import TemplateView
> from django.views.generic import ListView # ✅️
> 
> class ProductListView(ListView):# ✅️
>    template_name = 'product_module/product_list.html'
>    model = Product # تعیین این که از کدام جدول دیتا باید استخراج کند و به صفحه اچ تی ام ال بفرستد 
>    # همیشه با نام object_list در صفحات اچ تی ام ال شناخته می‌شود 
>    context_object_name = 'products' # change name «object_list» to «products» for use in html files
>    # اگر بخش زیر نباشد همه رکوردها نمایش خواهد شد و فیلتر اعمال نمیگردد
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

## 3.DetailView

### 3.1.ClassBaseView by [DetailView]

> File: `views.py`
>```python
> from django.views.generic.base import TemplateView
> from django.views.generic import ListView, DetailView # ✅️
> 
> class ProductListView(ListView):
>    template_name = 'product_module/product_list.html'
>    model = Product # تعیین این که از کدام جدول دیتا باید استخراج کند و به صفحه اچ تی ام ال بفرستد 
>    # همیشه با نام object_list در صفحات اچ تی ام ال شناخته می‌شود 
>    context_object_name = 'products' # change name «object_list» to «products» for use in html files
>    # اگر بخش زیر نباشد همه رکوردها نمایش خواهد شد و فیلتر اعمال نمیگردد
>    def get_queryset(self): # ایجاد قابلیت فیلتر برای لیست مد نظر
>        base_query = super(ProductListView, self).get_queryset()
>        data = base_query.filter(is_active=True) # فیلتر در اینجا لحاظ می‌گردد
>        return data
> 
> class ProductDetailView(DetailView):# ✅️
>    template_name = 'product_module/product_detail.html'
>    model = Product # تعیین این که از کدام جدول دیتا باید استخراج کند و به صفحه اچ تی ام ال بفرستد 
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
>File: `models.py`
>```python
>from django.db import models
>from django.urls import reverse
>from django.utils.text import slugify
>
>
>class Product(models.Model):
>    title = models.CharField(max_length=300, verbose_name='نام محصول')
>    category = models.ManyToManyField(
>        ProductCategory,
>        related_name='product_categories',
>        verbose_name='دسته بندی ها')
>    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند', null=True, blank=True)
>    price = models.IntegerField(verbose_name='قیمت')
>    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='توضیحات کوتاه')
>    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
>    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
>                            verbose_name='عنوان در url')
>    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
>    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')
>
>    def get_absolute_url(self):
>        return reverse('product-detail', args=[self.slug])
>
>    def save(self, *args, **kwargs):
>        # self.slug = slugify(self.title)
>        super().save(*args, **kwargs)
>
>    def __str__(self):
>        return f"{self.title} ({self.price})"
>
>    class Meta:
>        verbose_name = 'محصول'
>        verbose_name_plural = 'محصولات'
>```

## 4.FormView

### 4.1.ClassBaseView

> Files: `Forms.py`
>
>```python
>from django import forms
>from .models import ContactUs
>
>
>class ContactUsForm(forms.Form):
>    full_name = forms.CharField(label='نام و نام خانوادگی',
>                                max_length=50,
>                                error_messages={'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
>                                                'max_length': 'نام و نام خانوادگی نمی تواند بیشتر از 50 کاراکتر باشد'},
>                                widget=forms.TextInput(attrs={'class': 'form-control',  # کلاس سی اس اس می‌شود تخصیص داد
>                                                              'placeholder': 'نام و نام خانوادگی'}))
>    email = forms.EmailField(label='ایمیل ', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))
>    title = forms.CharField(label='عنوان', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان'}))
>    message = forms.CharField(label='متن پیام', widget=forms.Textarea(attrs={'class': 'form-control',
>                                                                             'placeholder': 'متن پیام',
>                                                                             'rows': '5',
>                                                                             'id': 'message'
>                                                                             }))
>
>
>class ContactUsModelForm(forms.ModelForm):
>    class Meta:
>        model = ContactUs
>        fields = ['full_name', 'email', 'title', 'message']
>        # fields = '__all__'
>        # exclude = ['response']
>        widgets = {  # فابلیت کانفیگ روی کلیدهای تعریفی در فیلدز
>            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
>            'email': forms.TextInput(attrs={'class': 'form-control'}),
>            'title': forms.TextInput(attrs={'class': 'form-control'}),
>            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'id': 'message'})
>        }
>        labels = {'full_name': 'نام و نام خانوادگی شما', 'email': 'ایمیل شما'}
>        error_messages = {'full_name': {'required': 'نام و نام خانوادگی اجباری می باشد. لطفا وارد کنید'}}
>```
>Files: `ContactUsage.html`
>```html
><form id="main-contact-form" class="contact-form row" action="{% url 'contact_us_page' %}"
>      method="post">
>    {% csrf_token %}
>
>    <div class="col-md-6 form-group">
>        {{ form.email.label_tag }}#  حتما باید کلمه کلیدی فرم باشد✅️
>        {{ form.email }}# ✅️
>        {{ form.email.errors }}# ✅️
>    </div>
>
>    <div class="col-md-6 form-group {% if contact_form.full_name.errors %} text-danger  {% endif %}">
>        {{ form.full_name.label_tag }}# ✅️
>        {{ form.full_name }}# ✅️
>        {{ form.full_name.errors }}# ✅️
>    </div>
>
>    <div class="col-md-12 form-group">
>        {{ form.title.label_tag }}# ✅️
>        {{ form.title }}# ✅️
>        {{ form.title.errors }}# ✅️
>    </div>
>
>    <div class="col-md-12 form-group">
>        {{ form.message.label_tag }}# ✅️
>        {{ form.message }}# ✅️
>        {{ form.message.errors }}# ✅️
>    </div>
>    <hr>
>    <div class="form-group col-md-12">
>        <button type="submit" class="btn btn-primary pull-right">ارسال</button>
>    </div>
></form>
>```
>Files: `models.py`
>
>```python
>from django.db import models
>
>
>class ContactUs(models.Model):
>    title = models.CharField(max_length=300, verbose_name='عنوان')
>    email = models.EmailField(max_length=300, verbose_name='ایمیل')
>    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
>    message = models.TextField(verbose_name='متن تماس با ما')
>    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
>    response = models.TextField(verbose_name='متن پاسخ تماس با ما', null=True, blank=True)
>    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)
>
>    class Meta:  # پارامتر صفحه ادمین جنگو
>        verbose_name = 'تماس با ما'
>        verbose_name_plural = 'لیست تماس با ما'
>
>    def __str__(self):
>        return self.title
>```
>Files: `views.py`
>
>```python
>from django.shortcuts import render, redirect
>from .forms import ContactUsForm, ContactUsModelForm
>from django.views.generic.edit import FormView
>
>
>class ContactUsView(View):
>    def get(self, request):
>        contact_form = ContactUsModelForm()
>        return render(request, 'contact_module/contact_us_page.html', {
>            'contact_form': contact_form
>        })
>
>    def post(self, request):
>        contact_form = ContactUsModelForm(request.POST)
>        if contact_form.is_valid():
>            contact_form.save()
>            return redirect('home_page')
>
>        return render(request, 'contact_module/contact_us_page.html', {
>            'contact_form': contact_form
>        })
>```
>
>File: `urls.py`
>
>```python
>from django.urls import path
>from . import views
>
>urlpatterns = [
>    # path('', views.Cotact_us_page , name='cotact_us_page'),
>    path('', views.ContactUsView.as_view() , name='cotact_us_page'),
>]
> ```

### 4.2.ClassBaseView by [FormView]

> Files: `views.py`
>
>```python
>from django.shortcuts import render, redirect
>from .forms import ContactUsForm, ContactUsModelForm
>from django.views.generic.edit import FormView # ✅️
>
>class ContactUsView(FormView):# ✅️
>    template_name = 'contact_module/contact_us_page.html'# ✅️
>    form_class = ContactUsModelForm# ✅️
>    success_url = '/contac-us'
>
>    def form_valid(self, form):# ✅️
>        form.save()# ✅️
>        return super().form_valid(form) # ✅️
>```

## 5.CreateView

### 5.1.ClassBaseView by [CreateView]

> Files: `views.py`
>
>```python
>from django.shortcuts import render, redirect
>from .forms import ContactUsForm, ContactUsModelForm
>from django.views.generic.edit import FormView, CreateView # ✅️
>from .models import ContactUs
>
>class ContactUsView(CreateView): # ✅️
>    model = contactUs
>    form_class = ContactUsModelForm # حتما باید مدل فرم باشد
>    template_name = 'contact_module/contact_us_page.html'
>    success_url = '/contact-us/'
>```
