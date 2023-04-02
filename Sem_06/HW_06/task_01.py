# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

__all__ = ["start_game", "guess_riddle"]


def start_game(riddles_dict: dict, number_trys: int):
    for key, item in riddles_dict.items():
        count = guess_riddle(key, item, number_trys)
        if count == 0:
            print("Не отгадали")
        else:
            print(f"Вы угадали с {count} раза!")


def guess_riddle(riddle: str, answers: list, n_trys: int) -> int:
    print(f"Загадка: {riddle}.")
    for i in range(n_trys):
        answer = input("Что это? - ").lower()
        if answer in answers:
            return i + 1
    return 0


if __name__ == '__main__':
    riddles_dict = {"Зимой и летом одним цветом.":["елка", "ель", "сосна"],
                    "Красна девица сидит в темнице, а коса на улице.":["морковь", "морковка"]
    }    
    attempts = 3    
    start_game(riddles_dict, attempts)