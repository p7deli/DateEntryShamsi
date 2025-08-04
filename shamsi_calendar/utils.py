# shamsi_calendar/utils.py
import jdatetime

def get_days_in_month(year, month):
    """تعداد روزهای ماه شمسی"""
    if month <= 6:
        return 31
    elif month <= 11:
        return 30
    else:
        # اسفند: بررسی سال کبیسه
        try:
            # تلاش برای ایجاد تاریخ 30 اسفند
            jdatetime.date(year, 12, 30)
            return 30
        except ValueError:
            return 29
