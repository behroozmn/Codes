* Syntax:
    ```
    $(selector).event(function (){});
    ```

# 1.MouseEvents

## 1.MouseSingleClick

  ```javascript
  $("#Button_1").click(function () {
    $("#ID").fadeOut();
});
  ```

## 2.MouseDoubleClick

  ```javascript
  $("#Button_2").dblclick(function () {
    $("#ID").fadeOut();
});
  ```

## 3.MouseEnter

* وقتی وارد محدوده مختصاتی شیء بشویم رخ می‌دهد و تفاوتی در شیء فرزند نمی‌کند
* وقتی وارد می‌شویم تنها ایونت رخ میدهد و فرزند ها تفاوتی نمیکند

  ```javascript
  $("#Button_5").mouseenter(function () {
      $("#enterAndLeave").fadeOut();
  });
  ```

## 4.MouseOver[Also Childs]

* اگر وارد فرزند (در داخل همان شیء) بشویم به منزله‌این است که گویی به شیء ورود کرده‌ایم
* وقتی وارد فرزند های می‌شویم هم بازم ایونت رخ میدهد

  ```javascript
  var over=0;
  $("#OverEvent").mouseover(function () { 
    over++;
    $("#OverEvent span").text(over);
  });
  ```

## 5.MouseDown

* کلیک روی شیء و نگهداشتن آن

  ```javascript
  $("#Button_4").mousedown(function () {
      $("#mouseUpAndDown").fadeOut();
  });
  ```

## 6.MouseUp

* کلید روی شیء و نگهداشتن و رها کردن کلیک از آن شیء

  ```javascript
  $("#Button_4").mouseup(function () {
      $("#mouseUpAndDown").fadeIn();
  });
  ``

## 7.MouseLeave

* فقط باید از محدوده مختصاتی شیء خارج شویم
* اگر در داخل شیء وارد فرزند شویم یعنی همچنان داخل شیء هستیم

  ```javascript
  $("#Button_5").mouseleave(function () {
      $("#enterAndLeave").fadeIn();
  });
  ```

## 8.MouseOut[Also Childs]

* اگر وارد فرزند بشویم به منزله‌این است که گویی از محدوده شیء خارج شده‌ایم

  ```javascript
  var out = 0;
  $("#OutEvent").mouseout(function () {
    out++;
    $("#OutEvent span").text(out);
  });
  ```

## 9.MouseMove

* جرکت درداخل شیء

  ```javascript
  $("#Button_6").mousemove(function (e) {
    var pageX = e.pageX;
    var pageY = e.pageY;
    var total = "(" + pageX + "," + pageY + ")";
    $("#move span").text(total); // نمایش در داخل اسپنی که داخل شیء دارای آی دی است
  });
  ```

## 10.Hover

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

# 2.KeboardEvents

## 1.keydown

* وقتی دکمه فشرده می‌شود، قبل از بالا آوردن کلید این رویداد رخ میدهد

```javascript
$("#firstInput").keydown(function (e) {
    var text = $("#firstInput").val(); // مقدار درونی input را برمیگرداند
    $("#secondInput").val(text);
});
```

## 2.keyup

* وقتی کلید فشرده شده است و دقیقا هنگامی که دکمه را رهاسازی میکنیم این رویداد رخ می‌دهد

```javascript
$("#firstInput").keyup(function (e) {
    var text = $("#firstInput").val(); // مقدار درونی input را برمیگرداند
    $("#secondInput").val(text);
});
```

## 3.keypress

* همانند «کی‌داون» است با این تفاوت که دکمه های غیر کاراکتری عمل نخواهد کرد
* غیر فعال در دکمه هایی که تاثیر کاراکتری ندارد

```javascript
$("#firstInput").keydown(function (e) {
    var text = $("#firstInput").val(); // مقدار درونی input را برمیگرداند
    $("#secondInput").val(text);
    console.log(e.type);
});
```

# 3.FormEvents

## 0.PreReqirement Codes

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

## 1.blur

* وقتی داخل یک شیء قرار میگیرد و از آن خارج می‌شوید
* مثلا یک تکس‌باکس که ورود میکنیم در آن و سپس از آن خارج می‌شویم
* فقط برای یک المان معنی پیدا میکند و کاری با المان‌های دیگر ندارد

```javascript
$("#firstInput").blur(function (e) {
    var text = e.type;
    $("#secondInput").val(text);
});
```

## 2.focusout[Parental Elemet]

* same as blur
* اگر روی والد درنظر بگیریم آنگاه اگر از روی هر فرزند خارج شویم رخداد اجرا می‌شود

```javascript
$("#parent").focusout(function (e) {
    var text = e.type;
    $("#secondInput").val(text);
});
```

## 3.focus

* هنگامی که وارد المان می‌شویم
* فقط برای یک المان معنی پیدا میکند و کاری با المان‌های دیگر ندارد

```javascript
$("#firstInput").focus(function (e) {
    var text = e.type;
    $("#secondInput").val(text);
});
```

## 4.focusin[Parental Elemet]

* same as focus
* اگر روی والد درنظر بگیریم آنگاه اگر از در هر فرزند وارد شویم رخداد اجرا می‌شود

```javascript
$("#parent").focusin(function (e) {
    var text = e.type;
    $("#secondInput").val(text);
});
```

## 5.change

* change the element value

```javascript
$("#change").change(function (e) {
    var selected = $("#change :selected").text();
    var text = e.type;
    $("#secondInput").val(selected);
});
```

## 6.select

* وقتی مقداری از متن داخل یک باکس را انتحاب می‌کنیم و به رنگ آبی درمی‌آید و قابلیت کپی و غیره پیدا میکنند

```javascript
$("#firstInput").select(function (e) {
    var text = e.type;
    $("#secondInput").val(text);
});
```

## 7.submit

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

# 4.window

## 1.resize

```javascript
$(window).resize(function () {
    $("#firstInput").val($(window).width());
});
```

## 2.scrol

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

## 3.ready

* وقتی یک کامپوننت بصورت کامل لود شود این رویداد رخ می‌دهد

```javascript
$("#myImage").ready(function () {
    ShowAlert();
});
```

## 4.holdReady

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

# 5.EventHandlerAttachment

## 1.on

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

## 2.of

* غیر فعال کردن یک رویداد از یک مولفه

```javascript
$("p").click(function (e) {
    $(this).css("background-color", "red");
});

