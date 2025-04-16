# Only in one line
# lambda is one type of function definition
# Second name of lambda is "Annonymous function"
# Syntax is:
#     lambda arg1, arg2: arg1 * arg2 + 10
#     lambda arg1      : value_if_true if condition  else  value_if_false
#     lambda arg1      : value_if_true if condition1 else  (value_if_true2 if condition2 else value_if_false)

function1 = lambda arg1, arg2: arg1 * arg2 + 10  # !!!!!!!!! don't use [CTRL+Shift+i]
print(function1(5, 2))

function2 = lambda x: "Positive" if x > 0 else ("Zero" if x == 0 else "Negative")
print(function2(-5))

