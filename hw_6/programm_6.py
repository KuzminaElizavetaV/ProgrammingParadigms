"""
Бинарный поиск
    ● Контекст
        Предположим, что мы хотим найти элемент в массиве (получить его индекс). Мы можем это сделать просто перебрав
        все элементы. Но что, если массив уже отсортирован? В этом случае можно использовать бинарный поиск.
        Принцип прост: сначала берём элемент находящийся посередине и сравниваем с тем, который мы хотим найти.
        Если центральный элемент больше нашего, рассматриваем массив слева от центрального, а если больше - справа и
        повторяем так до тех пор, пока не найдем наш элемент.
    ● Ваша задача
        Написать программу на любом языке в любой парадигме для бинарного поиска. На вход подаётся целочисленный массив
        и число. На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.
"""
from random import randint


def create_sorted_list(start: int, end: int, len_list: int) -> [int]:
    num_list = [randint(start, end) for _ in range(len_list)]
    num_list.sort()
    return num_list


def binary_search(num_list: [int], number: int) -> int | None:
    mid = len(num_list) // 2
    low = 0
    high = len(num_list) - 1

    while num_list[mid] != number and low <= high:
        if number > num_list[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return None
    else:
        return mid


def is_index_number_message(value: int | None) -> str:
    if value is None:
        return "Искомое число не найдено в списке!"
    else:
        return f"Индекс искомого числа равен {value}"


if __name__ == '__main__':
    number_list = create_sorted_list(1, 35, 25)
    print(number_list)
    print(is_index_number_message(binary_search(number_list, 32)))

