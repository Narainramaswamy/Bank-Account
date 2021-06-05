# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 07:20:31 2020

@author: S.Narain Ramaswamy
"""

class BankAccount:
    def __init__(self,accno,name,balance):
        self.accno = accno
        self.name = name
        self.balance = balance
    def deposit(self):
        amount1 = int(input("Enter the amount to be deposited: ")) 
        self.balance = self.balance + amount1
        
    def withdrawal(self):
        amount2 = int(input("Enter the amount to be withdrawn: "))
        if amount2 < self.balance:
            self.balance = self.balance - amount2
        else:
            print("Insufficient Balance!!!!")
        
    def bankFees(self):
        fees = self.balance * 0.05
        self.balance = self.balance - fees
        print("The fees amount is: ",fees)
      
    def display(self):
        print("The total amount left in the account is: ",self.balance)
b = BankAccount(188463557, "Narain", 50000)
yes = 1
while(yes):
    choice = int(input("Which one would you like to have a look at 1.deposit  2. withdrawal  3. bankFees "))
    
    if choice == 1:
        b.deposit()
        b.display()
    elif choice == 2:
        b.withdrawal()
        b.display()
    elif choice == 3:
        b.bankFees()
        b.display()
    else:
        print("Invalid Input!!!")
    yes = int(input("Do you want to continue 0. No  1. yes "))
        
        


        