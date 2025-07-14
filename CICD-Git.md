<div dir="rtl">

# Concept(مفاهیم)

- **حالتUntrackیاUnstage**: گاهی اوقات پیش می‌آید که می‌خواهید گیت از بررسی برخی از فایل‌ها و یا فولدرهای پروژه صرف نظر کند و تغییرات آن‌ها را نادیده بگیرد و آن‌ها را دنبال نکند(گیت مواظب آنها نیست)
- **حالتTrackedیاStage** : وقتی توسط دستور add به گیت اضافه می‌کنیم
    - مثلا می‌توان ۳ فایل جدید ایجاد کرد و ۲تای آن را add کرد و کامیت کرد و پس از اتمام کامیت مجددا یک فایل باقی مانده را add و سپس کامیت کرد و در این صورت دو کامیت مجزا خواهیم داشت
- **HEAD**: یک پوینتر برای نمایش جایی که الآن درآن هستم
- **fork**: ایجاد یک پروژه از پروژه اصلی (دراکانت یک شخص حقیقی) در اکانت شما (بعنوان یک پروژه مستقل که هر کار دلخواه را بدون تغییر روی پروژه اصلی صاحب آن انجام دهید)
- **bisect**: به گیت می‌گوییم که الآن اوضاع بد است و در کدام کامیت اوضاع خوب بوده است و گیت میرود و از وسط آنجا به بعد را می‌آورد و ازت می‌پرسد که آیا اینجا اوضاع خوب بوده است یاخیر و اگر خوب بوده میرود و وسط بعدی را پیشنهاد می‌دهد که آیا خوب بوده است یا خیر و شما باید کامپایل کنین و ببینید اوضاع چگونه است و خوب بود یا بد را به گیت گزارش بدهید تا
  کامیتی که اوضاع شروع به بد بودن کرده یافته شود

# توضیحات تکمیلی

- از کلید و امضا و gpg در گیت استفاده نکنید یا اگر استفاده می‌کنید باید همه تیم از امضا کلید استفاده نمایند
- سایت‌هایی که همانند گیت‌هاب سرویس ورژن کنترل ارائه می‌دهند: github، Bitbucket، gitlab،codeplex
- [url](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1)

# Commands

## Add

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

## Blame

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

## Branch

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

## Clone

وقتی بخواهیم یک ریپوزیتوری که ساخته شده است(قبلا دستور init آن توسط برنامه نویس زده شده است) را به سیستم خود منتقل نموده و از آن استفاده نماییم

```shell
git clone url
```

## Commit

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

### core.autocrlf

کاراکتر انتهایی هر خط(Line Ending) در سیستم‌عامل‌ها متفاوت است پس حین ایجاد تغییر در فایل‌ها (استفاده گروهی از یک ریپوزیتوری گیت از بستر سیستم‌عامل‌های متفاوت) ممکن است آخر خط‌های این فایل‌ها بسته به سیستم‌عامل CRLF یا LF درج شده باشد

🅰️ ویندوز: دو کاراکتر (“n\”) Line Feed و (“r\”) Carriage Return یا همان (CR LF)
🅱️ لینوکس و مک: کاراکتر (“n\”) Line Feed

- **windows**
    - بصورت خودکار گیت هنگام بررسی فایل‌های متنی، LF یا همان (“n\”) را به CRLF یا همان (“r\”) تبدیل می کند.
    - بصورت خودکار گیت هنگام ارسال فایل‌های متنی، CRLF (یا همان “r\”) به LF (یا همان “n\”) تبدیل می شود.
    - هنگام check in و check out کردن، گیت به صورت خودکار (“r\”) Carriage Return را حذف و اضافه می کند.
    - گیت بین LF و CRLF تفاوت قائل نشود و این مورد رو به عنوان «تغییر در محتوای فایل» در نظر نگیره باید این گزینه رو فعال کنیم.
    - `git config --global core.autocrlf true`
