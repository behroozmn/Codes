# 1.Shorthand

* به شما اجازه می دهد مقادیر متعدد خاص CSS را همزمان تنظیم کنید
* می توانید برگه های سبک مختصر تر ، صرفه جویی در وقت و انرژی را بنویسید
* شامل موارد زیر می‌شود
    * all
    * animation
    * animation-range
    * background
    * border
    * border-block
    * border-block-end
    * border-block-start
    * border-bottom
    * border-color
    * border-image
    * border-inline
    * border-inline-end
    * border-inline-start
    * border-left
    * border-radius
    * border-right
    * border-style
    * border-top
    * border-width
    * column-rule
    * columns
    * contain-intrinsic-size
    * container
    * flex
    * flex-flow
    * font
    * font-synthesis
    * font-variant
    * gap
    * grid
    * grid-area
    * grid-column
    * grid-row
    * grid-template
    * inset
    * inset-block
    * inset-inline
    * list-style
    * margin
    * margin-block
    * margin-inline
    * mask
    * mask-border
    * offset
    * outline
    * overflow
    * overscroll-behavior
    * padding
    * padding-block
    * padding-inline
    * place-content
    * place-items
    * place-self
    * position-try
    * scroll-margin
    * scroll-margin-block
    * scroll-margin-inline
    * scroll-padding
    * scroll-padding-block
    * scroll-padding-inline
    * scroll-timeline
    * text-box
    * text-emphasis
    * text-wrap
    * transition
    * view-timeline
    * -webkit-text-stroke
    * -webkit-border-before
    * -webkit-mask-box-image

## text-*

### text-decoration

* مورد none: سبب می‌شود که با نگه داشتن روی لینک زیر آن لینک خط نیافتد

```
text-decoration: none;
```

# 2.general

## display

[//]: # (TODO باید بعدا بخواهنم)

```css
header nav {
    display: flex;
}
```

### flex

> در حالت عادی دو اِلِمان ۱-تصویر ۲-محتوی(عنوان و متن) زیر هم قرار می‌گیرند

```html

<body>
<article class="post">
    <ul>
        <li>
            <a href="">
                <img src="bg.png" alt="">
                <div class="post__content">
                    <h3>Learning Django</h3>
                    <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Distinctio, dolore dolores
                        ipsam itaque labore laudantium quo rem similique soluta voluptate?
                    </p>
                </div>
            </a>
        </li>
    </ul>
</article>
</body>
</html>

```

* توسط قطعه‌کد زیر دو اِلِمان کنار هم قرار خواهند گرفت

```css
.post a {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```

## list-*

### list-style-type

```css
ul {
    list-style-type: none; /* حذف دایره‌های کنار یک بولت */
}
```

