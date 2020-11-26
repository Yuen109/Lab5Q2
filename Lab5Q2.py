loanAmout = int(input("The loan amount is :"))
annualInterestRate = int(input("The annual interest rate is :"))
monthlyPayment = int(input("THe monthly payment is :"))

startingBlance = loanAmout
payment = monthlyPayment
middleBlance = startingBlance - payment
interest = middleBlance * annualInterestRate/12/100
endingBlance = middleBlance + interest

print('''
            Starting            Middle              Ending
	Month	Balance   Payment   Balance   Interest  Balance
	-------------------------------------------------------
    ''')

for i in range(1,5):
    print("%8d%10.2f%10.2f%10.2f%10.2f%10.2f"%(i,startingBlance,payment,middleBlance,interest,endingBlance))
    
startingBlance = endingBlance
if startingBlance > payment:
    payment = monthlyPayment
else:
    payment = endingBlance
middleBlance = startingBlance - payment
interest = middleBlance * annualInterestRate/12/100
endingBlance = middleBlance + interest
 