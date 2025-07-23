<div dir="rtl">

# 🅰️ مفاهیم و نکات

* علامت دالر شروع شونده نشانه‌گر «جِی‌کوئری» است
* JQuery snippets
    * jqclick --> $(selector).click(function (e) {e.preventDefault();});
    *

# 🅰️ AJAX

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

## 🅱️ .ajaxStart(func(){})

* زمانی اجرا می‌شود که اولین درخواست AJAX آغاز شود
* هنگامی که ماژول ajax شروع می‌شود این تابع فراخوانی می‌شود
* فرآیندهای زیادی ممکن است به اجرا درآیند اما این تابع تنها در بدو استارت اولین فرآیند فراخوانی می‌شود
* گاهی در جی‌کوئری در این تابع توسط پلاگین BlockUI صفحه را قفل می‌کنیم تا اطلاعات صفحه لود شود و هنگامی که دستورات تعریفی و کارها تمام شد آن را توسط تابع ajaxStop از قفل در می‌آورد

```javascript
$(document).ajaxStart(function () {
    $('#loading').show(); // نمایش پیام "در حال بارگذاری..."
});
```

## 🅱️ .ajaxStop(func(){})

* زمانی اجرا می‌شود که آخرین درخواست AJAX تمام شود
* پس از اینکه همه فرایند‌های ajax تمام می‌شود این تابع فراخوانی می‌شود
* اگر در ajax تعداد ۱۰ فرایند موجود باشد آنگاه پس از اتمام همه موارد یک بار این تابع فراخوانی می‌گردد

```javascript
$(document).ajaxStop(function () {
    console.log('تمام درخواست‌ها انجام شدند.');
});
```

## 🅱️ .ajaxSend(func(event, request, settings){})

* هنگامی که URL درخواست AJAX ارسال می‌شود این تابع فراخوانی می‌گردد
* زمانی اجرا می‌شود که هر درخواست AJAX شروع به ارسال شود

```javascript
$(document).ajaxSend(function (event, request, settings) {
    console.log('درخواست فرستاده شد:', settings.url);
});
```

## 🅱️ .ajaxSuccess(func(event, request, settings){})

* هنگامی که عملیات ajax و کارهای ارسال و دریافت دیتا از URL با موفقیت انجام می‌شود
* مثلا هنگامی که url درخواست غلط باشد این تابع اجرا نمی‌شود

```javascript
$(document).ajaxSuccess(function (event, request, settings) {
    console.log('درخواست موفقیت‌آمیز بود:', settings.url);
});
```

## 🅱️ .ajaxComplete(func(event, request, settings){})

* زمانی که دستور ajax تمام شده باشد
* زمانی اجرا می‌شود که هر درخواست AJAX به پایان برسد  (چه موفق، چه ناموفق)
* اگر در ajax تعداد ۱۰ فرایند موجود باشد آنگاه به ازای هر فرآیند این تابع فرخوانی می‌گردد(تعداد۱۰بار فراخوانی می‌گردد)

```javascript
$(document).ajaxComplete(function (event, request, settings) {
    $('#loading').hide(); // پنهان کردن پیام "در حال بارگذاری..."
});
```

## 🅱️ .ajaxError(func(event, request, settings){})

* زمانی اجرا می‌شود که درخواست AJAX با خطا مواجه شود

```javascript
$(document).ajaxError(function (event, request, settings) {
    alert('خطایی رخ داده است!');
});
```

## 🅱️ .get(url, data, callback)

* درخواست GET به سرور برای گرفتن داده
* ایجاد یک فرایند مستقل برای اقدامات ajax که نیازمند رجوع به URL می‌باشد

```javascript
$.get("https://api.example.com/users ", {page: 1}, function (data) { // مثال برحسب  الگوی تعریف شده در ابتدای داکیومنت
    $('#result').html(JSON.stringify(data));
});
```

## 🅱️ .post(url, data, callback)

* درخواست POST به سرور برای ارسال داده

```javascript
$.post("https://api.example.com/submit ", {name: "Ali"}, function (response) { // مثال برحسب  الگوی تعریف شده در ابتدای داکیومنت
    console.log("پاسخ:", response);
});
```

## 🅱️ .getScript(url, callback)

* یک فایل جاوااسکریپت از سرور بارگذاری کن و اجرا کن
* یک فایل جاوااسکریپت را از سرور کوئری می‌زند و دریافت می‌کند و اجرا می‌کند
* یک مسیر در سمت سرور به تابع می‌دهیم و این مسیر در سرور موجود(یک فایل جاوا اسکریپت) است و آن را دریافت می‌کند و در سمت کلاینت اجرا میکند

```javascript
$.getScript("https://example.com/myscript.js ", function () {
    alert("اسکریپت بارگذاری شد!");
});
```

## 🅱️ jQuery.param(object)

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

## 🅱️ .load(url, data, callback)

* داده HTML از سرور بگیر و در یک المان DOM قرار بده

```javascript
$('#content').load("https://api.example.com/users-list.html ");
```

# 🅰️ Events

* Syntax:
    ```
    $(selector).event(function (){});
    ```

## 🅱️ MouseEvents

### ✅️ MouseSingleClick

  ```javascript
  $("#Button_1").click(function () {
    $("#ID").fadeOut();
});
  ```

### ✅️ MouseDoubleClick

  ```javascript
  $("#Button_2").dblclick(function () {
    $("#ID").fadeOut();
});
  ```

### ✅️ MouseEnter

* وقتی وارد محدوده مختصاتی شیء بشویم رخ می‌دهد و تفاوتی در شیء فرزند نمی‌کند
* وقتی وارد می‌شویم تنها ایونت رخ میدهد و فرزند ها تفاوتی نمیکند

  ```javascript
  $("#Button_5").mouseenter(function () {
      $("#enterAndLeave").fadeOut();
  });
  ```

### ✅️ MouseOver[Also Childs]

* اگر وارد فرزند (در داخل همان شیء) بشویم به منزله‌این است که گویی به شیء ورود کرده‌ایم
* وقتی وارد فرزند های می‌شویم هم بازم ایونت رخ میدهد

  ```javascript
  var over=0;
  $("#OverEvent").mouseover(function () { 
    over++;
    $("#OverEvent span").text(over);
  });
  ```

### ✅️ MouseDown

* کلیک روی شیء و نگهداشتن آن

  ```javascript
  $("#Button_4").mousedown(function () {
      $("#mouseUpAndDown").fadeOut();
  });
  ```

### ✅️ MouseUp

* کلید روی شیء و نگهداشتن و رها کردن کلیک از آن شیء

  ```javascript
  $("#Button_4").mouseup(function () {
      $("#mouseUpAndDown").fadeIn();
  });
  ``

### ✅️ MouseLeave

* فقط باید از محدوده مختصاتی شیء خارج شویم
* اگر در داخل شیء وارد فرزند شویم یعنی همچنان داخل شیء هستیم

  ```javascript
  $("#Button_5").mouseleave(function () {
      $("#enterAndLeave").fadeIn();
  });
  ```

### ✅️ MouseOut[Also Childs]

* اگر وارد فرزند بشویم به منزله‌این است که گویی از محدوده شیء خارج شده‌ایم

  ```javascript
  var out = 0;
  $("#OutEvent").mouseout(function () {
    out++;
    $("#OutEvent span").text(out);
  });
  ```

### ✅️ MouseMove

* جرکت درداخل شیء

  ```javascript
  $("#Button_6").mousemove(function (e) {
    var pageX = e.pageX;
    var pageY = e.pageY;
    var total = "(" + pageX + "," + pageY + ")";
    $("#move span").text(total); // نمایش در داخل اسپنی که داخل شیء دارای آی دی است
  });
  ```

### ✅️ Hover

* Only for Jquery
* conbine [mouseenter] and [mouseleave] from javascript
* ورود موس به داخل

  ```javascript
  $("#Button_3").hover(function () {
      $("#ID").fadeOut();
  }, function () {
      $("#ID").fadeIn();
  });
  ```

## 🅱️ KeboardEvents

### ✅️ keydown

* وقتی دکمه فشرده می‌شود، قبل از بالا آوردن کلید این رویداد رخ میدهد

```javascript
$("#firstInput").keydown(function (e) {
    var text = $("#firstInput").val(); // مقدار درونی input را برمیگرداند
    $("#secondInput").val(text);
});
```

### ✅️ keyup

* وقتی کلید فشرده شده است و دقیقا هنگامی که دکمه را رهاسازی میکنیم این رویداد رخ می‌دهد

```javascript
$("#firstInput").keyup(function (e) {
    var text = $("#firstInput").val(); // مقدار درونی input را برمیگرداند
    $("#secondInput").val(text);
});
```

### ✅️ keypress

* همانند «کی‌داون» است با این تفاوت که دکمه های غیر کاراکتری عمل نخواهد کرد
* غیر فعال در دکمه هایی که تاثیر کاراکتری ندارد

```javascript
$("#firstInput").keydown(function (e) {
    var text = $("#firstInput").val(); // مقدار درونی input را برمیگرداند
    $("#secondInput").val(text);
    console.log(e.type);
});
```

## 🅱️ FormEvents

### ✅️ PreReqirement Codes

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Keyboard Events</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="asset/css/bootstrap.min.css"/>
    <link rel="stylesheet" type="text/css" media="screen" href="asset/css/bootstrap-rtl.min.css"/>
    <script src="asset/js/jquery-3.3.1.min.js"></script>
    <script src="asset/js/Custom.js"></script>
</head>

<body>
<br>
<div class="container">
    <div class="row">
        <div class="col-md-4 col-md-offset-4">
            <form action="javascript:alert('sent');" id="form">
                <div class="panel panel-success">
                    <div class="panel-heading">
                        <h4>form events</h4>
                    </div>
                    <div class="panel-body" id="parent">
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="متن تستی" id="firstInput">
                        </div>
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="نتیجه" id="secondInput">
                        </div>
                        <div class="form-group">
                            <select id="change" class="form-control">
                                <option>mohammad</option>
                                <option>iman</option>
                                <option>elanz</option>
                                <option>soheil</option>
                            </select>
                        </div>
                        <div class="col-md-12">
                            <p class="text-danger" id="paragraph"></p>
                        </div>
                        <button type="submit" class="btn btn-success btn-block">send</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>
</body>

</html>
```

