# 1.Concept

استفاده از روش ماژولار(Modular) بهترین گزینه در کدنویسی و کامپایل پروژه‌هاست بگونه‌ای که بخش‌های مختلف پروژه به صورت ماژول‌های مجزا کامپایل شوند. این موضوع سبب بروز پیچیدگی خواهد شد که بدین جهت ابزار Make برای تسهیل این مراحل و خودکارسازی این فرایند مورد استفاده قرار می‌گیرد. روند کامپایل این ماژول‌ها در فایلی به‌نام Makefile تعریف می‌شوند.

وقتی شما دستور make را در خط فرمان می‌نویسید، برنامهٔ Make در دایرکتوری فعلی‌ای که در آن قرار دارید فایلی به‌نام Makefile را می‌خواند و شروع به پردازش اولین هدف موجود در آن می‌کند (Default Goal). اما قبل از اینکه دستورات موجود در این هدف اجرا شوند، Make باید تمام پیش‌نیازهای مربوط به آن هدف را پردازش کند. هر یک از این پیش‌نیازها نیز برای خود Rule
دارند که برای ساخت آن‌ها پردازش خواهد شد.

* برای کامپایل makefile.in باید برنامه make در سیستم‌عامل کامپایل‌کننده نصب شده باشد
* استفاده از Make وابسته به زبان برنامه‌نویسی خاصی نیست.
* دستورات فایل makefile در shell اجرا می‌شوند تا سبب ایجاد فایل اجرایی پروژه گردند
* فقط برای کامپایل برنامه‌ها استفاده نمی‌شود بلکه هر کاری اعم از بروزرسانی(فایل‌ها) و تغییر یا حذف نیز مورد استفاده قرار می‌گیرد
* بدلیل نوشته‌شدن جزئیات در Makefile ، امکان کامپایل و نصب را برای کاربر ساده (بدون اطلاعات فنی) فراهم می‌آورد
* کدهای تغییر کرده source پروژه را بصورت اتوماتیک تشخیص می‌دهد. این امکان زمانی مفید خواهد بود که تعداد کدهای source یک برنامه زیاد است

# 2.makefile Structure and Syntax

```makefile
target: dependencies
     commands # تو رفتگی حتما باید با تب باشد و اسپیس نباید استفاده شود
```

* درصورت کافی نبودن یک خط برای ادامه در خط بعدی در انتهای خط پُر شده یک \ قرار بدهید و به خط جدید بروید

# 3.Rules

قوانین  (Rules) به دو دسته کلی تقسیم می‌شوند:

**دسته اول-قوانین صریح (Explicit Rules):** خودمان بصورت مستقیم نام دقیق target، dependencies و دستورات build را مشخص کنی

* انعطاف‌پذیری بیشتر
* خوانایی واضح‌تر
* مثال: فرض کنید یک برنامه C دارید با نام `main.c` و می‌خواهید آن را به یک اجرایی به نام `myprogram` کامپایل کنید.

```makefile
myprogram: main.c
  gcc -o myprogram main.c
```

**دسته دوم-قوانین غیرصریح (Implicit Rules):** برنامه Make خودش تشخیص دهد چگونه یک فایل را بسازد، بدون اینکه شما جزئیات دستورات را بنویسید. این قوانین پیش‌فرض هستند و بر اساس پسوندهای فایل‌ها عمل می‌کنند.

* انعطاف‌پذیری کمتر (اما کاربرد عمومی دارد)
* خوانانی کوتاه‌تر اما گاهی گیج‌کننده برای تازه‌کارها
* مثال:اگر فایل `main.c` موجود باشد و یک target به نام `main.o` تعیین کنید، Make به صورت خودکار و ضمنی می‌داند که باید `main.c` را با gcc کامپایل کند.
    * یعنی می‌توانید فقط قطعه کد زیر را بعنوان قانون غیر صریح(Implicit Rules) بنویسید

```makefile
main.o:
```

* در موضوع قوانین غیرصریح (Implicit Rules) دو قطعه کد زیر مشابه هستند. موارد تعریف شده در بخش دوم بصورت ضمنی توسط برنامه Make خودش قانون ضمنی (implicit) را به کار می‌برد.

