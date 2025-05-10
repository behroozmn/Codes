```
return JsonResponse(Items.to_dict(), safe=False)
```

* توضیحات safeکه بصورت پیش‌فرض True است
    * اگر safe=Trueباشد آنگاه JsonResponse فقط مجاز است یک dict را بگیرد. یعنی اگر یک لیست یا نوع دیگری بفرستید، Django یک خطا می‌ده
    * اگر safe=False باشد
        * آنگاه اجازه می‌دهیم هر نوع object قابل سریالایز شدن JSON (مثل لیست , namedtuple , custom class ) را هم برگردانیم.
        * در این حالت، JsonResponse فرض می‌کند که شما مسئول مدیریت خروجی هستید.
