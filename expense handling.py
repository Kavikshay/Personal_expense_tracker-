import json
import shutil
from pathlib import Path 
with open("demo.json","r")as file:
	data=json.load(file)
while True:
	print ("====== EXPENSE TRACKER ======")
	print ("1. Add Expense")
	print ("2. Display All Expenses")
	print("3. Find Expense")
	print ("4. Delete Expense")
	print ("5. Calculate Expenses")
	print ("6. Filter by Category")
	print ("7. Export Expenses to Text File ")
	print ("8. Exit")
	a=int(input("enter your choice:"))
	if a==8:
		print("============================")
		break 
	if a==1:
		id=input("enter expenses id:")
		if id not in data["files"]:
			item=input("enter item name:")
			amount=int(input("enter item amount:"))
			catagory=input("enter item catagory:")
			date=input("enter date:")
			data["files"][id]={"item name":item,"amount":amount,"catagory":catagory,"date":date}
			with open("demo.json","w")as file:
				json.dump(data,file, indent=4)
		else:
			print("is already exists in data")
			
	if a==2:
		with open ("demo.json","r")as file:
			print()
			print(json.dumps(data, indent=4))
			
	if a==4:
		de=input("enter id to delete:")
		if de in data["files"]:
			del data["files"][de]
			with open ("demo.json","w")as file:
				json.dump(data,file, indent=4)
				print("\n data is deleted\n ")
		else:
			print("\n not found enter id again \n")
			
	if a==3:
		find=input("enter expenses id to find:")
		with open("demo.json","r")as file:
			json.load(file)
		if find in data["files"]:
			print("\n id found\n")
			print(find)
			print(json.dumps(data["files"][find], indent=4))
			
		else:
			print("\n not found please enter again\n")
			
	if a==5:
		with open("demo.json","r")as file:
			data=json.load(file)
		total=0
		count=0
		print("1.print total amount ")
		print("2.add or remove amount for id")
		c=int(input("enter choice:"))
		if c==1:
			for i in data["files"].values():
				count+=1
				total+=i["amount"]
			print("the total amount is:",total)
			print("total expenses exists",count)
			print()
			
		if c==2:
			rid=input("enter id to add or remove:")
			
			if rid in data["files"]:
				print("1.to add extra amount ")
				print("2.removr amount")
				edit=int(input(":"))
				
				if edit==1:
					add_amount=int(input("enter amount to add:"))
					data["files"][rid]["amount"]+=add_amount
					
				if edit==2:
					remove=int(input("enter amoyto remove:"))
					if remove<=data["files"][rid]["amount"]:
						data["files"][rid]["amount"]-=remove
					with open("demo.json","w")as file:
						json.dump(data,file)
					
				else:
					print("wrong option")			
			else:
				print("id not found")
				
		else:
			print("wrong choice")

	if a==6:
		cat=input("enter catagory:")
		with open("demo.json","r")as file:
			data=json.load(file)
		found=False
		for i,j in data["files"].items():
			if cat.lower()== j["catagory"].lower():
				found=True
				print("expenses id:",i)
				print("item:",j["item name"])
				print("amount:",j["amount"])
				print("catagory:",j["catagory"])
				print("date :",j["date"])
				print()
			elif found==False:
				print("not found enter again ")
	if a==7:
			with open("demo.json","r")as json_file:
				data=json.load(json_file)
			with open("my expenses.txt","w")as file:
				for i,j in data["files"].items():
					file.write("My experience")
					file.write(f"expenses id: {i}\n")
					file.write(f"item name : {j['item name']}\n")
					file.write(f"amount: {j['amount']}\n")
					file.write(f"category :{j['category']}\n")
					file.write(f"date :{j['date'']}\n")
	else:
		print("wrong choice enter again ")