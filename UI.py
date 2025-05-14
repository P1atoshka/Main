import tkinter as tk
from tkinter import messagebox
def validate():
    card = entry_card.get().replace(" ", "")
    first = entry_first.get()
    last = entry_last.get()
    if not (card.isdigit() and len(card) == 16 ):
         messagebox.showerror("Ошибка", "Номер карты должен состоять из 16 цифр")
         return
    if not (first.isalpha() and first.isupper()):
         messagebox.showerror("Ошибка", "Имя должно быть заглавными буквами")
         return
    if not (last.isalpha() and last.isupper()):
         messagebox.showerror("Ошибка", "Фамилия должна быть заглавными буквами")
         return

#UI
root = tk.Tk()
root.title("Валидация карты")

tk.Label(root, text = "Номер карты:").pack()
entry_card = tk.Entry(root)
entry_card.pack()

tk.Label(root, text = "ИМЯ (ЗАГЛАВНЫМИ):").pack()
entry_card = tk.Entry(root)
entry_card.pack()

tk.Label(root, text = "Фамилия (ЗАГЛАВНЫМИ):").pack()
entry_card = tk.Entry(root)
entry_card.pack()

tk.Button(root, text = "Проверить", command = validate).pack()

root.mainloop()
#ДЗ
#Настрой Цвета 
#Поменяй расположение кнопок
# Пофикси Ошибку
