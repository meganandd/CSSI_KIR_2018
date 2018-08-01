money = 100

#Used in the view inventory function. Can view items here.
inv = {
"Apple" : 5,
"Wheat" : 5
}

heartsoup = {
"Radish" : 1,
"Hydromelon" : 1,
"Voltfruit" : 1,
"Fresh Milk" : 1
}

applepie = {
"Apple" : 2,
"Tabantha" : 1,
"Wheat" : 1,
"Cane Sugar" : 2,
"Goat Butter" : 2
}

monstercake = {
"Monster Extract" : 2,
"Tabantha" : 2,
"Wheat" : 5,
"Cane Sugar" : 3,
"Goat Butter" : 1
}

meatandricebowl = {
"Raw Meat" : 4,
"Hylian Rice" : 3,
"Rock Salt" : 3
}

fruitandmushmix = {
"Apple" : 3,
"Hylian Shroom" : 3
}

enduringmilk = {
"Enduring Carrot" : 3,
"Fresh Milk" : 2
}

spicypepperseafood = {
"Hyrule Bass" : 2,
"Spicy Pepper" : 2
}

veggiericeballs = {
"Hylian Rice" : 3,
"Swift Violet" : 4
}

heartyclamchowder = {
"Fresh Milk" : 1,
"Tabantha" : 1,
"Wheat" : 3,
"Goat Butter" : 2
}

butteredapple = {
"Apple" : 2,
"Fortified Pumpkin" : 1,
"Goat Butter" : 2
}

#Used in the view recipe function. User will know what ingredients they need to make a certain dish.
recipes = {
    "Creamy Heart Soup" : heartsoup,
    "Apple Pie" : applepie,
    "Monster Cake" : monstercake,
    "Meat and Rice Bowl" : meatandricebowl,
    "Fruit and Mushroom Mix" : fruitandmushmix,
    "Enduring Milk" : enduringmilk,
    "Spicy Pepper Seafood" : spicypepperseafood,
    "Hasty Veggie Rice Balls" : veggiericeballs,
    "Hearty Clam Chowder" : heartyclamchowder,
    "Tough Hot Buttered Apple" : butteredapple,
}

recipebook = {
    "Creamy Heart Soup" : {"Radish" : 1, "Hydromelon" : 1, "Voltfruit" : 1,"Fresh Milk" : 1},
    "Apple Pie" : {"Apple" : 2,"Tabantha" : 1,"Wheat" : 1,"Cane Sugar" : 2,"Goat Butter" : 2},
    "Monster Cake" : {"Monster Extract" : 2,"Tabantha" : 2,"Wheat" : 5,"Cane Sugar" : 3,"Goat Butter" : 1},
    "Meat and Rice Bowl" : {"Raw Meat" : 4,"Hylian Rice" : 3,"Rock Salt" : 3},
    "Fruit and Mushroom Mix" : {"Apple" : 3,"Hylian Shroom" : 3},
    "Enduring Milk" : {"Enduring Carrot" : 3,"Fresh Milk" : 2},
    "Spicy Pepper Seafood" : {"Hyrule Bass" : 2,"Spicy Pepper" : 2},
    "Hasty Veggie Rice Balls" : {"Hylian Rice" : 3,"Swift Violet" : 4},
    "Hearty Clam Chowder" : {"Fresh Milk" : 1,"Tabantha" : 1,"Wheat" : 3,"Goat Butter" : 2},
    "Tough Hot Buttered Apple" : {"Apple" : 2,"Fortified Pumpkin" : 1,"Goat Butter" : 2},
}


#Used in the store function. Player can buy these ingredients to make dishes from the recipe book.
price_ingredients = {
"Radish" : 3,
"Hydromelon" : 4,
"Voltfruit" : 4,
"Fresh Milk" : 3,
"Apple" : 2,
"Tabantha" : 5,
"Wheat" : 1,
"Cane Sugar" : 2,
"Goat Butter" : 2,
"Monster Extract" : 8,
"Raw Meat" : 6,
"Hylian Rice" : 2,
"Rock Salt" : 3,
"Hylian Shroom" : 4,
"Enduring Carrot" : 5,
"Hyrule Bass" : 5,
"Spicy Pepper" : 3,
"Swift Violet" : 6,
"Fortified Pumpkin" : 5
}

#Used in the selling function. The amount the player will make for selling a complete dish.
sellprice_dishes = {
"Creamy Heart Soup" : 8,
"Apple Pie" : 10,
"Monster Cake" : 20,
"Meat and Rice Bowl" : 10,
"Fruit and Mushroom Mix" : 10,
"Enduring Milk" : 6,
"Spicy Pepper Seafood" : 12,
"Hasty Veggie Rice Balls" : 15,
"Hearty Clam Chower" : 25,
"Tough Hot Buttered Apple" : 30
}

