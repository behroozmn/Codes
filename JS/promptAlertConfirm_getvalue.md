```html
<!DOCTYPE html>
<html lang="en">
<body>

<button onclick="myfunc()">click me</button>
<p id="demo"></p>

</body>
<script>
    function myfunc() {
        if (confirm("لطفا انتخاب کنین که آیا می‌خواهید مقدار وارد نمایید یا خیر؟")) {
            var value = prompt("لطفا عدد خود را وارد نمایید", "عدد پیش‌فرض را ۲۰ درنظر می‌توان گرفت");
            document.getElementById("demo").innerHTML = value;
            alert(value);
        }
    }
</script>

</html>
```