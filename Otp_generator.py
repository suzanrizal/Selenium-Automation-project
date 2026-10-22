import random

def OTP_gen():

    n = int(input("Enter the leangth of OTP you want to generate: " ))

    OTP = ""

    for i in range(n):
        OTP += str(random.randint(0,9))
    return OTP

Generated = OTP_gen()
print("Generated OTP", Generated )    
