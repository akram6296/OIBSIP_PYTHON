import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
characters=['@','!','$','#','%','&','*','_','/','^',')','(','~']
print('WELCOME TO PASSWORD GENERATOR!')
print("******************************")
no_of_letters=int(input('Enter how many letters you want in your password:'))
no_of_numbers=int(input('Enter how many numbers you want in your password:'))
no_of_char=int(input('Enter how many characters you want in your password:'))
password_list=[]
for char in range(1,no_of_letters+1):
    char=random.choice(letters)
    password_list+=char
for char in range(1,no_of_numbers+1):
    char=random.choice(numbers)
    password_list+=char
for char in range(1,no_of_char+1):
    char=random.choice(characters)
    password_list+=char

random.shuffle(password_list)
password=''.join(password_list)
print(f"The Password is: {password}")