$("#ID").click(function (e) {
    $("p").off("click");
});
```

## one

* فقط یک بار رویداد اجرا شود

```javascript
$("p").click(function (e) {
    alert('hello');
});

$("p").one("click", function (e) {
    alert('hello');
});
```

# 6.Trigger

```javascript
$("#ID1").click(function (e) {
    alert('hello');
});

$("#ID2").click(function (e) {
    $("#ID1").trigger("click");
});
```

# 7.TriggerHandler

* انجام کارهای ظاهری و نه همه کارهای رویداد در مولفه اصلی که قرار است آن را اجرا کند
* اگر شما مثلا کاری انجام دهید و در انتها به صفحه ای ارجاع بدید آنگاه کارهای ظاهری و صفحه را انجام میدهد ولی به صفحه دیگر نمی‌رود

# 8.proxy

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

# 9.currentTarget

```javascript
$("#ID").click(function (event) {
    if (event.currentTarget === this) {
        alert('true');
    }
});
```

# 10.data

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

# 11.DelegateTarget

[//]: # (TODO: این گزینه رو باید بعدا مجددا آموزش ببینم)

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

# 12.preventDefault

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

# 13.stopImmediatePropagation

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

# 14.stopPropagation

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

# 15.NodeName

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

# 16.EventType

```javascript
$("#ID").click(function (e) {
    if (e.type == click) { // click , dblclick, mousemove...
        alert("Clicked")
    }
});
```

# 17.TimeStamp

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

# 18.which

* عدد اسکی را برمیگرداند

```javascript
$("#ID_Input").on("mousedown keydown", function (e) {
    $("#ListBox").append("type : " + e.type + " - " + "which :" + e.which + "<br/>");
});
```


