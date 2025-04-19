list1 = [3, 6, 8, 13, 4, 90]
list2 = ['a', 't', 'z']
list3 = "mostafa"
list4 = ['mohammad', 'milad', 'akbar', 'sara', 'iman','ali']

#Step1)-------------------------------------------------------------------------
#روش اول
result = [len(name) for name in list4]
print(f"Character lenght {list(list4)} ---> {result}")

# روش دوم
print(f"Character lenght {list(list4)} ---> {[len(name) for name in list4]}")
print("----------End1-------------")

#Step2)----------------------------------------------------------------------
print(f"max in {list(list1)} ---> {max(list1)}")
print(f"min in {list(list1)} ---> {min(list1)}")
print(f"max lenght in {list(list4)} ---> {max(list4, key=lambda n: len(n))}") #ماکزیمم را برحسب تعداد کاراکتر درنظر بگیر
print(f"max lenght in {list(list4)} ---> {min(list4, key=lambda n: len(n))}") #مینیمم را برحسب تعداد کاراکتر درنظر بگیر

