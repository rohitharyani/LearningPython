class Account:
	def __init__(self,owner,balance=0):
		self.owner = owner
		self.balance = balance


	def deposit(self,dep_amt):
		self.balance = self.balance + dep_amt
		print(f"Added {dep_amt} to the balance. \nNew Balance= ${self.balance}")


	def withdrawal(self,wd_amt):
		if self.balance >= wd_amt:
			self.balance = self.balance - wd_amt
			print(f"withdrawal complete. \nNew Balance= ${self.balance}")

		else:
			print(f"Sorry not enought funds. \nCurrent Balance = ${self.balance}")

	def __str__(self):
		return f"Owner: {self.owner} \nBalance: {self.balance}"


account = Account("Rohit", 500)
print(account)
account.deposit(1000)
account.withdrawal(200)