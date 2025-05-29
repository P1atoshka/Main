text = input()
count = sum(1 for char in text if char.islower())
print(count)
