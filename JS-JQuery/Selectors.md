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

## 5.3.Disable[:disabled]

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

## 5.4.enable[:enabled]

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

## 5.5.Empty[:empty]

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

## 5.6.Index Selector[:eq(X)]

* ایندکس ها از صفر شروع می‌شود
* انتخاب یک المنت بر اساس ترتیب ایندکس استفاده شدن آن

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_17">
            eq() => index Selector
        </a>
    </div>
    <div class="col-md-9" id="indexSelector">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>

    <div class="clearfix"></div>
</div>

```

```jquery
$("#Button_17").click(function () { 
    $("#indexSelector p:eq(2)").fadeOut(500);
});
```

## 5.7.even Selector[:even]

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_18">
            even Selector
        </a>
    </div>
    <div class="col-md-9" id="evenSelector">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>

    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_18").click(function () { 
    $("#evenSelector p:even").fadeOut(500);
});
```

## 5.8.file Selector[:file]

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_19">
            file Selector
        </a>
    </div>
    <div class="col-md-9" id="fileSelector">
        <input type="file" value="file Selector">
    </div>

    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_19").click(function () { 
    $("#fileSelector :file").fadeOut(500);
});
```

## 5.9.first-child[:first-child]

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_20">
            first-child Selector
        </a>
    </div>
    <div class="col-md-9" id="childSelector">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>

    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_20").click(function () { 
    $("#childSelector p:first-child").fadeOut(500);
});
```

## 5.10.first-of-type[:first-of-type]

* اولین تک معرفی شده از هر والد که میتواند مثلا دوتا دایو باشد که اولین از هرکدام از دایو را حذف نماید

```html

<div class="well" id="firstTypeSelector">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_21">
            first-of-Type Selector
        </a>
    </div>
    <div class="col-md-9">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>
    <div class="col-md-9">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>

    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_21").click(function () { 
    $("#childSelector p:first-of-type").fadeOut(500);
});
```

## 5.11.first[:first]

* اولین المنت رو در نظر میگیرد
* اگر چیزی انتحاب نشود اولین المنت صفحه را در نظر میگیرد

```html

<div class="well" id="firstSelector">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_22">
            first Selector
        </a>
    </div>
    <div class="col-md-9">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>
    <div class="col-md-9">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>

    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_22").click(function () { 
    $("#firstSelector p:first").fadeOut(500);
});
```

## 5.12.greaterthanSelector[::gt(X)]

* ایندکس شماره خاص به بعد همه را انتخاب کن

```html

<div class="well" id="greaterthanSelector">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_23">
            greater than Selector
        </a>
    </div>
    <div class="col-md-9">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>
    <div class="clearfix"></div>
</div>
</div>
```

```jquery
    $("#Button_23").click(function () { 
        $("#greaterthanSelector p:gt(2)").fadeOut(500);
    });
```

## 5.13.Has[:Has(<TAGNAME>)]

* اگر المانی وجود داشته باشد آن را اتخاب می‌کند
* بیشتر برای تگ استفاده می‌شود

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_25">
            :has() Selector
        </a>
    </div>
    <div class="col-md-9">
        <div class="MyClass">
            <p>
                Hello in a paragraph
            </p>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_25").click(function () { 
    $("div.MyClass:has(p)").fadeOut(500);
});
```

## 5.14.last-child[:last-child]

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_26">
            last child Selector
        </a>
    </div>
    <div class="col-md-9" id="LastChild">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_26").click(function () { 
    $("#LastChild p:last-child").fadeOut(500);
});
```

## 5.15.last-of-type[:last-of-type]

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_27">
            last of type Selector
        </a>
    </div>
    <div class="col-md-9" id="LastOfType">
        <div>
            <p>0</p>
            <p>1</p>
            <p>2</p>
            <p>3</p>
            <p>4</p>
        </div>
        <div>
            <p>0</p>
            <p>1</p>
            <p>2</p>
            <p>3</p>
            <p>4</p>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_27").click(function () { 
    $("#LastOfType p:last-of-type").fadeOut(500);
});
```

## 5.16.last[:last]

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_28">
            last Selector
        </a>
    </div>
    <div class="col-md-9" id="LastSelector">
        <div>
            <p>0</p>
            <p>1</p>
            <p>2</p>
            <p>3</p>
            <p>4</p>
        </div>
        <div>
            <p>0</p>
            <p>1</p>
            <p>2</p>
            <p>3</p>
            <p>4</p>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_28").click(function () { 
    $("#LastSelector p:last").fadeOut(500);
});
```

