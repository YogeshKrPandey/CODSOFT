# Task : Password generator

import random
import string


#length of Password
size = int(input("Enter length of desired password: "))


#getting character set
lower_char=string.ascii_lowercase
upper_char=string.ascii_uppercase
digits=string.digits
symbols=string.punctuation

char_set=lower_char+upper_char+digits+symbols

password=" "

for i in range(size):
    password += random.choice(char_set)

print("Generated Password: ",password)
