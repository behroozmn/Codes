#!/usr/bin/env python

# for
#     for variable in iterable:
#         Code
#
#
# for variable in iterable:
#     if condition1:
#         # کد برای condition1
#         if condition2:
#             # کد برای condition2
#         else:
#             # کد برای حالت دیگر condition2
#     else:
#         # کد برای حالت دیگر condition1


class loop:

    def forLoop1(self):
        listOfNumbers = [23, 54, 67, 89, 34, 9]
        for number in listOfNumbers:
            print(number * 2)

    def forLoop2(self):
        [print(x) for x in [1, 2, 3, 4, 5, 6, 11]]

    def forLoop3(self):
        for num in range(1, 10):
            if num % 2 == 1:
                for star in range(1, 6):  # [1, 2, 3, 4, 5]
                    print("*" * star)
            else:
                for star in range(5, 0, -1):  # [5, 4, 3, 2, 1]
                    print("*" * star)

    def whileLoop1(self):
        password = input("what is your password : ")
        while password != "1234":
            print("your password is wrong!!!")
            password = input("what is your password : ")
            print("your password is correct !!!!")

    def whileLoop2(self):
        num = 1
        while num < 30:
            # if(num == 5):
            #     break

            print("\U0001f600" * num)
            print("*" * num)
            num += 1


behrooz = loop()
# behrooz.forLoop1()
# behrooz.forLoop2()
# behrooz.forLoop3()
# behrooz.whileLoop1()
behrooz.whileLoop2()
