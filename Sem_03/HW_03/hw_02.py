#   В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов.

my_string = "Алексаандр Сергеевич Пушкин родился 26 мая (6 июня) 1799, Москва, \
    умер 29 января (10 февраля) 1837, Санкт-Петербург — русский поэт, драматург \
    и прозаик, заложивший основы русского реалистического направления, \
    литературный критик и теоретик литературы, историк, публицист, журналист. \
    Один из самых авторитетных литературных деятелей первой трети XIX века. \
    Ещё при жизни Пушкина сложилась его репутация величайшего национального \
    русского поэта. Пушкин рассматривается как основоположник современного \
    русского литературного языка. В 20-30 годах XIX века произошло формирование \
    современного литературного русского языка. Его создателем признаётся Пушкин, \
    а его произведения считаются энциклопедией образцов применения русского языка. \
    Однако процесс выработки адекватной оценки роли Пушкина, как создателя \
    современного языка шёл довольно долго. Он потребовал накопления значительного \
    объёма знаний о фактах и явлениях русского языка времени до Пушкина, \
    эпохи Пушкина и после него, подробного анализа этих фактов, и соответствующего \
    развития лингвистики русского языка, на что ушло, около 120 лет. \
    Ни в конце XIX в., ни в первое десятилетие XX в. об этом речи не было. \
    Даже в начале 40-х годов XX в. не все разделяли взгляд на Пушкина, как \
    на основоположника современного русского литературного языка. Окончательным \
    признанием такой роли Пушкина можно считать издание статьи известного \
    исследователя русского языка В. В. Виноградова, которая так и называлась \
    «А. С. Пушкин — основоположник русского литературного языка» \
    Вместе с этим новации А. С. Пушкина в области русского языка вошли \
    в практику по историческим меркам очень быстро. Несмотря на \
    существенные изменения, произошедшие в языке за почти двести лет, \
    прошедшие со времени создания его крупнейших произведений, и явные \
    стилистические различия языка Пушкина и современных писателей, система \
    современного русского языка, его грамматический, фонетический и \
    лексико-фразеологический строй в своём основном ядре остались и \
    продолжают оставаться и развиваться в пределах тех норм, что сформировал Пушкин."

my_list = my_string.replace(".", "").replace(",", "").replace("—", "").lower().split()

#count = 0
# for i in my_list:
#     count += 1
# print(f"Количество слов - {count}")

print(f"Количество слов - {len(my_list)}")

frequent = {my_list[i]: my_list.count(my_list[i]) for i in range(len(my_list))}
freq_10 = (sorted((value, key) for key, value in frequent.items())[:-11:-1])
print("Часто встречающиеся слова:")

for item in freq_10:    
    a = item[0]
    b = item[1]
    print(f"{a} раз - {b}")


# print("Часто встречаются слова:")
# print(sorted(frequent, key=my_string.count)[:-11:-1], sep="\n")


# freq_10 = sorted(frequent.values())[:-11:-1]
# print("Часто встречаются слова:")
# for key, value in frequent.items():
#     if value in freq_10:
#         print(f"{value} раз - {key}")  
  