* Syntax:
    ```
    $(selector).event(function (){});
    ```

# 1.MouseEvents

## 1.MouseSingleClick

  ```jquery
  $("#Button_1").click(function () {
    $("#ID").fadeOut();
  });
  ```

## 2.MouseDoubleClick

  ```jquery
  $("#Button_2").dblclick(function () {
      $("#ID").fadeOut();
  });
  ```

## 3.MouseEnter

* وقتی وارد محدوده مختصاتی شیء بشویم رخ می‌دهد و تفاوتی در شیء فرزند نمی‌کند
* وقتی وارد می‌شویم تنها ایونت رخ میدهد و فرزند ها تفاوتی نمیکند

  ```jquery
  $("#Button_5").mouseenter(function () {
      $("#enterAndLeave").fadeOut();
  });
  ```

## 4.MouseOver[Also Childs]

* اگر وارد فرزند (در داخل همان شیء) بشویم به منزله‌این است که گویی به شیء ورود کرده‌ایم
* وقتی وارد فرزند های می‌شویم هم بازم ایونت رخ میدهد

  ```jquery
  var over=0;
  $("#OverEvent").mouseover(function () { 
    over++;
    $("#OverEvent span").text(over);
  });
  ```

## 5.MouseDown

* کلیک روی شیء و نگهداشتن آن

  ```jquery
  $("#Button_4").mousedown(function () {
      $("#mouseUpAndDown").fadeOut();
  });
  ```

## 6.MouseUp

* کلید روی شیء و نگهداشتن و رها کردن کلیک از آن شیء

  ```jquery
  $("#Button_4").mouseup(function () {
      $("#mouseUpAndDown").fadeIn();
  });
  ``

## 7.MouseLeave

* فقط باید از محدوده مختصاتی شیء خارج شویم
* اگر در داخل شیء وارد فرزند شویم یعنی همچنان داخل شیء هستیم

  ```jquery
  $("#Button_5").mouseleave(function () {
      $("#enterAndLeave").fadeIn();
  });
  ```

## 8.MouseOut[Also Childs]

* اگر وارد فرزند بشویم به منزله‌این است که گویی از محدوده شیء خارج شده‌ایم

  ```jquery
  var out = 0;
  $("#OutEvent").mouseout(function () {
    out++;
    $("#OutEvent span").text(out);
  });
  ```

## 9.MouseMove

* جرکت درداخل شیء

  ```jquery
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

  ```jquery
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

## 2.keup

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