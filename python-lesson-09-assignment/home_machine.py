from coffee_code import SmartCoffeeMachine

#Create SmartCoffeeMachine object

home_machine = SmartCoffeeMachine(5000, "Samsung")

home_machine.report()


print("\n--- UPDATE THE COFFEE MENU ---\n")

new_coffee = input("\nPlease enter the new coffee you would like to add to the menu: ")

home_machine.update_menu(new_coffee)


print("\n--- MAKE A COFFEE ---\n")

coffee_type = input("\nPlease enter the type of coffee would you like me to make: ")

home_machine.make_coffee(coffee_type)


