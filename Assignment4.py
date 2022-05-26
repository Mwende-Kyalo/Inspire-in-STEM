#write a program to withdraw ksh. 25,000 if account balance is btn ksh. 100,000 to 200,000
#30% if account balance btn 500,000 and 1M 
#  above 1M deduct ksh. 15,000

acc_bal = input("What is your account balance?")
if (int(acc_bal) > 100000) and (int(acc_bal) < 200000):
    acc_bal = acc_bal - 25000 
    print("We have deducted ksh. 25,000 from your account")
    print(acc_bal)
elif (int(acc_bal) > 500000) and (int(acc_bal) < 1000000) :
    acc_bal = float(acc_bal) - (0.3*float(acc_bal))
    print("We have deducted 30 percent from your account") 
    print(acc_bal)
elif (int(acc_bal) >1000000) :
    acc_bal = acc_bal - 15000
    print("We have deducted ksh. 15,000 from your account")
else:
    print("No deduction done!")