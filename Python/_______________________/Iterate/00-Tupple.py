# List       → []
# Dictionary → { key1: value1, key2: value2 }
# Set        → {} 1-All Items must be uniq (No repeat)
#                 2-without sort
#                 3-without index #اندیس ناپذیر
#                 4-without call # نمی‌توانیم فراخوانی داشته باشیم
#
# Tuple      → () 1-Items cannot change(immutable)


class TuppleClass:
    _tuple1_1to50 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50)
    _tuple2 = (1, 2, 2, 3, 4, 5, 2, (4, 5, 3), 3, 3)  # immutable list
    _tuple3 = (1, 2, {2}, (3, 4), [2, 5], 2, (4, 5, 3), 3, 3)
    _tuple4 = tuple([1, 2, 3, 4, 5])

    def show_tuple_withfor(self, localtuple=_tuple2):
        for num in localtuple:
            print(num)

    # آرگومان ورودی تبدیل می‌شود به یک تاپل
    def func1(self, *args):
        total = 0
        for num in args:
            total += num
        print(f"func3: {args}------> {total}")


obj = TuppleClass()
obj.show_tuple_withfor()

obj.func1(1, 2, 3, 4)
obj.func1(12)

numbers = [1, 2, 3, 4, 5, 6]  # لیست است و میخواهیم بعنوان آرگومان ورودی به تابع بدهیم
obj.func1(*numbers)  # اگر ستاره نباشد ارور میدهد
