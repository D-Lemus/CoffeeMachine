from enum import Enum

class CoffeeType(Enum):
    ESPRESSO_SMALL= 1
    ESPRESSO_MEDIUM = 2
    ESPRESSO_LARGE = 3
    LATTE_SMALL = 4
    LATTE_MEDIUM = 5
    LATTE_LARGE = 6
    CAPUCCINO_SMALL = 7
    CAPUCCINO_MEDIUM = 8
    CAPUCCINO_LARGE = 9

COFFEE_INGREDIENTS = {
    # ESPRESSO
    CoffeeType.ESPRESSO_SMALL:  {"water": 30, "beans": 15, "milk": 0, "cups_small": 1,  "price": 4},
    CoffeeType.ESPRESSO_MEDIUM: {"water": 50, "beans": 16, "milk": 0, "cups_small": 1, "price": 5},
    CoffeeType.ESPRESSO_LARGE:  {"water": 70, "beans": 18, "milk": 0, "cups_small": 1,  "price": 6},

    # LATTE
    CoffeeType.LATTE_SMALL:  {"water": 30, "beans": 8,  "milk": 220, "cups_small": 1, "price": 6}, 
    CoffeeType.LATTE_MEDIUM: {"water": 30, "beans": 8,  "milk": 270, "cups_medium": 1, "price": 7},
    CoffeeType.LATTE_LARGE:  {"water": 30, "beans": 8,  "milk": 320, "cups_large": 1, "price": 8},

    # CAPUCCINO 
    CoffeeType.CAPUCCINO_SMALL:  {"water": 30, "beans": 8,  "milk": 180, "cups_small": 1, "price": 6},
    CoffeeType.CAPUCCINO_MEDIUM: {"water": 30, "beans": 8,  "milk": 240, "cups_medium": 1, "price": 7},
    CoffeeType.CAPUCCINO_LARGE:  {"water": 30, "beans": 8,  "milk": 310, "cups_large": 1, "price": 8} 
}


class coffee_machine:
    #Capacity constants
    MAX_BEANS = 200
    MAX_CUPS_SMALL = 10
    MAX_CUPS_MEDIUM = 10
    MAX_CUPS_LARGE = 10
    MAX_WATER = 2500
    MAX_MILK = 1000

    #Cofee Finance
    coffeeBank = 0
    espressoSold = 0
    latteSold = 0
    capuccinoSold = 0


    def __init__(self):
        self.beans = 200
        self.cupsSmall  = 10
        self.cupsMedium  = 10
        self.cupsLarge  = 10
        self.water = 2500
        self.milk  = 1000

    def show_data(self):
        print(f"COFEE MACHINE HAS:\nBeans: {self.beans} \nCups: {self.cups} \nWater: {self.water} \nMilk: {self.milk}\n=============================\n")


    def make_coffee(self,coffeeType,count):
        #Depending the cofffee type the ifs statement checks if removing the amount needed for each coffee is affordable, if it is then we calculate the difference 
        for i in range(count):
            #ESPRESSO
            if coffeeType == 1:
                if ((self.beans - coffee_machine.ESPRESSO_BEANS) >= 0 and (self.cups - 1) >= 0 and (self.water - coffee_machine.ESPRESSO_WATER) >= 0):

                    self.beans -= coffee_machine.ESPRESSO_BEANS
                    self.cups -= 1
                    self.water -= coffee_machine.ESPRESSO_WATER
                    print(f"Espresso #{i+1} Ready\n=============================\n")

                else: print(f"Espresso #{i+1} could not be filled because 1 or more ingredients is missing\n=============================\n")

            #LATTE
            elif coffeeType == 2:
                if ((self.beans - coffee_machine.LATTE_BEANS) >= 0 and (self.cups - 1) >= 0 and (self.water - coffee_machine.LATTE_WATER) >= 0) and (self.milk - coffee_machine.LATTE_MILK) >= 0:

                    self.beans -= coffee_machine.LATTE_BEANS
                    self.milk -= coffee_machine.LATTE_MILK
                    self.cups -= 1
                    self.water -= coffee_machine.LATTE_WATER
                    print(f"Latte  #{i+1} Ready\n=============================\n")

                else: print(f"Latte #{i+1} could not be filled because 1 or more ingredients is missing\n=============================\n")
            #CAPUCCINO
            elif coffeeType == 3:
                if ((self.beans - coffee_machine.CAPUCCINO_BEANS) >= 0 and (self.cups - 1) >= 0 and (self.water - coffee_machine.CAPUCCINO_WATER) >= 0) and (self.milk - coffee_machine.CAPUCCINO_MILK) >= 0:

                    self.beans -= coffee_machine.CAPUCCINO_BEANS
                    self.milk -= coffee_machine.CAPUCCINO_MILK
                    self.cups -= 1
                    self.water -= coffee_machine.CAPUCCINO_WATER
                
                    print(f"Capuccino  #{i+1} Ready\n=============================\n")

                else: print(f"Capuccino #{i+1} could not be filled because 1 or more ingredients is missing\n=============================\n")


    def machine_fill(self):
        #Checks if theres stuff to refill and then calculates the amount needed to fill AND avoid it from overflowing
        if (self.beans < coffee_machine.MAX_BEANS or self.cups < coffee_machine.MAX_CUPS_SMALL or self.water < coffee_machine.MAX_WATER or self.milk < coffee_machine.MAX_MILK or self.cups < coffee_machine.MAX_CUPS_MEDIUM or self.cups < coffee_machine.MAX_CUPS_LARGE):
            
            def calculate_refill(currentStorage, maxStorage):
                return maxStorage - currentStorage

            beansToAdd= calculate_refill(self.beans,coffee_machine.MAX_BEANS)
            cupsToAddSmall = calculate_refill(self.cups,coffee_machine.MAX_CUPS_SMALL)
            cupsToAddMedium = calculate_refill(self.cups,coffee_machine.MAX_CUPS_MEDIUM)
            cupsToAddLarge = calculate_refill(self.cups,coffee_machine.MAX_CUPS_LARGE)
            waterToAdd = calculate_refill(self.water,coffee_machine.MAX_WATER)
            milkToAdd = calculate_refill(self.milk,coffee_machine.MAX_MILK)

            self.beans += beansToAdd 
            self.cupsSmall += cupsToAddSmall
            self.cupsMedium += cupsToAddMedium
            self.cupsLarge += cupsToAddLarge
            self.water += waterToAdd
            self.milk += milkToAdd

            print(f"Added Beans: {beansToAdd}\nAdded Cups:\tSmall:{cupsToAddSmall}\tMedium:{cupsToAddMedium}\tLarge:{cupsToAddLarge}\nAdded Water: {waterToAdd}\nAdded Milk: {milkToAdd}\n=============================\n")
        else: print("\n=============================\nMachine Already Filled\n=============================\n")

