# Dictionary datatype
# key value pair
# unique key should be present
# example
# key:valuef
fruit_cart = {"apple":160,"banana":40,"Kivy":60,"black-current":100}
print(fruit_cart)
print(type(fruit_cart))

# comprehension
s = {n:n*3 for n in range(1,11)}
print(s)
print(type(s))

# mixed key
d = {1:'carrots','two':[1,2,3]}
print(d)

# list to dictionary
keys = [1,2,3,4,5,6]
values = ["A","B","C","D","E","F"]
z = zip(keys,values)
print(dict(z))

# keys duplication
print({1:"A",2:"B",1:"C",1:"D"})

# empty dictionary
li = []
di = {} #dict
se = set()

# Accessing
print(fruit_cart["apple"]) #you need pass keys

# additional builtin functions

# get()
print(fruit_cart.get("tomato"))

#print(fruit_cart["tomato"])  #you cannot pass key which is not exist
fruit_cart["Apple"]="40"
print(fruit_cart)

dict4={1:1,5:2,3:3}
dict4[5]=4
print(dict4)
fruit_cart1 = {"apple":160,"banana":40,"Kivy":60,"black-current":100}
fruit_cart1["banana"]=90
print(fruit_cart1)

# adding new pair
fruit_cart1["custard"]=250
print(fruit_cart1)
#fruit_cart1.update(apple:200)
#del fruit_cart1
#print(fruit_cart1)

#del fruit_cart1["custard"]
#print(fruit_cart1)

text_data = {1:"text1",2:"text2",3:"text3",4:"text1",5:"text1"}
print(len(text_data))

k = sorted(text_data)
print(type(k))
print(k)

# methods with . operator
print(fruit_cart1.keys())
print(fruit_cart1.values())

# items()

for k,v in fruit_cart1.items():
    print(k,v)
    print(fruit_cart1[k]*2)

print(fruit_cart.get("tomato",0))
print(fruit_cart.clear())

fruit_cart = fruit_cart1.copy() # shallow copy
print(id(fruit_cart))
print(id(fruit_cart1))
fruits = fruit_cart1.pop('kivy',0)
print(fruits)

print(fruit_cart1)
fruit_cart1.update({"apple":1200})
print(fruit_cart1)
