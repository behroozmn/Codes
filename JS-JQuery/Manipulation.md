# Manipulation

* در «جی‌کوئری» مبحث Manipulation(دستکاری) بمعنای تغییر یا دستکاری المان‌های «اچ‌تی‌اِم‌اِل» در DOM است.
* یکی از قدرتمندترین و پرکاربردترین بخش‌های «جی‌کوئری» که امکان ۱-اضافه ۲-حذف ۳-تغییر ۴-مدیریت محتوا و ساختار را به سهولت برای المان‌ها فراهم و مدیریت می‌کند

## 1.Add Elements

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

## 2.Remove Elements

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

## دستکاری «سی‌اِس‌آِس»

### .css()

* تنظیم استایل‌های CSS
* خاصیت‌های «سی‌اِس‌اِس» را تنظیم یا بخواند

```javascript
$('#box').css('color', 'red');
$('#box').css({
    'background-color': 'yellow',
    'font-size': '20px'
});
$('#myList').css('color', 'blue');
```