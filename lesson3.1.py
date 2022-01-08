# lesson3. the strings
input_string = input('Введите новую строку: ')

a = f'Это строка в которую {input_string} новую строку'

d = 'замена в строке'

a = a.replace(input_string, d)

print(len(a))

c = a.find('строка')

if c != 0:
    print('Да')
else:
    print('Нет')
