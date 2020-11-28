<div dir="rtl">

# آزمایش جمع دو مارتریس

در این آزمایش تلاش کردیم تا ثابت کنیم که به طور کلی و با شرایط یکسان، در زبان برنامه‌نویسی پایتون جمع دو ماتریس به صورت سطری، زمان بیشتری نسبت به جمع تو ماتریس به صورت ستونی صرف می‌کند.



## مقدمه
در کلاس درس «پردازش موازی» از ما خواسته شده در در یک زبان برنامه‌نویسی (به دلخواه خود) مشخص کنیم که در صورت داشتم دو ماتریس به یک اندازه و با درایه‌های مختلف؛ در صورتی که ماتریس‌ها به صورت سطری با یکدیگر جمع شوند کار زودتر انجام می‌شود یا به صورت ستونی؟

در این پرسش منظور از سطر (Row) همان بعد اول یک آرایه دو بعدی و منظور از ستون (Col) همان بعد دوم همان آرایه است.

بدیهی است که با جستجو در گوگل به راحتی می‌توان پاسخ چنین سؤالاتی را پیدا کرد اما هدف این آزمایش این است که خودمان به این نتیجه برسیم.



## شیوه نصب
برای اجرای این برنامه در کامپیوتر خود لازم است تا ماژول‌های موجود در requirements.txt بر روی سیستم‌تان نصب باشد. برای این کار تنها کافی است که دستور زیر را اجرا کنید.

`pip install -r requirements.txt`



## شیوه انجام آزمایش
در برنامه تابعی به نام `main` وجود دارد که تابع دیگری به نام `make_plt(Range, Steps)` را فراخوانی می‌کند. مقدار Range مشخص می‌کند که حداکثر طولی که ماتریس مربعی فرضی ما خواهد داشت چقدر است. عدد دوم فاصله بین هر دو عدد را مشخص می‌کند. مثلا `make_plt(1000, 50)` به ازای ماتریس‌هایی به طول ۱ تا ۱۰۰۰ آزمایش را تکرار می‌کند. به دلیل طولانی شدن زمان آزمایش عدد ۵۰ مشخص می‌کند در بازه‌های ۵۰ تایی ماتریس‌‌های بینابینی نادیده گرفته شوند. به عبارتی مثال فوق تنها ۲۰۰ بار اجرا می‌شود.

نکته: هر چقدر میزان Steps کمتر باشد، نتیجه آزمایش و نمودار حاصل دقیق‌تر است. از آن‌جایی که معمولا نتیجه آزمایش در اعدادی که بهم نزدیک هستند تفاوت چشم‌گیری ندارد؛ با افزایش Steps می‌توان سرعت اجرای کل آزمایش را زیاد کرد.

نکته ۲: بدیهی است که زمان و نتیجه آزمایش می‌تواند وابسته به سیستمی باشد که شما از آن استفاده می‌کنید. نتایج فعلی موجود در پوشه results بر مبنای پردازنده [Intel(R) Core(TM) i7-5500U CPU @ 2.40GHz](https://www.intel.com/content/www/us/en/products/processors/core/i7-processors/i7-5500u.html) حاصل شده است.

نکته ۳: این آزمایش در شرایط آزمایشگاهی صورت نگرفته است. نتایج حاصل از اجرای همین کد در سیستمی ایزوله می‌تواند کمی متفاوت باشد ولی «احتمالا» تغییری در نتیجه نهایی حاصل نخواهد شد.



## نتایج
کلیه نتایج در مسیر [results](https://github.com/LordArma/cambrac/tree/master/cambrac/results) ذخیره شده‌اند. نام هر پوشه شامل دو عدد است که عدد نخست بیانگر بیشترین اندازه ماتریس و عدد دوم میزان قدم است.
تصویر زیر خروجی سنگین‌ترین آزمایش صورت گرفته است که با ماتریسی به طول و عرض ۲۰ هزار و با قدم‌های هزار انجام شده است.
![alt text](https://github.com/LordArma/cambrac/blob/master/cambrac/results/Until20000Step1000/plot.png?raw=true "نتیجه اجرا تا سقف ۲۰ هزار با گام هزار")
همانطور که مشاهده می‌شود. با بزرگ شدن ابعاد ماتریس، تفاوت در جمع دو ماتریس به صورت سطری و یا ستونی بیشتر دیده می‌شود.

نکته: در سیستمی که من این آزمایش را انجام دادم، به ازای ماتریس‌هایی با حداکثر طول ۵۰ زمان اجرا به قدری کوتاه است (زیر میلی ثانیه) که زمان اجرا صفر در نظر گرفته می‌شود. در بین ۵۰ تا ۴۰۰ تفاوتی محسوسی بین جمع به صورت سطری و یا ستونی دیده نمی‌شود و برای ماتریس‌هایی که طول آن‌ها بیشتر از ۴۰۰ است این تفاوت کم‌کم دیده می‌شود.
 



## تماس و همکاری
راحت باشید! در صورت تمایل می‌توانید از این تمرین Fork گرفته و تغییرات خود را به صورت Pull Request برایم ارسال کنید. برای ارتباط مستقیم با من از ایمیل Arma@Jangal.co استفاده کنید.



## تشکر
با تشکر از دکتر «اسداله شاه بهرامی» که با مطرح کردن این موضوع در درس «پردازش موازی» اینجانب را با این موضوع آشنا فرمودند.
</div>
