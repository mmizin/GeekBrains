import heapq


def my_func(num_one, num_two, num_three):
    largest_integers = heapq.nlargest(2, list(locals().values()))  # [39, 26]
    return sum(largest_integers)


def my_func_sort(num_one, num_two, num_three):
    values = sorted(locals().values())
    return values[-1] + values[-2]


def my_func_max(num_one, num_two, num_three):
    values = list(locals().values())
    first_large_num = max(values)
    values.remove(first_large_num)
    second_large_num = max(values)
    return first_large_num + second_large_num


print(my_func(4, 3, 3))
print(my_func_sort(4, 3, 3))
print(my_func_max(4, 3, 3))
