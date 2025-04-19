# List       → []
# Dictionary → { key1: value1, key2: value2 }
# Set        → {} 1-All Items must be uniq (No repeat)
#                 2-without sort
#                 3-without index #اندیس ناپذیر
#                 4-without call # نمی‌توانیم فراخوانی داشته باشیم
#
# Tuple      → () 1-Items cannot change(immutable)

class DictionaryClass:
    Dic1 = {
        "name": "Behrooz",
        "family": "Mohammadi Nasab",
        "age": 31
    }

    Dic2 = {
        "mobile": "09191671085"
    }

    Dic3 = dict(first=1, second=2, third=3)

    Dic4 = {num: num for num in [1, 2, 3, 4, 5]}  # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

    Dic5 = {key: value ** 2 for key, value in Dic3.items()}  # {'first': 1, 'second': 4, 'third': 9}

    _Dic6 = {num: ("even" if num % 2 == 0 else "odd")  # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
             for num in [1, 2, 3, 4, 5]}

    __Dic7 = {num: num ** num for num in [1, 2, 3, 4, 5]}

    def __init__(self) -> None:
        pass

    def showValue(self):
        print(DictionaryClass.Dic1["name"])  # Behrooz
        print(DictionaryClass.Dic1["family"])  # MohammadiNasab
        print(DictionaryClass.Dic1["age"])  # 31
        # dict_values(['Behrooz', 'MohammadiNasab', 31])
        print(DictionaryClass.Dic1.values())
        print(DictionaryClass.Dic1.keys())  # dict_keys(['name', 'family', 'age'])

    def returnValue(self):
        return DictionaryClass.Dic1.get("name"), DictionaryClass.Dic1["family"], DictionaryClass.Dic1["age"]

    def printValuesByFor(self):
        for value in DictionaryClass.Dic1.values():
            print(value)

    def printKeysByFor(self):
        for key in DictionaryClass.Dic1.keys():
            print(DictionaryClass.Dic1[key])

    def printKeyValuesByFor(self):
        for key, value in DictionaryClass.Dic1.items():
            print(f"{key}: --> {value}")

    def printAll(self):
        print(DictionaryClass.Dic1)

    def isExist(self, x):
        if x in DictionaryClass.Dic1:
            print(DictionaryClass.Dic1[x])
        else:
            print(f"there is no {x} key in me")

    def clearData(self):
        DictionaryClass.Dic1.clear()

    def copyData(self):
        two = DictionaryClass.Dic1.copy()  # یک دیکشنری را دقیقا در دیگری می‌ریزد یعنی کپی میکند
        return two

    def popData(self):
        # one.pop("name") #کلید و مقدار را باهم پاک میکند
        # or
        # مقدار را اول داخل متغیر میریزد و سپس از دیکشنری حذف میکد
        result = DictionaryClass.Dic1.pop("name")

    def popLastItem(self):
        DictionaryClass.Dic1.popitem()  # آخرین کلید و مقدار را حذف میکند

    def concatenateDictionary(self):
        DictionaryClass.Dic1.update(DictionaryClass.Dic2)  # دیکشنری را به دیکنشری موجود می‌افراید

    # آرگومان ورودی تبدیل می‌شود به یک دیکشنری
    def func4(self, **kwargs):
        my_string = ""
        for key, value in kwargs.items():
            my_string = f"{my_string} {key}:{value} - "
        print(f"func4: {my_string}")


behrooz = DictionaryClass()
# behrooz.printValuesByFor()
# behrooz.printKeysByFor()
# behrooz.printKeyValuesByFor()
# behrooz.isExist("name")
# behrooz.clearData()

# print(behrooz.copyData().get("age"))
# print(behrooz.copyData() == one)
# print(behrooz.copyData() is one)

# behrooz.popLastItem()
# behrooz.printKeyValuesByFor()

# behrooz.concatenateDictionary()
# behrooz.printKeyValuesByFor()

# value1, value2, value3 = behrooz.returnValue()
# print(f"name:{value1}\n\nfamily:{value2}\n\nage:{value3}")

behrooz.printAll()

behrooz.func4(name="behrooz")
behrooz.func4(name="behrooz", FamilyName="Mohammadi")
behrooz.func4(name="behrooz", FamilyName="Mohammadi", born=1369, mobile="09191671085")