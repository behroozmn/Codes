# Compile Proces steps

برنامه GCC یک برنامه نوشته شده به زبان C یا C++ را در ۴ مرحله اجرا می کند به عنوان مثال، `gcc -o hello.exe hello.c` به صورت زیر انجام می شود

# 1️⃣️:PreProcessing[پیش‌پردازش]

* فایل‌های پیش‌پردازش شده دارای پسوند “i.” هستند.
* مشمول کلیه خطوط در زبان C است که با علامت # شروع می‌شوند.
    * شامل [defineها که تعریف مقادیر ثابت است] و [Headerها]
* در فایل خروجی پیش‌پردازنده برای کامنت‌گذاری از علامت # همراه با یک عدد استفاده می‌شود
* در این مرحله مجموعه دستورات پیش‌پردازنده با مقادیر واقعی‌شان جایگزین می‌شوند.
    * فایلی که با پسوند i می‌باشد حاوی هیچ «include» یا «define» نیست و بجای هرکدام از «include»‌ یا «define» مقادیر محتوی آنها قرار گرفته است
    * دستورات پیش‌پردازنده با محتوایشان جایگزین شده‌اند و خود این دستورات یا کامنت شده یا حذف شده‌اند.
    * در این مرحله، عملکرد کامپایلر به‌صورت بازگشتی است.
        * یعنی ابتدا کتابخانه‌هایی که سورس کد به آنها نیاز دارد را می‌یابد، سپس کتابخانه‌هایی که کتابخانه‌های سورس کد به آنها نیاز دارد را می‌یابد
        * این کار را تا جایی ادامه می‌دهد که کتابخانه‌ای موردنیاز کتابخانه دیگر نباشد.
        * پس از یافتن آنها، از همان نقطه شروع ، اقدام به جایگزینی کتابخانه‌ها با محتوای آنها در کد می‌کند
* برای مقداردهی به ثابت‌های کد، می‌توان در هنگام کامپایل این مقادیر داده شود.[در قطعه کد FORM1 بجای تعریف مقدار A تحت عنوان «define» آن را در هنگام کامپایل مقدار دهید]

gcc -E [Name of Source Code] -o [Name of Output File]

* `gcc -E metech2.c -o PreProcessed.i`
* `cpp file.c > PreProcessedFile.i` #via the GNU C Preprocessor (cpp.exe)

```shell
//metech3.c Source Code
#include <stdio.h>
int main(){
printf("5 * 2 = %d", A);
}
```

`gcc -DA=100 metech3.c -o output`

# 2️⃣️:Compilling[کامپایل]

* در این مرحله کد پیش‌پردازش شده کامپایل می‌شود یعنی کد زبان C به یک کد اسمبلی تبدیل می‌شود
* زبان اسمبلی: یکی از زبان‌های سطح پایین محسوب می‌شود که در آن ما معمولاً مستقیماً با رجیسترهای پردازنده درگیر هستیم(عملیات ریاضی و منطقی از طریق کار روی رجیسترها)
* معمولاً فایل‌های تبدیل شده به فایل اسمبلی دارای پسوند “s.” هستند.


* gcc -S [Name of Source Code] -o [Name of Output file]

`gcc -S metech2.c -o assembled.s` # as -o hello.o hello.s → The assembler (as.exe) converts the assembly code into machine code

# 3️⃣️:CreatingObjectFile[تبدیل کداسمبلی به زبان‌ماشین]

* Object fileها:
    * کدهای صفر و یک هستند که توسط پردازنده قابل‌فهم و اجراست.(دستورالعمل اجرایی پردازنده)
    * فایل object نتیجه کامپایل یک فایل منبع (مانند main.c) است بدون اینکه لینک شده باشد
    * معمولاً Object File ها دارای پسوند “o.” هستند.
    * نمی‌توان به‌صورت یک فایل متنی باز کرد
    * برای دیدن محتوای Object file از دستور objdump استفاده نمایید
    * داخل آن مجموعه سری کد به فرمت هگز می‌باشد
* یکی از راه‌های Close source کردن کد ، تبدیل آن به یک Object file است که عملاً قابلیت تغییر ندارد
* در این مرحله کد اسمبلی به کد زبان ماشین(Object file) تبدیل می‌شود

## Commands

`gcc -c [Name of Source Code] -o [Name of Output file]`
`gcc -c metech2.c -o ObjectFile.o`

برای دیس‌اسمبل کردن (Disassemble) یک فایل اُبجِکت (Object File)
`objdump [Option] [File] `

* [-D]:  تبدیل کد ماشین به اسمبلی
    * تمام بخش‌های قابل اجرا و داده‌های کد ماشین را دیس‌اسمبل کند
    * `objdump -D ObjectFile.o`

```shell
make install  #کپی فایل‌های کامپایل شده در مسیرهای درست
nm ObjectFile.so # مشاهده توابع داخل یک آبجکت فایل
```

