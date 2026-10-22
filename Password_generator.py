import random 

def random_password():

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special = "!@#$%&*"

    password = ""

    password = password + random.choice(uppercase)
    password = password + random.choice(lowercase)
    password = password + random.choice(special)
    password = password + random.choice(numbers)

    characters = uppercase+lowercase+special+numbers


    for i in range(12):
        password = password + random.choice(characters) 
    return password
    
password = random_password()
print("Random password : ", password)