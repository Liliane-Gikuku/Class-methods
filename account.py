class Account:
    def __init__(Self,name,account_type,number,balance):
        Self.name=name
        Self.account_type=account_type
        Self.number=number
        Self.balance=balance

    def withdraw(Self,amount):
        Self.balance-=amount
        return Self.balance

    def deposit(Self,amount):
        Self.balance+=amount
        return Self.balance
