# Задача № 1 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def task1():
    str1 = 'мама дом бубу вор один'
    words = str1.split(' ')
    letter = 'а'
    letter2 = 'б'
    letter3 = 'в'
    str2 = []
    for word in words:
        if letter not in word and letter2 not in word and letter3 not in word:
            str2.append(word)
    print(str2)
task1()
# Задача № 2 Создайте программу для игры с конфетами человек против человека.
import random
def candy_game():
    turn_move = random.randint(1, 2)
    if turn_move == 1:
        print('\nВы ходите первым!\n')
        def human():
            print('С каким колличеством вы хотите играть')
            candy = int(input())
            while candy >= 1:
                print('\nСколько кофет вы хотите взять? не более 28\n')
                human_turn = int(input())
                computer_turn = random.randint(1, 28)
                if human_turn <= 28:
                    candy -= human_turn
                    if candy <= 0:
                        print('\nВы выйграли!')
                        break
                    print('осталось ', candy)
                    print('\nход комьютера\n')
                    if candy % 30 == 0:
                        candy -= 1
                        if candy <= 0:
                            print('\nВы програли')
                            break
                        print('осталось ', candy)
                    elif candy <= 28:
                        candy - 28
                        print('вы проиграли')
                        break
                    else:
                        candy -= computer_turn
                        if candy <= 0:
                            print('\nВы програли')
                            break
                        print('осталось ', candy )
                elif human_turn > 28:
                    print('Введено неверное значение')
        human()
    else:
        print('\nПервый ход за компьютером!\n')
        def comp():
            candy = random.randint(120, 300)
            print('Компьютер решил играть с ', candy, 'конфетами')
            while candy >= 1:
                print('\nход комьютера\n')
                computer_turn = random.randint(1, 28)
                if candy % 30 == 0:
                    candy -= 1
                    if candy <= 0:
                        print('\nВы програли')
                        break
                    print('осталось ', candy)
                elif candy <= 28:
                        candy - 28
                        print('вы проиграли')
                else:
                    candy -= computer_turn
                    if candy <= 0:
                        print('\nВы програли')
                        break
                    print('осталось ', candy )
                print('\nСколько кофет вы хотите взять? не более 28\n')
                human_turn = int(input())
                if human_turn <= 28:
                    candy -= human_turn
                    if candy <= 0:
                        print('\nВы выйграли!')
                        break
                    print('осталось ', candy)
                elif human_turn > 28:
                    print('Введено неверное значение')
        comp()
candy_game()
# Задача № 3 Создайте программу для игры в ""Крестики-нолики"".
# Задача № 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Задача № 5 Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.