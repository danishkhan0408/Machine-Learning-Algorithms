# -*- coding: utf-8 -*-
#OOP in Python
class bank:
	name = "SBI"
	branch = "ABC branch"
	loc = "Pune"
	br_manager = "Manager Babu"
	def printinfo(this):
		print("Name: {}\nBranch: {}\nLocation: {}\nBranch Manager:{}".format(this.name,this.branch,this.loc,this.br_manager))
	
#create the object
#b1=bank()
#print(b1.name)
#b1.printinfo()

#creating a parent class

class myAccount(bank):
	def __init__(self): #self is same as "this"
		self.myname='danish'
		self.acctype='savings'
		self.accnum=123123
		self.balance=123456
		self.history=[]
				
	def printMyInfo(self):
		print("My account details\nName: {}\nAccount Type: {}\nAccount Number: {}\nBalance: {}".format(self.myname,self.acctype,self.accnum,self.balance))
		
	def printBankInfo(self):
		print("My bank details:\nMy Bank is {}\nBranch {}".format(bank.name,bank.branch))
		
	def withdrawals(self,amount):
		if(amount>self.balance):
			print("Insufficient balance")
		else: 
			print("amount before withdrawal {}".format(self.balance))
			self.balance-=amount
			self.printMyInfo()
			self.history.append('Withdrawal:'+str(amount))
			
	def depsits(self,amount):
		print("amount before deposit {}".format(self.balance))
		self.balance+=amount
		self.printMyInfo()	
		self.history.append('Deposit:'+str(amount))
	
	def printLastNTrans(self,n):
		print(self.history[-n:])

	
obj1=myAccount()

obj1.printMyInfo()		
obj1.printBankInfo()
obj1.printinfo()

obj1.withdrawals(456)
obj1.depsits(200)

obj1.printLastNTrans(50)		
	
		
		
		
		
	