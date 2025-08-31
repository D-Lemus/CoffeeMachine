
from coffeeMachine import coffee_machine as cm


class coffee_shop:
    def __init__(self):
        self.machine = cm()
        pass

    def show_main_menu(self):
        print("Welcome to Java\n")
        print("What would you like to order?")
        for coffee in cm.coffee_type:         
            print(f"{coffee.value}.  {coffee.name}")
        print("=" * 30)
        print("10 -. Administrate")
        user_option=int(input("ENTER OPTION: ").strip())
        if user_option >= 1 and user_option <= 3:
            how_many=int(input("How many [max is 3]: ").strip())
            cm.make_coffees(user_option,how_many)
            

 
    def _show_analytics(self):
        pass

    def _show_finance(self):
        pass

    def show_admin_menu(self):
        pass

cf = coffee_shop() 

cf.show_main_menu()