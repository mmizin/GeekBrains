from pprint import pprint


class OfficeDepartmentsError(Exception):

    def __init__(self):
        self.text = 'You have passed wrong name department. ' \
                    'Valid name departments are: finance, bookkeeping, reception.'
        super().__init__(self.text)


class NoneExistentEquipmentError(Exception):

    def __init__(self):
        self.text = 'You don\'t have this equipment in ware house!'
        super().__init__(self.text)


class OfficeEquipment:

    def __init__(self, trade_mark, model, price):
        self.trade_mark = trade_mark
        self.model = model
        self.price = price


class Warehouse:
    ware_house = {}
    sent_items = {}

    @classmethod
    def technique_reception(cls, *args):

        for obj in args:
            cls.ware_house.setdefault(obj.__class__.__name__, [])
            cls.ware_house[obj.__class__.__name__].append(obj.__dict__)

    @staticmethod
    def send_items_to_office(*args, department):
        departments = ['finance', 'bookkeeping', 'reception']

        if department not in departments:
            raise OfficeDepartmentsError
        Warehouse.sent_items.setdefault(department, {})

        for obj_si in args:
            obj_si_name = obj_si.__class__.__name__
            obj_si_params = obj_si.__dict__
            for item in Warehouse.ware_house[obj_si_name]:
                if item['model'] == obj_si_params['model']:
                    Warehouse.sent_items[department].setdefault(obj_si_name, [])
                    Warehouse.sent_items[department][obj_si_name].append(item)
                    Warehouse.ware_house[obj_si_name].remove(item)
                    break
                else:
                    raise NoneExistentEquipmentError


class Printer(OfficeEquipment):

    def __init__(self, trade_mark, model, price=0, laser=False, inkjet=False):
        super().__init__(trade_mark, model, price)
        self.laser = laser
        self.inkjet = inkjet
        self.laser = laser


class Scanner(OfficeEquipment):

    def __init__(self, trade_mark, model, price=0, paper_size=['A4']):
        super().__init__(trade_mark, model, price)
        self.paper_size = paper_size


class Xerox(OfficeEquipment):

    def __init__(self, trade_mark, model, price=0, print_speed=0, paper_size=['A4']):
        super().__init__(trade_mark, model, price)
        self.print_speed = print_speed
        self.paper_size = paper_size


printer = Printer(trade_mark='Sumsung', model='1101', inkjet=True, price=100)
printer2 = Printer(trade_mark='Sony', model='1101-2', laser=True, price=110)
scanner = Scanner(trade_mark='Sony', model='1102', price=200)
xerox = Xerox(trade_mark='Xerox', print_speed=30, model='1103', price=300)

Warehouse().technique_reception(printer, printer, printer2, scanner, xerox)
pprint(Warehouse().ware_house)
print('---------------------------------------------------------------------------------------------------\n')
Warehouse().send_items_to_office(printer, printer, scanner, department='finance')
pprint(Warehouse().sent_items)


