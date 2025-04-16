اگر تعداد آیتم‌ها زیاد باشد آنگاه برای نمایش تعداد زیاد نیاز به صفحه بندی داریم

File: `product_module/views.py`

```python
class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product  # تعیین این که از کدام جدول دیتا باید استخراج کند و به صفحه اچ تی ام ال بفرستد 
    context_object_name = 'products'  # change name «object_list» to «products» for use in html files
    ordering = ['-price']  # مرتب‌سازی بر پایه یک پارامتر برحسب نزولی یا سعودی 
    paginate_by = 6  # تعداد چند پارامتر در یک صفحه نمایش داده شود
```

File: `/product_module/templates/product_module/product_list.html`

```html
...
<div class="col-sm-9 padding-right">
    <div class="features_items"><!--features_items-->
        <h2 class="title text-center">محصولات عمده</h2>
        {% for product in products %}
        {% include 'includes/product_item_partial.html' with product=product %}
        {% endfor %}
        <div class="clearfix"></div>
        <ul class="pagination">
            {% if page_obj.has_previous %}# ✅️
            <li><a href="?page={{ page_obj.previous_page_number }}">قبلی</a></li>
            {% endif %}
            {% for pageNumber in paginator.page_range %}# ✅️
            <li class="{% if page_obj.number == pageNumber %} active {% endif %}">
                <a href="?page={{ pageNumber }}">{{ pageNumber }}</a># ✅️
            </li>
            {% endfor %}
            {% if page_obj.has_next %}# ✅️
            <li><a href="?page={{ page_obj.next_page_number }}">بعدی</a></li># ✅️
            {% endif %}

        </ul>
    </div><!--features_items-->
</div>
...
```