## Create ObjectFile.so

**مرحله اول:** یک فایل با پسوند سی ایجاد نمایید که حاوی کد زبان سی باشد

cat `libhello.c`

```c
#include <stdio.h>

void say_hello() {
    printf("Hello from .so file!\n");
}
```

**مرحله‌دوم:** تبدیل به آبحکت‌فایل

```shell
gcc -shared -fPIC -o libhello.so libhello.c
```

**مرحله‌سوم:** استفاده در برنامه

```shell
gcc main.c -o app -L. -lhello
```

**مرحله‌چهارم:**

```shell
./app
# output: Hello from .so file!
```

# 4️⃣️:Linker[لینک‌کردن]

* لینک کردن فرآیند ترکیب چندین فایل object و کتابخانه‌ها (libraries) برای ایجاد یک فایل اجرایی (executable)، کتابخانه به اشتراک گذاری شده (shared library) یا کتابخانه استاتیک (static library) است.
* دو نوع لینک کردن داریم:
    * ۱-نوع Static Linking: تمام کُد (از جمله کتابخانه‌ها) در زمان لینک به فایل executable اضافه می‌شود. فایل بزرگ‌تر ولی مستقل
    * ۲-نوع Dynamic Linking: کتابخانه‌ها در زمان اجرا بارگذاری می‌شوند. فایل کوچک‌تر و به اشتراک‌گذاری کتابخانه‌ها ممکن است
* تجمیع فایل‌های مستقل کنار هم که بعضا با هم ارتباط دارند(همانند includeهایی که در کد سبب فراخوانی یک فایل دیگر می‌شود)
* لینکر یک مرحله ضروری در کامپایل است و فایل object تنها نیمی از کار است و بدون لینک کردن با کتابخانه‌ها،نمی‌توان یک برنامه کامل و اجراپذیر ساخت.

## Commands

در عمل، مردم اغلب مستقیماً از gcc برای لینک کردن استفاده می‌کنند، چون gcc خودش می‌داند چه کتابخانه‌ها و فایل‌های اولیه‌سازی را باید به ld بدهد و نیاز نیست مانند دستور ld آن را مستقیمان وارد نماییم

`ld -o hello.exe hello.o ...libraries...` #the linker (ld or ld.exe) links the object code with the library code to produce an executable file hello.exe

* این برنامه `ld` است که فایل‌های object (مثل hello.o) و کتابخانه‌ها (مثل libc.a) را با هم ترکیب می‌کند و یک فایل اجرایی می‌سازد.
* عبارت `libraries`  را باید وارد نماییم یعنی کتابخانه‌های لازم (مانند libc.a یا libm.so) را هم به لینکر بدهیم.



## example1


  فرض کنید شما یک فایل C دارید به نام hello.c:

```c
#include <stdio.h>

int main() {
    printf("Hello, world!\n");
    return 0;
}
```

* دو دستور زیر یکسان‌هستند و دستور gcc خودش کارهای ld را نیز انجام می‌دهد

```shell
gcc -o hello.exe hello.o
```

```shell
gcc -c hello.c -o hello.o # کامپایل بدون لینک (فقط تولید فایل آبجکت)
ld -o hello.exe hello.o /usr/lib/x86_64-linux-gnu/crt0.o -lc # لینک کردن با کتابخانه‌ها
./hello.exe # اجرای برنامه
# output: Hello, world!
```
نکته‌ها:
* بخش /usr/lib/.../crt0.o: فایل اولیه‌سازی برنامه
* بخش -lc: کتابخانه استاندارد C (libc.a)



## example2
فرض کنید دو فایل داریم:فایل‌اول `main.c` که شامل تابع main و فایل‌دوم `helper.c`که شامل تابع addاست

Filename: `main.c`

```c
#include <stdio.h>

int add(int a, int b); // تعریف در helper.c

int main() {
    printf("Sum: %d\n", add(5, 7));
    return 0;
}
```

Filename: `helper.c`

```c
int add(int a, int b) {
    return a + b;
}
```

```shell
# کامپایل هر فایل به صورت جداگانه
gcc -c main.c -o main.o
gcc -c helper.c -o helper.o
```

```shell
gcc main.o helper.o -o program # لینک کردن آبجکت‌فایل‌ها
```

```shell
./program # اجرای برنامه
# output: Sum: 12
```

# Images

![installSteps.jpg](../Files-SourceFiles/Images/install.jpg "installSteps.jpg")
<br>
![Linker.jpg](../Files-SourceFiles/Images/Linker.jpg "Linker")
<br>
![compilation.jpg](../Files-SourceFiles/Images/compilation.jpg "compilation.jpg")
<br>
![CompilePhase.jpg](../Files-SourceFiles/Images/CompilePhase.jpg "CompilePhase.jpg")