### ✅️ blur

* وقتی داخل یک شیء قرار میگیرد و از آن خارج می‌شوید
* مثلا یک تکس‌باکس که ورود میکنیم در آن و سپس از آن خارج می‌شویم
* فقط برای یک المان معنی پیدا میکند و کاری با المان‌های دیگر ندارد

```javascript
$("#firstInput").blur(function (e) {
    var text = e.type;
    $("#secondInput").val(text);
});
```

### ✅️ focusout[Parental Elemet]

* same as blur
* اگر روی والد درنظر بگیریم آنگاه اگر از روی هر فرزند خارج شویم رخداد اجرا می‌شود

```javascript
$("#parent").focusout(function (e) {
    var text = e.type;
    $("#secondInput").val(text);
});
```

### ✅️ focus

* هنگامی که وارد المان می‌شویم
* فقط برای یک المان معنی پیدا میکند و کاری با المان‌های دیگر ندارد

```javascript
$("#firstInput").focus(function (e) {
    var text = e.type;
    $("#secondInput").val(text);
});
```

### ✅️ focusin[Parental Elemet]

* same as focus
* اگر روی والد درنظر بگیریم آنگاه اگر از در هر فرزند وارد شویم رخداد اجرا می‌شود

```javascript
$("#parent").focusin(function (e) {
    var text = e.type;
    $("#secondInput").val(text);
});
```

### ✅️ change

* change the element value

```javascript
$("#change").change(function (e) {
    var selected = $("#change :selected").text();
    var text = e.type;
    $("#secondInput").val(selected);
});
```

### ✅️ select

* وقتی مقداری از متن داخل یک باکس را انتحاب می‌کنیم و به رنگ آبی درمی‌آید و قابلیت کپی و غیره پیدا میکنند

```javascript
$("#firstInput").select(function (e) {
    var text = e.type;
    $("#secondInput").val(text);
});
```

### ✅️ submit

* وقتی فرم سابمیت می‌شود
* می‌توان برای سابمیت شدن شرایط بگذارید که تحت شرایط خاص فقط سابمیت صورت گیرد

```javascript
$("#form").submit(function (e) {
    var text = $("#firstInput").val();
    if (text === 'Behrooz Mohammadinasab') {
        return;
    } else {
        e.preventDefault(); // فرم سابمیت نشود
    }
});
```

## 🅱️ window

### ✅️ resize

```javascript
$(window).resize(function () {
    $("#firstInput").val($(window).width());
});
```

### ✅️ scrol

```javascript
var scrollTimes = 0;
$(window).scroll(function () {
    $("#scrollevent").val(scrollTimes += 1);
});
$(window).scroll(function () {
    if ($(window).scrollTop() > 150) {
        $("#navbar").addClass("myNavbar");
    } else {
        $("#navbar").removeClass("myNavbar");
    }
});
```

### ✅️ ready

* وقتی یک کامپوننت بصورت کامل لود شود این رویداد رخ می‌دهد

```javascript
$("#myImage").ready(function () {
    ShowAlert();
});
```

### ✅️ holdReady

