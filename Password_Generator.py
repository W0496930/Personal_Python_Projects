#This is a simple random password generator, it uses a random variable generator
#To create a password out of the "chars" variable which has all the included characters it is able to use.
import random

print("Your password is: ")

chars = "abcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()?"

password = ""
for x in range(16):
    password += random.choice(chars)

print(password)
