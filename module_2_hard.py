def pass_(number):
    password = ''
    for i in range(1, number):
        for j in range(1,number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password

number = int(input('Введите число от 3 до 20: '))
if number <= 2 or number >= 21:
        print('Число вне диапазона')
result = pass_(number)
print('Пароль: ', result)