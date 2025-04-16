# بررسی درستی یا نادرستی یا همان تروسینس یا فالسینس
# اگر تنها حتی یک آیتم از مواردی که به این تابع داده شده است ترو باشد مقدار ترو را برمی‌گرداند

def func1():
    numbers = [0, 0, 0, 0]
    print(f"{numbers} --> {any(numbers)}")


def func2():
    numbers = [0, 0, 0, 1]
    print(f"{numbers} --> {any(numbers)}")


def func3():
    data = [False, False, False, False]
    print(f"{data} --> {any(data)}")


def func4():
    data = [False, False, False, True]
    print(f"{data} --> {any(data)}")


def func5():
    print(any([]))


def func5():
    numbers = [2, 4, 6, 8]
    result = (any([num % 2 != 0 for num in numbers]))
    print(f"{numbers} --> {result}")


def func6():
    numbers = [2, 4, 6, 7]
    result = (any([num % 2 != 0 for num in numbers]))
    print(f"{numbers} --> {result}")


func1()
func2()
func3()
func4()
func5()
func6()
