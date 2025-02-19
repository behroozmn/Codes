هنگام رخ دادن یک رویداد خاص (مثل کلیک، حرکت ماوس، فشردن کلید و غیره)، یک تابع مشخص اجرا شود

> * element:  المان «اج‌تی‌ام‌ال» که می‌خواهید رویداد به آن متصل کنید (مثل یک دکمه، لینک یا صفحه)\
> * event(click,mouseover,keydown,...): نوع رویدادی که می‌خواهید گوش دهید\
> * func:  تابعی که هنگام رخ دادن رویداد اجرا می‌شود.

```javascript
var element = document.getElementById("btn");
element.addEventListener("click", func);

function func() {
    Code;
}   
```
