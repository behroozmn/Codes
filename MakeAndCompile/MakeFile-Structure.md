# مفاهیم

استفاده از روش ماژولار(Modular) بهترین گزینه در کدنویسی و کامپایل پروژه‌هاست بگونه‌ای که بخش‌های مختلف پروژه به صورت ماژول‌های مجزا کامپایل شوند. این موضوع سبب بروز پیچیدگی خواهد شد که بدین جهت ابزار Make برای تسهیل این مراحل و خودکارسازی این فرایند مورد استفاده قرار می‌گیرد. روند کامپایل این ماژول‌ها در فایلی به‌نام Makefile تعریف می‌شوند.

وقتی شما دستور make را در خط فرمان می‌نویسید، برنامهٔ Make در دایرکتوری فعلی‌ای که در آن قرار دارید فایلی به‌نام Makefile را می‌خواند و شروع به پردازش اولین هدف موجود در آن می‌کند (Default Goal). اما قبل از اینکه دستورات موجود در این هدف اجرا شوند، Make باید تمام پیش‌نیازهای مربوط به آن هدف را پردازش کند. هر یک از این پیش‌نیازها نیز برای خود Rule
دارند که برای ساخت آن‌ها پردازش خواهد شد.

* برای کامپایل makefile.in باید برنامه make در سیستم‌عامل کامپایل‌کننده نصب شده باشد
* استفاده از Make وابسته به زبان برنامه‌نویسی خاصی نیست.
* دستورات فایل makefile در shell اجرا می‌شوند تا سبب ایجاد فایل اجرایی پروژه گردند
* فقط برای کامپایل برنامه‌ها استفاده نمی‌شود بلکه هر کاری اعم از بروزرسانی(فایل‌ها) و تغییر یا حذف نیز مورد استفاده قرار می‌گیرد
* بدلیل نوشته‌شدن جزئیات در Makefile ، امکان کامپایل و نصب را برای کاربر ساده (بدون اطلاعات فنی) فراهم می‌آورد
* کدهای تغییر کرده source پروژه را بصورت اتوماتیک تشخیص می‌دهد. این امکان زمانی مفید خواهد بود که تعداد کدهای source یک برنامه زیاد است




## makefile Structure

```makefile
target: dependencies
     commands # تو رفتگی حتما باید با تب باشد و اسپیس نباید استفاده شود
```

* درصورت کافی نبودن یک خط برای ادامه در خط بعدی در انتهای خط پُر شده یک \ قرار بدهید و به خط جدید بروید
* قوانین  (Rules) به دو دسته کلی تقسیم می‌شوند:
  * قوانین صریح (Explicit Rules): خودمان بصورت مستقیم نام دقیق target، dependencies و دستورات build را مشخص کنی
    * مثال: فرض کنید یک برنامه C دارید با نام `main.c` و می‌خواهید آن را به یک اجرایی به نام `myprogram` کامپایل کنید.
      ```makefile
         myprogram: main.c
       gcc -o myprogram main.c
      ```
  * قوانین غیرصریح (Implicit Rules):برنامه Make خودش تشخیص دهد چگونه یک فایل را بسازد، بدون اینکه شما جزئیات دستورات را بنویسید. این قوانین پیش‌فرض هستند و بر اساس پسوندهای فایل‌ها عمل می‌کنند.
    * مثال:اگر فایل `main.c` موجود باشد و یک target به نام `main.o` تعیین کنید، Make به صورت خودکار می‌داند که باید `main.c` را با gcc کامپایل کند.یعنی می‌توانید فقط قطعه کد زیر را بنویسید
```shell
main.o:
```

    * دو قطعه کد زیر مشابه هستند

```shell
#1
main.o:

#2
main.o: main.c
  gcc -c main.c -o main.o

```

## makefile Structure

