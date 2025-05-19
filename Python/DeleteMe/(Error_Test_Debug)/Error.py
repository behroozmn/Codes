try:
    pass
    # Code
except NameError as NameE:  # Handle NameError Error
    print(NameE)
    print(NameE.message)
    pass
    # مدیریت ارور NameEror در این بلاک صورت می‌گیرد
except IOError as IOE:  # Handle NameError Error
    print(IOE)
    print(IOE.message)
    # مدیریت ارور IOError در این بلاک صورت می‌گیرد

except:  # ErrorHandler of each other error type
    pass
    # مدیریت ارور IOError در این بلاک صورت می‌گیرد
else:
    pass
    # اگر قسمت ترای بدون ارور اجرا شود این بلاک اجرا می‌شود
finally:
    pass
    # در هر صورت این بلاک اجرا خواهد شد
