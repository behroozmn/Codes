users = [{'name': 'Behrooz', 'family': 'nadery', 'born': 1369, 'shopCart': []},
         {'name': 'Alireza', 'family': 'saberi', 'born': 1400, 'shopCart': []},
         {'name': 'Attefeh', 'family': 'Rezaie', 'born': 1372, 'shopCart': ['kotlin', 'vue']}]


def func1():
    print(f"func1:{len(users)}")


def func2():
    result = filter(lambda user: len(user['shopCart']) == 0, users)
    print(f"func2(filter):{list(result)}")


func1()
func2()
