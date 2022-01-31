# ages = {"Dave": 24, "Mary": 42, "John": 58}
# print(ages["Dave"])
# print(ages["John"])
#
# primary = {
#     "red": [255, 25, 10],
#     "green": [10, 25, 255],
#     "blue": [25, 255, 10],
# }
#
# print(primary["red"])
# print(primary["blue"])
#
# bad_dict = {
#     False: "one two three",
# }
#
#
# try:
#     print("Hello")
#     print(1/0)
# except ZeroDivisionError:
#     print("Divided be zero")
# finally:
#     print("This code will run no matter what")
#
#
# try:
#     print(1)
#     print(10/0)
# except ZeroDivisionError:
#     print("unknown_var")
# finally:
#     print("This is executed last")
#
# a = "{x}, {y}".format(x=5, y =12)
# print(a)
#
# str = "{c}, {b}, {a}".format(a=5, b=9, c=7)
# print(str)
#
# print(",".join(["spam", "eggs", "ham"]))
#
# print("Hello me".replace("me", "world"))
#
# print("This is a sentence.".startswith("This"))
#
# print("This is a sentence.".endswith("sentence."))
#
# print("This is a sentence.".upper())
#
# print("THIS IS A SENTENCE".lower())
#
# print("spam, eggs, ham".split(","))
#
# print(abs(-99))
# print(abs(50))
# print(abs(0.1))
#
#
# a = min([sum([11,22]),max(abs(-30),2)])
# print(a)
#
# nums = [55, 44, 33, 22, 11]
# if all([i > 5 for i in nums]):
#     print("All larger than 5")
# if any([i%2 == 0 for i in nums]):
#     print("At least one is even")
# for v in enumerate(nums):
#     print(v)
#
# filename = input("Enter a filename: ")

# with open(filename) as f:
#     text = f.read()
#
# print(text)
#
#
# def count_char(text, char):
#     count = 0
#     for c in text:
#         if c == char:
#             count += 1
#     return count
# print(count_char(text, "u"))
#
# for char in "mu":
#     perc = 100 * count_char(text, char) / len(text)
#     print("{0} - {1}%".format(char, round(perc, 2)))

# nums = (55, 44, 33, 22)
# print(max(min(nums[:2]),abs(-42)))
#
# def pure_function(x, y):
#     temp = x + 2*y
#     return temp/(2*x+y)
#
# some_list = []
#
# def impure(arg):
#     some_list.append(arg)
#
#
# def my_func(f, arg):
#     return f(arg)
#
# my_func(lambda x: 2*x*x, 5)
#
#
# def add_five(x):
#     return x + 5
#
# nums = [11, 22, 33, 44, 55]
# result = list(map(add_five, nums))
# print(result)
#
# result = list(map(lambda x: x+5, nums))
# print(result)
#
# res = list(filter(lambda x: x%2 ==0, nums))
# print(res)
#
#
# names = ["Mia", "Sviatlana", "Anton", "Arseni"]
# result_names = list(filter(lambda x: len(x) > 5, names))
# print(result_names)
#
#
# def countdown(i):
#     while i > 0:
#         yield i
#         i -= 1
# for i in countdown(25):
#     print(list(countdown(i)))

# def infinite_five():
#     while True:
#         yield 5
# for i in infinite_five():
#     print(i)

# def make_word():
#     word = ""
#     for i in "spam":
#         word += i
#         yield word
# print(list(make_word()))

def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial(8))


# def sum_to(x):
#     return x+sum_to(x-1)
# print(sum_to(5))

# def is_even(x):
#     if x == 0:
#         return True
#     else:
#         return is_odd(x-1)
# def is_odd(x):
#     return not is_even(x)
# print(is_odd(17))
# print(is_even(23))
#
from itertools import count

for i in count(1):
    print(i)
    if i >= 11:
        break
#
from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))
# # takewhile - возвращает элементы из итер.объекта, которые удовл. предиккативной функции;
# # chain -  объединяет объекты в один;
# # accumulate - возвращает сумму знаяений внуртри объекта;
#
#
# from itertools import product, permutations
#
# letter = ("A", "B")
# print(list(product(letter, range(2))))
# print(list(permutations(letter)))
#
# a = {1,2}
# print(len(list(product(range(3), a))))
#
# nums = {1, 2, 3, 4, 5, 6}
# nums = {0, 1, 2, 3}&nums
# nums = filter(lambda x: x>1, nums)
# print(len(list(nums)))
#
# # def power(x, y):
# #     if y == 0:
# #         return 1
# #     else:
# #         return x*power(x, y-1)
# #
# # print(power(2, 3)

# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))
#
#
# n = int(input())
# a = 1
# b = 1
# def fib(n):
#     while b < n:
#         print(b, end = " ")
#         a, b = b, a+b
#
# print(fib(n))

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
class Cat(Animal):
    def purr(self):
        print("Purr ...")
