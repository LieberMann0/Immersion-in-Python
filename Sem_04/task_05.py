# Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

def prize(names: list[str], level: list[int], bonuses: list[str]) -> dict[str, float]:
    result = {}

    for name, salary, bonus in zip(names, level, bonuses):
        result[name] = (salary * float(bonus[:-1])) / 100
    return result

n = ["Вася", "Алёша", "Иван Иванович"]
l = [20000, 15000, 30000]
b = ["5.5%", "10.25%", "3.8%"]

print(prize(n, l, b))
