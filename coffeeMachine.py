from enum import Enum

class coffee_machine:

    class coffee_type(Enum):
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
    coffee_type.ESPRESSO_SMALL:  {"water": 30, "beans": 10, "milk": 0, "cup_size": "small",  "price": 4, "ice": 0},
    coffee_type.ESPRESSO_MEDIUM: {"water": 50, "beans": 14, "milk": 0, "cup_size": "small", "price": 5, "ice": 0},
    coffee_type.ESPRESSO_LARGE:  {"water": 70, "beans": 18, "milk": 0, "cup_size": "small",  "price": 6, "ice": 0},

    # LATTE
    coffee_type.LATTE_SMALL:  {"water": 30, "beans": 10, "milk": 200, "cup_size": "small",  "price": 6, "ice": 50}, 
    coffee_type.LATTE_MEDIUM: {"water": 30, "beans": 14, "milk": 250, "cup_size": "medium", "price": 7, "ice": 60},
    coffee_type.LATTE_LARGE:  {"water": 30, "beans": 18, "milk": 270, "cup_size": "large",  "price": 8, "ice": 80},

    # CAPPUCCINO
    coffee_type.CAPUCCINO_SMALL:  {"water": 30, "beans": 10, "milk": 140, "cup_size": "small",  "price": 6, "ice": 50},
    coffee_type.CAPUCCINO_MEDIUM: {"water": 50, "beans": 14, "milk": 180, "cup_size": "medium", "price": 7, "ice": 60},
    coffee_type.CAPUCCINO_LARGE:  {"water": 70, "beans": 18, "milk": 240, "cup_size": "large",  "price": 8, "ice": 80}
    }

    #Capacity constants
    MAX_BEANS = 200
    MAX_CUPS_SMALL = 10
    MAX_CUPS_MEDIUM = 10
    MAX_CUPS_LARGE = 10
    MAX_CUPS = 10
    MAX_WATER = 2500
    MAX_MILK = 1000
    MAX_ICE = 500

    #Cofee Finance
    coffee_bank = 0
    espresso_sold = 0
    latte_sold = 0
    capuccino_sold = 0


    def __init__(self):
        self.beans = 200

        self.cups_small  = 10
        self.cups_medium  = 10
        self.cups_large  = 10

        self.water = 2500
        self.milk  = 1000
        self.ice   = 500

    def show_data(self):
        print(f"COFEE MACHINE HAS:\nBeans: {self.beans} \nCups: {self.cups} \nWater: {self.water} \nMilk: {self.milk}\n=============================\n")
    
    def get_cups_inventory(self,cup_size):
        #Returns inventory based on the size
        cup_inventory = {
            "small" : self.cups_small,
            "medium" : self.cups_medium,
            "large" : self.cups_large

        }
        return cup_inventory.get(cup_size)

    def _consume_cup(self, cup_size):
        """Consumes cup in relation to the inventory"""

        if cup_size == "small":
            self.cups_small -= 1
        if cup_size == "medium":
            self.cups_small -= 1
        if cup_size == "large":
            self.cups_small -= 1


    def _has_enough_ingredients(self, recipe, temperature, cup_size):
        """Checks if the machine has enough ingredients before making coffee"""
        has_enough = (
            self.beans >= recipe['beans'] and
            self.get_cups_inventory(cup_size) >= 1 and
            self.water >= recipe['water'] and
            self.milk  >= recipe['milk']
        )
        if temperature != 0:
            has_enough = has_enough and (self.ice >= recipe['ice'])

        return has_enough


    def _consume_ingredients(self, coffee_type, temperature):
        coffee_type = COFFEE_INGREDIENTS[coffee_type]
        cup_size = coffee_type["cup_size"]
        self.beans -= coffee_type['beans']
        self.water -= coffee_type['water']
        self.beans -= coffee_type['milk']
        self._consume_cup(cup_size)
        if temperature != 0:
            self.ice -= coffee_type['ice']
        
    def _make_one_coffee(self,coffee_type,coffee_number,temperature):
        """Depending the cofffee type the ifs statement checks if removing the amount needed for each coffee is affordable, if it is then we calculate the difference """
        
        if self ._has_enough_ingredients(coffee_type):
            self._consume_ingredients(coffee_type,temperature)
            recipe = COFFEE_INGREDIENTS[coffee_type]
            self.coffee_bank += recipe["price"]
            print(f"{coffee_type.name} #{coffee_number} is ready")
            return True
        else:       
            print(f"{coffee_type.name} #{coffee_number} could not be made due to 1 or more ingredients missing")
            return False


    def make_coffees(self,coffee_type,how_many):
        """Makes multiple coffees with a limit of 3 coffees per machine"""
        success =0
        if how_many <= 3:
            for i in range(how_many):
                if self._make_one_coffee(coffee_type,i+1,temperature) == True:
                    success += 1
                else:
                    break

            if coffee_type.startswith("ESPRESSO"):
                self.espresso_sold += success
            elif coffee_type.startswith("LATTE"):
                self.latte_sold += success
            elif coffee_type.startswith("CAPUCCINO"):
                self.capuccino_sold += success

        return success


    def machine_fill(self):
        #Checks if theres stuff to refill and then calculates the amount needed to fill AND avoid it from overflowing
        if (self.beans < coffee_machine.MAX_BEANS or self.cups < coffee_machine.MAX_CUPS_SMALL or self.water < coffee_machine.MAX_WATER or self.milk < coffee_machine.MAX_MILK or self.cups < coffee_machine.MAX_CUPS_MEDIUM or self.cups < coffee_machine.MAX_CUPS_LARGE):
            
            def calculate_refill(currentStorage, maxStorage):
                return maxStorage - currentStorage


            beans_to_add= calculate_refill(self.beans,coffee_machine.MAX_BEANS)
            cups_to_add_small = calculate_refill(self.cups_small,coffee_machine.MAX_CUPS_SMALL)
            cups_to_add_medium = calculate_refill(self.cups_medium,coffee_machine.MAX_CUPS_MEDIUM)
            cups_to_add_large = calculate_refill(self.cups_large,coffee_machine.MAX_CUPS_LARGE)
            water_to_add = calculate_refill(self.water,coffee_machine.MAX_WATER)
            milk_to_add = calculate_refill(self.milk,coffee_machine.MAX_MILK)
            ice_to_add = calculate_refill(self.ice,coffee_machine.MAX_ICE)

            self.beans += beans_to_add 
            self.cups_small += cups_to_add_small
            self.cups_medium += cups_to_add_medium
            self.cups_large += cups_to_add_large
            self.water += water_to_add
            self.milk += milk_to_add
            self.ice += ice_to_add

            print(f"Added Beans: {beans_to_add}\n")
            print(f"Added Small Cups: {cups_to_add_small}\n")
            print(f"Added Medium Cups: {cups_to_add_medium}\n")
            print(f"Added Large Cups: {cups_to_add_large}\n")
            print(f"Added Water: {water_to_add}\n")
            print(f"Added Milk: {milk_to_add}\n")
            print(f"Added Ice: {ice_to_add}\n")
            print("=" * 12)

        else: 
            print("=" * 12)
            print("Machine Already Filled.")
            print("=" * 12)

        
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
"""
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
        
"""
