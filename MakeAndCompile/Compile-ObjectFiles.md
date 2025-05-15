# Create ObjectFile.so

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