## 5.17.lessThanSelector[:lt(X)]

* انتخاب المان‌های با ایندکس کمتر از یک عدد خاص

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_29">
            :ls() => Less Than Selector
        </a>
    </div>
    <div class="col-md-9" id="LessThan">
        <p>0</p>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
        <p>5</p>
        <p>6</p>
        <p>7</p>
        <p>8</p>
        <p>9</p>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_29").click(function () { 
    $("#LessThan p:lt(4)").fadeOut(500);// میتوان عدد منفی نیز بپذیرد
});
```

## 5.18.not[:not]

* حاوی ویژگی نباشد

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_34">
            :not() Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="NotSelector">
            <div>
                <input type="checkbox" name="a">
                <span>ایمان</span>
            </div>
            <div>
                <input type="checkbox" name="b">
                <span>محمد</span>
            </div>
            <div>
                <input type="checkbox" name="c" checked="checked">
                <span>سهیل</span>
            </div>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_34").click(function () { 
    $("input:not(:checked) , input:not(:checked) + span").fadeOut(500);
});
```

## 5.19.nth_child[:nth_child(X)]

* Not ZeroBase
* از عدد یک شروع می‌شود
* در والدهای یکسان فرزند شماره خاص را انتخاب نماید

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_35">
            :nth-child() Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="MyChild">
            <div>
                <ul>
                    <li>محمد</li>
                    <li>میلاد</li>
                    <li>علی</li>
                </ul>
            </div>
            <div>
                <ul>
                    <li>سبحان</li>
                    <li>مرتضی</li>
                </ul>
            </div>
            <div>
                <ul>
                    <li>الناز</li>
                    <li>سارا</li>
                    <li>سمیه</li>
                    <li>فائزه</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_35").click(function () { 
    $("#MyChild ul li:nth-child(3n)").fadeOut(500); // nth-child(even) یا  nth-child(2)
});
```

## 5.20.nth-last-child[:nth-last-child(X)]

* Not ZeroBase
* از عدد یک شروع می‌شود
* در والدهای یکسان فرزند شماره خاص را انتخاب نماید با این تفاوت که از آخر شروع به اجرا می‌نماید و نه از ابتدا

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_36">
            :nth-last-child() Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="ID">
            <div>
                <ul>
                    <li>محمد</li>
                    <li>میلاد</li>
                    <li>علی</li>
                    <li>رضا</li>
                    <li>عباس</li>
                    <li>سمیرا</li>
                </ul>
            </div>
            <div>
                <ul>
                    <li>سبحان</li>
                    <li>مرتضی</li>
                </ul>
            </div>
            <div>
                <ul>
                    <li>الناز</li>
                    <li>سارا</li>
                    <li>سمیه</li>
                    <li>فائزه</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_36").click(function () { 
    $("#ID ul li:nth-last-child(2)").fadeOut(500); // nth-last-child(even) یا  nth-last-child(2n)
});
```

## 5.21.nth_Of_Type[:nth_Of_Type(X)]

* وقتی چند والد(مثلا دیو) داریم آنگاه اگر بخواهیم از بین تگ‌های متفاوت داخل دیو، دومین پی را انتخاب کنیم که در تمام والد ها دومین فرزند انتخاب شود

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_37">
            :nth-of-type() Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="ID">
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
            <hr>
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
            <hr>
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_37").click(function () { 
    $("#ID div p:nth-of-type(2)").fadeOut(500);
});
```

## 5.22.nth-last-of-type[:nth-last-of-type]

* وقتی چند والد(مثلا دیو) داریم آنگاه اگر بخواهیم از بین تگ‌های متفاوت داخل دیو، دومین پی را انتخاب کنیم که در تمام والد ها دومین فرزند انتخاب شود با این تفاوت که از آخر انتخاب و شمارش میکند ونه از اول

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_38">
            :nth-last-of-type() Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="ID">
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
            <hr>
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
            <hr>
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_38").click(function () { 
    $("#ID div p:nth-last-of-type(2)").fadeOut(500);
});
```

## 5.23.only-child[:only-child]

