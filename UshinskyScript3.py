#!/usr/bin/python3
"""два случайных набора чисел"""
import random as rm
a1 = {rm.randint(1, 100) for i in range(10)} #Создаём два набора рандомных чисел (числа могут быть от 1 до 100, кол-во чисел 10 )
a2 = {rm.randint(1, 100) for i in range(10)}
print(f'{len(a1)}')
print(f'{len(a2)}')
print(f'a1: {a1} \n a2:{a2}')

print(f'Входят одновременно в оба: {sorted(a1.intersection(a2))}')
print(f'Входят только в первое, но не входят во второе: {sorted(a1.difference(a2))}')
print(f'Входят только во второе, но не входят в первое: {sorted(a2.difference(a1))}')
print(f'Входят в первое или во второе, но не в оба из них одновременно: {sorted(a1.symmetric_difference(a2))}')