* HoldReady(True # مانع لود شدن کامل صفحه بشو
* HoldReady(False) # اجازه بده صفحه بصورت کامل لود بشود

```javascript
$.holdReady(true);
$.getScript("asset/js/test.js", function () { // یک اسکریپت رو لود کن 
    $.holdReady(false); // وقتی لود تمام شد اجازه بده صفحه کاملا لود بشه
});
$(document).ready(function () {
    ShowAlert();
});

```

## 🅱️ EventHandlerAttachment

### ✅️ on

* چند تا رویداد رو به یک سلکتور متصل یا الصاق یا الحاق می‌کنیم
* در مثال زیر به جای نوشتن دو رویداد اول مستقیما رویداد سوم را می‌نویسیم

```javascript
// $("#onAttachment").click(function (e) { 
//    alert('same event');
// });

// $("#onAttachment").mouseleave(function () { 
//     alert('same event mouseleave');
// });

$("#onAttachment").on("click dblclick", function () {
    alert('bind with on');
});
```

* اگر بخواهیم در رویدادهای متفاوت عمل متفاوت داشته باشد

```javascript
$("#onAttachment").on({
    click: function () {
        alert('bind with on for click');
    },
    mouseleave: function () {
        alert('bind with on for mouseleave');
    }
});
```

```javascript
// مثال دوم

$("#ID").on("click", "button", function (e) { // برو در مولفه «آی‌دی» در رویداد کلیک آن برروی المنت‌های دکمه آن رویداد فراخوانی شود و کارهای داخل تابع را انجام بده 
    alert(e.delegateTarget);
});
```

### ✅️ of

* غیر فعال کردن یک رویداد از یک مولفه

```javascript
$("p").click(function (e) {
    $(this).css("background-color", "red");
});

$("#ID").click(function (e) {
    $("p").off("click");
});
```

### ✅️ one

* فقط یک بار رویداد اجرا شود

```javascript
$("p").click(function (e) {
    alert('hello');
});

$("p").one("click", function (e) {
    alert('hello');
});
```

## 🅱️ Trigger

```javascript
$("#ID1").click(function (e) {
    alert('hello');
});

$("#ID2").click(function (e) {
    $("#ID1").trigger("click");
});
```

## 🅱️ TriggerHandler

* انجام کارهای ظاهری و نه همه کارهای رویداد در مولفه اصلی که قرار است آن را اجرا کند
* اگر شما مثلا کاری انجام دهید و در انتها به صفحه ای ارجاع بدید آنگاه کارهای ظاهری و صفحه را انجام میدهد ولی به صفحه دیگر نمی‌رود

## 🅱️ proxy

* مثلا رویداد وقفه توسط صفحه اجرا می‌شود و نه مولفه پس در هنگام تنظیم مولفه به مشکل می‌خوریم و عملیات انجام نمی‌شود برای همین شکل دوم آورده شده مشکل را حل میکند

```javascript
// 
$("p").click(function (e) {
    setInterval(setInterval(function () {
        $(this).addClass("bg-red") // this refer to window
    }), 600);
});

// ✅️
$("p").click(function (e) {
    setInterval($.proxy(function () {
        $(this).addClass("bg-red"); // this refer to p
    }, this), 600);
});
```

## 🅱️ currentTarget

```javascript
$("#ID").click(function (event) {
    if (event.currentTarget === this) {
        alert('true');
    }
});
```

## 🅱️ data

* ارسال دیتا به تابع برای استفاده در بدنه تابع

```javascript
$("#ID").on("click", {myValue: 'test'}, function (event) {
    alert(event.data.myValue);
})
```

```javascript
for (var i = 0; i <= 4; i++) {
    $("#ID button").eq(i).on("click", {myValue: i}, function (event) {
        alert(event.data.myValue);
    });
}
```

## 🅱️ DelegateTarget

[//]: # (Todo: Need to Review)

* باتوجه به مثال دوم کارش این است که برمیگردد به خود المنت اولی که ایونت رو روی آن فراخوانی کردید

```javascript
$(".mybutton").click(function (e) {
    alert(e.delegateTarget);
});
```

```javascript
$("#myDeletegate").on("click", "button", function (e) {
    alert(e.delegateTarget);
});
```

## 🅱️ preventDefault

* تابع preventDefault باعث ممانعت در اجرای عمل پیش‌فرض یک رویداد و تگ(که باید به‌صورت عادی کار خود را انجام دهد) می‌گردد
* تابع isDefaultPrevented بررسی میکند که آیا در یک تگ و رویداد ممانعت به عمل آمده است یا خیر

```javascript
$("a").click(function (e) {
    e.preventDefault(); //ممانعت از انجام کلید لینک مورد نظر یعنی لینک نباید عمل کند

    if (e.isDefaultPrevented()) { // آیا کار عادی تگ در وضعیت غیر فعال در آمده است
        alert('true');
    }
});
```

## 🅱️ stopImmediatePropagation

* اگر از یگ رویداد چندین مورد تعریف کرده باشیم آنگاه وقتی یکی رو اجرا کرد دیگری ها رو نادیده بگیرد و دیگر بقیه انجام نشود از این به بعد رویداد پیش‌فرض این گزینه باشد(از بین چندین مورد یکسان)

```javascript
$("#ID").click(function (e) {
    alert('ID #1 clicked');
    e.stopImmediatePropagation(); // رویداد کلیک را برای بقیه غیر فعال کن و فقط این رویداد قابل اجرا باشد

    if (e.isImmediatePropagationStopped()) {
        alert('true');
    }
});

$("#ID").click(function (e) {
    alert('ID #2 clicked');
});

$("#ID").click(function (e) {
    alert('ID #3 clicked');
});
```

## 🅱️ stopPropagation

* اگر برای یک مولفه رویداد تعریف کرده باشید و برای والد آن هم تعریف کرده باشید آنگاه اگر این مورد را برای فرزند انجام دهید دیگر رویداد والد رخ نخواهد داد

```html
    <p id="IdParent">
    my name is <span style="color: red">BehroozMohammadiNasab</span>
</p>
```

```javascript
$("#IdParent span").click(function (e) {
    alert("span");
    e.stopPropagation();
});

$("#IdParent").click(function (e) {
    alert("paragraph");
});
```

## 🅱️ NodeName

* گزینش اِلِمان بر حسب رفتاری که سلکت میکنیم
* مثال زیر سه مربع دارد که هرکدام کلیک کنیم نام آن المان رو برمیگرداند

```html

<style>
    p,
    span,
    strong {
        padding: 30px;
        margin: 20px;
        border: 1px solid black;
    }
</style>
</head>
<body>
<div class="container">
    <div class="row">
        <p>
            <strong>
                    <span>
                        span
                    </span>
            </strong>
        </p>
    </div>
</div>
```

```javascript
$("body").click(function (e) {
    debugger;
    alert(e.target.nodeName);
});
```

## 🅱️ EventType

```javascript
$("#ID").click(function (e) {
    if (e.type == click) { // click , dblclick, mousemove...
        alert("Clicked")
    }
});
```

## 🅱️ TimeStamp

* تفاوت زمانی رویداد انجام شده تا اپوخ‌تایم
* برحسب میلی‌ثانیه است
* کاربرد آن مثلا در اندازه‌گیری زمان پاسخ‌دهی کاربر یا سیستم

```javascript
// مثلاً تشخیص اینکه دو کلیک چقدر با هم فاصله زمانی داشته‌اند.
let lastClickTime = 0;

$('#myButton').on('click', function (e) {
    if (e.timestamp - lastClickTime < 300) {
        console.log("Double click شناسایی شد!");
    }
    lastClickTime = e.timestamp;
});
```

## 🅱️ which

* عدد اسکی را برمیگرداند

```javascript
$("#ID_Input").on("mousedown keydown", function (e) {
    $("#ListBox").append("type : " + e.type + " - " + "which :" + e.which + "<br/>");
});
```

# 🅰️ Pages

## 🅱️ document

* کل صفحه از بالا تا پایین با تمام اسکرول‌های آن

```javascript
$(document).ready(function () { //Ready: -> وقتی صفحه کامل لود شد تابع را اجرا بنماید
    $("#ID").fadeOut(3000);    // المان را در ۳ثانیه حذف نماید
});
``` 

## 🅱️Window

* صفحه پیش رو که درصفحه مرورگر، به هرکدام از قسمت‌های اسکرول شده در ابعاد صفحه نمایش

# 🅰️ Animations

## 🅱️ Basic Animations

### ✅️ .show()

```javascript
$("#ShowButton").click(function (e) {
    // 1️⃣️
    $(selector).show();

    // 2️⃣️
    $("#ShowTest p").show("slow");

    // 3️⃣️
    $("#ShowTest p").show(1000);

    // 4️⃣️
    $("#ShowTest p").show(500, function () {
        alert("hello");
    });

    // 5️⃣️
    $("#ShowTest p").first().show(1000, function NextParagraph() { //هر پنج تگ پی را یکی یکی با فاصله یک ثانبه محو کند
        $(this).next("p").show(1000, NextParagraph);
    });
});
```

### ✅️ .hide()

```javascript

$("#HideButton").click(function (e) {
    // 1️⃣️
    $(selector).hide();

    // 2️⃣️
    $("#HideTest p").hide("slow");

    // 3️⃣️
    $("#HideTest p").hide(1000);

    // 4️⃣️
    $("#HideTest p").hide(1000, function () {
        alert("hello");
    });

    // 5️⃣️
    $("#HideTest p:last-child").hide(1000, function HideNext() {
        $(this).prev().hide(1000, HideNext);
    });
});
```

### ✅️ .toggle()

مقدار display را روی none تنظیم می‌کند یا روی وضعیت قبلی که اعم از "block" یا "inline" یا "inline-block" یا غیره باشد

```javascript
$("#ToggleButton").click(function (e) {
    // 1️⃣️
    $("#ToggleTest p").toggle("slow");

    // 2️⃣️
    $("#ToggleTest p").toggle(1000);

    // 3️⃣️
    $("#ToggleTest p").toggle(1000, function () {
        console.log('hello');
    });

    // 4️⃣️
    // اگر true: المان‌ها نمایش داده می‌شوند 
    // اگر false: المان‌ها پنهان می‌شوند 
    var status = false; // یا true بسته به اینکه بخواهید نمایش |پنهان کنید
    $("#ToggleTest p").toggle(status);
});
```

## 🅱️ Sliding Animation

### ✅️ .slideDown()

* المان(ها) را با انیمیشن "باز شدن" از بالا به پایین نمایش می‌دهد.

```javascript
$("#SlideDownButton").click(function (e) {

    // 1️⃣️️
    $("#SlideDownTest").slideDown("slow");

    // 2️⃣️
    $("#SlideDownTest").slideDown(2000);

    // 3️⃣️
    $("#SlideDownTest p").first().slideDown(1000, function NextSlide() {
        $(this).next("p").slideDown(1000, NextSlide);
    });
});
```

### ✅️ .slideUp()

* المان(ها) را با انیمیشن "فشرده شدن" از پایین به بالا پنهان می‌کند.

```javascript
$("#SlideUpButton").click(function (e) {

    // 1️⃣️️
    $("#SlideUpTest").slideUp("slow");

    // 2️⃣️
    $("#SlideUpTest").slideUp(2000);

    // 3️⃣️
    $("#SlideUpTest").slideUp(1000, function () {
        alert('Done');
    });
});
```

### ✅️ .slideToggle()

* خودکار بین slideUp و slideDown تاگل می‌کند
* وضعیت المان(ها) را با انیمیشن باز/بسته کردن عمودی معکوس می‌کند.
* هر فراخوانی، اگر المان:
    * نمایان بود → با انیمیشن بالا رفتنی پنهان می‌شود
    * پنهان بود → با انیمیشن پایین آمدنی نمایش داده می‌شود

```javascript
$("#SlideToggleButton").click(function (e) {
    $("#SlideToggleTest p").slideToggle(1500);
});
```

```javascript
$("#DelayButton").click(function (e) {
    $("#div_1").slideUp(2000).slideDown(2000);
    $("#div_2").slideUp(2000).delay(1000).slideDown(2000);
});

$("#StopButton").click(function (e) {
    $("#StopDiv").stop().slideToggle(1500);
});

```

## 🅱️ Fading Animation

### ✅️ .fadeIn();

* المان(ها) را با انیمیشن "نمایان شدن" از شفاف به کاملاً دیدنی نمایش می‌دهد.

```javascript
$("#FadeInButton").click(function (e) {

    // 1️⃣️
    $("#FadeInTest p").fadeIn();

    // 2️⃣️
    $("#FadeInTest p").fadeIn(2000);

    // 3️⃣️
    $("#FadeInTest p").fadeIn("slow");

    // 4️⃣️
    $("#FadeInTest p").fadeIn(1000, function () {
        console.log('hello');
    });

    // 5️⃣️
    $("#FadeInTest p").first().fadeIn(1000, function NextFade() {
        $(this).next("p").fadeIn(1000, NextFade);
    });
});
```

### ✅️ .fadeOut()

* المان(ها) را با انیمیشن "پنهان شدن" از دیدنی شفاف به پنهان تغییر وضعیت می‌دهد.

```javascript
 $("#FadeOutButton").click(function (e) {

    // 1️⃣️
    $("#FadeOutTest p").fadeOut();

    // 2️⃣️
    $("#FadeOutTest p").fadeOut(1000);

    // 3️⃣️
    $("#FadeOutTest p").fadeOut("fast");

    // 4️⃣️
    $("#FadeOutTest p").fadeOut(1000, function () {
        console.log('hello');
    });

    // 5️⃣️
    $("#FadeOutTest p:last-child()").fadeOut(1000, function PrevFade() {
        $(this).prev("p").fadeOut(1000, PrevFade);
    });
});
```

### ✅️ .fadeTo(duration, opacity)

* شفافیت (opacity) المان(ها) را به مقدار مشخص شده (0 تا 1) تغییر می‌دهد.
* این تابع فقط شفافیت را تغییر می‌دهد، ولی المان را نمایش یا پنهان نمی‌کند  (یعنی display تغییر نمی‌کند)

```javascript
$(".colored").click(function (e) {
    // $(selector).fadeTo(duration, opacity);

    // 1️⃣️
    $(this).fadeTo(200, 0.2);


    //2️⃣️
    $(this).fadeTo(200, 0.2, function () {
        console.log('test');
    });
});
```

### ✅️ .fadeToggle(duration)

* وضعیت المان(ها) را با انیمیشن شفاف/ناشفاف کردن معکوس می‌کند.

```javascript

$("#FadeToggleButton").click(function (e) {
    // 1️⃣️
    $("#FadeToggleTest p").fadeToggle(200);
});
```

## 🅱️ Custome Animation

### ✅️ .animate(propery,duration,easing)

Syntax:

```javascript
$(selector).animate(propery, option);
$(selector).animate(propery, duration, easing);
```

```javascript
 $(".colored").click(function (e) {
    $(this).animate({
        "height": "20px",
        "width": "20px",
        "opacity": "0.3"
    }, {
        duration: 1000,
        done: function () {
            console.log('hello');
        }
    });
});
```

```javascript
$("#StrButton").click(function (e) {
    $(".inside").animate({"bottom": "0px"}, 2000);
    $(".inside").animate({"right": "0px"}, 2000);
    $(".inside").animate({"top": "0px"}, 2000);
});
```

### ✅️ .finish()

```javascript
$("#FinButton").click(function (e) {
    $(".inside").finish();
});
```

## 🅱️ QUEUE

* هر کار انیمیشن که داریم انجام میدهیم یک صف نامیده می‌شوند
* گاهی میخواهیم چندین فعالیت و کار پشت سر هم انجام شوند تا یک تجربه انیمیشن بوقوع بپیوندد، آنگاه هر کدام یک صف است

### ✅️ .queue() | .dequeue()

* اگر بخواهیم یک صف به مجموعه صفوف انیمیشن اضافه نماییم از روش زیر استفاده می‌کنیم
* نکته: در انهای صف حتما باید از دیکیو استفاده شود تا صف بعدی به اجرا دربیاید وگرنه صف اضافه شده پس از انجام سبب توقف مجموعه صف می‌شوند
* تابع queue به شما اجازه می‌دهد تا فانکشن‌ها را به صف پیش‌فرض (یا یک صف مشخص) اضافه کنید ، تا بعداً به ترتیب اجرا شوند.
* تابع dequeue مرحله بعدی در صف را اجرا می‌کند. این تابع زمانی استفاده می‌شود که شما یک تابع را به صف اضافه کرده‌اید و می‌خواهید jQuery را وادار کنید به اجرای مرحله بعدی ادامه دهد.

```javascript
$("#StrButton").click(function (e) {
    $(".inside").animate({"bottom": "0"}, 2000); // Queue Number 1️⃣️
    $(".inside").animate({"right": "0"}, 2000);  // Queue Number 2️⃣️
    $(".inside").queue(function () {
        $(this).css({"background-color": "red"}).dequeue(); // Queue Number 3️⃣️
    });
    $(".inside").animate({"top": "0"}, 2000); // Queue Number 4️⃣️
});
```

```html

<body>
<br>
<div class="container">
    <div class="row">
        <div class="col-md-12">
            <div class="well" style="height: 350px;">
                <div class="col-md-9">
                    <div class="Test" style="position: absolute;top:0;">
                        <div class="inside"></div>
                    </div>
                </div>
                <div class="col-md-4 pull-left">
                    <a class="btn btn-success btn-block" id="StrButton">
                        Start
                    </a>
                    <a class="btn btn-success btn-block" id="ClearButton">
                        Clear Queue
                    </a>
                    <a class="btn btn-success btn-block" id="OffButton">
                        jQuery.fx.off
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>
```

```css
.colored {
    width: 100px;
    height: 100px;
    background-color: brown;
    position: relative;
    float: right;
    margin-left: 10px;
}

.Test {
    width: 300px;
    height: 300px;
    border: 2px solid red;
}

.inside {
    width: 20px;
    height: 20px;
    background-color: black;
    position: inherit;
    margin: 5px;
    left: 0px;
}
```

### ✅️ .clearQueue()

* سبب پاک نمودن اعضای صف انیمیشن می‌شود(محموعه عضوهای صف انیمیشن که از کنار هم قرار دادن آن انیمشین کامل اجرا می‌شود)
* البته عضو در داخل صف انیمیشن(بعنوان تنها عضو صف[زیرا بقیه پاک شدند])به اجرای خود ادامه می‌دهد و پس از اتمام کار آن انیمشن متوقف می‌شود

```javascript
$("#ClearButton").click(function (e) {
    $(".inside").clearQueue();
});
```

### ✅️ .stop()

انیمیشن در حین کار خود در همان حالت کنونی متوقف شود

```javascript
$("#btn").click(function (e) {
    $("#selector").stop();
});
```

```javascript
$("#selector").stop().clearQueue();
```

### ✅️ $.fx.off

* در jQuery، متغیر سراسری $.fx.off وجود دارد که کنترل می‌کند آیا انیمیشن‌ها اجرا شوند یا خیر :
    * اگر $.fx.off = true باشد: تمام انیمیشن‌ها غیرفعال می‌شوند.
    * اگر $.fx.off = false باشد: انیمیشن‌ها فعال هستند (پیش‌فرض).

* هر بار که تابع زیر فراخوانی شود، وضعیت انیمیشن‌های jQuery را فعال یا غیرفعال می‌کند.

```javascript
        var toggleFx = function () {
    $.fx.off = !$.fx.off;
};
```

* اولین بار که بدنه تابع بالا اجرا شود، $.fx.off از حالت پیش‌فرض (false) به true تغییر می‌کند و انیمیشن‌ها غیرفعال می‌شوند.
* بار بعد، $.fx.off دوباره به false تغییر می‌کند و انیمیشن‌ها فعال می‌شوند.
* این تغییر وضعیت به صورت چرخشی ادامه پیدا می‌کند.

در مثال زیر هر بار روی دکمه کلیک کنید، وضعیت انیمیشن تغییر می‌کند: اگر فعال باشد، جعبه حرکت می‌کند. اگر غیرفعال باشد، حرکت بدون انیمیشن اتفاق می‌افتد (یا اصلاً حرکت نمی‌کند، بسته به تنظیمات).

```html

<button id="toggle">Toggle Animation</button>
<div id="box" style="width:100px;height:100px;background:red;position:relative"></div>

<script>
    var toggleFx = function () {
        $.fx.off = !$.fx.off;
    };

    $('#toggle').on('click', function () {
        toggleFx(); // توگل وضعیت انیمیشن
        $('#box').animate({left: '+=100'}, 1000);
    });
</script>
```

*     اگر $.fx.off = true باشد، تمام توابعی مثل .animate(), .fadeIn(), .slideUp() و غیره بلافاصله اجرا می‌شوند بدون هیچ انیمیشنی  — یعنی فقط تغییرات CSS اعمال می‌شوند ولی "انتقال" وجود ندارد. 

# 🅰️ Functions

## 🅱️ time

### ✅️ setInterval

* اجرای یک تابع بعد از گذشت مقدار داده شده

> پیاده‌سازی ویژگی درحال تایپ

```javascript
$("#myTextbox").keypress(function (e) {
    $("#ID").text("در حال تایپ ....");
});
$("#myTextbox").keyup(function (e) {
    setInterval(function () {
        $("#ID").text("");
    }, 1000);
});
```

### ✅️ [fadeIn]|[fadeout]

* مرئی و نامرئی شدن یک مولفه از صفحه

```javascript
$("#Button_3").hover(function () {
    $("#ID").fadeOut();
}, function () {
    $("#ID").fadeIn();
});
```

```javascript
$("#Button_3").mouseenter(function () {
    $("#ID").fadeOut();
});

$("#Button_3").mouseleave(function () {
    $("#ID").fadeIn();
});
```

# 🅰️ Functions

برای اینکه یک پارامتر را برای اعمال تغییرات انتخاب کنیم

## 🅱️ ID Selector

  ```javascript
  $(document).ready(function () {
    $("#Button_1").click(function () {
        $("#IdSelector").fadeOut(3000); // توسط شارپ و نام آی دی آن تگ مربوطه
    });
});
  ``` 

### ✅️ ParentChile[>]

* با انتخاب والد به سراغ انتخاب فرزند می‌رویم و تگهای مورد نظر را انتخاب می‌کنیم
* آی دی را پیدا میکند و یک لایه زیر نگاه میکند و هرچی تگ باشد آن را مد نظر قرار میگیرد
* هر چند تعداد لایه زیرین دارای تگ باشد آن را مد نظر قرار **نخواهد** داد
* در مثال زیر تگ تست مورد انتخاب واقع نمی‌شود

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_11">
            Parent > Child Selector
        </a>
    </div>
    <div class="col-md-9" id="Parent">
        <p class="test">1</p>
        <p>2</p>
        <p class="test">3</p>
        <p>4</p>
        <p class="test">5</p>
        <div>
            <p>test</p>
        </div>
    </div>
    <div class="clearfix"></div>
</div
```

```javascript
$("#Button_11").click(function () {
    $("#Parent > p.test").fadeOut(500);
});
```

### ✅️ Descendent[space]

* با انتخاب والد به سراغ انتخاب فرزند می‌رویم و تگهای مورد نظر را انتخاب می‌کنیم
* هر چند تعداد لایه زیرین دارای تگ باشد آن را مد نظر قرار میدهد

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_13">
            Descendant Selector
        </a>
    </div>
    <div class="col-md-9" id="descendantId">
        <p>1</p>
        <p>2</p>
        <div>
            <p>test</p>
        </div>
        <p>3</p>
        <p>4</p>
        <p>5</p>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_13").click(function () {
    $("#descendantId p").fadeOut(500);
});
```

### ✅️ contain

* ملاک محتوی مقدار تگ است و نه خصیصه

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_12">
            Contains Selector
        </a>
    </div>
    <div class="col-md-9" id="ID">
        test
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_12").click(function () {
    $("#ID:contains('test')").fadeOut(500);
});
```

## 🅱️ Class Selector

  ```javascript
  $(document).ready(function () {
    $("#Button_2").click(function () {
        $(".ClassName").fadeOut(3000); // توسط نقطه و نام کلاس مربوطه
    });
});
  ```

## 🅱️ All Elements Selector

  ```javascript
  $(document).ready(function () {
    $("#Button_3").click(function () {
        $("*").fadeOut(3000);
    });
});
  ```

## 🅱️ Attribute Selector

### ✅️ Contains[Key*=Value]

* اجرای عملیات روی هر تگ که نام آن مشخص شده باشد و مقدار آن نیز شامل محتوی مشخص شده باشد
* مقدار مورد نظر باید مشمول بشود و مهم نیست کجای مقدار خصیصه باشد

```html

