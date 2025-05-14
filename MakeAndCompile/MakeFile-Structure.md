# 1.Variables

* با کاراکتر دالر شروع می‌شود
* متغیرهای باید درون پرانتز یا آکولاد قرار بگیرند

## 1.Automatic variables

* Automatic variables are set by make after a rule is matched.
    * $@: the target filename.
    * $*: the target filename without the file extension.
    * $<: the first prerequisite filename.
    * $^: the filenames of all the prerequisites, separated by spaces, discard duplicates.
    * $+: similar to $^, but includes duplicates.
    * $?: the names of all prerequisites that are newer than the target, separated by spaces.

### 1.1.Makefile sample

* در قطعه‌کد زیر شکل عادی و شکل توأم با متغیر را مشاهده می‌کنید(هر دو یکسان هستند ولی با نگارش متفاوت)

  ```shell
  # شکل عادی فایل
  all: hello.exe
  hello.exe: hello.o
       gcc -o hello.exe hello.o
  hello.o: hello.c
       gcc -c hello.c
  clean:
       rm hello.o hello.exe
  ```

  ```shell
  # شکل متغیرگونه فایل
  all: hello.exe
  # $@ matches the target; $< matches the first dependent
  hello.exe: hello.o
      gcc -o $@ $<
  hello.o: hello.c
      gcc -c $<
  clean:
      rm hello.o hello.exe
  ```

# VirtualPath

**مورد VPATH(باحروف بزرگ)**

* تعیین دایرکتوری جهت جستجوی وابستگی‌ها(Dependencies) و فایل‌های تارگت
* For example: Search for dependencies and targets from "src" and "include" directories.The directories are separated by space

  ```shell
  VPATH = src include
  ```

**مورد vpath(باحروف کوچک)**

* برای دقت بیشتر پیرامون نوع فایل و مسیر جستجوی فایل
* For example: Search for .c files in "src" directory; .h files in "include" directory, The pattern matching character '%' matches filename without the extension

  ```
  vpath %.c src
  vpath %.h include
  ```