```makefile
#1️⃣️ Explicit Rule یا غیرصریح
main.o:

#2️⃣️:Implicit Rule یا صریح
main.o: main.c
  gcc -c main.c -o main.o

```

# 4.Variables

* با کاراکتر دالر شروع می‌شود
* متغیرهای باید درون پرانتز یا آکولاد قرار بگیرند
* در makefile از متغیرهای استاندارد و رایج نظیر موارد زیر استفاده می‌شود
    * CC:
        * CC = gcc
    * CFLAGS = -Wall -Wextra -g
    * CPPFLAGS
    * LDFLAGS

<div style="direction: rtl">

## 4.1GeneralVariable

جدول کامل متغیرهای رایج در Makefile

| نام متغیر       | نوع      | توضیح کامل                                                  | مثال استفاده                         |
|-----------------|----------|-------------------------------------------------------------|--------------------------------------|
| `CC`            | کامپایلر | مشخص کننده کامپایلر C (مانند `gcc`, `clang`)                | `CC = gcc`                           |
| `CXX`           | کامپایلر | مشخص کننده کامپایلر C++ (مانند `g++`, `clang++`)            | `CXX = g++`                          |
| `CPP`           | کامپایلر | پیش‌پردازنده C/C++                                          | `CPP = cpp`                          |
| `FC`            | کامپایلر | کامپایلر زبان Fortran                                       | `FC = gfortran`                      |
| `PC`            | کامپایلر | کامپایلر Pascal (مانند `fpc`)                               | `PC = fpc`                           |
| `CFLAGS`        | گزینه‌ها | گزینه‌های کامپایلر برای زبان C                              | `CFLAGS = -Wall -Wextra -O2`         |
| `CXXFLAGS`      | گزینه‌ها | گزینه‌های کامپایلر برای زبان C++                            | `CXXFLAGS = -std=c++17 -g`           |
| `FFLAGS`        | گزینه‌ها | گزینه‌های کامپایلر Fortran                                  | `FFLAGS = -O3 -m64`                  |
| `PFLAGS`        | گزینه‌ها | گزینه‌های کامپایلر Pascal                                   | `PFLAGS = -Mobjfpc -Criot`           |
| `CPPFLAGS`      | گزینه‌ها | گزینه‌های پیش‌پردازنده C/C++ (مثل `-I`, `-D`)               | `CPPFLAGS = -Iinclude -DNDEBUG`      |
| `LDFLAGS`       | گزینه‌ها | گزینه‌های لینکر (مانند `-L`, `-rpath`)                      | `LDFLAGS = -L/usr/local/lib`         |
| `LDLIBS`        | لینکاژ   | لیبری‌هایی که باید لینک شوند                                | `LDLIBS = -lm -lpthread`             |
| `AR`            | کارولیب  | کارولیب (archive tool) برای ساخت static library             | `AR = ar`                            |
| `ARFLAGS`       | گزینه‌ها | گزینه‌های `ar` (مانند `rcs`)                                | `ARFLAGS = rcs`                      |
| `RANLIB`        | کارولیب  | ابزاری برای ایجاد فهرست نمادهای قابل لینک در static library | `RANLIB = ranlib`                    |
| `RM`            | سیستمی   | دستور حذف فایل (معمولاً `rm -f`)                            | `RM = rm -f`                         |
| `INSTALL`       | سیستمی   | دستور نصب فایل‌ها در سیستم                                  | `INSTALL = install`                  |
| `prefix`        | مسیر     | پیشوند مسیر اصلی برای نصب (معمولا `/usr/local`)             | `prefix = /usr/local`                |
| `exec_prefix`   | مسیر     | پیشوند مسیر اجرایی (معمولا `$(prefix)`)                     | `exec_prefix = $(prefix)`            |
| `bindir`        | مسیر     | مسیر نصب اجرایی‌ها                                          | `bindir = $(exec_prefix)/bin`        |
| `includedir`    | مسیر     | مسیر نصب header فایل‌ها                                     | `includedir = $(prefix)/include`     |
| `libdir`        | مسیر     | مسیر نصب لیبری‌ها                                           | `libdir = $(exec_prefix)/lib`        |
| `datadir`       | مسیر     | مسیر نصب داده‌های مشترک                                     | `datadir = $(prefix)/share`          |
| `mandir`        | مسیر     | مسیر نصب فایل‌های راهنما (man pages)                        | `mandir = $(datadir)/man`            |
| `SRCS`          | منبع     | لیست فایل‌های منبع (مانند `.c`, `.cpp`, `.f90`)             | `SRCS = main.c utils.c`              |
| `OBJS`          | object   | لیست فایل‌های object (مانند `.o`)                           | `OBJS = main.o utils.o`              |
| `HDRS`          | منبع     | لیست header فایل‌ها (مانند `.h`)                            | `HDRS = utils.h`                     |
| `TARGET`        | خروجی    | نام برنامه یا لیبری نهایی                                   | `TARGET = myprogram`                 |
| `PROGS`         | خروجی    | لیست تمام برنامه‌هایی که build می‌شوند                      | `PROGS = app1 app2`                  |
| `LIBS`          | خروجی    | لیست لیبری‌هایی که build می‌شوند                            | `LIBS = libmylib.a`                  |
| `TESTS`         | تست      | لیست تست‌های واحد یا تست‌کیس‌ها                             | `TESTS = test_math test_utils`       |
| `DOCS`          | مستندات  | فایل‌های مستندات تولیدی (مانند HTML, PDF)                   | `DOCS = docs/html/index.html`        |
| `TAGS`          | ابزار    | فایل‌های تگ (برای vim/emacs)                                | `TAGS = tags`                        |
| `MAKEDEPEND`    | ابزار    | ابزاری برای تولید وابستگی‌های include                       | `MAKEDEPEND = makedepend`            |
| `YACC`          | ابزار    | parser generator (مانند `bison`)                            | `YACC = bison`                       |
| `LEX`           | ابزار    | lexer generator (مانند `flex`)                              | `LEX = flex`                         |
| `FLEX`          | ابزار    | flex lexer generator                                        | `FLEX = flex`                        |
| `BISON`         | ابزار    | Bison parser generator                                      | `BISON = bison`                      |
| `MOC`           | Qt       | Meta-Object Compiler for Qt                                 | `MOC = moc`                          |
| `UIC`           | Qt       | UI compiler for Qt                                          | `UIC = uic`                          |
| `QMAKE`         | Qt       | QMake utility                                               | `QMAKE = qmake`                      |
| `JAVAC`         | Java     | کامپایلر زبان Java                                          | `JAVAC = javac`                      |
| `JFLAGS`        | گزینه‌ها | گزینه‌های کامپایلر Java                                     | `JFLAGS = -g`                        |
| `PYTHON`        | Python   | مفسر یا کامپایلر Python                                     | `PYTHON = python3`                   |
| `SWIG`          | ابزار    | ابزار تولید wrapper بین زبان‌های مختلف                      | `SWIG = swig`                        |
| `SWIGFLAGS`     | گزینه‌ها | گزینه‌های SWIG                                              | `SWIGFLAGS = -python`                |
| `SED`           | سیستمی   | جستجو و جایگزینی الگو در فایل‌ها                            | `SED = sed`                          |
| `AWK`           | سیستمی   | پردازش الگو و داده در فایل‌ها                               | `AWK = awk`                          |
| `GREP`          | سیستمی   | جستجو در فایل‌ها                                            | `GREP = grep`                        |
| `CP`            | سیستمی   | کپی کردن فایل‌ها                                            | `CP = cp`                            |
| `MV`            | سیستمی   | تغییر نام یا انتقال فایل                                    | `MV = mv`                            |
| `MKDIR`         | سیستمی   | ایجاد پوشه                                                  | `MKDIR = mkdir -p`                   |
| `TAR`           | سیستمی   | ابزار tar برای فشرده‌سازی                                   | `TAR = tar`                          |
| `ZIP`           | سیستمی   | ابزار zip برای فشرده‌سازی                                   | `ZIP = zip`                          |
| `UNZIP`         | سیستمی   | ابزار unzip برای باز کردن فایل‌های zip                      | `UNZIP = unzip`                      |
| `GIT`           | ابزار    | مدیریت نسخه‌ها                                              | `GIT = git`                          |
| `VALGRIND`      | تست      | ابزار تست حافظه                                             | `VALGRIND = valgrind`                |
| `GCOV`          | تست      | ابزار code coverage برای GCC                                | `GCOV = gcov`                        |
| `PERL`          | سیستمی   | مفسر Perl                                                   | `PERL = perl`                        |
| `PHP`           | سیستمی   | مفسر PHP                                                    | `PHP = php`                          |
| `SHELL`         | سیستمی   | shell استفاده شده در Makefile (معمولاً `/bin/sh`)           | `SHELL = /bin/bash`                  |
| `MAKE`          | ابزار    | خود دستور `make`                                            | `MAKE = make`                        |
| `DESTDIR`       | مسیر     | مسیر موقت برای نصب (قبل از root)                            | `DESTDIR = /tmp/install`             |
| `PREFIX`        | مسیر     | معادل `prefix`، برای سازگاری با بعضی پروژه‌ها               | `PREFIX = /opt/myapp`                |
| `VERSION`       | عمومی    | نسخه نرم‌افزار                                              | `VERSION = 1.0.0`                    |
| `DEBUG`         | گزینه‌ها | فلگ برای enable کردن debug                                  | `DEBUG = -g`                         |
| `OPTIMIZE`      | گزینه‌ها | فلگ بهینه‌سازی                                              | `OPTIMIZE = -O3`                     |
| `PROFILE`       | گزینه‌ها | فلگ برای profiling                                          | `PROFILE = -pg`                      |
| `STATIC`        | گزینه‌ها | فلگ برای build static                                       | `STATIC = -static`                   |
| `SHARED`        | گزینه‌ها | فلگ برای build shared library                               | `SHARED = -shared`                   |
| `PIC`           | گزینه‌ها | Position Independent Code برای لیبری‌های shared             | `PIC = -fPIC`                        |
| `THREADS`       | گزینه‌ها | فلگ برای پشتیبانی از multi-threading                        | `THREADS = -pthread`                 |
| `VERBOSE`       | گزینه‌ها | فلگ برای نمایش جزئیات build                                 | `VERBOSE = 1`                        |
| `CONFIG`        | عمومی    | تنظیمات پیکربندی                                            | `CONFIG = release`                   |
| `OS`            | عمومی    | سیستم عامل هدف                                              | `OS = Linux`                         |
| `ARCH`          | عمومی    | معماری CPU هدف                                              | `ARCH = x86_64`                      |
| `EXEEXT`        | خروجی    | پسوند فایل اجرایی (در ویندوز `.exe`)                        | `EXEEXT = .exe`                      |
| `OBJEXT`        | object   | پسوند فایل object                                           | `OBJEXT = .o`                        |
| `LIBEXT`        | خروجی    | پسوند فایل لیبری (`.a`, `.so`, `.dll`)                      | `LIBEXT = .a`                        |
| `DOCSDIR`       | مسیر     | مسیر ذخیره مستندات                                          | `DOCSDIR = $(prefix)/doc/$(PROJECT)` |
| `ETCDIR`        | مسیر     | مسیر فایل‌های config                                        | `ETCDIR = $(prefix)/etc`             |
| `DATADIR`       | مسیر     | مسیر داده‌های برنامه                                        | `DATADIR = $(prefix)/data`           |
| `LOCALEDIR`     | مسیر     | مسیر فایل‌های ترجمه                                         | `LOCALEDIR = $(DATADIR)/locale`      |
| `SYSCONFDIR`    | مسیر     | مسیر فایل‌های پیکربندی سیستمی                               | `SYSCONFDIR = /etc`                  |
| `LOCALSTATEDIR` | مسیر     | مسیر داده‌های محلی سیستم (مانند log, run)                   | `LOCALSTATEDIR = /var`               |
| `INFODIR`       | مسیر     | مسیر info manuals                                           | `INFODIR = $(prefix)/info`           |
| `HTMLDIR`       | مسیر     | مسیر مستندات HTML                                           | `HTMLDIR = $(DOCSDIR)/html`          |
| `PDFDIR`        | مسیر     | مسیر مستندات PDF                                            | `PDFDIR = $(DOCSDIR)/pdf`            |
| `MANDIR`        | مسیر     | مسیر فایل‌های man page                                      | `MANDIR = $(DATADIR)/man`            |
| `XSLTPROC`      | ابزار    | XSLT processor                                              | `XSLTPROC = xsltproc`                |
| `DOXYGEN`       | ابزار    | ابزار تولید مستندات Doxygen                                 | `DOXYGEN = doxygen`                  |
| `SPHINXBUILD`   | ابزار    | ابزار ساخت مستندات Sphinx                                   | `SPHINXBUILD = sphinx-build`         |
| `CTEST`         | تست      | تست runner برای CMake                                       | `CTEST = ctest`                      |
| `AUTOMAKE`      | ابزار    | ابزار Automake                                              | `AUTOMAKE = automake`                |
| `AUTOCONF`      | ابزار    | ابزار Autoconf                                              | `AUTOCONF = autoconf`                |
| `LIBTOOL`       | ابزار    | ابزار Libtool                                               | `LIBTOOL = libtool`                  |
| `PKG_CONFIG`    | ابزار    | ابزار pkg-config برای یافتن لیبری‌ها                        | `PKG_CONFIG = pkg-config`            |
| `WGET`          | سیستمی   | دانلود فایل از طریق HTTP                                    | `WGET = wget`                        |
| `CURL`          | سیستمی   | دانلود/آپلود داده از طریق شبکه                              | `CURL = curl`                        |
| `SSH`           | سیستمی   | اتصال به روت Remote                                         | `SSH = ssh`                          |
| `SCP`           | سیستمی   | کپی فایل روی SSH                                            | `SCP = scp`                          |
| `RSYNC`         | سیستمی   | سنکرون کردن فایل‌ها                                         | `RSYNC = rsync`                      |
| `DATE`          | سیستمی   | نمایش یا تبدیل تاریخ                                        | `DATE = date`                        |
| `UUIDGEN`       | سیستمی   | تولید UUID                                                  | `UUIDGEN = uuidgen`                  |
| `BASENAME`      | سیستمی   | نمایش نام فایل بدون مسیر                                    | `BASENAME = basename`                |
| `DIRNAME`       | سیستمی   | نمایش مسیر فایل بدون نام فایل                               | `DIRNAME = dirname`                  |
| `REALPATH`      | سیستمی   | نمایش مسیر واقعی فایل                                       | `REALPATH = realpath`                |
| `HOSTNAME`      | سیستمی   | نمایش نام هاست                                              | `HOSTNAME = hostname`                |
| `UNAME`         | سیستمی   | نمایش اطلاعات سیستم                                         | `UNAME = uname`                      |
| `ID`            | سیستمی   | نمایش شناسه کاربر                                           | `ID = id`                            |
| `WHOAMI`        | سیستمی   | نمایش نام کاربر فعلی                                        | `WHOAMI = whoami`                    |

