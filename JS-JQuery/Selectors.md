برای اینکه یک پارامتر را برای اعمال تغییرات انتخاب کنیم

# 1.ID Selector

  ```jquery
  $(document).ready(function () {
      $("#Button_1").click(function () { 
         $("#IdSelector").fadeOut(3000); // توسط شارپ و نام آی دی آن تگ مربوطه
      });
  });
  ``` 

## 1.1.ParentChile[>]

* با انتخاب والد به سراغ انتخاب فرزند می‌رویم و تگهای مورد نظر را انتخاب می‌کنیم
* آی دی را پیدا میکند و یک لایه زیر نگاه میکند و هرچی تگ باشد آن را مد نظر قرار میگیرد
* هر چند تعداد لایه زیرین دارای تگ باشد آن را مد نظر قرار **نخواهد** داد
* در مثال زیر تگ تست مورد انتخاب واقع نمی‌شود

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_11">
            Parent > Child Selector
        </a>
    </div>
    <div class="col-md-9" id="Parent">
        <p class="test">1</p>
        <p>2</p>
        <p class="test">3</p>
        <p>4</p>
        <p class="test">5</p>
        <div>
            <p>test</p>
        </div>
    </div>
    <div class="clearfix"></div>
</div
```

```jquery
$("#Button_11").click(function () { 
    $("#Parent > p.test").fadeOut(500);
});
```

## 1.2.Descendent[space]

* با انتخاب والد به سراغ انتخاب فرزند می‌رویم و تگهای مورد نظر را انتخاب می‌کنیم
* هر چند تعداد لایه زیرین دارای تگ باشد آن را مد نظر قرار میدهد

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_13">
            Descendant Selector
        </a>
    </div>
    <div class="col-md-9" id="descendantId">
        <p>1</p>
        <p>2</p>
        <div>
            <p>test</p>
        </div>
        <p>3</p>
        <p>4</p>
        <p>5</p>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_13").click(function () { 
    $("#descendantId p").fadeOut(500);
});
```

## 1.3.contain

* ملاک محتوی مقدار تگ است و نه خصیصه

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_12">
            Contains Selector
        </a>
    </div>
    <div class="col-md-9" id="ID">
        test
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_12").click(function () { 
    $("#ID:contains('test')").fadeOut(500);
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

## 4.1.Contains[Key*=Value]

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

## 4.2.ContainsWord[Key~=Value]

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

## 4.3.EndsWith[Key$=Value]

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

## 4.4.Equal[Key=Value]

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

## 4.5.StartWith[Key^=Value]

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

# 5.Type Selector

## 5.1.Button[":button"]

* هر تگ که نوع آن از نوع دکمه باشد

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_9">
            Button Selector
        </a>
    </div>
    <div class="col-md-9">
        <input type="button" value="input button">

        <button> button</button>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_9").click(function () { 
    $(":button").fadeOut(3000);
});
```

## 5.2.checkbox[":checkbox"]

* هر تگ که نوع آن از نوع دکمه باشد

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_10">
            checkbox Selector
        </a>
    </div>
    <div class="col-md-9">
        <input type="checkbox">checkbox

    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_10").click(function () { 
    $(":checkbox").fadeOut(500);
});
```

## 5.3.Disable

* انخاب موارد غیر فعال شده

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_14">
            disabled Selector
        </a>
    </div>
    <div class="col-md-9">
        <input type="button" disabled value="disabled">
        <input type="button" value="notdisabled">
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_14").click(function () { 
    $("input:disabled").fadeOut(500);
});
```

## 5.4.enable

* انخاب موارد فعال

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_15">
            enabled Selector
        </a>
    </div>
    <div class="col-md-9">
        <input type="button" value="enabled">
        <input type="button" disabled value="notenabled">
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_15").click(function () { 
    $("input:enabled").fadeOut(500);
});
```

## 5.5.Empty

* انخاب موارد خالی

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_16">
            empty Selector
        </a>
    </div>
    <div class="col-md-9 alert alert-warning"></div>

    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_16").click(function () { 
    $("div:empty").fadeOut(500);
});
```