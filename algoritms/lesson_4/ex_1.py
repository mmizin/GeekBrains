# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

import cProfile

def test_1(l):
    tmp = list(l)
    i = 0

    while i < len(l) - 1:
        if tmp[i] > tmp[i + 1]:
            tmp[i], tmp[i+1] = tmp[i + 1], tmp[i]
            i = 0
        else:
            i += 1

    min_n, max_n = tmp[0], tmp[-1]
    idx_min = l.index(min_n)
    idx_max = l.index(max_n)

    l[idx_min], l[idx_max] = l[idx_max], l[idx_min]


def test_2(l):
    sorted_l = sorted(l)
    min_n, max_n = sorted_l[0], sorted_l[-1]
    idx_min = l.index(min_n)
    idx_max = l.index(max_n)
    l[idx_min], l[idx_max] = l[idx_max], l[idx_min]


def test_3(l):
    min_n, max_n = min(l), max(l)
    idx_min = l.index(min_n)
    idx_max = l.index(max_n)
    l[idx_min], l[idx_max] = l[idx_max], l[idx_min]



#timeit
# python -m timeit -n 1000 -s "import ex_1" "ex_1.test_1([i for i in range(2,10)])"
# 1000 loops, best of 3: 2.14 usec per loop
#
# python -m timeit -n 1000 -s "import ex_1" "ex_1.test_2([i for i in range(2,10)])"
# 1000 loops, best of 3: 1.64 usec per loop
#
# python -m timeit -n 1000 -s "import ex_1" "ex_1.test_3([i for i in range(2,10)])"
# 1000 loops, best of 3: 1.53 usec per loop

# The best variant is #3
# Because we use built-in methods to perform actions.


#cProfile.run
# 1   19.358   19.358   24.710   24.710 ex_1.py:11(test_1)
# 1    0.000    0.000    3.134    3.134 ex_1.py:29(test_2)
# 1    0.000    0.000    3.964    3.964 ex_1.py:37(test_3)
