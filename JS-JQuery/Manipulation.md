# Manipulation

* در «جی‌کوئری» مبحث Manipulation(دستکاری) بمعنای تغییر یا دستکاری المان‌های «اچ‌تی‌اِم‌اِل» در DOM است.
* یکی از قدرتمندترین و پرکاربردترین بخش‌های «جی‌کوئری» که امکان ۱-اضافه ۲-حذف ۳-تغییر ۴-مدیریت محتوا و ساختار را به سهولت برای المان‌ها فراهم و مدیریت می‌کند

## Add Elements

### .append()

* اضافه کردن محتوا به انتهای یک المان

```javascript
$('#myDiv').append('<p>پاراگراف جدید</p>');
```

### .prepend()

* اضافه کردن محتوا به ابتدای یک المان

```javascript
$('#myList').append('<li>آیتم ۲</li>');
```

### .before()

* اضافه کردن محتوی قبل از المان

```javascript
$('#myList').before('<h2>لیست من</h2>');
```

### .after()

* اضافه کردن محتوی بعد از المان

## Remove Elements

### .remove()

* کاملاً حذف کند

```javascript
$('#oldElement').remove();
```

### .empty()

* فقط محتوای داخلی را پاک کند

## تغییر محتوا

### .html()

* محتوای HTML یک المان را بر می‌گرداند یا تنظیم می‌کند (فقط اولین المان را برمی‌گرداند)

```javascript
$('#title').html('<strong>عنوان جدید</strong>');
```

### .text()

* تمام محتوای متنی المان‌های انتخابی را با هم ترکیب کرده و برمی‌گرداند (بدون HTML)

```javascript
$('#description').text('این یک توضیح است.');
```

## دستکاری ویژگی‌ها (Attributes)

### .attr()

* ویژگی‌های HTML مثل src, href, class و غیره را تنظیم یا بخوانید

```javascript
$('img').attr('src', 'new-image.jpg');
```

### .removeAttr()

* یک ویژگی را حذف کند

### .prop()

* خاصیت‌های DOM (مانند checked, disabled) را تنظیم یا بخوانید

```javascript
$('input').prop('disabled', true);
```

## دستکاری کلاس‌ها

### .addClass()

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

### .removeClass()

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

### .toggleClass()

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

#### مثال۱:سوییچ کردن یک کلاس (مثل dark mode)

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

#### مثال۲:تغییر دادن چند کلاس با هم

```javascript
$('#myElement').toggleClass('class1 class2 class3');
```

#### مثال۳:تغییر دادن چند کلاس با هم همراه با شرط

```javascript
let isHighlighted = true;
$('#myElement').toggleClass('highlighted', isHighlighted);
```

### .hasClass()

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

## .css()

* دستکاری «سی‌اِس‌آِس»
* تنظیم استایل‌های CSS
* خاصیت‌های «سی‌اِس‌اِس» را تنظیم یا بخواند

#### Get Propertyname

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

#### Set Propertyname

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

#### scroll

```javascript
$(".myBox").click(function (e) {
    $("#ID").scrollLeft(100); // از سمت چپ ۱۰۰ تا خودکار اسکرول می‌شود
    $("#ID").scrollTop(100); // اسکرول ۱۰۰ پیکسل از سمت بالا

    // $("#ID").scrollTop();
});
```

#### offset

‌موقعیت اِلِمان کنونی نسبت به داکیومنت

```javascript
$(".myBox").click(function (e) {
    var offset = $(this).offset();
    var top = offset.top;
    var left = offset.left;
});

$(this).offset({left: 0, top: 0});
```

#### positions

‌موقعیت اِلِمان کنونی نسبت به آفست والد خود

```javascript
$(".myBox").click(function (e) {
    var position = $(this).position();
    var top = position.top;
    var left = position.left;
});
```

## .attr()

به منظور دریافت مقدار یا تنظیم مقدار جدید به یک ویژگی از تگ‌های اچ تی ام ال مورد استفاده قرار می‌گیرد

