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




    def __init__(self):
        self.beans = 200

        self.cups_small  = 10
        self.cups_medium  = 10
        self.cups_large  = 10

        self.water = 2500
        self.milk  = 1000
        self.ice   = 500

            #Cofee Finance
        self.coffee_bank = 0
        self.espresso_sold = 0
        self.latte_sold = 0
        self.capuccino_sold = 0

        #Payment methods
        self.payment_card = 0
        self.payment_cash = 0

        self.beans_refilled = 0
        self.water_refilled = 0
        self.milk_refilled = 0
        self.ice_refilled = 0
        self.small_cups_refilled = 0
        self.medium_cups_refilled = 0
        self.large_cups_refilled = 0

    def show_data(self):
        print("=" * 30)
        print(f"COFEE MACHINE HAS:\nBeans: {self.beans}")
        print(f"\nSmall Cups: {self.cups_small}")
        print(f"\nMedium Cups: {self.cups_medium}")
        print(f"\nWater: {self.water}")
        print(f"\nMilk: {self.milk}")
        print("\n=" * 30)


    
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
            self.cups_medium -= 1
        if cup_size == "large":
            self.cups_large -= 1


    def _has_enough_ingredients(self, coffee_type,cup_size,temperature):
        """Checks if the machine has enough ingredients before making coffee"""
        has_enough = (
            self.beans >= coffee_type['beans'] and
            self.get_cups_inventory(cup_size) >= 1 and
            self.water >= coffee_type['water'] and
            self.milk  >= coffee_type['milk']
        )
        if temperature != 0:
            has_enough = has_enough and (self.ice >= coffee_type['ice'])

        return has_enough


    def _consume_ingredients(self, coffee_type, temperature):
        coffee_type = self.COFFEE_INGREDIENTS[coffee_type]
        cup_size = coffee_type["cup_size"]
        self.beans -= coffee_type['beans']
        self.water -= coffee_type['water']
        self.milk -= coffee_type['milk']
        self._consume_cup(cup_size)
        if temperature != 0:
            self.ice -= coffee_type['ice']

        self.alert_inventory()

    def _make_one_coffee(self,coffee_type,coffee_number,temperature):
        """Depending the cofffee type the ifs statement checks if removing the amount needed for each coffee is affordable, if it is then we calculate the difference """
        
        recipe = self.COFFEE_INGREDIENTS[coffee_type]
        cup_size = recipe["cup_size"]

        if self._has_enough_ingredients(recipe, cup_size, temperature):
            self._consume_ingredients(coffee_type,temperature)
            self.total_order = recipe["price"]
            print(f"\n{coffee_type.name} #{coffee_number} is ready")
            return True
        else:       
            print(f"\n{coffee_type.name} #{coffee_number} could not be made due to 1 or more ingredients missing")
            return False


    def make_coffees(self,coffee_type,how_many,temperature):
        """Makes multiple coffees with a limit of 3 coffees per machine"""
        success =0
        if how_many <= 3:
            for i in range(how_many):
                if (self._make_one_coffee(coffee_type,i+1,temperature) == True):
                    success += 1
                else:
                    break
        if success > 0:
            if coffee_type.name.startswith("ESPRESSO"):
                self.espresso_sold += success
            elif coffee_type.name.startswith("LATTE"):
                self.latte_sold += success
            elif coffee_type.name.startswith("CAPUCCINO"):
                self.capuccino_sold += success

        return success

    def alert_inventory(self):
        """Alerts if any ingredient is low"""
        low_ingredients = []
        if self.beans < coffee_machine.MAX_BEANS * 0.25:
            low_ingredients.append("beans")
        if self.cups_small < coffee_machine.MAX_CUPS_SMALL * 0.25:
            low_ingredients.append("small cups")
        if self.cups_medium < coffee_machine.MAX_CUPS_MEDIUM * 0.25:
            low_ingredients.append("medium cups")
        if self.cups_large < coffee_machine.MAX_CUPS_LARGE * 0.25:
            low_ingredients.append("large cups")
        if self.water < coffee_machine.MAX_WATER * 0.25:
            low_ingredients.append("water")
        if self.milk < coffee_machine.MAX_MILK * 0.25:
            low_ingredients.append("milk")
        if self.ice < coffee_machine.MAX_ICE * 0.25:
            low_ingredients.append("ice")

        if low_ingredients:
           print(f"\n===Warning: Low inventory for the following ingredients===")
           for i in low_ingredients:
               print(f"- {i}")

    def machine_fill(self):
        #Checks if theres stuff to refill and then calculates the amount needed to fill AND avoid it from overflowing
        if (self.beans < coffee_machine.MAX_BEANS or self.cups_small < coffee_machine.MAX_CUPS_SMALL or self.water < coffee_machine.MAX_WATER or self.milk < coffee_machine.MAX_MILK or self.cups_medium < coffee_machine.MAX_CUPS_MEDIUM or self.cups_large < coffee_machine.MAX_CUPS_LARGE):
            
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

            self.beans_refilled += beans_to_add
            self.water_refilled += water_to_add
            self.milk_refilled += milk_to_add
            self.ice_refilled += ice_to_add
            self.small_cups_refilled += cups_to_add_small
            self.medium_cups_refilled += cups_to_add_medium
            self.large_cups_refilled += cups_to_add_large

            print("\n=" * 30)
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

        
    def payment_method(self,total_order):  
        print(f"\nYour total is: ${total_order}")

        input("\nPress Enter to continue with the payment...")

        while True:
            try:
                donate = int(input("\nYou want to donate a dollar to dog shelter?\n1 - YES\n2 - NO, IN OTHER MOMENT\n> ").strip())
                if (donate == 1):

                    print(f"\nThank you! With your donation included, the total is ${total_order + 1}.")
                    break
                elif (donate == 2):
                    break
                else:
                    print("\nEnter a valid number")
            except ValueError:
                print("\nEnter a valid number")


        while True:
            try:
                total = 0 
                method =int(input("\nWhat is yor payment method?\n1 - CARD\n2 - CASH\n> ").strip())
                if (method == 1):
                    self.payment_card += 1

                    print(f"\nYou are to going pay ${total_order} with card. Thanks for your purchase! :)")
                    self.coffee_bank += total_order
                    break
                elif (method == 2):
                    self.payment_cash += 1

                    print(f"\nYou are to going pay ${total_order} with cash. Thanks for your purchase! :)")
                    self.coffee_bank += total_order
                    break
                else:
                    print("\nEnter a valid number")
            except ValueError:
                print("\nEnter a valid number")  