import random as rn
import string as s


def generator(min_length,numbers=True,special_characters=True):
    
    letters=s.ascii_letters
    digits=s.digits
    special=s.punctuation

    characters=letters
    password=""
    char=""
    
    while len(password)<=min_length:

        if numbers and special_characters:
            characters=characters+digits+special
            char=rn.choice(characters)

        elif numbers:
            characters+=digits
            char=rn.choice(characters)

        elif special_characters:
            characters+=special
            char=rn.choice(characters)

        else:
            char=rn.choice(characters)
        
        password+=char
            
    print("your password is:"+ password)

while True:
    x= int(input("what is the length of your password:"))
    y=input("do you want numbers in your password?(yes/no)").lower()=='yes' 
    z=input("do you want special charatcters in your password?(yes/no)").lower()=='yes' 
    print()
    generator(x,y,z)
    print()
    con=input("do you want another password?(y/n)").lower()=='y'
    print()
    if con:
        continue
    else:
        break

print("hope you like your password")




   