### Get Attribute

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

### Set Attribute

```javascript
$(selector).attr(attributeName, value);
$(selector).attr({
    attributeName1: value1,
    attributeName2: value2
});
```

### RemoveAttributes

```javascript
$("#input").removeAttr("class");
```

```javascript
setInterval(() => {
    $("#input").attr("class", "form-control");
}, 3000);
```

## .prop()

همانند attr می‌باشد ولی با ای تفاوت که تابع attr همان مقدار که تگ توسط آن بوجود آمده را در خود دارد ولی مقدار prop مقدار کنونی که تغییر کرده را نگهداری میکند

* مثلا اگر یک تکس‌باکس دارای مقدار اولیه باشد در این صورت مقدار attr آن همان نوشته است ولی اگر متن را توسط جاوااسکریپت تغییر بدهیم آنگاه تابع prop مقدار تغییر یافته را نشان میدهد و تابع attr همچنان همان مقدار گذشته را نگهداری میکند

```javascript
$(selector).prop(attributeName);
```

### Get Attribute

```javascript
$("#ID").prop("value", function () {
    return "Behrooz";
});
```

### Set Attribute

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

### Remove Attribute

```javascript
$("#input2").removeProp("test");
```

### .val

گِت کردن و سِت کردن مقادیر متنی که در فرم‌ها و موارد متنی کاربرد دارد

```javascript
$("#input3").val("newText"); // مقدار متنی به مقدار جدید تغییر می‌کند

var data = $("#input3").val(); // دریافت مقدار جدید

alert(data);
```

## .clone() | .append()

از یک تگ عینا کپی میکند و به تگ دیگر اضافه می‌کند

```javascript
$("#ID").click(function (e) {
    var copied = $("#myPragraph").clone();
    $("#cloneParagraphs").append(copied);
});
```

## انواع wrap

* در jQuery ، توابع wrap(), wrapInner(), و wrapAll() همه مربوط به جاسازی (wrapping) المان‌ها با تگ HTML دیگری هستند،
* این سه تابع برای "پوشاندن" المان‌ها با یک المان جدید استفاده می‌شوند.

فرض کنید قطعه کد زیر را دارید

```html

<div class="box">محتوای ۱</div>
<div class="box">محتوای ۲</div>
```

### .wrap()

* هر المان جداگانه در مجموعه انتخابی شما را با یک تگ HTML حوله‌گیری (wrap)  می‌کند.
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
    <div class="box">محتوای ۱</div>
</div>
<div class="wrapper">
    <div class="box">محتوای ۲</div>
</div>
```

### .wrapInner()

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
    <div class="inner-wrapper">محتوای ۱</div>
</div>
<div class="box">
    <div class="inner-wrapper">محتوای ۲</div>
</div>
```

### .wrapAll()

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
    <div class="box">محتوای ۱</div>
    <div class="box">محتوای ۲</div>
</div>
```

#### برگرداندن unwrap

* تابع unwrap() والد مستقیم المان(های) انتخابی را حذف می‌کند — یعنی فقط والد را پاک می‌کند و المان‌های اصلی باقی می‌مانند
* اگر یک المان توی یک تگ دیگه wrap شده باشه، با unwrap() فقط اون تگ wrap کننده حذف می‌شه
* unwrap() فقط یک سطح بالا می‌رود.
* اگر چندین لایه wrap وجود داشته باشد، فقط یک لایه را حذف می‌کند.

بافرض این که کد به شکل زیر باشد

```html

<div class="wrapper">
    <div class="box">محتوای ۱</div>
</div>
<div class="wrapper">
    <div class="box">محتوای ۲</div>
</div>
```

با استفاده از این کد jQuery:

```javascript
$('.box').unwrap();
```

نتیجه:

```html

<div class="box">محتوای ۱</div>
<div class="box">محتوای ۲</div>
```

#### برگرداندن wrapInner

Before:

```html

