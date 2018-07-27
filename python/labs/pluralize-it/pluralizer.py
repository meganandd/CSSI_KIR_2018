num = int(raw_input("Enter a number: "));
word = str(raw_input("Enter a word: "));

if (word == "catch" or word == "beach" or word == "snatch" or word == "reach"):
    print ("Output: " + str(num) + " " + word + "es")
elif (word[-3:] == "ife"):
    print ("Output: " + str(num) + " " + word[:-3] + "ives")
elif (word[-2:] == "ch" or word[-2:] == "sh"):
    print ("Output: " + str(num) + " " + word + "es")
elif (word[-2:] == "us"):
    print ("Output: " + str(num) + " " + word[:-2] + "i")
elif (word[-2:] == "ay" or word[-2:] == "oy" or word[-2:] == "ey" or word[-2:] == "uy"):
    print ("Output: " + str(num) + " " + word + "s")
elif (word[-1:] == "y"):
    print ("Output: " + str(num) + " " + word[:-1] + "ies")
elif (num > 1 or num == 0):
    print ("Output: " + str(num) + " " + word + "s")
else:
    print ("Output: " + str(num) + " " + word)
