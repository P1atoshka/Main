a, b = sorted([input(), input()])
print({'желтый синий':'зеленый', 'желтый красный':'оранжевый', 'красный синий':'фиолетовый'}.get(f'{a} {b}') or a if a == b else 'ошибка')





