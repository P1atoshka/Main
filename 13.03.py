a,b,c,d = int(input()),int(input()),int(input()),int(input())

left = max(a, b)
right = min(c, d)

if left > right:
    print("пустое множество")
elif left == right:
    print(left)  
else:
    print(left, right)  