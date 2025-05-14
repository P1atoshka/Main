def is_valid_card_number(card_number):
    card_number = card_number.replace(" ", "")
    return card_number.isdigit() and len(card_number) == 16
def is_all_uppercase(name):
    
    return name.isupper() and name.isalpha()   

def main():
    card_number = input("Введите номер карты (16 цифр): ").strip()
    first_name = input("Введите имя владельца карты: ").strip()
    last_name = input("Введите фамилию владельца карты: ").strip()
    if is_valid_card_number(card_number):
        print("Номер карты введен правильно.")
    else:
        print("Ошибка: номер карты должен состоять из 12 цифр.")

    if is_all_uppercase(first_name):
        print("Имя введено правильно (все буквы заглавные).")
    else:
        print("Ошибка: имя должно содержать только заглавные буквы.")

    if is_all_uppercase(last_name):
        print("Фамилия введена правильно (все буквы заглавные).")
    else:
        print("Ошибка: фамилия должна содержать только заглавные буквы.")

if __name__ == "__main__":
    main()
