#Savings calculator

#Creates variable where user enters the starting amount of money
money_start = input("Enter initial amount of money ($): ")

#Creates variable where user enters the number of years they want to save
savings_years = input("Enter number of years to save: ")

#Creates variable where user enters interest rate
interest_rate = input("Enter annual interest rate (%): ")


#Formula to convert inputs into numbers and calculate interest earned
money_result = float(money_start) * float(interest_rate)/100 * float(savings_years)

#Compares money_result to target amount

exceeds_target = money_result > 10000

#prints savings earned (money_result)

print(f"Amount of savings earned: ${money_result:.2f}")

#Prints True if savings earned is more than 10000

print(f"Greater than $10000: {exceeds_target}")