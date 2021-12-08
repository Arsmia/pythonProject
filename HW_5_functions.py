#
# # 1.Написать скрипт который в создаст список целых чисел.
#
# numbers = []
#
# for i in range(1,71):
#     numbers.append(i)
# print("numbers = ", numbers)
#
# # 2.Написать скрипт который в создаст список целых чётных чисел.
# numbers = [i for i in range(1,71) if i % 2 == 0]
# print("numbers = ", numbers)
# # 3.Написать скрипт который в создаст список целых нечётных чисел.
#
# numbers = [i for i in range(1,71) if i % 2 != 0]
# print("numbers = ", numbers)
# # 4.Написать скрипт который из списка целых чисел выведет чётные числа.
# numbers = [1,2,3,4,5,6,7,8,9,10]
# numbers_2 = []
# for element in numbers:
#     if element % 2 == 0:
#         numbers_2.append(element)
# print("numbers_2 = ", numbers_2)
# # 5.Написать скрипт который из списка целых чисел выведет нечётные числа.
# numbers = [1,2,3,4,5,6,7,8,9,10]
# numbers_2 = []
# for i in numbers:
#     if i % 2 != 0:
#         numbers_2.append(i)
# print("numbers_2 = ", numbers_2)
# # 6.Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.
#
# numbers = [i for i in range(1,71) if i % 2 == 0 if i % 5 == 0]
# print("numbers = ", numbers)
#
# # 7.Написать скрипт который из списка целых чисел выведет количество чётных чисел которые делятся на 5 без остатка.
# numbers = len([i for i in range(1,71) if i % 5 == 0])
# print("numbers = ", numbers)
# # 8.Написать скрипт который создаст список целых рандомных чисел.
import random

# numbers = list(range(random.randint(1, 71)))
# print("numbers = ", numbers)
# # 9.Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его на списки по 5 элементов.
# numbers = list(range(1, 71))
#
# def chunk_list(lst,chunk_size):
#
#     for i in range(0, len(lst), chunk_size):
#         yield lst[i:i + chunk_size]
#
# print("list_5 = ", list(chunk_list(numbers, 5)))

# 10.Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.
# numbers = list(range(1, 71))

#
# def lists(l_1, l_2):
#     numbers = list(range(1, 71))
#
#
# l_1 = []
# l_2 = []
#
# for i in numbers:
#
#     if i % 2 == 0:
#         l_1.append(i)
#     if i % 2 != 0:
#         l_2.append(i)
#
# print("l_1 = ", l_1)
# print("l_2 = ", l_2)
#
# lists(l_1, l_2)


# 11.Написать скрипт который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.
from typing import Union, Any, List

stars_5 = []
for i in range(1, 71):
    list_5 = random.sample(range(1, 71), 5)
    stars_5.append(list_5)
print("stars_5 = ", stars_5)


# 12.Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars

# list_sum = list(map(sum, stars_5))
# print("list_sum = ", list_sum)
# 13.Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка. В одном списке внутренние списки из 5_stars сумма чисел которых >= 100, а другой сумма чисел которых < 100. Если какого-то списка не получится, то вместо него вернуть текст “No lists”
#
# def lists(stars_5):
#     l_3 = []
#     l_4 = []
#
#     for i in range(len(stars_5)):
#         if sum(stars_5[i]) >= 100:
#             l_3.append(stars_5[i])
#
#         elif sum(stars_5[i]) < 100:
#             l_4.append(stars_5[i])
#     if not l_3:
#         print("no lists")
#     else:
#         print("l_3 = ", l_3)
#     if not l_4:
#         print("no lists")
#     else:
#         print("l_4 = ", l_4)
#
# lists(stars_5)
#

# 14.Написать функцию которая получив на вход ваш возраст, выведет вам через какой срок вы сумеете отложить 10 000$, 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.
# def kubyshka():
#     while True:
#             age = int(input("Введите возраст: "))
#             money = int(input("Ваша сумма накоплений: "))
#             money_month = int(input("Сумма накоплений в месяц: "))
#
#         except:
#             print("Введите правильное значение: ")
#
#
# age_10k = (10000 - int(money) + int(money_month) * 12) // 12 + int(age)
# age_20k = (20000 - int(money) + int(money_month) * 12) // 12 + int(age)
# age_30k = (30000 - int(money) + int(money_month) * 12) // 12 + int(age)
# age_50k = (50000 - int(money) + int(money_month) * 12) // 12 + int(age)
# age_100k = (100000 - int(money) + int(money_month) * 12) // 12 + int(age)
# print("Нужна сумма 10000$ собрана за  ", age_10k)
# print("Нужна сумма 20000$ собрана за  ", age_20k)
# print("Нужна сумма 30000$ собрана за  ", age_30k)
# print("Нужна сумма 50000$ собрана за  ", age_50k)
# print("Нужна сумма 100000$ собрана за  ", age_100k)
# #
# kubyshka()

# 15.Написать фукнцию, которая получив на вход стартовую ЗП Junior QA и количество лет стажа, выведет в консоль прогресс роста ЗП по каждому году из выведенного количества лет стажа.
# Внутри функция учитывает дорожную карту развития скилов QA и список, полезных для компании, активностей которые может делать QA.
# def salary(progres):
#     work_experience = 2
#     salary_junior = 500
#     while True:
#         salary = int(input("Введите ЗП: "))
#
#
# progres = (salary / salary_junior) ** 1 / work_experience - 1
#
# print("progres = ", progres)
#
# salary(progres)


# 16.Написать скрипт который сгенерирует список имён пользователей. Список имён вывести в консоль.
from russian_names import RussianNames

rn = RussianNames(count=70, patronymic=False, transliterate=True)
for person in rn:
    print(person)

# 17.Написать скрипт который сгенерирует список имён файлов. К каждому имени  файла надо прикрепить номер итерации цикла как порядковый номер.
item = []
new_users = [str(RussianNames)]
for i in new_users:
    new_users.append(str(item) + str(i) + ".txt")
    item += 1
print(new_users)