</div>

* با وجود makefile زیر با زدن دستور `make` باید main.c را با دستور `gcc -Wall -Wextra -g -o main main.c` کامپایل کند

```makefile
CC = gcc
CFLAGS = -Wall -Wextra -g

main: main.c
```

* با وجود makefile زیر با زدن دستور `make` باید دستور `gcc -Wall -Wextra -g   -c -o main.o main.c` اجرا شود
    * اگر فایل main.c وجود نداشته باشد، make نمی‌تواند main.o را بسازد و خطا می‌دهد.

```makefile
CC = gcc
CFLAGS = -Wall -Wextra -g

all: main.o

main.o:
```

## 4.2.Automatic variables[متغیرهای خودکار]

متغیرهایی هستند که توسط make به صورت خودکار وقتی یک قاعده(rule) با یک هدف(target) و وابستگی‌های(prerequisites) آن مطابقت پیدا می‌کند ، تنظیم می‌شوند
این متغیرها بسیار مفید هستند زیرا به شما اجازه می‌دهند بدون نوشتن دوباره مسیرها و نام فایل‌ها، در دستورات build استفاده کنید.

* Automatic variables are set by make after a rule is matched.
    * $@: این متغیر حاوی مقدار تارگت است(دقیقا عبارت تارگت)
    * $*: این متغیر حاوی فقط نام تارگت است(بدون پسوند)
    * $<: نام اولین پیشنیاز
    * $^: تمام پیشنیازها(**بدون** تکرار)
        * اگر بیشتر از یک مورد باشند توسط خط فاصله از هم جدا خواهند شد
    * $+: تمام پیشنیازها(**با** تکرار)
        * اگر بیشتر از یک مورد باشند توسط خط فاصله از هم جدا خواهند شد
    * $?: نام تمام وابستگی‌ها(پیش‌نیازها) که جدیدتر از هدف(تارگت) هستند
        * اگر بیشتر از یک مورد باشند توسط خط فاصله از هم جدا خواهند شد
        * وقتی make یک قاعده(rule)را پردازش می‌کند، زمان آخرین تغییر هر فایل را بررسی می‌کند.اگر یکی از وابستگی‌ها بعد از ساختن تارگت تغییر کرده باشد، آن وابستگی "جدیدتر" محسوب می‌شود.

