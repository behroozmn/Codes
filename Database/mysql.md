# 1.Install

```shell
sudo apt install mysql- server #Installation
sudo mysql_secure_installation #ایجاد تنظیمات اولیه
```

# 2.Login

```shell

sudo mysql
mysql -u <USER> -p PASSWORD # [OR] mysql -u <USER> -p → then !EnterPassword
mysql -u <USER> -p <DataBaseName> # → then !EnterPassword
mysql> quite #خروج
```

# 3.DataBase

```shell
mysql> CREATE DATABASE <database_name>;
mysql> CREATE DATABASE <database_name> CHARACTER SET character_set COLLATE collation;
mysql> SHOW DATABASES;
mysql> USE database;
mysql> DROP DATABASE IF EXISTS database;
mysql> DROP DATABASE <db_name>;
```

# 4.user

create

```shell
mysql> CREATE USER username IDENTIFIED BY 'password';
mysql> CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```

List or Show

```shell
mysql > select * from mysql.user
mysql > desc mysql.user
mysql > select host, user, password from mysql.user

```

Delete:

```shell
mysql> DROP USER 'jeffrey'@'localhost';
mysql> DROP USER IF EXISTS username;
```

## 4.4.Permision

**typeOfPermission**

* **ALL PRIVILEGES**: allow a MySQL user all access to a designated database (or if no database is selected, across the system)
* **CREATE**: allows them to create new tables or databases
* **DROP**: allows them to them to delete tables or databases
* **DELETE**: allows them to delete rows from tables
* **INSERT**: allows them to insert rows into tables
* **SELECT**: allows them to use the Select command to read through databases
* **UPDATE**: allow them to update table rows
* **GRANT OPTION**: allows them to grant or remove other users' privileges

## 4.4.1.Assigne permission

```shell
mysql> GRANT [typeOfPermission] ON [databaseName].[tableName] TO '[username]'@'localhost’;
mysql> GRANT ALL PRIVILEGES ON *.* TO 'newusername'@'localhost' IDENTIFIED BY 'password';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'newusername'@'localhost';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'newusername'@'localhost' WITH GRANT OPTION;
```

## 4.4.2.Revoke permission

```shell
mysql > REVOKE [typeOfPermission] ON [databaseName].[tableName] FROM '[username]'@'localhost’;
mysql> REVOKE ALL ON [database name].[table name] FROM '[username]'@'localhost'
```

# 5.Table

Create:

```shell
mysql> CREATE TABLE table ( column_1 column_1_data_type, column_2 column_2_data_taype );
```

Show:

```shell
mysql> SHOW TABLES;
mysql> SHOW TABLES FROM DBName;
```

Edit:

```shell
mysql> ALTER TABLE table ADD COLUMN column data_type; #افزودن ستون جدید به جدول
```

Delete

```shell
mysql> ALTER TABLE table DROP COLUMN column; #حذف ستون از جدول
mysql> DROP TABLE IF EXISTS table #حذف یک جدول
```