import sys
from  ATMMenu import menu
from ATMExcept import DepositError,InsuffFundError,WithdrawError
from ATMOperations import deposit,withdraw,balenq
while(True):
    try:
        menu()
        ch=int(input("Enter ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("Don't try to deposit alnums,strs and symbols-Invalid Trans")
                except DepositError:
                    print("Don't enter -Ve/Zero Deposits:")
            case 2:
                try:
                    withdraw()
                except WithdrawError:
                    print("Ur Account have Insufficient Funds--Read Pyhton Notes:")
            case 3:
                balenq()
            case 4:
                print("Thx for using program")
                sys.exit()
            case _:
                print("Ur Selection of Operation is wrong and try again")
    except ValueError:
        print("Don't enter strs,alnums and symbols for choice:")
