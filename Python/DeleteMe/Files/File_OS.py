import os
import time
import fnmatch
import glob

print(os.listdir('/'))
print(os.path.isdir('/'))

print("---------------")

result = os.scandir('/home/Files')
for item in result:
    if item.is_file():  # if item.is_file():
        print(f'File {item.name}: {time.ctime(item.stat().st_mtime)}')

# result = os.stat('./my_files/doc.txt')
# print(time.ctime(result.st_mtime))

# os.mkdir('test')  # 1-Error if exist 2-Error with subDirectory
# os.makedirs('/tmp/test/sub_ddsfdsfdsfsirectory1')  # 1-Error if exist


print('################')
print('#### Delete ####')
print('################')

# os.remove("/tmp/test/sub_ddsfdsfdsfdsfsirectory1"); # اگر فایل موجود نباشد خطا برمی‌گرداند
# os.unlink("/tmp/test/sub_ddsfdsfdsfsdfsdfsdfsdfdsfdsfsirectory1"); # اگر فایل موجود نباشد خطا برمی‌گرداند

# os.rmdir("/tmp/test/sub_ddsfdsfdsfsdfsdfsdfsdfdsfdsfsirectory1"); # فقط پوشه های خالی رو پاک میکنه
