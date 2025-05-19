numbers = [1, 2, 3, 4, 5, 6]

# numbers.reverse() #در لیست تغییر ایجاد میکند

print(f"reversed in [{numbers}] ---> {list(reversed(numbers))}")

chars = "hello"
print(f"reversed in {chars} ---> {list(reversed(chars))}")
print(f"reversed in {chars} ---> {chars[::-1]}")

nameRes = ''
print(nameRes.join(list(reversed("hello"))))

for num in reversed(range(0, 10)):
    print(num)
print("----")
for num in range(9, -1, -1):
    print(num)
