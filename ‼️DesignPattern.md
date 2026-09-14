The Design Patterns are descriptions of communicating objects and class that are customized to solve a general design problem in a particular context.

<div dir="rtl">

مبحث DesignPattern به توضیحات پیرامون برقراری ارتباط با اشیاء و کلاس‌ها می‌پردازد که توسط آن این نحو ارتباط را برای رفع یک مشکل، خاص منظوره می‌کند

* برخی از استانداردها با توجه به مشکل مدّنظر برای تنظیم روابط بین کلاس‌ها و آبجکت‌ها طراحی می‌شود تا سبب اقزایش بهنگی در کدنویسی گردد
* در یک پروژه همگان ملزم به تبعیت از آن الگو حواهند بود
* مبحث «الگوهای طراحی» یا Design Pattern، پیرو عنوان Object Oriented می‌باشد.
* بدلیل عدم وجود مشکل خاص در برخی «زبان‌های برنامه‌نویسی» گاهی یک «الگوهای طراحی» در آن زبان بدون کاربرد خواهد بود
* گاهی توسط شیوه کدنویسی یا Aspect Oriented مشکل برطرف می‌گردد و نیاز به استفاده از یک «الگوی طراحی» خاص نیست
* باید توجه داشت که ممکن است گاهی اتخاذ یک الگوی طراحی به اشتباه صورت گیرد و سبب گره در کدنویسی گردد


* Categories
    * Creational Patterns: الگوهای طراحی برمبنای ایجاد و ساخت «آبجکت»
        * **Singleton**: تنهای یک شیء از یک کلاس ساخته بشود و هربار شیء ساخته شده را مورد استفاده قرار دهد
        * **FactoryMethod**: پنهان‌سازی پیچیدگی‌های ساخت شیء برپایه وراثت(البته نیاز به نوشتن کد بیشتری دارد)
        * **AbstractFactory**: همانند FactoryMethod-pattern بگونه Factory والد و Factory فرزند(داینامیک‌سازی کلاس فرزند) پیچیدگی زیاد کلاس‌ها را هنگام ایجاد شیء تسهیل می‌دهد. مناسب FrameWork نویسی زیرا پیچیدگی‌ها مرتفع می‌گردد
        * **Builder**: هنگام تولید آبجکت با تعداد پارامتر زیاد کاربرد دارد تا کارها و اقدام‌ها کاهش یابد
        * **Prototype**: به جای ایجاد شیء جدید از طریق توابع سازنده، اشیاء جدید توسط کپی از شیء موجود ایجاد شوند
    * Structural Patterns: الگوهای طراحی بر مبنای «تنظیم روابط آبجکت‌ها» از نوع **ترکیب‌سازی** آبجکت‌ها با یکدیگر
        * **Adapter**: تبدیل رابط یک کلاس به رابط دیگری که کلاینت انتظار دارد، تا کلاس‌های ناسازگار با هم بتوانند همکاری کنند.
        * **Bridge**: جداسازی یک انتزاع (abstraction) از پیاده‌سازی (implementation) آن، تا هر دو بتوانند مستقل از هم تغییر کنند.
        * **Composite**: ترکیب اشیاء به‌صورت ساختار درختی برای نمایش سلسله‌مراتب "کل-جزء"، به‌گونه‌ای که کلاینت یکسان با اجزای تکی و گروهی رفتار کند.
        * **Decorator**: افزودن مسئولیت‌های جدید به یک شیء به‌صورت پویا (بدون تغییر کد یا ارث‌بری)، با پیچیدن آن در یک شیء دکوراتور.
        * **Facade**: فراهم‌کردن یک رابط ساده و یکپارچه برای مجموعه‌ای از رابط‌های پیچیده یک زیرسیستم.
        * **Flyweight**: استفاده‌ی بهینه از حافظه با به‌اشتراک‌گذاری بخش‌های مشترک حالت اشیاء بین تعداد زیادی از آن‌ها.
        * **Proxy**: کنترل دسترسی به یک شیء با استفاده از یک جایگزین (نماینده) که همان رابط را پیاده‌سازی می‌کند (مثلاً برای lazy loading، امنیت، یا لاگ‌گیری).
    * Behavioral Patterns: الگوهای‌طراحی برمبنای «تنظیم روابط‌آبجکت‌ها» از نوع استفاده یک آبجکت در آبجکت دیگر(رفع پیچیدگی)
        * **Chain of Responsibility**: انتقال درخواست در یک زنجیره از گیرنده‌ها تا زمانی که یکی از آن‌ها آن را پردازش کند.
        * **Command**: کپسوله‌سازی یک درخواست به‌صورت یک شیء فرمان، برای پارامترسازی کلاینت‌ها با درخواست‌های مختلف یا پیاده‌سازی `undo` یا `redo`.
        * **Interpreter**: تعریف گرامر یک زبان ساده و یک مفسر برای آن زبان با استفاده از بازنمایی سلسله‌مراتبی از عبارات.
        * **Iterator**: دسترسی متوالی به عناصر یک مجموعه بدون افشای نمایش داخلی آن.
        * **Mediator**: کاهش وابستگی‌های پیچیده بین اشیاء با انتقال ارتباطات به یک شیء واسط (مدیریت تعاملات مرکزی).
        * **Memento**: ذخیره و بازیابی حالت داخلی یک شیء بدون نقض انکپسوله‌سازی — معمولاً برای پیاده‌سازی `undo`.
        * **Observer**: تعریف یک وابستگی یک‌به‌چند بین اشیاء به‌گونه‌ای که هنگام تغییر وضعیت یک شیء، همه وابسته‌ها به‌طور خودکار به‌روز شوند.
        * **State**: اجازه دادن به یک شیء که رفتارش را با تغییر حالت داخلی‌اش تغییر دهد، گویی کلاس آن تغییر کرده است.
        * **Strategy**: تعریف خانواده‌ای از الگوریتم‌ها، کپسوله‌سازی هرکدام و جایگزینی آن‌ها به‌صورت قابل تعویض در زمان اجرا.
        * **Template** Method: تعریف الگوریتمی در یک متد که برخی مراحل آن به زیرکلاس‌ها واگذار شده است — ساختار کلی ثابت است، ولی جزئیات توسط زیرکلاس‌ها پیاده‌سازی می‌شوند.
        * **Visitor**: افزودن عملکردهای جدید به مجموعه‌ای از کلاس‌ها بدون تغییر کد آن‌ها، با تعریف یک کلاس "بازدیدکننده" که بر روی آن‌ها عمل می‌کند.

# 1. 🅰️Creational.Singleton(تنها تولید یک شیءبه ازای هربار ساخت شیء جدید)

* **ساخت تنها و تنها یک نمونه از یک شیء**: در این روش هرگاه از یک کلاس یک شیء جدید می‌سازیم آنگاه فقط وفقط یک شیء ساخته‌می‌شود(همان شیء ساخته شده که برای اولین بار از این کلاس ساخته شده است)
* **تضمین کنترل منابع**: زمانی که محدودیت منابع(مثل:دیتابیس یا پرینتر یا فایل)وجود داشته باشد و بخواهیم تضیمن شود که ارتباط فقط باید از یک کلاس خاص صورت پذیرد
* این مدل طراحی دارای قاعده ثابت است(عدم انعطاف‌پذیر)
* تنها با یک آبجکت راه‌اندازی می‌شود و نیاز به چندین آبجکت برای پیاده‌سازی ندارد.
* نکته: هرگاه به این تفکر برخوردید که نیاز به Stateهای متفاوت و Dataهای متفاوت است باید فکر سینگلتون را از ذهن خارج کرد
* مثال‌ها:
    * وجود تنها یک پرینتر
    * کانکشن به دیتابیس

## 1.1. 🅱️Implement

کلاسی که قرار است تحت الگوی طراحی Singleton باشد باید از قواعد زیر پیروی کند

* درون کلاس یک آبجکت(Instance) از خود کلاس می‌سازیم
* دسترسی به این آبجکت را از درون کلاس میسر می‌نماییم
* تعریف متغیرهااز نوع private (برای محدودسازی دسترسی از بیرون)بدلیل عدم تغییر مستقیم در پارامترهای کلاس
* تک آبجکت را از نوع Static قرار می‌دهیم
* جهت جلوگیری از ساخت شیء جدید به ازای ساخته شدن شیء
    * قرار دادن متد Constructor در حالت private تا فقط از درون شیء بشود آبجکت جدید ساخته شود
    * یک متد public با نام getInstance برای دسترسی عمومی برای همه از بیرون ایجاد میکنیم تا هربار هنگام ساخت شیء این شیء مورد استفاده قرار بگیرد

## 1.2. 🅱️ python

```python
# ╔════════╗
# ║ Simple ║ پشتبانی از آرگومان ورودی ندارد و نمی‌توان به تابع سازنده چیزی بفرستید
# ╚════════╝
# گر بخواهید هنگام ساختن شیء مقداری بفرستید (مثلاً Singleton("config"))، کار نمی‌کند یا خطا می‌دهد.
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# ╔════════════╗
# ║ Singleton1 ║ # ❌️ Old_Version: super(Singleton, cls) -----> ✅️New_Version: super()
# ╚════════════╝
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not Singleton._instance:
            Singleton._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return Singleton._instance


# ╔════════════╗
# ║ Singleton2 ║
# ╚════════════╝
class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]
```

مثال1️⃣️: ConnectionPool ساده برای اتصال به دیتابیس

```python
import sqlite3


class DatabaseConnectionPool:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnectionPool, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize_pool()

        return cls._instance

    def _initialize_pool(self):
        self.connections = []

        for _ in range(5):
            conn = sqlite3.connect(':memory:')
            self.connections.append(conn)

    def get_connection(self):
        if not self.connections:
            raise Exception('There is no connection in the pool')

        return self.connections.pop()

    def release_connection(self, conn):
        self.connections.append(conn)


pool_1 = DatabaseConnectionPool()
pool_2 = DatabaseConnectionPool()

conn_1 = pool_1.get_connection()
cursor_1 = conn_1.cursor()
cursor_1.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT)")
cursor_1.execute("INSERT INTO products (name) VALUES ('Iphone')")
cursor_1.execute("INSERT INTO products (name) VALUES ('Samsung')")
conn_1.commit()

pool_1.release_connection(conn_1)

conn_2 = pool_2.get_connection()
cursor_2 = conn_2.cursor()
cursor_2.execute("SELECT * FROM products")
print(cursor_2.fetchall())
pool_2.release_connection(conn_2)
```

## 1.3. 🅱️java

* نمونه‌های رایج در جاوا: Runtime ، Logger
* Spring Beans:در اسپرینگ تمامیBean هایی که ساخته می‌شوند به‌صورت پیش‌فرض از نوع سینگلتون است
* دارای تابع Constructor بدون پارامتر است

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

```java
Singleton s = Singleton.getInstance(); // در صورت استفاده از سینگلتون باید اینگونه شیء تولید کرد
Singleton s = new Singleton(); //❌️ در صورت استفاده از Singleton این خط خواهد بود
```

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

### 1.3.1. ✅️LazySingletonClass

طبق قاعده جاوا(در بحث Class Loading ) اولین Touch از یک کلاس(حتی Import در Junit ) سبب Instantiate از تمامی مقادیر استاتیک آن کلاس می‌شود. پس کلاس سینگلتون حتماً دارای یک نمونه آبجکت می‌باشد.حالا اگر برنامه به‌صورت سینگلتون باشد و حتی یک ارتباط با دیتابیس نداشته باشد آنگاه اتقلاف منابع خواهیم داشت(این مثال در برخی منابع ممکن است دارای Cost زیاد
باشد) پس می‌توان قطعه کد بالا به‌صورت Lazy نگارش شود یعنی هرگاه به شیء نیاز شد آنگاه آبجکت تولید گردد

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

### 1.3.2. ✅️ThreadSafeSingletonClass

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

# 2. 🅰️Creational.Builder(مدیریت هزینه‌ها و منابع‌ها در هنگام تولید آبجکت با تعداد پارامتر زیاد)

هنگامی که شرایط زیر برقرار باشد می‌توان از این «الگوی‌طراحی» استفاده نمود

* هنگام **تولید آبجکت با تعداد پارامتر زیاد**
* هنگامی‌که ساخت آبجکت Cost زیاد دارد(مثل کوئری دیتابیس مثلا QuerySet در جنگو)
* هنگامی‌که نمونه‌های قابل تولید از کلاس(باتوجه به مقادیر) می‌تواند رفتار متفاوت داشته باشند
* **هدف‌ایجاد**: تسهیل مقداردهی پارامترهای زیاد هنگام ساخت کلاس به‌صورت یکجا
    * فراهم کردن یک رابط برای ساخت شیء پیچیده به‌صورت تدریجی و مرحله‌ای
* اجزا
    * **Product**:(محصول) شیء نهایی است که توسط Builder ساخته می‌شود.
    * **Builder**: یک رابط یا کلاس انتزاعی که مسئول ایجاد و عملیات ساخت بخش‌های مختلف شیء است.
    * **ConcreteBuilder**: پیاده‌سازی واقعی کلاس Builder است که جزئیات ساخت را انجام می‌دهد(کمک می‌کند تا فرآیند ساخت طبق دستورالعمل‌های مشخص پیش برود)
    * **Director**: مسئول هدایت فرآیند ساخت است (گاهی اوقات اختیاری است).
        * وقتی ترتیب توابع مهم باشد و الگوی خاصی مد نظر باشد از این ساختار استفاده می‌کنیم
        * اگر فرآیند ساخت پیچیده باشد، می‌توانیم از Director استفاده کنیم تا فرآیند ساخت تحت کنترل باشد.
        * اگر ساده باشد، می‌توانیم از Builder به‌طور مستقیم استفاده کنیم.
    * **Client**: مسئول درخواست از Builder برای ساخت شیء است.
* مثال: هنگام ایجاد یک کلاس QueryBuilder برای SQL که نیازمند تعداد پارامترهای زیاد نظیر موارد زیر می‌باشد:
    * تعداد اجزای Selection
    * دریافت تک به تک عبارت‌های شرطی که بعنوان where استفاده خواهد شد یا همانWhere clause ها
    * GroupBy ها
    * OrderBy ها و …
* نکات
    * استفاده از inner class ها دراین الگوی طراحی توصیه می‌شود
        * پیشنهاد می‌شود کلاس اصلی را به‌صورت innerClass درون کلاس Builder تعریف نمود تا پیچیدگی کاهش یابد
    * معمولاً اسم Builder را به انتهای کلاس می‌افزایند
    * متدهایی تحت عناوین مثلاً build یا getResult ایجاد نماییم تا بعنوان ارائه دهنده خروجی نهایی یا آبجکت نهایی عمل نماید

## 2.1. 🅱️ Python

```python
# ╔═════════╗
# ║ Product ║
# ╚═════════╝
class Computer:
    def __init__(self, processor, memory, storage, graphics):
        self.processor = processor
        self.memory = memory
        self.storage = storage
        self.graphics = graphics

    def __str__(self):
        return f"Computer with {self.processor} CPU, {self.memory}GB RAM, {self.storage}GB Storage, {self.graphics} Graphics."


# ╔═════════╗
# ║ Builder ║ # سازنده
# ╚═════════╝
from abc import ABC, abstractmethod


class ComputerBuilder(ABC):  # یک رابط است که تمامی متدهایی را که برای ساخت یک کامپیوتر نیاز داریم (مثلاً تنظیم پردازنده، حافظه، ذخیره‌سازی و گرافیک) را تعریف می‌کند.

    @abstractmethod
    def set_processor(self, processor: str):
        pass

    @abstractmethod
    def set_memory(self, memory: int):
        pass

    @abstractmethod
    def set_storage(self, storage: int):
        pass

    @abstractmethod
    def set_graphics(self, graphics: str):
        pass

    @abstractmethod
    def build(self) -> Computer:
        pass


# ╔═════════════════╗
# ║ ConcreteBuilder ║ # پیاده‌سازی واقعی سازنده
# ╚═════════════════╝
class GamingComputerBuilder(ComputerBuilder):

    def __init__(self):
        self.computer = Computer(None, None, None, None)

    def set_processor(self, processor: str):
        self.computer.processor = processor

    def set_memory(self, memory: int):
        self.computer.memory = memory

    def set_storage(self, storage: int):
        self.computer.storage = storage

    def set_graphics(self, graphics: str):
        self.computer.graphics = graphics

    def build(self) -> Computer:
        return self.computer


# ╔══════════╗
# ║ Director ║ # مسئول ساخت
# ╚══════════╝
class Director:  # فرآیند ساخت کامپیوترهای خاص را مدیریت می‌کند

    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def construct_gaming_computer(self):
        self.builder.set_processor("Intel i9")
        self.builder.set_memory(32)
        self.builder.set_storage(1024)
        self.builder.set_graphics("NVIDIA RTX 3080")

    def construct_office_computer(self):
        self.builder.set_processor("Intel i5")
        self.builder.set_memory(16)
        self.builder.set_storage(512)
        self.builder.set_graphics("Integrated")


# ╔════════╗
# ║ Client ║
# ╚════════╝
if __name__ == "__main__":  # استفاده از Director

    gaming_computer_builder = GamingComputerBuilder()
    director = Director(gaming_computer_builder)
    director.construct_gaming_computer()

    gaming_computer = gaming_computer_builder.build()
    print(gaming_computer)

    # استفاده از Director برای ساخت یک کامپیوتر اداری
    office_computer_builder = GamingComputerBuilder()  # می‌توان از همان کلاس برای ساخت نوع دیگری از کامپیوتر استفاده کرد
    director = Director(office_computer_builder)
    director.construct_office_computer()

    office_computer = office_computer_builder.build()
    print(office_computer)

###### output:
# Computer with Intel i9 CPU, 32GB RAM, 1024GB Storage, NVIDIA RTX 3080 Graphics.
# Computer with Intel i5 CPU, 16GB RAM, 512GB Storage, Integrated Graphics.
```

