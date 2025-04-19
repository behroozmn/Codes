data = open("/etc/passwd")

#1)
# print(data.read())
# data.seek(2) # جابجایی کرسر به نقطه خاص از فایل
# print(data.read())

#2)
# textLines = data.readlines() # یک لیست از خطوط که آخر هر خط یک بک‌اسلش‌اِن قرار میدهد
# print(textLines)
# print(f"----> {textLines[5]}")


#3)
with open("/etc/passwd", encoding='UTF-8',mode="r") as bFile:
    for l in bFile:
        line = l.strip()
        # mylist = lines.rsplit(",")
        print(line)