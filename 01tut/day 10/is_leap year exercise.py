def is_leap(year_):
    if year_ % 4 == 0:
        if year_ % 100 == 0:
            if year_ % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year_int, month_int):
    if month_int > 12 or month_int < 1:
        return "Invalid month input"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    selected_month = month_days[month_int - 1]
    if is_leap(year_int) and month_int == 2:
        return selected_month + 1
    else:
        return selected_month


# Do not change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
