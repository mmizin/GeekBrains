elements = input('Enter elements separated by ",": ')

if elements:
    elements = list(map(lambda e: e.strip(),  elements.split(',')))

    swap_list = []
    for i in range(0, len(elements), 2):
        try:
            elements[i], elements[i+1] = elements[i+1], elements[i]
            swap_list.append(elements[i])
            swap_list.append(elements[i+1])
        except IndexError:
            swap_list.append(elements[-1])

    print(swap_list)