برای فهم بهتر $? به توضیحات زیر توجه نمایید
```makefile
main.o: main.c defs.h
    $(CC) -c $< -o $@
```

* فرض شود که
    * فایل `main.c` آخرین بار ۱۰ دقیقه قبل تغییر کرده‌باشد
    * فایل `defs.h` آخرین بار ۲ ساعت قبل تغییر کرده‌باشد
    * فایل `main.o` آخرین بار ۳ ساعت قبل تغییر کرده‌باشد
* آنگاه
    * فایل main.c جدیدتر از main.o است. پس یعنی باید در $? باشد
    * فایل defs.h قدیمی‌تر از main.o است. پس یعنی بایددر $? نباشد
* بنابراین
    * $? = main.c

## 4.4.Sample1

```makefile
main.o: main.c utils.h
    $(CC) -c $< -o $@
```

* $@ → `main.o`
* $< → `main.c`
* $^ → `main.c` `utils.h`
* $* → `main`
* $+ → `main.c` `utils.h`
* $? → Only the dependencies that are newer than `main.o`
    * فقط وابستگی‌هایی که جدیدتر از main.o هستند
    * مثلاً اگر utils.h تغییر کرده باشد، $? برابر main.c utils.h می‌شود

## 4.4.Sample2

```makefile
all: program
program: main.o utils.o
    $(CC) $^ -o $@
main.o: main.c defs.h
    $(CC) -c $< -o $@
utils.o: utils.c defs.h
    $(CC) -c $< -o $@
```