<div class="well" TestName="TestValue Hello">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_4">
            Attribute Contains Selector
        </a>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_4").click(function () {
    $("[TestName*='TestValue']").fadeOut(3000);
});
```

### ✅️ ContainsWord[Key~=Value]

* اجرای عملیات روی هر تگ که نام آن مشخص شده باشد و مقدار آن نیز شامل محتوی مشخص شده بعنوان یک کلمه مستقل باشد
* اگر کلمه به هم شامل عبارت به هم چسبیده باشد قبول نیست و باید با خط فاصله از هم جدا شود تا تبدیل به یک کلمه مستقل شود

```html

<div class="well" TestName="TestValue Hello">
    <div class="well" WordName="WordValue Test">
        <div class="col-md-3 pull-left">
            <a class="btn btn-warning btn-block" id="Button_5">
                Attribute Contains Word Selector
            </a>
        </div>
    </div>
</div>
</div>
```

```javascript
$("#Button_5").click(function () {
    $("[WordName~='WordValue']").fadeOut(3000);
});
```

### ✅️ EndsWith[Key$=Value]

* مقدار محتوی خصیصه به چه چیزی ختم شود

```html

<div class="well" EndWith="Hello Mohammad">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_6">
            Attribute Ends With Selector
        </a>
    </div>
```

```javascript
$("#Button_6").click(function () {
    $("[EndWith$='ad']").fadeOut(3000);
});
```

### ✅️ Equal[Key=Value]

* مقدار محتوی خصیصه دقیقا برابر چه مقداری شود

```html

<div class="well" Equal="Hello">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_7">
            Attribute Equal Selector
        </a>
    </div>