## 2.2. 🅱️ Java

* در جاوا کلاس‌هایی از جمله DocumentBuilder وStringBuilder و Locale.Builder یا JsonBuilder وجود دارد که در آن از این شیوه استفاده شده است

### 2.2.1. ✅️ StringBuilder

کلاس StringBuilder (موجود در Java.lang) قابلیت افزودن دیتا به یک رشته را به گونه‌ای دارد که بعنوان رشته اصلی عمل کرده و هر بار دیتای جدید مستقیماً با آن اضافه می‌شود و نیازبه ساخت شیء string جدید بعنوان subString نیست تا آن شیء را به رشته اصلی(شیء اصلی) append نماییم

```java
StringBuilder builder = new StringBuilder();
string result = builder.append("Hello, I am").append(33).append("years old").toString();
```

### 2.2.2. ✅️ H264PropertiesBuilder

#### 2.2.2.1. ❇️ without Builder

فرض کنید کلاس decoder فرمت H262 را بخواهیم پیاده‌سازی نماییم آنگاه بدلیل وجود پارامترهای زیاد، در حالت بدون Builder به شکل زیر می‌باشد(۱-کلاس سازنده با پارامتر زیاد ۲-getter برای هرکدام ۳-setter برای هرکدام)

```java
public class H263Properties{
    int keyInt;
    int minKeyInt;
    int sceneCut;
    int bFrames
    int bAdabt
    int qp
    int bitrate
    boolean bFrameBias
    int crf
    int qpstep
    int pbRatio
    int chromaOffset
    float rateTol
    byte pass
    boolean state
    int direct
    int meRange
    boolean weightB
    boolean noFastPSkip

    #تابع سازنده
    public  H263Properties(int keyInt, int minKeyInt, int sceneCut,int bFrames,int bAdabt, int qp, int bitrate, boolean bFrameBias, int crf, int qpstep, int pbRatio, int chromaOffset, float rateTol, byte pass, boolean state, int direct, int meRange, boolean weightB, boolean noFastPSkip){}

    #ایجاد کلاس سِتِر برای همه پارامترهای این کلاس
    public void setMinKeyInt(int minKeyInt){
        this.minKeyInt = minKeyInt;
        return this.minKeyInt = minKeyInt;
    }

    #ایجاد کلاس گِتِر برای همه پارامترهای این کلاس
    public int getMinKeyInt(){
        return minKeyInt;
    }
    
}
```

کلاس main شیوه بدون Builder به شکل زیر خواهد شد

```java
public class Main {
    public static void main(String[] args){
        H263Properties  decoder – new  H263Properties();
        decoder.setbAdapt(12) ;
        decoder.setbweghtB(yes) ;
        decoder.setrateTol (1.5) ;
        …
        تعداد بسیار زیاد باید تنظیم نماید
    }
}
```

#### 2.2.2.2. ❇️ with Builder

باید کلاسH264Properties بدون Builder را همانند بخش قبل داشته باشیم و همراه آن کلاس در وضعیت Builder نیز به شکل زیر تولید شود

```java
public class H263Properties‌Builder{
    int keyInt;
    int minKeyInt;
    int sceneCut;
    int bFrames
    int bAdabt
    int qp
    int bitrate
    boolean bFrameBias
    int crf
    int qpstep
    int pbRatio
    int chromaOffset
    float rateTol
    byte pass
    boolean state
    int direct
    int meRange
    boolean weightB
    boolean noFastPSkip

    #نوشت تابع مشابه سِتِر اما بدون کلمه سِتِر برای همه پارامترهای این کلاس به شکل زیر
    public  H263PropertiesBuilder MinKeyInt(int minKeyInt){ #نکته: کلمه سِت از نام تابع حذف شده است
        this.minKeyInt = minKeyInt;
        return this;
    }
    
    public H263Properties build() {
        H263Properties decoder = new  H263Properties();
        decoder.setbAdapt(badapt) ;
        decoder.setbweghtB(weightB) ;
        decoder.setrateTol (rateTol) ;
        ...
        //یک بار برای تک تک پارامترها مقدارها را قرار می‌دهیم
    }
}
```

کلاس main شیوه Builder به شکل زیر خواهد شد

```java
public class Main {
    public static void main(String[] args){
        H263Properties decoderBuilder = new  H263PropertiesBuilder();
        H263Properties decoder = builderDecoder.frame(12).KeyInt(17).rateTol(1.5).minKeyInt(2).sceneCut(9)……….build() ;
    }
}
```

* **نکته‌ها**
    * در کلاس Builder مقدار بازگشتی تابع Setter هرکدام از پارامترها باید به‌جای نوع(مثلا int یا string یا …) به نام کلاس تغییر پیدا کند
    * در کلاس Builder کلمه set از نام تابع بازگشتی حذف می‌شود
    * در کلاس Builder توابع getter همانند وضعیت بدون Builder خواهند بود
    * در کلاس Builder تابع build را ایجاد نماییم که قرار است خروجی نهایی رو برگرداند

# 3. 🅰️Creational.Prototype(به جای ایجاد شیء جدید از طریق توابع سازنده، اشیاء جدید توسط کپی از شیء موجود ایجاد شوند)

این امکان را می‌دهد که یک شیء جدید را از طریق کپی کردن شیء موجود و اعمال تغییرات بر روی نسخه‌های جدید، ایجاد کنید

* اغلب در موقعیت‌هایی استفاده می‌شود که نیاز به ایجاد نسخه‌های مشابه از یک شیء با تنظیمات خاص نیاز باشد
* **هدف**: جلوگیری از ساختن مکرر اشیاء مشابه است
    * زمانی که ایجاد اشیاء پیچیده هزینه‌بر است
    * زمانی که نیاز به ایجاد نسخه‌های مشابه با تفاوت‌های جزئی داریم
    * زمانی که تغییرات زیادی روی شیء انجام نمی‌دهید
    * زمانی که می‌خواهید تاریخچه از اشیاء ایجاد شده داشته باشید
* **Shallow Copy(کپی سطحی)**: یک کپی سطحی از شیء اصلی ایجاد می‌شود.
    * به این معنی که شیء جدید به شیء اصلی اشاره می‌کند (درواقع، به آن ارجاع داده می‌شود) در حالی که مقادیر اولیه (مثل لیست‌ها) به صورت مشترک بین شیء اصلی و کپی استفاده می‌شوند.
* **Deep Copy**: در این حالت، یک کپی کامل از شیء اصلی و تمام مقادیر داخلی آن ایجاد می‌شود. در این حالت، حتی شیء‌های داخلی (مثل لیست‌ها) نیز به طور کامل کپی می‌شوند و از شیء اصلی جدا می‌شوند.

## 3.1. 🅱️Python

```python
import copy


class Prototype:
    def __init__(self, name, data):
        self.name = name
        self.data = data  # یک لیست به عنوان داده

    def __str__(self):
        return f"Prototype(Name: {self.name}, Data: {self.data})"

    def clone_shallow(self):  # کپی سطحی (Shallow Copy)
        return copy.copy(self)

    def clone_deep(self):  # کپی عمیق (Deep Copy)
        return copy.deepcopy(self)


original_prototype = Prototype("Original", [1, 2, 3])
shallow_copy = original_prototype.clone_shallow()
deep_copy = original_prototype.clone_deep()

shallow_copy.data[0] = 100  # تغییر اولین عنصر در لیست کپی سطحی
deep_copy.data[1] = 200  # تغییر دومین عنصر در لیست کپی عمیق

# نمایش نتایج
print("Original Prototype:", original_prototype)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)

# بررسی حافظه
print("\nMemory Address of original prototype data:", id(original_prototype.data))
print("Memory Address of shallow copy data:", id(shallow_copy.data))
print("Memory Address of deep copy data:", id(deep_copy.data))

# output:
## -----> Original Prototype: Prototype(Name: Original, Data: [100, 2, 3])
## -----> Shallow Copy: Prototype(Name: Original, Data: [100, 2, 3])
## -----> Deep Copy: Prototype(Name: Original, Data: [1, 200, 3])
## -----> 
## -----> Memory Address of original prototype data: 140324630499072
## -----> Memory Address of shallow  copy      data: 140324630499072
## -----> Memory Address of deep     copy      data: 140324630507968

```

* DAO(DataAccessObject):  یک Design Pattern است. می‌گوید متدهای ادیت در دیتابیس را از یک کلاس اصلی جدا کرده و یک کلاس همنام با افزونه DAO بسازید و وظیفه واکشی و ثبت اطلاعات پیرامون کلاس اصلی را به آن بسپارید

# 4. 🅰️Creational.FactoryMethod(پنهان‌سازی پیچیدگی‌های ساخت شیء برپایه وراثت)

در این الگوی طراحی مسئولیت انتخاب نوع شیء و چگونگی پیاده‌سازی را به زیرکلاس‌ها واگذار می‌کند، در حالی که کلاس پایه الگوریتم کلی کار را حفظ می‌کند. به عبارتی در کلاس پایه(والد) می‌دانیم که چه کاری قرار است انجام شود ولی چگونگی انجام کار و پیاده‌سازی و اعمال پیچیدگی‌ها در زیرکلاس انجام خواهد شد

* **هدف‌ایجاد**:پنهان‌سازی پیچیدگی‌های ساخت شیء(برنامه‌نویس درگیر پیچیدگی‌های آبجکت‌ها نشود و به سهولت نمونه بسازد)
* این الگوی طراحی برپایه اصل وراثت بنا نهاده شده(Inheritance).نوع دقیق شیء توسط زیرکلاس‌ها مشخص می‌شود
* موارد کاربرد
    * زمانی که از سیستم cache استفاده می‌شود
    * .خصوصا زمانی که تولید نمونه‌ها پرهزینه خواهد بود(ارتباط با دیتابیس، پرینتر، اسکنر،دیوایس‌های External وغیره)
        * یک راه دیگر این است که می‌توان نمونه‌ها را در فضای استاتیک نگهداری کرد و در ه‍ربار فراخوانی فقط از آن استفاده نمود
* مثال
    * کلاسی برای تبدیل فرمت عکس به فرمت‌های گوناگون(JPG, PNG, GIF, SVG, غیره) که در آن «ساختارکلاس» و پارامترهای هر فرمت نسبت به دیگری منحصربه‌فرد خواهد بود
    * Number Format: نوع اعداد فارسی یا عربی یا فرمت انگلیسی باشد
    * Resource Bundle: ایجاد نمونه متفاوت برحسب تنظیمات
    * Calendar: نوع تقویم جلالی یا میلادی یا هجری‌قمری یا عبری یا پهلوی یا غیره باشد(قطعه‌کد زیر که برحسب منطقه خاص می‌تواند Locale بپذیرد)
* این الگوی طراحی به کد قابلیت گسترش می‌دهد(در مثال تغییر فرمت تصاویر به یکدیگر می‌توانیم به سهولت یک فرمت جدید بیافزاییم)
* برای کدنویسی در این الگوی طراحی از تایپ هینت‌های پیشرفته(نظیر استفاده از TypeVar و Generic) برای حفظ دقت نوع در سلسله مراتب کلاس استفاده نمایید
* استفاده از if-else درون FactoryMethod نشان دهنده این است که طراحی ضعیف است. هر شرط باید به یک زیرکلاس تبدیل شود.
* ساده‌ترین قانون
    * اگر نیاز دارید همیشه چند شیء خاص با هم کار کنند، از الگوی طراحی Abstract Factory استفاده کنید.
    * اگر فقط یک شیء با واریانت‌های مختلف دارید، از الگوی طراحی Factory Method استفاده کنید

## 4.1. 🅱️ PythonExample

