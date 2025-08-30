

class CoffeeMachine:
    #Capacity constants
    MAX_BEANS = 200
    MAX_CUPS = 10
    MAX_WATER = 2500
    MAX_MILK = 1000

    #Price constants
    ESPRESSO_PRICE=4
    LATTE_PRICE=7
    CAPUCCINO_PRICE=6

    #Ingredient Cost constants for each Cofee Type
    ESPRESSO_WATER,ESPRESSO_BEANS = 250,16
    LATTE_WATER,LATTE_MILK, LATTE_BEANS = 250,75,20
    CAPUCCINO_WATER,CAPUCCINO_MILK, CAPUCCINO_BEANS = 200,100,12

    #Cofee Finance
    coffeeBank = 0
    espressoSold = 0
    latteSold = 0
    capuccinoSold = 0


    def __init__(self):
        self.beans = 200
        self.cups = 10
        self.water = 2500
        self.milk = 1000

    def showData(self):
        print(f"COFEE MACHINE HAS:\nBeans: {self.beans} \nCups: {self.cups} \nWater: {self.water} \nMilk: {self.milk}\n=============================\n")


    def makeCofee(self,coffeeType,count):
        #Depending the cofffee type the ifs statement checks if removing the amount needed for each coffee is affordable, if it is then we calculate the difference 
        for i in range(count):
            #ESPRESSO
            if coffeeType ==1:
                if ((self.beans - CoffeeMachine.ESPRESSO_BEANS) >= 0 and (self.cups - 1) >= 0 and (self.water - CoffeeMachine.ESPRESSO_WATER) >= 0):

                    self.beans -= CoffeeMachine.ESPRESSO_BEANS
                    self.cups -= 1
                    self.water -= CoffeeMachine.ESPRESSO_WATER
                    print(f"Espresso #{count} Ready\n=============================\n")

                else: print(f"Espresso #{count} could not be filled because 1 or more ingredients is missing\n=============================\n")

            #LATTE
            elif coffeeType ==2:
                if ((self.beans - CoffeeMachine.LATTE_BEANS) >= 0 and (self.cups - 1) >= 0 and (self.water - CoffeeMachine.LATTE_WATER) >= 0) and (self.milk - CoffeeMachine.LATTE_MILK) >= 0:

                    self.beans -= CoffeeMachine.LATTE_BEANS
                    self.milk -= CoffeeMachine.LATTE_MILK
                    self.cups -= 1
                    self.water -= CoffeeMachine.LATTE_WATER
                    print(f"Latte  #{count} Ready\n=============================\n")

                else: print(f"Latte #{count} could not be filled because 1 or more ingredients is missing\n=============================\n")
            #CAPUCCINO
            elif coffeeType ==3:
                if ((self.beans - CoffeeMachine.CAPUCCINO_BEANS) >= 0 and (self.cups - 1) >= 0 and (self.water - CoffeeMachine.CAPUCCINO_WATER) >= 0) and (self.milk - CoffeeMachine.CAPUCCINO_MILK) >= 0:

                    self.beans -= CoffeeMachine.CAPUCCINO_BEANS
                    self.milk -= CoffeeMachine.CAPUCCINO_MILK
                    self.cups -= 1
                    self.water -= CoffeeMachine.CAPUCCINO_WATER
                
                    print(f"Capuccino  #{count} Ready\n=============================\n")

                else: print(f"Capuccino #{count} could not be filled because 1 or more ingredients is missing\n=============================\n")


    def machineFill(self):
        #Checks if theres stuff to refill and then calculates the amount needed to fill AND avoid it from overflowing
        if (self.beans < CoffeeMachine.MAX_BEANS or self.cups < CoffeeMachine.MAX_CUPS or self.water < CoffeeMachine.MAX_WATER or self.milk < CoffeeMachine.MAX_MILK):
            
            #Lambda to OverKill
            calculate_refill = lambda currentStorage, maxStorage: maxStorage - currentStorage

            beansToAdd= calculate_refill(self.beans,CoffeeMachine.MAX_BEANS)
            cupsToAdd = calculate_refill(self.cups,CoffeeMachine.MAX_CUPS)
            waterToAdd = calculate_refill(self.water,CoffeeMachine.MAX_WATER)
            milkToAdd = calculate_refill(self.milk,CoffeeMachine.MAX_MILK)

            self.beans += beansToAdd 
            self.cups += cupsToAdd
            self.water += waterToAdd
            self.milk += milkToAdd

            print(f"Added Beans: {beansToAdd}\nAdded Cups: {cupsToAdd}\nAdded Water: {waterToAdd}\nAdded Milk: {milkToAdd}\n=============================\n")





            

#MAIN
leave = False
c = CoffeeMachine()
print("Welcome To JavaCofeeStore.")
while leave == False: 

    print(f"What would YOU like?\n\n\t1 - Make ESPRESSO:  {CoffeeMachine.ESPRESSO_PRICE}$\n\t2 - Make LATTE:     {CoffeeMachine.LATTE_PRICE}$\n\t3 - Make CAPUCCINO: {CoffeeMachine.CAPUCCINO_PRICE}$\n")
    print(f"\t4 - SHOW DATA:\n\t5 - REFILL:\n\t6 - TO LEAVE:\n\n=============================")
    opcion =int(input().strip())
    print(opcion.typ)
    if opcion ==1: 
        c.makeCofee(1,1)
    elif opcion ==2: 
        c.makeCofee(2,1)
    elif opcion ==3: 
        c.makeCofee(3,1)
    elif opcion ==4: 
        c.showData()       
    elif opcion ==5: 
        c.machineFill()
    elif opcion ==6: 
        leave == True

        

