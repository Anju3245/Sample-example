print("enter your first name:")
first_name = input()
print("enter your last name:")
last_name = input()
print(f"his full name is {first_name} {last_name}")
out_file = open("c.txt", 'w')
out_file.write(indata+ "his full name is "+)
out_file.close()
