# Basic Animations

## .show()

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

## .hide()

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

## .toggle()

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

# Sliding Animation

## .slideDown()

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

## .slideUp()

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

## .slideToggle()

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

# Fading Animation

## .fadeIn();

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

## .fadeOut()

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

## .fadeTo(duration, opacity)

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

## .fadeToggle(duration)

* وضعیت المان(ها) را با انیمیشن شفاف/ناشفاف کردن معکوس می‌کند.

```javascript

$("#FadeToggleButton").click(function (e) {
    // 1️⃣️
    $("#FadeToggleTest p").fadeToggle(200);
});
```

# Custome Animation

## .animate(propery,duration,easing)

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

## .finish()

```javascript
$("#FinButton").click(function (e) {
    $(".inside").finish();
});
```

# QUEUE

* هر کار انیمیشن که داریم انجام میدهیم یک صف نامیده می‌شوند
* گاهی میخواهیم چندین فعالیت و کار پشت سر هم انجام شوند تا یک تجربه انیمیشن بوقوع بپیوندد، آنگاه هر کدام یک صف است

## .queue() | .dequeue()

* اگر بخواهیم یک صف به مجموعه صفوف انیمیشن اضافه نماییم از روش زیر استفاده می‌کنیم
* نکته: در انهای صف حتما باید از دیکیو استفاده شود تا صف بعدی به اجرا دربیاید وگرنه صف اضافه شده پس از انجام سبب توقف مجموعه صف می‌شوند
* تابع queue به شما اجازه می‌دهد تا فانکشن‌ها را به صف پیش‌فرض (یا یک صف مشخص) اضافه کنید ، تا بعداً به ترتیب اجرا شوند.
* تابع dequeue مرحله بعدی در صف را اجرا می‌کند. این تابع زمانی استفاده می‌شود که شما یک تابع را به صف اضافه کرده‌اید و می‌خواهید jQuery را وادار کنید به اجرای مرحله بعدی ادامه دهد .

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

## .clearQueue()

* سبب پاک نمودن اعضای صف انیمیشن می‌شود(محموعه عضوهای صف انیمیشن که از کنار هم قرار دادن آن انیمشین کامل اجرا می‌شود)
* البته عضو در داخل صف انیمیشن(بعنوان تنها عضو صف[زیرا بقیه پاک شدند])به اجرای خود ادامه می‌دهد و پس از اتمام کار آن انیمشن متوقف می‌شود

```javascript
$("#ClearButton").click(function (e) {
    $(".inside").clearQueue();
});
```

## .stop()

انیمیشن در حین کار خود در همان حالت کنونی متوقف شود

```javascript
$("#btn").click(function (e) {
    $("#selector").stop();
});
```

```javascript
$("#selector").stop().clearQueue();
```

## $.fx.off

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
* این تغییر وضعیت به صورت چرخشی  ادامه پیدا می‌کند.


در مثال زیر هر بار روی دکمه کلیک کنید، وضعیت انیمیشن تغییر می‌کند: اگر فعال باشد، جعبه حرکت می‌کند. اگر غیرفعال باشد، حرکت بدون انیمیشن اتفاق می‌افتد (یا اصلاً حرکت نمی‌کند، بسته به تنظیمات).
```html
<button id="toggle">Toggle Animation</button>
<div id="box" style="width:100px;height:100px;background:red;position:relative"></div>

<script>
var toggleFx = function() {
    $.fx.off = !$.fx.off;
};

$('#toggle').on('click', function() {
    toggleFx(); // توگل وضعیت انیمیشن
    $('#box').animate({ left: '+=100' }, 1000);
});
</script>
```


*     اگر $.fx.off = true باشد، تمام توابعی مثل .animate(), .fadeIn(), .slideUp() و غیره بلافاصله اجرا می‌شوند بدون هیچ انیمیشنی  — یعنی فقط تغییرات CSS اعمال می‌شوند ولی "انتقال" وجود ندارد. 
