#Return Boolean Value
number_1 = -100
number_2 = -200
# == : returns true if the value of number_1 is equal to number_2
print(f'{number_1} == {number_2} : { number_1 == number_2 }')
# != : returns true if the value of number_1 is not equal to number_2
print(f'{number_1} != {number_2} : { number_1 != number_2 }')
# > : returns true if the value of number_1 is greater than number_2
print(f'{number_1} > {number_2} : { number_1 > number_2 }')
# >= : = or >
print(f'{number_1} >= {number_2} : { number_1 >= number_2 }')
# < : returns true if the value of number_1 is less than number_2
print(f'{number_1} < {number_2} : { number_1 < number_2 }')
# <= : = or <
print(f'{number_1} <= {number_2} : { number_1 <= number_2 }')



# is → check By ماهیت و مقدار
# == → check By مقدار
list1 = ['a', 'b', 'c']
list2 = list1
list3 = list(list1)
print(list1)
print(list2)
print(list3)
print(list1 == list2)
print(list1 == list3)
print(list1 is list2)
print(list1 is list3)