# List       → []
# Dictionary → { key1: value1, key2: value2 }
# Set        → {} 1-All Items must be uniq (No repeat)
#                 2-without sort
#                 3-without index #اندیس ناپذیر
#                 4-without call # نمی‌توانیم فراخوانی داشته باشیم
#
# Tuple      → () 1-Items cannot change(immutable)


class SetClass:
    _set1 = {3, 5, 't', 'z', 2, 7, 1, 1, 1, 5, 5, 5, 5}
    _set2 = {"ali", "milad", "mohammad", "sara"}
    _set3 = {"mohammad", "ahmad", "reza", "ali"}
    _set4 = {x ** 2 for x in range(20)}
    _set5 = {char for char in "Behrooz Mohammadi Nasab Sahzabi"}

    def showData(self):
        for item in self._set1:
            print(item)
        print(self._set1)

    def functions(self, mySet):
        mySet.add(8)

        if 4 in mySet:
            mySet.remove(2)

        mySet.discard(4)  # اگر عدد بود آن را پاک میکند و اگر نبود ارور نمیدهد و دستور بدون ارور رد می‌شود
        print(mySet)


behrooz = SetClass()

behrooz.showData()

behrooz.functions(SetClass._set1)

print(SetClass._set2 | SetClass._set3)  # {'ahmad', 'mohammad', 'reza', 'milad', 'sara', 'ali'}  # نمایش اجتماع بدون تکرار

print(SetClass._set2 & SetClass._set3)  # {'ali', 'mohammad'}  #نمایش اشتراک بدون تکرار

print(SetClass._set4)

print(SetClass._set5)
