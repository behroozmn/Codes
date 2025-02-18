# Render

## 1.render_to_string
درییافت آدرس یک فایل «اچ‌تی‌اِم‌آِل» و تبدیل به رشته و استفاده از آن

```
from django.template.loader import render_to_string
def dynamic_name(request, name):
    dic_keys = list(dic_id.keys())
    dic_values = list(dic_id.values())

    data = None
    for key, val in dic_id.items():
        if val == name:
            data = key
    if data is not None:
        return HttpResponse(f'input from url is : {name} and data is : {data}<br><br>'
                            f'<a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>')
    else:
        response_data = render_to_string('NotResponse.html')✅️
        return HttpResponse(response_data)
```

## 2. static
```
from django.shortcuts import render✅️
def dynamic_name(request, name):
    dic_keys = list(dic_id.keys())
    dic_values = list(dic_id.values())

    data = None
    for key, val in dic_id.items():
        if val == name:
            data = key
    if data is not None:
        return HttpResponse(f'input from url is : {name} and data is : {data}<br><br>'
                            f'<a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>')
    else:
        return render(request, 'NotResponse.html')✅️
```

## 3 DTL(Django Template Language)
 >منظور همان دو آکولاد باز و بسته است 

```
from django.shortcuts import render
days = {
    'saturday': 'this is satureday in disctionary',
    'sunday': 'this is sunday in disctionary',
    'monday': 'this is monday in disctionary',
    'tuesday': 'this is tuesday in disctionary',
    'wednesday': 'this is wednesday in disctionary',
    'thursday': 'this is thursday in disctionary',
    'friday': 'this is friday in disctionary',
}


def dynamic_days(reqeust, day):
    day_data = days.get(day)
    if day_data is not None:
        context = {
            "data": day_data
        }
        # DTL -> Django Template Language

        return render(reqeust, 'challenges/challenge.html', context)✅️ # این اسم مهم نیست مهم ارسال دیکشنری است که به صفحخه دیکشنری ارسال بشود
        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
    return HttpResponseNotFound('day does not exists')

```
> Note: Can use [built-In Templates](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/)