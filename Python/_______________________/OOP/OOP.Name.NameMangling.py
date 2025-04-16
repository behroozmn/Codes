# _name    => define local variable
#             Note: در پایتون هیچ قلمرویی تحت عنوان پرایویت نداریم
#             Note: استفاده از یک آندرلاین قبل متغیر تنها یک قرارداد است ولی باز در هرکجا به پرایویت می‌توان دسترسی داشت

# __name   => name mangling: available only with _classname__variable in use time
#             Note: در پایتون همه نامگذاری‌ها قراردادی است ولی تنها نِیم‌مَنگِلینگ است که سبب تغییر در نام آیتم می‌شود

# __name__ => in python special function define in this form such as __init__ as construction



class User:
    _mobile = "09191671085"  # بعنوان پیشنهاد در لیست intelliSence نمایش داده نمی‌شود و تلویحاً بعنوان متغیر محلی تلفی‌می‌شود
    __password = "myPassword"  # Generally __password is not available. only available by _User__password

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def get_mobile(self):
        return self._mobile


obj = User("behrooz", 33)
print(obj.name)
print("☓️:" + obj._mobile)  # استفاده از پارامتر محلی داخل یک کلاس بصورت مستقیم توصیه نمی‌شود
print("✓:" + obj.get_mobile)
print(obj._User__password)  # وقتی یک پارامتر را با دوتا آندرلاین تعریف کنیم و توسط شکل فوق به آن دسترسی داشته باشیم را nameMangling می‌گویند