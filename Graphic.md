# 📍️ wayland


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