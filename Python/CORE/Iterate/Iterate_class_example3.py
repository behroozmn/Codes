class User:
    ActiveUsers = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.index = 0
        User.ActiveUsers.append({'name': name, 'age': age})

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(User.ActiveUsers):
            person = User.ActiveUsers[self.index]
            self.index += 1
            return person
        raise StopIteration


person_1 = User('mohammad', 24)
person_2 = User('sara', 20)

print(f"ActiveUsers:{User.ActiveUsers}\n\n")

for item in User('ali', 60):
    print(item)
