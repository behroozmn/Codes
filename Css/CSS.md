### margin

```
margin: 2rem auto; #وسط چین می‌کند

```

### box

```
box-shadow: 0 2px 8px rgba(0,0,0,.3)
```

### font

```
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,700;1,900&display=swap');

html {
    font-family: 'Roboto', sans-serif;
}
```

### border

اگر بخواهیم که گزینه آخر بوردر نداشته باشد

```css
li:last-child {
    border-bottom: none
}  
```

### link[a]

با نگه داشتن روی لینک زیر آن خط نیافتد

```
text-decoration: none
```

با انیمیشن رفتار انجام شود

```
li a {
    transition: all ease .3s;
}
li a:hover, /* موس روی لینک برود*/ /*همچنین ویرگول ب معنی یا هست*/
li a:active { /*  موس روی لینک  کلیک کند یا کلیک را نگه دارد و مثلا دِرَگ نماید*/
    color: #006b1b;
}
```

### display

```
header nav {
    display: flex; /*مهم و باید خوانده شود*/
}
```

### اجباری نمودن یک تنظیمات

```
.errorlist {
    padding-right: 0 !important;
}
```