- **Linux And Mac**
    - اگر به هر دلیلی (“r\”) در انتهای خطوط موجود باشد، هنگام ذخیره در ریپوزیتوری، توسط گیت حذف خواهد شد. طبیعتا لازم نیست هنگام واکشی اطلاعات از ریپوزیتوری تغییری اعمال شود پس فقط در هنگام input لازم است این تبدیل انجام شود.
    - گیت هنگام بررسی فایل های متنی هیچ تبدیلی را انجام نمی دهد.
    - هنگام ارسال فایل های متنی، CRLF (یا همان “r\”) به LF (یا همان “n\”) تبدیل می شود.
    - برخی از افراد استفاده از آن را هنگام توسعه در سیستم های یونیکس توصیه می کنند
    - `git config --global core.autocrlf input`
- **disable(Default)**
    - گیت هیچ تبدیلی را هنگام بررسی یا ارسال فایل های متنی انجام نمی دهد.
    - اگر تنظیم تعریف نشده باشد، این مقدار پیش فرض است.
    - `git config --global core.autocrlf=false`

<div dir="ltr">

- core.autocrlf #fix LineEnding problem [url](https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings?platform=windows)
    - git config --global core.autocrlf true #windows
    - git config --global core.autocrlf input #Linux And Mac
    - git config --global core.autocrlf=false #disable(Default)

</div>

## Diff

```shell
git diff HEAD # تغییرات صورت گرفته نسبت به هِد چه مواردی و چه تغییراتی است
git diff --staged # چه چیزی از مواردی که در استیج هستن تغییر پیدا کرده است
git diff FileName
git diff --color
```

## Fetch

* با این دستور هیچ تغییری در منابع لوکال به‌وجود نمیآید وتنها ریموت بروزرسانی می‌شد
* با دستور fetch صحت تغییرات مخزن آنلاین را مشاهده می‌کنیم
* تغییرات به لوکال منتقل نمی‌شود
* تمام ااطلاعات را از سرور می‌گیرد و ریپوزیتوری ریموت که در سیستم شما هست را بروزرسانی می‌کند
* بعد استفاده از دستور fetch، کدتون هیج تغییری نمیکنه(هیچ تغییری در نسخه staging area و نسخه local repository رخ نمی‌دهد)
* زمانی که از اطلاعات تغییر یافته در سرور(توسط دیگران) که می‌بایست مرج بشود اطمینان ندارید اول تغییرات راfetch کنید(تنها دریافت اطلاعات) و بعد از بررسی آن تغییرات را در شاخه مورد نظر مرج نمایید

نکته: دو دستور زیر باهم مساوی هستند

```shell
git pull origin master               # 🅰️
git fetch && git merge origin/master # 🅱️

```

```shell
git fetch origin #    تنها مشاهده تغییرات سرور آنلاین(ریموت)
git fetch <remoteName> # بروزرسانی تمام تغییرات در ریپوزیتوری ریموت موجود درسیستم لوکال
git fetch <remoteName> <branch> بروزرسانی تغییرات برنچ مورد نظر از ریپوزیتوری ریموت در سیستم لوکال
git fetch --all # تمام ریموت‌های ثبت شده و شاخه های آنها را دریافت می کند
git fetch --dry--run # فقط نمایش خروجی کاری که می‌خواهد انجام شود و هیچ کاری نمی‌کند
```

<div style="display: flex; flex-direction: column; align-items: center;">

![git-Fetching.gif](_srcFiles/Images/git-Fetching.gif "git-Fetching.gif")

</div>

## Init

همواره برای شروع به گیت باید از دستور زیر استفاده شود. یعنی این دستور یک پوشه مخفی گیت ایجاد می‌کند و مدیریت گیت را برعهده می‌گیرد

```shell
cd <Dir>; git init
```

## Log

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

## Merge

