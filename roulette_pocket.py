try:
    n = int(input("Введите номер кармана (от 0 до 36): "))
    if not 0 <= n <= 36:
        print("Ошибка: номер кармана должен быть от 0 до 36")
    else:
        print(["Зеленый" if n == 0 else "Красный" if n in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36] else "Черный"][0])
except ValueError:
    print("Ошибка: пожалуйста, введите целое число")

if __name__ == "__main__":
    determine_pocket_color() 