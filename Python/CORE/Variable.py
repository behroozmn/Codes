# CaseSensitive
# Can insert many type of data into one variable
# string can use one or double qoute

# MyAge = 23      → upper camel case - Use for Classes

x, y = 400, 500
personChild = None  # None Means EMPTY
BoolData = True  # first char must uppercase

username = "behrooz"
# username = input("Insert username: ")

print(f"the BoolData is {BoolData}")
print("the BoolData is {BoolData}")
print(f"sum is : {x + y}")
print(f"multiply 2 and 6 is : {2 * 6}")
print(username[2])
print("Name: " + username)
print(round(12.2565856, 5))

print(list(range(4, 10)))  # [4, 5, 6, 7, 8, 9]
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]

userRank = 1
print("you got GOLD medal") if userRank == 1 else print("no medal")
