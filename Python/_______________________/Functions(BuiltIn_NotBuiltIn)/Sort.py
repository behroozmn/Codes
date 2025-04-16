
def func2sort_NoChange():
    numbers = [1, 5, 8, 4, 6, 2]
    print(f"func2(befor): {list(numbers)}")
    result = sorted(numbers, reverse=False)
    print(f"func2(sorted result): {result}")
    print(f"func2(after): {list(numbers)}")


def func4sort_Change():
    numbers = [1, 5, 8, 4, 6, 2]
    print(f"func4(befor): {list(numbers)}")
    numbers.sort(reverse=False)
    print(f"func4(after): {list(numbers)}")

# لیست ها برای مرتب سازی نیاز به کلید دارند


def func5():
    users = [
        {'name': 'taha', 'family': 'MohammadiNasab', 'age': 40},
        {'name': 'mohammad', 'family': 'ketabi', 'age': 23},
        {'name': 'sara', 'family': 'nadery', 'age': 80},
        {'name': 'ali', 'family': 'Mohamadi', 'age': 30}
    ]
    print(users)
    print(sorted(users, key=lambda user: user['age'], reverse=False))

func2sort_NoChange()
print("")
func4sort_Change()
print("")
func5()
