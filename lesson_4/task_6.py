
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. 
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. 
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle

print('a)')
num = int(input('Введите стартовое число '))
for el in count(num):
    if el > (num + 10):
        break
    print(el, end=' ')

print()

print('b)')
cities = ['Moscow', 'Paris', 'New York']
my_iter = cycle(cities)
i = 0
while i < 12:
    print(next(my_iter), end=' ')
    i += 1
