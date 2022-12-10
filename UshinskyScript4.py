#!/usr/bin/python3
"""Создать игровой инвентарь"""
import time
Inventory = {} #Наш инвентарь, пока он пуст
MaxWeight=int(input("Максимальный вес инвентаря: ")) #Максимальный вес нашего инвентаря, его выбираем мы сами
a= sum(Inventory.values()) #Сумма веса (значений) нашего инвентаря
while True:
    print(f'Ваш инвентарь (Предмет:вес) : {Inventory}')
    print(f'Предметы вашего инвентаря: ')
    for i in Inventory.items():
        print(f'{i}')
    print(f'Вес вашего инвентаря: {a}')
    if a == 0:
        new_item = str(input(f'Ваш инвентарь пуст, вы можете добавить новый предмет или не добавлять предметы (new or no)\n:'))
    else:
        new_item = str(input(f'Хотите добавить новый предмет или удалить старый? (new - добавить новый, del - удалить старый, no - не добавлять предмет)\n:'))
    if new_item == 'new':
        print('Какой предмет вы хотите?: ')
        item = input("Введите предмет: ")
        weight = int(input("Введите вес: "))
        a = sum(Inventory.values())
        if a + weight < MaxWeight:
            isName = Inventory.get(item, weight)
            Inventory[item] = weight
            a = sum(Inventory.values())
        else:
            print('!!!У вас не хватает места в инвентаре, чтобы добавить этот предмет. \n Выберите предмет с меньшим весом или удалите предмет из вашего инвентаря, чтобы освободить место!!!')
    elif new_item == 'del' and a!=0:
        print('Какой предмет вы хотите удалить?: ')
        n = input("")
        if n == 'all':
            Inventory.clear()
            a = sum(Inventory.values())
            print('Вы очистили свой инвентарь')
            continue
        del Inventory[n]
        a = sum(Inventory.values())
        print(f'Предмет {n} был удалён из вашего инвентаря')
    elif new_item == 'no':
        print(f'Вы решили не добавлять предметы')
        a = sum(Inventory.values())
        print(f'Ваш инвентарь на текущий момент: {Inventory} с общим весом: {a}')
        break
    else:
        print(f'***Неправильный ввод, попробуйте \"new\" для добавления нового предмета, \"del\" для удаления старого предмета или \"no\" если не хотите брать новые предметы')
        time.sleep(1)
