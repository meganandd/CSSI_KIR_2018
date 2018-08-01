# print ("Hello world!");

# JavaScript vvv
# if (condition) {
#     stuff to do
# }
#
# Python vvv
# if condition:
#     stuff to do

# This is a comment in python
# variable_name = "Megan";
# variable_name2 = raw_input("Enter your name: ");
# print (variable_name);
# print (variable_name2);

# number = float(raw_input("Type a number: "));
# #print (number / 5);
# print ("Your result: " + str(number / 5));

# print ("Megan" * 5);
# #multiply a string by a number
#
# first_name = raw_input("Enter your first name: ");
# last_name = raw_input("Enter your last name: ");
# print ("Hello, " + first_name + " " + last_name + ".");
#
# steve = "jobs";
# print (type(steve));
# #True, False
# #steve = []; -- list
# #steve = {}; -- dictionary
#
# steve = int(raw_input("Type a number: "))
# bill = int(raw_input("Type another number: "))
#
# if steve == 0:
#     print ("avocado")
# elif steve == 0 and bill == 5:
#     print ("watermelon")
# elif steve == 1:
#     print ("fruity")
# else:
#     print ("pineapple")

# steve = int(raw_input("Enter a number: "))
#
# for i in range(5, 10, -1):
#     print(i)
#
# i = 0
# while i < steve:
#     print(i)
#     i += 1
#
# for x in "Megan":
#     print(x)
#
# def steve(a, b, c,):
#     # print(a)
#     # print(b)
#     # print(c)
#     return 5
#
# bill = steve(1, 2, 3)
# print(bill) #print 5
#
# steve(1, 2, 3)

# def full_name(first_name, last_name):
#     print("Hello world " + first_name + " " + last_name)

# full_name("Megan", "Andersen")

# instructors = ["adam", 'teddy']
# print(instructors)
# instructors.append("lisa")
# print(instructors)

#.remove("adam")
# del instructors[0]
# for i in instructors:
#   print(i)

#Exercise 0
intArr = [2]
sum = 0
if (len(intArr) < 2):
    print(0)
else:
    for i in range(0, 2):
        sum += intArr[i]
        print(sum)

#Exercise 1
intList = [13, 13, 13, 13, 6]
sum = 0
for i in range(0, len(intList)):
    if (intList[i] == 13):
        sum += 0
    else:
        sum += intList[i]
print sum

#Exercise 2
strList = ["Megan", "dog", "cat", "cat"]

def has_two_cats(strList):
    count = 0
    for str in strList:
        if (str == "cat"):
            count = count + 1
    if (count == 2):
        return True
    else:
        return False

print(has_two_cats(strList))

#Exercise 3
def fill_with_larger(numList):
    #biggestNum = 0
    firstNum = numList[0]
    lastNum = numList[len(numList) - 1]
    if (firstNum > lastNum):
        numList = [firstNum for i in numList]
        print numList
    else:
        numList = [lastNum for i in numList]
        print numList

(fill_with_larger([2, 7]))