<div class="box">
    <div class="inner-wrapper">محتوای ۱</div>
</div>
```

Code:

```javascript
$('.box').contents().unwrap();
```

After:

```html

<div class="box">محتوای ۱</div>
```

#### برگرداندن wrapAll

* برای wrapAll()، معکوس مستقیمی وجود ندارد، ولی می‌توانید والد مشترک را پاک کنید

Before:

```html

<div class="all-wrapper">
    <div class="box">محتوای ۱</div>
    <div class="box">محتوای ۲</div>
</div>
```

Code:

```javascript
$('.all-wrapper').children().unwrap();
```

After:

```html

<div class="box">محتوای ۱</div>
<div class="box">محتوای ۲</div>
```

## .after()|.before()|.insertAfter()|.insertBefore()

* درج المان‌ها یا محتوا در موقعیت‌های خاص نسبت به المان‌های دیگر استفاده می‌شوند.
* تفاوت اصلی بین آنها این است که چه چیزی را جایگذاری می‌کنند و کجا قرارشان می‌دهند

| تابع                    | نحوه فراخوانی                     | عملکرد                                         | مثال                                    |
|-------------------------|-----------------------------------|------------------------------------------------|-----------------------------------------|
| `.after(content)`       | `$(selector).after(content)`      | **بعد از** هر المان انخابی قرار می‌دهد         | `$('.box').after('<p>جدید</p>')`        |
| `.before(content)`      | `$(selector).before(content)`     | **قبل از** هر المان انتخابی قرار می‌دهد        | `$('.box').before('<p>جدید</p>')`       |
| `.insertAfter(target)`  | `$(content).insertAfter(target)`  | **محتوا را بعد از** تارگت انتخابی قرار می‌دهد  | ` $('<p>...</p>').insertAfter('.box')`  |
| `.insertBefore(target)` | `$(content).insertBefore(target)` | **محتوا را قبل از** تارگت  انتخابی قرار می‌دهد | ` $('<p>...</p>').insertBefore('.box')` |

---




قطعه کد زیر را مد نظر قرار دهید

```html

<div class="box">محتوای ۱</div>
<div class="box">محتوای ۲</div>
```

### .after( content )

* محتوای داده شده را بعد از هر یک از المان‌های انتخابی قرار می‌دهد.

```javascript
$('.box').after('<p>پس از محتوای ۱</p>');
```

نتیجه: بعد از هر باکس یک «تگ‌پی» درج شد.

```html

<div class="box">محتوای ۱</div>
<p>پس از محتوای ۱</p>

<div class="box">محتوای ۲</div>
<p>پس از محتوای ۱</p>
```

### .before( content )

* محتوای داده شده را قبل از هر یک از المان‌های انتخابی قرار می‌دهد.

```javascript
$('.box').before('<p>قبل از محتوای ۱</p>');
```

نتیجه: قبل از هر باکس یک «تگ‌پی» درج شد.

```html
<p>قبل از محتوای ۱</p>
<div class="box">محتوای ۱</div>

<p>قبل از محتوای ۱</p>
<div class="box">محتوای ۲</div>
```

### .insertAfter( target )

* المان(های) انتخابی را بعد از تارگت قرار می‌دهد.
* در این مورد ابتدا المان۱ انتخاب می‌شود و بعد گفته می‌شود که المان۲ به بعد از المان۱ افزوده گردد

```javascript
$('<p>NewContent</p>').insertAfter('.box');
```

نتیجه:

```html

<div class="box">محتوای ۱</div>
<p>NewContent</p>

<div class="box">محتوای ۲</div>
<p>NewContent</p>
```

### .insertBefore( target )

* المان(های) انتخابی را قبل از تارگت قرار می‌دهد.

```javascript
$('<p>NewContent</p>').insertBefore('.box');
```

نتیجه:

```html
<p>NewContent</p>
<div class="box">محتوای ۱</div>

<p>NewContent</p>
<div class="box">محتوای ۲</div>
```
