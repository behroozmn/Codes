
```shell
pip freeze # check for "virtualenv" that must be installed
python3 -m venv myenv #ایجاد مجیط مجازی مستقل از سیستم اصلی 
source myenv/bin/activate #فعال‌سازی محیط مجازی مختص به پروژه‌خاص
pip install django
pip freeze # باید بسته جنگو نصب شده در لیست موجود باشد
           # This package is also installed: 1-asgire 2-sqlparse 3-tzdata 
```

<div style="direction:rtl;">
به مسیری که پوشه venv در آن موجود است رفته و در کنار پوشه venv ، پوشه پروژه را ایجاد نمایید
</div>

```shell
django-admin startproject config . # پروژه با نام کانفیگ در مسیر جاری ایجاد می‌کنیم
```

```python
pip install djangorestframework
pip install markdown
pip install django-filter
```

File: `setting.py`
```python
INSTALL_APPS=[... , 'rest_framework' ,...]
```

File: `urls.py`
```python

urlpatterns = [
    ...
    path('api/auth/', include('rest_framework.urls'))
]
```

