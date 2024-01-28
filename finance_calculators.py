import math

# User needs to choose either 'investment' or bond
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

option = input("Enter either 'investment' or 'bond' from the menu above to proceed:")
option1 = option.lower() 
investment ="investment"
bond ="bond"

if option1 == investment :  # if investment was chosen
    
    deposit = float(input("How much would you like to deposit? :"))
    interest_rate = float(input("What is the interst rate (%pa)? :"))
    time = float(input("For how many years do you want to invest? :"))
    interest0 = input("Is it compound or simple interest?")
    interest = interest0.lower()
    compound = "compound"
    simple = "simple"
    
    if interest == simple:
        total = deposit * (1 + (interest_rate/100*2))
        print(f'You will have £{total:.2f} after {time}, years')

    elif interest == compound:
            total = deposit*(1+interest_rate/100)**time # round to 2dp
            print(f'You will have £{total:.2f}')

    else: print("Did not recognise your answer")

elif option1 == bond: # if bond was chosen
    
    value = float(input("What is the value of your house?: "))
    interest_rate = float(input("What is your annual interest rate?: "))
    interest = (1+(interest_rate/100)/12)
    time = int(input("How many months do you want the payments?: "))
    repayment = (interest_rate/100/12*value)/(1-(interest)**-time)
    

    print(f'You will have to pay £{repayment:.2f} each month')



