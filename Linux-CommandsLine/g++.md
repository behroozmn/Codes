Syntax: g++ [options] [files]

# options:

* [-o]: specifies the output executable filename.
* [-g]: generates additional symbolic debuggging information for use with gdb debugger.
* [-Wall]: prints "all" warning messages. نمایش تمام هشدار ها

# Examples

```shell
g++ -o myCode.exe file.cpp  # تک فایل
g++ -o myCode file1.cpp file2.cpp # چند فایل
g++ -c file1.cpp && g++ -c file2.cpp  &&   g++ -o myprog.exe file1.o file2.o # چند فایل
```
