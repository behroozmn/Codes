# 1.Intro

* در حین وارد کردن دیتای جدید یا ادیت، مقادیر وارد شده مطابق با نوع دیتای مدل و جدول باشد
* یا بخواهیم فیلتر برای وارد کردن دیتا قرار بدهیم یعنی مثلا کاربر باید یک پارامتر را اعداد بین یک تا بیست وارد نماید وگرنه نتواند و خطا بدهد
* مثلا یک عنوان نباید بیشتر از ۳۰۰ کاراکتر باشد و گرنه پیعام خطا بدهد
* یا دیتا را نباید خالی قرا دهیم وگرنه پیعام خطا بدهد
*

# 2.Implement

## 2.1.رول اول[بررسی هر پارامتر توسط تابع مستقل]

* edit file `serialize.py` For Item: `priority

  ```python
  from rest_framework import serializers
  from .models import Todo
  
  
  class TodoSerializer(serializers.ModelSerializer):
        def validate_priority(self,priority):
            if priority < 10 or priority > 20:
               raise serializers.ValidationError('priority is not ok')
            return priority
        class Meta:
            model = Todo
            fields = '__all__'
  ````

## 2.1.رول دوم[یک تابع برای همه ورودی ها]

* edit file `serialize.py` For Item: `priority

  ```python
  from rest_framework import serializers
  from .models import Todo
  
  
  class TodoSerializer(serializers.ModelSerializer):
        def validate(self, attrs):
            print(attrs)
            return super().validate(attrs)
  
        class Meta:
            model = Todo
            fields = '__all__'
  ````








  