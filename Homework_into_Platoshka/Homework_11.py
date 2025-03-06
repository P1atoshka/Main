x = int(input())
print((x-1)//4 + 1)

numbers = [64, 34, 25, 12, 22, 11, 90]
numbers.sort()
print("Отсортированный массив:", numbers)

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        print(numbers[i])



