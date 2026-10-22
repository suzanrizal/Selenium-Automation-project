import random

lenght = int(input("Enter OTP length: "))

otp = ""
for i in range(lenght):
    otp += str(random.randint(0,9))

print("Generated OTP: ", otp)

import random

length = int(input("Enter OTP length: "))

otp = ""

for i in range(length):
    otp += str(random.randint(0, 9))

print("Generated OTP:", otp)








        



