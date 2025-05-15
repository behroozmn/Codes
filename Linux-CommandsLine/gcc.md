* عبارت GCC مخفف GNU Compiler Collection می‌باشد
* توسط ریچارد استالمن توسعه داده شده است
* کامپایلر Clang که بر مبنای پروژه LLVM توسعه داده شده و بسیار شبیه به کامپایلر GCC است.
* کامپایلر MSVS که مخفف MicroSoft Visual Studio هست و توسط مایکروسافت توسعه داده شده است.
* کامپایلر GCC در سیستم‌عامل‌هایی که کرنل آنها بر مبنای UNIX نوشته شده باشد(مثل لینوکس یا مک) عملکرد بهتری دارد و عملکرد gcc در ویندوز کندتر هست
* `sudo apt install gcc`: نصب کامپایلر جی‌سی‌سی

**CommandSyntax:** gcc Options Files

# options:

* [-o Output]: ایجاد فایل باینتری خروجی
* [-D<NameofConstant>=Value]: بجای تعریف ثابت‌ها تحت عنوان «دیفاین» مقادیر را درهنگام کامپایل مقدار دهی کرد
    * gcc -D<NameOfConstant>=Value NameOfSourceCode -o NameOfOutputFile]
* [-S outFile.c]: specifies to produce assembly code, instead of object code
    * ایجاد یک «فایل‌اسمبلی» (که حاوی کداسمبلی است) بجای ایجاد «آبجکت‌فایل» توسط کامپایلر
    * gcc -S metech2.c -o assembled.s

```shell
gcc main.c -o outpu_bin_file
```

# Environment Variables

[//]: # (Todo: Need to Review)
GCC uses the following environment variables:

* **PATH**: For searching the executables and run-time shared libraries (.dll, .so)
* **CPATH**: For searching the include-paths for headers.
    * It is searched after paths specified in -I<dir> options.
    * `C_INCLUDE_PATH` and `CPLUS_INCLUDE_PATH` can be used to specify C and C++ headers if the particular language was indicated in pre-processing
* **LIBRARY_PATH**: For searching library-paths for link libraries.
    * It is searched after paths specified in -L<dir> options.
