from Container_Recycling_Machine import Container_Recycling_Machine
import sys
import os

while True:
	obj1 = Container_Recycling_Machine()
	while True:
		value = 0
		obj1.accept_product()
		value = obj1.select_product()

		if value:
			print("(N)ext customer or (Q)uit ?")
			a = input().lower()
			if a == 'q':
				sys.exit()
			elif a =='n':
				break