* فقط انتخاب تک فرزند ها

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_39">
            :only-child Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="ID">
            <div>
                <ul>
                    <li>محمد</li>
                    <li>میلاد</li>
                    <li>علی</li>
                </ul>
            </div>
            <hr>
            <div>
                <ul>
                    <li>سبحان</li>
                </ul>
            </div>
            <hr>
            <div>
                <ul>
                    <li>سبحان</li>
                </ul>
            </div>
            <hr>
            <div>
                <ul>
                    <li>سبحان</li>
                    <li>مرتضی</li>
                </ul>
            </div>
            <hr>
            <div>
                <ul>
                    <li>الناز</li>
                    <li>سارا</li>
                    <li>سمیه</li>
                    <li>فائزه</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_39").click(function () { 
    $("#ID li:only-child").fadeOut(500);
});
```

## 5.24.only-of-type[:only-of-type]

* در انواع مختلف هرکدام که تنهای کی از آن ها در دایره والد موجود است را انتخاب کن

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_40">
            :only-of-type Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="ID">
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <b>bold 2</b>
                <span>span</span>
            </div>
            <hr>
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
            <hr>
            <div>
                <p>paragraph</p>
                <span>test</span>
                <p>paragraph</p>
                <b>bold</b>
                <span>span</span>
            </div>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_40").click(function () { 
    $("#ID b:only-of-type").fadeOut(500);
});
```

## 5.25.parent[:parent]

* تگ‌هایی که حدافل یک فرزند داشته باشد یا اینکه بعنوان والد شناخته شده باشد

```html

<style>
    td {
        width: 40px;
        height: 40px;
        background: green;
    }
</style>

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_41">
            :parent Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="ID">
            <table border="1">
                <tr>
                    <td>mohammad</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Ali</td>
                    <td></td>
                </tr>
            </table>
        </div>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_41").click(function () { 
    $("#ID td:parent").fadeOut(500);
});
```


# 6.Has Attribute

* المان‌هایی که دارای یک خصیصه با کلید تعیین شده باشند را انتخاب نماید

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_24">
            Has Attribute Selector
        </a>
    </div>
    <div class="col-md-9">
        <div class="alert alert-warning" HasAttribute="HasAttribute">test</div>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_24").click(function () { 
    $("div[HasAttribute]").fadeOut(500);
});
```

# 7.Multiple Attribute Selector

* اگر همزمان از چند خصیصه با نام کلیدواژه خاص استفاده میکرد

```html
div class="well">
<div class="col-md-3 pull-left">
    <a class="btn btn-warning btn-block" id="Button_30">
        multiple Attribute Selector
    </a>
</div>
<div class="col-md-9">
    <div class="MultipleAttribute" multipleAttribute="Test">
        <p>
            Hello in a paragraph
        </p>
    </div>
</div>
<div class="clearfix"></div>
</div>
```

```jquery
$("#Button_30").click(function () { 
    $("div[class][multipleAttribute*='Te']").fadeOut(500); //اگر از کلاس و از مالتیپل‌آتریبیوت استفاده میکرد که شامل عبارت خاص بود
    //
});
```

# 8.Multiple Selector

* انتخاب چند المان بصورت همزمان

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_31">
            multiple Selector
        </a>
    </div>
    <div class="col-md-9">
        <div class="MultipleSelector">
            division with class
        </div>

        <p id="MultipleSelector">
            paragraph with id
        </p>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_31").click(function () { 
    $("div.MultipleSelector , #MultipleSelector").fadeOut(500);
});
```

# 9.Next Adjacent Selector یا NextTag

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_32">
            next adjacent Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="NextAdjacent">
            main selector
        </div>
        <div>
            division with class
        </div>
        <p>
            paragraph with id
        </p>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_32").click(function () { 
    $("#NextAdjacent + div + p").fadeOut(500); //آی دی رو دیدی برو بعد تگ دایو تگ پی رو انتخاب کن
});
```

# 10.Next Siblings Selector

* بعد از یک تگ خاص همه موارد را انتخاب کن

```html

<div class="well">
    <div class="col-md-3 pull-left">
        <a class="btn btn-warning btn-block" id="Button_33">
            next siblings Selector
        </a>
    </div>
    <div class="col-md-9">
        <div id="NextSiblings"></div>
        <div>
            division with class
        </div>
        <p>
            paragraph with id
        </p>
        <p>
            paragraph with id
        </p>
        <p>
            paragraph with id
        </p>
        <p>
            paragraph with id
        </p>
    </div>
    <div class="clearfix"></div>
</div>
```

```jquery
$("#Button_33").click(function () { 
    $("#NextSiblings ~ p").fadeOut(500); //همه تگ های بعد از آی دی را انتخاب کن
});
```

```html

```

```jquery

```