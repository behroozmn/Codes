The Design Patterns are descriptions of communicating objects and class that are customized to solve a general design problem in a particular context.

<div dir="rtl">

مبحث DesignPattern به توضیحات پیرامون برقراری ارتباط با اشیاء و کلاس‌ها می‌پردازد که توسط آن این نحو ارتباط را برای رفع یک مشکل،‌ خاص منظوره می‌کند

* برخی از استانداردها با توجه به مشکل مدّنظر برای تنظیم روابط بین کلاس‌ها و آبجکت‌ها طراحی می‌شود تا سبب اقزایش بهنگی در کدنویسی گردد
* در یک پروژه همگان ملزم به تبعیت از آن الگو حواهند بود
* مبحث «الگوهای طراحی» یا Design Pattern، پیرو عنوان Object Oriented می‌باشد.
* بدلیل عدم وجود مشکل خاص در برخی «زبان‌های برنامه‌نویسی» گاهی یک «الگوهای طراحی» در آن زبان بدون کاربرد خواهد بود
* گاهی توسط شیوه کدنویسی یا Aspect Oriented مشکل برطرف می‌گردد و نیاز به استفاده از یک «الگوی طراحی» خاص نیست
* باید توجه داشت که ممکن است گاهی اتخاذ یک الگوی طراحی به اشتباه صورت گیرد و سبب گره در کدنویسی گردد


* Categories
    * Creational Patterns: الگوهای طراحی برمبنای ایجاد و ساخت «آبجکت»
        * Singleton: تنهای یک شیء از یک کلاس ساخته بشود و هربار شیء ساخته شده را مورد استفاده قرار دهد
        * FactoryMethod: پنهان‌سازی پیچیدگی‌های ساخت شیء برپایه وراثت( البته نیاز به نوشتن کد بیشتری دارد)
        * AbstractFactory: همانند FactoryMethodpattern بگونه Factory والد و Factory فرزند(داینامیک‌سازی کلاس فرزند) پیچیدگی زیاد کلاس‌ها را هنگام ایجاد شیء تسهیل می‌دهد. مناسب FrameWork نویسی زیرا پیچیدگی‌ها مرتفع می‌گردد
        * BuilderPattern: هنگام تولید آبجکت با تعددا پارامتر زیاد کاربرد دارد تا کارها و اقدام‌ها کاهش یابد
        * Prototype: اشیاء جدید توسط کپی از شیء موجود[بجای ایجاد شیء جدید از طریق توابع سازنده (Constructor)]
    * Structural Patterns: الگوهای طراحی بر مبنای «تنظیم روابط آبجکت‌ها» از نوع **ترکیب‌سازی** آبجکت‌ها با یکدیگر
        * Adapter:
        * Bridge:
        * Composite:
        * Decorator:
        * Facade:
        * Flyweight:
        * Proxy:
    * Behavioral Patterns: الگوهای‌طراحی برمبنای «تنظیم روابط‌آبجکت‌ها» از نوع استفاده یک آبجکت در آبجکت دیگر(رفع پیچیدگی)
        * Chain of responsibility:
        * Command:
        * Interpreter:
        * Iterator:
        * Mediator:
        * Memento:
        * Observer:
        * State:
        * Strategy:
        * template:
        * Visitor:

# 1. 🅰️ Singleton

* **ساخت تنها و تنها یک نمونه از یک شیء**: هربار که یک‌کلاس را New می‌کنیم آنگاه یک شیء جدید از آن کلاس بوجود می‌آید. درصورتی که بخواهیم با هربار New کردن شیء جدید ساخته نشود از این روش استفاده می‌کنیم.
* **تضمین کنترل منابع**: زمانی که محدودیت منابع وجود دارد مثلاً دیتابیس یا پرینتر یا فایل یا هرچیز دیگر که می‌خواهیم مطمئن بشویم که ارتباط با آن ریسورس تماماً با این کلاس صورت می‌گیرد
* این مدل طراحی دارای قاعده ثابت است(عدم انعطاف‌پذیر)
* مثال‌ها:
    * نمونه‌های رایج در جاوا: Runtime ، Logger
    * Spring Beans:در اسپرینگ تمامیBean هایی که ساخته می‌شوند بصورت پیش‌فرض از نوع سینگلتون است
    * وجود تنها یک پرینتر
    * کانکشن به دیتابیس
    * نکته: هرگاه به این تفکر برخوردید که نیاز به Stateهای متفاوت و Dataهای متفاوت است باید فکر سینگلتون را از ذهن خارج کرد
*

## 1.1. 🅱️ Design manual

* تنها با یک آبجکت راه‌اندازی می‌شود و نیاز به چندین آبجکت برای پیاده‌سازی ندارد.
* کلاس سینگلتون به این صورت است که یک Instance از خود کلاس Singleton درون سینگلتون وجود دارد یعنی خود کلاس، خودش را New کرده است. تک آبجکتی که قرار است همه به آن دسترسی پیدا کنند را داخل خود کلاس سینگلتون می‌گذاریم
* تک آبجکت را از نوع Private قرار می‌دهیم: وگرنه ممکن است در خلال کدنویسی Null یا دستکاری کند
* تک آبجکت را از نوع Static قرار می‌دهیم
* دارای تابع Constructor بدون پارامتر است
* برای اینکه کسی نتواند این کلاس را New نماید و آبجکت جدید بسازد:
    * متد Constructor آن را در حالت Private قرار می‌دهیم تا به هیچ عنوان قابلیت ساخت آبجکت جدید نداشته باشد، مگر از طریق ساخته شدن داخل خود کلاس آن
    * در آخر یک متد نهایی داریم که از نوع Public هست و همه از طریق آن به سینگلتون دسترسی دارند با نامی مثلاً GetInstance