sellprice_ingredients = {
"Radish" : 2,
"Hydromelon" : 3,
"Voltfruit" : 2,
"Fresh Milk" : 2,
"Apple" : 1,
"Tabantha" : 3,
"Wheat" : 1,
"Cane Sugar" : 1,
"Goat Butter" : 1,
"Monster Extract" : 4,
"Raw Meat" : 3,
"Hylian Rice" : 1,
"Rock Salt" : 1,
"Hylian Shroom" : 2,
"Enduring Carrot" : 3,
"Hyrule Bass" : 3,
"Spicy Pepper" : 1,
"Swift Violet" : 3,
"Fortified Pumpkin" : 2,
"Creamy Heart Soup" : 8,
"Apple Pie" : 10,
"Monster Cake" : 20,
"Meat and Rice Bowl" : 10,
"Fruit and Mushroom Mix" : 10,
"Enduring Milk" : 6,
"Spicy Pepper Seafood" : 12,
"Hasty Veggie Rice Balls" : 15,
"Hearty Clam Chower" : 25,
"Tough Hot Buttered Apple" : 30
}

def buy (money):
    print("")
    print("Store:")
    print("-------------")
    for key, val in price_ingredients.items():
        p_str3 = "{:<33}{:<33}".format("Ingredient: " + key, "Price: " + str(val))
        print(p_str3)
        print("-------------")
    purchase = input("What would you like to buy? ")
    if (purchase in price_ingredients) == True:
        amount = input("How much of that would you like to buy? ")
        subtractamount = price_ingredients[purchase] * int(amount)
        money = money - subtractamount
        if (purchase in inv) == True:
            inv[purchase] = inv[purchase] + int(amount)
        else:
            inv[purchase] = int(amount)
    else:
        print("Item requested is not in the store.")
    return money

def sell (money):
    print("")
    print("Inventory:")
    print("-------------")
    for key, val in inv.items():
        p_str4 = "{:<30}{:<30}".format("Item: " + key, "Amount: " + str(val))
        print(p_str4)
        print("-------------")
    sellwhat = input("What would you like to sell? ")
    if (sellwhat in inv) == True:
        amountsold = input("How much of that item would you like to sell? ")
        #addamount = inv[sellwhat] * int(amountsold)
        addamount = sellprice_ingredients[sellwhat] * int(amountsold)
        money = money + int(addamount)
        if (sellwhat in inv) == True:
            inv[sellwhat] = inv[sellwhat] - int(amountsold)
            money = money + int(addamount)
            if int(inv[sellwhat]) == 0:
                del inv[sellwhat]
            #if int(inv[sellwhat]) < 0:
                #del inv[sellwhat]
    else:
        print("The item you're trying to sell does not exist.")
    return money

def make (inv, recipebook):
    for dish in recipes:
        print("-------------")
        print("Dish: " + dish)
        print("-------------")
        ingredients = recipes[dish]
        for key, val in ingredients.items():
            p_str = "{:<30}{:<35}".format("Ingredient: " + key, "Amount: " + str(val))
            print(p_str)
        print("")
    count = 0
    makewhat = input("What dish would you like to make? ")
    if (makewhat in recipebook) == True:
        for ingredient, amount in recipebook[makewhat].items():
            if (ingredient in inv) == True:
                if int(inv[ingredient]) >= int(amount):
                    count = count + 1
                else:
                    print("Sorry you don't have enough ingredients to make " + makewhat)
        if count == len(recipebook[makewhat]):
            for ingredient, amount in recipebook[makewhat].items():
                inv[ingredient] = int(inv[ingredient]) - int(amount)
                if int(inv[ingredient]) == 0:
                    del inv[ingredient]
            if makewhat in inv:
                inv[makewhat] = inv[makewhat] + 1
            else:
                inv[makewhat] = 1



while True:
    mainmenu = input("Type 'v' to view inventory"
    "\nType 'm' to view current balance"
    "\nType 'b' to buy ingredients"
    "\nType 'r' to view the recipe book"
    "\nType 'd' to make a dish"
    "\nType 's' to sell an item"
    "\nType 'q' to quit"
    "\n>>> "
    )

    if mainmenu == "v":
        print("")
        print("Inventory:")
        print("-------------")
        for key, val in inv.items():
            p_str4 = "{:<30}{:<30}".format("Item: " + key, "Amount: " + str(val))
            print(p_str4)
            print("-------------")
        print("")

    elif mainmenu == "b":
        money = buy (money)
        print("")

    elif mainmenu == "r":
        for dish in recipes:
            print("-------------")
            print("Dish: " + dish)
            print("-------------")
            ingredients = recipes[dish]
            for key, val in ingredients.items():
                p_str = "{:<30}{:<30}".format("Ingredient: " + key, "Amount: " + str(val))
                print(p_str)
            print("")

    elif mainmenu == "d":
        make (inv, recipebook)

    elif mainmenu == "m":
        print("Current balance: " + str(money))
        print("")

    elif mainmenu == "s":
        money = sell (money)
        print("")

    elif mainmenu == "q":
        break