</div>
```

```javascript
$("#Button_7").click(function () {
    $("[Equal='Hello']").fadeOut(3000);
});
```

### ✅️ StartWith[Key^=Value]

* مقدار محتوی خصیصه دقیقا با چه مقداری شروع شود

```html

<div class="well" StartWith="Hello Mohammad">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_8">
            Attribute Start With Selector
        </a>
    </div>
</div>
```

```javascript
$("#Button_8").click(function () {
    $("[StartWith^='He']").fadeOut(3000);
});
```

## 🅱️ Type Selector

### ✅️ Button[":button"]

* هر تگ که نوع آن از نوع دکمه باشد

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_9">
            Button Selector
        </a>
    </div>
    <div class="col-md-9">
        <input type="button" value="input button">

        <button> button</button>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_9").click(function () {
    $(":button").fadeOut(3000);
});
```

### ✅️ checkbox[":checkbox"]

* هر تگ که نوع آن از نوع دکمه باشد

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_10">
            checkbox Selector
        </a>
    </div>
    <div class="col-md-9">
        <input type="checkbox">checkbox

    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_10").click(function () {
    $(":checkbox").fadeOut(500);
});
```

### ✅️ Disable[:disabled]

* انخاب موارد غیر فعال شده

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_14">
            disabled Selector
        </a>
    </div>
    <div class="col-md-9">
        <input type="button" disabled value="disabled">
        <input type="button" value="notdisabled">
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_14").click(function () {
    $("input:disabled").fadeOut(500);
});
```

### ✅️ enable[:enabled]

* انخاب موارد فعال

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_15">
            enabled Selector
        </a>
    </div>
    <div class="col-md-9">
        <input type="button" value="enabled">
        <input type="button" disabled value="notenabled">
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_15").click(function () {
    $("input:enabled").fadeOut(500);
});
```

### ✅️ Empty[:empty]

* انخاب موارد خالی

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_16">
            empty Selector
        </a>
    </div>
    <div class="col-md-9 alert alert-warning"></div>

    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_16").click(function () {
    $("div:empty").fadeOut(500);
});
```

### ✅️ Index Selector[:eq(X)]

* ایندکس ها از صفر شروع می‌شود
* انتخاب یک المنت بر اساس ترتیب ایندکس استفاده شدن آن

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_17">
            eq() => index Selector
        </a>
    </div>
    <div class="col-md-9" id="indexSelector">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>

    <div class="clearfix"></div>
</div>

```

```javascript
$("#Button_17").click(function () {
    $("#indexSelector p:eq(2)").fadeOut(500);
});
```

### ✅️ even Selector[:even]

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_18">
            even Selector
        </a>
    </div>
    <div class="col-md-9" id="evenSelector">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>

    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_18").click(function () {
    $("#evenSelector p:even").fadeOut(500);
});
```

### ✅️ file Selector[:file]

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_19">
            file Selector
        </a>
    </div>
    <div class="col-md-9" id="fileSelector">
        <input type="file" value="file Selector">
    </div>

    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_19").click(function () {
    $("#fileSelector :file").fadeOut(500);
});
```

### ✅️ first-child[:first-child]

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_20">
            first-child Selector
        </a>
    </div>
    <div class="col-md-9" id="childSelector">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>

    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_20").click(function () {
    $("#childSelector p:first-child").fadeOut(500);
});
```

### ✅️ first-of-type[:first-of-type]

* اولین تک معرفی شده از هر والد که میتواند مثلا دوتا دایو باشد که اولین از هرکدام از دایو را حذف نماید

```html

<div class="well" id="firstTypeSelector">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_21">
            first-of-Type Selector
        </a>
    </div>
    <div class="col-md-9">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>
    <div class="col-md-9">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>

    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_21").click(function () {
    $("#childSelector p:first-of-type").fadeOut(500);
});
```

### ✅️ first[:first]

* اولین المنت رو در نظر میگیرد
* اگر چیزی انتحاب نشود اولین المنت صفحه را در نظر میگیرد

```html

<div class="well" id="firstSelector">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_22">
            first Selector
        </a>
    </div>
    <div class="col-md-9">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>
    <div class="col-md-9">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>

    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_22").click(function () {
    $("#firstSelector p:first").fadeOut(500);
});
```

### ✅️ greaterthanSelector[::gt(X)]

* ایندکس شماره خاص به بعد همه را انتخاب کن

```html

<div class="well" id="greaterthanSelector">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_23">
            greater than Selector
        </a>
    </div>
    <div class="col-md-9">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>
    <div class="clearfix"></div>
</div>
</div>
```

```javascript
    $("#Button_23").click(function () {
    $("#greaterthanSelector p:gt(2)").fadeOut(500);
});
```

### ✅️ Has[:Has(<TAGNAME>)]

* اگر المانی وجود داشته باشد آن را اتخاب می‌کند
* بیشتر برای تگ استفاده می‌شود

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_25">
            :has() Selector
        </a>
    </div>
    <div class="col-md-9">
        <div class="MyClass">
            <p>
                Hello in a paragraph
            </p>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_25").click(function () {
    $("div.MyClass:has(p)").fadeOut(500);
});
```

### ✅️ last-child[:last-child]

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_26">
            last child Selector
        </a>
    </div>
    <div class="col-md-9" id="LastChild">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_26").click(function () {
    $("#LastChild p:last-child").fadeOut(500);
});
```

### ✅️ last-of-type[:last-of-type]

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_27">
            last of type Selector
        </a>
    </div>
    <div class="col-md-9" id="LastOfType">
        <div>
            <p>0</p>
            <p>1</p>
            <p>2</p>
            <p>3</p>
            <p>4</p>
        </div>
        <div>
            <p>0</p>
            <p>1</p>
            <p>2</p>
            <p>3</p>
            <p>4</p>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_27").click(function () {
    $("#LastOfType p:last-of-type").fadeOut(500);
});
```

### ✅️ last[:last]

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_28">
            last Selector
        </a>
    </div>
    <div class="col-md-9" id="LastSelector">
        <div>
            <p>0</p>
            <p>1</p>
            <p>2</p>
            <p>3</p>
            <p>4</p>
        </div>
        <div>
            <p>0</p>
            <p>1</p>
            <p>2</p>
            <p>3</p>
            <p>4</p>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_28").click(function () {
    $("#LastSelector p:last").fadeOut(500);
});
```

### ✅️ lessThanSelector[:lt(X)]

* انتخاب المان‌های با ایندکس کمتر از یک عدد خاص

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_29">
            :ls() => Less Than Selector
        </a>
    </div>
    <div class="col-md-9" id="LessThan">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
        <p>5</p>
        <p>6</p>
        <p>7</p>
        <p>8</p>
        <p>9</p>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_29").click(function () {
    $("#LessThan p:lt(4)").fadeOut(500);// میتوان عدد منفی نیز بپذیرد
});
```

### ✅️ not[:not]

* حاوی ویژگی نباشد

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_34">
            :not() Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="NotSelector">
            <div>
                <input type="checkbox" name="a">
                <span>ایمان</span>
            </div>
            <div>
                <input type="checkbox" name="b">
                <span>محمد</span>
            </div>
            <div>
                <input type="checkbox" name="c" checked="checked">
                <span>سهیل</span>
            </div>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_34").click(function () {
    $("input:not(:checked) , input:not(:checked) + span").fadeOut(500);
});
```

### ✅️ nth_child[:nth_child(X)]

* Not ZeroBase
* از عدد یک شروع می‌شود
* در والدهای یکسان فرزند شماره خاص را انتخاب نماید

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_35">
            :nth-child() Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="MyChild">
            <div>
                <ul>
                    <li>محمد</li>
                    <li>میلاد</li>
                    <li>علی</li>
                </ul>
            </div>
            <div>
                <ul>
                    <li>سبحان</li>
                    <li>مرتضی</li>
                </ul>
            </div>
            <div>
                <ul>
                    <li>الناز</li>
                    <li>سارا</li>
                    <li>سمیه</li>
                    <li>فائزه</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_35").click(function () {
    $("#MyChild ul li:nth-child(3n)").fadeOut(500); // nth-child(even) یا  nth-child(2)
});
```

### ✅️ nth-last-child[:nth-last-child(X)]

* Not ZeroBase
* از عدد یک شروع می‌شود
* در والدهای یکسان فرزند شماره خاص را انتخاب نماید با این تفاوت که از آخر شروع به اجرا می‌نماید و نه از ابتدا

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_36">
            :nth-last-child() Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="ID">
            <div>
                <ul>
                    <li>محمد</li>
                    <li>میلاد</li>
                    <li>علی</li>
                    <li>رضا</li>
                    <li>عباس</li>
                    <li>سمیرا</li>
                </ul>
            </div>
            <div>
                <ul>
                    <li>سبحان</li>
                    <li>مرتضی</li>
                </ul>
            </div>
            <div>
                <ul>
                    <li>الناز</li>
                    <li>سارا</li>
                    <li>سمیه</li>
                    <li>فائزه</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_36").click(function () {
    $("#ID ul li:nth-last-child(2)").fadeOut(500); // nth-last-child(even) یا  nth-last-child(2n)
});
```

### ✅️ nth_Of_Type[:nth_Of_Type(X)]

* وقتی چند والد(مثلا دیو) داریم آنگاه اگر بخواهیم از بین تگ‌های متفاوت داخل دیو، دومین پی را انتخاب کنیم که در تمام والد ها دومین فرزند انتخاب شود

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_37">
            :nth-of-type() Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="ID">
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
            <hr>
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
            <hr>
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_37").click(function () {
    $("#ID div p:nth-of-type(2)").fadeOut(500);
});
```

### ✅️ nth-last-of-type[:nth-last-of-type]

* وقتی چند والد(مثلا دیو) داریم آنگاه اگر بخواهیم از بین تگ‌های متفاوت داخل دیو، دومین پی را انتخاب کنیم که در تمام والد ها دومین فرزند انتخاب شود با این تفاوت که از آخر انتخاب و شمارش میکند ونه از اول

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_38">
            :nth-last-of-type() Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="ID">
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
            <hr>
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
            <hr>
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_38").click(function () {
    $("#ID div p:nth-last-of-type(2)").fadeOut(500);
});
```

