num1 = float(input("Число 1: "))
num2 = float(input("Число 2: "))
operation = input('''
Выберите операцию:
+ сложение
- вычитание
* умножение
/ деление
''')

if operation == '+':
    print("Результат", num1 + num2)
elif operation == '-':
    print("Результат", num1 - num2)
elif operation == '*':
    print("Результат", num1 * num2)
elif operation == '/':
    if num2 == 0:
        print("Деление на ноль запрещено")
    else:
        print("Результат", num1 / num2)
else:
    print('Выбрана неизвестная операция')