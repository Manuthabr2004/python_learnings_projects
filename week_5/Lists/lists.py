
fruits = ["apples" , "mango" , "banana", "guva"]
vegetables = ["onion", "tomato", "bringal", "carrot"]
grocery = [fruits , vegetables]
print(grocery)
grocery[-1][-1] = 'beans'
print(grocery)
fruits.extend(fruits)
print(fruits)
print(grocery)
fruits.pop([1][0])
print(grocery)
grocery.remove(fruits)
print(grocery)
grocery.append(fruits)
print(grocery)
