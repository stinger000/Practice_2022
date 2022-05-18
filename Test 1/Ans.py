# Решение контрольной номер 1

# Задание 1

def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


# Задание 2

def days_in_year(year: int) -> int:
    if is_leap_year(year):
        return 366
    return 365


# Задание 3

# Возвращает количество дней в заданном месяце
def days_in_month(month: int, year: int) -> int:
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        months[1] = 29
    return months[month - 1]


def is_date_correct(day: int, month: int, year: int) -> bool:
    if day <= 0 or month <= 0 or month > 12:
        return False
    max_days_count = days_in_month(month, year) # Максимальное количество дней в текущем месяце
    if day > max_days_count:
        return False
    return True


# Задание 4

def time_delta_in_days(init_day, init_month, init_year,
                       end_day, end_month, end_year) -> int:
    days = 0
    if end_year > init_year:

        days += days_in_month(init_month, init_year) - init_day

        current_month = init_month + 1
        while current_month <= 12:
            days += days_in_month(current_month, init_year)
            current_month += 1

        current_year = init_year + 1
        while current_year < end_year:
            days += days_in_year(current_year)
            current_year += 1

        current_month = 1
        while current_month < end_month:
            days += days_in_month(current_month, end_month)
            current_month += 1
        days += end_day
        return days


print(
    time_delta_in_days(18, 5, 2022, 15, 3, 2047)
)

