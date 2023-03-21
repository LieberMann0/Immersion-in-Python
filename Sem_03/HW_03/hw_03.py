# Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут
# в рюкзак передав его максимальную грузоподъёмность. 

import itertools

things = {
    "котелок": 1,
    "посуда": 2,
    "топор": 2,
    "палатка": 3,
    "спальник": 2,
    "продукты": 10,
    "одежда": 3,
    "обувь": 3,
    "аптечка": 1,
    "гигиена": 2,
    "техсредства": 4
}

MAX_WEIGHT = 15
i = 2
thingspack = []
weight = 0
while i <= len(things):
    for key, value in things.items():        
        things_set = itertools.combinations(things.keys(), i)        
        for item in things_set:            
            for j in item:                
                thingspack.append(j)                
                weight += things[j]
                if weight == MAX_WEIGHT:
                    print(thingspack)
            thingspack = []
            weight = 0
    i += 1
