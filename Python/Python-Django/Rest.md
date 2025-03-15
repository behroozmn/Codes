from audioop import reversefrom flask import redirect

# FORM

* Method: تعیین نوع درخواست که از نوع گت باشد یا پست
    * GET
        * بصورت پیش‌فرض همه درخواست‌ها گت هست مگر اینکه تغییر داده شود
        * ارسال دیتا در «یوآراِل»
        * استفاده معمول در هنگام فیلتر کردن
    * POST
        * ارسال دیتا در هِدِر
        * ```python
          if request.method == 'POST'
             print(request.POST)
             return redirect(reverse('URL_NAME'))
          ```

* Action: ارسال فرم به کدام آدرس از «یوآراِل»ها
    * اگر قرار داده نشود به همان «یوآراِل» که فرم درآن ارسال شده است ارسال می‌شود(هرصفحه که باشیم)
* Name: در هِدِر پارامتر به همین نام به سمت سرور ارسال خواهد شد
* required:‌اگر بخواهیم فرم به سمت سرور ارسال بشود باید حتما پارامتر مورد نظر پر شده باشد
* placeholder: مقدار پیشفرض برای نمایش مقدار خالی چه باشد
* value: مقداری که بصورت پیشفرض ارسال شود
    * `<input type="submit" name="submit" class="" value="ارسـال">`
    * `<button type="submit" class="">ارسال</button`
* csrf_token: برای اطمینان ازاینکه مبدا ارسال کننده صحیح می‌باشد

## inputType

* type=text
* type=email
* type=submit
* type=color
* type=time
* type=date
* type=button
* type=checkbox
* type=datetime-local
* type=file
* type=hidden
* type=image
* type=month
* type=number
* type=password
* type=radio
* type=range
* type=reset
* type=search
* type=tel
* type=url
* type=week

```html

<form id="main-contact-form" class="contact-form row" name="contact-form" method="post">
    <div class="form-group col-md-6">
        <input type="text" name="name" class="form-control" required="required"
               placeholder="نام">
    </div>
    {% csrf_token %}
    <div class="form-group col-md-6">
        <input type="email" name="email" class="form-control" required="required"
               placeholder="ایمیـل">
    </div>
    <div class="form-group col-md-12">
        <input type="text" name="subject" class="form-control" required="required"
               placeholder="موضـوع">
    </div>
    <div class="form-group col-md-12">
        <textarea name="message" id="message" required="" class="form-control" rows="8" placeholder="پیغـام شمـا"></textarea>
    </div>
    <div class="form-group col-md-12">
        <button type="submit" class="">ارسال</button
    </div>
</form>
```

# 2.Error

* CSRF Token:ممنوعیت دسترسی برای هنگامی که از توکن زیر در خلال فرم استفاده نشده باشد
  * `{% csrf_token %}`