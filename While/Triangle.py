x,y,z = map(int(input(),input(),input()))
print("Равносторонний"if x==y==z else "Равнобедренный" if x in(y,z) or y == z else "Разносторонний")
