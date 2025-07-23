# 🅰️ مفاهیم و نکات

* **دیتابیس** : پایگاه‌داده فیزیکی که شامل تمام داده‌ها و فایل‌های مرتبط آن است
    * یک دیتابیس می‌تواند شامل چندین Schema باشد
* Schema(اسکیما): نحوه مدیریت و سازمان‌دهی(نظام منطقیِ ساختاریافته) داده‌ها در دیتابیس
    * هر اسکیما می‌تواند شامل چندین جدول‌ودیگر اشیاءپایگاه‌داده باشد
    * کارهای اسکیما
        1. طراحی منطقی ساختار جداول(Tables)و ستون‌های‌آن(Columns) و نوع داده‌ی هر ستون(Data Types)
            - بطورمثال: جدول users شامل ستون‌های id (عددی)، name (رشته‌ای) و email (رشته‌ای) باشد.
        2. طراحی منطقی روابط بین جداول(Relationships) که مثلا رابطه‌ی «یک‌به‌چند» یا «چندبه‌چند» باشند
            - بطور مثال: جدول orders ممکن است به جدول users از طریق کلید خارجی (user_id) مرتبط باشد
        3. قیدها(Constraints)
        4. تعیین قوانین و محدودیت‌ها : شامل قیدهایی مثل PRIMARY KEY، FOREIGN KEY، NOT NULL، UNIQUE و غیره
    * اسکیما در انواع دیتابیس
        * در پایگاه‌داده PostgreSQL : اسکیما به‌طور گسترده استفاده می‌شود و می‌توانید چندین Schema در یک پایگاه‌داده داشته باشید.
        * در پایگاه‌داده MySQL: اسکیما و Database تقریباً معادل هستند. به عبارت دیگر، ایجاد یک Schema معادل با ایجاد یک Database است.
        * در پایگاه‌داده SQLserver :Schema یک لایه‌ی منطقی در داخل یک Database است.
* **database Sharding**:خرد کردن دیتا(از بزرگ به کوچک)
    * optimizing database management systems by separating the rows or columns of a larger database table into multiple smaller tables
* **Database partition**:خرد کردن دیتا(از بزرگ به کوچک)
    * division of a logical database into distinct independent parts

![DatabaseSharding.jpg](../_srcFiles/Images/DatabaseSharding.jpg "DatabaseSharding.jpg")
![DatabasePartition.jpg](../_srcFiles/Images/DatabasePartition.jpg "DatabasePartition.jpg")

# 🅰️ SQLCommands

## 🅱️ select

* GROUP BY: گروه‌بندی اطلاعات
    * برای گروه‌بندی کردن (سورت) کوئری استفاده می‌شود اما به نحوی که از توابع ۱-کانت ۲-ماکس ۳-مین ۴-سام استفاده شود
* **HAVING**: همواره با گروپ‌بای می‌آید
* ORDER BY: مرتب‌سازی اطلاعات

```shell
SELECT column_1, column_2 FROM tableName;
SELECT * FROM tableName;
SELECT * FROM tableName limit 2; #فقط نمایش دو رکورد اول
SELECT * from tableName \G;  #نمایش خروجی به شکل مطلوب

#Where/Like
SELECT * FROM tableName WHERE column = value;
SELECT * FROM tableName WHERE column LIKE 'val%' ;    #(%) represent zero or more unknown characters
SELECT * FROM tableName WHERE column LIKE '%max%';
SELECT * FROM tableName WHERE column LIKE value;    #(_) represent a single unknown character

#GROUP BY
SELECT COUNT(column_1), column_2 FROM tableName GROUP BY column_2; # تعداد متغیرهای موجود در ستون‌دوم و دسته‌بندی آن‌ها بصورت صعودی

#ORDER BY
SELECT column_1, column_2 FROM table ORDER BY column_1      #ترتیب صعودی
SELECT column_1, column_2 FROM table ORDER BY column_1 DESC # ترتیب نزولی

```

> UNION

```shell
SELECT column FROM tableName1 UNION SELECT column FROM tableName2; #ترکیب خروجی دو یا چند سِلِکت  از جدول (حتی جداول‌ متفاوت)
```

## 🅱️ INSERT

```shell
INSERT INTO tableName VALUES ( 'data_A', 'data_B', 'data_C' );
INSERT INTO tableName ( column_A, column_B, column_C ) VALUES ( 'data_1A', 'data_1B', 'data_1C' ), ( 'data_2A', 'data_2B', 'data_2C' ), ( 'data_3A', 'data_3B', 'data_3C' );
INSERT INTO tableName ( column_A, column_B, column_C ) VALUES ( 'data_A', 'data_B', 'data_C' );
```

## 🅱️ UPDATE

