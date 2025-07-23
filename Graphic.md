# 📍️ wayland

<div dir="rtl">

* تصویر
    * ادوبی ilustrator
    * ادوبی فوتوشاپ
* تصویر و نمایش ساختار شیء
    * ۲بعدی: autoCad
    * ۳بعدی: 3Dmax
* تصویر (کتاب و صفحه آرایی و کارهای کتاب)
    * adobe indesign
* ویدئو:
    * primier: شرکت ادوبی
    * davinchi: شرکت دیگر
* موشن گرافی
    * afterEffect: تیزرهای تبلیغاتی مثلا ابتدای تیزر استورکس که آقای جدی انجام داده بود
* ضبط ویدئو(رکورد)
    * TechSmit snagit recorder [محمد اردوخانی با این دوره‌های پایتون و غیره را ضبط کرده است]

</div>


در نسخه دبیان۱۱ وقتی یک برنامه بالا نمی‌آید از روش زیر عمل می‌کنیم

```shell
sudo apt install qtwayland5
vim /etc/profile.d/behrooz
export QT_QPA_PLATFORM=wayland
export XDG_SESSION_TYPE=wayland
export ANKI_WAYLAND=1
export QT_QPA_PLATFORMTHEME=qt5ct
```

Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.