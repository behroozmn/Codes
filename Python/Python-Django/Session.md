> برای ذخیره اطلاعات ازنوع آبجکت از سشن استفاده نکنید\
> برای ذخیره اطلاعات سبک نظیر آی دی یا رشته متنی یا بولین یامشابه استفاده شود

* Suyntax Create
    * `request.session["Key"] = Value`

* Suyntax Read[1]
    * `Value=request.session["Key"]` #اگر پیدا نکند ارور برمیگرداند
* Suyntax Read[2]
    * `Value=request.session.get('Key')`# اگر پیدا نکند مقدار هیچی برمیگرداند و ارور نمی‌دهد  
