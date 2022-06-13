class Atm:
    def __init__(self,cardno,pin):
        self.cardno = cardno
        self.pin = pin

    def check_balance(self):
        print("Your balance is 100000")

    def withdrawl(self,amount):
        if amount <= 100000:
            print("Money insufficient")
            
        else:
            new_amount = 100000 - amount
            print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))

            
        

def main():
    Card_number = input("insert your card number - ")
    pin_number  = input("enter your pin number - ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number  - "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amoun :- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()
