# درصورت استفاده از همه موارد ترتیب اولیت استفاده به شکل زیر است:
# اول: parameters
# دوم: *args
# سوم: default parameters
# چهارم: **kwargs

# Args: اگر در آرگومان ورودی موارد زیر را دیدید
#      *args => Tuple
#      **kwargs => Dictionary

class Functions:
    def func1(self, num, power=2):
        print(f"func1: {num ** power}")

    def func2(self, first, last):
        print(f"func2: {first} {last}")

    # تبدیل می‌شود به یک تاپل
    def func3_holico(self, *args):
        total = 0
        for num in args:
            total += num
        print(f"func3: {args}------> {total}")

    # آرگومان ورودی تبدیل می‌شود به یک دیکشنری
    def func4(self, **kwargs):
        my_string = ""
        for key, value in kwargs.items():
            my_string = f"{my_string} {key}:{value} - "
        print(f"func4: {my_string}")

    def func5(self, a, b, *args, define_parameter="defalut", **kwargs):
        print(f"func5: {a}, {b} {args}, {define_parameter}, {kwargs}")


behrooz = Functions()

behrooz.func1(2, 3)  # output:8
behrooz.func1(3)  # output:9

behrooz.func2("behrooz", "mohammad")
behrooz.func2(last="mohammad", first="behrooz")

person = {"first": "behrooz", "last": "Mohamadi"}
behrooz.func2(**person)
behrooz.func2(*person)

behrooz.func3_holico(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

numbers = [1, 2, 3, 4, 5, 6] #لیست است و میخواهیم بعنوان آرگومان ورودی به تابع بدهیم
behrooz.func3_holico(*numbers)  # اگر ستاره نباشد ارور میدهد

behrooz.func4(name="behrooz", FamilyName="Mohammadi")
behrooz.func4(name="behrooz", FamilyName="Mohammadi", born=1369, mobile="09191671085")

behrooz.func5(1, 2, 6, first_name="Behrooz", last_name="MohamadiNasab")
