a,b = int(input()),int(input())
s = input()
if s == '+':
    print(a+b)
elif s == '-':
    print(a-b)
elif s == '*':
    print(a*b)
elif s == '/':
    if b != 0:
        print(a/b)
    else:
        print("На ноль делить нельзя")
else:
    print("неверная операция")



















