print("enter number frist:")
frist = input()
print("enter second number:")
second = input()
print("enter third number:")
third = input()
if frist > second:
    if frist > third:
        print(f"{frist} is the largest")
    else:
        print(f"{third} is the largest ")
else:
     if second > third:
        print(f"{second} the largest")
     else:
        print(f"{third} is the largest ")
