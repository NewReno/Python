# # Задача 1
# cel_temp = float(input("Введите температуру в градусах Цельсия: "))
# fahrenheit_temp = (cel_temp * 9/5) + 32
# print(f"{cel_temp}°C = {fahrenheit_temp:.1f}°F")

# Задача 2
name = "Иван"
age = 30
is_student = False
print(f"Имя: {name}, Возраст: {age}, Студент: {is_student}")

# задача 3
string_input = input("Введите строку: ")
if len(string_input) > 0:
    print(f"Количество символов: {len(string_input)}")
    print(f"Первый символ: {string_input[0]}")
    print(f"Последний символ: {string_input[-1]}")
else:
    print("Строка пуста.")
print(f"Строка в верхнем регистре: {string_input.upper()}")