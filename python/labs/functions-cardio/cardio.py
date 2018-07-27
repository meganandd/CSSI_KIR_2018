#import type

def longest_word(str1, str2, str3):
    if len(str1) > len(str2) and len(str1) > len(str3):
        return str1
    elif len(str2) > len(str1) and len(str2) > len(str3):
        return str2
    else:
        return str3

#print(longest_word("Megan", "App", "Triangle"))

def reverse_string(str):
    reverse = ""
    index = len(str)
    while index > 0:
        reverse += str[index - 1]
        index = index - 1
    return reverse

#print(reverse_string("Megan"))

def sum_to_n(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum

#print(sum_to_n(10))

def is_triangle(s1, s2, s3):
    if (s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1):
        return False;
    else:
        return True;

#print(is_triangle(30, 1, 1))

def roll_dice(num):
    import random
    sum = 0;
    while num > 0:
        sum += random.randint(1,6)
        num = num - 1
    return sum

#print(roll_dice(3))

#prime = only divisible by itself and by 1

def isPrime(num):
    if (num == 1 or num == 2):
        return True
    else:
        for i in range(2, num):
            if (num % i == 0):
                return False
            else:
                return True

#print(isPrime(3))

def snake_case(camelCaseString):
    split = list(camelCaseString)
    for i in range(len(split)):
        if split[i].isupper():
            split[i] = split[i].lower()
            if i != 0:
                split[i] = "_" + split[i]
    finalstr = ''.join(split)
    print(finalstr)

snake_case("MeganIsSocool")

def get_number_input():
     satisfied = 0;
     while satisfied == 0:
         try:
             user_input = input("Please enter a number. >>> ")
         except NameError:
             user_input = input("Please enter a number. >>> ")
         while satisfied == 0:
            try:
                if type(user_input) == int or float(user_input) == float:
                    print("Thank you for the number!")
                    satisfied = 1
            except NameError:
                user_input = input("Please enter a number. >>> ")

get_number_input()
