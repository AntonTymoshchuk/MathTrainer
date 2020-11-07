from random import Random
from os import system
from datetime import datetime
from time import sleep

if __name__ == '__main__':
    system('clear')
    print('Тренер счёта в уме\n')

    print('Размер числа А : ', end='')
    number_a_max_size = int(input())

    print('Размер числа В : ', end='')
    number_b_max_size = int(input())

    number_a_max_value = 1
    number_b_max_value = 1

    iteration = 0
    while iteration < number_a_max_size:
        number_a_max_value *= 10
        iteration += 1

    iteration = 0
    while iteration < number_b_max_size:
        number_b_max_value *= 10
        iteration += 1

    number_a_max_value -= 1
    number_b_max_value -= 1

    while True:
        system('clear')
        print('Тренер счёта в уме\n')

        number_a = Random().randint(1, number_a_max_value)
        number_b = Random().randint(1, number_b_max_value)
        action = ['плюс', 'минус', 'умножить на',
                  'разделить на'][Random().randint(0, 3)]

        swap_numbers = bool(Random().randint(0, 1))
        if swap_numbers:
            swap_value = number_a
            number_a = number_b
            number_b = swap_value

        result = None
        if action == 'плюс':
            result = number_a + number_b
        elif action == 'минус':
            result = number_a - number_b
        elif action == 'умножить на':
            result = number_a * number_b
        elif action == 'разделить на':
            result = round(number_a / number_b, 3)

        system_str = 'echo "{0} {1} {2}" | festival --tts ' \
                     '--language russian'.format(number_a, action, number_b)
        system(system_str)

        start_time = datetime.now()
        print("Ваш ответ : ", end='')
        answer_str = input()
        count_time = datetime.now() - start_time

        if answer_str.lower() == 'exit':
            system('clear')
            break

        system('clear')
        print('Тренер счёта в уме\n')

        answer = float(answer_str)
        if answer == result:
            print('Правильно, {0} с\n'.format(count_time.seconds))
        else:
            print('Неправильно, {0} с\n'.format(count_time.seconds))
        sleep(1)