```python
from abc import ABC, abstractmethod


# ╔════════════╗
# ║ Example1️⃣️: ║ 
# ╚════════════╝
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass


class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()


class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()


️
######✅️ ====> Alternative for Animal,AnimalFactory
######✅️ class Animal:
######✅️     def speak(self):
######✅️         raise NotImplementedError
######✅️ class AnimalFactory:
######✅️     def create_animal(self):
######✅️         raise NotImplementedError

# Ussing
print(DogFactory().create_animal().speak())  # Woof!
print(CatFactory().create_animal().speak())  # Meow!

# ╔════════════╗
# ║ Example2️⃣️: ║ 
# ╚════════════╝
from abc import ABC, abstractmethod


# region Vehicle Abstract class

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        raise NotImplementedError


# endregion

# region Vehicles

class Car(Vehicle):
    def move(self):
        print('car is moving...')


class Truck(Vehicle):
    def move(self):
        print('truck is moving...')


class Motorcycle(Vehicle):
    def move(self):
        print('motorcycle is moving...')


# endregion

# region Vehicle Abstract Class

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> 'Vehicle':
        raise NotImplementedError


# endregion

# region Vehicle Factories

class CarFactory(VehicleFactory):
    def create_vehicle(self) -> 'Vehicle':
        return Car()


class TruckFactory(VehicleFactory):
    def create_vehicle(self) -> 'Vehicle':
        return Truck()


class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self) -> 'Vehicle':
        return Motorcycle()


# endregion

# region Get Vehicle Factory

def get_vehicles_factory(vehicle_type: str) -> 'VehicleFactory':
    factories = {
        'car': CarFactory,
        'truck': TruckFactory,
        'motorcycle': MotorcycleFactory
    }

    if vehicle_type in factories:
        return factories[vehicle_type]()

    raise ValueError('Your desired vehicle factory not found')


# endregion

# region Client Code

if __name__ == '__main__':
    vehicle_factory = get_vehicles_factory('car')
    vehicle = vehicle_factory.create_vehicle()
    print(vehicle)
    vehicle.move()

# endregion

# ╔════════════╗
# ║ Example3️⃣️: ║ 
# ╚════════════╝
from abc import ABC, abstractmethod


# ======================
# 1. محصول انتزاعی (قرارداد رفتاری)
# ======================
class PaymentProcessor(ABC):
    """
    رابط انتزاعی برای تمام درگاه‌های پرداخت.
    تضمین می‌کند همه درگاه‌ها حداقل این دو رفتار را پیاده‌سازی کنند.
    """

    @abstractmethod
    def pay(self, amount: float) -> str:
        """دریافت مبلغ و بازگرداندن پیام تراکنش"""
        pass

    @abstractmethod
    def get_gateway_name(self) -> str:
        """بازگرداندن نام درگاه پرداخت"""
        pass


# ======================
# 2. محصولات ملموس (پیاده‌سازی‌های واقعی)
# ======================
class ZarinpalProcessor(PaymentProcessor):
    """درگاه پرداخت زرین‌پال"""

    def pay(self, amount: float) -> str:
        return f"✅ پرداخت {amount:,} تومان از طریق زرین‌پال موفقیت‌آمیز بود."

    def get_gateway_name(self) -> str:
        return "زرین‌پال"


class PayPingProcessor(PaymentProcessor):
    """درگاه پرداخت پی‌پینگ"""

    def pay(self, amount: float) -> str:
        return f"✅ پرداخت {amount:,} تومان از طریق پی‌پینگ تأیید شد."

    def get_gateway_name(self) -> str:
        return "پی‌پینگ"


# ======================
# 3. سازنده انتزاعی (منطق کلی کسب‌وکار)
# ======================
class PaymentService(ABC):
    """
    کلاس پایه‌ای که:
    - منطق اصلی پرداخت را پیاده‌سازی می‌کند (process_payment)
    - ساخت شیء را به زیرکلاس‌ها واگذار می‌کند (_create_processor)
    - به جزئیات پیاده‌سازی درگاه وابسته نیست
    """

    @abstractmethod
    def _create_processor(self) -> PaymentProcessor:
        """
        Factory Method اصلی:
        - هر زیرکلاس نوع درگاه را مشخص می‌کند
        - نام با _ نشان‌دهنده داخلی بودن و عدم استفاده مستقیم توسط کلاینت
        """
        pass

    def process_payment(self, amount: float) -> None:
        """
        منطق کسب‌وکار اصلی (یکسان برای همه درگاه‌ها):
        1. ساخت درگاه از طریق Factory Method
        2. اجرای پرداخت
        3. لاگ‌گیری یکدست
        """
        processor = self._create_processor()  # تمرکز الگو: ساخت به زیرکلاس واگذار شد
        result = processor.pay(amount)
        print(f"\n[سیستم] تراکنش از طریق {processor.get_gateway_name()}:")
        print(result)


# ======================
# 4. سازنده‌های ملموس (انتخاب نوع درگاه)
# ======================
class ZarinpalService(PaymentService):
    """سرویس پرداخت با درگاه زرین‌پال"""

    def _create_processor(self) -> PaymentProcessor:
        return ZarinpalProcessor()


class PayPingService(PaymentService):
    """سرویس پرداخت با درگاه پی‌پینگ"""

    def _create_processor(self) -> PaymentProcessor:
        return PayPingProcessor()


# ======================
# 5. استفاده در دنیای واقعی (کلاینت)
# ======================
def main():
    print("=" * 50)
    print("سیستم پرداخت فروشگاه آنلاین")
    print("=" * 50)

    # لیست سرویس‌های پرداخت (بدون نیاز به if-else برای انتخاب درگاه!)
    services = [
        ZarinpalService(),
        PayPingService()
    ]

    # پردازش پرداخت برای هر درگاه
    for service in services:
        service.process_payment(150000)  # مبلغ ثابت برای تست

    # ✨ نکته طلایی گسترش:
    # برای افزودن درگاه جدید (مثلاً آیدی‌پی):
    # 1. کلاس IdPayProcessor از PaymentProcessor بسازید
    # 2. کلاس IdPayService از PaymentService ارث ببرد و _create_processor را پیاده‌سازی کند
    # 3. در لیست services اضافه کنید
    # → هیچ خط از کد موجود تغییر نمی‌کند! (اصل Open/Closed)


if __name__ == "__main__":
    main()

# ╔════════════╗
# ║ Example4️⃣️: ║ 
# ╚════════════╝

from abc import ABC, abstractmethod
from typing import Final


# =============================================================================
# 📌 توضیح ساختار پیاده‌سازی:
# - این پیاده‌سازی **فقط** از الگوی "فکتوری متد" استفاده می‌کند.
# - **هیچ "فکتوری کلاس" (Simple Factory) در این کد وجود ندارد**.
#   (فکتوری کلاس = کلاسی با منطق شرطی داخلی مثل if/else برای انتخاب نوع شیء)
# - تمام تصمیم‌گیری‌ها از طریق ارث‌بری و پیاده‌سازی متد توسط زیرکلاس‌ها انجام می‌شود.
# =============================================================================


# ======================
# 1. محصول انتزاعی: قرارداد رفتاری برای همه درگاه‌های ارسال پیامک
# ======================
class SMSProvider(ABC):
    """رابط انتزاعی برای تمام درگاه‌های ارسال پیامک"""

    @abstractmethod
    def send(self, phone: str, message: str) -> bool:
        """ارسال پیامک به شماره مشخص با متن داده‌شده"""
        pass

    @abstractmethod
    def get_provider_name(self) -> str:
        """بازگرداندن نام درگاه ارائه‌دهنده سرویس"""
        pass


# ======================
# 2. محصولات ملموس: پیاده‌سازی‌های واقعی درگاه‌ها
# ======================
class KaveNegarProvider(SMSProvider):
    """درگاه پیامک کاوه نگار"""

    def send(self, phone: str, message: str) -> bool:
        # در پیاده‌سازی واقعی، اینجا ارتباط با API کاوه نگار برقرار می‌شود
        print(f"📡 در حال ارسال از طریق کاوه نگار به {phone}...")
        return True  # فرض موفقیت‌آمیز بودن برای مثال

    def get_provider_name(self) -> str:
        return "کاوه نگار"


class SignalProvider(SMSProvider):
    """درگاه پیامک سیگنال"""

    def send(self, phone: str, message: str) -> bool:
        # در پیاده‌سازی واقعی، اینجا ارتباط با API سیگنال برقرار می‌شود
        print(f"📡 در حال ارسال از طریق سیگنال به {phone}...")
        return True  # فرض موفقیت‌آمیز بودن برای مثال

    def get_provider_name(self) -> str:
        return "سیگنال"


# ======================
# 3. سازنده انتزاعی: تعریف چارچوب کلی ارسال پیامک
# ======================
class SMSProviderService(ABC):
    """
    کلاس پایه‌ای که:
    - منطق اصلی ارسال پیامک را پیاده‌سازی می‌کند (send_message)
    - ساخت شیء درگاه را به زیرکلاس‌ها واگذار می‌کند
    - به جزئیات پیاده‌سازی درگاه وابسته نیست
    """

    # =========================================================================
    # 🔑 این متد، همان "فکتوری متد" است!
    # - متد انتزاعی که توسط زیرکلاس‌ها پیاده‌سازی می‌شود
    # - تصمیم "کدام درگاه ساخته شود" را به زیرکلاس واگذار می‌کند
    # - هسته اصلی الگوی فکتوری متد
    # =========================================================================
    @abstractmethod
    def _create_sms_provider(self) -> SMSProvider:
        """فکتوری متد: مسئول ساخت نمونه‌ی درگاه پیامک"""
        pass

    def send_message(self, phone: str, message: str) -> None:
        """
        منطق کسب‌وکار اصلی (یکسان برای همه درگاه‌ها):
        1. ساخت درگاه از طریق فکتوری متد
        2. ارسال پیامک
        3. گزارش نتیجه
        """
        # مرحله 1: دریافت درگاه از طریق فکتوری متد (بدون دانستن نوع دقیق)
        provider: SMSProvider = self._create_sms_provider()

        # مرحله 2: ارسال پیامک با استفاده از رابط انتزاعی
        success = provider.send(phone, message)

        # مرحله 3: گزارش نتیجه
        status = "✅ موفق" if success else "❌ ناموفق"
        print(f"[سیستم] ارسال از طریق {provider.get_provider_name()} به {phone}: {status}")


# ======================
# 4. سازنده‌های ملموس: پیاده‌سازی فکتوری متد برای هر درگاه
# ======================
class KaveNegarService(SMSProviderService):
    """سرویس ارسال پیامک با درگاه کاوه نگار"""

    # =========================================================================
    # 🔑 این پیاده‌سازی، همان "فکتوری متد" برای درگاه کاوه نگار است!
    # - هر زیرکلاس نوع خاص خود را مشخص می‌کند
    # - بدون نیاز به تغییر کد کلاس پایه
    # =========================================================================
    def _create_sms_provider(self) -> SMSProvider:
        return KaveNegarProvider()


class SignalService(SMSProviderService):
    """سرویس ارسال پیامک با درگاه سیگنال"""

    # =========================================================================
    # 🔑 این پیاده‌سازی، همان "فکتوری متد" برای درگاه سیگنال است!
    # =========================================================================
    def _create_sms_provider(self) -> SMSProvider:
        return SignalProvider()


# ======================
# 5. استفاده در دنیای واقعی (کلاینت)
# ======================
def main() -> None:
    """اجرای نمونه‌ی سیستم ارسال پیامک"""
    print("=" * 60)
    print("سیستم ارسال پیامک - پیاده‌سازی استاندارد فکتوری متد")
    print("=" * 60)

    # لیست سرویس‌های پیامک (بدون هیچ شرط‌بندی برای انتخاب درگاه!)
    services: list[SMSProviderService] = [
        KaveNegarService(),
        SignalService()
    ]

    # ارسال پیامک از هر درگاه
    phone_number: Final[str] = "09123456789"
    message: Final[str] = "سلام! کد تأیید شما: 123456"

    for idx, service in enumerate(services, 1):
        print(f"\n{'─' * 58}")
        print(f"ارسال شماره {idx} با {service.__class__.__name__}")
        print(f"{'─' * 58}")
        service.send_message(phone_number, message)

    # ✨ نکته طلایی گسترش:
    # برای افزودن درگاه جدید (مثلاً فارس‌پی):
    # 1. کلاس FarapayamProvider از SMSProvider بسازید
    # 2. کلاس FarapayamService از SMSProviderService ارث ببرد
    # 3. متد _create_sms_provider را در FarapayamService پیاده‌سازی کنید
    # 4. نمونه‌ی FarapayamService را به لیست services اضافه کنید
    # → هیچ خط از کد موجود تغییر نمی‌کند! (اصل باز بودن برای گسترش، بسته بودن برای تغییر)

    # 📌 یادآوری مهم:
    # - "فکتوری متد" = متد انتزاعی _create_sms_provider و پیاده‌سازی‌های آن در زیرکلاس‌ها
    # - "فکتوری کلاس" (Simple Factory) در این پیاده‌سازی وجود ندارد.
    #   (اگر وجود داشت، یک کلاس واحد با متدی شامل if/else برای انتخاب درگاه می‌بود)


if __name__ == "__main__":
    main()
```

## 4.2. 🅱️ Example-Java

```java
import java.util.Calendar;
Calendar x = Calendar.getInstance(Locale.English); #getInstance is Factory
System.out.println(x);
System.out.println(x.get(Calendar.SECOND));
```

* مثال: در مسئله تبدیل فرمت‌تصاویر یک اینترفیس بنام «ImageConvertor» خواهیم داشت که همه «کلاس‌های فرزند» با این اینترفیس تعامل برقرار خواهند کرد و این اینترفیس یک متد بنام Convert خواهد داشت که اطلاعات را میگیرد و خروجی را برمی‌گرداند

به کلاس زیر و نیز پیاده‌سازی‌های آن توجه نمایید

```java
public abstract class Calculation {
    protected int amountPerMonth;
    protected int taxPercent;
    protected string product;

    public Calculation(int amountPerMonth, int taxPercent, string product) {
        this.amountPerMonth =  amountPerMonth;
        this.taxPercent = taxPercent;
        this.product= product;
    }

    public abstract int calculate();
}
```

پیاده‌سازی از نوع Calculation1 :

```java
public class Calculation1 extends Calculation {
    public Calculation1(int amountPerMonth, int taxPercent, string product) {
        super(amountPerMonth, taxPercent, product);
    }
    @Override
    public abstract int calculate() {
        return amountPerMonth * taxPercent + 200;
    }
}
```

پیاده‌سازی از نوع Calculation2 :

```java
public class Calculation2 extends Calculation {
    public Calculation2(int amountPerMonth, int taxPercent, string product) {
        super(amountPerMonth, taxPercent, product);
    }
    @Override
    public abstract int calculate() {
        return amountPerMonth * taxPercent;
    }
}
```

پیاده‌سازی FactoryClass :

```java
public class CalculationFactory {
    public Calculation createCalculation(int amountPerMonth, int taxPercent, string product, boolean flag) {
        if (flag) {
            return new Calculation1(amountPerMonth, taxPercent, product);
        } else {
            return new Calculation2(amountPerMonth, taxPercent, product);
        }
    }
}
```

# 5. 🅰️Creational.AbstractFactory(همانند FactoryMethod فقط هنگام پیچیدگی بیشتر)

الگوی Abstract Factory یک الگوی طراحی از نوع Creational (سازنده) است که برای ساخت خانواده‌ای از اشیای مرتبط یا وابسته به هم، بدون مشخص کردن کلاس دقیق آن‌ها استفاده می‌شود.به زبان ساده:به‌جای اینکه مستقیماً از کلاس‌ها نمونه بسازیم (new)، یک کارخانه می‌سازیم که خودش اشیای مرتبط را برای ما تولید می‌کند.

* کارخانه‌ای که خودش کارخانه تولید می‌کند. یعنی Factory والد و Factory فرزند
* کاربرد در سیستم‌های بزرگ و آبجکت‌های سنگین که بخواهند ساخت کلاس فرزند را dynamic کنند.
* وجود interfaceهای مشترک از 2 گروه الف: به ازای هر Factory ب:به ازای هر کلاس‌هایی که داخل Factory است
* مثال کلاس Document Builder: برای Parse کردن فایلXML که یک آبجکت Node به‌صورت درختی برمی‌گرداند که می‌توان به تمامی المنت‌هایxml مورد نظر دسترسی پیدا کرد
* نکات
    * گروهی از factory ها دارای interface مشترک خواهند بودو با هم استفاده می‌شوند
    * abstract Factory ‌ها گروهی از Factory ها هستند که همواره برای ساخته شدن آن‌ها باید ابتدا از یک Factory شروع کرد و سپس به abstractFactory رسید.
    * پیچیدگی در پیاده‌سازی
    * نیاز به abstraction های زیاد
    * الگویی مناسب برای framework ها محسوب می‌شود.(Framework نویس‌ها)

## 5.1. 🅱️ PythonExamples

مثال اول:

```python
from abc import ABC, abstractmethod


# === محصولات انتزاعی (قرارداد خانواده) ===
class Button(ABC):
    @abstractmethod
    def click(self): pass


class Checkbox(ABC):
    @abstractmethod
    def check(self): pass


# === کارخانه انتزاعی (قرارداد ساخت خانواده) ===
class GUIFactory(ABC):  # همزمان دکمه و چک‌باکس می‌سازد و تضمین می‌کند هر دو از یک خانواده (ویندوز یا مک) باشند
    @abstractmethod
    def create_button(self) -> Button: pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox: pass  # ← تفاوت با Factory Method: چند محصول!


# === خانواده ویندوز ===
class WindowsButton(Button):
    def click(self): return "کلیک دکمه ویندوزی"


class WindowsCheckbox(Checkbox):
    def check(self): return "تیک چک‌باکس ویندوزی"


class WindowsFactory(GUIFactory):
    def create_button(self): return WindowsButton()

    def create_checkbox(self): return WindowsCheckbox()  # ← همه محصولات یک خانواده


# === خانواده مک ===
class MacFactory(GUIFactory):
    def create_button(self): return MacButton()  # فرض وجود

    def create_checkbox(self): return MacCheckbox()
```

مثال دوم: سناریو: دو تم UI داریم (Light/Dark) و هر تم باید Button و Checkbox هم‌ساز خودش را تولید کند

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


# ---------- Abstract Products (Interfaces) ----------
class Button(Protocol):
    def render(self) -> str:
        ...


class Checkbox(Protocol):
    def render(self) -> str:
        ...


# ---------- Concrete Products ----------
@dataclass(frozen=True)
class LightButton:
    def render(self) -> str:
        return "LightButton"


@dataclass(frozen=True)
class DarkButton:
    def render(self) -> str:
        return "DarkButton"


@dataclass(frozen=True)
class LightCheckbox:
    def render(self) -> str:
        return "LightCheckbox"


@dataclass(frozen=True)
class DarkCheckbox:
    def render(self) -> str:
        return "DarkCheckbox"


# ---------- Abstract Factory ----------
class UIAbstractFactory(Protocol):
    # یک خانواده محصولات مرتبط را تولید می‌کند
    def create_button(self) -> Button:
        ...

    def create_checkbox(self) -> Checkbox:
        ...


# ---------- Concrete Factories ----------
class LightThemeFactory:
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()


class DarkThemeFactory:
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()


# ---------- Client ----------
def build_screen(factory: UIAbstractFactory) -> str:
    """
    کلاینت فقط factory انتزاعی را می‌گیرد و محصولات را می‌سازد؛
    هیچ وابستگی به کلاس‌های concrete ندارد.
    """
    btn = factory.create_button()
    cb = factory.create_checkbox()
    return f"Screen[{btn.render()} + {cb.render()}]"


if __name__ == "__main__":
    print(build_screen(LightThemeFactory()))
    print(build_screen(DarkThemeFactory()))
```

مثال سوم[کاربردی و پیشرفته‌تر]: سیستم نوتیفیکیشن چندکاناله

```python
from abc import ABC, abstractmethod
from typing import Final


# =============================================================================
# 📌 بخش ۱: محصولات انتزاعی (قرارداد برای هر کانال)
# =============================================================================
class Notifier(ABC):
    """قرارداد ارسال نوتیفیکیشن"""

    @abstractmethod
    def send(self, message: str) -> bool:   pass


class Logger(ABC):
    """قرارداد لاگ‌گیری رویدادها"""

    @abstractmethod
    def log(self, event: str) -> None:    pass


# =============================================================================
# 📌 بخش ۲: محصولات ملموس — خانواده SMS
# =============================================================================
class SMSNotifier(Notifier):
    def send(self, message: str) -> bool:
        print(f"📱 ارسال پیامک: {message}")
        return True  # در عمل: ارتباط با API


class SMSLogger(Logger):
    def log(self, event: str) -> None:
        print(f"📝 [پیامک] لاگ: {event}")


# =============================================================================
# 📌 بخش ۳: محصولات ملموس — خانواده ایمیل
# =============================================================================
class EmailNotifier(Notifier):
    def send(self, message: str) -> bool:
        print(f"✉️ ارسال ایمیل: {message}")
        return True


class EmailLogger(Logger):
    def log(self, event: str) -> None:
        print(f"📝 [ایمیل] لاگ: {event}")


# =============================================================================
# 📌 بخش ۴: کارخانه انتزاعی (هسته الگو)
# =============================================================================
class NotificationFactory(ABC):
    """
    کارخانه انتزاعی برای ساخت خانواده کامل نوتیفیکیشن.
    تضمین می‌کند که Notifier و Logger همیشه از یک خانواده باشند.
    """

    @abstractmethod
    def create_notifier(self) -> Notifier:
        """ساخت کامپوننت ارسال پیام"""
        pass

    @abstractmethod
    def create_logger(self) -> Logger:
        """ساخت کامپوننت لاگ‌گیری"""
        pass


# =============================================================================
# 📌 بخش ۵: کارخانه‌های ملموس (پیاده‌سازی خانواده‌ها)
# =============================================================================
class SMSNotificationFactory(NotificationFactory):
    """کارخانه خانواده پیامک"""

    def create_notifier(self) -> Notifier:
        return SMSNotifier()

    def create_logger(self) -> Logger:
        return SMSLogger()  # ← همیشه با هم استفاده می‌شوند


