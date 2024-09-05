# if 
x = 30
y = 50

if x == y:
    print("equal")
elif x > y:
    print(f"{x} is greater than {y}")
else:
    print(x, "is less than", y)

z = 70
if x < y and x < z:
    print(x, "is less than", y, "and", z)

if x < y or x < z:
    print(x, "is less than", y, "or", z)

# for
list1 = ["apples", "oranges", "bananas"]
for i in list1:
    print(i)

for count, ele in enumerate(list1):
    print(ele, "is the", count, "element in the list")

for i in range(0,4):
    print(i)

# while
i = 0
while i <= 7:
    print(i)
    i+=1

# functions
def name(first_name, last_name):
    print("Hi, my name is", first_name, last_name)
name("Sophie", "Eng")

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def kids(child3, child2, child1):
  print("The youngest child is " + child3)
kids(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def country(country = "Norway"):
  print("I am from " + country)
country("Sweden")
country()