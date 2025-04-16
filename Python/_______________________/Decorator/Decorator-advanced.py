def before_after(func):
    def wrapper():
        print(f"Before={0}")
        func()
        print(f"After={1}")

    return wrapper


print("#########################################")
print("######## روش اول:برگرداندن یک تابع ######")
print("#########################################")


def say_hello():
    print("hello")


tempFunc = before_after(say_hello)
tempFunc()

print("\n##################################")
print("###  Decorator #### 0 Argument ###")
print("##################################")


@before_after
def say_hello():
    print("hello")


say_hello()

print("\n##################################")
print("###  Decorator #### 1 Argument ###")
print("##################################")


# x only sent to wrapper[not sent to num_before_after]
def one_arg_before_after(func):
    def wrapper(x):
        print(f"Before={x - 1}")
        func(x)
        print(f"After={x + 1}")

    return wrapper


@one_arg_before_after
def say_hello(x):
    print(f"----1arg---->hi {x}")
    print(f"----1arg---->hi")


say_hello(256)

print("\n##################################")
print("###  Decorator #### 2 Argument ###")
print("##################################")


def two_args_before_after(func):
    def wrapper(arg1, arg2):
        print(f"Before:      [arg1:{arg1}] - [arg2:{arg2}]")
        func(arg1, arg2)
        print(f"After:       [arg1:{arg1}] - [arg2:{arg2}]")

    return wrapper


@two_args_before_after
def show_name(name, family):
    print(f"---2arg--->  {name} {family}")


show_name('behrooz', 'Mohamadinasab')

print("\n###############################")
print("###  Decorator ##### (*Arg) ###")
print("###############################")


def many_args_before_after(func):
    def wrapper(*args):
        print(f"Before      [{args}]")
        func(args)
        print(f"After       [{args}]")

    return wrapper


@many_args_before_after
def show_data(*args):
    print(f"---*arg---> {args}")


show_data('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address')

print("\n##########################################")
print("###  Decorator with(*Arg and **kwargs) ###")
print("##########################################")


def exec_before_after(func):
    def wrapper(*args, **kwargs):
        print(f"Before      [args:{args}]")
        func(*args, **kwargs)
        print(f"After       [kwargs:{kwargs}]")

    return wrapper


@exec_before_after
def show_data(*args, **kwargs):
    print(f"==========> {args} - {kwargs}")


show_data('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address', Fname="Behi", Lname="Mohamadi")
print("\n\n")
show_data('Behrooz', 'MohamadiNasab', 'phone', 'male', 'address', Fname="Behi")
print("\n\n")
show_data('Behrooz', 'MohamadiNasab', 'phone')
print("\n\n")
show_data( Fname="Behi", Lname="Mohamadi")
print("\n\n")
show_data('male')
print("\n\n")
show_data(Fname="Behi")
