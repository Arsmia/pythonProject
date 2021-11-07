import names, randomtimestamp as rd

from functions_from_functions_1 import a_2


item = 0

# def a_1():
#     print("Hello a_1")
# a_1()


# def a_1 (item_1, item_2):
#     print("Hello a_1")
# a_1(10,20)

def a_1(item_1, item_2):
    result = item_1 + 100
#     print("item_1 = ", item_1)
#     print("result = ", result)
# a_1(30,50)


# def a_2(y_1):
#
#     result = y_1 + 500
#
#
#     print("--------------Hello a_2")
#     print("item_1 = ", y_1)
#     print("result = ", result)


# a_2(5)


# for i in range(0,10):
#
#     a_2(i)
#     print("==============")
#
#     a_1(i, i*2)
#     print("**************")

# def a_2(y_1):
#     result = "Hello, " + y_1
#     print(result)

for i in range(0,10):

    user_name = names.get_full_name()
    gen_date = rd.random_date()
    # print("gen_date = ", gen_date)

    # print("user_name = ", user_name)
    a_2(user_name, gen_date)

