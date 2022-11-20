list = ["Mia", "Sister"]
list.insert(1, "is ")
list.insert(2, "my ")
print(list)
print(list.index("my "))

i = 1
while i < 5:
    print(i, end=' ')
    i += 1
    if i == 3:
        print("Три отсутствует в цикле")
        continue
