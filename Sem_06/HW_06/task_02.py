# Создать модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY.
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

__all__ = ["check_date"]

_EVERY_FOURTH = 4
_FEBRUARY = 2
_LEAP_DAYS = 29
_BEGIN = 1
_MONTHS_DAYS = {1: 31,
                2: 28,
                3: 31,
                4: 30,
                5: 31,
                6: 30,
                7: 31,
                8: 31,
                9: 30,
                10: 31,
                11: 30,
                12: 31
}


def _leap_year(year: int) -> bool:
    return not year % _EVERY_FOURTH


def check_date(date: str) -> bool:
    day, month, year = [int(element) for element in date.split('.')]

    if _leap_year(year):
        mon_day = _MONTHS_DAYS.copy()
        mon_day[_FEBRUARY] = _LEAP_DAYS
    else:
        mon_day = _MONTHS_DAYS

    if month in mon_day and _BEGIN <= day <= mon_day.get(month):
        return True
    return False


if __name__ == '__main__':
    print(check_date('01.01.0001'))       
    print(check_date('31.12.9999'))
    print(check_date('28.02.0001'))
    print(check_date('29.02.0004')) 
    print(check_date('29.02.0001'))
    print(check_date('32.01.0001'))


