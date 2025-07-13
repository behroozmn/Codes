<div dir="rtl">

# Concept(مفاهیم)

- **حالتUntrackیاUnstage**: گاهی اوقات پیش می‌آید که می‌خواهید گیت از بررسی برخی از فایل‌ها و یا فولدرهای پروژه صرف نظر کند و تغییرات آن‌ها را نادیده بگیرد و آن‌ها را دنبال نکند(گیت مواظب آنها نیست)
- **حالتTrackedیاStage** : وقتی توسط دستور add به گیت اضافه می‌کنیم
    - مثلا می‌توان ۳ فایل جدید ایجاد کرد و ۲تای آن را add کرد و کامیت کرد و پس از اتمام کامیت مجددا یک فایل باقی مانده را add و سپس کامیت کرد و در این صورت دو کامیت مجزا خواهیم داشت
- **HEAD**: یک پوینتر برای نمایش جایی که الآن درآن هستم
- **fork**: ایجاد یک پروژه از پروژه اصلی (دراکانت یک شخص حقیقی) در اکانت شما (بعنوان یک پروژه مستقل که هر کار دلخواه را بدون تغییر روی پروژه اصلی صاحب آن انجام دهید)
- **bisect**: به گیت می‌گوییم که الآن اوضاع بد است و در کدام کامیت اوضاع خوب بوده است و گیت میرود و از وسط آنجا به بعد را می‌آورد و ازت می‌پرسد که آیا اینجا اوضاع خوب بوده است یاخیر و اگر خوب بوده میرود و وسط بعدی را پیشنهاد می‌دهد که آیا خوب بوده است یا خیر و شما باید کامپایل کنین و ببینید اوضاع چگونه است و خوب بود یا بد را به گیت گزارش بدهید تا
  کامیتی که اوضاع شروع به بد بودن کرده یافته شود

# Applications(نرم‌افزارها)

- نرم‌افزار دسکتاپ لینوکسی gitk یک نرم افزار است برای visualize and browse history پروژه گیت که با apt نصب می‌شود

# توضیحات تکمیلی

- از کلید و امضا و gpg در گیت استفاده نکنید یا اگر استفاده می‌کنید باید همه تیم از امضا کلید استفاده نمایند
- سایت‌هایی که همانند گیت‌هاب سرویس ورژن کنترل ارائه می‌دهند: github، Bitbucket، gitlab،codeplex
- [url](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1)

# Commands

## init

همواره برای شروع به گیت باید از دستور زیر استفاده شود. یعنی این دستور یک پوشه مخفی گیت ایجاد می‌کند و مدیریت گیت را برعهده می‌گیرد

```shell
cd <Dir>; git init
```

## clone

وقتی بخواهیم یک ریپوزیتوری که ساخته شده است(قبلا دستور init آن توسط برنامه نویس زده شده است) را به سیستم خود منتقل نموده و از آن استفاده نماییم

```shell
git clone url
```

## add

* اگر بخواهیم یک فایل را به حالت stage شده دربیاوریم از دستور زیر استفاده می‌کنیم
* فایل های استیج شده قابلیت کامیت خواهند داشت
* همواره برای اینکه بخواهیم یک نسخه پایدار داشته باشیم باید از دستور کامیت استفاده شود و این دستور کامیت حتما باید پس از دستور add زده شود

```shell
git add File.index
git add File1 File2 ...
git add .  # → [new] + [modified]
git add -u # → [modified] + [deleted]
git add -A # → [new] + [modified] + [deleted] ⇉ Stages Everything
git -A     # ⇄ [git add .] + [git add -u]
``` 

## blame

از بلیم برای عیب‌یابی استفاده می‌شود.(بلیم یعنی مقصر پیدا کردن=تقصیر چه کسی است)

```shell
git help blame         # نمایش توضیحات
git blame FileName -L8 # خط شماره ۸ فایل مذکور توسط چه کسانی نوشته یا تغییر یافته است
git blame fileName     # نمایش تاریخچه تغییرات فایل مورد نظر
```

