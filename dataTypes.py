# basic examples of different python data types

# ---------------------------- string ----------------------------
str1 = "Hello world!"
str2 = "My name is Sophie."
str3 = str1 + " " + str2
print(str3)
print(str1, str2)
print(f"{str1} {str2}")

# ---------------------------- int ----------------------------
int1 = 4
int2 = 2

int3 = int1 + int2
print(int1, "plus", int2, "equals", int3)
int4 = int1 - int2
print(int1, "minus", int2, "equals", int4)

int3 = int1 * int2
print(int1, "times", int2, "equals", int3)
int4 = int1 / int2
print(int1, "divided (/)", int2, "equals", int4)
int4 = int1 // int2
print(int1, "divided (//)", int2, "equals", int4)

# ---------------------------- list ----------------------------
list1 = ["apples", "oranges", "bananas"]
print(list1)
print(len(list1))
print(list1[1])

list2 = ["eggplants", "cucumbers", "capsicums"]

    # list of lists
list3 = [list1, list2]
print(list3)

    # iteration
for i in range(len(list3)):
    print(list3[i])

for count, ele in enumerate(list3):
    print(count, ele)

for i in range(len(list3)):
    for j in range(len(list3[i])):
        print(list3[i][j])

    # string to list
list4 = list(str1)
print(list4)
list5 = str1.split()
print(list5)

    # adding and subtracting from lists
list1.append("blueberries")
print(list1)
list1.extend(["raspberries"])
print(list1)
list1.insert(1, "strawberries")
print(list1)

list1.remove("raspberries")
print(list1)
list1.pop(3)

    # modify list
list1[0] = "fuji apples"
print(list1)

list1[1], list1[0] = list1[0], list1[1]
print(list1)

    # copy list
list6 = [x for x in list1]
print(list6)
list7 = ["I love "+x for x in list1]
print(list7)

    # sort
list6.sort()
print(list6)
list6.reverse()
print(list6)

    # slicing
list8 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print("::",list8[::])
print("0:7:",list8[0:7:])
print(":7:",list8[:7:])
print(":-3:",list8[:-3:])
print("::2",list8[::2])
print("-2::",list8[-2::])
print("-5::",list8[-5::])
print("-1:-7:",list8[-1:-7:]) # nonsense
print("-7:-1:",list8[-7:-1:])

# ---------------------------- tuple ----------------------------
tuple1 = (1, 2, 3, 3, 4)
print(tuple1)

# ---------------------------- set ----------------------------
set1 = {1, 2, 3, 4, 3}
print(set1)
set2 = {1, "hi", False}

set1.add(5)
print(set1)
set1.remove(5)
print(set1)

# ---------------------------- dict ----------------------------
dict1 = {
    "fruit":"apple",
    "vegetable":"carrot",
    "protein":"salmon",
    "days":7
}
print(dict1)

dict2 = dict(name = "Sophie", age = 20, city = "Oakland")
print(dict2)

    # get value
print(dict1["fruit"])
print(dict1.get("fruit"))
print(dict1.values())

    # get keys
keys = dict1.keys()
print(keys)

items = dict1.items()
print(items)
# for key, value in items:
#     print(key)
#     print(value)

    # change, add, remove
dict2["city"] = "San Francisco"
print(dict2)

dict2["state"] = "California"
print(dict2)

dict2.pop("state")
print(dict2)