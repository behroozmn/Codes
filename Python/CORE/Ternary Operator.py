# ternary:A ternary operator exists in some programming languages, and it allows you to shorten a simple If-Else block. It takes in 3 or more operands:
#  syntax: [value_if_true] if [condition] else [value_if_false]
#               │                  │              │
#               │                  │              └──> A value that's returned if the condition evaluates to False.
#               │                  │
#               │                  └─> A boolean condition that has to be satisfied to return value if true.
#               │
#               └──> A value that's returned if the condition evaluates to True.

def condition1():
    a, b = 10, 20
    min = a if a < b else b
    print(min)


def condition2():
    age = 17
    outcome = 'Go home.' if age < 16 else 'Not sure...' if 16 <= age < 18 else 'Welcome'
    print(outcome)


def condition3():
    a, b = 100, 20
    print((b, a)[a < b])


def condition4():
    a, b = 10, 20
    print((lambda: b, lambda: a)[a < b]())


def condition5():
    a, b = 10, 20
    print("Both a and b are equal" if a == b else "a is greater than b"
    if a > b else "b is greater than a")


def condition5_Alternative():
    a, b = 10, 20
    if a != b:
        if a > b:
            print("a is greater than b")
        else:
            print("b is greater than a")
    else:
        print("Both a and b are equal")


def condition6():
    a, b = 5, 7
    print(a, "is greater") if (a > b) else print(b, "is Greater")


# ⇉ a if condition  else b
condition1()
condition6()

print("---------Step 2------------")
# ⇉ a if condition1 else b if condition2 else c
condition2()

# ⇉ print({True: a, False: b} [a < b])
condition3()

# ⇉ Lambda
condition4()

# ⇉ nested ternary operator
condition5()
condition5_Alternative()
