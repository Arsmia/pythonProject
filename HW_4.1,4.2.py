# # # Task № 1
# # def convert_currency(real_to_USD):
# while True:
#
#     amount = input("enter BYN ")
#     conversion_result = int(amount) / 2.55
#     print(conversion_result)
#     print("Ты ввёл " + amount + " USD" + ", конвертируемая сумма в " + "BYN " + " = " + str(conversion_result))


# Task № 2
def convert_currency(real_from_BYN):
    count = 0
amount = input("Enter BYN ")
currency_usd = 2.55
currency_eur = 2.92
currency_chf = 2.67
currency_gbp = 3.42
currency_cny = 0.38
conversion_result = ([int(amount) / currency_usd], [int(amount) / currency_eur],[int(amount) / currency_chf], [int(amount) / currency_gbp], [int(amount) / currency_cny])
print("conversion_result_usd == ", conversion_result[0])
print("conversion_result_eur == ", conversion_result[1])
print("conversion_result_chf == ", conversion_result[2])
print("conversion_result_gbp == ", conversion_result[3])
print("conversion_result_cny == ", conversion_result[4])
print("Press Enter to exit")
