<div dir="rtl">

* REGEX: RegularExpression
* ^: معرف ابتدای کلمه
* ^: گاهی معنی NOT می‌دهد ← علامتر carret داخل کروشه
* $: معرف انتهای کلمه
* .: معرف کاراکتری حتما باید باشد ولی مهم نیست چه چیزی باشد
* اگر دستور مشخص کند که اگر کاراکتر اول x و کاراکتر y فلان باشد آنگاه به z تبدیل بنماید، اگر خطی دارای تنها یک x باشد در این دستور هیچ تغییری نمیکند


* [[:alnum:]] - [A-Za-z0-9] Alphanumeric characters
* [[:alpha:]] - [A-Za-z] Alphabetic characters
* [[:blank:]] - [ \t] Space or tab characters only
* [[:cntrl:]] - [\x00-\x1F\x7F] Control characters
* [[:digit:]] - [0-9] Numeric characters
* [[:graph:]] - [!-~] Printable and visible characters
* [[:lower:]] - [a-z] Lower-case alphabetic characters
* [[:print:]] - [ -~] Printable (non-Control) characters
* [[:punct:]] - [!-/:-@[-`{-~] Punctuation characters
* [[:space:]] - [ \t\v\f\n\r] All whitespace chars
* [[:upper:]] - [A-Z] Upper-case alphabetic characters
* [[:xdigit:]] - [0-9a-fA-F] Hexadecimal digit characters

```shell
cat /etc/passwd | grep "^b" #تمام خط‌هایی که اول آن با b شروع می‌شود
cat /etc/passwd | grep "^[b]" #تمام خط‌هایی که اول آن با b شروع می‌شود
cat /etc/passwd | grep "^[abc]" #تمام خط‌هایی که اول آن a یا b یا c باشد
cat /etc/passwd | grep "^[a-h]"#تمام خط‌هایی که اول آن a تا h باشد
cat /etc/passwd | grep "^[a-c][f-n]" #کاراکتر اول از حرف a تا c و کاراکترر دوم ار حروف f تا n باشد
cat /etc/passwd | grep "^[a-n]..[f]" #کاراکتر اول از a تا n باشد و کاراکتر دوم و سوم مهم نیست ولی کاراکتر چهارم باید f باشد
cat /etc/passwd | grep "^[^b]" #تمام خط‌هایی که اول آن با b شروع نمی‌شود
cat /etc/passwd | grep n$ #تمام خط‌هایی که آخر آن به n ختم شود
cat /etc/passwd | grep [n]$ #تمام خط‌هایی که آخر آن به n ختم شود
cat /etc/passwd | grep [abc]$ #تمام خط‌هایی که آخر آن a یا b یا c باشد
cat /etc/passwd | grep [a-h]$ #تمام خط‌هایی که آخر آن a تا h باشد
```

</div>