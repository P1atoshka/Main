full_name = input() #ALAN ASS
parts = full_name.split()
if len(parts) == 2 and parts[0].istitle() and parts[1].istitle():
    print("YES")
else:
    print("NO")