```shell
UPDATE tableName SET column_1 = value_1, column_2 = value_2 WHERE column_A=value;

```

## 🅱️ DELETE

```shell
DELETE FROM tableName WHERE column='value';
DELETE FORM tableName WHERE column=’value’ limit 1; #حذف رکورد از جدول [حذف تنها یک مورد درصورت وجود چندین رکورد]
```

## 🅱️ REPLACE

```shell
REPLACE INTO tableName (primaryKey, column1, column2) VALUES ('abc', 1, 2); #اگر رکورد وجود داشت تغییر میکند ودرغیر اینصورت به جدول اضافه می‌شود
Replace Into configuration(`Group`,`Name`,`Value`) Values('sadr','debug','Dashboard'); #اگر رکورد وجود داشت تغییر میکند ودرغیر اینصورت به جدول اضافه می‌شود
```

## 🅱️ Operator

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

## 🅱️ Functions

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

**نکته‌ها**:

* برخی از توابع مثل GROUP_CONCAT() فقط در پایگاه‌های خاصی مثل MySQL موجود هستند.
* توابع FIRST() و LAST() در تمام سیستم‌های SQL وجود ندارند و بیشتر در MS Access استفاده می‌شوند. در MySQL و PostgreSQL از LIMIT یا DISTINCT ON استفاده می‌شود.
* این توابع زمانی قدرتمندتر می‌شوند که با دستوراتی مانند GROUP BY و WHERE ترکیب شوند.

# 🅰️ MYSQL

## 🅱️ Install

```shell
sudo apt install mysql- server #Installation
sudo mysql_secure_installation #ایجاد تنظیمات اولیه
```

## 🅱️ Login

```shell

sudo mysql
mysql -u <USER> -p PASSWORD # [OR] mysql -u <USER> -p → then !EnterPassword
mysql -u <USER> -p <DataBaseName> # → then !EnterPassword
mysql> quite #خروج
```

## 🅱️ DataBase

```shell
mysql> CREATE DATABASE <database_name>;
mysql> CREATE DATABASE <database_name> CHARACTER SET character_set COLLATE collation;
mysql> SHOW DATABASES;
mysql> USE database;
mysql> DROP DATABASE IF EXISTS database;
mysql> DROP DATABASE <db_name>;
```

## 🅱️ user

```shell
#create
mysql> CREATE USER username IDENTIFIED BY 'password';
mysql> CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

#List or Show
mysql > select * from mysql.user
mysql > desc mysql.user
mysql > select host, user, password from mysql.user

#Delete:
mysql> DROP USER 'jeffrey'@'localhost';
mysql> DROP USER IF EXISTS username;
```

### ✅️ Permision

**typeOfPermission**

* **ALL PRIVILEGES**: allow a MySQL user all access to a designated database (or if no database is selected, across the system)
* **CREATE**: allows them to create new tables or databases
* **DROP**: allows them to them to delete tables or databases
* **DELETE**: allows them to delete rows from tables
* **INSERT**: allows them to insert rows into tables
* **SELECT**: allows them to use the Select command to read through databases
* **UPDATE**: allow them to update table rows
* **GRANT OPTION**: allows them to grant or remove other users' privileges

### ✅️ Assigne permission

```shell
mysql> GRANT [typeOfPermission] ON [databaseName].[tableName] TO '[username]'@'localhost’;
mysql> GRANT ALL PRIVILEGES ON *.* TO 'newusername'@'localhost' IDENTIFIED BY 'password';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'newusername'@'localhost';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'newusername'@'localhost' WITH GRANT OPTION;
```

### ✅️ Revoke permission

```shell
mysql > REVOKE [typeOfPermission] ON [databaseName].[tableName] FROM '[username]'@'localhost’;
mysql> REVOKE ALL ON [database name].[table name] FROM '[username]'@'localhost'
```

## 🅱️ Table

```shell
#Create:
mysql> CREATE TABLE table ( column_1 column_1_data_type, column_2 column_2_data_taype );

#Show:
mysql> SHOW TABLES;
mysql> SHOW TABLES FROM DBName;

#Edit:
mysql> ALTER TABLE table ADD COLUMN column data_type; #افزودن ستون جدید به جدول

#Delete
mysql> ALTER TABLE table DROP COLUMN column; #حذف ستون از جدول
mysql> DROP TABLE IF EXISTS table #حذف یک جدول
```

# 🅰️ Reddis

* دیتا را بصورت Key-Value ذخیره می‌کند
* تمام دیتا را در حافظه نگه‌داری می‌کند یعنی سریع است
* حتی می‌تواند بعنوان کش‌سرور استفاده شود
* هرنوع Data از هر نوع Structure را ذخیره می‌کند
* می‌توان بعنوان صف از آن استفاده کرد که دیتا به او بدهیم و آن به دیگران بدهد