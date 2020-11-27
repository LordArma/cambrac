<div dir="rtl">

# آزمایش جمع دو مارتریس

در این آزمایش تلاش کردیم تا ثابت کنیم که به طور کلی و با شرایط یکسان، در زبان برنامه‌نویسی پایتون جمع دو ماتریس به صورت سطری، زمان بیشتری نسبت به جمع تو ماتریس به صورت ستونی صرف می‌کند.



## مقدمه
در کلاس درس «پردازش موازی» از ما خواسته شده در در یک زبان برنامه‌نویسی (به دلخواه خود) مشخص کنیم که در صورت داشتم دو ماتریس به یک اندازه و با درایه‌های مختلف؛ در صورتی که ماتریس‌ها به صورت سطری با یکدیگر جمع شوند کار زودتر انجام می‌شود یا به صورت ستونی؟

در این پرسش منظور از سطر (Row) همان بعد اول یک آرایه دو بعدی و منظور از ستون (Col) همان بعد دوم همان آرایه است.

بدیهی است که با جستجو در گوگل به راحتی می‌توان پاسخ چنین سؤالاتی را پیدا کرد اما هدف این آزمایش این است که خودمان به این نتیجه برسیم.



## شیوه نصب
برای اجرای این برنامه در کامپیوتر خود لازم است تا ماژول‌های موجود در requirements.txt بر روی سیستم‌تان نصب باشد. برای این کار تنها کافی است که دستور زیر را اجرا کنید.

`pip install requirements.txt `



## شیوه انجام آزمایش
در قسمت `__name__` تابعی به نام `show_plt(Range, Steps)` وجود دارد. مقدار Range مشخص می‌کند که حداکثر طولی که ماتریس مربعی فرضی ما خواهد داشت چقدر است. عدد دوم فاصله بین هر دو عدد را مشخص می‌کند. مثلا `show_plt(1000, 50)` به ازای ماتریس‌هایی به طول ۱ تا ۱۰۰۰ آزمایش را تکرار می‌کند. به دلیل طولانی شدن زمان آزمایش عدد ۵۰ مشخص می‌کند در بازه‌های ۵۰ تایی ماتریس‌‌های بینابینی نادیده گرفته شوند. به عبارتی مثال فوق تنها ۲۰۰ بار اجرا می‌شود.

نکته: هر چقدر میزان Steps کمتر باشد، نتیجه آزمایش و نمودار حاصل دقیق‌تر است. از آن‌جایی که معمولا نتیجه آزمایش در اعدادی که بهم نزدیک هستند تفاوت چشم‌گیری ندارد؛ با افزایش Steps می‌توان سرعت اجرای کل آزمایش را زیاد کرد.

نکته ۲: بدیهی است که زمان و نتیجه آزمایش می‌تواند وابسته به سیستمی باشد که شما از آن استفاده می‌کنید. نتایج فعلی موجود در پوشه results بر مبنای سیستمی با مشخصات زیر است:

```shell
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   39 bits physical, 48 bits virtual
CPU(s):                          4
On-line CPU(s) list:             0-3
Thread(s) per core:              2
Core(s) per socket:              2
Socket(s):                       1
NUMA node(s):                    1
Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           61
Model name:                      Intel(R) Core(TM) i7-5500U CPU @ 2.40GHz
Stepping:                        4
CPU MHz:                         2055.753
CPU max MHz:                     3000.0000
CPU min MHz:                     500.0000
BogoMIPS:                        4789.20
L1d cache:                       64 KiB
L1i cache:                       64 KiB
L2 cache:                        512 KiB
L3 cache:                        4 MiB
NUMA node0 CPU(s):               0-3
Vulnerability Itlb multihit:     KVM: Mitigation: VMX unsupported
Vulnerability L1tf:              Mitigation; PTE Inversion
Vulnerability Mds:               Mitigation; Clear CPU buffers; SMT vulnerable
Vulnerability Meltdown:          Mitigation; PTI
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and secco
                                 mp
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitizat
                                 ion
Vulnerability Spectre v2:        Mitigation; Full generic retpoline, IBPB conditional, IBRS_FW, ST
                                 IBP conditional, RSB filling
Vulnerability Srbds:             Mitigation; Microcode
Vulnerability Tsx async abort:   Not affected
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat
                                  pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx
                                  pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good no
                                 pl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 mo
                                 nitor ds_cpl est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 ss
                                 e4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rd
                                 rand lahf_lm abm 3dnowprefetch cpuid_fault epb invpcid_single pti
                                  ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erm
                                 s invpcid rdseed adx smap intel_pt xsaveopt dtherm ida arat pln p
                                 ts md_clear flush_l1d

```



## نتایج
کلیه نتایج در مسیر results ذخیره شده‌اند. نام هر پوشه شامل دو عدد است که عدد نخست بیانگر بیشترین اندازه ماتریس و عدد دوم میزان قدم است.
تصویر زیر خروجی سنگین‌ترین آزمایش نجام شده است که با ماتریسی به طول و عرض ۱۰ هزار و با قدم‌های پانصد انجام شده است.
![alt text](https://github.com/LordArma/cambrac/blob/master/results/Until10000Step500/plot.png?raw=true "نتیجه اجرا تا سقف ۱۰ هزار با گام پانصد")
همانطور که مشاهده می‌شود. با بزرگ شدن ابعاد ماتریس، تفاوت در جمع دو ماتریس به صورت سطری و یا ستونی بیشتر دیده می‌شود.



## تماس و همکاری
راحت باشید! در صورت تمایل می‌توانید از این تمرین Fork گرفته و تغییرات خود را به صورت Pull Request برایم ارسال کنید. برای ارتباط مستقیم با من از ایمیل Arma@Jangal.co استفاده کنید.



## تشکر
با تشکر از دکتر «اسداله شاه بهرامی» که با مطرح کردن این موضوع در درس «پردازش موازی» اینجانب را با این موضوع آشنا فرمودند.
</div>
