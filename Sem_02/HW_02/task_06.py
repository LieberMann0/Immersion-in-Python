# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import decimal

balance = 0
count = decimal.Decimal(0)
COUNT_OPER = 3
action = 4
MULTIPLICITY = 50
MIN_SUM = 30
MAX_SUM = 600
STRAF_PERCENTAGE = 0.015
BONUS_PERCENTAGE = 0.03
TAX_PERCENTAGE = 0.1
TOP_SUM = 5_000_000

decimal.getcontext().prec=2

while action < 1 or action > 3:
    action = int(input("Пополнить - 1, Снять - 2, Выйти - 3 - "))

    match action:
        case 1:
            top_up = int(input(f"Сумма пополнения (кратна {MULTIPLICITY}) - "))

            while top_up % MULTIPLICITY != 0:                
                top_up = int(input(f"Сумма пополнения должна быть кратна {MULTIPLICITY} - "))
                if balance > TOP_SUM:
                    balance -= balance * TAX_PERCENTAGE

            balance += top_up
            count += 1

            if count % COUNT_OPER == 0:                
                balance += balance * BONUS_PERCENTAGE
            
            if balance > TOP_SUM:
                    balance -= balance * TAX_PERCENTAGE
            
            print("Баланс -", balance)
            print()

        case 2:
            withdraw = int(input(f"Сумма для снятия (кратна {MULTIPLICITY}) - "))            

            while withdraw % MULTIPLICITY != 0 and withdraw < balance:
                withdraw = int(input(f"Сумма для снятия (кратна {MULTIPLICITY}) - "))

                if withdraw > balance:
                    print("Сумма снятия превышает сумму на счете -", balance)

                if balance > TOP_SUM:
                    balance -= balance * TAX_PERCENTAGE

            balance -= withdraw

            if balance > 0:
                to_down = balance * STRAF_PERCENTAGE
                if to_down < MIN_SUM:
                    balance -= MIN_SUM                    
                elif to_down > MAX_SUM:
                    balance -= MAX_SUM
                else:
                    balance -= to_down            
            
            count += 1

            if count % COUNT_OPER == 0:
                balance += balance * BONUS_PERCENTAGE

            if balance > TOP_SUM:
                    balance -= balance * TAX_PERCENTAGE

            print("Баланс -", balance)
            print()
        
        case 3:
            print("До свидания")
            break
