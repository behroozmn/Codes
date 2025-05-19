🧩 الگوی ساده: فرض کنید می‌خواهیم با استفاده از AJAX، لیستی از کاربرها را از سرور بگیریم و نمایش دهیم.
URL=`https://api.example.com/users `

```javascript
{
    page: 1
}
```

| تابع               | نوع          | موقعیت اجرا                        | مثال                                    |
|--------------------|--------------|------------------------------------|-----------------------------------------|
| `$.ajaxStart()`    | Global Event | وقتی اولین «ایجکس» شروع شود        | `$(document).ajaxStart(...)`            |
| `$.ajaxSend()`     | Global Event | قبل از ارسال هر «ایجکس»            | `$(document).ajaxSend(...)`             |
| `$.ajaxSuccess()`  | Global Event | وقتی «ایجکس» موفقیت‌آمیز باشد      | `$(document).ajaxSuccess(...)`          |
| `$.ajaxError()`    | Global Event | وقتی «ایجکس» با خطا مواجه شود      | `$(document).ajaxError(...)`            |
| `$.ajaxComplete()` | Global Event | وقتی «ایجکس» تمام شود              | `$(document).ajaxComplete(...)`         |
| `$.ajaxStop()`     | Global Event | وقتی آخرین «ایجکس» تمام شود        | `$(document).ajaxStop(...)`             |
| `$.get()`          | AJAX Method  | GET Request to server              | `$.get(url, data, callback)`            |
| `$.post()`         | AJAX Method  | POST Request to server             | `$.post(url, data, callback)`           |
| `.load()`          | AJAX Method  | بارگذاری «اِچ‌تی‌اِم‌اِل» در المان | `$(selector).load(url, data, callback)` |
| `$.getScript()`    | AJAX Method  | بارگذاری و اجرای JS                | `$.getScript(url, callback)`            |
| `jQuery.param()`   | Utility      | convert Object to QueryString      | `jQuery.param(obj)`                     |

---

# .ajaxStart(func(){})

* زمانی اجرا می‌شود که اولین درخواست AJAX آغاز شود
* هنگامی که ماژول ajax شروع می‌شود این تابع فراخوانی می‌شود
* فرآیندهای زیادی ممکن است به اجرا درآیند اما این تابع تنها در بدو استارت اولین فرآیند فراخوانی می‌شود
* گاهی در جی‌کوئری در این تابع توسط پلاگین BlockUI صفحه را قفل می‌کنیم تا اطلاعات صفحه لود شود و هنگامی که دستورات تعریفی و کارها تمام شد آن را توسط تابع ajaxStop از قفل در می‌آورد

```javascript
$(document).ajaxStart(function () {
    $('#loading').show(); // نمایش پیام "در حال بارگذاری..."
});
```

# .ajaxStop(func(){})

* زمانی اجرا می‌شود که آخرین درخواست AJAX تمام شود
* پس از اینکه همه فرایند‌های ajax تمام می‌شود این تابع فراخوانی می‌شود
* اگر در ajax تعداد ۱۰ فرایند موجود باشد آنگاه پس از اتمام همه موارد یک بار این تابع فراخوانی می‌گردد

```javascript
$(document).ajaxStop(function () {
    console.log('تمام درخواست‌ها انجام شدند.');
});
```

# .ajaxSend(func(event, request, settings){})

* هنگامی که URL درخواست AJAX ارسال می‌شود این تابع فراخوانی می‌گردد
* زمانی اجرا می‌شود که هر درخواست AJAX شروع به ارسال شود

```javascript
$(document).ajaxSend(function (event, request, settings) {
    console.log('درخواست فرستاده شد:', settings.url);
});
```

# .ajaxSuccess(func(event, request, settings){})

* هنگامی که عملیات ajax و کارهای ارسال و دریافت دیتا از URL با موفقیت انجام می‌شود
* مثلا هنگامی که url درخواست غلط باشد این تابع اجرا نمی‌شود

```javascript
$(document).ajaxSuccess(function (event, request, settings) {
    console.log('درخواست موفقیت‌آمیز بود:', settings.url);
});
```

# .ajaxComplete(func(event, request, settings){})

* زمانی که دستور ajax تمام شده باشد
* زمانی اجرا می‌شود که هر درخواست AJAX به پایان برسد  (چه موفق، چه ناموفق)
* اگر در ajax تعداد ۱۰ فرایند موجود باشد آنگاه به ازای هر فرآیند این تابع فرخوانی می‌گردد(تعداد۱۰بار فراخوانی می‌گردد)

```javascript
$(document).ajaxComplete(function (event, request, settings) {
    $('#loading').hide(); // پنهان کردن پیام "در حال بارگذاری..."
});
```

# .ajaxError(func(event, request, settings){})

* زمانی اجرا می‌شود که درخواست AJAX با خطا مواجه شود

```javascript
$(document).ajaxError(function (event, request, settings) {
    alert('خطایی رخ داده است!');
});
```

# .get(url, data, callback)

* درخواست GET به سرور برای گرفتن داده
* ایجاد یک فرایند مستقل برای اقدامات ajax که نیازمند رجوع به URL می‌باشد

```javascript
$.get("https://api.example.com/users ", {page: 1}, function (data) { // مثال برحسب  الگوی تعریف شده در ابتدای داکیومنت
    $('#result').html(JSON.stringify(data));
});
```

# .post(url, data, callback)

* درخواست POST به سرور برای ارسال داده

```javascript
$.post("https://api.example.com/submit ", {name: "Ali"}, function (response) { // مثال برحسب  الگوی تعریف شده در ابتدای داکیومنت
    console.log("پاسخ:", response);
});
```

# .getScript(url, callback)

* یک فایل جاوااسکریپت از سرور بارگذاری کن و اجرا کن
* یک فایل جاوااسکریپت را از سرور کوئری می‌زند و دریافت می‌کند و اجرا می‌کند
* یک مسیر در سمت سرور به تابع می‌دهیم و این مسیر در سرور موجود(یک فایل جاوا اسکریپت) است و آن را دریافت می‌کند و در سمت کلاینت اجرا میکند

```javascript
$.getScript("https://example.com/myscript.js ", function () {
    alert("اسکریپت بارگذاری شد!");
});
```

# jQuery.param(object)

* تبدیل یک شیء به رشته Query String در «ایجکس»
* پارامترهای URL که در شکل زیر هستند را تنها برمی‌گرداند
    * name=Behrooz&family=MohamadiNasab // http://localhost/api/Data?name=Behrooz&family=MohamadiNasab

```javascript
$("#Btn").click(function (e) {
    var object = {name: "Behrooz", family: "MohamadiNasab"};
    var param = jQuery.param(object);
    alert(param);

    $.get("/Home/GetUserByName" + "?" + param, function (res) {
        $.each(res, function (index, value) {
            $("#UsersList").append("<li>" + value.Name + " " + value.Family + "</li>");
        });
    });
});
```

```javascript
var params = jQuery.param({name: "Ali", age: 25});
// خروجی: name=Ali&age=25
```

# .load(url, data, callback)

* داده HTML از سرور بگیر و در یک المان DOM قرار بده

```javascript
$('#content').load("https://api.example.com/users-list.html ");
```