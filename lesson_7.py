import names
import secrets


# a = [1,2,3]
# for i in a:
#     print(i)
#
# b = list(range(20))
# print(b)
#
# c = [i for i in range(20) if i % 2 == 0]
# print(c)
#
# d = [i for i in range(20) if i % 2 != 0]
# print(d)
#
# d_1 = list(range(2, 20, 2))
# print(d_1)
#
# i = 0
# e = ["item_" + str(i) for i in range(20)]
# print(e)
#
# f = []
# for i in range(20):
#     h = names.get_full_name()
#     f.append(h)
# print(f)

# a = []
# for i in range(20):
#     k = []
#     b = names.get_full_name()
#     c = list(range(18,99))
#     d = list(range(1500,5000))
#     e = secrets.choice(c)
#     f = secrets.choice(d)
#     k.append(b)
#     k.append(e)
#     k.append(f)
#     a.append(k)
# print(a)
#
# def name_1():
#     a = []
#     for i in range(40):
#         name = names.get_full_name()
#         print(name)
#     return a
#
# name_1()

# def name_1():
#     a = []
#     for i in range(20):
#         name = names.get_full_name()
#         a.append(name)
#     return a
# name_2 = name_1()
# print(name_2)
a = []

# def amount():
#
#     word = input("Word: ")
#     how_many = int(input("Repeat: "))
#     for i in range(how_many):
#         a.append(word + str(i))
#     return a
#
# print(amount())
#
# file = "C:/Users/Светлана/PycharmProjects/pythonProject/list.txt"
#
# with open(file, "w") as f:
#     writer = f.writelines("\n".join(a))

def year():
    a = int(input("Enter year: "))
    if a % 4 == 0:
        print("это високосный год")
    else:
        print("это невисокосный год")
    return a
year()
