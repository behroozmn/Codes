# time

## setInterval

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

## [fadeIn]|[fadeout]

* مرئی و نامرئی شدن یک مولفه از صفحه

```jquery
$("#Button_3").hover(function () {
    $("#ID").fadeOut();
}, function () {
    $("#ID").fadeIn();
});
```

```jquery
$("#Button_3").mouseenter(function () {
    $("#ID").fadeOut();
});

$("#Button_3").mouseleave(function () {
    $("#ID").fadeIn();
});
```