- ابتدا باید به برنچ مستر برویم و سپس یک برنچ را مرج کنیم تا آن برنج فرعی روی مستر اعمال شود
- در هنگام تایید یک **mergeRequest** گزینه Squash commit سبب ترکیب چندین کامیت(در برنچ مد نظر) به یک کامیت در برنچ مقصد می‌شود
- در هنگام تایید یک **mergeRequest** گزینه **Approved** به معنای تایید یک درخواست است. یعنی فرد بررسی‌کننده تغییرات کد را مطالعه و ارزیابی کرده و هیچ مشکلی در آن پیدا نکرده است.در پروژه‌ها، قبل از ادغام، نیاز است که یک یا چند نفر تغییرات را بررسی و تأیید کنند که این فرآیند به عنوان "Code Review" شناخته می‌شود
- برای جلوگیری از کانفلیکت باید برای هر کار کوچک کامیت زد

merge DevBehrooz into main

```shell
git branch #فهمیدن اینکه در چه برنچی هستیم
git checkout branch1 #ورود به برنچ۱ که قصد داریم برنچ۲ را درون آن مرج نماییم
git merge branch2 # افزودن دیتای برنچ۲ به برنچ۱
git push origin
git push origin branch2
git push origin branch1
```

```shell
# fast-forward(--ff): وقتی تغییرات نداشته باشد یا کم باشد دراین صورت برای ادغام، کامیت جدید ایجاد نمیکند
# no-fast-forward(--no-ff): ایجاد کامیت جدید و قابل دسترس برای هر دو برنچ
# --abort حذف عملیات مرج در زمانی که یک کانفلیکتی رخ داده است
git merge --abort <branch-name>
git merge --no-commit <branch-name>
checkout main git merge --no-ff -m "Merge branch Develop into main" Develop # هرچند در وضعیت «فست‌فوروارد[عدم ساخت کامیت جدید بخاطر نبودن تفاوت بین دو برنچ]» هستیم، اما سیستم را ملزم به ایجاد کامیت می‌کنیم
```

<div style="display: flex; flex-direction: column; align-items: center;">

![git-fast-forward.gif](_srcFiles/Images/git-fast-forward.gif "git-fast-forward.gif")
![git-NofastForward.gif](_srcFiles/Images/git-NofastForward.gif "git-NofastForward.gif")
![git-mergeConflict.gif](_srcFiles/Images/git-mergeConflict.gif "git-mergeConflict.gif")

</div>

## Pull

- در **مرحله اول** همانند **fetch** عمل میکند و تمام ااطلاعات را از سرور می‌گیرد و ریپوزیتوری ریموت داخل سیستم را بروزرسانی می‌کند
- **مرحله دوم**: اطلاعات نسخه **remote repository** رو با نسخه **local repository** مرج میکنه
    - به همین خاطر تغییرات سرور در سیستم شما آورده می‌شود
- **مرحله سوم:** اگر درحال تغییر در فایل هستید ممکن است **conflict** رخ دهد که باید این تعارض را مرتفع نمایید
- زمانی که از اطلاعات تغییر یافته در سرور(توسط دیگران) که می‌بایست مرج بشود اطمینان ندارید اول تغییرات راfetch کنید(تنها دریافت اطلاعات) و بعد از بررسی آن تغییرات را در شاخه مورد نظر مرج نمایید
- می‌توان چندین سرور ریموت داشته باشیم. مثلا ریموت سرور «گیت‌لب‌(شرکت)» یا «گیت‌هاب(شخصی‌برنامه‌نویس)» یا «گیت‌هاب(شرکت بستر اینترنت)» باشد

نکته: دو دستور زیر باهم مساوی هستند

```shell
git pull origin master; # ✅️
git fetch; git merge origin/master; # ✅️

```

