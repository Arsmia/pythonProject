import json
dict_item = {}

dict_item = {
    1: "Sviatlana",
    2: ["Anton", "Julia", "Vladik"],
    3: "Mia",
    4: {"name": "Arseni"}
}

# print(4, "=", dict_item[4]["name"])
# x = dict_item.get(4).get("name")
# print(x, len(x))
#
#
# dict_item["city"] = "Warsaw"
# print(dict_item)
#
# dict_item[1] = "Sviatlanka"
# print(dict_item, len(dict_item))
#
# del dict_item[2]
# print(dict_item, len(dict_item))
#
# dict_item.pop("city")
# print(dict_item, len(dict_item))

# print("dict_item", dict_item)
#
#
# dict_2 = dict_item
# print("dict_2", dict_2)
#
# dict_2["city"] = "Gdansk"
#
# dict_3 = dict_item
# print("dict_3", dict_3)
#
# dict_4 = dict_item.copy()
# print("dict_4 ", dict_4)

# for key, value in dict_item.items():
#     print("key", key, "value", value)
#
# for key in dict_item:
#     print("item", dict_item[key])
#
# names = ("Sviatlana", "Anton", "Arseni", "Mia")
# salary = 5000
# a = dict.fromkeys(names, salary)
# print(a)

path = "C:/Users/Светлана/PycharmProjects/pythonProject/"
file_title = "python_json_lesson.json"

full_name = path + file_title

# with open(full_name, "w") as jf:
#     json.dump(dict_item, jf)

with open(full_name, "r") as jf:
    json_data = jf.read()
    json_object = json.loads(json_data)

    print("json_data:", json_data, type(json_data))
    print("json_object:", json_object, type(json_object))
    print(json_object["2"])