**switch:**

<div dir="ltr">

* -L : تعیین شماره خط
    * -L8 → خط شماره ۸ را در نظر بگیر
    * -L8,10 →خط ۸تا خط شماره ۱۰ را در نظر بگیر
    * اگر شماره خط نگذاریم همه فایل را در نظر خواهد گرفت

</div>

## branch

- **branch**: شاخه‌های گیت
- شاخه های محلی در مسیر`/git/refs/heads./.` ذخیره می شود. اجرای دستور `git branch` یک لیست از مرجع های شاخه محلی تولید می کند.
- شاخه های سرور در مسیر`/git/refs/remotes./.` ذخیره می شود.
- **master**: برنچ اصلی در بدو ساختن یک پروژه گیت[هر پروژه بصورت پیش‌فرض یک برنچ دارد که نام آن مستر است]
- **remote**: پروژه موجود در بستر شبکه رو می‌گویند
- **Origin**: می‌توان دو تا ریموت داشت یعنی اولی در سرور شرکت با نام «اُریجین» و دیگری در مثلا سرور گیت‌هاب با نام «مای اُریجین» که برای این کار باید از دستور زیر استفاده نمایید
    - **حالت اول**: پروژه در شرکت موجود است و شما آن را کلون کرده اید. پس یک ریموت داریم و باید ریموت دوم را تولید نمایید
        - git remote add myorigin https://github.com/behroozmn/project1
    - **حالت دوم**: فقط یک پروزه لوکال دارید و این پروژه اصلا در شبکه و سروری وجود ندارد پس باید در سروری اضافه نمایید
        - git remote add origin https://git.sherkat.ir/behrooz/project1
        - git remote add myorigin https://github.com/behroozmn/project1

```shell
git branch # نمایش برنچ‌های لوکال پروژه و علامت ستاره یعنی این که روی چه برنچی قرار داریم
git branch -r  # نمایش برنچ‌های ریموت پروژه
git branch BranchName #ساخت یک برنچ جدید با نام دلخواه
git branch -d BranchName #حذف یک برنچ
git checkout [branchName] #ورود به یک برنچ
```

## Status

نمایش وضعیت کنونی گیت

```shell
git status
git log # شماره کامیت رو هم نشان می‌دهد
git log --stat --summary #مشاهده کارهایی که کرده‌اید
git log -p # مشاهده کارهایی که کردید با تفاوت دیف‌ها
git show [CommitHashName | TagName]
```

## rm

```shell
git rm FileName # حذف یک فایل از گیت و همچنین از فایل‌سیستم
git rm --cached <FileNames> # حذف فایل «استیج» شده موجود در گیت
git rm --cached -r <FOLDER> # حذف فولدر «استیج» شده موجود در گیت
git checkout HEAD -- <file_path> # فایلی که به اشتباه حذف شده است(استیج شده بوده) رو از آخرین کامیت برمی‌گردانیم
```

---
> حذف یک فایل که به اشتباه به گیت اضافه و کامیت شده است

```shell
git rm --cached giant_file # Stage our giant file for removal, but leave it on disk
git commit --amend -CHEAD  # Amend the previous commit with your change Simply making a new commit won't work, as you need to remove the file from the unpushed history as well
git push                   # Push our rewritten, smaller commit

```

## Push

قرار دادن دیتا به درون سرور از سیستم لوکال خودمان

```shell
git push origin master # در سرور «اُریجین» برنچ «مستر» را اضافه کن

```

حذف یک فایل هم از گیت و هم از فایل‌سیستم

## Remote

کارهای مربوطه به پروژه سرور شبکه[میتوانیم دوتا ریموت داشته باشیم یکی مثلا نام «اوریجین» در سرور شرکت و دیگری مثلا در گیت‌هاب بنام «مای اوریجین»]

