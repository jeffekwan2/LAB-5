'''

filename:loanTable.py
date:Nov 16
author: JK
'''
loanAmount = int(input('The loan amount is: '))
annualInterestRate = int(input('The annual interest rate is: '))
monthlyPayment = int(input('The monthly payment is: '))

startingBalance = loanAmount
payment = monthlyPayment
middleBalance = startingBalance - payment
interest = middleBalance * annualInterestRate/12/100
endingBalance = middleBalance + interest
month = 1


print('''
		Starting            Middle              Ending
	Month	Balance   Payment   Balance   Interest  Balance
-------------------------------------------------------''')
while (endingBalance>0):
    print('%-10d%10.2f%10.2f%10.2f%10.2f%10.2f'%
      (month,startingBalance,payment,middleBalance,interest,endingBalance))
    startingBalance = endingBalance
    if endingBalance < payment:
        payment = endingBalance
    middleBalance = startingBalance - payment
    interest = middleBalance * annualInterestRate/12/100
    endingBalance = middleBalance + interest
    month += 1
