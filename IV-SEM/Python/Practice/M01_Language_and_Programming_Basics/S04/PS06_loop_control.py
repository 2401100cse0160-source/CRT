p1 = "S123"

for i in range(3):
    p2 = input()
    if p1 == p2:
        print("login successful")
        break 
else:
    print("Account locked")