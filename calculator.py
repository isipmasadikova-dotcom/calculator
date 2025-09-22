print('Выберете режим работы калькулятора')
print('1. Арифметический')
print('2. Операция сравнения')
print('3. Логический')

var = input('Ввести номер режима работы:')


if var == '1':
    num1 = input()
    operator = input()
    num2 = input()
    if operator == '+':
        result = num1 + num2
        print(result)
    elif operator == '-':
        result = num1 - num2
        print(result)
    elif operator == '*':
        result = num1 * num2
        print(result)
    elif operator == '/':
        result = num1 / num2
        print(result)
    elif operator == '//':
        result = num1 / num2
        print(result)
    elif operator == '%':
        result = num1 % num2
        print(result)
    elif operator == '':
        result = num1  num2
        print(result)   
if var == '2':
    num1 = input()
    oper_sr = input()
    num2 = input()
    if num1 == num2: 
        print('Равны')
    elif num1 != num2:
        print('Не равны')
    elif num1 >  num2:
        print(num1, 'Больше', num2)
    elif num1 < num2: 
        print(num1, 'Меньше', num2)
    elif num1 >= num2:
        print(num1,'Больше либо равно', num2)
    elif num1 <= num2:
        print(num1,'Меньше либо равно', num2)
if var == '3':
    num1 = input()
    log_op = input()
    num2 = input() 
    Flag = 'true'
    if log_op == 'and':
        if Flag:
            result = num1 and num2
            print(str(result))
        else: 
            print(result)
    elif log_op == 'or':
        if Flag:
            result = num1 or num2 
            print(result)
        else:
            print(result)
    elif log_op == 'not':
        if Flag:
            result = not num2
            print(result)
        else:
            print(not num1)
            print(not num2)