```shell
git remote # تمام اطلاعات مربوط به ریموت را نمایش می‌دهد
git remote -v  # نمایش اطلاعات بیشتر 
git remote rename server1 server2
git remote origin myOrigin
git remote show <RemoteName[origin|myOrigin]>
git remote show origin # show info about remote o

# اگر پروژه تا اکنون درحال کار بصورت لوکال است وبخواهیم به سرور انتقال بدهیم به روش زیر افدام نمایید
git remote add origin https://... #یک پروژه در سرور اضافه کن و نام آن را «اریجین» بگذار و آدرس آن هم فلان است و نکته این است که قبل از پوش به سرور اضافه نخواهد شد و باید حتما پوش کنیم
git remote add coworkers_repo https://github.com/sokanacademy/coworkers_repo.git
```

## fetch

* با این دستور هیچ تغییری در منابع لوکال به‌وجود نمیآید وتنها ریموت بروزرسانی می‌شد
* با دستور fetch صحت تغییرات مخزن آنلاین را مشاهده می‌کنیم
* تغییرات به لوکال منتقل نمی‌شود
* تمام ااطلاعات را از سرور می‌گیرد و ریپوزیتوری ریموت که در سیستم شما هست را بروزرسانی می‌کند
* بعد استفاده از دستور fetch، کدتون هیج تغییری نمیکنه(هیچ تغییری در نسخه staging area و نسخه local repository رخ نمی‌دهد)
* زمانی که از اطلاعات تغییر یافته در سرور(توسط دیگران) که می‌بایست مرج بشود اطمینان ندارید اول تغییرات راfetch کنید(تنها دریافت اطلاعات) و بعد از بررسی آن تغییرات را در شاخه مورد نظر مرج نمایید
* نکته: دو دستور زیر باهم مساوی هستند
    * git pull origin master
    * git fetch; git merge origin/master;

```shell
git fetch origin #    تنها مشاهده تغییرات سرور آنلاین(ریموت)
git fetch <remoteName> # بروزرسانی تمام تغییرات در ریپوزیتوری ریموت موجود درسیستم لوکال
git fetch <remoteName> <branch> بروزرسانی تغییرات برنچ مورد نظر از ریپوزیتوری ریموت در سیستم لوکال
git fetch --all # تمام ریموت‌های ثبت شده و شاخه های آنها را دریافت می کند
git fetch --dry--run # فقط نمایش خروجی کاری که می‌خواهد انجام شود و هیچ کاری نمی‌کند
```

![git-Fetching.gif](_srcFiles/Images/git-Fetching.gif "git-Fetching.gif")

## Reset

برای خارج نمودن یک فایل استیج شده از دستور زیر استفاده می‌نماییم

```shell
git reset FileName # خارج نمودن فایل از استیج
git reset --hard #نادیده گرفتن تمام تغییرات لوکال
```

![git-SoftReset.gif](_srcFiles/Images/git-SoftReset.gif "git-SoftReset.gif")
![git-HardReset.gif](_srcFiles/Images/git-HardReset.gif "git-HardReset.gif")

## tag

- **tag**: برچسب زدن به روی یک کامیت و معمولا برای زمانی یک برچسب را روی کامیت میزنیم که بخواهیم راحت تر آن را پیدا کنیم یا اینکه مثلا در کامیت مورد نظر رلیز صورت گرفته است
- توسط این تگ‌ها می‌توانیم پروژه را ورژن بندی نماییم و هرگاه بخواهیم به ورژن ۲ دسترسی یابیم آنگاه به آن کامیت «چک‌اوت» نماییم و ورژن را راه‌اندازی نماییم
- در حالت عادی پوش، تگ به سرور پوش نمی‌شود یعنی با دستور git push تگ پوش نمی‌شود

