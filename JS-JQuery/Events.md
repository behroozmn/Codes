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

# 6.TriggerHandler

* انجام کارهای ظاهری و نه همه کارهای رویداد در مولفه اصلی که قرار است آن را اجرا کند
* اگر شما مثلا کاری انجام دهید و در انتها به صفحه ای ارجاع بدید آنگاه کارهای ظاهری و صفحه را انجام میدهد ولی به صفحه دیگر نمی‌رود

# 7.proxy

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

