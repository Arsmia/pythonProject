import time
# count = 0
# while True:
#     print(count, "- Hello")
#     count +=1
#     time.sleep(.200)
#     break

# while count < 10:
#     count += 1
#     print(count, "-Hello")
#     time.sleep(.500)
#
# for i in range (0,10):
#     print(i)
#     time.sleep(.500)
#
# arr = [1,50,10,67,40,2,20,60,3]
# for i in arr:
#     multiply_i = i*10
#     print( "multi_ply = ", multiply_i,)

# for i in arr:
#     dev_i = i % 10
#     if dev_i == 0:
#         print("i = ", i, "dev_i = ", dev_i)

# for i in arr:
#     if i == 67:
#         print("i = ",i)
#         break
# time.sleep(.300)
#
# for i in arr:
#     print("i= ",i)
#     if i == 67:
#         continue
#     print("Hello ", i*10)
#     print("============================")

# while True:
#     name = input("Enter your name: ")
#     print("Hello ", name, count)
#     count += 1
#
curr="USD"
curr_rate=3.9
while True:
    usd_input=int(input("Enter USD: "))
    usd_pln = usd_input*curr_rate
    print("You enter: ", usd_input)
    print("Your_PLN:", usd_pln)