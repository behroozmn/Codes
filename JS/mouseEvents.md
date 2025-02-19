```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body onload="loadbody()">

<div onmouseover="mouseOver(this)"
     onmouseout="mouseOut(this)"
     onmousedown="mouseDown(this)"
     onmouseup="mouseUp(this)"
     style="width: 120px; height: 20px; background-color: purple; color: black;
    padding: 40px;"> javascript
</div>


</body>

<script>
    function mouseDown(om1) {
        om1.innerHTML = "onMouseDown";
        om1.style.backgroundColor = "red";
    }

    function mouseOver(om1) {
        om1.innerHTML = "onMouseOver";
        om1.style.backgroundColor = "green";
    }

    function mouseUp(om2) {
        om2.innerHTML = "onMouseUp";
        om2.style.backgroundColor = "blue";
    }

    function mouseOut(om2) {
        om2.innerHTML = "onMouseOut";
        om2.style.backgroundColor = "yellow";
    }

</script>

</html>
```