### ✅️ only-child[:only-child]

* فقط انتخاب تک فرزند ها

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_39">
            :only-child Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="ID">
            <div>
                <ul>
                    <li>محمد</li>
                    <li>میلاد</li>
                    <li>علی</li>
                </ul>
            </div>
            <hr>
            <div>
                <ul>
                    <li>سبحان</li>
                </ul>
            </div>
            <hr>
            <div>
                <ul>
                    <li>سبحان</li>
                </ul>
            </div>
            <hr>
            <div>
                <ul>
                    <li>سبحان</li>
                    <li>مرتضی</li>
                </ul>
            </div>
            <hr>
            <div>
                <ul>
                    <li>الناز</li>
                    <li>سارا</li>
                    <li>سمیه</li>
                    <li>فائزه</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_39").click(function () {
    $("#ID li:only-child").fadeOut(500);
});
```

### ✅️ only-of-type[:only-of-type]

* در انواع مختلف هرکدام که تنهای کی از آن ها در دایره والد موجود است را انتخاب کن

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_40">
            :only-of-type Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="ID">
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <b>bold 2</b>
                <span>span</span>
            </div>
            <hr>
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
            <hr>
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_40").click(function () {
    $("#ID b:only-of-type").fadeOut(500);
});
```

### ✅️ parent[:parent]

* تگ‌هایی که حدافل یک فرزند داشته باشد یا اینکه بعنوان والد شناخته شده باشد

```html

<style>
    td {
        width: 40px;
        height: 40px;
        background: green;
    }
</style>

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_41">
            :parent Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="ID">
            <table border="1">
                <tr>
                    <td>mohammad</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Ali</td>
                    <td></td>
                </tr>
            </table>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_41").click(function () {
    $("#ID td:parent").fadeOut(500);
});
```

### ✅️ selected[:selected]

* selected text in selectBox
* در المان سلکت‌باکس گزینه ای که انتخاب می‌شود را انتخاب می‌کند

```html
...
<div class="panel panel-success">
    <div class="panel-heading">
        <h4>form events</h4>
    </div>
    <div class="panel-body" id="parent">
        <div class="form-group">
            <input type="text" class="form-control" placeholder="متن تستی" id="firstInput">
        </div>
        <div class="form-group">
            <input type="text" class="form-control" placeholder="نتیجه" id="secondInput">
        </div>
        <div class="form-group">
            <select id="ID" class="form-control">
                <option>mohammad</option>
                <option>iman</option>
                <option>elanz</option>
                <option>soheil</option>
            </select>
        </div>
        <div class="col-md-12">
            <p class="text-danger" id="paragraph"></p>
        </div>
        <button type="submit" class="btn btn-success btn-block">send</button>
    </div>
</div>
...
```

```javascript
$("#ID").change(function (e) {
    var selected = $("#ID :selected").text();
    var text = e.type;
    $("#secondInput").val(selected);
});
```

## 🅱️ Has Attribute

* المان‌هایی که دارای یک خصیصه با کلید تعیین شده باشند را انتخاب نماید

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_24">
            Has Attribute Selector
        </a>
    </div>
    <div class="col-md-9">
        <div class="alert alert-warning" HasAttribute="HasAttribute">test</div>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_24").click(function () {
    $("div[HasAttribute]").fadeOut(500);
});
```

## 🅱️ Multiple Attribute Selector

* اگر همزمان از چند خصیصه با نام کلیدواژه خاص استفاده میکرد

```html
div class="well">
<div class="col-md-3 pull-left">
    <a class="btn btn-warning btn-block" id="Button_30">
        multiple Attribute Selector
    </a>
</div>
<div class="col-md-9">
    <div class="MultipleAttribute" multipleAttribute="Test">
        <p>
            Hello in a paragraph
        </p>
    </div>
</div>
<div class="clearfix"></div>
</div>
```

```javascript
$("#Button_30").click(function () {
    $("div[class][multipleAttribute*='Te']").fadeOut(500); //اگر از کلاس و از مالتیپل‌آتریبیوت استفاده میکرد که شامل عبارت خاص بود
    //
});
```

## 🅱️ Multiple Selector

* انتخاب چند المان بصورت همزمان

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_31">
            multiple Selector
        </a>
    </div>
    <div class="col-md-9">
        <div class="MultipleSelector">
            division with class
        </div>

        <p id="MultipleSelector">
            paragraph with id
        </p>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_31").click(function () {
    $("div.MultipleSelector , #MultipleSelector").fadeOut(500);
});
```

## 🅱️ Next Adjacent Selector یا NextTag

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_32">
            next adjacent Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="NextAdjacent">
            main selector
        </div>
        <div>
            division with class
        </div>
        <p>
            paragraph with id
        </p>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_32").click(function () {
    $("#NextAdjacent + div + p").fadeOut(500); //آی دی رو دیدی برو بعد تگ دایو تگ پی رو انتخاب کن
});
```

## 🅱️ Next Siblings Selector

* بعد از یک تگ خاص همه موارد را انتخاب کن

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_33">
            next siblings Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="NextSiblings"></div>
        <div>
            division with class
        </div>
        <p>
            paragraph with id
        </p>
        <p>
            paragraph with id
        </p>
        <p>
            paragraph with id
        </p>
        <p>
            paragraph with id
        </p>
    </div>
    <div class="clearfix"></div>
</div>
```

```javascript
$("#Button_33").click(function () {
    $("#NextSiblings ~ p").fadeOut(500); //همه تگ های بعد از آی دی را انتخاب کن
});
```

## 🅱️ This

* این دیس به چیزی که سلکت کردیم برمی‌گردد

```html

```

```javascript
$("p").click(function (e) { // هر تگ پی که موجود باشد
    $(this).css("background-color", "red");
});

```

# 🅰️ Manipulation

* در «جی‌کوئری» مبحث Manipulation(دستکاری) بمعنای تغییر یا دستکاری المان‌های «اچ‌تی‌اِم‌اِل» در DOM است.
* یکی از قدرتمندترین و پرکاربردترین بخش‌های «جی‌کوئری» که امکان ۱-اضافه ۲-حذف ۳-تغییر ۴-مدیریت محتوا و ساختار را به سهولت برای المان‌ها فراهم و مدیریت می‌کند

## 🅱️ تغییر محتوا

### ✅️ .html()

* محتوای HTML یک المان را بر می‌گرداند یا تنظیم می‌کند (فقط اولین المان را برمی‌گرداند)

```javascript
$('#title').html('<strong>عنوان جدید</strong>');
```

### ✅️ .text()

* تمام محتوای متنی المان‌های انتخابی را با هم ترکیب کرده و برمی‌گرداند (بدون HTML)

```javascript
$('#description').text('این یک توضیح است.');
```

## 🅱️ دستکاری کلاس‌ها

### ✅️ .addClass()

* اضافه نمودن کلاس

```javascript
$('div').addClass('MyCssClass');
$('#myList li').addClass('MyCssClass');
```

```javascript
$("#IDBtn").click(function () {
    $("#IdDiv p").addClass(function (index, currentClass) {
        if (index === 1) {
            return "MyCssClass";
        } else {
            return "test";
        }
    });
});
```

```javascript
$("#IDBtn").click(function () {
    $("#IdDiv p").addClass(function (index, currentClass) {
        if (currentClass.toLowerCase().indexOf("test") >= 0) { // indexOf: بررسی کند که مقدار تست در داخل رشته وجود دارد یا خیر اگر بلی آنگاه مقدار را بزرگتر و مساوی صفر برمی‌گرداند
            return "";
        } else {
            return "MyCssClass";
        }
    });
});
```

### ✅️ .removeClass()

* حذف نمودن کلاس

```javascript
$("#IDBtn").click(function () {
    $("#IdDiv p").removeClass(function (index, currentClass) {
        if (index === 0) {
            return "MyCssClass";
        } else {
            return "";
        }
    });
});
```

### ✅️ .toggleClass()

* این تابع به صورت خودکار چک می‌کند که آیا المان دارای کلاس مشخص شده است یا خیر
    * اگر داشته باشد آنگاه کلاس را پاک می‌کند
    * اگر نداشته باشد آنگاه کلاس را اضافه می‌کند
* فقط کلاس‌ها را تغییر می‌دهد، محتوای HTML یا متن را تغییر نمی‌دهد
* برای موارد toggle menu, dark mode, active states, animation classes مناسب است
* بهترین استفاده آن زمانی است که نمی‌دانید المان دارای کلاس هست یا نه و می‌خواهید خودکار تعیین شود

```javascript
$(selector).toggleClass("نام کلاس");
$('button').toggleClass('active');
```

* عبارت condition: یک مقدار بولین (true یا false) است.
    * اگر true باشد، کلاس اضافه می‌شود
    * اگر false باشد، حذف می‌شود.

```javascript
$(selector).toggleClass("نام کلاس", condition); // condition is TRUE or FALSE
```

#### ☑️ مثال۱:سوییچ کردن یک کلاس (مثل dark mode)

```html

<button id="toggleBtn">فعال/غیرفعال کردن تم تاریک</button>
<div id="box" style="width: 200px; height: 200px; background: #eee;"></div>
```

```css
.dark-mode {
    background: #333;
    color: white;
}
```

```javascript
$('#toggleBtn').click(function () {
    $('#box').toggleClass('dark-mode');
});
```

#### ☑️ مثال۲:تغییر دادن چند کلاس با هم

```javascript
$('#myElement').toggleClass('class1 class2 class3');
```

#### ☑️ مثال۳:تغییر دادن چند کلاس با هم همراه با شرط

```javascript
let isHighlighted = true;
$('#myElement').toggleClass('highlighted', isHighlighted);
```

### ✅️ .hasClass()

* چک کند که آیا المان دارای یک کلاس خاص است
* اگر بلی آنگاه مقدار true برمی‌گرداند وگرنه مقدار False برمیگرداند

