با خوشحالی و دقت کامل، متن شما رو بر اساس درخواستت گسترش می‌دم. تمام مواردی که نوشتی **حذف نمی‌شه** و به همراه توضیحات بیشتر، مثال‌های عملی‌تر و نکات کاربردی جاوااسکریپت/جی‌کوئری، آنها را گسترش داده و ساختاردهی می‌کنم.

---

## 📝 فصل: دستکاری DOM با jQuery (Manipulation)

در «جی‌کوئری»، قسمت **Manipulation** به معنای تغییر یا دستکاری المان‌های HTML در **DOM** است.  
این یکی از قدرتمندترین و پرکاربردترین بخش‌های jQuery است که امکان **افزودن، حذف، تغییر و مدیریت** محتوا و ساختار المان‌ها را به صورت بسیار ساده و دقیق فراهم می‌کند.

---

### 🔧 1. افزودن المان‌ها (Add Elements)

#### `.append()`

اضافه کردن محتوا **به انتهای** یک المان

```js
$('#myDiv').append('<p>پاراگراف جدید</p>');
```

#### `.prepend()`

اضافه کردن محتوا **به ابتدای** یک المان

```js
$('#myList').prepend('<li>آیتم ۱</li>');
```

#### `.before()`

اضافه کردن محتوا **قبل از** المان

```js
$('#myList').before('<h2>لیست من</h2>');
```

#### `.after()`

اضافه کردن محتوا **بعد از** المان

```js
$('#myList').after('<p>این لیست است</p>');
```

---

### ❌ 2. حذف المان‌ها (Remove Elements)

#### `.remove()`

حذف کامل یک المان از DOM

```js
$('#oldElement').remove();
```

#### `.empty()`

حذف فقط محتوای داخلی یک المان (ولی خود المان را نگه می‌دارد)

```js
$('#container').empty(); // فقط فرزندان حذف می‌شوند
```

---

### 🖋️ تغییر محتوا (Content Manipulation)

#### `.html()`

محتوای HTML یک المان را تنظیم یا برمی‌گرداند. **فقط اولین المان** را در نظر می‌گیرد.

```js
$('#title').html('<strong>عنوان جدید</strong>');
```

#### `.text()`

تمام محتوای متنی المان‌های انتخابی را بدون HTML ترکیب کرده و برمی‌گرداند.

```js
$('#description').text('این یک توضیح است.');
```

---

### ⚙️ دستکاری ویژگی‌ها (Attributes)

#### `.attr()`

تنظیم یا خواندن ویژگی‌های HTML مثل `src`, `href`, `class` و غیره.

```js
$('img').attr('src', 'new-image.jpg');
```

#### `.removeAttr()`

حذف یک ویژگی از المان

```js
$('a').removeAttr('target');
```

#### `.prop()`

استفاده برای خاصیت‌های DOM مثل `checked`, `disabled`, `selected`.

```js
$('input').prop('disabled', true);
```

> 💡 نکته: `.prop()` برای خاصیت‌های منطقی (Boolean) مثل `checked` مناسب‌تر از `.attr()` است.

---

### 🎨 دستکاری کلاس‌ها (Class Manipulation)

#### `.addClass()`

اضافه کردن یک یا چند کلاس به المان(ها)

```js
$('div').addClass('highlight');
$('#myList li').addClass('active');
```

مثال با استفاده از callback:

```js
$("#IDBtn").click(function () {
    $("#IdDiv p").addClass(function (index, currentClass) {
        return index === 0 ? "first" : "other";
    });
});
```

#### `.removeClass()`

حذف یک یا چند کلاس از المان(ها)

```js
$('.highlight').removeClass('highlight');
```

مثال با شرط:

```js
$("#IDBtn").click(function () {
    $("#IdDiv p").removeClass(function (index, currentClass) {
        if (currentClass.includes("test")) {
            return "test";
        }
    });
});
```

#### `.toggleClass()`

تعویض (فعال/غیرفعال کردن) یک یا چند کلاس به صورت خودکار

