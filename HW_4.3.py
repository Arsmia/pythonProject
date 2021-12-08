# Задача №3
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#                 "конвертированная сумма в EUR = int"
#                 "конвертированная сумма в CHF = int"
#                 "конвертированная сумма в GBP = int"
#                 "конвертированная сумма в CNY = int"
#
#     3. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     4. Валюту пользователя определите сами.

def main():
   your_money = get_money()
   your_currency = get_currency(str(your_money))
   print("your_money = ", your_currency)


def get_money():
    while True:
        your_money = input("Enter your money: ")
        if your_money == " ":
            print("Вы ввели пустое поле. Введите число.")
            return your_money, False
        if int(your_money) <= 0:
            print("Введите положительное число.")
            return your_money, False
        try:
            your_money = int(your_money)
        except ValueError:
            print("Вы ввели не число. Введите число.")
        if int(your_money) > 0:
            return your_money, True
        continue

def get_currency(your_money):
    int_money = int(your_money)
    return int_money
currency_list = ["USD","EUR","CHF","GBP","CNY"]
your_money = input("Enter your money: ")
currency_usd = 2.55
currency_eur = 2.92
currency_chf = 2.67
currency_gbp = 3.42
currency_cny = 0.38
conversion_result = ([int(your_money) / currency_usd], [int(your_money) / currency_eur], [int(your_money) / currency_chf], [int(your_money) / currency_gbp], [int(your_money) / currency_cny])
print("conversion_result_usd == ", conversion_result[0])
print("conversion_result_eur == ", conversion_result[1])
print("conversion_result_chf == ", conversion_result[2])
print("conversion_result_gbp == ", conversion_result[3])
print("conversion_result_cny == ", conversion_result[4])

get_currency(your_money)