```javascript
$("#IDBtn").click(function () {
    $("#IdDiv p").removeClass(function () {
        var status = $(this).hasClass("MyCssClass"); // آیا دارای کلاس داده شده است یا خیر
        if (status) {
            return "MyCssClass";
        } else {
            return "MyCssClass2";
        }
    });

});
```

## 🅱️ .css()

* دستکاری «سی‌اِس‌آِس»
* تنظیم استایل‌های CSS
* خاصیت‌های «سی‌اِس‌اِس» را تنظیم یا بخواند

### Get Propertyname

```javascript
var x = $(selector).css(Propertyname); //  Get property

var widthOfElemet = $(this).css("width")
var data = $(this).css(["width", "height"])

var width = $(this).width();
var innerWidth = $(this).innerWidth(); // پهنا به همراه پدینگ
var outerWidth = $(this).outerWidth(); // پهنا به همراه پدینگ به همراه ضخامت بوردر
var realOuterWidth = $(this).outerWidth(true); // پهنا به همراه پدینگ به همراه ضخامت بوردر به همراه مارجینگ
$(".myBox").click(function (e) {
    var offset = $(this).offset();
    var top = offset.top;
    var left = offset.left;
});
```

### ✅️ Set Propertyname

```javascript
$(selector).css(Propertynamem, value); // set property 
$('#box').css('color', 'red');
$('#box').css({'background-color': 'yellow', 'font-size': '20px'});
$('#myList').css('color', 'blue');
$(this).width(function () {
    return 300;
});
$(this).width(300)
````

### ✅️ scroll

```javascript
$(".myBox").click(function (e) {
    $("#ID").scrollLeft(100); // از سمت چپ ۱۰۰ تا خودکار اسکرول می‌شود
    $("#ID").scrollTop(100); // اسکرول ۱۰۰ پیکسل از سمت بالا

    // $("#ID").scrollTop();
});
```

### ✅️ offset

‌موقعیت اِلِمان کنونی نسبت به داکیومنت

```javascript
$(".myBox").click(function (e) {
    var offset = $(this).offset();
    var top = offset.top;
    var left = offset.left;
});

$(this).offset({left: 0, top: 0});
```

### ✅️ positions

‌موقعیت اِلِمان کنونی نسبت به آفست والد خود

```javascript
$(".myBox").click(function (e) {
    var position = $(this).position();
    var top = position.top;
    var left = position.left;
});
```

## 🅱️ .attr()

* به منظور دریافت مقدار یا تنظیم مقدار جدید به یک ویژگی از تگ‌های اچ تی ام ال مورد استفاده قرار می‌گیرد
* ویژگی‌های HTML مثل src, href, class و غیره را تنظیم یا بخوانید

### ✅️ Get Attribute

```javascript
$("#test").click(function (e) {
    var inputValue = $("#input").attr("value"); // value is attribute
    alert(inputValue);
});
```

```javascript
$(selector).attr(attributeName, function () {
    return value;
});
```

```javascript
$('img').attr('src', 'new-image.jpg');
```

### ✅️ Set Attribute

```javascript
$(selector).attr(attributeName, value);
$(selector).attr({
    attributeName1: value1,
    attributeName2: value2
});
```

### ✅️ RemoveAttributes

* یک ویژگی را حذف کند

```javascript
$("#input").removeAttr("class");
```

```javascript
setInterval(() => {
    $("#input").attr("class", "form-control");
}, 3000);
```

## 🅱️ .prop()

همانند attr می‌باشد ولی با ای تفاوت که تابع attr همان مقدار که تگ توسط آن بوجود آمده را در خود دارد ولی مقدار prop مقدار کنونی که تغییر کرده را نگهداری میکند

* مثلا اگر یک تکس‌باکس دارای مقدار اولیه باشد در این صورت مقدار attr آن همان نوشته است ولی اگر متن را توسط جاوااسکریپت تغییر بدهیم آنگاه تابع prop مقدار تغییر یافته را نشان میدهد و تابع attr همچنان همان مقدار گذشته را نگهداری میکند

```javascript
$(selector).prop(attributeName);
```

### ✅️ Get Attribute

```javascript
$("#ID").prop("value", function () {
    return "Behrooz";
});
```

```javascript
$('input').prop('disabled', true);
```

### ✅️ Set Attribute

```javascript
$("#input2").prop("value", "changed");

$("#input2").prop({
    value: "MyCustomValue",
    class: "NewClass"
});
```

```javascript
setInterval(() => {
    $("#input2").prop("class", "form-control");
}, 3000);
```

### ✅️ Remove Attribute

```javascript
$("#input2").removeProp("test");
```

### ✅️ .val

گِت کردن و سِت کردن مقادیر متنی که در فرم‌ها و موارد متنی کاربرد دارد

```javascript
$("#input3").val("newText"); // مقدار متنی به مقدار جدید تغییر می‌کند

var data = $("#input3").val(); // دریافت مقدار جدید

alert(data);
```

## 🅱️ wraps

* در jQuery ، توابع wrap(), wrapInner(), و wrapAll() همه مربوط به جاسازی (wrapping) المان‌ها با تگ HTML دیگری هستند،
* این سه تابع برای "پوشاندن" المان‌ها با یک المان جدید استفاده می‌شوند.

فرض کنید قطعه کد زیر را دارید

```html

<div class="box">FirstContent</div>
<div class="box">SecondContent</div>
```

### ✅️ .wrap()

* هر المان جداگانه در مجموعه انتخابی شما را با یک تگ HTML حوله‌گیری (wrap) می‌کند.
* هر المان به طور جداگانه یک والد جدید پیدا می‌کند.
* هر المان جداگانه wrap می‌شود(تعداد والدها: به تعداد المان‌ها)
* هنگام استفاده: وقتی می‌خواهیم هر المان جداگانه یک والد جدید داشته باشد (مثلاً لیست‌های جداگانه)

با اجرای کد جی‌کوئری زیر

```javascript
$('.box').wrap('<div class="wrapper"></div>');
```

نتیجه به شکل زیر در خواهد آمد

```html

<div class="wrapper">
    <div class="box">FirstContent</div>
</div>
<div class="wrapper">
    <div class="box">SecondContent</div>
</div>
```

### ✅️ .wrapInner()

* به جای اینکه خود المان را wrap کنیم، محتوای آن را wrap می‌کنیم
* محتوای داخل هر المان را با یک تگ HTML جدید wrap می‌کند — یعنی فقط روی بچه‌های مستقیم (innerHTML)  عمل می‌کند.
* محتوای داخل هر المان wrap می‌شود(تعداد والدها: به تعداد المان‌ها)
*
    * هنگام استفاده: وقتی می‌خواهیم فقط محتوای یک المان را بپوشانیم (بدون تغییر خود المان)

با اجرای کد جی‌کوئری زیر

```javascript
$('.box').wrapInner('<div class="inner-wrapper"></div>');
```

نتیجه به شکل زیر در خواهد آمد

```html

<div class="box">
    <div class="inner-wrapper">FirstContent</div>
</div>
<div class="box">
    <div class="inner-wrapper">SecondContent</div>
</div>
```

### ✅️ .wrapAll()

* همه المان‌های انتخابی را با یک تگ HTML با هم wrap می‌کند — یعنی تمام المان‌ها درون یک المان جدید قرار می‌گیرند.
* تمام المان‌ها با هم یک والد مشترک پیدا می‌کنند.
* تمام المان‌ها با هم یک wrap می‌شوند(تعداد والدها: فقط یک والد)
* هنگام استفاده: وقتی می‌خواهیم چند المان مختلف را با یک تگ واحد wrap کنیم (مثلاً یک section برای چند عنصر)

با اجرای کد جی‌کوئری زیر

```javascript
$('.box').wrapAll('<div class="all-wrapper"></div>');
```

نتیجه به شکل زیر در خواهد آمد

```html

<div class="all-wrapper">
    <div class="box">FirstContent</div>
    <div class="box">SecondContent</div>
</div>
```

### ✅️ Return  unwrap

* تابع unwrap() والد مستقیم المان(های) انتخابی را حذف می‌کند — یعنی فقط والد را پاک می‌کند و المان‌های اصلی باقی می‌مانند
* اگر یک المان توی یک تگ دیگه wrap شده باشه، با unwrap() فقط اون تگ wrap کننده حذف می‌شه
* unwrap() فقط یک سطح بالا می‌رود.
* اگر چندین لایه wrap وجود داشته باشد، فقط یک لایه را حذف می‌کند.

بافرض این که کد به شکل زیر باشد

```html

<div class="wrapper">
    <div class="box">FirstContent</div>
</div>
<div class="wrapper">
    <div class="box">SecondContent</div>
</div>
```

با استفاده از این کد jQuery:

```javascript
$('.box').unwrap();
```

نتیجه:

```html

<div class="box">FirstContent</div>
<div class="box">SecondContent</div>
```

### ✅️ Return wrapInner

Before:

```html

<div class="box">
    <div class="inner-wrapper">FirstContent</div>
</div>
```

Code:

```javascript
$('.box').contents().unwrap();
```

After:

```html

<div class="box">FirstContent</div>
```

### ✅️ Return wrapAll

* برای wrapAll()، معکوس مستقیمی وجود ندارد، ولی می‌توانید والد مشترک را پاک کنید

Before:

```html

<div class="all-wrapper">
    <div class="box">FirstContent</div>
    <div class="box">SecondContent</div>
</div>
```

Code:

```javascript
$('.all-wrapper').children().unwrap();
```

After:

```html

