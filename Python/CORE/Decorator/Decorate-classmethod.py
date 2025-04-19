# decorator
# تغییر عملکرد یک تابع بطوریکه بجای استفاده از منابع نمونه از منابع کلاس استفاده می‌کند
# دسترسی مستقیم به دیتای کلاس بدون ساخت شیء نمونه

class User:
    activeUsers = 0

    @classmethod
    def func1(cls):
        return cls.activeUsers


print("روش اول: بدون نیاز ساخت شیء از کلاس")
print(User.func1())

print("روش دوم:  الزام بر ساختن شیء از کلاس")

obj1 = User()
print(obj1.func1())