```shell

git pull <RemoteName> <localBranch> # Fetch and Merge branch localBranch from RemoteBranch
git pull origin [master|develop|bug|...] 
# 1️⃣️:تمام تغییرات شاخه لوکال(مستر یا دِوِلُپ یا باگ یا هرچیزی دیگر) را از سرور گیت بگیر و در ریپوزیتوری ریموت(موجود در سیستم لوکال) بروزرسانی کن
# 2️⃣️:تغییرات آورده شده را در شاخه لوکال نیز اعمال کن یعنی مرج کن
# 3️⃣️:اگر تغییرات تعارض داشت پیام بده تا توسط کاربر این تعارض مرتفع گردد
git pull MyGithub DevMohammadinasab # Fetch and Merge LocalBranch DevMohammadinasab from MyGithub(ServerName)
git pull origin develop # Fetch and Merge branch develop from origin(سرور ریموت که نام آن را اوریجین گذاشته‌ایم)
```

<div style="display: flex; flex-direction: column; align-items: center;">


![git-pull.gif](_srcFiles/Images/git-pull.gif "git-pull.gif")

</div>

## Push

قرار دادن دیتا به درون سرور از سیستم لوکال خودمان

```shell
git push origin master # در سرور «اُریجین» برنچ «مستر» را اضافه کن

```

## Rebase

```shell
# شاخه ها
# main: A --- B --- C
# feature: D --- E

# Rebase
git checkout feature
git rebase main
# A --- B --- C  (main)
#                    \
#                      D' --- E' (feature)

# Merge
git checkout main
git merge feature
# A --- B --- C --- D' --- E' (main)

```

- Rebase
    - فرآیند انتقال یا ترکیب یک سری از «کامیت»ها از یک برنچ، به یک «کامیت» پایه جدید در برنچ دیگر
    - مبنای ایجاد کامیت جدید
    - دلیل اصلی تغییر پایه، خطی نگه داشتن تاریخچه پروژه است
    - عمل Rebase در شاخه‌های ریموت نیازمند force push است

```shell
$git checkout Feature; git rebase master # Rebase the Feature into master 
# کل شاخه «فیچر» روی شاخه مستر منتقل شود
# این کار از طریق بازنویسی سابقه پروژه با ایجاد کامیت‌های تازه برای هر کامیت در شاخه  مستر صورت می‌گیرد
```

- standard rebase:
    - هرگز نباید مرتکب «کامیت» مجدد یا همان rebase commit شوید.زیرا Rebase کاری که می‌کند این است که «کامیت» جدید را جایگزین «کامیت» های قدیمی می‌کند و به نظر می رسد که بخشی از تاریخچه ی پروژه شما، به طور ناگهانی از بین رفته است.


- Interactive rebase(تعاملی):
    - این وضعیت امکان تغییر دادن کامیت‌ها در هنگام انتقالشان به شاخه جدید را فراهم می‌کند.
    - این وضعیت قوی‌تر از rebase خودکار است، چون کنترل کاملی روی سابقه کامیت شاخه ارائه می‌کند.
    - به طور معمول از این روش برای پاکسازی یک سابقه شلوغ، پیش از ادغام شاخه feature در master استفاده می‌شود.
    - item
        - **reword**: تغییر «مسیج» کامیت
        - **edit**: Amend this commit
        - **squash**: Meld commit into the previous commit
        - **fixup**: Meld commit into the previous commit, without keeping the commit's log message
        - **exec**: Run a command on each commit we want to rebase
        - **drop**: Remove the commit

```shell
git checkout Feature; git rebase -i master # [OR] git rebase --interactive master # دستورهای فوق باعث باز شدن ویرایشگر می‌شود و همه کامیت‌هایی که باید منتقل شوند، برای اصلاحات فهرست می‌شوند
# out:replace pick with [fixup | squash | edit | pick | reword | exec | drop]
#     pick 22d6d7c Commit message#1
#     pick 44e8a9b Commit message#2
#     pick 79f1d2h Commit message#3

```

<div dir="ltr">

rebase: «git rebase» copies the commits from the current branch, and puts these copied commits on top of the specified branch.

</div>



<div style="display: flex; flex-direction: column; align-items: center;">

![git-rebase.gif](_srcFiles/Images/git-rebase.gif "git-rebase.gif")
![git-Rebase-InteractiveRebase.gif](_srcFiles/Images/git-Rebase-InteractiveRebase.gif "git-Rebase-InteractiveRebase.gif")
![git-Rebase-InteractiveRebase-Squash.gif](_srcFiles/Images/git-Rebase-InteractiveRebase-Squash.gif "git-Rebase-InteractiveRebase-Squash.gif")



