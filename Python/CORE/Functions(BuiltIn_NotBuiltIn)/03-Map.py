# map: calls a function for all its members of iterable
#    ---> Syntax: map(function, iterable) ==> Return: an iterable mapObject
#                                         ==> Ussing: list(mapObject) or Tuple(mapObject) or ...
#    ---> Note: تنها یکبار روی لیست یا غیره می‌تواند پیمایش صورت بپذیرد و در پیمایش دوم با لیست خالی مواجه می‌شود
#    ---> itarate: پیمایش
#    ---> iterable: هر چیزی که روی آیتم‌های آن قابلیت پیمایش وچود داشته باشد
#    ---> Note:  به صورت «لِیزی» عمل می‌کند، به این معنی که محاسبات تنها زمانی انجام می‌شود که به نتایج آن نیاز باشد


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["akbar", "natasha", "zeinab", "maryam", "Kobra"]
users = [{'name': 'amirali', 'family': 'ojaghi', 'born': 1369, 'shopCart': []},
         {'name': 'mahmood', 'family': 'sabeti', 'born': 1400, 'shopCart': []},
         {'name': 'hossein', 'family': 'taheri', 'born': 1372, 'shopCart': ['kotlin', 'vue']}]


def func1():
    def square(x):
        return x ** 2

    squared_numbers = map(square, numbers)
    # Alternatives: squared_numbers = map(lambda x: x ** 2, numbers)

    # تبدیل به لیست
    squared_list = list(squared_numbers)
    print(squared_list)  # خروجی: [1, 4, 9, 16, 25]


def func2_map_filter():
    result_user = filter(lambda user: not user['shopCart'], users)
    result_user_name = lambda user: user['name']
    result = map(result_user_name, result_user)
    # ALTERNATIVE =====> result = [user['name'] for user in users if len(user['shopCart']) == 0]
    print(f"func4(filterAndMap):{list(result)}")


def func3():
    upper_names = map(lambda name: name.upper(), names)
    print(f"func5{list(upper_names)}")
    print(f"func5(خالی خواهد بود زیرا یک بار پیمایش شده است){list(upper_names)}")  # خالی خواهد بود زیرا پیمایش سبب تخلیه می‌گردد


def func4():
    result = map(lambda person: person['family'], users)
    print(f"func3:{list(result)}")
    # Alternatives:
    #           families = []
    #           for person in users: families.append(person['family'])
    #           print(f"{families}")


def func5():
    def add(x, y):
        return x + y

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    added_numbers = map(add, list1, list2)
    # ALTERNATIVE =====> added_numbers = map(lambda x, y: x + y, list1, list2)

    # تبدیل به لیست
    result_list = list(added_numbers)
    print(result_list)  # خروجی: [5, 7, 9]


func1()
print()
func2_map_filter()
print()

func3()
print()

func4()
print()

func5()