class EmailNotificationFactory(NotificationFactory):
    """کارخانه خانواده ایمیل"""

    def create_notifier(self) -> Notifier:
        return EmailNotifier()

    def create_logger(self) -> Logger:
        return EmailLogger()  # ← همیشه با هم استفاده می‌شوند


# =============================================================================
# 📌 بخش ۶: کلاینت — استفاده صحیح از خانواده‌ها
# =============================================================================
def send_notification(factory: NotificationFactory, message: str) -> None:
    """
    تابع کلاینت که:
    - به جزئیات پیاده‌سازی وابسته نیست
    - از کارخانه برای دریافت کل خانواده استفاده می‌کند
    - تضمین می‌کند کامپوننت‌ها با هم سازگار باشند
    """
    # دریافت کل خانواده از یک کارخانه
    notifier = factory.create_notifier()
    logger = factory.create_logger()

    # استفاده هماهنگ از کامپوننت‌های خانواده
    if notifier.send(message):
        logger.log(f"پیام '{message}' ارسال شد")
    else:
        logger.log(f"خطا در ارسال پیام '{message}'")


# =============================================================================
# 📌 اجرای نمونه
# =============================================================================
def main():
    print("🚀 سیستم نوتیفیکیشن چندکاناله\n")

    # ارسال از طریق خانواده پیامک
    print("─" * 50)
    print("ارسال با کانال پیامک:")
    print("─" * 50)
    sms_factory = SMSNotificationFactory()
    send_notification(sms_factory, "کد تأیید: 789012")

    # ارسال از طریق خانواده ایمیل
    print("\n" + "─" * 50)
    print("ارسال با کانال ایمیل:")
    print("─" * 50)
    email_factory = EmailNotificationFactory()
    send_notification(email_factory, "سفارش شما ثبت شد")

    # ✨ گسترش آینده:
    # برای افزودن کانال پوش‌نوتیفیکیشن:
    # 1. PushNotifier و PushLogger بسازید
    # 2. PushNotificationFactory از NotificationFactory ارث ببرد
    # 3. در تابع send_notification هیچ تغییری نیاز نیست!


if __name__ == "__main__":
    main()

# ╔═════════╗
# ║ OUTPUT: ║ 
# ╚═════════╝

# 🚀 سیستم نوتیفیکیشن چندکاناله
# 
# ──────────────────────────────────────────────────
# ارسال با کانال پیامک:
# ──────────────────────────────────────────────────
# 📱 ارسال پیامک: کد تأیید: 789012
# 📝 [پیامک] لاگ: پیام 'کد تأیید: 789012' ارسال شد
# 
# ──────────────────────────────────────────────────
# ارسال با کانال ایمیل:
# ──────────────────────────────────────────────────
# ✉️ ارسال ایمیل: سفارش شما ثبت شد
# 📝 [ایمیل] لاگ: پیام 'سفارش شما ثبت شد' ارسال شد
```

## 5.2. 🅱️ JavaExamples

مثال اول DocumentBuilderFactory:

```java
DocumentBuilderFactory abstractFactory = DocumentBuilderFActory.newInstance();
DocumentBuilder documentBuilder = abstractFactory.newDocumentBuilder();
Document document = documentBuilder.pars(new ByteArrayInputStream("<person><firstName>Behrooz</firstName><lastName>MohammadiNasab</lastName></person>".getBytes(“UTF-8”)));
document.normalizeDocument();
System.out.println(documentBuilder.getClass());
System.out.println(document.getClass());
```

مثال دوم MediaConverterFactory

```java
MediaConverterFactory abstraactFactory =
          MediaConverterAbstractFactory.createFactory(Converter.Type.IMAGE);
try{
      Converter converter = abstractFactory.createConverter(new File(“/FileName/Directions/pic1.bmp”),Converter.CodeTypes.JPG);
      System.out.println(abstractFactory.getClass());
      System.out.println(converter.getClass());
      byte[] bytes = converter.doConvert();
} catch (FileNotFountExeption | ConvertionExeption e) { e.printStachTrace(); }

public interface MediaConverterAbstractFactory {
   static MediaConverterFactory createFactory(Converter.Type type) {
      switch (type) {
         case AUDIO:
            return new MusicConverterFactory();
         case VIDEO:
            return new VideoConverterFactory();
         case Image:
            return new ImageConverterFactory();
      }
      throw new OllegalArgumentsException(“Wrong Converter Type”);
   }
}

public class ImageConverterFactory implements MediaConverterFactory {
   public Converter createConverter(File file, Converter.CodecTypes toImageType)
      throws FileNotFoundException {
         String name = file.getName().toLowerCase();
         if (name.endWith(“.bmp”)){ 
            switch (toImageType){
               case JPG:
                  return new BmpToJpgConverter(file);
               // AND MORE
            }
         }
         throw new IllegalArgumentException(“No Converter Found”);
   }
}
```

که کار آن این است که در حالت‌های موسیقی و ویدئو و عکس بتواند فرمت‌های متفاوت را تبدیل نماید.

# 6. 🅰️ Behavioral.Command(انجام عملیات تحت آبجکت مستقل)

الگویی است که یک «دستور یا درخواست یا عملیات» را به‌جای اینکه مستقیم و فوری اجرا کند ابتدا آن را بعنوان یک آبجکت مستقل درنظر می‌گیرد. آبجکتی که تمام اطلاعات لازم برای انجام دستور نظیر گیرندهٔ عملیات، پارامترها، و … را در خودش نگه می‌دارد نتیجه این است که فرستندهٔ درخواست(Invoker) از اجراکنندهٔ واقعی(Receiver) جدا می‌شود و در این خلال می‌توان علمیات
متفاوت نظیر صف‌کردن، ذخیره‌کردن، لاگ‌گرفتن، اجرای با تأخیر، و Undo یا Redo را نیز داشته باشیم و هندل نماییم

به زبان ساده: به‌جای اینکه “کلیک روی دکمه” مستقیم برود و “کد روشن‌کردن چراغ” را صدا بزند، یک آبجکت Command می‌سازید که می‌گوید «روشن‌کردن چراغ با این پارامترها»، بعد دکمه فقط execute() را صدا می‌زند.

* معمولا در موارد زیر استفاده می‌شود
    * **کاهش وابستگی(Decoupling)**: فراخوانی کننده(Invoker) نداند دقیقاً چه کسی یا چگونه کار را انجام می‌دهد. فقط بداند «یک کامند قابل اجرا» دارد.
    * **تغییرپذیری‌رفتار درزمان‌اجرا**: بتوانید به یک دکمه یا منو یا روش روتین، فرمان‌های مختلف وصل کنید.
    * **صف‌واجرای باتأخیر**: فرمان‌ها را در Queue نگه دارید و بعداً یا در یک Worker اجرا کنید
    * ثبت‌وبازپخش (Macro یا History یا Auditing): فرمان‌ها را ذخیره کنید و دوباره اجرا کنید(مثل macro recording)
    * Undo یا Redo: با نگه‌داشتن تاریخچهٔ فرمان‌های اجراشده و پیاده‌سازی `undo()` بتوانید بازگشت انجام دهید
    * تراکنش و Rollback: چند عملیات را پشت سر هم اجرا کنید و اگر یکی شکست خورد، قبلی‌ها را برگردانید(مفهوم rollback شبیه‌تراکنش)
* اجزای اصلی این الگوی‌طراحی
    * جزء **Command**: «اینترفیس» یا «پروتکلِ‌فرمان»(مثلاً `execute()` و گاهی `undo()`).
    * جزء **ConcreteCommand**: پیاده‌سازی مشخص یک فرمان (مثل TurnOnLightCommand).
    * جزء **Receiver**: کسی که کار واقعی را انجام می‌دهد (مثل Light که متد `on()` دارد).
    * جزء **Invoker**: کسی که فرمان را اجرا می‌کند (مثل RemoteButton یا منو). معمولاً فقط `command.execute()` را صدا می‌زند.
    * جزء **Client**: کسی که همه چیز را سرِ هم می‌کند: Receiver را می‌سازد، ConcreteCommand می‌سازد و به Invoker می‌دهد
* جریان اجرا به صورت عادی:
    * Client → (Create Receiver + Command) → Connect Command to Invoker → Invoker: execute() → Do Command on Receiver
* صف یا Queue(محل نگهداری تسک‌ها یا جاب‌ها که خودش کاری نمی‌کند و فقط داده را نگه‌می‌دارد) و پروسس یا worker(پردازه که تسک را از صف برمیدارد و آن را اجرا میکند) متفاوت هستند
* به صف، Broker هم می‌گویند
* جزء کامند باید چه چیزی را در خود نگه دارد
    * حداقل باید مرجع Receiver به همراه پارامترهای لازم را نگهداری کند
    * برای Undo باید وضعیت قبل را هم ذخیره کند، یا بتواند «عمل معکوس» را انجام دهد
* برای اعمال Undo/Redo استاندارد
    * رویکرد اول **InverseOperation**: هر فرمان `undo()` دارد که اثر همان فرمان را برمی‌گرداند (مثلاً Reserve → Release).
    * رویکرد دوم **Snapshot/Memento**: قبل از `execute()` یک snapshot از حالت لازم ذخیره می‌کنید و در `undo()` آن را برمی‌گردانید (مخصوصاً وقتی برگشت‌پذیری با عملیات معکوس سخت است).
    * استفاده از History
        * `undo_stack`: بعد از اجرای موفق، فرمان را push می‌کنید.
        * `redo_stack`: وقتی undo می‌کنید، فرمان به redo می‌رود؛ وقتی redo می‌کنید دوباره برمی‌گردد
* دستورات مرکب(Composite): یک فرمان می‌توند خودش شامل چند فرمان باشد
    * `execute()` همه را به ترتیب اجرا کند
    * `undo()` همه را برعکس برگرداند
* تفاوت‌ها با دیگر الگوهای طراحی مشابه
    * Strategy: الگوی طراحی استراتژی معمولاً «الگوریتم یا سیاست» را برای یک کار انتخاب می‌کند؛ کامند بیشتر «یک درخواست/اکشن» را آبجکت می‌کند تا «زمان اجرا» یا «صف» یا «تاریخچه» یا «آندو» داشته باشد.
    * Observer/Event: الگوی طراحی آبزرو برای «خبر کردن چند شنونده» است؛ کامند برای «نمایندگی یک عمل».
    * ChainOfResponsibility: درخواست در یک زنجیره پاس می‌شود تا یکی هندل کند؛ در کامند، درخواست از قبل به شکل آبجکت فرمان ساخته شده و فراخوانی کننده آن را اجرا می‌کند.

## 6.1. 🅱️ Examples

مثال 1️⃣️:

```python
from abc import ABC, abstractmethod