- اگر کلاس وجود داشت → حذف می‌کند
- اگر کلاس نبود → اضافه می‌کند

##### ✅ مثال 1: سوییچ کردن یک کلاس (مانند تم تاریک)

```html

<button id="toggleBtn">فعال/غیرفعال کردن تم تاریک</button>
<div id="box" style="width: 200px; height: 200px; background: #eee;"></div>

<style>
    .dark-mode {
        background: #333;
        color: white;
    }
</style>

<script>
    $('#toggleBtn').click(function () {
        $('#box').toggleClass('dark-mode');
    });
</script>
```

##### ✅ مثال 2: تغییر چند کلاس با هم

```js
$('#myElement').toggleClass('class1 class2 class3');
```

##### ✅ مثال 3: تغییر کلاس با شرط

```js
let isHighlighted = true;
$('#myElement').toggleClass('highlighted', isHighlighted); // اگر true باشد، اضافه می‌کند
```

#### `.hasClass()`

بررسی وجود یک کلاس در المان — خروجی `true` یا `false`

```js
if ($('#myDiv').hasClass('active')) {
    console.log('این المان فعال است');
}
```

مثال پیشرفته:

```js
$("#IDBtn").click(function () {
    $("#IdDiv p").each(function () {
        if ($(this).hasClass("MyCssClass")) {
            $(this).removeClass("MyCssClass");
        } else {
            $(this).addClass("MyCssClass");
        }
    });
});
```

---

### 🎨 دستکاری CSS (Style Manipulation)

#### `.css()`

تنظیم یا خواندن خاصیت‌های CSS یک المان

```js
$('#box').css('color', 'red');
```

تنظیم چند خاصیت با یک شیء:

```js
$('#box').css({
    'background-color': 'yellow',
    'font-size': '20px'
});
```

---

### 🧩 نکات کاربردی بیشتر

| مورد                   | توضیح                                                                                                                                                                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Performance Tip**    | وقتی می‌تونی از `class` به جای مستقیم نوشتن `css()` استفاده کنی، بهتر است. زیرا تغییر دادن کلاس‌ها کارآمدتر است.                                                              |
| **Chaining**           | تمام این متدها اجازه می‌دهند دستورات را زنجیره‌ای بنویسیم: `$('div').addClass('x').css('color','red')`                                                                        |
| **Callback Functions** | برخی متدها مثل `addClass()`, `removeClass()` و `toggleClass()` از callback پشتیبانی می‌کنند که به شما اجازه می‌دهد بر اساس موقعیت یا وضعیت المان، عملیات داینامیک انجام دهید. |

---

### 📁 خلاصه دستورات

| دستور            | عملکرد                                       |
|------------------|----------------------------------------------|
| `.append()`      | اضافه کردن محتوا به انتهای المان             |
| `.prepend()`     | اضافه کردن محتوا به ابتدای المان             |
| `.before()`      | اضافه کردن قبل از المان                      |
| `.after()`       | اضافه کردن بعد از المان                      |
| `.remove()`      | حذف کامل المان                               |
| `.empty()`       | پاک کردن محتوای المان                        |
| `.html()`        | تنظیم یا گرفتن محتوای HTML (فقط اولین المان) |
| `.text()`        | تنظیم یا گرفتن محتوای متنی (بدون HTML)       |
| `.attr()`        | خواندن/تنظیم ویژگی HTML                      |
| `.removeAttr()`  | حذف یک ویژگی                                 |
| `.prop()`        | خواندن/تنظیم خاصیت DOM                       |
| `.addClass()`    | اضافه کردن کلاس                              |
| `.removeClass()` | حذف کلاس                                     |
| `.toggleClass()` | تعویض (اضافه/حذف) کلاس                       |
| `.hasClass()`    | چک کردن وجود کلاس                            |
| `.css()`         | خواندن/تنظیم خاصیت CSS                       |

---

اگر خواستی این محتوا رو به صورت **فایل HTML کامل با مثال‌های تعاملی** داشته باشی، فقط بگو! 😊