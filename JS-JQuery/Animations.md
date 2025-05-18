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




