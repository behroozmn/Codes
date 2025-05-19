# List       → []
# Dictionary → { key1: value1, key2: value2 }
# Set        → {} 1-All Items must be uniq (No repeat)
#                 2-without sort
#                 3-without index #اندیس ناپذیر
#                 4-without call # نمی‌توانیم فراخوانی داشته باشیم
#
# Tuple      → () 1-Items cannot change(immutable)

class ListClass:
    def __init__(self):
        _list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        _list2 = ["Python", True, 5, [4, 5, 6]]
        _list3 = ["red", "blue", "green", "gray", "yellow", "orange", 3.6]
        _list4 = []
        _list5 = [num * 2 for num in _list1]
        _list6 = [char.upper() for char in "behrooz"]
        _list7_even = [num for num in _list1 if num % 2 == 0]
        _list7_odd = [num for num in _list1 if num % 2 != 0]
        _list8 = [num * 2 if num % 2 == 0 else num * 3 for num in _list1]
        _list9 = "BehroozMohammadiNasab"
        _list10_nestedList = [[1, 2, 3], [4, 5, 6]]
        _list11 = [num ** 2 for num in range(1, 11)]

    def getDataAll(self, myList):
        for x in myList:
            print(f"the value is : {x}")

    def getDataAllByCount(self, mylist):
        indexCount = len(mylist)
        index = 0
        while index < indexCount:
            x = mylist[index]
            print(f"the value is : {x}")
            index += 1

    def fill_list(self):
        for num in self._list1:
            self._list4.append(num ** 2)

    def get_alldata_revese(self, mylist):
        mylist.reverse()
        print(mylist)

    def get_select_item(self, mylist):
        # List[start:end:step]

        value1 = mylist[1]  # output: 2
        value2 = mylist[-5:]  # output: [12, 13, 14, 15, 16]
        value3 = mylist[::2]  # output: [1, 3, 5, 7, 9, 11, 13, 15]
        value4 = mylist[0:]  # output: All items [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        value5 = mylist[:]  # output: All items [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        value6 = mylist[::-1]  # List[start:end:step] output: Reverse [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        value7 = mylist[:3]
        print(f"value1:{value1}")
        print(f"value2:{value2}")
        print(f"value3:{value3}")
        print(f"value4:{value4}")
        print(f"value5:{value5}")
        print(mylist == value5)
        print(mylist is value5)
        print(f"value6:{value6}")
        print(f"value7:{value7}")


def list_functions(self, mylist):
    first_item = mylist.pop(0)
    last_item = mylist.pop()
    length = {len(mylist)}
    mylist.extend(["ali", "hassan", "hossein"])
    mylist.append(["alii", "hassann", "hosseinn"])
    mylist.insert(-1, "Behrooz")
    mylist.remove(13)
    # mylist.clear()  # remove all elements
    # mylist.sort()  # only number
    print(f"length: {length}")
    print(f"firstItem:{first_item}")
    print(f"lastItem:{last_item}")
    print(mylist)


def search(self, mylist):
    index1 = mylist.index(5)
    index2 = mylist.index(7, 3, 10)  # از اندیس ۴ تا اندیس ۱۱ جستجو نماید
    print(index1)
    print(index2)

    tmp = '.'.join(['ab', 'pq', 'rs'])
    print(tmp)

# behrooz.getDataAll(list._list8)
# behrooz.getDataAllByCount(list._list2)
# behrooz.fillList()
# behrooz.getDataAll(list._list4)
# behrooz.getDataAll_Revese(list._list1)
# behrooz.get_select_item(list.list1)
# print(list._list10_nestedList[1][2])  # output: 6
# [[print(x) for x in y] for y in list._list10_nestedList] # output: 1 NewLine 2 NewLine 3 NewLine 4 NewLine 5 NewLine 6
# behrooz.listFunctions(list._list1)
# behrooz.search(list._list1)
# print(list._list11)

# behrooz = list()
