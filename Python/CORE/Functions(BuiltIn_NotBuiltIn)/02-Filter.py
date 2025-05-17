# filter: choice elements by condition
#       ---> Syntax: filter(function, iterable) ==> Return: an IterableObject
#                                               ==> Ussing: list(IterableObject) or Tuple(IterableObject) or ...
#       ---> Filter a iterable by condition(only apply to items which true condition on it) فیلتر روی یک ایتریبل اگر در شرط بگنجد
#       ---> itarate Means پیمایش


numbers = [1, 2, 3, 4, 5, 6]
names = ["akbar", "fatemeh", "zeinab", "maryam", "Kobra"]
users = [{'name': 'Behrooz', 'family': 'nadery', 'born': 1369, 'shopCart': []},
         {'name': 'Alireza', 'family': 'saberi', 'born': 1400, 'shopCart': []},
         {'name': 'Attefeh', 'family': 'Rezaie', 'born': 1372, 'shopCart': ['kotlin', 'vue']}]


def func1_get_even():
    evens = filter(lambda num: num % 2 == 0, numbers)
    print(f"func1:{list(evens)}")


def func3():  # Use with Falsyness Or Trusynes
    result = filter(lambda user: not user['shopCart'], users)  # [not user['shopCart']] OR [len(user['shopCart']) == 0]
    # result = filter(lambda user: len(user['shopCart']) == 0, users)
    print(f"func3(alt):{list(result)}")


def func4_map_filter():
    result_user = filter(lambda user: not user['shopCart'], users)
    result_user_name = lambda user: user['name']
    result = map(result_user_name, result_user)
    # ALTERNATIVE =====> result = [user['name'] for user in users if len(user['shopCart']) == 0]
    print(f"func4(filterAndMap):{list(result)}")


func1_get_even()
print()

func3()
print()

func4_map_filter()
