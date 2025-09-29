print('Выберете режим работы калькулятора')
print('1. Арифметический')
print('2. Операция сравнения')
print('3. Логический')

var = input('Ввести номер режима работы:')

if var == '1':
    # Арифметический режим
    num1 = float(input("Введите первое число: "))
    operator = input("Введите операцию (+, -, *, /, //, %, **): ")
    num2 = float(input("Введите второе число: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Ошибка: деление на ноль!"
    elif operator == '//':
        if num2 != 0:
            result = num1 // num2
        else:
            result = "Ошибка: деление на ноль!"
    elif operator == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            result = "Ошибка: деление на ноль!"
    elif operator == '**':
        result = num1 ** num2
    else:
        result = "Неизвестная операция"
    
    print("Результат:", result)

elif var == '2':
    # Режим сравнения
    num1 = float(input("Введите первое число: "))
    oper_sr = input("Введите операцию сравнения (==, !=, >, <, >=, <=): ")
    num2 = float(input("Введите второе число: "))
    
    if oper_sr == '==':
        result = 'Равны' if num1 == num2 else 'Не равны'
    elif oper_sr == '!=':
        result = 'Не равны' if num1 != num2 else 'Равны'
    elif oper_sr == '>':
        result = f'{num1} Больше {num2}'
    elif oper_sr == '<':
        result = f'{num1} Меньше {num2}'
    elif oper_sr == '>=':
        result = f'{num1} Больше либо равно {num2}'
    elif oper_sr == '<=':
        result = f'{num1} Меньше либо равно {num2}'
    else:
        result = "Неизвестная операция сравнения"
    
    print(result)

elif var == '3':
    # Логический режим
    value1 = input("Введите первое значение (true/false или любой текст): ").lower() == 'true'
    log_op = input("Введите логическую операцию (and, or, not): ")
    
    if log_op == 'not':
        result = not value1
        print(f"not {value1} = {result}")
    else:
        value2 = input("Введите второе значение (true/false или любой текст): ").lower() == 'true'
        if log_op == 'and':
            result = value1 and value2
            print(f"{value1} and {value2} = {result}")
        elif log_op == 'or':
            result = value1 or value2
            print(f"{value1} or {value2} = {result}")
        else:
            print("Неизвестная логическая операция")
else:
    print("Неверный выбор режима")
