# تلفیق دو ایتِرِیت با یکدیگر تبدیل به یک ایتریت جدید که شامل هردوی آن‌ها می‌باشد
# اگر یک بار پیمایش شود خالی خواهد شد

from unittest import result


list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9, 10]
students = ["mohammad", "iman", "sara"]
midterm = [78, 80, 94]
final = [91, 84, 97]


def func1_CreateZip():
    result = zip(list1, list2)
    print(f"[func1]=> combine {list1} and {list2}: -------> {list(result)}")
    print(f"[func1]=> combine {list1} and {list2}: --2th--> {list(result)}\n") #یکبار پیمایش سبب تخلیه می‌گردد

def func2_CreateZip():
    finalGrades = [pair for pair in zip(students,midterm, final)]
    # finalGrades = [pair for pair in zip(students,midterm)]
    print(f"[func2]=> {list(finalGrades)}\n")

def func3_Extract():
    myList = [(1, 5), (3, 7), (6, 4), (7, 9)]
    print(f"[func3]=> extract from {myList}: ----> {list(zip(*myList))}\n")

def func4():
    result=zip(midterm, final)
    print(f"[func4]=> {list(result)}\n")

def func5_max():
    result=map(
            lambda pair: max(pair),
            zip(midterm, final)
        )
    print(f"[func5(max)]=> {list(result)}\n")

def func6_MaxZip():
    finalGrades = zip(
    students,
        map(
            lambda pair: max(pair),
            zip(midterm, final)
        )
    )
    print(f"[func6(Max_Zip)]=> {dict(finalGrades)}")

def func6_MaxZip_WithIndex(): # use index
    finalGrades = {t[0]: max(t[1], t[2]) for t in zip(students, midterm, final)}
    print(f"[func6(Max_Zip)]=> {finalGrades}")

def func7_avg():
    result= map(
            lambda pair: (pair[0] + pair[1]) / 2,
            zip(midterm, final)
        )
    print(f"[func7(avg)]=> {list(result)}")

def func7_avg_WithIndex():
    average = zip(
    students,
        map(
            lambda pair: (pair[0] + pair[1]) / 2,
            zip(midterm, final)
        )
    )
    print(f"[func7(avg)]=> {dict(average)}")

func1_CreateZip()
func2_CreateZip()
func3_Extract()
func4()
func5_max()
func6_MaxZip()
func6_MaxZip_WithIndex()
func7_avg()
func7_avg_WithIndex()


