# `__NAME__`

## 1.`__init__`

نقش تابع سازنده در هر کلاس را ایفا می‌کند

```python
class User:
    def __init__(self, name, age):  # تابع سازنده
        self.name = name
        self.age = age

    def show_data(self):
        print(self.name, self.age)


obj = User("behrooz", 33)
obj.show_data()

```

## 2. `__len__`

فقط زمانی می‌شود از این تابع استفاده کرد که فانکشن آن تعریف شده باشد یا خودمان یا ارث‌بری

```python
class Behrooz:
    def __init__(self, _name):
        self.name = _name

    def __len__(self):
        return 20


obj = Behrooz("Alii")
print(len(obj))
```

## 3. `__add__` و `__mul__` و `__truediv__` و `__sub__`

```python
class Behrooz:
    def __init__(self, _name):
        self.name = _name

    # بجای عملگر  + استفاده می‌شود
    def __add__(self, other):
        return f"Need to plus with {self.name} or {other}"

    # بجای عملگر *استفاده می‌شود
    def __mul__(self, other):
        return f"Need to multiplier with {self.name} or {other}"

    # بجای عملگر / استفاده می‌شود
    def __truediv__(self, other):
        return f"Need to division with {self.name} or {other}"

    # بجای عملگر - استفاده می‌شود
    def __sub__(self, other):
        return f"Need to minus with {self.name} or {other}"


obj = Behrooz("Alii")

print(obj)
print(obj + "salam")
print(obj - "salam")
print(obj * "salam")
print(obj / "salam")

```

| Function               | Oprator |
|------------------------|---------|
| __isub__(self,p2)      | -=      | 
| __imul__(self,p2)      | *=      | 
| __itruediv__(self,p2)  | \=      | 
| __floordiv__(self,p2)  | \\      | 
| __ifloordiv__(self,p2) | \=      | 

## 4.`__repr__`

باتعریف این تابع سبب می‌شویم در هنگام پرینت آبجکت تهیه شده از یک کلاس تابع اجرا شود وگرنه آدرس شیء در حافظه نمایش می‌شود\
یعنی اگر بخواهیم که بچای نمایش دیتای فنی دیتای خوانا به کاربر نمایش داده شود

```python
class Behrooz:
    def __init__(self, _name):
        self.name = _name

    def __repr__(self) -> str:
        return f"behroooz class attribute is [{self.name}]"


obj = Behrooz("Alii")
print(obj)


```