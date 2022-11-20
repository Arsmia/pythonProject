# # name = input("What is your name? ")
# # message = "Hello, " + name + "!"
# # print(message)
# #
# # response = input("What year were you born? ")
# # year = int(response)
# # age = 2022 - year
# # if year <= 2022:
# #     print("You are " + str(age) + " years old")
# # else:
# #     print("Enter the correct year")
# #
# # # print("My name is {username}. I'm {age}.format(username = "Sviatlana", age = 36))
# #
# # username = str("Sviatlana")
# # age = 36
# # print(f"My name is {username}. I\'m {age}.")
# #
# # print(ord("S"))
# # print(chr(83))
#
# # a = input()
# # print(a.upper())
# # print(a.capitalized()) - первый символ к верхнему регистру, остальные к нижнему.
#
# # a = "12345"
# # a.isdigit() - если хотя бы 1 символ - цифра вернет True
# # a.startwith("1") - True, если строка начинает с символа, переданного в качестве аргумента
# # a.replace (old, new, count)
# # a.split () - разбить текст на слова
#
# # a = input()
# # b = a.replace("'", "\\'").replace('"','\\"')
# # print(b)
#
# # a, b = map(int, input().split())
# # if a % 10 == 0 and b % 10 != 0:
# #     print("True")
# # elif a % 10 != 0 and b % 10 == 0:
# #     print("True")
# # else:
# #     print("False")
# #
# #
# # a,b = map(int, input().split())
# # l = (a**2+b**2)**0.5 - vector length
# # if l >= 10:
# #     print("True")
# # else:
# #     print("False")
# #
# # a = input()
# # if a == a[::-1]: - строка является палиндромом
# #     print("True")
# # else:
# #     print("False")
# #
# # a, b = map(int, input().split()) - На вход подаются два трехзначных числа. Верните True, если суммы цифр в них равны и False -- если не равны.
# # x = a // 100
# # y = a // 10 - x * 10
# # z = a - x * 100 - y * 10
# # m = b // 100
# # n = b // 10 - m * 10
# # o = b - m * 100 - n * 10
# # print(x + y + z == m + n + o)
# #
# # a = float(input()) - Напишите программу, которая реализует логику работы функции sign().
# # if a > 0:
# #     print("1")
# # elif a < 0:
# #     print("-1")
# # elif a == 0:
# #     print("0")
#
# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)
#
#
# a = float(input())
# if 1<=a<=5:
#     print("True")
# else:
#     print("False")
#
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# a = int(input())
# if a>0:
#     print(numbers[::a])
# На вход подается целое положительное число. Верните список чисел, которые нацело делятся на это число.
#
#
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = int(input())
# if a in numbers:
#     print("True")
# else:
#     print("False")
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] - На вход подается число. Удалите все элементы списка после элемента, равного этому числу.
# a = int(input())
# x = a - 1
# if a in numbers:
#     print(numbers[:x])
# else:
#     print(numbers)

# numbers = list(map(int, input().split())) - На вход подается список целых чисел. Поменяйте местами первый и последний элементы.
# a = numbers[0]
# b = numbers[-1]
#
# if len(numbers) > 1:
#     del numbers[0]
#     del numbers[-1]
#     numbers.insert(0, b)
#     numbers.append(a)
#     print(numbers)
# else:
#     print(numbers)

# N = int(input()) - на вход подается число N. Найдите его факториал, то есть произведение натуральных чисел от 1 до N:
# x = 1
# for i in range(1, N):
#     x *= i + 1
# print(x)
#
# n, k = input().split()
# n = int(n)
# k = float(k)
#
# s = 0.0
# for i in range(1, n+1):
#     i = i ** k
#     s += i
# print(round(s,3))


# number = int(input()) - Вводится целое положительное число n. Выведите True, если число простое и False, если составное (то есть, имеет делители, отличные от 1 и самого себя).
# x = 0 - делитель
# for i in range(1, number//2 + 1):
#     if number % i == 0:
#         x += 1
# print(x <= 2)

# result = [] - Найдите и выведите в порядке возрастания все двузначные числа, которые равны утроенному произведению своих цифр и выведите результат в виде списка.  Числа в списке должны быть расположены в порядке возрастания.
# for i in range(10, 100):
#     a = i//10%10
#     b = i % 10
#     if a*b*3 == i:
#         result.append(i)
# print(result)

# i = 0
# while i <= 4:
#     i += 1
#     print("Hello, while loops!")

# numbers = [22, 9, 37, 44, 46, 69, 24, 100, 97, 57, 1, 6, 27, 96, 16, 82, 10, 95, 99, 78, 62, 50, 77, 86, 56, 40, 49, 32, 53, 76, 63, 67, 52, 0, 93, 84, 28, 8, 41, 79, 25, 21, 71, 43, 81, 72, 20, 90, 39, 75, 85, 14, 15, 60, 64, 5, 66, 4, 36, 98, 80, 12, 47, 91, 73, 45, 31, 65, 87, 74, 11, 34, 33, 18, 58, 23, 68, 94, 92, 17, 26, 88, 35, 13, 7, 42, 38, 19, 48, 29, 3, 59, 55, 51, 89, 2, 70, 83, 61, 54, 30]
# i = 0
# x = 1
# for i in range(1, len(numbers)-1):
#     i += 1
#     if int(numbers[i-1]) < int(numbers[i]) and int(numbers[i])>int(numbers[i+1]):
#         x += 1
# print(x)

# while i<(len(numbers)):
#     if numbers[i-1] < numbers[i] and numbers[i] > numbers[i+1]:
#         x += 1
#     i += 1
# print(x)

# start, goal, days = map(int, input().split())
# i = 0
# while start < goal:
#     i += 1
#     start *= 1.1
#     if start >= goal and i < days:
#         break
#     elif start >= goal and i >= days:
#         print('False')
# print('True')

phonebook = {
    "Arseni": "694627564",
    "Sviatlana": "694627561",
    "Anton": "795554296",
}
name_book = dict(
    Anton = "Strachuk",
    Sviatlana = "Strachuk",
    Mia = "Strachuk",
    Arseni = "Strachuk",
)

phonebook["Mia"] = "Ipad_10"

if "Arseni" in phonebook:
    print("True")

if "Mia" in name_book:
    print(name_book["Mia"])

print(phonebook["Anton"])

phonebook.get("Mama", "this contact is unavailable")

phonebook.pop("Mama", "this opertion is unavailable")

print(len(name_book))

# На вход программы подаются kk пар слов: слово на русском и его перевод на испанский. Последней строкой подается еще одно слово на русском. Выведите перевод последнего слова.
# k = int(input())
# vocabulary = {}
#
# for i in range(0, k):
#     ru, sp = input().split()
#     vocabulary.setdefault(ru, sp)
# x = input()
# print(vocabulary[x])

for name, phone in phonebook.items():
    print(name, phone)

for k, v in name_book.items():
    print(k, v)

for name in phonebook.keys():
    print(name)

for name in name_book.values():
    print(name)

phonebook.update(name_book)
print(phonebook)