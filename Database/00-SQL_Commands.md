# 1.select

```shell
SELECT column_1, column_2 FROM tableName;
SELECT * FROM tableName;
SELECT * FROM tableName limit 2; #فقط نمایش دو رکورد اول
SELECT * from tableName \G;  #نمایش خروجی به شکل مطلوب
```

Where/Like

```shell
SELECT * FROM tableName WHERE column = value;
SELECT * FROM tableName WHERE column LIKE 'val%' ;    #(%) represent zero or more unknown characters
SELECT * FROM tableName WHERE column LIKE '%max%';
SELECT * FROM tableName WHERE column LIKE value;    #(_) represent a single unknown character
```

GROUP BY: گروه‌بندی اطلاعات

برای گروه‌بندی کردن (سورت) کوئری استفاده می‌شود اما به نحوی که از توابع ۱-کانت ۲-ماکس ۳-مین ۴-سام استفاده شود

> **HAVING**: همواره با گروپ‌بای می‌آید

```shell
SELECT COUNT(column_1), column_2 FROM tableName GROUP BY column_2; # تعداد متغیرهای موجود در ستون‌دوم و دسته‌بندی آن‌ها بصورت صعودی
```

ORDER BY: مرتب‌سازی اطلاعات

```shell
SELECT column_1, column_2 FROM table ORDER BY column_1      #ترتیب صعودی
SELECT column_1, column_2 FROM table ORDER BY column_1 DESC # ترتیب نزولی

```

UNION

```shell
SELECT column FROM tableName1 UNION SELECT column FROM tableName2; #ترکیب خروجی دو یا چند سِلِکت  از جدول (حتی جداول‌ متفاوت)
```

# 2.INSERT

```shell
INSERT INTO tableName VALUES ( 'data_A', 'data_B', 'data_C' );
INSERT INTO tableName ( column_A, column_B, column_C ) VALUES ( 'data_1A', 'data_1B', 'data_1C' ), ( 'data_2A', 'data_2B', 'data_2C' ), ( 'data_3A', 'data_3B', 'data_3C' );
INSERT INTO tableName ( column_A, column_B, column_C ) VALUES ( 'data_A', 'data_B', 'data_C' );
```

# 3.UPDATE

```shell
UPDATE tableName SET column_1 = value_1, column_2 = value_2 WHERE column_A=value;

```

# 4.DELETE

```shell
DELETE FROM tableName WHERE column='value';
DELETE FORM tableName WHERE column=’value’ limit 1; #حذف رکورد از جدول [حذف تنها یک مورد درصورت وجود چندین رکورد]
```

# 5.REPLACE

```shell
REPLACE INTO tableName (primaryKey, column1, column2) VALUES ('abc', 1, 2); #اگر رکورد وجود داشت تغییر میکند ودرغیر اینصورت به جدول اضافه می‌شود
Replace Into configuration(`Group`,`Name`,`Value`) Values('sadr','debug','Dashboard'); #اگر رکورد وجود داشت تغییر میکند ودرغیر اینصورت به جدول اضافه می‌شود
```

# 6.Operator

| Operator      | What it does                                                          |
|---------------|-----------------------------------------------------------------------|
| `=`           | tests for equality                                                    |
| `!=`          | tests for inequality                                                  |
| `<`           | tests for less-than                                                   |
| `>`           | tests for greater-than                                                |
| `<=`          | tests for less-than or equal-to                                       |
| `>=`          | tests for greater-than or equal-to                                    |
| `BETWEEN`     | tests whether a value lies within a given range                       |
| `IN`          | tests whether a row's value is contained in a set of specified values |
| `EXISTS`      | tests whether rows exist, given the specified conditions              |
| `LIKE`        | tests whether a value matches a specified string                      |
| `IS NULL`     | tests for NULL values                                                 |
| `IS NOT NULL` | tests for all values other than NULL                                  |

# 7.Functions

| نام تابع         | توضیحات                                                           | مثال                                        |
|------------------|-------------------------------------------------------------------|---------------------------------------------|
| `COUNT()`        | تعداد رکوردهای مورد نظر را برمی‌گرداند                            | `SELECT COUNT(name) FROM employees;`        |
| `AVG()`          | میانگین مقادیر یک ستون عددی را محاسبه می‌کند                      | `SELECT AVG(salary) FROM employees;`        |
| `SUM()`          | مجموع مقادیر یک ستون عددی را برمی‌گرداند                          | `SELECT SUM(quantity) FROM orders;`         |
| `MAX()`          | بزرگترین مقدار یک ستون را برمی‌گرداند                             | `SELECT MAX(price) FROM products;`          |
| `MIN()`          | کوچکترین مقدار یک ستون را برمی‌گرداند                             | `SELECT MIN(age) FROM users;`               |
| `GROUP_CONCAT()` | مقادیر یک ستون را در یک گروه به صورت رشته‌ای ادغام می‌کند (MySQL) | `SELECT GROUP_CONCAT(name) FROM employees;` |
| `FIRST()`        | اولین مقدار یک ستون را برمی‌گرداند                                | `SELECT FIRST(order_date) FROM orders;`     |
| `LAST()`         | آخرین مقدار یک ستون را برمی‌گرداند                                | `SELECT LAST(login_time) FROM users;`       |
| `STDDEV()`       | انحراف معیار مقادیر یک ستون عددی را محاسبه می‌کند                 | `SELECT STDDEV(score) FROM results;`        |
| `VARIANCE()`     | واریانس مقادیر یک ستون عددی را محاسبه می‌کند                      | `SELECT VARIANCE(age) FROM patients;`       |

<div style="direction:rtl">

**نکته‌ها**:

* برخی از توابع مثل GROUP_CONCAT() فقط در پایگاه‌های خاصی مثل MySQL موجود هستند.
* توابع FIRST() و LAST() در تمام سیستم‌های SQL وجود ندارند و بیشتر در MS Access استفاده می‌شوند. در MySQL و PostgreSQL از LIMIT یا DISTINCT ON استفاده می‌شود.
* این توابع زمانی قدرتمندتر می‌شوند که با دستوراتی مانند GROUP BY و WHERE ترکیب شوند.

</div>
