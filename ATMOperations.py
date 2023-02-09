from ATMExcept import DepositError, InsuffFundError, WithdrawError
bal=500.0
def deposit():
    damt=float(input("Enter ur deposit amount:"))
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Ur Account xxxxxxxxxxxx123 credited with INR:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter ur withdraw amount:"))
    if(wamt<=0):
        raise WithdrawError
    elif((wamt+500)>bal):
        raise InsuffFundError
    else:
        bal=bal-wamt
        print("Ur Account xxxxxxxxxx123 debited with INR:{}".format(wamt))
        print("Now ur Account Bal:{}".format(bal))

def balenq():
    print("Ur Account bal:{}".format(bal))
