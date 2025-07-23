<div style="direction: rtl">

# 🅰️ مفاهیم و نکات

*
    * Document:کل صفحه از بالا تا پایین با تمام اسکرول‌های آن
* Window: صفحه پیش رو که درصفحه مرورگر، به هرکدام از قسمت‌های اسکرول شده در ابعاد صفحه نمایش
* موضوع CDN مربوط به زمانی است که بخواهیم یک کتابخانه را بصورت آنلاین استفاده نماییم
* جاوا اسکریپت خط به خط اجرا می‌شود و وقتی تگی شناسایی نشده باشد نمی‌توانید توسط جاوا اسکریپت روی آن تغییرات بزنید.مگر اینکه در رویداد لود کامل صفحه عملیات را قرار دهید
* debugger: هرگاه به آن خط برسد متوقف می‌شود و در inspector در تب دیباگر می‌توان وضعیت را رصد کرد

# 🅰️ AddElements

```html
<!DOCTYPE html>
<html lang="en">
<body>
<div id="div1">
    <p id="p1">element1</p>
    <p id="p2">element2</p>
</div>
</body>

<script>
    var elem_div = document.getElementById("div1");
    var newElem_p = document.createElement("p");
    var elem_p1 = document.getElementById("p1");
    var elem_p2 = document.getElementById("p2");

    var text = document.createTextNode("NewText");
    newElem_p.appendChild(text);
    elem_div.appendChild(newElem_p);
    elem_div.insertBefore(newElem_p, elem_p2);
    elem_div.removeChild(elem_p2);
    elem_div.replaceChild(newElem_p, elem_p1);
</script>
</html>
```

# 🅰️ Prompt|alert|alarm

```html
<!DOCTYPE html>
<html lang="en">
<body>

<button onclick="myfunc()">click me</button>
<p id="demo"></p>

</body>
<script>
    function myfunc() {
        if (confirm("لطفا انتخاب کنین که آیا می‌خواهید مقدار وارد نمایید یا خیر؟")) {
            var value = prompt("لطفا عدد خود را وارد نمایید", "عدد پیش‌فرض را ۲۰ درنظر می‌توان گرفت");
            document.getElementById("demo").innerHTML = value;
            alert(value);
        }
    }
</script>

</html>
```

# 🅰️ Events

## 🅱️ addEventListener

هنگام رخ دادن یک رویداد خاص (مثل کلیک، حرکت ماوس، فشردن کلید و غیره)، یک تابع مشخص اجرا شود

* element: المان «اج‌تی‌ام‌ال» که می‌خواهید رویداد به آن متصل کنید (مثل یک دکمه، لینک یا صفحه)\
* event(click,mouseover,keydown,...): نوع رویدادی که می‌خواهید گوش دهید\
* func: تابعی که هنگام رخ دادن رویداد اجرا می‌شود.

```javascript
var element = document.getElementById("btn");
element.addEventListener("click", func);

function func() {
    Code;
}   
```

</div>

## 🅱️ MouseEvents

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body onload="loadbody()">

<div onmouseover="mouseOver(this)"
     onmouseout="mouseOut(this)"
     onmousedown="mouseDown(this)"
     onmouseup="mouseUp(this)"
     style="width: 120px; height: 20px; background-color: purple; color: black;
    padding: 40px;"> javascript
</div>


</body>

<script>
    function mouseDown(om1) {
        om1.innerHTML = "onMouseDown";
        om1.style.backgroundColor = "red";
    }

    function mouseOver(om1) {
        om1.innerHTML = "onMouseOver";
        om1.style.backgroundColor = "green";
    }

    function mouseUp(om2) {
        om2.innerHTML = "onMouseUp";
        om2.style.backgroundColor = "blue";
    }

    function mouseOut(om2) {
        om2.innerHTML = "onMouseOut";
        om2.style.backgroundColor = "yellow";
    }

</script>

</html>
```





