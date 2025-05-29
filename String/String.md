# 🎓 Методы Строк В Python 

## `capitalize()`
👉 Делает первую букву строки заглавной, остальные - строчными.

``` python
text = "hello world"
print(text.capitalize()) # Hello world
```

## `swapcase()`
👉 Меняет регистр каждой буквы на противоположный: маленькие -> большие и наоброт.

``` python
text = "Hello WoRLd"
print(text.swapcase()) # hELLO wOrlD
```
## `title()`
👉 Каждое слово начинается с заглавной буквы.

``` python
text = "hello world as python"
print(text.title()) # Hello World As Python

```
## `lower()/ upper()`
👉 Каждое слово начинается с заглавной буквы.

``` python
text1 = "hello"
text2 = "HELLO"
print(text1.upper()) # HELLO 
print(text2.lower()) # hello
```