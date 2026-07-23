import random
#create a list of numbers , characters , letters
numbers = ['1', 2, 3, 4, 5, 6, 7, 8, 9, 0]
letters = ['a', 'b,','c','D','E','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
special_characters = ['!','@','#','$','%','$','^','&','*','(',')','+','=']
list_number = str(numbers)
print(list_number)
#take  a input of how many words need from this 3 categoris for password
a = int(input("Enter a how many  number:"))
b = int(input("Enter how many letters:"))
c = int(input("Enter how many  characters:"))
num_choice = random.choices(list_number, k=a) #select a random integers from list
letter_choice = random.choices(letters, k=b)#select random strings
special_choice = random.choices(special_characters, k=c)#select random characters

print(num_choice)
print(letter_choice)
print(special_choice)

conv_num = ""
for num in num_choice:
    conv_num += num
print(conv_num)
for letter in letter_choice:
     conv_num += letter
print(conv_num)





