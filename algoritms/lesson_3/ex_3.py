# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


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
    print(l)


def test_2(l):
    sorted_l = sorted(l)
    min_n, max_n = sorted_l[0], sorted_l[-1]
    idx_min = l.index(min_n)
    idx_max = l.index(max_n)
    l[idx_min], l[idx_max] = l[idx_max], l[idx_min]

    print(l)


def test_3(l):
    min_n, max_n = min(l), max(l)
    idx_min = l.index(min_n)
    idx_max = l.index(max_n)
    l[idx_min], l[idx_max] = l[idx_max], l[idx_min]

    print(l)


test_1([i for i in range(2, 10)])
test_2([i for i in range(2, 10)])
test_3([i for i in range(2, 10)])