# -------------------- device interface --------------------
class Device(ABC):
    @abstractmethod
    def turn_on(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def turn_off(self, *args, **kwargs):
        raise NotImplementedError


# -------------------- devices --------------------
class TV(Device):
    def turn_on(self, *args, **kwargs):
        print('TV is on')

    def turn_off(self, *args, **kwargs):
        print('TV is off')


class DVDPlayer(Device):
    def turn_on(self, *args, **kwargs):
        print('DVD Player is on')

    def turn_off(self, *args, **kwargs):
        print('DVD Player is off')


# -------------------- Command Interface --------------------
class RemoteControlCommand(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError


# -------------------- commands --------------------
class TurnOnCommand(RemoteControlCommand):
    def __init__(self, device: Device):
        self.device = device

    def execute(self):
        self.device.turn_on()


class TurnOffCommand(RemoteControlCommand):
    def __init__(self, device: Device):
        self.device = device

    def execute(self):
        self.device.turn_off()


# -------------------- Invoker --------------------
class RemoteControl:
    def __init__(self):
        self.commands = {}

    def add_command(self, command_name: str, command: RemoteControlCommand):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            raise KeyError(f'Command {command_name} does not exist')


# -------------------- client --------------------
if __name__ == '__main__':
    remote_control = RemoteControl()
    tv = TV()
    dvd_player = DVDPlayer()
    remote_control.add_command('turn_on_tv', TurnOnCommand(tv))
    remote_control.add_command('turn_off_tv', TurnOffCommand(tv))
    remote_control.add_command('turn_on_dvd', TurnOnCommand(dvd_player))
    remote_control.add_command('turn_off_dvd', TurnOffCommand(dvd_player))
    for key, value in remote_control.commands.items():
        print(f'command name is : {key}')

    remote_control.execute_command(input('enter your command: '))
```

مثال 2️⃣️: کنترل از راه دور به همراه Undo در پیاده‌سازی

* Receiver: `Light`
* Commands: روشن یا خاموش
* Invoker:  RemoteControl که یک “دکمه” دارد و آخرین فرمان را برای undo نگه می‌دارد
* Remote(Invoker) هیچ‌وقت `light.on()` را مستقیم صدا نمی‌زند؛ فقط `command.execute()` را می‌شناسد.
* کامندها «درخواست» را آبجکت کرده‌اند و بنابراین undo هم طبیعی می‌شود

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Optional


# -------- Command Interface --------
class Command(Protocol):
    """قرارداد فرمان: حداقل execute و (برای این مثال) undo."""

    def execute(self) -> None: ...

    def undo(self) -> None: ...


# -------- Receiver --------
@dataclass
class Light:
    """Receiver: کار واقعی اینجاست."""
    is_on: bool = False

    def on(self) -> None:
        self.is_on = True
        print("💡 Light: ON")

    def off(self) -> None:
        self.is_on = False
        print("💡 Light: OFF")


# -------- Concrete Commands --------
@dataclass(frozen=True)
class LightOnCommand:
    """فرمان روشن کردن چراغ."""
    light: Light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        # معکوسِ روشن‌کردن: خاموش‌کردن
        self.light.off()


@dataclass(frozen=True)
class LightOffCommand:
    """فرمان خاموش کردن چراغ."""
    light: Light

    def execute(self) -> None:
        self.light.off()

    def undo(self) -> None:
        # معکوسِ خاموش‌کردن: روشن‌کردن
        self.light.on()


# -------- Invoker --------
class RemoteControl:
    """
    Invoker: فقط می‌داند یک Command دارد و execute() را صدا می‌زند.
    از Light و جزئیاتش خبر ندارد.
    """

    def __init__(self) -> None:
        self._slot: Optional[Command] = None
        self._last: Optional[Command] = None  # برای Undo

    def set_command(self, command: Command) -> None:
        self._slot = command

    def press_button(self) -> None:
        if self._slot is None:
            print("Remote: no command set")
            return
        self._slot.execute()
        self._last = self._slot

    def press_undo(self) -> None:
        if self._last is None:
            print("Remote: nothing to undo")
            return
        self._last.undo()
        self._last = None


if __name__ == "__main__":
    light = Light()
    remote = RemoteControl()

    remote.set_command(LightOnCommand(light))
    remote.press_button()  # ON
    remote.press_undo()  # undo -> OFF

    remote.set_command(LightOffCommand(light))
    remote.press_button()  # OFF
    remote.press_undo()  # undo -> ON

```

مثال 3️⃣️: اجرای تراکنش سفارش به همراه Rollback به همراه History در داخل مثال

* سناریو: برای ثبت سفارش، چند عملیات پشت سر هم انجام می‌شود:
    1. رزرو موجود
    2. شارژ پرداخت
    3. ساخت ارسال یا حمل‌ونقل(یا همان Shipment)
    4. ارسال ایمیل تأیید(اختیاری/جبرانی)
* اگر هرمرحله شکست خورد، مراحل قبلی باید rollback شوند(باundo). این دقیقاً یکی از جاهایی است که Command خیلی ارزشمند می‌شود

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, List, Optional
import uuid


# -------------------- Command Protocols --------------------
class UndoableCommand(Protocol):
    """
    فرمان‌های قابل بازگشت (برای rollback و undo/redo).
    نکته: در سیستم‌های واقعی ممکن است undo "کاملاً برگشت" نباشد
    و به شکل عملیات جبرانی (compensating action) انجام شود.
    """

    def execute(self) -> None: ...

    def undo(self) -> None: ...

    def describe(self) -> str: ...


# -------------------- Receivers (Business Services) --------------------
@dataclass
class InventoryService:
    stock: dict[str, int]
    reserved: dict[str, int]

    def reserve(self, sku: str, qty: int) -> None:
        available = self.stock.get(sku, 0)
        if qty <= 0:
            raise ValueError("qty must be positive")
        if available < qty:
            raise RuntimeError(f"Not enough stock for {sku}. available={available}, need={qty}")

        self.stock[sku] = available - qty
        self.reserved[sku] = self.reserved.get(sku, 0) + qty

    def release(self, sku: str, qty: int) -> None:
        if qty <= 0:
            raise ValueError("qty must be positive")
        reserved_qty = self.reserved.get(sku, 0)
        if reserved_qty < qty:
            raise RuntimeError(f"Release exceeds reserved for {sku}. reserved={reserved_qty}, release={qty}")

        self.reserved[sku] = reserved_qty - qty
        self.stock[sku] = self.stock.get(sku, 0) + qty


@dataclass
class PaymentService:
    """
    مدل ساده‌شده پرداخت.
    در دنیای واقعی باید idempotency-key، وضعیت تراکنش، و خطاهای شبکه را مدیریت کنید.
    """
    charges: dict[str, int]  # charge_id -> amount_cents
    refunds: dict[str, int]  # refund_id -> amount_cents

    def charge(self, amount_cents: int) -> str:
        if amount_cents <= 0:
            raise ValueError("amount must be positive")
        charge_id = f"ch_{uuid.uuid4().hex[:10]}"
        self.charges[charge_id] = amount_cents
        return charge_id

    def refund(self, charge_id: str) -> str:
        if charge_id not in self.charges:
            raise RuntimeError("Cannot refund: unknown charge_id")
        refund_id = f"rf_{uuid.uuid4().hex[:10]}"
        self.refunds[refund_id] = self.charges[charge_id]
        return refund_id


@dataclass
class ShippingService:
    shipments: dict[str, str]  # shipment_id -> order_id
    canceled: set[str]

    def create_shipment(self, order_id: str) -> str:
        shipment_id = f"sh_{uuid.uuid4().hex[:10]}"
        self.shipments[shipment_id] = order_id
        return shipment_id

    def cancel_shipment(self, shipment_id: str) -> None:
        if shipment_id not in self.shipments:
            raise RuntimeError("Unknown shipment_id")
        self.canceled.add(shipment_id)


@dataclass
class EmailService:
    sent: List[str]

    def send(self, to: str, subject: str, body: str) -> None:
        # نمونه ساده: فقط ذخیره در لیست
        self.sent.append(f"to={to} subject={subject} body={body}")


# -------------------- Concrete Commands --------------------
@dataclass
class ReserveStockCommand:
    inventory: InventoryService
    sku: str
    qty: int
    _executed: bool = False  # برای جلوگیری از undo قبل از execute

    def execute(self) -> None:
        self.inventory.reserve(self.sku, self.qty)
        self._executed = True

    def undo(self) -> None:
        if self._executed:
            self.inventory.release(self.sku, self.qty)

    def describe(self) -> str:
        return f"ReserveStock(sku={self.sku}, qty={self.qty})"


@dataclass
class ChargePaymentCommand:
    payments: PaymentService
    amount_cents: int
    charge_id: Optional[str] = None

    def execute(self) -> None:
        self.charge_id = self.payments.charge(self.amount_cents)

    def undo(self) -> None:
        # عملیات جبرانی: refund
        if self.charge_id is not None:
            self.payments.refund(self.charge_id)

    def describe(self) -> str:
        return f"ChargePayment(amount_cents={self.amount_cents})"


@dataclass
class CreateShipmentCommand:
    shipping: ShippingService
    order_id: str
    shipment_id: Optional[str] = None

    def execute(self) -> None:
        self.shipment_id = self.shipping.create_shipment(self.order_id)

    def undo(self) -> None:
        if self.shipment_id is not None:
            self.shipping.cancel_shipment(self.shipment_id)

    def describe(self) -> str:
        return f"CreateShipment(order_id={self.order_id})"


@dataclass
class SendEmailCommand:
    email: EmailService
    to: str
    subject: str
    body: str
    _sent: bool = False

    def execute(self) -> None:
        self.email.send(self.to, self.subject, self.body)
        self._sent = True

    def undo(self) -> None:
        # ایمیل معمولاً قابل undo واقعی نیست.
        # در سیستم واقعی ممکن است "ایمیل اصلاحی/لغو" بفرستید یا هیچ کاری نکنید.
        pass

    def describe(self) -> str:
        return f"SendEmail(to={self.to}, subject={self.subject})"


# -------------------- Transaction Runner (Invoker-like) --------------------
class TransactionRunner:
    """
    این کلاس یک لیست از Commandها را اجرا می‌کند.
    اگر یکی شکست بخورد، فرمان‌های اجراشده را برعکس undo می‌کند (rollback).
    این دقیقاً همان کاربرد transactional/rollback در Command است. :contentReference[oaicite:13]{index=13}
    """

    def __init__(self) -> None:
        self.audit_log: List[str] = []

    def run(self, commands: List[UndoableCommand]) -> None:
        executed: List[UndoableCommand] = []
        try:
            for cmd in commands:
                self.audit_log.append(f"EXEC: {cmd.describe()}")
                cmd.execute()
                executed.append(cmd)
            self.audit_log.append("DONE: transaction committed")
        except Exception as exc:
            self.audit_log.append(f"ERROR: {type(exc).__name__}: {exc} -> rollback")
            # rollback در جهت معکوس
            for cmd in reversed(executed):
                try:
                    self.audit_log.append(f"UNDO: {cmd.describe()}")
                    cmd.undo()
                except Exception as undo_exc:
                    # در سیستم واقعی: اینجا باید alert/compensation اضافی داشته باشید
                    self.audit_log.append(f"UNDO-FAILED: {cmd.describe()} err={undo_exc}")
            raise


# -------------------- Demo --------------------
if __name__ == "__main__":
    inventory = InventoryService(stock={"SKU-1": 2}, reserved={})
    payments = PaymentService(charges={}, refunds={})
    shipping = ShippingService(shipments={}, canceled=set())
    email = EmailService(sent=[])

    order_id = "ORDER-1001"

    # یک سناریوی موفق
    tx1 = TransactionRunner()
    commands_ok: List[UndoableCommand] = [
        ReserveStockCommand(inventory, "SKU-1", 1),
        ChargePaymentCommand(payments, 5000),
        CreateShipmentCommand(shipping, order_id),
        SendEmailCommand(email, "user@example.com", "Order confirmed", f"Your order {order_id} is confirmed."),
    ]
    tx1.run(commands_ok)

    print("=== Audit (OK) ===")
    print("\n".join(tx1.audit_log))
    print("stock:", inventory.stock, "reserved:", inventory.reserved)
    print("charges:", payments.charges, "refunds:", payments.refunds)
    print("shipments:", shipping.shipments, "canceled:", shipping.canceled)
    print("emails:", email.sent)

    # یک سناریوی شکست (کمبود موجودی) که باید rollback کند
    tx2 = TransactionRunner()
    commands_fail: List[UndoableCommand] = [
        ReserveStockCommand(inventory, "SKU-1", 5),  # اینجا خطا می‌دهد
        ChargePaymentCommand(payments, 7000),
        CreateShipmentCommand(shipping, "ORDER-FAIL"),
    ]
    try:
        tx2.run(commands_fail)
    except Exception:
        pass

    print("\n=== Audit (FAIL + rollback) ===")
    print("\n".join(tx2.audit_log))
    print("stock:", inventory.stock, "reserved:", inventory.reserved)

```

* نکته‌های کلیدی این مثال
    * هر قدم کسب‌وکار یک Command جداست؛ بنابراین اضافه/حذف/تعویض قدم‌ها آسان می‌شود.
    * rollback با undo در جهت معکوس انجام می‌شود (خیلی مهم برای حفظ سازگاری).
    * بعضی عملیات‌ها undo واقعی ندارند (مثل ایمیل). اینجا مفهوم عملیات جبرانی مطرح می‌شود.
    * این سبک طراحی پایهٔ خیلی از سیستم‌های workflow، orchestration و حتی sagas (در مقیاس بزرگ‌تر) است.

# 7. 🅰️ Behavioral.Mediator(ارتباط همه کامپوننت‌ها فقط ازطریق واسط)

```text
  ┌─────────┐        ┌─────────┐         ┌─────────┐
  │  شیء A  │         │  شیء B  │        │  شیء C  │
  └────┬────┘        └────┬────┘         └────┬────┘
       │                  │                   │
       │همگان تنها با واسط(میانجی) حرف می‌زنند │
       │                  │                   │
       ▼                  ▼                   ▼
  ┌────────────────────────────────────────────────┐
  │              Mediator (میانجی)                 │
  │   می‌داند چه زمان  باید به چه شیء پیام بدهد     │
  └────────────────────────────────────────────────┘
```

* این الگوی طراحی تحت عنوان میانجی شناخته می‌شود.
* ارتباطات پیچیده و درهم‌تنیده بین اشیاء را متمرکز می‌کند. به جای اینکه اشیاء مستقیماً یکدیگر را بشناسند و صدا بزنند، همه از طریق یک شیء میانجی (Mediator) با هم ارتباط می‌گیرند
* مزایا
    * کاهش وابستگی: کامپوننت‌ها همدیگر را نمی‌شناسند
    * تغییر آسان: افزودن کامپوننت جدید = تغییر فقط میانجی
    * تست‌پذیری: هر کامپوننت جداگانه تست می‌شود
    * خوانایی: منطق ارتباط در یک جا متمرکز است
* ️ معایب
    * میانجی بزرگ: اگر مراقب نباشید، میانجی تبدیل به یک «خدای همه‌کاره» (God Object) می‌شود
    * اگر میانجی خراب شود، کل سیستم از کار می‌افتد
    * پیچیدگی پنهان: فهم جریان برنامه سخت‌تر می‌شود چون همه‌چیز از یک نقطه رد می‌شود

## 7.1. 🅱️ Examples1

چت‌روم به عنوان Mediator عمل می‌کند. هر کاربر فقط پیامش را به چت‌روم می‌دهد و چت‌روم آن را به بقیه می‌رساند.

```python
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class ChatMediator(ABC):
    """رابط انتزاعی میانجی برای چت‌روم.
    هر میانجی یا mediator باید بتواند پیام یک فرستنده را به بقیه برساند."""

    @abstractmethod
    def send_message(self, message: str, sender: "User") -> None:
        """ارسال پیام از طرف یک کاربر به بقیه کاربران.

        Args:
            message: متن پیام.
            sender: کاربری که پیام را فرستاده (تا به خودش برنگردد).
        """
        pass


class ChatRoom(ChatMediator):
    """چت‌روم به عنوان میانجی مرکزی.
    تمام پیام‌ها از اینجا عبور می‌کنند.
    هیچ کاربری مستقیماً با کاربر دیگر ارتباط ندارد."""

    def __init__(self) -> None:
        self._users: List[User] = []

    def add_user(self, user: "User") -> None:
        """افزودن کاربر به چت‌روم.

        Args:
            user: کاربری که وارد چت‌روم می‌شود.
        """
        self._users.append(user)

    def send_message(self, message: str, sender: "User") -> None:
        """ارسال پیام به همه کاربران به جز فرستنده.

        Args:
            message: متن پیام.
            sender: فرستنده پیام (خودش پیام را دریافت نمی‌کند).
        """
        for user in self._users:
            if user is not sender:
                user.receive(message)


class User:
    """کاربر چت.
    هر کاربر فقط یک میانجی (چت‌روم) را می‌شناسد و هیچ اطلاعی از بقیه کاربران ندارد.
    """

    def __init__(self, name: str, mediator: ChatMediator) -> None:
        """
        Args:
            name: نام کاربر.
            mediator: چت‌رومی که کاربر در آن عضو است.
        """
        self.name = name
        self._mediator = mediator

    def send(self, message: str) -> None:
        """ارسال پیام از طریق میانجی.

        Args:
            message: متن پیام ارسالی.
        """
        print(f"[{self.name}] ارسال: {message}")
        self._mediator.send_message(message, self)

    def receive(self, message: str) -> None:
        """دریافت پیام از میانجی.
        Args:
            message: متن پیام دریافتی.
        """
        print(f"  ← [{self.name}] دریافت: {message}")


# ─── استفاده ───
if __name__ == "__main__":
    # ۱. ساخت چت‌روم (Mediator)
    room = ChatRoom()

    # ۲. ساخت کاربران (همه فقط چت‌روم را می‌شناسند)
    ali = User("علی", room)
    sara = User("سارا", room)
    reza = User("رضا", room)

    # ۳. عضویت در چت‌روم
    room.add_user(ali)
    room.add_user(sara)
    room.add_user(reza)

    # ۴. علی پیام می‌فرستد → سارا و رضا دریافت می‌کنند
    ali.send("سلام، سرور اصلی بالا اومد!")
    # خروجی:
    # [علی] ارسال: سلام، سرور اصلی بالا اومد!
    #   ← [سارا] دریافت: سلام، سرور اصلی بالا اومد!
    #   ← [رضا] دریافت: سلام، سرور اصلی بالا اومد!
```

## 7.2. 🅱️ Examples2

پیاده‌سازی مثال بالا به روش دیگر: چت‌روم به عنوان Mediator عمل می‌کند. هر کاربر فقط پیامش را به چت‌روم می‌دهد و چت‌روم آن را به بقیه می‌رساند.

```python
from abc import ABC, abstractmethod
from typing import Any, List


# region mediator interface

class Mediator(ABC):
    @abstractmethod
    def notify(self, message: str, sender: Any):
        raise NotImplementedError

    @abstractmethod
    def add_component(self, component: 'Component'):
        raise NotImplementedError


# endregion

# region components

class Component:
    def __init__(self, mediator: Mediator, name: str) -> None:
        self.name = name
        self._mediator = mediator
        # mediator.add_component(self)

    def __repr__(self):
        return f'<Component name={self.name} />'

    def __str__(self):
        return repr(self)

    def send(self, message: str) -> None:
        self._mediator.notify(message, self)

    def receive(self, message: str) -> None:
        print(f'{self} received {message}')


# endregion

# region concrete mediator

class ConcreteMediator(Mediator):
    def __init__(self):
        self._components: List[Component] = []

    def add_component(self, component: Component):
        if component not in self._components:
            self._components.append(component)

    def notify(self, message: str, sender: Any):
        for component in self._components:
            if component != sender:
                component.receive(message)


# endregion

# region client

if __name__ == '__main__':
    # mediator object
    mediator_object = ConcreteMediator()

    # components
    component_1 = Component(mediator_object, 'Component 1')
    component_2 = Component(mediator_object, 'Component 2')
    component_3 = Component(mediator_object, 'Component 3')

    # add components to mediator
    mediator_object.add_component(component_1)
    mediator_object.add_component(component_2)
    mediator_object.add_component(component_3)

    # send message
    component_1.send(message='this is component 1 message')
    print('----------')
    component_3.send(message='this is component 3 message')

# endregion

# python3 main.py 
# output: <Component name=Component 2 /> received this is component 1 message
# output: <Component name=Component 3 /> received this is component 1 message
# output: ----------
# output: <Component name=Component 1 /> received this is component 3 message
# output: <Component name=Component 2 /> received this is component 3 message

```

## 7.3. 🅱️ Examples3

سیستم هماهنگی سفارش فروشگاه آنلاین
چالش: وقتی مشتری سفارشی ثبت می‌کند، چندین ماژول باید به ترتیب فعال شوند:

1. انبار → موجودی را چک کند
2. پرداخت → پول را کسر کند
3. ارسال → بسته را بفرستد

بدون Mediator، ماژول «انبار» باید ماژول «پرداخت» را بشناسد و مستقیماً صدا بزند. ماژول «پرداخت» باید «ارسال» را بشناسد. اگر فردا ماژول «فاکتور» اضافه شود، باید کد همه ماژول‌ها را تغییر دهید.

راه‌حل: یک OrderMediator می‌سازیم که تمام هماهنگی‌ها را مدیریت کند.

```python
from __future__ import annotations
from abc import ABC, abstractmethod


class OrderMediator(ABC):
    """رابط انتزاعی Mediator یا همان میانجی برای هماهنگی فرآیند سفارش.

    هر کامپوننت (انبار، پرداخت، ارسال) رویدادهای خود را به این میانجی گزارش می‌دهد و میانجی تصمیم می‌گیرد مرحله بعدی چیست.
    """

    @abstractmethod
    def notify(self, sender: str, event: str) -> None:
        """اطلاع‌رسانی یک رویداد و تصمیم‌گیری برای مرحله بعد.

        Args:
            sender: نام کامپوننت فرستنده (مثل 'inventory').
            event: نوع رویداد (مثل 'stock_confirmed').
        """
        ...


class OrderSystem(OrderMediator):
    """میانجی یا mediator اصلی سیستم سفارش.

    این کلاس تنها جایی است که منطق ترتیب مراحل سفارش نوشته شده. هیچ کامپوننتی از مرحله بعدی خبر ندارد.
    """

    def __init__(self) -> None:
        # ساخت کامپوننت‌ها و تزریق Mediator به آن‌ها
        self.inventory = Inventory(self)
        self.payment = Payment(self)
        self.shipping = Shipping(self)
        self.notification = Notification(self)

    def notify(self, sender: str, event: str) -> None:
        """مدیریت جریان سفارش بر اساس رویدادها.

        Args:
            sender: کامپوننتی که رویداد را فرستاده.
            event: نوع رویداد رخ‌داده.
        """
        if event == "order_placed":
            print("📦 سفارش ثبت شد")
            print("   → بررسی موجودی انبار...")
            self.inventory.check_stock()

        elif event == "stock_confirmed":
            print("✅ موجودی تأیید شد")
            print("   → شروع فرآیند پرداخت...")
            self.payment.process()

        elif event == "payment_done":
            print("💳 پرداخت موفق")
            print("   → هماهنگی ارسال بسته...")
            self.shipping.dispatch()

        elif event == "shipped":
            print("🚚 بسته ارسال شد")
            print("   → ارسال پیامک به مشتری...")
            self.notification.send_sms()

        elif event == "sms_sent":
            print("📱 پیامک ارسال شد")
            print("🎉 فرآیند سفارش تکمیل!")


class Inventory:
    """ماژول انبار - فقط میانجی را می‌شناسد."""

    def __init__(self, mediator: OrderMediator) -> None:
        self._mediator = mediator

    def check_stock(self) -> None:
        """بررسی موجودی و اطلاع‌رسانی به میانجی."""
        print("      [انبار] کالا موجود است ✓")
        self._mediator.notify("inventory", "stock_confirmed")


class Payment:
    """ماژول پرداخت - فقط میانجی را می‌شناسد."""

    def __init__(self, mediator: OrderMediator) -> None:
        self._mediator = mediator

    def process(self) -> None:
        """پردازش پرداخت و اطلاع‌رسانی به Mediator."""
        print("      [پرداخت] مبلغ ۲,۵۰۰,۰۰۰ تومان کسر شد ✓")
        self._mediator.notify("payment", "payment_done")


class Shipping:
    """ماژول ارسال - فقط میانجی را می‌شناسد."""

    def __init__(self, mediator: OrderMediator) -> None:
        self._mediator = mediator

    def dispatch(self) -> None:
        """ارسال بسته و اطلاع‌رسانی به Mediator."""
        print("      [ارسال] کد رهگیری: ۱۲۳۴۵۶۷۸۹ ✓")
        self._mediator.notify("shipping", "shipped")


class Notification:
    """ماژول اطلاع‌رسانی - فقط میانجی را می‌شناسد."""

    def __init__(self, mediator: OrderMediator) -> None:
        self._mediator = mediator

    def send_sms(self) -> None:
        """ارسال پیامک و اطلاع‌رسانی به Mediator."""
        print("      [پیامک] «سفارش شما ارسال شد» ✓")
        self._mediator.notify("notification", "sms_sent")


# ─── استفاده ───
if __name__ == "__main__":
    system = OrderSystem()

    # فقط یک رویداد اولیه → بقیه مراحل خودکار طی می‌شود
    system.notify("customer", "order_placed")

    # خروجی:
    # 📦 سفارش ثبت شد
    #    → بررسی موجودی انبار...
    #       [انبار] کالا موجود است ✓
    # ✅ موجودی تأیید شد
    #    → شروع فرآیند پرداخت...
    #       [پرداخت] مبلغ ۲,۵۰۰,۰۰۰ تومان کسر شد ✓
    # 💳 پرداخت موفق
    #    → هماهنگی ارسال بسته...
    #       [ارسال] کد رهگیری: ۱۲۳۴۵۶۷۸۹ ✓
    # 🚚 بسته ارسال شد
    #    → ارسال پیامک به مشتری...
    #       [پیامک] «سفارش شما ارسال شد» ✓
    # 📱 پیامک ارسال شد
    # 🎉 فرآیند سفارش تکمیل!
```

## 7.4. 🅱️ Examples4: Event Bus for microservice architecture

چالش: در یک سیستم بزرگ (مثلاً اسنپ یا دیجی‌کالا)، ده‌ها سرویس وجود دارد: سرویس کاربران، سرویس سفارشات، سرویس ایمیل، سرویس تحلیل داده، سرویس پیامک و... .

* اگر هر سرویس بخواهد مستقیماً با بقیه API صدا بزند:
    * سرویس کاربران باید آدرس ۱۰ سرویس دیگر را بداند
    * اگر سرویس ایمیل دان شود، سرویس کاربران هم خطا می‌دهد
    * اضافه کردن سرویس جدید = تغییر کد ۱۰ سرویس قدیمی
* راه‌حل: یک Event Bus (که در واقع یک Mediator است) می‌سازیم. هر سرویس فقط رویدادهایش را در Event Bus منتشر می‌کند و هر سرویسی که علاقه‌مند است، مشترک آن رویداد می‌شود.
* نکته کلیدی: اگر فردا سرویس «پوش نوتیفیکیشن» اضافه شود، فقط یک کلاس جدید PushService می‌سازید و آن را در user.registered مشترک می‌کنید. هیچ‌کدام از ۴ سرویس قبلی تغییر نمی‌کنند.

```python
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Callable, Any
from collections import defaultdict


class EventMediator(ABC):
    """رابط انتزاعی Mediator برای سیستم Event Bus.

    در معماری میکروسرویس، این رابط تضمین می‌کند که سرویس‌ها
    مستقیماً با هم وابستگی نداشته باشند.
    """

    @abstractmethod
    def subscribe(self, event_type: str, handler: Callable[[Dict[str, Any]], None]) -> None:
        """ثبت‌نام برای دریافت یک نوع رویداد خاص.

        Args:
            event_type: نوع رویداد (مثل 'user.registered').
            handler: تابعی که هنگام وقوع رویداد اجرا می‌شود.
        """
        ...

    @abstractmethod
    def publish(self, event_type: str, data: Dict[str, Any]) -> None:
        """انتشار یک رویداد و اطلاع‌رسانی به تمام مشترکین.

        Args:
            event_type: نوع رویداد.
            data: داده‌های همراه رویداد.
        """
        ...


class EventBus(EventMediator):
    """Event Bus به عنوان Mediator مرکزی معماری میکروسرویس.

    این کلاس تنها نقطه ارتباطی بین تمام سرویس‌هاست.
    هر سرویس فقط این کلاس را می‌شناسد و هیچ اطلاعی
    از بقیه سرویس‌ها ندارد.

    Attributes:
        _subscribers: دیکشنری از نوع رویداد به لیست handlerها.
    """

    def __init__(self) -> None:
        self._subscribers: Dict[str, List[Callable]] = defaultdict(list)

    def subscribe(self, event_type: str, handler: Callable[[Dict[str, Any]], None]) -> None:
        """ثبت یک handler برای نوع خاصی از رویداد.

        Args:
            event_type: نوع رویداد (مثل 'user.registered').
            handler: تابع واکنش به رویداد.
        """
        self._subscribers[event_type].append(handler)
        print(f"   🔔 مشترک جدید برای [{event_type}] ثبت شد")

    def publish(self, event_type: str, data: Dict[str, Any]) -> None:
        """انتشار رویداد و اجرای handler تمام مشترکین.

        Args:
            event_type: نوع رویداد منتشرشده.
            data: داده‌های رویداد (مثل اطلاعات کاربر).
        """
        handlers = self._subscribers.get(event_type, [])
        if not handlers:
            print(f"   ⚠️ رویداد [{event_type}] مشترکی ندارد")
            return

        print(f"\n📡 رویداد [{event_type}] منتشر شد: {data}")
        for handler in handlers:
            handler(data)


# ─── سرویس‌های مستقل (هر کدام در یک فایل/پکیج جداگانه هستند) ───


class UserService:
    """سرویس مدیریت کاربران.

    مسئولیت: ثبت‌نام کاربر و انتشار رویداد.
    وابستگی: فقط EventMediator (هیچ سرویس دیگری را نمی‌شناسد).
    """

    def __init__(self, bus: EventMediator) -> None:
        self._bus = bus

    def register_user(self, username: str, email: str) -> None:
        """ثبت‌نام کاربر جدید و اطلاع‌رسانی به سیستم.

        Args:
            username: نام کاربری.
            email: ایمیل کاربر.
        """
        print(f"\n👤 ثبت‌نام کاربر: {username}")
        # ذخیره در دیتابیس (شبیه‌سازی)
        self._bus.publish("user.registered", {
            "username": username,
            "email": email,
        })


class EmailService:
    """سرویس ایمیل.

    مسئولیت: ارسال ایمیل‌های خودکار.
    وابستگی: فقط EventMediator.
    """

    def __init__(self, bus: EventMediator) -> None:
        self._bus = bus
        # اعلام علاقه‌مندی به رویداد ثبت‌نام
        self._bus.subscribe("user.registered", self._on_user_registered)

    def _on_user_registered(self, data: Dict[str, Any]) -> None:
        """واکنش به ثبت‌نام کاربر جدید.

        Args:
            data: داده‌های رویداد شامل username و email.
        """
        print(f"   📧 ایمیل خوش‌آمدگویی → {data['email']}")


class AnalyticsService:
    """سرویس تحلیل داده.

    مسئولیت: به‌روزرسانی داشبورد آماری.
    وابستگی: فقط EventMediator.
    """

    def __init__(self, bus: EventMediator) -> None:
        self._bus = bus
        self._bus.subscribe("user.registered", self._on_user_registered)

    def _on_user_registered(self, data: Dict[str, Any]) -> None:
        """ثبت آمار ثبت‌نام جدید.

        Args:
            data: داده‌های رویداد.
        """
        print(f"   📊 آمار: کاربر جدید '{data['username']}' به داشبورد اضافه شد")


class SMSService:
    """سرویس پیامک.

    مسئولیت: ارسال پیامک تأیید.
    وابستگی: فقط EventMediator.
    """

    def __init__(self, bus: EventMediator) -> None:
        self._bus = bus
        self._bus.subscribe("user.registered", self._on_user_registered)

    def _on_user_registered(self, data: Dict[str, Any]) -> None:
        """ارسال پیامک تأیید ثبت‌نام.

        Args:
            data: داده‌های رویداد.
        """
        print(f"   📱 پیامک تأیید → کاربر {data['username']}")


# ─── استفاده ───
if __name__ == "__main__":
    # ۱. ساخت Event Bus (تنها نقطه ارتباطی)
    bus = EventBus()

    # ۲. راه‌اندازی سرویس‌ها (ترتیب مهم نیست!)
    # هر سرویس خودش را در رویدادهای مورد علاقه‌اش ثبت می‌کند
    email_svc = EmailService(bus)
    analytics_svc = AnalyticsService(bus)
    sms_svc = SMSService(bus)
    user_svc = UserService(bus)

    # ۳. ثبت‌نام کاربر
    # UserService فقط یک رویداد منتشر می‌کند.
    # بقیه سرویس‌ها خودکار و بدون وابستگی واکنش نشان می‌دهند.
    user_svc.register_user("ali_dev", "ali@example.com")

    # خروجی:
    #    🔔 مشترک جدید برای [user.registered] ثبت شد
    #    🔔 مشترک جدید برای [user.registered] ثبت شد
    #    🔔 مشترک جدید برای [user.registered] ثبت شد
    #
    # 👤 ثبت‌نام کاربر: ali_dev
    # 📡 رویداد [user.registered] منتشر شد: {'username': 'ali_dev', 'email': 'ali@example.com'}
    #    📧 ایمیل خوش‌آمدگویی → ali@example.com
    #    📊 آمار: کاربر جدید 'ali_dev' به داشبورد اضافه شد
    #    📱 پیامک تأیید → کاربر ali_dev
```

# 8. 🅰️ Behavioral.Memento(ذخیره و بازیابی حالت داخلی یک شیء)

ذخیره و بازیابی حالت داخلی یک شیء بدون نقض انکپسوله‌سازی

* معمولاً برای پیاده‌سازی `undo` بکار می‌رود
* سه رکن دارد
    1. «متغیر» یا `Originator` : شیئی که وضعیت آن تغییر می‌کند و نیاز به ذخیره/بازیابی دارد.
    2. «لحظه‌ی نشان‌شده» یا`Memento`: شیئی که وضعیت را در خود ذخیره می‌کند
    3. «نگه‌دارنده لحظه‌های نشان‌شده» یا `Caretaker`:شیئی که مسئول نگهداری از عکس‌هاست، اما حق ندارد محتویات عکس(لحظه‌نشان‌شده) را تغییر دهد(فقط آن را نگه می‌دارد و وقتی خواستید به شما پس می‌دهد)
* **Encapsulation**: چالش اصلی Memento کپسوله‌سازی (Encapsulation) است. اگر Caretaker یا «نگه‌دارنده لحظه‌های نشان‌شده» به متغیرهای داخلی «لحظه‌ی نشان‌شده» دسترسی داشته باشد، ممکن است آن‌ها را تغییر دهد که این کار اشتباه است. برای حل این مشکل Encapsulation الگوی طراحی Memento معمولاً دو رابط (Interface) دارد:
    1. رابط پهن (Wide Interface):Originator به تمام فیلدهای خصوصی Memento دسترسی دارد تا بتواند وضعیت را بخواند و بنویسد.
    2. رابط باریک (Narrow Interface): Caretaker فقط یک اشاره‌گر به Memento دارد و فقط آن را در یک لیست نگه می‌دارد. او نمی‌داند داخل Memento چه خبر است.
        * (در زبان‌هایی مثل `Java/C++` این کار با کلاس‌های داخلی یا `Friend class`ها انجام می‌شود، اما در پایتون با استفاده از `__` یا `@property` این مفهوم را شبیه‌سازی می‌کنیم).
* **MemoryManagement**: اگر وضعیت شیء شما بسیار بزرگ باشد (مثلاً یک تصویر بزرگ یا یک دیتابیس درون حافظه)، ذخیره کردن کامل آن در هر Memento باعث نشت حافظه (MemoryLeak) می‌شود. راه‌حل این است که به جای ذخیره کل وضعیت (Full State)، فقط تغییرات (Deltas / Diffs) را ذخیره کنید. یا اینکه از تکنیک Copy-on-Write استفاده کنید.
* **Lifecycle یا چرخه حیات**
    * چه کسی Memento را می‌سازد؟ Originator.
    * چه کسی آن را نابود می‌کند؟ Caretaker (وقتی از تاریخچه حذف می‌شود).
    * این تقسیم وظایف باعث می‌شود Originator نیازی نداشته باشد تاریخچه را در ذهن خود نگه دارد و Caretaker نیازی به درک منطق Originator داشته باشد.

چه زمانی از آن استفاده کنیم؟

* وقتی نیاز به پیاده‌سازی Undo/Redo دارید.
* وقتی نیاز به ذخیره Snapshot (نقاط کنترل یا Checkpoints) دارید.
* وقتی می‌خواهید وضعیت یک شیء را سریالایز (Serialize) کرده و بعداً بازیابی کنید.

## 8.1. 🅱️ Examples1: TextEditor

یک ویرایشگر متن ساده داریم که قابلیت "بازگشت به عقب" (Undo) را دارد.

1. **رابط باریک (Narrow Interface)**: Caretaker فقط این را می‌بیند. هیچ متد دسترسی (Getter) ندارد و فقط یک شیءOpaque (غیرشفاف) است.
2. **رابط پهن (Wide Interface)**: Originator این را می‌بیند و اجازه دارد تمام متغیرهای داخلی را بخواند و بنویسد.

```python
class TextEditorMemento:
    """کلاس Memento که وضعیت ویرایشگر را ذخیره می‌کند."""

    def __init__(self, text: str):
        self._text = text  # ذخیره وضعیت فعلی متن

    def get_text(self) -> str:
        """
        دریافت متن ذخیره شده.
        
        Returns:
            str: متن ذخیره شده در این یادگار.
        """
        return self._text


class TextEditor:
    """کلاس Originator که وضعیت آن تغییر می‌کند و می‌تواند وضعیت خود را ذخیره و بازیابی کند."""

    def __init__(self):
        self._text = ""

    def type_words(self, words: str) -> None:
        """
        اضافه کردن کلمات به متن.
        
        Args:
            words (str): کلماتی که باید به متن اضافه شوند.
        """
        self._text += words

    def get_text(self) -> str:
        """
        دریافت متن فعلی.
        
        Returns:
            str: متن فعلی ویرایشگر.
        """
        return self._text

    def create_memento(self) -> TextEditorMemento:
        """
        ایجاد یک «لحظه‌ی نشان‌شده» یا همان Memento از وضعیت فعلی.
        
        Returns:
            TextEditorMemento: شیئی که وضعیت فعلی را در خود دارد.
        """
        return TextEditorMemento(self._text)  # ایجاد عکس از وضعیت فعلی

    def restore(self, memento: TextEditorMemento) -> None:
        """
        بازیابی وضعیت ویرایشگر از روی یک «لحظه‌ی نشان‌شده».
        
        Args:
            memento (TextEditorMemento): «لحظه‌ی نشان‌شده» که وضعیت قبلی را دارد.
        """
        self._text = memento.get_text()  # بازگرداندن تخته وایت‌برد به حالت عکس


class History:
    """
    کلاس Caretaker که مسئول نگهداری از تاریخچه «لحظه‌های نشان‌شده» است
    """

    def __init__(self):
        self._mementos = []

    def push(self, memento: TextEditorMemento) -> None:
        """
        ذخیره یک «لحظه‌ی نشان‌شده» در تاریخچه.
        
        Args:
            memento (TextEditorMemento): «لحظه‌ی نشان‌شده» که باید ذخیره شود.
        """
        # اضافه کردن عکس به لیست عکس‌ها
        self._mementos.append(memento)

    def pop(self) -> TextEditorMemento:
        """
        دریافت آخرین «لحظه‌ی نشان‌شده» ذخیره شده.
        
        Returns:
            TextEditorMemento: آخرین «لحظه‌ی نشان‌شده» ذخیره شده.
        """
        return self._mementos.pop()  # برداشتن آخرین عکس از لیست


# 9. --- اجرای مثال ---
editor = TextEditor()
history = History()

editor.type_words("سلام ")
history.push(editor.create_memento())  # ذخیره وضعیت

editor.type_words("دنیا ")
history.push(editor.create_memento())  # ذخیره وضعیت

editor.type_words("!!")
print(f"متن فعلی: {editor.get_text()}")  # خروجی: سلام دنیا !!

# 10. بازگشت به عقب (Undo)
editor.restore(history.pop())
print(f"بعد از اولین Undo: {editor.get_text()}")  # خروجی: سلام دنیا 

editor.restore(history.pop())
print(f"بعد از دومین Undo: {editor.get_text()}")  # خروجی: سلام 
```

### 8.1.1. ✅️ شکل دوم از پیاده‌سازی

```python
from typing import List


# Memento
class Memento:
    def __init__(self, state: str):
        self._state = state

    @property
    def state(self):
        return self._state

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f'<Memento state="{self._state}" />'


# Originator
class TextEditor:
    def __init__(self):
        self._content = ''

    @property
    def content(self):
        return self._content

    def write(self, text: str):
        self._content += text

    def save(self) -> Memento:
        return Memento(self._content)

    def restore(self, memento: Memento):
        if memento:
            self._content = memento.state


# CareTaker
class CareTaker:
    def __init__(self, editor: TextEditor):
        self._editor = editor
        self._history: List[Memento] = []
        self.save_state()

    def save_state(self):
        self._history.append(self._editor.save())

    def undo(self):
        if not self._history:
            return

        self._editor.restore(self._history.pop())

    def show_history(self):
        print(self._history)


if __name__ == '__main__':
    editor_1 = TextEditor()
    caretaker = CareTaker(editor_1)

    editor_1.write('Hello ')
    caretaker.save_state()
    caretaker.show_history()
    print(f'-------- {editor_1.content} --------')

    editor_1.write('World!')
    # caretaker.save_state()
    caretaker.show_history()
    print(f'-------- {editor_1.content} --------')

    caretaker.undo()
    caretaker.show_history()
    print(f'-------- {editor_1.content} --------')

    caretaker.undo()
    caretaker.show_history()
    print(f'-------- {editor_1.content} --------')
```

## 8.2. 🅱️ Examples2: ConfigurationManager

```python
from dataclasses import dataclass
from typing import Dict, Any, List
import copy


@dataclass()
class ConfigMemento:
    settings: Dict[str, Any]
    version: str


class ConfigurationManager:
    def __init__(self):
        self._settings = {'theme': 'light',
                          'font_size': 12,
                          'auto_save': True,
                          'language': 'en'}
        self._version = '1.0.0'

    def update_settings(self, key: str, value: Any):
        if key not in self._settings:
            raise KeyError(f'Invalid settings key: {key}')  # ارور هنگامی که یک کلید را بخواهیم تنظیم نماییم که در لیست وجود ندارد

        self._settings[key] = value

    def create_memento(self) -> ConfigMemento:
        return ConfigMemento(settings=copy.deepcopy(self._settings),
                             version=self._version)

    def restore_from_memento(self, memento: ConfigMemento):
        self._settings = copy.deepcopy(memento.settings)
        self._version = memento.version

    def display_config(self):
        for key, value in self._settings.items():
            print(f'{key}: {value}')

        print('=======================================')


class ConfigHistory:
    def __init__(self):
        self._history: List[ConfigMemento] = []
        self._redo_stack: List[ConfigMemento] = []
        self._max_states = 10

    def save_state(self, memento: ConfigMemento) -> None:
        if len(self._history) >= self._max_states:
            self._history.pop(0)

        self._history.append(memento)
        self._redo_stack.clear()

    def undo(self) -> ConfigMemento:
        if not self._history:
            raise ValueError('There is no history')

        current_state = self._history.pop()
        self._redo_stack.append(current_state)

        if not self._history:
            return current_state

        return self._history[-1]

    def redo(self) -> ConfigMemento:
        if not self._redo_stack:
            raise ValueError('There is no item in redo_stack')

        next_state = self._redo_stack.pop()
        self._history.append(next_state)
        return next_state

    def get_current_state(self) -> ConfigMemento:
        if not self._history:
            raise ValueError('There is no history')

        return self._history[-1]


if __name__ == '__main__':
    config_manager = ConfigurationManager()
    history = ConfigHistory()

    # initial state
    history.save_state(config_manager.create_memento())
    config_manager.display_config()

    # change some configs
    config_manager.update_settings('theme', 'dark')
    config_manager.update_settings('font_size', 20)

    history.save_state(config_manager.create_memento())
    config_manager.display_config()

    # change other settings
    config_manager.update_settings('auto_save', False)
    config_manager.update_settings('language', 'fa')

    history.save_state(config_manager.create_memento())
    config_manager.display_config()

    # first undo operation
    print('-------- undo last operation ---------')
    config_manager.restore_from_memento(history.undo())
    config_manager.display_config()

    # second undo operation
    print('-------- undo last operation ---------')
    config_manager.restore_from_memento(history.undo())
    config_manager.display_config()

    print('-------- redo last operation ---------')
    config_manager.restore_from_memento(history.redo())
    config_manager.display_config()
```

## 8.3. 🅱️ Examples3 : فرم چند مرحله‌ای (Use Case رایج)

هدف این مثال: در این مثال می‌خواهیم نشان دهیم که Caretaker چگونه می‌تواند چندین وضعیت را مدیریت کند و ما بتوانیم نه فقط به مرحله قبل، بلکه به یک مرحله خاص در گذشته برگردیم. این الگو در فرم‌های ثبت‌نام چند مرحله‌ای (Wizard) در وب‌سایت‌ها بسیار رایج است.

```python
from typing import Dict, Any, List, Optional


# --- Memento ---
class FormStepState:
    """
    یادگاری که وضعیت فرم در یک مرحله خاص را نگه می‌دارد.
    """

    def __init__(self, step_name: str, data: Dict[str, Any]) -> None:
        self.__step_name = step_name
        self.__data = data.copy()  # کپی کردن دیکشنری برای جلوگیری از تغییرات مرجع

    def get_step_name(self) -> str:
        """دریافت نام مرحله"""
        return self.__step_name

    def get_data(self) -> Dict[str, Any]:
        """دریافت داده‌های ذخیره شده"""
        return self.__data


# --- Originator ---
class UserProfile:
    """
    پروفایل کاربر که در طول مراحل فرم پر می‌شود.
    """

    def __init__(self) -> None:
        self._data: Dict[str, Any] = {}

    def update_data(self, new_data: Dict[str, Any]) -> None:
        """
        به روز رسانی داده‌های پروفایل
        Args:
            new_data (Dict[str, Any]): داده‌های جدید برای اضافه شدن
        """
        self._data.update(new_data)
        print(f"داده‌های فعلی پروفایل: {self._data}")

    def create_memento(self, step_name: str) -> FormStepState:
        """
        ایجاد یادگار از وضعیت فعلی
        Args:
            step_name (str): نام مرحله‌ای که در آن هستیم
        Returns:
            FormStepState: یادگار ساخته شده
        """
        return FormStepState(step_name, self._data)

    def restore_from_memento(self, memento: FormStepState) -> None:
        """
        بازگرداندن پروفایل به وضعیت یک یادگار خاص
        Args:
            memento (FormStepState): یادگاری که باید بازیابی شود
        """
        self._data = memento.get_data().copy()
        print(f"پروفایل به مرحله '{memento.get_step_name()}' بازگشت. داده‌ها: {self._data}")


# --- Caretaker ---
class FormWizard:
    """
    مدیر فرم که تاریخچه مراحل را نگه می‌دارد.
    """

    def __init__(self) -> None:
        self._steps_history: List[FormStepState] = []

    def save_step(self, memento: FormStepState) -> None:
        """
        ذخیره وضعیت یک مرحله
        Args:
            memento (FormStepState): یادگار مرحله
        """
        self._steps_history.append(memento)

    def go_back_to_step(self, step_name: str) -> Optional[FormStepState]:
        """
        پیدا کردن و بازگرداندن یادگار یک مرحله خاص (برای بازگشت به عقب)
        Args:
            step_name (str): نام مرحله‌ای که می‌خواهیم به آن برگردیم
        Returns:
            Optional[FormStepState]: یادگار پیدا شده یا None
        """
        # جستجو در تاریخچه برای پیدا کردن مرحله مورد نظر
        for i in range(len(self._steps_history) - 1, -1, -1):
            if self._steps_history[i].get_step_name() == step_name:
                # حذف مراحل بعد از این مرحله از تاریخچه
                self._steps_history = self._steps_history[:i + 1]
                return self._steps_history[i]
        return None


# --- اجرای مثال ---
if __name__ == "__main__":
    profile = UserProfile()
    wizard = FormWizard()

    # مرحله ۱: اطلاعات شخصی
    profile.update_data({"name": "Ali", "age": 30})
    wizard.save_step(profile.create_memento("Personal_Info"))

    # مرحله ۲: آدرس
    profile.update_data({"city": "Tehran", "zip": "12345"})
    wizard.save_step(profile.create_memento("Address"))

    # مرحله ۳: پرداخت (کاربر منصرف می‌شود و می‌خواهد به مرحله آدرس برگردد)
    profile.update_data({"card_number": "1234-5678"})

    print("\n--- کاربر پشیمان شد و می‌خواهد به مرحله Address برگردد ---")
    # Caretaker وضعیت مرحله Address را پیدا می‌کند
    target_memento = wizard.go_back_to_step("Address")

    if target_memento:
        # Originator خود را از روی آن بازیابی می‌کند
        profile.restore_from_memento(target_memento)
```

## 8.4. 🅱️ Examples4: Industry Standard

* شرح مثال: مدیریت تراکنش‌های مالی و بانکی
* هدف این مثال: در صنعت بانکداری و سیستم‌های مالی، مفهوم Rollback حیاتی است. اگر یک تراکنش چند مرحله‌ای (مثلاً کسر از حساب A، اضافه به حساب B، ثبت در لاگ) در مرحله دوم به خطا بخورد، سیستم باید دقیقاً به حالتی برگردد که قبل از شروع تراکنش داشته است.
* این مثال نشان‌دهنده مدیریت خطا، کپسوله‌سازی دقیق و استفاده از Memento برای تضمین یکپارچگی داده‌ها(Data و Integrity)است.
* در این مثال، TransactionManager (Caretaker) هیچ درکی از منطق بانکی ندارد؛ فقط اسنپ‌شات‌ها را نگه می‌دارد.
* در مثال پایین BankAccount (Originator) به شدت از موجودی خود محافظت می‌کند و فقط از طریق متدهای withdraw و deposit تغییر می‌کند.
* استفاده از __slots__ در AccountSnapshot نشان‌دهنده توجه به مدیریت حافظه در مقیاس بزرگ است (وقتی میلیون‌ها تراکنش در ثانیه ثبت می‌شود، هر بایت حافظه مهم است).
* این الگو تضمین می‌کند که حتی در صورت بروز فاجعه (Exception)، داده‌های مالی سیستم دچار تناقض (Inconsistency) نمی‌شوند.

```python
from typing import List
import random


# --- Memento ---
class AccountSnapshot:
    """
    اسنپ‌شات (عکس فوری) از وضعیت حساب بانکی.
    در اینجا از __slots__ برای بهینه‌سازی حافظه استفاده شده است (یک تکنیک فنی در پایتون).
    """
    __slots__ = ['__balance', '__account_id']

    def __init__(self, account_id: str, balance: float) -> None:
        self.__account_id = account_id
        self.__balance = balance

    def get_balance(self) -> float:
        """دریافت موجودی ذخیره شده"""
        return self.__balance

    def get_account_id(self) -> str:
        """دریافت شناسه حساب"""
        return self.__account_id


# --- Originator ---
class BankAccount:
    """
    حساب بانکی که وضعیت مالی آن تغییر می‌کند.
    """

    def __init__(self, account_id: str, initial_balance: float) -> None:
        self.__account_id = account_id
        self.__balance = initial_balance

    def deposit(self, amount: float) -> None:
        """
        واریز به حساب
        Args:
            amount (float): مبلغ واریزی
        """
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        """
        برداشت از حساب
        Args:
            amount (float): مبلغ برداشتی
        """
        self.__balance -= amount

    def get_balance(self) -> float:
        """دریافت موجودی فعلی"""
        return self.__balance

    def create_snapshot(self) -> AccountSnapshot:
        """
        ایجاد اسنپ‌شات قبل از شروع تراکنش
        Returns:
            AccountSnapshot: وضعیت حساب قبل از تغییر
        """
        return AccountSnapshot(self.__account_id, self.__balance)

    def rollback(self, snapshot: AccountSnapshot) -> None:
        """
        بازگرداندن حساب به وضعیت اسنپ‌شات (Rollback)
        Args:
            snapshot (AccountSnapshot): اسنپ‌شاتی که باید بازیابی شود
        """
        self.__balance = snapshot.get_balance()
        print(f"[Rollback] حساب {self.__account_id} به موجودی {self.__balance} بازگشت.")


# --- Caretaker ---
class TransactionManager:
    """
    مدیر تراکنش‌ها که مسئولیت شروع، کامیت و رول‌بک تراکنش‌ها را بر عهده دارد.
    """

    def __init__(self) -> None:
        # در یک سیستم واقعی، این لیست ممکن است در یک دیتابیس لاگ شود
        self._active_snapshots: List[AccountSnapshot] = []

    def begin_transaction(self, account: BankAccount) -> AccountSnapshot:
        """
        شروع تراکنش و ذخیره وضعیت فعلی
        Args:
            account (BankAccount): حسابی که تراکنش روی آن انجام می‌شود
        Returns:
            AccountSnapshot: اسنپ‌شات اولیه برای رول‌بک احتمالی
        """
        snapshot = account.create_snapshot()
        self._active_snapshots.append(snapshot)
        return snapshot

    def commit_transaction(self, snapshot: AccountSnapshot) -> None:
        """
        تایید تراکنش و حذف اسنپ‌شات از لیست فعال (چون دیگر نیازی به رول‌بک نیست)
        Args:
            snapshot (AccountSnapshot): اسنپ‌شاتی که باید از لیست حذف شود
        """
        if snapshot in self._active_snapshots:
            self._active_snapshots.remove(snapshot)
            print("[Commit] تراکنش با موفقیت تایید شد. اسنپ‌شات حذف گردید.")

    def rollback_transaction(self, account: BankAccount, snapshot: AccountSnapshot) -> None:
        """
        لغو تراکنش و بازگرداندن وضعیت به حالت اول
        Args:
            account (BankAccount): حسابی که باید رول‌بک شود
            snapshot (AccountSnapshot): اسنپ‌شات اولیه
        """
        account.rollback(snapshot)
        if snapshot in self._active_snapshots:
            self._active_snapshots.remove(snapshot)


# --- شبیه‌سازی یک تراکنش انتقال وجه ---
def transfer_money(from_acc: BankAccount, to_acc: BankAccount, amount: float, manager: TransactionManager) -> None:
    """
    شبیه‌سازی انتقال وجه با قابلیت رول‌بک در صورت بروز خطا
    Args:
        from_acc (BankAccount): حساب مبدا
        to_acc (BankAccount): حساب مقصد
        amount (float): مبلغ انتقال
        manager (TransactionManager): مدیر تراکنش‌ها
    """
    print(f"\n--- شروع انتقال {amount} تومان از حساب {from_acc.get_balance()} به حساب مقصد ---")

    # ۱. شروع تراکنش و گرفتن اسنپ‌شات از حساب مبدا
    snapshot = manager.begin_transaction(from_acc)

    try:
        # ۲. برداشت از مبدا
        from_acc.withdraw(amount)

        # ۳. شبیه‌سازی یک خطای ناگهانی در سیستم (مثلاً قطعی شبکه یا خطای مقصد)
        if random.choice([True, False]):
            raise Exception("خطای شبکه در هنگام واریز به حساب مقصد!")

        # ۴. واریز به مقصد
        to_acc.deposit(amount)

        # ۵. تایید تراکنش
        manager.commit_transaction(snapshot)
        print(f"انتقال موفق. موجودی مبدا: {from_acc.get_balance()}")

    except Exception as e:
        # در صورت بروز خطا، رول‌بک کردن تراکنش
        print(f"[Error] {e}")
        manager.rollback_transaction(from_acc, snapshot)


# --- اجرای مثال ---
if __name__ == "__main__":
    # تنظیم seed برای اینکه در اجراهای مختلف، گاهی خطا رخ دهد و گاهی ندهد
    random.seed(42)

    account_a = BankAccount("ACC-101", 1000.0)
    account_b = BankAccount("ACC-202", 500.0)
    tx_manager = TransactionManager()

    # تلاش برای انتقال وجه (ممکن است به دلیل خطای شبیه‌سازی شده، رول‌بک شود)
    transfer_money(account_a, account_b, 200.0, tx_manager)

    print(f"\nوضعیت نهایی حساب A: {account_a.get_balance()}")
```

# 9. 🅰️ Behavioral.Observer(هنگام تغییر وضعیت یک شیء، همه وابسته‌ها به‌طور خودکار به‌روز شوند)

پیاده‌سازی مکانیزم Publish-Subscribe (انتشار-اشتراک) توسط تعریف یک رابطه "یک به چند" بین اشیاء به طوری که وقتی یک شیء (به نام Subject یا Publisher) وضعیتش تغییر می‌کند، تمام اشیاء وابسته به آن (به نام Observers یا Subscribers) به صورت خودکار مطلع شده و به‌روزرسانی می‌شوند.

* مثال‌ها
    * یک سایت فرشگاهی که وقتی تراکنش پرداخت انجام شد به فرآینده‌های مستقل میگوید که هرکدام کارهای خودش را انجام دهد
        * ارسال پیامک
        * ارسال ایمیل
        * کم کردن از انبار
        * شروع پردازش ارسال مرسوله
        * کلیه کارهای مورد نیاز
    * اطلاع‌رسانی به نفرات دنبال کننده یک صفحه برای ارسال یک ویدیو در صفحه آپارات خود
    * ایتا همزمان که عکس بارگزاری میشود حالت دوم و سوم یعنی thumbnail آن هم ایجاد می‌شود
        * همزمان پردازش هوش مصنوعی هم برای آن عکی اجرا می‌آید تا تحلیل دیتا صورت پذیرد
    *

* ارکان اصلی
    1. Subject(موضوع/ناشر): شیئی که وضعیت آن تغییر می‌کند و لیستی از مشاهده‌گران را نگهداری می‌کند.
    2. Observer(مشاهده‌گر): شیئی که منتظر تغییرات Subject است و یک متد update دارد تا در صورت تغییر، صدا زده شود.
* django.core.signals
    * این الگوی طراحی در جنگو تحت عنوان django.core.signals در هسته خود پیاده‌سازی کرده است.
    * تابع post_save تمام وابستگی هایبین app ها را دارد و هنگام نیاز سیگنال به دیگران میدهد که کارهای نیاز رو انجام دهد
* کپسوله‌سازی و Coupling (وابستگی): بزرگترین مزیت Observer، کاهش وابستگی (Loose Coupling) است. Subject فقط می‌داند که Observerها یک رابط مشترک (update) را پیاده‌سازی کرده‌اند. او نمی‌داند آن‌ها چه کلاس‌هایی هستند، چه کار می‌کنند یا چند تا هستند. شما می‌توانید در زمان اجرا (Runtime) Observerها را اضافه یا حذف کنید بدون اینکه کد Subject را تغییر دهید
* نشت حافظه (Memory Leaks): اگر یک Observer دیگر نیازی به دریافت نوتیفیکیشن ندارد (مثلاً پنجره‌ای در UI بسته شده است) اما فراموش کنید آن را از لیست Subject حذف (detach) کنید، Subject همچنان یک Reference به آن نگه می‌دارد. این کار باعث می‌شود garbage collector نتواند آن Observer را از حافظه پاک کند و حافظه سیستم پر می‌شود.
* ترتیب اطلاع‌رسانی و وابستگی متقابل: Observerها هرگز نباید فرض کنند که به ترتیب خاصی صدا زده می‌شوند. همچنین، یک Observer نباید در متد update خود، وضعیت Subject را تغییر دهد، زیرا این کار باعث ایجاد حلقه بی‌نهایت (Infinite Loop) یا رفتارهای پیش‌بینی‌ناپذیر می‌شود.

## 9.1. 🅱️ Examples1: درک پایه با یک ایستگاه هواشناسی

هدف این مثال: نشان دادن ساختار پایه الگو، یعنی نحوه ثبت‌نام (attach)، لغو اشتراک (detach) و اطلاع‌رسانی (notify). در این مثال از مدل Pull استفاده می‌کنیم؛ یعنی Subject فقط خبر می‌دهد که "تغییری رخ داد" و Observer خودش باید برود و داده جدید را از Subject بخواند.

```python
from abc import ABC, abstractmethod
from typing import List


# --- Observer Interface ---
class DisplayElement(ABC):
    """
    رابط پایه برای تمام نمایشگرها.
    """

    @abstractmethod
    def display(self) -> None:
        """نمایش اطلاعات روی صفحه"""
        pass


class Observer(ABC):
    """
    رابط مشاهده‌گر که متد به‌روزرسانی را تعریف می‌کند.
    """

    @abstractmethod
    def update(self, temperature: float, humidity: float) -> None:
        """
        به‌روزرسانی وضعیت مشاهده‌گر هنگام تغییر داده‌ها.
        
        Args:
            temperature (float): دمای جدید.
            humidity (float): رطوبت جدید.
        """
        pass


# --- Subject Interface ---
class Subject(ABC):
    """
    رابط موضوع (ناشر) برای مدیریت مشاهده‌گران.
    """

    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        """
        ثبت‌نام یک مشاهده‌گر جدید.
        
        Args:
            observer (Observer): مشاهده‌گری که باید اضافه شود.
        """
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        """
        حذف یک مشاهده‌گر.
        
        Args:
            observer (Observer): مشاهده‌گری که باید حذف شود.
        """
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        """اطلاع‌رسانی به تمام مشاهده‌گران ثبت‌نام شده."""
        pass


# --- Concrete Subject ---
class WeatherData(Subject):
    """
    کلاس اصلی ایستگاه هواشناسی که داده‌ها را دریافت و مدیریت می‌کند.
    """

    def __init__(self) -> None:
        self._observers: List[Observer] = []  # لیست مشاهده‌گران
        self._temperature: float = 0.0
        self._humidity: float = 0.0

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        # صدا زدن متد update تمام مشاهده‌گران
        for observer in self._observers:
            observer.update(self._temperature, self._humidity)

    def measurements_changed(self) -> None:
        """این متد زمانی صدا زده می‌شود که داده‌های جدیدی از سنسورها برسد."""
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float) -> None:
        """
        تنظیم داده‌های جدید هواشناسی.
        
        Args:
            temperature (float): دمای اندازه‌گیری شده.
            humidity (float): رطوبت اندازه‌گیری شده.
        """
        self._temperature = temperature
        self._humidity = humidity
        self.measurements_changed()  # اطلاع‌رسانی به مشاهده‌گران


# --- Concrete Observers ---
class CurrentConditionsDisplay(Observer, DisplayElement):
    """
    نمایشگر شرایط فعلی آب و هوا.
    """

    def __init__(self, weather_data: Subject) -> None:
        self._temperature = 0.0
        self._humidity = 0.0
        self._weather_data = weather_data
        # ثبت‌نام در ایستگاه هواشناسی
        self._weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self.display()

    def display(self) -> None:
        print(f"نمایشگر فعلی: دما = {self._temperature}°C, رطوبت = {self._humidity}%")


# --- اجرای مثال ---
if __name__ == "__main__":
    weather_data = WeatherData()

    # ایجاد و ثبت‌نام نمایشگر
    current_display = CurrentConditionsDisplay(weather_data)

    # تغییر داده‌ها (این کار باعث notify شدن خودکار می‌شود)
    weather_data.set_measurements(25.5, 60.0)
    weather_data.set_measurements(28.0, 55.0)
```

## 9.2. 🅱️ Examples2: سیستم اطلاع‌رسانی موجودی فروشگاه

هدف این مثال: در این مثال می‌خواهیم مدل Push را پیاده‌سازی کنیم. یعنی Subject دقیقاً مشخص کند چه چیزی تغییر کرده است. همچنین نشان می‌دهیم که چگونه Observerهای مختلف می‌توانند به یک روکش واحد، واکنش‌های کاملاً متفاوتی نشان دهند. این الگو در سیستم‌های E-commerce برای اطلاع‌رسانی کاهش موجودی یا تغییر قیمت بسیار رایج است.

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any


# --- Observer Interface ---
class StockObserver(ABC):
    """
    رابط مشاهده‌گر برای سیستم موجودی.
    """

    @abstractmethod
    def update(self, product_name: str, new_stock: int, price_changed: bool) -> None:
        """
        به‌روزرسانی وضعیت بر اساس داده‌های ارسال شده (Push Model).
        
        Args:
            product_name (str): نام محصولی که تغییر کرده است.
            new_stock (int): موجودی جدید محصول.
            price_changed (bool): آیا قیمت هم تغییر کرده است؟
        """
        pass


# --- Subject ---
class ProductInventory:
    """
    کلاس مدیریت موجودی محصولات (Subject).
    """

    def __init__(self) -> None:
        self._observers: List[StockObserver] = []
        self._products: Dict[str, Dict[str, Any]] = {}  # دیکشنری برای نگهداری محصولات

    def attach(self, observer: StockObserver) -> None:
        """اضافه کردن مشاهده‌گر"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: StockObserver) -> None:
        """حذف مشاهده‌گر برای جلوگیری از نشت حافظه"""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, product_name: str, new_stock: int, price_changed: bool) -> None:
        """
        اطلاع‌رسانی به تمام مشاهده‌گران با ارسال مستقیم داده‌ها (Push).
        
        Args:
            product_name (str): نام محصول تغییر یافته.
            new_stock (int): موجودی جدید.
            price_changed (bool): وضعیت تغییر قیمت.
        """
        for observer in self._observers:
            observer.update(product_name, new_stock, price_changed)

    def update_stock(self, product_name: str, quantity: int, new_price: float = None) -> None:
        """
        به‌روزرسانی موجودی یک محصول و اطلاع‌رسانی به سیستم.
        
        Args:
            product_name (str): نام محصول.
            quantity (int): تعداد اضافه/کم شده.
            new_price (float, optional): قیمت جدید در صورت تغییر.
        """
        if product_name not in self._products:
            self._products[product_name] = {"stock": 0, "price": 0.0}

        self._products[product_name]["stock"] += quantity
        price_changed = False
        if new_price is not None:
            self._products[product_name]["price"] = new_price
            price_changed = True

        current_stock = self._products[product_name]["stock"]
        print(f"[Inventory] موجودی {product_name} به {current_stock} تغییر یافت.")

        # فراخوانی notify با مدل Push (ارسال مستقیم داده‌ها)
        self.notify(product_name, current_stock, price_changed)


# --- Concrete Observers ---
class EmailAlertSystem(StockObserver):
    """
    سیستم اطلاع‌رسانی ایمیلی (فقط وقتی موجودی کم است ایمیل می‌زند).
    """

    def update(self, product_name: str, new_stock: int, price_changed: bool) -> None:
        # منطق فیلترینگ: فقط اگر موجودی زیر ۱۰ بود ایمیل بزن
        if new_stock < 10:
            print(f"[Email] هشدار: موجودی {product_name} کم است ({new_stock} عدد). ایمیل ارسال شد.")


class AnalyticsDashboard(StockObserver):
    """
    داشبورد تحلیلی (همه تغییرات را لاگ می‌کند).
    """

    def update(self, product_name: str, new_stock: int, price_changed: bool) -> None:
        status = "و تغییر قیمت" if price_changed else ""
        print(f"[Dashboard] لاگ سیستم: {product_name} -> موجودی: {new_stock} {status}")


# --- اجرای مثال ---
if __name__ == "__main__":
    inventory = ProductInventory()

    # ثبت‌نام سیستم‌های مختلف
    email_system = EmailAlertSystem()
    dashboard = AnalyticsDashboard()

    inventory.attach(email_system)
    inventory.attach(dashboard)

    print("--- به‌روزرسانی اولیه ---")
    inventory.update_stock("Laptop", 50)  # موجودی ۵۰ -> ایمیل زده نمی‌شود

    print("\n--- فروش و کاهش موجودی ---")
    inventory.update_stock("Laptop", -45)  # موجودی ۵ -> ایمیل زده می‌شود

    print("\n--- تغییر قیمت ---")
    inventory.update_stock("Smartphone", 20, new_price=999.0)
```

## 9.3. 🅱️ Examples3: سیستم فید داده‌های بازار مالی (Industry Standard)

هدف این مثال: این یک مثال کاملاً فنی از صنعت FinTech (فناوری مالی) است. در این سیستم، یک Market Data Feed (Subject) به صورت مداوم و با فرکانس بالا قیمت سهام را دریافت می‌کند. چندین سیستم (Observer) مثل ربات معامله‌گر، موتور نمودار و سیستم لاگ مالی به این داده‌ها نیاز دارند. در این مثال، Thread Safety برای جلوگیری از Race Condition و مدیریت دقیق
چرخه حیات Observerها پوشش داده شده است.

```python
import threading
import time
from abc import ABC, abstractmethod
from typing import List, Protocol


# --- استفاده از Protocol برای تعریف رابط (روش مدرن و Pythonic) ---
class MarketObserver(Protocol):
    """
    پروتکل مشاهده‌گر بازار مالی.
    استفاده از Protocol به جای ABC اجازه می‌دهد کلاس‌ها بدون نیاز به ارث‌بری صریح، 
    فقط با پیاده‌سازی متد update، به عنوان Observer شناخته شوند (Duck Typing با تایید استاتیک).
    """

    def update(self, symbol: str, price: float, timestamp: float) -> None:
        """
        دریافت تیک (Tick) جدید بازار.
        
        Args:
            symbol (str): نماد سهام.
            price (float): قیمت جدید.
            timestamp (float): زمان دقیق ثبت قیمت.
        """
        ...


# --- Subject ---
class MarketDataFeed:
    """
    فید داده‌های بازار مالی (Subject).
    این کلاس باید در محیطی با Threadهای متعدد (چند نخی) امن باشد.
    """

    def __init__(self) -> None:
        self._observers: List[MarketObserver] = []
        # استفاده از Lock برای تضمین Thread Safety در هنگام تغییر لیست Observerها
        self._lock = threading.Lock()

    def subscribe(self, observer: MarketObserver) -> None:
        """
        ثبت‌نام امن در محیط چند نخی.
        
        Args:
            observer (MarketObserver): مشاهده‌گری که باید اضافه شود.
        """
        with self._lock:
            if observer not in self._observers:
                self._observers.append(observer)

    def unsubscribe(self, observer: MarketObserver) -> None:
        """
        لغو اشتراک امن برای جلوگیری از نشت حافظه.
        
        Args:
            observer (MarketObserver): مشاهده‌گری که باید حذف شود.
        """
        with self._lock:
            try:
                self._observers.remove(observer)
            except ValueError:
                pass

    def broadcast_tick(self, symbol: str, price: float, timestamp: float) -> None:
        """
        ارسال تیک قیمتی به تمام مشاهده‌گران.
        نکته فنی: لیست Observerها را در یک کپی (Snapshot) می‌رییم تا اگر در حین notify
        یکی از Observerها خودش را unsubscribe کرد، حلقه با خطا مواجه نشود.
        
        Args:
            symbol (str): نماد سهام.
            price (float): قیمت لحظه‌ای.
            timestamp (float): زمان ثبت.
        """
        # کپی کردن لیست در داخل قفل برای جلوگیری از تغییر حین پیمایش
        with self._lock:
            observers_snapshot = list(self._observers)

        # صدا زدن Observerها خارج از قفل برای جلوگیری از Deadlock
        for observer in observers_snapshot:
            observer.update(symbol, price, timestamp)


# --- Concrete Observers ---
class TradingBot:
    """
    ربات معامله‌گر (فقط به تغییرات شدید قیمت واکنش نشان می‌دهد).
    """

    def __init__(self, bot_id: str) -> None:
        self.bot_id = bot_id
        self._last_price: float = 0.0

    def update(self, symbol: str, price: float, timestamp: float) -> None:
        # منطق فیلترینگ: فقط اگر نوسان بیشتر از ۲٪ بود معامله کن
        if self._last_price > 0 and abs(price - self._last_price) / self._last_price > 0.02:
            action = "BUY" if price > self._last_price else "SELL"
            print(f"[{self.bot_id}] نوسان شدید در {symbol}! قیمت: {price} -> دستور {action} ارسال شد.")
        self._last_price = price


class ChartingEngine:
    """
    موتور رسم نمودار (همه تیک‌ها را برای رسم کندل‌استیک ذخیره می‌کند).
    """

    def update(self, symbol: str, price: float, timestamp: float) -> None:
        # در سیستم واقعی، این داده‌ها در یک آرایه حلقوی (Ring Buffer) ذخیره می‌شوند
        print(f"[Chart] آپدیت نمودار {symbol}: قیمت={price}, زمان={timestamp:.2f}")


class FinancialAuditLogger:
    """
    سیستم لاگ مالی (برای ثبت تمام تیک‌ها جهت ممیزی و Compliance).
    """

    def update(self, symbol: str, price: float, timestamp: float) -> None:
        # شبیه‌سازی عملیات I/O کند (نوشتن در دیتابیس)
        # در سیستم واقعی، این Observer باید در یک Thread جداگانه یا از طریق Queue اجرا شود
        # تا سرعت broadcast را پایین نیاورد.
        pass  # print(f"[Audit] لاگ شد: {symbol} @ {price}")


# --- اجرای مثال و شبیه‌سازی محیط Real-time ---
if __name__ == "__main__":
    feed = MarketDataFeed()

    # ایجاد Observerها
    bot = TradingBot("AlphaBot")
    chart = ChartingEngine()
    logger = FinancialAuditLogger()

    # ثبت‌نام
    feed.subscribe(bot)
    feed.subscribe(chart)
    feed.subscribe(logger)

    print("--- شروع دریافت داده‌های بازار ---")

    # شبیه‌سازی دریافت تیک‌های قیمتی در یک حلقه
    # در سیستم واقعی، این داده‌ها از طریق سوکت (WebSocket) از بورس دریافت می‌شوند
    ticks = [
        ("AAPL", 150.0),
        ("AAPL", 151.0),
        ("AAPL", 155.0),  # نوسان شدید (بیش از ۲٪ نسبت به ۱۵۱) -> ربات باید BUY بزند
        ("AAPL", 148.0),  # نوسان شدید نزولی -> ربات باید SELL بزند
    ]

    for symbol, price in ticks:
        current_time = time.time()
        feed.broadcast_tick(symbol, price, current_time)
        time.sleep(0.1)  # شبیه‌سازی فاصله زمانی بین تیک‌ها

    print("\n--- پایان شبیه‌سازی ---")
```

# 10. 🅰️ Behavioral.Interpreter

## 10.1. 🅱️ Examples1:

## 10.1. 🅱️ Examples1:

</div>