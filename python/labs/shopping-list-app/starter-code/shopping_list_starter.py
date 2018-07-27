#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

choice = ""

def addItem():
    what_add = raw_input("What would you like to add? >>> ")
    if what_add in shopping_list:
        print "Oops! That item is already in your shopping list"
        print("")
    else:
        shopping_list.append(what_add)
        print("Item added!")
        print("")

def removeItem():
    what_remove = raw_input("What would you like to remove? >>> ")
    certain = raw_input("Are you sure you would like to remove " + what_remove + "? Type 'y' or 'n'. >>> ")
    if certain == "y":
        if what_remove in shopping_list:
            shopping_list.remove(what_remove)
            print("Item removed!")
            print("")
        else:
            print("Oops! That item is not in the shopping list.")
            print("")
    else:
        print("Item not removed!")

def check():
    check_item = raw_input("What item would you like to check for? >>> ")
    if check_item in shopping_list:
        print("'" + check_item + "'" + " is in the shopping list.")
        print("")
        remove_q = raw_input("Would you like to remove " + "'" + check_item + "'? Type 'y' or 'n'. >>> " )
        if remove_q == "y":
            removeItem()
        elif remove_q == "n":
            print ("Item will not be removed.")
            print("")
    else:
        print("'" + check_item + "'" + " is not in the shopping list.")
        print("")
        add_q = raw_input("Would you like to add " + "'" + check_item + "'? Type 'y' or 'n'. >>> " )
        if add_q == "y":
            addItem()
        elif add_q == "n":
            print ("Item will not be added.")
            print("")


def show():
    for items in shopping_list:
        print(items)
    print("")

print("Welcome to the shopping list app!")

shopping_list = []

while choice.lower() != "e":
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")
    print("")

    choice = raw_input("Enter your choice [a|b|c|d|e]: ")

    # Your code below! Handle the cases when the user chooses a, b, c, d, or e

    if (choice.lower() == 'a'):
        addItem()
    elif (choice.lower() == "b"):
        removeItem()
    elif (choice.lower() == "c"):
        check()
    elif (choice.lower() == "d"):
        show()
