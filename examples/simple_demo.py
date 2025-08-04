# examples/simple_demo.py

import tkinter as tk
from customtkinter import CTkLabel
from shamsi_calendar import ShamsiDateEntry, ModernShamsiDateEntry

def show_selected_date():
    selected_old = old_date_entry.get()
    selected_new = new_date_entry.get()
    result = f'old: {str(selected_old)}\nnew: {str(selected_new)}'
    lbl_result.configure(text=result)

root = tk.Tk()
root.title("مقایسه تقویم شمسی")
root.geometry("400x400")
root.config(bg='#f8f9fa')

# فریم اصلی
main_frame = tk.Frame(root, bg='#f8f9fa')
main_frame.pack(fill='both', expand=True, padx=20, pady=20)

# عنوان
title = tk.Label(main_frame, text="مقایسه تقویم شمسی", 
                font=('Arial', 14, 'bold'),
                bg='#f8f9fa', fg='#333333')
title.pack(pady=(0, 20))

# تقویم قدیمی
old_label = tk.Label(main_frame, text="تقویم قدیمی:", 
                    font=('Arial', 10, 'bold'),
                    bg='#f8f9fa', fg='#333333')
old_label.pack(anchor='w')

old_date_entry = ShamsiDateEntry(main_frame)
old_date_entry.pack(fill='x', pady=(0, 15))

# تقویم جدید
new_label = tk.Label(main_frame, text="تقویم مدرن:", 
                    font=('Arial', 10, 'bold'),
                    bg='#f8f9fa', fg='#333333')
new_label.pack(anchor='w')

new_date_entry = ModernShamsiDateEntry(main_frame)
new_date_entry.pack(fill='x', pady=(0, 15))

# دکمه نمایش
btn = tk.Button(main_frame, text="نمایش تاریخ‌ها", 
                command=show_selected_date,
                bg='#007bff', fg='black',
                font=('Arial', 10, 'bold'),
                relief='flat', padx=20, pady=5)
btn.pack(pady=10)

# برچسب نتیجه
lbl_result = CTkLabel(main_frame, text="", width=200, height=100,
                     font=("Arial", 20), text_color='black',
                     anchor='center')
lbl_result.pack(pady=10)

root.mainloop()
