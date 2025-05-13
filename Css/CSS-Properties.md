# 1.Shorthand

* به شما اجازه می دهد مقادیر متعدد خاص CSS را همزمان تنظیم کنید
* می توانید برگه های سبک مختصر تر ، صرفه جویی در وقت و انرژی را بنویسید
* شامل موارد زیر می‌شود
    * all
    * animation
    * animation-range
    * background
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
    * view-timeline
    * -webkit-text-stroke
    * -webkit-border-before
    * -webkit-mask-box-image

## border-*

### border-bottom

```css
li:last-child {
    border-bottom: none; /* اگر بخواهیم که گزینه آخر بوردر نداشته باشد*/
}  
```

## margin-*

### margin

```css
p {
    margin: 2rem auto; /*وسط چین می‌کند*/
}
```

## text-*

### text-decoration

* مورد none: سبب می‌شود که با نگه داشتن روی لینک زیر آن لینک خط نیافتد

```css
p {
    text-decoration: none;
}
```

## transition-*

### transition[[url]](https://developer.mozilla.org/en-US/docs/Web/CSS/transition)

```css
li a {
    transition: all ease .3s; /*با انیمیشن رفتار انجام شود*/
}

li a:hover, /* موس روی لینک برود*/ /*همچنین ویرگول ب معنی یا هست*/
li a:active { /*  موس روی لینک  کلیک کند یا کلیک را نگه دارد و مثلا دِرَگ نماید*/
    color: #006b1b;
}
```

```css
li a {
    transition: margin-right 2s;
    transition: margin-right 2s 0.5s;
    transition: margin-right 2s ease-in-out;
    transition: margin-right 2s ease-in-out 0.5s;
    transition: margin-right 2s, color 1s;
    transition: all 1s ease-out;
}
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

## font-*

### font-family

```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,700;1,900&display=swap');

html {
    font-family: 'Roboto', sans-serif;
}
```

```css
p {
    font-family: "Gill Sans", sans-serif;
    /* OR */
    font-family: "Gill Sans Extrabold", sans-serif;
}
```

## box-*

### box-shadow[[url]](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow)

```css
p {
    box-shadow: none;
    box-shadow: 0 2px 8px rgba(0, 0, 0, .3);
    box-shadow: 10px 5px 5px red;
    box-shadow: 60px -16px teal;
    box-shadow: 12px 12px 2px 1px rgba(0, 0, 255, 0.2);
    box-shadow: inset 5em 1em gold;
    box-shadow: 3px 3px red, -1em 0 0.4em olive;
}
```

