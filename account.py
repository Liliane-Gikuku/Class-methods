from datetime import datetime
class Account:
    def __init__(self,name,phone_number,account_type,account_number,id):
        self.name=name
        self.phone_number=phone_number
        self.account_type=account_type
        self.account_number=account_number
        self.id=id
        self.balance=0
        self.deposits=[]
        self.new_account=0


        #Add a new attribute to the class Account called deposits which by default is an empty list.
         #Add another attribute to the class Account called withdrawals which by default is an empty list.
        self.deposits=[]
        self.withdrawls=[]
        self.transaction=100
        self.loan_balance=0

        #Modify the withdrawal method to append each successful withdrawal to self.withdrawals

    def withdraw(self,amount):
         self.amount=amount
         date=datetime.now()
         if amount<=0:
             return f"Hello customer, you can't withdraw. Withdrawal should be greater than zero"
         elif amount>self.balance:
             return f"Hello customer,your balance is {self.balance}Frw,You can't withdraw {amount}Frw."
         elif amount<self.balance+ self.transaction:
            return f"Hello customer, your balance is {self.balance}Frw. There is no transaction fee to withdraw {amount}Frw."
             
         else:
             self.balance-=amount
             dct={"date":date.strftime("%d/%m/%Y"),"amount":amount,"narration":f'thank you for withdrawing {amount}Frw on {date}'}
             self.withdrawals.append(dct)
             withdrawal_amount=self.balance-self.transaction
         if amount>withdrawal_amount:
              return "Hello customer, your balance is insufficient to withdraw"
         self.balance-=amount+self.transaction
          #to include a transaction fee of 100 per transaction.
         return f"Hello {self.name}, You have withdrawn {self.withdrawls}Frw and your new balance is {self.balance}Frw on {date.strftime('%d/%m/%Y')}). You paid 100 for the transaction."
         
           
          
    def deposit(self,amount):
        date=datetime.now()
        self.amount=amount
        if amount<=0:
            return f"Deposit must be greater than zero(0)"
        else:
         self.balance+=amount
         dct={"date":date.strftime("%d/%m/%Y"),"amount":amount,"narration":f'thank you for depositing {amount}Frw on {date}'}
         self.deposits.append(dct)
        return f"Hello {self.name}, You have deposited {amount}Frw. Your new balance is {self.balance}Frw."
    #Add a new method called deposits_statement which using a for loop prints each deposit in a new line

    def deposits_statement(self):
        for i in self.deposits:
            print(i)
#Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
    def withdrawals_statement(self):
        for i in self.withdrawls:
            print(i)

 #Add a method to show the current balance.
    def current_balance(self):
        return f"Your current balance is {self.balance}Frw."

    def full_statement(self):
        statement=self.deposits+self.withdrawals
        for a in statement:
            print(a["narration"])

    def borrow(self,amount):
        sum=0
        for y in self.deposits:
            sum+=y["amount"]
        if len(self.deposits) <10:
            return f"you are not eligible to borrow. You need to make {10-len(self.deposits)} more deposits to borrow "
        if amount<100:
            return f"you can borrow atleast 100"
        if amount>sum/3:
           return f"Hello customer, you can only borrow upto {sum/3}"
        if self.balance!=0:
           return f"Hello customer, you have {self.balance}Frw on your balance. You can't borrow yet you still have balance on your account."


        if self.loan_balance!=0:
            return f"Hello customer, you have a debt of {self.loan_balance}Frw you have to pay first for you to borrow."
        else:
            interest= 3/100*(amount)
            self.loan_balance+=amount+interest
            return f"Hello customer, you have borrowed {amount}Frw. Your loan is now at {self.loan_balance}Frw."
    
    def loan_repayment(self,amount):
        
         if amount>self.loan_balance:
             self.balance+=amount-self.loan_balance
             self.loan_balance=0
             return f" Hello customer, thank you for paying the loan of {amount-self.loan_balance}Frw your account balance is {self.balance}Frw."      
         else:
             self.loan_balance-=amount
             return f"Thank you"
            
         
    def transfer(self,amount,new_account):
        if amount<=0:
            return "invalid amount"
        if amount>=self.balance:
            return f"Dear customer you have insuficient funds to make a transfer"
        if isinstance(new_account,Account):
            self.balance-=amount
            new_account.balance+=amount
            return f"Dear customer, you have sent {amount}Frw to {new_account} with the name {new_account.name}.your new balance is {self.balance}Frw.Thank you."




