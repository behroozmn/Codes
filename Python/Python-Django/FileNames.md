* `manage.py`
    * فایل اصلی پروژه که برای بالا آمدن پروزه این فایل را استارت می‌کنیم

* `__init__.py`
    * بدون این فایل، پایتون نمی‌تواند دایرکتوری را به‌عنوان یک بسته شناسایی کند(قابلیت استفاده از ماژول‌های داخل آن دایرکتوری وجود نخواهد داشت)
    *
        * هرگاه یک بسته (یا ماژول) وارد شود، کد داخل این فایل اجرا می‌شود
    * اجرای کدهای خاصی را برای راه‌اندازی یا پیکربندی بسته خود
    * به شما این امکان را می‌دهد که کدهای خاصی را هنگام وارد کردن بسته اجرا کنید
    * این فایل به‌ویژه در سازماندهی و مدیریت ماژول‌ها و زیر بسته‌ها بسیار مفید است

* `test.py`
    * انجام کارهای unitTest را مدیریت می‌کند
* `asgi.py` ,  `wsgi.py`
    * فایل‌هایی که برای «Deploy» کردن پروژه از آن استفاده می‌شود
* `models.py`
    * امور دیتابیس
    * شامل موجودیت‌ها یا انتیتی
* `admin.py`
    * نحوه کانفیگ‌کردن و نمایش آیتم‌های موجود در models در داخل ادمین جنگو
* `test.py`
    * انجام کارهای «یونیت‌تِست» را مدیریت می‌کند
* Directory: `migrations`
    * امور دیتابیس
    * تغییرات دیتابیس رو داخل خودش نگهداری میکند
* `apps.py`
    * جزییات و اطلاعات هر اپلیکیشن یا ماژول
      ```python
      from django.apps import AppConfig
      class YazahraConfig(AppConfig):
      default_auto_field = 'django.db.models.BigAutoField'
      name = 'yazahra'
      verbose_name = 'ماژول آزماشی که بهروز دارد کار میکند'
      ```
* `setting.py`
    * `LANGUAGE_CODE = 'fa-ir'` تغییر زبان داشبورد از انگلیسی به فارسی
    * `MEDIA_ROOT = BASE_DIR / 'MyDir'` مدیاهای ارسالی کاربر بصورت پیش‌فرض کجا ذخیره گردد
        * must be absolute name
    * `MEDIA_URL = 'MyDir'` باز کردن یک مسیر خاص در آدرس‌های داخلی جنگو
        * بصورت پیش‌فرض همه مسیرهای جنگو بسته است مگر که مسیر خاصی را باز نمایید که باید در فایل یوآراِل نیز این گزینه را اضافه نمایید
    * `SESSION_COOKIE_AGE = 120` مقدار زمان عمر سشن را روی ۲دقیقه تنظیم می‌کند
        * بصورت پیش‌فرض مقدار آن دو هفته است
    * `AUTH_USER_MODEL = 'account_module.user'` تعیین نام مدل[جدول دیتابیس] که باید بابت احراز هویت مورد استفاده قرار بگیرد
        * نام مآژول و یک نقطه و نانم کلاس مدل یعنی نیاز به آوردن نام فایل نیست
    *  `REST_FRAMEWORK = {...}` تنظیمات «دی‌آراِف» و رست را این قسمت قرار می‌دهیم
       * `'DEFAULT_PAGINATION_CLASS'`
         * `'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination'` # use «page=۱|۲|۳|......» for pagenumber
         * `'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination'` # use «limit» for X record in one page and «offset» for begin at X record 
       * `'DEFAULT_AUTHENTICATION_CLASSES'`
         * `'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.BasicAuthentication']` # send user and pass for all pages
       * `'DEFAULT_PERMISSION_CLASSES'`
         * `'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated']` # execute code when authenticate is valid(when user logedin)






REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
} 

