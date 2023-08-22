

value = 5
while value > 0:
    print(value)
    value -=1


lst = [100,200,300]
fruit = {"apple":10, "banana":20, "kiwi":30}
for item in fruit.items():
    print(item)



#print("------breake-----")
lst = list(range(1,11))
print(lst)
for i in lst:
    if i > 5:
        break
        print("item:{0}".format(i))

#print("--------cintinu---")
lst = list(range(1,11))
print(lst)
for i in lst:
    if i % 2 == 0:
        continue



print("----range함수----")
print(list(range(10)))
print(list(range(2000,2024)))
print(list(range(1,32)))
for i in range(5):
    print(i)



print("---- 리스트 내장 ---")
lst = list(range(1,11))
print([i**2 for i in lst if i >5])
tp = ("aplle", "kiwi", "orange")
print([len(i) for i in tp])
fruit = {100:"apple", 200:"kiwi"}
print([v.upper() for v in fruit.values()])