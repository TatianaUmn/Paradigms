# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.


def sort_list_imperative(numbers):
    length = len(numbers)
    for i in range(length):
        for j in range(0, length - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

numbers = [5, 2, 8, 1, 9]
sorted_numbers = sort_list_imperative(numbers)
print(sorted_numbers)


# Задача №2
#Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

numbers = [57, 20, 81, 13, 9]
sorted_numbers = sort_list_declarative(numbers)
print(sorted_numbers)