![DesignPatternSingleton.png](./_srcFiles/Images/DesignPattern.png "DesignPatternSingleton.png")

در قطعه کد زیر اگر هش‌کد دو نمونه مساوی باشند آنگاه در خروجی تصریح خواهد شد

```java
Runtime firstInstance = Runtime.getRuntime();
firstinstance.gc(); //Garbage Collector //این موضوع فقط نمایش است وگرنه بصورت پیش‌فرض توسط جاوا اجرا می‌شود
System.out.println(firstInstance);

Runtime anotherInstance = Runtime.getRuntime();
System.out.println(anotherInstance);

if (firstInstance == anotherInstance){
    System.out.println("Two instance are equal");
}
```

## 1.2. 🅱️ Singleton Class

قطعه کد زیر یک نمونه از اتصال دیتابیس از نوع سینگلتون است:

```java
public class DBConnection {
   // متغیر از نوع Static است زیرا باید از کلاس یک نمونه شیء بیشتر ساخته نشود و هرکس خواست از این نمونه استفاده نماید
   // متغیر از نوع private است زیرا کسی نتواند این مقدار رو تغییر و مستقیماً از آن استفاده نماید
   private static DBConnection dbconnection = new DBConnection();
   
   // متد Constructor این کلاس ساخته شده و private تعریف شده است تا هیچ‌کس خارج کلاس نتواند از این تابع سازنده استفاده نماید. بعبارتی تابع سازنده آن قابل فراخوانی نیست و چون این کلاس تنها یک تابع سازنده دارد پس کسی نمی‌تواند از روی آن شی جدید بسازد
   private DBConnection(){}
   
   // متد getInstance تا هرکسی بخواهد نمونه‌ای از کلاس رو بگیرد شیء که یکبار ساخته شده است را فراخوانی نماید. خروجی بازگشتی از نوع singleton است
   public static DBConnection getInstance(){
      return dbConnection;
   }
}
```

در صورت استفاده از سینگلتون باید با دستور زیر شیء تولید کرد

```java
Singleton s = Singleton.getInstance();
```

در صورت استفاده از Singleton خط زیر **غلط** خواهد بود:

```java
Singleton s = new Singleton(); //غلط است
```

## 1.3. 🅱️ LazySingletonClass

طبق قاعده جاوا(در بحث Class Loading ) اولین Touch از یک کلاس(حتی Import در Junit ) سبب Instantiate از تمامی مقادیر استاتیک آن کلاس می‌شود. پس کلاس سینگلتون حتماً دارای یک نمونه آبجکت می‌باشد.حالا اگر برنامه بصورت سینگلتون باشد و حتی یک ارتباط با دیتابیس نداشته باشد آنگاه اتقلاف منابع خواهیم داشت(این مثال در برخی منابع ممکن است دارای Cost زیاد باشد) پس می‌توان قطعه کد بالا بصورت Lazy نگارش شود یعنی هرگاه به شیء نیاز شد آنگاه آبجکت تولید گردد

```java
public class DBConnection {
   private static DBConnection dbconnection = null;
   private DBConnection(){}
   public static DBConnection getInstance(){
      if(dbconnection == null){
         dbconnection = new DBConnection();
      }
      return dbConnection;
   }
}
```

## 1.4. 🅱️ ThreadSafeSingletonClass

این شرایط وجود دارد که کلاس را بعداً Thread safe نماییم: یعنی اگر برنامه در محیط Concurrent اجرا می‌شودوچندین Thread همزمان چندین کلاس را Instance نمایند آنگاه سبب بروز مشکل خواهد شد

روش 1️⃣️:

```java
public class DBConnection {
   private static DBConnection dbconnection = null();
   private DBConnection(){}
   public synchronized static DBConnection getInstance(){
      if(dbconnection == null){
         dbconnection = new DBConnection();
      }
      return dbConnection;
   }
}
```

روش 2️⃣️:

```java
public class DBConnection {
   private static DBConnection dbconnection = null();
   private DBConnection(){}
   public static DBConnection getInstance(){
      if(dbconnection == null)
         synchronized (DBConnection.class){
            if(dbconnection == null){
               dbconnection = new DBConnection();
            }
         }
     }
     return dbConnection;
   }
}
```

توضیحات: اگر یک thread داخل محدوده بلوک Synchronized قرار داشته باشد آنگاه اگر thread دوم به این بلاک برسد، صبر می‌کند تا thread اول از این بلاک عبور کند و سپس Thread دوم وارد این بلاک می‌شود.(پردازه برای دومی قفل می‌شود و با خروج اولی قفل آن باز می‌شود)


</div>

* DAO(DataAccessObject):  یک Design Pattern است. می‌گوید متدهای ادیت در دیتابیس را از یک کلاس اصلی جدا کرده و یک کلاس همنام با افزونه DAO بسازید و وظیفه واکشی و ثبت اطلاعات پیرامون کلاس اصلی را به آن بسپارید