<div class="box">FirstContent</div>
<div class="box">SecondContent</div>
```

## 🅱️ Insertion (درج کردن)

* توابعی نظیر after و before و insertAfter و insertBefore
* درج المان‌ها یا محتوا در موقعیت‌های خاص نسبت به المان‌های دیگر استفاده می‌شوند.
* تفاوت اصلی بین آنها این است که چه چیزی را جایگذاری می‌کنند و کجا قرارشان می‌دهند

| تابع                    | نحوه فراخوانی                     | عملکرد                                         | مثال                                    |
|-------------------------|-----------------------------------|------------------------------------------------|-----------------------------------------|
| `.after(content)`       | `$(selector).after(content)`      | **بعد از** هر المان انخابی قرارمی‌دهد          | `$('.box').after('<p>جدید</p>')`        |
| `.before(content)`      | `$(selector).before(content)`     | **قبل از** هر المان انتخابی قرارمی‌دهد         | `$('.box').before('<p>جدید</p>')`       |
| `.insertAfter(target)`  | `$(content).insertAfter(target)`  | **محتوا را بعد از** تارگت انتخابی قرارمی‌دهد   | ` $('<p>...</p>').insertAfter('.box')`  |
| `.insertBefore(target)` | `$(content).insertBefore(target)` | **محتوا را قبل از** تارگت  انتخابی قرارمی‌دهد  | ` $('<p>...</p>').insertBefore('.box')` |
| `.prepend(content)`     | `$(selector).prepend(content)`    | محتوا را در ابتدای هر المان انتخابی قرارمی‌دهد | `$('.box').prepend('<p>...</p>')`       |
| `.prependTo(target)`    | `$(content).prependTo(target)`    | المان جدید را در ابتدای تارگت قرارمی‌دهد       | `$('<p>...</p>').prependTo('.box')`     |
| `.append(content)`      | `$(selector).append(content)`     | محتوا را در انتهای هر المان انتخابی قرارمی‌دهد | `$('.box').append('<p>...</p>')`        |
| `.appendTo(target)`     | `$(content).appendTo(target)`     | المان جدید را در انتهای تارگت قرارمی‌دهد       | `$('<p>...</p>').appendTo('.box')`      |
| `.clone()`              | `$(selector).clone()`             | یک کپی از المان انتخابی می‌گیرد                | `$('.box').first().clone()`             |

---




قطعه کد زیر را مد نظر قرار دهید

```html

<div class="box">FirstContent</div>
<div class="box">SecondContent</div>
```

### ✅️ .after( content )

* محتوای داده شده را بعد از هر یک از المان‌های انتخابی قرارمی‌دهد.

```javascript
$('.box').after('<p>After FirstContent</p>');
```

نتیجه: بعد از هر باکس یک «تگ‌پی» درج شد.

```html

<div class="box">FirstContent</div>
<p>After FirstContent</p>

<div class="box">SecondContent</div>
<p>After FirstContent</p>
```

### ✅️ .before( content )

* محتوای داده شده را قبل از هر یک از المان‌های انتخابی قرارمی‌دهد.

```javascript
$('.box').before('<p>Before FirstContent</p>');
```

نتیجه: قبل از هر باکس یک «تگ‌پی» درج شد.

```html
<p>Before FirstContent</p>
<div class="box">FirstContent</div>

<p>Before FirstContent</p>
<div class="box">SecondContent</div>
```

### ✅️ .insertAfter( target )

* المان(های) انتخابی را بعد از تارگت قرارمی‌دهد.
* در این مورد ابتدا المان۱ انتخاب می‌شود و بعد گفته می‌شود که المان۲ به بعد از المان۱ افزوده گردد

```javascript
$('<p>NewContent</p>').insertAfter('.box');
```

نتیجه:

```html

<div class="box">FirstContent</div>
<p>NewContent</p>

<div class="box">SecondContent</div>
<p>NewContent</p>
```

### ✅️ .insertBefore( target )

* المان(های) انتخابی را قبل از تارگت قرارمی‌دهد.

```javascript
$('<p>NewContent</p>').insertBefore('.box');
```

نتیجه:

```html
<p>NewContent</p>
<div class="box">FirstContent</div>

<p>NewContent</p>
<div class="box">SecondContent</div>
```

### ✅️ .prepend( content )

* محتوا را در ابتدای هر المان انتخابی قرارمی‌دهد (داخل المان، قبل از سایر محتوا).

```javascript
$('.box').prepend('<strong>شروع: </strong>');
```

نتیجه: به هر باکس یک استرانگ در ابتدای آن اضافه می‌کند

```html

<div class="box">
    <strong>Start: </strong>FirstContent
</div>
<div class="box">
    <strong>Start: </strong>SecondContent
</div>
```

### ✅️ .prependTo( target )

* المان جدید را در ابتدای تارگت قرارمی‌دهد.
* ⚠️ در این حالت، شما اول المان جدید را می‌سازید و بعد به جی‌کوئری می‌گویید "این رو ببر و در ابتدای المان دیگری قرار بده".

```javascript
$('<strong>Start: </strong>').prependTo('.box');
```

نتیجه:همان عملکرد prepend() ولی با سینتکس معکوس

```html

<div class="box">
    <strong>Start: </strong>FirstContent
</div>
<div class="box">
    <strong>Start: </strong>SecondContent
</div>
```

### ✅️ .append( content )

* محتوا را در انتهای هر المان انتخابی قرارمی‌دهد (داخل المان، بعد از سایر محتوا).

```javascript
$('.box').append('<strong> - پایان</strong>');
```

نتیجه:به هر باکس یک استرانگ در انتهای آن اضافه می‌کند

```html

<div class="box">
    FirstContent<strong> - End</strong>
</div>
<div class="box">
    SecondContent<strong> - End</strong>
</div>
```

### ✅️ .appendTo( target )

* المان جدید را در انتهای تارگت قرارمی‌دهد.
* مثل prependTo، ولی در انتهای المان مقصد.

```javascript
$('<strong> - پایان</strong>').appendTo('.box');
```

نتیجه:همانند مثال قبل

```html

<div class="box">
    FirstContent<strong> - End</strong>
</div>
<div class="box">
    SecondContent<strong> - End</strong>
</div>
```

### ✅️ .clone()

* یک کپی از المان(های) انتخابی می‌گیرد.
* این کاربردی است وقتی می‌خواهید یک المان را جابه‌جا کنید یا کپی کنید بدون اینکه اصل آن حذف شود.

```javascript
$('.box').first().clone().appendTo('body');
```

نتیجه: اولین باکس کپی شده به انتهای بادی اضافه شد

```html

<div class="box">FirstContent</div>
<div class="box">SecondContent</div>

<!-- یک کپی اضافی از اولین .box -->
<div class="box">FirstContent</div>
```

## 🅱️ Replacement (جایگزینی)

| تابع             | نحوه فراخوانی                      | عملکرد                                                                               | مثال                                   |
|------------------|------------------------------------|--------------------------------------------------------------------------------------|----------------------------------------|
| `.replaceWith()` | `$(selector).replaceWith(content)` | المان(ها) را با محتوای جدید **جایگزین** می‌کند                                       | `$('.box').replaceWith('<p>جدید</p>')` |
| `.replaceAll()`  | `$(content).replaceAll(selector)`  | محتوای جدید را جایگزین تمام المان‌های `selector` می‌کند (سینتکس معکوس `replaceWith`) | `$('<p>جدید</p>').replaceAll('.box')`  |

---



قطعه کد زیر را مد نظر قرار دهید

```html

<div class="box">FirstContent</div>
<div class="box">SecondContent</div>
```

### ✅️ .replaceWith()

* المان(ها) انتخابی را با محتوای جدید جایگزین می‌کند.

```javascript
$('.box').replaceWith('<div class="new-box">New Content</div>');
```

نتیجه:

```html

<div class="new-box">New Content</div>
<div class="new-box">New Content</div>
```

### ✅️ .replaceAll()

* محتوای جدید را جایگزین تمام المان‌های target می‌کند (سینتکس معکوس replaceWith).

```javascript
$('<div class="new-box">New Content</div>').replaceAll('.box');
```

نتیجه: همانند قبل

```html

<div class="new-box">New Content</div>
<div class="new-box">New Content</div>
```

✅ فقط تفاوت در نحوه فراخوانی است.

## 🅱️ Removal (حذف کردن)

| تابع        | نحوه فراخوانی          | عملکرد                                                                             | مثال                 |
|-------------|------------------------|------------------------------------------------------------------------------------|----------------------|
| `.detach()` | `$(selector).detach()` | المان(ها) را از «دام یا دی‌اُاِم» حذف می‌کند ولی **داده/رویداد‌ها** را نگه می‌دارد | `$('.box').detach()` |
| `.remove()` | `$(selector).remove()` | المان(ها) را از «دام یا دی‌اُاِم» حذف می‌کند و **داده/رویداد‌ها** را پاک می‌کند    | `$('.box').remove()` |
| `.empty()`  | `$(selector).empty()`  | **محتوای داخلی** المان(ها) را پاک می‌کند (ولی خود المان‌ها باقی می‌مانند)          | `$('.box').empty()`  |

---




قطعه کد زیر را مد نظر قرار دهید

```html

<div class="box">FirstContent</div>
<div class="box">SecondContent</div>
```

### ✅️ .detach()

* المان(ها) را از DOM حذف می‌کند، ولی رویداد‌ها و داده‌های جی‌کوئری متصل به آن‌ها را حفظ می‌کند — مناسب برای استفاده دوباره.

```javascript
$('.box').detach();
```

نتیجه:

```html
<!-- هیچ المان .box وجود ندارد -->
```

* ولی اگر بعداً دوباره اضافه کنید (مثلاً با appendTo())، رویداد‌ها و داده‌ها باقی خواهند ماند.

### ✅️ .remove()

* مثل detach()، ولی تمام داده‌ها و رویداد‌های jQuery متصل به المان‌ها را پاک می‌کند

```javascript
$('.box').remove();
```

نتیجه:

```html
<!-- هیچ المان .box وجود ندارد -->
```

ولی برخلاف detach()، اگر بخواهید دوباره استفاده کنید، باید مجدداً ساختار کاملش را درست کنید.

### ✅️ .empty()

* محتوای داخلی هر المان (مانند متن و فرزندان HTML) را پاک می‌کند، ولی خود المان والد را نگه می‌دارد

```javascript
$('.box').empty();
```

نتیجه:

```html

<div class="box"></div>
<div class="box"></div>
```

محتوای FirstContent و SecondContent حذف شده‌اند، ولی <div class="box"> ها باقی مانده‌اند

</div>

