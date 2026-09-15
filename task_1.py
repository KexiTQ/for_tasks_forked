## Программа запрашивает у пользователя натуральное число, меньшее `1_000_000_000`.  
## Если пользователь ввёл число вне диапазона, программа выводит строку `Input error` и останавливается.  
## Иначе выводится **самая большая цифра** введённого числа.

print("Starting programm")

number = int(input("Input number: "))

if number >= 1_000_000_000 or number < 1:
    print("Input ERROR")
else:
    maxdigit = 0
    
    while number > 0:
        digit = number % 10
        if digit >= maxdigit:
            maxdigit = digit
        number = number// 10
print("Max digit",maxdigit)