# import random
# import random as rand
# from random import *
# from random import randint, choice
# from random import randint as r_i, choice as r_ch

# vsCode--> python: select interpreter #تغییر در ورژن‌های پایتون در ویژوآل استودیو کد
# encapsulation: توابع و متغیرها و موارد را در یک کلاس قرار بدهیم
# __name__ --> name of the module(file)


class User:
    def __init__(self, name, age):  # تابع سازنده
        self.name = name
        self.age = age

    def show_data(self):
        print(self.name, self.age)


obj = User("behrooz", 33)
obj.show_data()
print("آیا شیء یک نمونه از کلاس است؟", isinstance(obj, User))
