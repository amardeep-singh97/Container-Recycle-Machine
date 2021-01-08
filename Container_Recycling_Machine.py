from Container import Container
import sys

class Container_Recycling_Machine:
	def __init__(self):
		self.obj = Container("",0,0,0,0,[])

	def accept_product(self):
		print("\n","Balance: ${:.2f}".format(self.obj.balance),"\n","Please select a product: (Can,Bottle,Box,Newspaper,Stop): ")
		self.obj.option = input("").lower()

	def select_product(self):
		item_list = list()
		if self.obj.option == "stop":
			return self.print_receipt()
		elif self.obj.option in ["can","bottle","box","newspaper"]:
			while True:
				input_val = int(input("How many {0}(s) do you have?: ".format(self.obj.option) ))
				if input_val <=50:
					self.obj.number_of_items = input_val
					break
				else:
					print("Please put less than 50 items","\n")
					continue
			self.obj.total_number += self.obj.number_of_items
			print("Please place {0} {1}(s) into machine.".format(self.obj.number_of_items,self.obj.option))
			for i in range(self.obj.number_of_items):
				print("{0} Accepted".format(self.obj.option))
			if self.obj.option == "can":
				self.obj.money = 0.20*self.obj.number_of_items
				self.obj.balance += self.obj.money
				print("You added {0} {1}(s) for $0.20 each. You have ${2:.2f}.".format(self.obj.number_of_items,self.obj.option,self.obj.money))
				item_list.append(self.obj.number_of_items)
				item_list.append(self.obj.option)
				item_list.append(self.obj.money)
			if self.obj.option == "bottle":
				self.obj.money = 0.50*self.obj.number_of_items
				self.obj.balance += self.obj.money
				print("You added {0} {1}(s) for $0.50 each. You have ${2:.2f}.".format(self.obj.number_of_items,self.obj.option,self.obj.money))
				item_list.append(self.obj.number_of_items)
				item_list.append(self.obj.option)
				item_list.append(self.obj.money)
			if self.obj.option == "newspaper":
				self.obj.money = 0.10*self.obj.number_of_items
				self.obj.balance += self.obj.money
				print("You added {0} {1}(s) for $0.10 each. You have ${2:.2f}.".format(self.obj.number_of_items,self.obj.option,self.obj.money))
				item_list.append(self.obj.number_of_items)
				item_list.append(self.obj.option)
				item_list.append(self.obj.money)
			elif self.obj.option == "box":
				self.obj.money = 1.00*self.obj.number_of_items
				self.obj.balance += self.obj.money
				print("You added {0} {1}(s) for $1.00 each. You have ${2:.2f}.".format(self.obj.number_of_items,self.obj.option,self.obj.money)) 
				item_list.append(self.obj.number_of_items)
				item_list.append(self.obj.option)
				item_list.append(self.obj.money)
			self.obj.item.append(item_list)
			return 0
		else:
			print("Put right item in the machine")

	def print_receipt(self):
		print("\n","-------Final Receipt-------","\n")
		for i in self.obj.item:
			print("{0} {1}(s)             ${2:.2f}".format(i[0],i[1],i[2]))
		print("\n","Number of containers:     {}".format(self.obj.total_number))
		print(" Amount paid:              ${0:.2f}".format(self.obj.balance))
		print("\n","Thank you for recycling at FedUni!","\n")
		return 1