class Dog(Animal):
    def bark(self):
        print("Woof!")
fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()


class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def bark(self):
        print("Grrr......")
class Dog(Wolf):
    def bark(self):
        print("Wolf*")
husky = Dog("Max", "grey")
husky.bark()


class A:
    def method(self):
        print("A method")
class B(A):
    def another_method(self):
        print("B method")
class C(B):
    def third_method(self):
        print("C method")

c = C()
c.method()
c.another_method()
c.third_method()

class SpecialString:
    def __init__(self, cont):
        self.cont = cont
    def __gt__(self, other):
        for index in range(len(other.cont)+1):

            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs


# __lt___ "<"
# __le__ "<="-1
# __eq__ "=="
# __ne__ "!="
# __gt__ ">"
# __ge__ ">="

# __len__ len()
# __getitem__ для индексации
# __setitem__ для присваивания значения индексированному элементу
# __delitem__ для удаления индексированных элементов
# __iter__ для перебора обЪектов (for)
# __contains__для in

# import random
#
# class VagueList:
#     def __init__(self, cont):
#         self.cont = cont
#
#     def __getitem__(self, index):
#         return self.cont[index + random.randint(0, len(-1, 1)]
#     def __len__(self):
#         return random.randint(0, len(self,cont)*2)
#
# vague_list = VagueList(["A", "B", "C", "D", "E"])
# print(len(vague_list))
# print(len(vague_list))
# print(vague_list[2])
# print(vague_list[2])


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x+ other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

class SpecialString:
    def __init__(self,cont):
        self.cont = cont
    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam/hello)

# class SpecialString:
#     def __init__(self, cont):
#         self.cont = cont
#     def __gt__(self, other):
#         for index in range(len(other.cont)+1):
#             result = other.cont[:index] + ">" + self.cont
#             result += ">" + other.cont[index:]
#             print(result)
# spam = SpecialString("spam")
# eggs = SpecialString("eggs")
# spam>eggs

class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __add__(self, other):
        x = self.name + '&' + other.name
        y = self.capacity + other.capacity
        return Juice(x, y)

    def __str__(self):
        return str(self.name) + ' (' + str(self.capacity) + 'L)'


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)


# with open("books.txt","r") as f:
#     lines = f.readlines()
#     for s in lines:
#         s1 = s.strip()
#         print(s1[0], len(s1), sep = '')

# for line in file:
#     if line[-1] == '\n':
#         print(line[0] + str(len(line) - 1))
#     else:
#         print(line[0] + str(len(line)))


import re

# pattern = r"spam"
#
# if re.match(pattern, "spamspamspam"):
#     print("Match")
# else:
#     print("No match")
#
#
# if re.match(pattern, "eggspamsausagespam"):
#     print("Match")
# else:
#     print("No match")
#
# if re.search(pattern, "eggspamsausagespam"):
#     print("Match")
# else:
#     print("Mo match")
# print(re.findall(pattern, "essspamsausagespam"))
#
# match = re.search(pattern, "eggspamsausage")
#
# if match:
#     print(match.group())
#     print(match.start())
#     print(match.end())
#     print(match.span())
#
#
# str = "My name is David. Hi David."
# pattern = r"David"
# newstr = re.sub(pattern, "Amy", str)
# print(newstr)
#
# pattern= r"gr.y"
#
# if re.match(pattern, "grey"):
#     print("Match 1")
# if re.match(pattern, "gray"):
#     print("Match 2")
# if re.match(pattern, "blue"):
#     print("Match 3")
#
#
# pattern = r"^gr.y$"
#
# if re.match(pattern, "grey"):
#     print("Match_1")
# if re.match(pattern, "gray"):
#     print("Match_2")
# if re.match(pattern, "stringray"):
#     print("Match_3")
#
# pattern = r"[A-Z][A-Z][0-9]"
#
# if re.search(pattern, "LS8"):
#     print("Match 1")
# if re.search(pattern, "E3"):
#     print("Match 2")
# if re.search(pattern, "1ab"):
#     print("Match 3")
#
# pattern = r"[^A-Z]"
#
# if re.search(pattern, "this is all quiet"):
#     print("Match 1")
# if re.search(pattern, "AbCdEfG123"):
#     print("Match 2")
# if re.search(pattern, "THISISALLSHOUTING"):
#     print("Match 3")
#
# test = []
# for i in range(2):
#     test.append(100)
#     test.append(3)
# print(test)
#
# for i in range(0, 2):
#     for i in range(0, 4):
#         print(i)

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghjklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())


pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

pattern = r"(a)(b(?:c)(d)(?:e))"
print(len(match.groups()))


# pattern = r"gr(a|e)y"
#
# match = re.match(pattern, "gray")
# if match:
#     print("Жопа")
# match = re.match(pattern, "grey")
# if match:
#     print("Толстая жопа")
# match = re.match(pattern, "griy")
# if match:
#     print("очень Толстая жопа")