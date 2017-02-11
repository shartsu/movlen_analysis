#! ~/anaconda/bin/python
import numpy as np

def itemPickup(filename, max_userno, max_itemno):
		list_line = []
		item_check = [None]*101
		user_check = [None]*101
		with open(filename) as f:
			for str_line in f.read().splitlines():
					userno = int(str_line.split('::')[0])
					itemno = int(str_line.split('::')[1])
					if max_userno+1 > userno and max_itemno+1 > itemno: 
							list_line.append(str_line)
							# to check lost data
							item_check[itemno] = itemno
							user_check[userno] = userno
		print("items:", item_check[1:100])
		print("users:", user_check[1:100])
		return list_line

if __name__ == "__main__":
		list_item = itemPickup("./ratings.dat", 100, 100) #100 user, 100 items

		# writeout list_item to file
		output_file = open("ratings-100.dat", "w")
		for item in list_item:
				output_file.write("%s\n" % item)

