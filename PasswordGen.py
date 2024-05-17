#import needed modules

import string
import random

def password_strength(password):
    #determine password strength
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit= False
    has_special_character = False

    #check password length
    if len(password) >= min_length:
        length_validated = True
    else:
        length_validated = False
    
    #check for varying character types
    for char in password:
        if char in string.ascii_uppercase:
            has_uppercase = True
        elif char in string.ascii_lowercase:
            has_lowercase = True
        elif char in string.digits:
            has_digit = True
        elif char in string.punctuation:
            has_special_character = True
    
    #define strength score
    strengthscore =sum([length_validated, has_uppercase, has_lowercase, has_special_character, has_digit])

    return strengthscore


#prepare string functions 

str1 = string.ascii_lowercase
str2 = string.ascii_uppercase
str3 = string.digits
str4 = string.punctuation

#input desired length 

length = int(input("Enter password length: "))

#make character list 

s = []

s.extend(list(str1))
s.extend(list(str2))
s.extend(list(str3))
s.extend(list(str4))

# put strings together
password = "".join(random.sample(s, length))
print("Generated password: ", password)

strengthscore = password_strength(password)
print("Password Strength:", strengthscore)