* for `main.o`
    * $@ = main.o → TargetName
    * $< = main.c → First Dependency
    * $^ = main.c defs.h → All dependences, discard duplicates.
    * $* = main → 'TargetName' without extension
    * $?
        * فقط فایل‌هایی که جدیدتر از main.o هستند (مثلاً main.c)
    * $+ = main.c defs.h → All dependences
        * در این حالت تکراری نداریم
* for `utils.o`
    * $@ = utils.o
    * $< = utils.c
    * $^ = utils.c defs.h
    * $* = utils
    * $?
        * فایل‌هایی که جدیدتر از utils.o هستند (مثلاً utils.c)
    * $+ = utils.c defs.h
    * =
* for `program`
    * $@ = program
    * $^ = main.o utils.o → All dependences, discard duplicates.
    * $< = main.o → First Dependency
    * $* = program → 'TargetName' without extension
    * $?
        * فایل‌هایی که جدیدتر از program هستند (مثلاً main.o)
    * $+ = main.o utils.o

## 4.5.Sample3

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
  # Ussing variables(استفاده از مدل متغیرگونه)
  all: hello.exe
  # $@ matches the target; $< matches the first dependent
  hello.exe: hello.o
      gcc -o $@ $<
  hello.o: hello.c
      gcc -c $<
  clean:
      rm hello.o hello.exe
  ```

# 5.VirtualPath

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
