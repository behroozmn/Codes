# حالت اول

## حالت بدون ساختار:زیر هم قرار گرفتن تگ‌ها

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<article class="post">
    <ul>
        <li>
            <a href="">
                <img src="bg.png">
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
## اصلاحات
> در حالت عادی دو تگ ۱-تصویر ۲-متن(عنوان و متن) زیر هم قرار می‌گیرند درحالی که توسط قطعه کد زیر دو تگ کنار هم قرار خواهند گرفت

```css
.post a {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```

## حالت اصلاح شده:  حالت کنار هم قرار گرفتن

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<style>
    ul {
        list-style-type: none; /* حذف دایره‌ها */
    }

    .post a {
        display: flex;
        justify-content: space-between;
        align-items: center;
        /*flex-direction: column;s*/
    }
</style>
<body>
<article class="post">
    <ul>
        <li>
            <a href="">
                <img src="bg.png">
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