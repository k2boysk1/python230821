# DemoDict.py

colors = {"apple":"red", "banana":"yellow"}
print(len(colors))
colors["kiwi"] = "green"

# 검색
print(colors["apple"])


for item in colors.items():
    print(item)



phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print("kim" in phone)
print("kang" not in phone)
p = phone
print(p)
print(phone)
print(id(phone), id(p))
print(phone["kim"])

import copy
device = {"아이폰":5, "아이패츠":10}

device2 = copy.deepcopy(device)
#device2 - device


device2["맥북"] = 20
print(device)
print(device2)