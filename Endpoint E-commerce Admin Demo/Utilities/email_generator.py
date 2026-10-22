import random

def emailgenerator():
    letters = "abcdefghijklmnopqrstuvwxyz" 
    username = ""

    for i in range(9):
        username = username + random.choice(letters)
        
    number = random.randint(100,999)
    return username + str(number) + "@gmail.com"
    