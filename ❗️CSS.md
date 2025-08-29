<div dir="rtl">

# 1. 🅰️ مفاهیم و نکات

<div style="display: flex; flex-direction: column; align-items: center;">

![ruleset](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_syntax/Syntax/ruleset.png)
![_declaration](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_syntax/Syntax/css_syntax_-_declaration.png)
![](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_syntax/Syntax/css_syntax_-_statements_venn_diag.png)

</div>

# 2. 🅰️ Properties

## 2.1. 🅱️ Shorthand

* به شما اجازه می دهد مقادیر متعدد خاص CSS را همزمان تنظیم کنید
* می توانید برگه های سبک مختصر تر ، صرفه جویی در وقت و انرژی را بنویسید
* شامل موارد زیر می‌شود

```
all
animation
animation-range
background
border-block
border-block-end
border-block-start
border-bottom
border-color
border-image
border-inline
border-inline-end
border-inline-start
border-left
border-radius
border-right
border-style
border-top
border-width
column-rule
columns
contain-intrinsic-size
container
flex
flex-flow
font
font-synthesis
font-variant
gap
grid
grid-area
grid-column
grid-row
grid-template
inset
inset-block
inset-inline
list-style
margin-block
margin-inline
mask
mask-border
offset
outline
overflow
overscroll-behavior
padding
padding-block
padding-inline
place-content
place-items
place-self
position-try
scroll-margin
scroll-margin-block
scroll-margin-inline
scroll-padding
scroll-padding-block
scroll-padding-inline
scroll-timeline
text-box
text-emphasis
text-wrap
view-timeline
-webkit-text-stroke
-webkit-border-before
-webkit-mask-box-image
```

### 2.1.1. ✅️ border-*

#### 2.1.1.1. ❇️ border-bottom

```css
li:last-child {
    border-bottom: none; /* اگر بخواهیم که گزینه آخر بوردر نداشته باشد*/
}  
```

### 2.1.2. ✅️ margin-*

#### 2.1.2.1. ❇️ margin

```css
p {
    margin: 2rem auto; /*وسط چین می‌کند*/
}
```

### 2.1.3. ✅️ text-*

#### 2.1.3.1. ❇️ text-decoration

* مورد none: سبب می‌شود که با نگه داشتن روی لینک زیر آن لینک خط نیافتد

```css
p {
    text-decoration: none;
}
```

### 2.1.4. ✅️ transition-*

#### 2.1.4.1. ❇️ transition[[url]](https://developer.mozilla.org/en-US/docs/Web/CSS/transition)

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

## 2.2. 🅱️ general

### 2.2.1. ✅️ display

[//]: # (Todo: Need to Review)

```css
header nav {
    display: flex;
}
```

#### 2.2.1.1. ❇️ flex

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

### 2.2.2. ✅️ list-*

#### 2.2.2.1. ❇️ list-style-type

```css
ul {
    list-style-type: none; /* حذف دایره‌های کنار یک بولت */
}
```

### 2.2.3. ✅️ font-*

#### 2.2.3.1. ❇️ font-family

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

### 2.2.4. ✅️ box-*

#### 2.2.4.1. ❇️ box-shadow[[url]](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow)

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

# 3. 🅰️ Statement

## 3.1. 🅱️ RulesSets

* نوع Rulesets :مجموعه‌ای از declaration های CSS که توسط Selectorها تخصیص پیدا می‌کنند

## 3.2. 🅱️ At-rules

* نوع At-rules: مواردی که با علامت @ آغاز می‌شوند.

```
@charset
@color-profile
@container
@counter-style
@font-feature-values
@font-palette-values
@keyframes
@layer
@media
@namespace
@page
@position-try
@property
@scope
@starting-style
@supports
@view-transition

```

### 3.2.1. ✅️ @font-face

```CSS
@font-face {
    font-family: Behroooooooz;
    src: url('http://www.parsquran.com/data/fonts/UthmanTN.otf') format('opentype');
```

```html
font-family: Behroooooooz
```

```
TrueType                 font/ttf
OpenType                 font/otf
Web Open Font Format     font/woff
Web Open Font Format2    font/woff2
```

### 3.2.2. ✅️ @import

```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,700;1,900&display=swap');

html {
    font-family: 'Roboto', sans-serif;
}
```

# 4. 🅰️ اجباری نمودن یک خصلت برای یک اِلِمان

```css
selector {
    property: value; /* normal declaration */
    property: value !important; /* important declaration (preferred) */
    property: value ! important; /* important declaration (not preferred) */
}

```

## 4.1. 🅱️ Example1

```css
.errorlist {
    padding-right: 0 !important;
}
```

</div>