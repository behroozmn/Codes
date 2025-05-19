# print(test)
# None = 1

# raise IndexError('throw index error')
# raise ValueError('invalid value')


def print_with_custom_color(text, color):
    colors = ('red', 'green', 'blue')
    if type(text) is not str:
        raise TypeError("text must be a string")
    elif color not in colors:
        raise ValueError(f"{color} is not in colors")
    else:
        print(f"printed {text} in {color}")


print_with_custom_color("Behrooz", 'red')
print_with_custom_color(2, 'red')
print_with_custom_color("Behrooz", 'redd')
