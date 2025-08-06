import tkinter as tk
from tkinter import ttk
import jdatetime
from .utils import get_days_in_month
from .locale.fa import WEEKDAYS_FA, MONTH_NAMES_FA


class ModernShamsiDateEntry(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master)
        self.selected_date = jdatetime.date.today()
        self.configure(style='Modern.TFrame')
        
        # تنظیم استایل‌ها
        self.setup_styles()
        
        # ایجاد فریم اصلی
        self.main_frame = ttk.Frame(self, style='Modern.TFrame')
        self.main_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # ورودی تاریخ
        self.entry_frame = ttk.Frame(self.main_frame, style='Modern.TFrame')
        self.entry_frame.pack(fill='x', pady=(0, 5))
        
        self.entry = ttk.Entry(self.entry_frame, width=20, font=('Arial', 10), 
                              style='Modern.TEntry')
        self.entry.pack(side='left', fill='x', expand=True)
        self.entry.insert(0, self.format_date(self.selected_date))
        self.entry.bind('<KeyRelease>', self.on_entry_change)
        
        # دکمه تقویم
        self.calendar_btn = ttk.Button(self.entry_frame, text="📅", width=3, 
                                      command=self.open_calendar, style='Modern.TButton')
        self.calendar_btn.pack(side='right', padx=(5, 0))
        
        # پنجره تقویم
        self.calendar_window = None

    def setup_styles(self):
        """تنظیم استایل‌های مدرن"""
        style = ttk.Style()
        
        # استایل فریم اصلی
        style.configure('Modern.TFrame', background='#f8f9fa', relief='flat')
        
        # استایل ورودی
        style.configure('Modern.TEntry', 
                       fieldbackground='white',
                       borderwidth=2,
                       relief='solid',
                       font=('Arial', 10))
        
        # استایل دکمه
        style.configure('Modern.TButton',
                       background='#007bff',
                       foreground='black',
                       borderwidth=0,
                       relief='flat',
                       font=('Arial', 10, 'bold'))
        
        # استایل دکمه‌های تقویم
        style.configure('Calendar.TButton',
                       background='#ffffff',
                       foreground='#333333',
                       borderwidth=1,
                       relief='solid',
                       font=('Arial', 9))
        
        style.map('Calendar.TButton',
                 background=[('active', '#e3f2fd'), ('pressed', '#bbdefb')])
        
        # استایل دکمه امروز
        style.configure('Today.TButton',
                       background='#28a745',
                       foreground='black',
                       borderwidth=0,
                       relief='flat',
                       font=('Arial', 9, 'bold'))
        
        # استایل دکمه انتخاب شده
        style.configure('Selected.TButton',
                       background='#007bff',
                       foreground='white',
                       borderwidth=0,
                       relief='flat',
                       font=('Arial', 9, 'bold'))

    def format_date(self, date):
        """فرمت کردن تاریخ برای نمایش"""
        return f"{date.year}/{date.month:02d}/{date.day:02d}"

    def on_entry_change(self, event=None):
        """هنگام تغییر ورودی"""
        try:
            text = self.entry.get()
            if text and '/' in text:
                parts = text.split('/')
                if len(parts) == 3:
                    year, month, day = map(int, parts)
                    self.selected_date = jdatetime.date(year, month, day)
        except:
            pass

    def open_calendar(self):
        """باز کردن پنجره تقویم"""
        if self.calendar_window:
            self.calendar_window.destroy()
        
        self.calendar_window = tk.Toplevel(self)
        self.calendar_window.title("تقویم شمسی")
        self.calendar_window.resizable(False, False)
        self.calendar_window.configure(bg='#f8f9fa')
        
        # تنظیم موقعیت پنجره
        x = (self.winfo_screenwidth() // 2) - (400 // 2)
        y = ((self.winfo_screenheight() // 2) - (500 // 2)) - 20
        self.calendar_window.geometry(f"400x500+{x}+{y}")
        
        self.current_year = self.selected_date.year
        self.current_month = self.selected_date.month
        
        self.create_calendar_widgets()
        self.render_calendar()

    def create_calendar_widgets(self):
        """ایجاد ویجت‌های تقویم"""
        # فریم اصلی
        main_frame = ttk.Frame(self.calendar_window, style='Modern.TFrame')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # هدر با نام ماه و سال
        header_frame = ttk.Frame(main_frame, style='Modern.TFrame')
        header_frame.pack(fill='x', pady=(0, 10))
        
        # دکمه‌های تغییر ماه
        prev_btn = ttk.Button(header_frame, text="◀", width=3,
                             command=lambda: self.change_month(-1), style='Modern.TButton')
        prev_btn.pack(side='left')
        
        # نمایش ماه و سال
        self.header_label = tk.Label(header_frame, text="", 
                                   font=('Titr', 15, 'bold'), 
                                   bg='#f8f9fa', fg='#333333')
        self.header_label.pack(side='left', expand=True)
        
        next_btn = ttk.Button(header_frame, text="▶", width=3,
                             command=lambda: self.change_month(1), style='Modern.TButton')
        next_btn.pack(side='right')
        
        # فریم انتخاب سال
        year_frame = ttk.Frame(main_frame, style='Modern.TFrame')
        year_frame.pack(fill='x', pady=(0, 10))
        
        tk.Label(year_frame, text="(سال)", font=('Titr', 10), 
                bg='#f9f9fa', fg='#333333').pack(side='left')
        
        self.year_var = tk.StringVar(value=str(self.current_year))
        year_spinbox = tk.Spinbox(year_frame, from_=1300, to=1500, 
                                 textvariable=self.year_var, width=8,
                                 font=('Arial', 10, 'bold'), command=self.on_year_change)
        year_spinbox.pack(side='left', padx=(5, 0))
        
        # فریم روزهای هفته
        weekdays_frame = ttk.Frame(main_frame, style='Modern.TFrame')
        weekdays_frame.pack(fill='x', pady=(0, 5))
        
        # نام روزهای هفته
        weekday_names = ['شنبه', 'یکشنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنج‌شنبه', 'جمعه']
        for i, day_name in enumerate(weekday_names):
            label = tk.Label(weekdays_frame, text=day_name, 
                           font=('Titr', 8, 'bold'),
                           bg='#e9ecef', fg='#495057',
                           width=5, height=2)
            label.grid(row=0, column=i, padx=1, pady=1, sticky='nsew')
        
        # تنظیم وزن ستون‌ها
        for i in range(7):
            weekdays_frame.grid_columnconfigure(i, weight=1)
        
        # فریم روزهای ماه
        self.days_frame = ttk.Frame(main_frame, style='Modern.TFrame')
        self.days_frame.pack(fill='both', expand=True)
        
        # تنظیم وزن ردیف‌ها و ستون‌ها
        for i in range(7):
            self.days_frame.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.days_frame.grid_rowconfigure(i, weight=1)
        
        # فریم دکمه‌ها
        buttons_frame = ttk.Frame(main_frame, style='Modern.TFrame')
        buttons_frame.pack(fill='x', pady=(10, 0))
        
        # دکمه امروز
        today_btn = ttk.Button(buttons_frame, text="امروز", 
                              command=self.go_to_today, style='Today.TButton')
        today_btn.pack(side='left')
        
        # دکمه تایید
        ok_btn = ttk.Button(buttons_frame, text="تایید", 
                           command=self.confirm_selection, style='Modern.TButton')
        ok_btn.pack(side='right')
        
        # دکمه لغو
        cancel_btn = ttk.Button(buttons_frame, text="لغو", 
                               command=self.cancel_selection, style='Modern.TButton')
        cancel_btn.pack(side='right', padx=(0, 5))

    def on_year_change(self):
        """هنگام تغییر سال"""
        try:
            self.current_year = int(self.year_var.get())
            self.render_calendar()
        except ValueError:
            pass

    def change_month(self, step):
        """تغییر ماه"""
        self.current_month += step
        if self.current_month < 1:
            self.current_month = 12
            self.current_year -= 1
        elif self.current_month > 12:
            self.current_month = 1
            self.current_year += 1
        
        self.year_var.set(str(self.current_year))
        self.render_calendar()

    def render_calendar(self):
        """رندر کردن تقویم"""
        # پاک کردن روزهای قبلی
        for widget in self.days_frame.winfo_children():
            widget.destroy()
        
        # به‌روزرسانی هدر
        month_name = MONTH_NAMES_FA[self.current_month - 1]
        self.header_label.config(text=f"{month_name} {self.current_year}")
        
        # محاسبه روز شروع ماه
        first_day = jdatetime.date(self.current_year, self.current_month, 1)
        start_day = (first_day.togregorian().weekday() + 1) % 7
        
        # تعداد روزهای ماه
        days_in_month = get_days_in_month(self.current_year, self.current_month)
        
        row = 0
        col = start_day
        
        # ایجاد دکمه‌های روزها
        for day in range(1, days_in_month + 1):
            btn = tk.Button(self.days_frame, text=str(day), 
                           font=('Arial', 10),
                           width=5, height=2,
                           command=lambda d=day: self.select_date(d))
            
            # تنظیم رنگ دکمه
            if (self.current_year == self.selected_date.year and 
                self.current_month == self.selected_date.month and 
                day == self.selected_date.day):
                btn.configure(bg='#007bff', fg='white', relief='flat')
            elif (self.current_year == jdatetime.date.today().year and 
                  self.current_month == jdatetime.date.today().month and 
                  day == jdatetime.date.today().day):
                btn.configure(bg='#28a745', fg='white', relief='flat')
            else:
                btn.configure(bg='white', fg='#333333', relief='solid')
            
            btn.grid(row=row, column=col, padx=1, pady=1, sticky='nsew')
            
            col += 1
            if col > 6:
                col = 0
                row += 1

    def select_date(self, day):
        """انتخاب تاریخ"""
        self.selected_date = jdatetime.date(self.current_year, self.current_month, day)
        self.render_calendar()

    def go_to_today(self):
        """رفتن به تاریخ امروز"""
        today = jdatetime.date.today()
        self.current_year = today.year
        self.current_month = today.month
        self.selected_date = today
        self.year_var.set(str(self.current_year))
        self.render_calendar()

    def confirm_selection(self):
        """تایید انتخاب"""
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.format_date(self.selected_date))
        if self.calendar_window:
            self.calendar_window.destroy()
            self.calendar_window = None

    def cancel_selection(self):
        """لغو انتخاب"""
        if self.calendar_window:
            self.calendar_window.destroy()
            self.calendar_window = None

    def get(self):
        """برگرداندن تاریخ انتخاب‌شده"""
        return self.selected_date


# نگه داشتن کلاس قدیمی برای سازگاری
class ShamsiDateEntry(ModernShamsiDateEntry):
    """کلاس قدیمی برای سازگاری با کدهای قبلی"""
    pass
