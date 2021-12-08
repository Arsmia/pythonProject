# file_path = "C:/Users/Светлана/PycharmProjects/pythonProject/"
# file_name = "lesson.txt"
#
# file_path_name = file_path + file_name
#
# names_list = ["Sviatlana", "Anton", "Arseni", "Mia"]
# with open(file_path_name, "w") as txt_file:
#     for i in names_list:
#
#         txt_file.write(i)
#         txt_file.write("\n")

        # txt_file.write("\n".join(names_list))

# with open(file_path_name, "r") as txt_file:
#     read_f = txt_file.readlines()
#
#     for i in read_f:
#         print(i.rstrip(), type(i))

# with open(file_path_name, "w") as txt_file:
#     name = input("Name ")
#     surname = input("Surname ")
#     full_name = name + surname + "\n"
#
#     txt_file.write(full_name)
#
#
# with open(file_path_name, "w") as txt_file:
#     name = "Sviatlana"
#     surname = "\nStrachuk"
#     full_name = name + surname
#
#     txt_file.write(full_name)
import csv

file_path = "C:/Users/Светлана/Desktop/Courses/Python_HW/"
file_name = "lesson.csv"

csv_file_name = file_path + file_name

users = [
    ["Sviatlana", 35],
    ["Anton", 35],
    ["Arseni", 12],
    ["Mia", 3]
]
# for item in range(0, 100):
#     for ul_item in users:
#         name_age = []
#
#         new_name = ul_item[0] + "_" + str(item)
#         print(new_name)
#
# with open(csv_file_name, "w") as cf:
#     writer = csv.writer(cf)
#
#     writer.writerows(users)

new_users = []
for item in range(0, 100):
    for ul_item in users:
        name_age = []
        new_name = ul_item[0] + "_" + str(item)

        new_age = 10 + item
        name_age.append(new_name)
        name_age.append(new_age)

        new_users.append(name_age)
#         print(users)
#     print(users)
#
# for ii in new_users:
#     print(ii)
with open(csv_file_name, "a") as cf:
    writer = csv.writer(cf)

    writer.writerows(new_users)