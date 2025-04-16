# Decorator
#  => property: convert function to property or attribute such as:
#  =======> getter[getter is func and must ussing by () ,but when use @property, it changed to attribute and () will remove]
#
class behrooz:

    def __init__(self, _name, _family, _age):
        self.name = _name
        self.family = _family
        self.age = _age

    # برای دسترسی به متد باید حتما پرانتز باز و بسته گذاشته بشود ولی وقتی از تابع getter استفاده می‌کنیم با گذاشتن Decorator تحت عنوان  property نباید پرانتز گذاشت
    @property  # اگر پراپرتی را قرار ندهیم آنگاه برای فراخوانی مقدار باید حتما پرانتز باز و بسته رو قرار دهیم
    def age(self):
        return self._age

    # توابعی که Decorator تحت عنوان property و setter قرار دارد سبب می‌شود تا رفتارِ تابع تغییر کند و در حالت متغیر استفاده گردد
    # نکته: کلمه age که در خط زیر است از تابع بالایی که همراه property است آمده است و باید هم‌نام آن باشد
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            self._age = 0

    @property
    def fullName(self):  # تبدیل یک تابع به یک پراپرتی و نه متد
        return f"{self.name} {self.family}"


obj1 = behrooz("behrooz", "MohamadiNasab", -18)
print(obj1.age)  # اگر پراپرتی را در بالای گِتِر متغیر قرار نمی‌دادیم باید در اینجا پرانتز باز و بسته قرار می‌دادیم

obj1.age = 40
print(obj1.age)

obj1.age = -15
print(obj1.age)

obj1.age = 18
print(obj1.age)

print(obj1.fullName) # به حالت متد فراخوانی نمیکنیم بلکه به حالت پراپرتی(خصیصه) فراخوانی می‌کنیم