def payment_method(self):  
    total = 0 
    while True:
        try:
            donate = int(input("You want to donate a dollar to dog shelter \n\n\t1 - YES\n\t2 - NO, IN OTHER MOMENT\n> ").strip())
            if (donate == 1):
                total += 1
                print(f"Thanks, your new total is ${total}")
                break
            elif (donate == 2):
                print(f"Thanks, your total is ${total}")
                break
            else:
                print("Enter a valid number")
        except ValueError:
            print("Enter a valid number")

while True:
    try:
        total = 0 
        method =int(input("What is yor payment method?\n\n\t1 - CARD\n\t2 - CASH").strip())
        if (method == 1):
            print(f"Thanks, you are to going pay ${total} with card")
            break
        elif (method == 2):
            print(f"Thanks, you are to going pay ${total} with cash")
            break
        else:
            print("Enter a valid number")
    except ValueError:
        print("Enter a valid number")       

#MAIN
leave = False
c = coffee_machine()
print("Welcome To JavaCofeeStore.")

print()

while not leave: 

    print(f"What would YOU like?\n\n\t1 - Make ESPRESSO:  {coffee_machine.ESPRESSO_PRICE}$\n\t2 - Make LATTE:     {coffee_machine.LATTE_PRICE}$\n\t3 - Make CAPUCCINO: {coffee_machine.CAPUCCINO_PRICE}$")
    print(f"\t4 - ADMINISTRATE:\n\t5 - LEAVE")
    opcion =int(input("Choose option: ").strip())


    try:
        if opcion ==1: 
            latteNumber = int(input("How Many?: ").strip())
            c.make_coffee(1,latteNumber)
            input("Press ENTER to continue...")

        elif opcion ==2: 
            espressoNumber = int(input("How Many?: ").strip())
            c.make_coffee(2,espressoNumber)
            input("Press ENTER to continue...")

        elif opcion ==3:
            capuccinoNumber = int(input("How Many?: ").strip()) 
            c.make_coffee(3,capuccinoNumber)
            input("Press ENTER to continue...")

        elif opcion ==4: 

            Password = input("Admin Password: ")

            if (Password == "M3vty7frw2@20"):
                while True:
                    try:
                        print(f"\n=============================\n\t1. - SHOW DATA:\n\t2 - REFILL:\n\t3 - TO LEAVE:\n\n=============================")
                        adminOption = int(input("Choose Option: ").strip())
                        

                        if adminOption == 1:
                            c.show_data()
                            input("Press ENTER to continue...")
                        elif adminOption == 2:
                            c.machine_fill()
                            input("Press ENTER to continue...")
                        elif adminOption == 3:
                            break

                    except ValueError: 
                        print("Please enter a vlid number ")
            else:
                print("Wrong Password. Bye.\n")
                input("Press ENTER to exit...\n")
                
                
        elif opcion ==5: 
            leave = True


    except ValueError:
        print("Please enter a valid number")
        

