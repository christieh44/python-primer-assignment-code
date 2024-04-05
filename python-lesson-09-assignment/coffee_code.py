class KitchenAppliance:
    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand
    def report(self):
        print("\nThis is the " + self.brand + " " + str(self.model_number) + " super Smart Coffee Machine\n")
class SmartCoffeeMachine(KitchenAppliance):
    def __init__(self, model_number, brand, coffee_menu=['latte', 'cappuccino', 'flat white']):
        KitchenAppliance.__init__(self, model_number, brand)
        self.coffee_menu = coffee_menu

    #Updates coffee menu  
    def update_menu(self, new_coffee):

        if new_coffee not in self.coffee_menu:
            self.coffee_menu.append(new_coffee)
            print ("\nThe updated coffee menu is: " + str(self.coffee_menu) + "\n")

        else:
            print(f"\n{new_coffee} is already on the menu")

    #Adds new coffee types until user is finished
        while(new_coffee != "none"):
           
            new_coffee = input("\nWould you like to add another coffee to the menu?\nEnter 'none' if finished: ")

            if new_coffee == "none":
                print("\n\nThe available coffees on the new menu are: " + str(self.coffee_menu) + "\n")
            
            elif new_coffee not in self.coffee_menu:
                self.coffee_menu.append(new_coffee)
                print(f"\nThe updated coffee menu on the {self.brand} machine is: " + str(self.coffee_menu) + "\n")

            else: 
                print(f"\n{new_coffee} is already on the menu\n")

    #Makes coffee from available coffee types          
    def make_coffee(self, coffee_type):
        if(coffee_type not in self.coffee_menu):            
            print(f"\nI'm sorry {coffee_type} is not available. Please choose a coffee from the menu.\n")
            print("\nThe coffees available are: " + str(self.coffee_menu) + "\n")
            coffee_type = input("\nPlease enter the type of coffee would you like me to make: ")
            self.make_coffee(coffee_type)

        else:
            print(f"\n\nMaking a {coffee_type}...\n")
            print("\nEnjoy your coffee!\n")