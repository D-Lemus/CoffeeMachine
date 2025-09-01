
from coffeeMachine import coffee_machine as cm


class coffee_shop:
       

    def __init__(self):
        self.machine = cm()
        
 
    def show_analytics(self):
        #desgloce de analiticas de refil
        print("-" * 30)
        print("            Refills Report            ")
        print("=" * 30)
        print(f"Total Coffe Beans Refilled:\t{self.machine.beans_refilled}")
        print(f"Total Milk Refilled:\t{self.machine.milk_refilled}")
        print(f"Total Water Refilled:\t{self.machine.water_refilled}")
        print(f"Total Ice Refilled:\t{self.machine.ice_refilled}\n")
        print(f"Total Small Cups Refilled:\t{self.machine.small_cups_refilled}")
        print(f"Total Medium Cups Refilled:\t{self.machine.medium_cups_refilled}")
        print(f"Total large Cups Refilled:\t{self.machine.large_cups_refilled}")
        print("=" * 30)
        


    def show_finance(self):
        #desgloce de ventas
        print("-" * 30)
        print("            Sales Report            ")
        print("=" * 30)
        print(f"Expresso Sold:\t{self.machine.espresso_sold}")
        print(f"Latte Sold:\t{self.machine.latte_sold}")
        print(f"Capuccino Sold:\t{self.machine.capuccino_sold}\n")
        print(f"Total Coffee Sold:\t{self.machine.espresso_sold + self.machine.capuccino_sold + self.machine.latte_sold}\n")
        print("-" * 30)
        print(f"Cash payments:\t${self.machine.payment_cash}")
        print(f"Card payments:\t${self.machine.payment_card}\n")
        print(f"Total Sales:\t${self.machine.coffee_bank}")
    

    def show_admin_menu(self):
        print("1.Analytics\n2.Finance\n")
        admin_option=int(input("ENTER OPTION: \n").strip())

        if admin_option == 1: self.show_analytics()
        elif admin_option == 2:self.show_finance()
        else: 
            print("Wrong Option, try again.")
            return False

        
    def _display_menu(self):
        print("Welcome to Java\n")
        print("What would you like to order?")
        for coffee in self.machine.coffee_type:  
            print(f"{coffee.value}. {coffee.name} - ${self.machine.COFFEE_INGREDIENTS[coffee]['price']}")
        

        print("=" * 30)
        print("10 -. Administrate")

    def _get_user_choice(self,user_option):

        #ESPRESSO
        if user_option >= 1 and user_option <= 3:
            how_many=int(input("How many [max is 3]: \n").strip())

            if how_many <= 3:

                coffee_enum = list(self.machine.coffee_type)[user_option-1]
                self.machine.make_coffees(coffee_enum,how_many,1)
                self.machine.payment_method(self.machine.total_order)
        #LATTE
        elif user_option >= 4 and user_option <= 9:
            how_many=int(input("How many [max is 3]: \n").strip())
            if how_many <= 3:
                temperature = int(input("You want Coffee Hot or Cold:\n\t1.HOT\n\t2.COLD\n").strip())


                #converitr opcion a enum
                coffee_enum = list(self.machine.coffee_type)[user_option-1]
                self.machine.make_coffees(coffee_enum,how_many,temperature)
                self.machine.payment_method(self.machine.total_order)

        #CAPUCCINO
        elif user_option == 10:
            psswrd=input("Admin password: ").strip()
            if psswrd == 'M3vty7frw2@20':
                self.show_admin_menu()
            else: 
                print("Wrong Password. Bye.")

        else:
            print("Wrong option. Try Again.")
            return False

    def show_main_menu(self):
        
        self._display_menu()
        user_option=int(input("ENTER OPTION: \n").strip())
        self._get_user_choice(user_option)

        