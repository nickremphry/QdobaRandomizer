import random

rice = random.randint(0,3)
beans = random.randint(0,3)
protein = random.randint(0,7)
queso = random.randint(0,3)
salsa = random.randint(0,8)
cheese = random.randint(0,1)
sourCream = random.randint(0,1)
guac = random.randint(0,1)
toppings = random.randint(0,6)

def displayRice():
    if(rice == 0):
        print("Rice: None")
    elif(rice == 1):
        print("Rice: Cilantro Lime Rice")
    elif(rice == 2):
        print("Rice: Seasoned Brown Rice")
    else:
        print("Rice: Both Rices")

def displayBeans():
    if(beans == 0):
        print("Beans: None")
    elif(beans == 1):
        print("Beans: Black Beans")
    elif(beans == 2):
        print("Beans: Pinto Beans")
    else:
        print("Beans: Both Beans")

def displayProtein():
    if(protein == 0):
        print("Protein: None")
    elif(protein == 1):
        print("Protein: Grilled Adobo Chicken")
    elif(protein == 2):
        print("Protein: Pulled Pork")
    elif(protein == 3):
        print("Protein: Ground Beef")
    elif(protein == 4):
        print("Protein: Smoked Brisket")
    elif(protein == 5):
        print("Protein: Grilled Steak")
    elif(protein == 6):
        print("Protein: Cholula Hot and Sweet Chicken")
    else:
        print("Protein: Impossible Plant Based")

def displayQueso():
    if(queso == 0):
        print("Queso: None")
    elif(queso == 1):
        print("Queso: 3-Cheese Queso")
    elif(queso == 2):
        print("Queso: Diablo Queso")
    else:
        print("Queso: No Queso")
    
def displaySalsa():
    if(salsa == 0):
        print("Salsa: None")
    elif(salsa == 1):
        print("Salsa: Pico De Gallo")
    elif(salsa == 2):
        print("Salsa: Corn Salsa")
    elif(salsa == 3):
        print("Salsa: Roasted Tomato Salsa")
    elif(salsa == 4):
        print("Salsa: Salsa Verde")
    elif(salsa == 5):
        print("Salsa: Salsa Roja")
    elif(salsa == 6):
        print("Salsa: Fiery Habanero Salsa")
    elif(salsa == 7):
        print("Salsa: Jalapeno Verde")
    else:
        print("Salsa: Chile Crema")

def displayCheese():
    if(cheese == 0):
        print("Cheese: No")
    else:
        print("Cheese: Yes")

def displaySourCream():
    if(sourCream == 0):
        print("Sour Cream: No")
    else:
        print("Sour Cream: No")

def displayGuac():
    if(guac == 0):
        print("Guac: No")
    else:
        print("Guac: Yes")

def displayToppings():
    if(toppings == 0):
        print("Toppings: None")
    elif(toppings == 1):
        print("Toppings: Lettuce")
    elif(toppings == 2):
        print("Toppings: Tortilla Strips")
    elif(toppings == 3):
        print("Toppings: Cotija Cheese")
    elif(toppings == 4):
        print("Toppings: Cilantro")
    elif(toppings == 5):
        print("Toppings: Pickled Jalapenos")
    else:
        print("Toppings: Pickled Onions")

def randomize():
    displayRice()
    displayBeans()
    displayProtein()
    displayQueso()
    displaySalsa()
    displayCheese()
    displaySourCream()
    displayToppings()

randomize()