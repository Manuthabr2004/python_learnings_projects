list = [1,2,3,4,5,6,7,8,9,10,100,200,13,28,50,187,50,40,654,98]
#to find maximum in list using max() and without max()
print(max(list))
x = list[0]
for item in list:
    print(item)
    if item > x:
        x = item
print(f"max letter is {x}")
#to find sum of items in list total sum
sum = 0
for item in list:
    sum = sum + item
print(sum)
print(len(str(sum)))