فایل Makefile شامل پنج بخش مختلف هستند :
1.     1. قانون صریح (Explicit Rule): معلوم می‌کند چه‌وقت و چطور، باید فایل(ها)ساخته شود.target ها ممکن است به فایل‌(ها) دیگری یا دستورهایی خاص جهت ساخت آن فایل Target  وابستگی داشته باشد.
    2. قوانین غیرصریح (Implicit Rule) معلوم می‌کنند چه وقت و چطور باید دسته‌ای از فایل‌ها که بر اساس نامشان دسته‌بندی شده‌اند ساخته شوند.
    3. متغیرها برای نسبت دادن مقادیر متنی به نامی مشخص است؛ و برای رجوع به آن مقدار متنی، می‌توان از نام متغیر استفاده کرد. یک مثال نوشتن نام تمام فایل‌های آبجکت مورد استفاده در برنامه درون یک متغیر با نام objects است. (برای رجوع ساده‌تر)
    4. رهنمون‌ها فرامینی هستند برای اجرای کارهای خاص که در هنگام پردازش Makefile مورد استفاده قرار می‌گیرند. مانند:
        ◦ خواندن محتویات Makefile دیگری در دل یک Makefile
        ◦ تصمیم‌گیری (بر اساس مقدار درون یک متغیر) برای پردازش کردن یا نکردن قسمتی از Makefile
        ◦ مقدار دهی به متغیرها از طریق متنی که شامل چندین خط است.
    5. کامنت: با نوشتن کارکتر # می‌توان توضیحاتی در Makefile نوشت که عملاً پردازش نمی‌شوند و فقط برای خواناتر شدن Makefile برای انسان خواهند شد.




# x.Variables

* با کاراکتر دالر شروع می‌شود
* متغیرهای باید درون پرانتز یا آکولاد قرار بگیرند

## x.Automatic variables

* Automatic variables are set by make after a rule is matched.
    * $@: the target filename.
    * $*: the target filename without the file extension.
    * $<: the first prerequisite filename.
    * $^: the filenames of all the prerequisites, separated by spaces, discard duplicates.
    * $+: similar to $^, but includes duplicates.
    * $?: the names of all prerequisites that are newer than the target, separated by spaces.

### x.x.Sample

در قطعه‌کد زیر شکل عادی و شکل توأم با متغیر را مشاهده می‌کنید(هر دو یکسان هستند ولی با نگارش متفاوت)

  ```shell
  all: hello.exe
  hello.exe: hello.o
       gcc -o hello.exe hello.o
  hello.o: hello.c
       gcc -c hello.c
  clean:
       rm hello.o hello.exe
  ```

  ```shell
  # Ussing variables
  all: hello.exe
  # $@ matches the target; $< matches the first dependent
  hello.exe: hello.o
      gcc -o $@ $<
  hello.o: hello.c
      gcc -c $<
  clean:
      rm hello.o hello.exe
  ```

## 2.VirtualPath

**وی‌پَت با حروف کوچک یا VPATH**: تعیین دایرکتوری جهت جستجوی وابستگی‌ها(Dependencies) و فایل‌های تارگت

* For example: Search for dependencies and targets from "src" and "include" directories.The directories are separated by space

```shell
VPATH = src include
```

**وی‌پَت با حروف بزرگ یا vpath**: برای دقت بیشتر پیرامون نوع فایل و مسیر جستجوی فایل

* For example: Search for .c files in "src" directory; .h files in "include" directory, The pattern matching character '%' matches filename without the extension

```
vpath %.c src
vpath %.h include
```

# Sample1: Hello World

```shell
// hello.c
#include <stdio.h>
int main() {
    printf("Hello, world!\n");
    return 0;
}


//makefile
all: hello.exe
hello.exe: hello.o
	 gcc -o hello.exe hello.o
hello.o: hello.c
	 gcc -c hello.c
clean:
	 rm hello.o hello.exe
```

**توضیحات**

* فایل makeFile را باید در مسیر جاری پروژه قرار دهیم
* بخش all بصورت پیش‌فرض اجرا می‌شود
* اگر پس از اجرای دستور ALL مجدد این دستور را اجرا نماییم با دستور زیر مواجه می‌شویم
    * `make: Nothing to be done for 'all'`
* ترتیب اجرای خط به خط
    * ابتدا سراغ تارگت `all` رفته و درمیابد که پیش‌نیاز آن `hello.exe` است
    * میرود سراغ تارگت `hello.exe` و مشاهده میکند که پیش نیاز آن فایل `hello.o` است
    * میرود سراغ تارگت `hello.o` و مشاهده میکند که پیش‌نیاز آن فایل hello.c است که متوجه می‌شود که این فایل در مسیر جاری وجود دارد
    * در ادامه این فایل را میخواند
    * در ادامه دستورات این تارگت(که فایل پیش‌نیاز آن را پیدا کرده است یعنی دستورات تارگت `hello.o`) را اجرا میکند یعنی دستور زیر
    ```shell
    gcc -c hello.c
    ```
    * حال که بادستور بالا فایل `hello.o` ایجاد شد در ادامه دستور تارگت hello.exe را اجرا میکند یعنی دستور زیر
    ```shell
    `gcc -o hello.exe hello.o`
    ```
    


