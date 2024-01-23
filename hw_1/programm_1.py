"""Сортировка списка
Задача №1
Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

Задача №2
Написать точно такую же процедуру, но в декларативном стиле"""


def sort_list_imperative(num_list: []) -> []:
    if len(num_list) <= 1:
        return num_list

    pivot = num_list[len(num_list) // 2]
    left = [x for x in num_list if x < pivot]
    middle = [x for x in num_list if x == pivot]
    right = [x for x in num_list if x > pivot]
    return sort_list_imperative(right) + middle + sort_list_imperative(left)


def sort_list_declarative(num_list: []) -> []:
    return sorted(num_list, reverse=True)


if __name__ == '__main__':
    number_list = input('ВВЕДИТЕ ЧИСЛА СПИСКА ЧЕРЕЗ ПРОБЕЛ: ').split()
    number_list = [int(x) for x in number_list]
    print(f'ИСХОДНЫЙ СПИСОК: {number_list}')
    print(f'БЫСТРАЯ СОРТИРОВКА ИМПЕРАТИВНЫЙ СТИЛЬ: {sort_list_imperative(number_list)}')
    print(f'БЫСТРАЯ СОРТИРОВКА ДЕКЛАРАТИВНЫЙ СТИЛЬ: {sort_list_declarative(number_list)}')
