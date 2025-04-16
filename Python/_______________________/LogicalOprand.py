# AND
print("---------AND----------")

print(f"True and True : { True and True }")
print(f"False and True : { False and True }")
print(f"True and False : { True and False }")
print(f"False and False : { False and False }")

userAge = 17
userGender = "female"
if userAge >= 18 and userGender == "male":
    print("you have to go to soldiery")
else:
    print("you can stay at home")


# OR
print("---------OR----------")
print(f"True or True : { True or True }")
print(f"False or True : { False or True }")
print(f"True or False : { True or False }")
print(f"False or False : { False or False }")

weather = "sunny"
if weather == "sunny" or weather == "cloudy":
    print("we can travel")
else:
    print("we can not travel")


# NOT
print("--------NOT-----------")
print(f"not True : { not True }")
print(f"not False : { not False }")

isBrotherComming = False
if not isBrotherComming:
    print("my sister said : i wont come")

# Combine
print("-------Combine------------")
age = 50
if (0 <= age <= 2) or (8 <= age < 65):
    print("you should pay 10 dollars")
if not ((2 < age < 8) or age >= 65):
    print("you should pay 10 dollars")