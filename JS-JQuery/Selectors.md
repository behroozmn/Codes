برای اینکه یک پارامتر را برای اعمال تغییرات انتخاب کنیم

# 1.ID Selector

  ```jquery
  $(document).ready(function () {
      $("#Button_1").click(function () { 
         $("#IdSelector").fadeOut(3000); // توسط شارپ و نام آی دی آن تگ مربوطه
      });
  });
  ``` 

# 2.Class Selector

  ```jquery
  $(document).ready(function () {
      $("#Button_2").click(function () { 
         $(".ClassName").fadeOut(3000); // توسط نقطه و نام کلاس مربوطه
      });
  });
  ```

# 3.All Elements Selector

  ```jquery
  $(document).ready(function () {
      $("#Button_3").click(function () {
         $("*").fadeOut(3000);
      });
  });
  ```

# 4.Attribute Selector

## 4.1.Contains Selector[Key*=Value]

* اجرای عملیات روی هر تگ که نام آن مشخص شده باشد و مقدار آن نیز شامل محتوی مشخص شده باشد
* مقدار مورد نظر باید مشمول بشود و مهم نیست کجای مقدار خصیصه باشد

```html

<div class="well" TestName="TestValue Hello">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_4">
            Attribute Contains Selector
        </a>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_4").click(function () { 
    $("[TestName*='TestValue']").fadeOut(3000);
});
```

## 4.2.Contains Word Selector[Key~=Value]

* اجرای عملیات روی هر تگ که نام آن مشخص شده باشد و مقدار آن نیز شامل محتوی مشخص شده بعنوان یک کلمه مستقل باشد
* اگر کلمه به هم شامل عبارت به هم چسبیده باشد قبول نیست و باید با خط فاصله از هم جدا شود تا تبدیل به یک کلمه مستقل شود

```html

<div class="well" TestName="TestValue Hello">
    <div class="well" WordName="WordValue Test">
        <div class="col-md-3 pull-left">
            <a class="btn btn-warning btn-block" id="Button_5">
                Attribute Contains Word Selector
            </a>
        </div>
    </div>
</div>
</div>
```

```jquery
$("#Button_5").click(function () { 
    $("[WordName~='WordValue']").fadeOut(3000);
});
```

## 4.3.Ends With Selector[Key$=Value]

* مقدار محتوی خصیصه به چه چیزی ختم شود

```html

<div class="well" EndWith="Hello Mohammad">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_6">
            Attribute Ends With Selector
        </a>
    </div>
```

```jquery
$("#Button_6").click(function () { 
    $("[EndWith$='ad']").fadeOut(3000);
});
```

## 4.4.Equal Selector[Key=Value]

* مقدار محتوی خصیصه دقیقا برابر چه مقداری شود

```html

<div class="well" Equal="Hello">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_7">
            Attribute Equal Selector
        </a>
    </div>
</div>
```

```jquery
$("#Button_7").click(function () { 
    $("[Equal='Hello']").fadeOut(3000);
});
```

## 4.5.Start With Selector[Key^=Value]

* مقدار محتوی خصیصه دقیقا با چه مقداری شروع شود

```html

<div class="well" StartWith="Hello Mohammad">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_8">
            Attribute Start With Selector
        </a>
    </div>
</div>
```

```jquery
$("#Button_8").click(function () { 
    $("[StartWith^='He']").fadeOut(3000);
});
```

