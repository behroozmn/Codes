```html
<!DOCTYPE html>
<html lang="en">
<body>
<div id="div1">
    <p id="p1">element1</p>
    <p id="p2">element2</p>
</div>
</body>

<script>
    var elem_div = document.getElementById("div1");
    var newElem_p = document.createElement("p");
    var elem_p1 = document.getElementById("p1");
    var elem_p2 = document.getElementById("p2");

    var text = document.createTextNode("NewText");
    newElem_p.appendChild(text);
    elem_div.appendChild(newElem_p);
    elem_div.insertBefore(newElem_p, elem_p2);
    elem_div.removeChild(elem_p2);
    elem_div.replaceChild(newElem_p, elem_p1);
</script>
</html>
```