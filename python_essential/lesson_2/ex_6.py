products_l = list()
data = ['name', 'price', 'count', 'unit']
count = 1


def get_analytics(products):
    dt = {}
    name, price, count, unit = [], [], [], []

    for c, d in products:
        name.append(d['name'])
        price.append(d['price'])
        count.append(d['count'])
        unit.append(d['unit'])

    dt.setdefault('name', name)
    dt.setdefault('price', price)
    dt.setdefault('count', count)
    dt.setdefault('unit', unit)

    return dt


while True:
    input_data = input("Add your data: name, price, count, unit. When you finish, write 'Done' ")
    input_products = list(map(lambda x: x.strip(), input_data.split(',')))
    if input_data and len(input_products) == 4:
        tmp_d = dict()
        for i in range(len(data)):
            tmp_d.setdefault(data[i], input_products[i])
        products_l.append((count, tmp_d))
        count += 1
    elif products_l and input_data.lower() == 'done':
        for k, v in get_analytics(products_l).items():
            print(f'{k}: {v}')
        break
