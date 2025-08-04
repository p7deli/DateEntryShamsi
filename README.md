# تقویم شمسی مدرن - Modern Shamsi Calendar

این کتابخانه یک رابط کاربری مدرن و زیبا برای انتخاب تاریخ شمسی ارائه می‌دهد.

## ویژگی‌های جدید

### 🎨 طراحی مدرن

- رنگ‌بندی زیبا و حرفه‌ای
- استایل‌های مدرن و responsive
- انیمیشن‌های نرم

### 📅 قابلیت‌های پیشرفته

- نمایش کامل نام روزهای هفته
- انتخاب مستقیم سال
- دکمه "امروز" برای رفتن سریع به تاریخ امروز
- نمایش تاریخ انتخاب شده با رنگ متمایز
- نمایش تاریخ امروز با رنگ سبز

### 🔧 بهبودهای فنی

- رفع مشکل محاسبه روزهای ماه اسفند
- مدیریت بهتر خطاها
- کد تمیزتر و قابل نگهداری

## نحوه استفاده

### استفاده از کلاس مدرن

```python
import tkinter as tk
from shamsi_calendar import ModernShamsiDateEntry

root = tk.Tk()
root.title("تقویم شمسی مدرن")

# ایجاد ورودی تاریخ مدرن
date_entry = ModernShamsiDateEntry(root)
date_entry.pack(padx=20, pady=20)

# دریافت تاریخ انتخاب شده
selected_date = date_entry.get()
print(f"تاریخ انتخاب شده: {selected_date}")

root.mainloop()
```

### استفاده از کلاس قدیمی (برای سازگاری)

```python
from shamsi_calendar import ShamsiDateEntry

# استفاده مشابه قبل
date_entry = ShamsiDateEntry(root)
```

## ویژگی‌های UI جدید

### 1. ورودی تاریخ

- فرمت استاندارد: `YYYY/MM/DD`
- امکان تایپ مستقیم تاریخ
- اعتبارسنجی خودکار

### 2. پنجره تقویم

- اندازه ثابت و مناسب (400x500)
- مرکز قرار دادن خودکار
- طراحی responsive

### 3. کنترل‌های تقویم

- دکمه‌های تغییر ماه (◀ و ▶)
- انتخاب مستقیم سال با Spinbox
- دکمه "امروز" برای رفتن سریع

### 4. نمایش روزها

- نام کامل روزهای هفته
- رنگ‌بندی متمایز برای تاریخ انتخاب شده
- رنگ سبز برای تاریخ امروز
- دکمه‌های بزرگ و قابل کلیک

### 5. دکمه‌های عملیات

- دکمه "تایید" برای انتخاب نهایی
- دکمه "لغو" برای بستن بدون انتخاب

## رنگ‌بندی

- **پس‌زمینه اصلی**: `#f8f9fa` (خاکستری روشن)
- **دکمه‌های اصلی**: `#007bff` (آبی)
- **دکمه امروز**: `#28a745` (سبز)
- **تاریخ انتخاب شده**: `#007bff` (آبی)
- **تاریخ امروز**: `#28a745` (سبز)
- **روزهای عادی**: `#ffffff` (سفید)

## مثال کامل

```python
import tkinter as tk
from shamsi_calendar import ModernShamsiDateEntry

class CalendarApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("برنامه تقویم شمسی")
        self.root.geometry("500x300")

        # ایجاد ورودی تاریخ
        self.date_entry = ModernShamsiDateEntry(self.root)
        self.date_entry.pack(padx=20, pady=20)

        # دکمه نمایش تاریخ
        show_btn = tk.Button(self.root, text="نمایش تاریخ",
                            command=self.show_date)
        show_btn.pack(pady=10)

    def show_date(self):
        selected_date = self.date_entry.get()
        print(f"تاریخ انتخاب شده: {str(selected_date)}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CalendarApp()
    app.run()
```

## تغییرات نسخه 0.2.0

- ✅ اضافه شدن کلاس `ModernShamsiDateEntry`
- ✅ رفع مشکل محاسبه روزهای اسفند
- ✅ بهبود UI و UX
- ✅ اضافه شدن قابلیت انتخاب مستقیم سال
- ✅ نمایش بهتر تاریخ انتخاب شده
- ✅ سازگاری با کدهای قبلی

## نیازمندی‌ها

- Python 3.6+
- tkinter (معمولاً همراه Python نصب می‌شود)
- jdatetime

## نصب

```bash
pip install jdatetime
```

## مجوز

این پروژه تحت مجوز MIT منتشر شده است.
