<div style="direction:rtl;">

## توضیحات

- محیط مجازی (Virtual Environment): امکان ایجاد فضا مستقل و جداگانه پروژه‌ها از هم(جلوگیری از تداخل) در وابستگی‌های نصب بسته‌ها و کتابخانه‌ها را فراهم می‌آورد
- هر پروژه می‌تواند نسخه‌های خاص خود از کتابخانه‌ها را داشته باشد بدون اینکه بر روی پروژه‌های دیگر تأثیر بگذارد.
- نکته: در محیط venv نیاز به زدن دستور ```python3 -m pip install requests``` نیست و تنها نوشتن ```pip install``` کار میکند
- حتما باید بسته virtualenv در سیستم نصب باشد تا بتوانین مجیط مجازی virtualEnvironment بوجود بیاورید(یعنی در خروجی دستور `pip freeze` این بسته موجود باشد)

</div>

## Linux and python Command

- ```apt install python3.11-venv``` #معمولا در پایتون نسخه۳ نصب می‌شود
- ```python3 -m venv myenv``` #ایجاد محیط مجازی با نام دلخواه
    - پس از زدن ستور بالا یک فولدر در مسیر کنونی ایجاد می‌شود که حاوی زیرفولدرهایی برای نگهداری ساختار بسته‌های نصبی خواهد بود
    - Alternative(windows): ```python3 -m vitrualenv venv```
- ```source myenv/bin/activate``` #فعال‌سازی محیط مجازی مختص به پروژه‌خاص
    - Alternatives(windows): ```.\MyVenv\Scripts\activate```
- ```pip install package_name``` #نصب بسته در بستر پروژه‌خاص
- deactivate #غیر فعال سازی و خروج از محیط مجازی