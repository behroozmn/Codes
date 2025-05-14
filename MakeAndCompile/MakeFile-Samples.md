# 1.Hello World

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

# 2.makefile sample

```makefile
CC      = gcc
CFLAGS  = -Wall -Wextra -g
CPPFLAGS= -Iinclude
LDFLAGS =
LDLIBS  = -lm

SRCS    = main.c utils.c
OBJS    = $(SRCS:.c=.o)
TARGET  = myprogram

all: $(TARGET)

$(TARGET): $(OBJS)
    $(CC) $(LDFLAGS) $(OBJS) -o $@ $(LDLIBS)

%.o: %.c
    $(CC) $(CFLAGS) $(CPPFLAGS) -c $< -o $@

clean:
    rm -f $(OBJS) $(TARGET)
```


توضیح کوتاه برخی قسمت‌ها:

* مورد $(CC) و $(CFLAGS) و غیره: متغیرها را فراخوانی می‌کنند.
* مورد $(SRCS:.c=.o): تمام .cها را به .o تبدیل می‌کند (مانند main.c → main.o).
* مورد $@: اسم هدف (target) فعلی است (مانند myprogram).
* مورد $<: اولین وابستگی (dependency) است (مانند main.c در حین کامپایل main.o).
     
