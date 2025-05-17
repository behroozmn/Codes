# iterate: پیمایش یا تکرار کردن
#
# iterable: Objects which can iterate and can convert to iterator
#      ---> iterableObjects: Lists, Tuples, Dictionaryes, Sets, Strings
#      ---------> iterableObject is not a iterator[but by function it can chage to iterator]
#      ---> Note: we can not iterate on iterableObjects first. It should be converted to iterator and then iterate on it
#      ---> Note: موضوع توالی و پشت سر هم بودن، جزء مهمترین مولفه در این ساختار است
#      ---> Generally ussing with loops(for and ...)
#      ---> next(): ussing next function for access to next item
#
# iterator: object that can iterate on items by itself, and It can sequentially access the elements of an iterable
#      ---> iterator=iterableObjects.iter();
#      ---> class who must define __iter__() to  return iterator [Obj.iter()]
#      ---> class who must define __next__() to  return next item and if nextItem is not available, return [StopIteration exception]) [Obj.next()]


numbers = [1, 2, 3]  # iterableObjects
colors = ('red', 'green', 'blue')  # iterableObjects
name = "Behrooz"  # iterableObjects

iterator = iter(numbers)

print(iterator)  # output: <list_iterator object at 0x7fb1fd78e8f0>
print(next(iterator))  # output: 1
print(next(iterator))  # output: 2
print(next(iterator))  # output: 3
# print(next(iterator)) # output: Exception(StopIteration) [only 3 items is Exist in iterableObjects]


iterName = iter(name)
print(next(iterName))
print(next(iterName))
print(next(iterName))
print(next(iterName))
