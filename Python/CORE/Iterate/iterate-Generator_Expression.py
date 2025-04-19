# Generator: create function as sequentional lazy items
#        --> create or generate items only when ussing
#        --> Generate values incrementally when need
#        --> Note: اگر کار با دیتای زیادی صورت می‌گیرد بهتر است از  جنریتور استفاده شود
#        --> Note: دیتا یکباره لود نمی‌شود و یک به یک انجام می‌شود
#        --> Note: روشی برای ایجاد ایتریتور
#        --> Note: اگر دستورات را داخل یک پرانتز قرار بدهیم(در مثال تصریح شده است)
#        --> Note: بطور پیش‌فرض ایتریتور هستند و نیاز به تعریف تابع نکست ندارند
#        --> Note: اگر یک ماژول یک جنریتور برگرداند آنگاه ناگزیر باید روی آن پیمایش کرد تا به محتوی آن دست یافت
# yield:
#    ------> Note: وضعیت تابع(شامل مقادیر متغیرها و موقعیت اجرای تابع) حفظ می‌شود
#    ------> Note:  قابلیت ادامه تابع از همان نقطه توقف
#    ------> Note:  عدم محاسبه و برگرداندن یکباره تمام مقادیر بلکه محاسبه و تولیدیکی پس از دیگری


print("#########################")
print("### Example1: yield #####")
print("#########################")


def nums():
    for num in range(20):
        yield num


g = nums()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print("##########################")
print("### Example1: ()     #####")
print("##########################")
myGenerator = (num for num in range(20))
print(myGenerator)
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))

print("#########################")
print("### Example2: yield #####")
print("#########################")


def func_generator(maximom):
    count = 1
    while count <= maximom:
        yield count
        count += 1


counter = func_generator(3)  # استفاده از حالت جنریتور
print(next(counter))  # -> 1
print(next(counter))  # -> 2
print(next(counter))  # -> 3
# print(next(counter))  # if run error

print("#############################")
print("### Example3: فیبوناتچی #####")  # 0,1,1,2,3,5,8,13,21,...
print("#############################")

print("--------------------byList----------------------")


def fib_list(maximom):  # 10
    numbers = []  # [1,1]
    a, b = 0, 1
    while len(numbers) <= maximom:
        numbers.append(b)
        a, b = b, a + b
    return numbers


print(f"By List ===> {fib_list(10)}")
for num in fib_list(10):
    print(f"------> {num}")


def fib_generator(maximom):
    count = 0
    a, b = 0, 1

    while count < maximom:
        a, b = b, a + b
        yield b
        count += 1


print("-----------------byGenerator--------------------")

print(f"By Generator ===> {fib_list(10)}")
for num in fib_generator(10):  # استفاده از حالت جنریتور
    print(f"------> {num}")

print("##################")
print("### Example4 #####")
print("##################")
from time import time

start_time = time()
print(f"byGenerator: {sum(num for num in range(100000000))}")  # --> GeneratorExprerssion
end_time = time()
print(f"--------->  Time(s): {end_time - start_time}")

start_time = time()
print(f"ussing list: {sum([num for num in range(100000000)])}")  # Not GeneratorExprerssion, only send list to sum function
end_time = time()
print(f"---------->  Time(s): {end_time - start_time}\n")
