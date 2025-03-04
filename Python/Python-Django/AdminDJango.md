####  افزودن جداول در داشتبورد مدیریت ادمین
```python
from . import models
admin.site.register(models.Product)
```

#### تغییر زبان داشبورد از انگلیسی به فارسی
File: setting.py
`LANGUAGE_CODE = 'fa-ir'`