```shell
git tag #نمایش تگ‌های فعلی پروژه
git tag -a <TagName> -m "<Message>" #افزودن تگ به کامیت فعلی
git tag -a v2.0 -m "Release for ..."
# [-m] پیغامی که برای یک تگ بعنوان توضیحات اضافی می‌نویسیم
# [-a] معرف «اَنوتِیت»است که نام یک تگ را مشخص می‌کند
git tag -a v1.8 <CommitHashName> # افزودن تک به یک کامیت موجود
# در اینجا یک صفحه باز می‌شود و توضیحات می‌خواهد
git tag -l "v*" # هر تگی که با وی شروع می‌شود را لیست کند
git show <tagName>
git push origin <TagName> # تگ در پوش عادی به سرور اضافه نمی‌شود و باید توسط نام تگ آن را به سرور اضافه نماییم
git push origin --tags # تگ در پوش عادی به سرور اضافه نمی‌شود ، با دستور روبرو تمام تگ‌ها را به سرور اضافه می‌کنیم
```

## Config

LIST

```shell
git config --list
git config --list --show-origin
git config -l
```

SET

```shell
git config --global user.name "بهروز محمدی نسب" 
git config --global user.email "behroozmn@chmail.ir"
git config credential.helper store #store user and password
git config --edit --local
git config --global alias.Behrooz "log --all --decorate --oneline --graph"
git config --global core.editor "vim"
git config --global core.autocrlf [true | input | false] #prevent auto append "^M" to end of each lines(Run in windows system. )
git config --global core.autocrlf true    #windows
git config --global core.autocrlf input  #Linux And Mac
git config --global core.autocrlf=false #disable(Default)
```

## commit

* پس از افزودن فایل‌ها توسط دستور add در گیت، از طریق دستور commit آن را بعنوان یک تغییر پایدار در گیت تثبیت می‌نماییم
* فایل های استیج شده قابلیت کامیت خواهند داشت
* همواره برای اینکه بخواهیم یک نسخه پایدار داشته باشیم باید از دستور کامیت استفاده شود و این دستور کامیت حتما باید پس از دستور add زده شود

```shell
git commit -m "متن دلخواه"
git commit # بازکردن یک ادیتور و نهایتا نوشتن متن دلخواه و سپس ذخیره آن
git commit -am "Message" # همزمان «اَد» کردن و سپس کامیت کردن
git commit --amend -m "New Description" #ویرایش متن یک کامیت  اگر هنوز در سرور پوش نکرده باشید ولی پوش شده باشد دیگر نمیشود
Note: amend means modify the last commit of the current branch

```

## Diff

```shell
git diff HEAD # تغییرات صورت گرفته نسبت به هِد چه مواردی و چه تغییراتی است
git diff --staged # چه چیزی از مواردی که در استیج هستن تغییر پیدا کرده است
git diff FileName
git diff --color
```

## log

```shell
--all
--graph
--abbrev-commit
--decorate
--date=relative
--stat

```

```shell
git log
git log --graph --all #نمایش گراف برپایه کاراکترهای اسکی
git log --graph       #نمایش گراف برپایه کاراکترهای اسکی برای برنچ فعلی که توش هستیم
git log --all --decorate --oneline --graph
git log --all --decorate --graph
git log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(auto)%d%C(reset)' --all
git log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(auto)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)'
git log --graph --pretty="%C(yellow) Hash: %h %C(blue)Date: %ad %C(green) Message: %s " --date=human --date=relative
git log --graph --pretty="%C(yellow) Hash: %h %C(blue)Date: %ad %C(green) Message: %s " --date=human
git log --all --decorate --oneline --graph --stat

```

## Checkout

```shell
git checkout BranchName # رفتن به یک برنچ جدید
git checkout TagName # رفتن به یک تگ جدید
```

اگر فایلی را خراب کرده‌اید و می‌خواهید به وضعیت قبل برگردانید

```shell
git checkout -- FileName # برگرداندن یک فایل به وضعیت آخرین کامیت آن
git checkout HEAD -- <file_path> # فایلی که به اشتباه حذف شده است(استیج شده بوده) رو از آخرین کامیت برمی‌گردانیم
```

</div>









![CheatSheet_Git.jpg](_srcFiles/Images/CheatSheet_Git.jpg "CheatSheet_Git.jpg")