</div>

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

## Reset

برای خارج نمودن یک فایل استیج شده از دستور زیر استفاده می‌نماییم

```shell
git reset FileName # خارج نمودن فایل از استیج
git reset --hard #نادیده گرفتن تمام تغییرات لوکال
```

<div style="display: flex; flex-direction: column; align-items: center;">

![git-SoftReset.gif](_srcFiles/Images/git-SoftReset.gif "git-SoftReset.gif")
![git-HardReset.gif](_srcFiles/Images/git-HardReset.gif "git-HardReset.gif")

</div>

## Rm

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

## Status

نمایش وضعیت کنونی گیت

```shell
git status
git log # شماره کامیت رو هم نشان می‌دهد
git log --stat --summary #مشاهده کارهایی که کرده‌اید
git log -p # مشاهده کارهایی که کردید با تفاوت دیف‌ها
git show [CommitHashName | TagName]
```

## Tag

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

# Files

## .gitignore

- تنها یک فایل از نوع gitignore در تمام پروژه خواهیم داشت(می‌شود دوتا یا چند تا باشد ولی استاندارد نیست)
- فایل مخفی gitignore فقط برای فایل‌هایی کاربرد دارد که untracked هستند یعنی هنوز با دستور git add به stage در گیت اضافه نشدند
    - اگر بخواهیم یک فایل که اضافه شده است را حذف نماییم از دستور git rm --cached NAME استفاده می‌کنیم
-

<div dir="ltr">
```shell
touch .gitignore #go to the root of your local Git, and create it
```

-
    * → The asterisk symbol matches zero or more characters.
- /access.log → نادیده گرفتن دقیقا این فایل در مسیر اصلی پروژه
    - access.log
- access.log → فایل که در هرکجا باشد
    - [access.log]
    - [logs/access.log]
    - [var/logs/access.log]
- *.log → #ignore any files with the .log extension[all .log files]
    - error.log
    - logs/debug.log
    - build/logs/error.log
- logs/**  → نادیده گرفتن همه مواردی که در مسیر روت پروژه در فولدر لاگ قرار دارد
- **/build → [نادیده گرفتن تمام فولدرها(بامحتویات آن) که نام آن بیلد است][files and folders in any build folder]
    - var/build
    - pub/build
    - build
- temp/ → ignore ALL files in ANY directory named temp
    - .idea/ → Ignore IDE specific files
    - .vscode/ → Ignore IDE specific files
- foo/**/bar
    - foo/bar
    - foo/a/bar
    - foo/a/b/c/bar
- access?.log
    - access0.log
    - access1.log
    - accessA.log
- foo??
    - fooab
    - foo23
    - foo0s
- *.[oa]
    - file.o
    - file.a
- *.[!oa]
    - file.s
    - file.1
    - file.0
- access.[0-2].log
    - access.0.log
    - access.1.log
    - access.2.log
- file.[a-c].out
    - file.a.out
    - file.b.out
    - file.c.out
- file.[a-cx-z].out
    - file.a.out
    - file.b.out
    - file.c.out
    - file.x.out
    - file.y.out
    - file.z.out
- access.[!0-2].log
    - access.3.log
    - access.4.log
    - access.Q.log
- [/lib/**/name] #All name folders, and files and folders in any name folder within the lib folder.
- [*.file] #All files withe .file extention
- [*name/] #All folders ending with name
- [name?.file] #? matches a single non-specific character
- [name[a-z].file] #[range] matches a single character in the specified range (in this case a character in the range of a-z, and also be numberic.)

</div>

</div>


<div style="display: flex; flex-direction: column; align-items: center;">

![CheatSheet_Git.jpg](_srcFiles/Images/CheatSheet_Git.jpg "CheatSheet_Git.jpg")

</div>
