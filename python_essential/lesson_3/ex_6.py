def int_func(some_string: str):
    return some_string.title()


def make_title():
    input_data = list(map(lambda x: x.strip().lower(), input('Enter your words separated by " ": ').split()))
    for word in list(map(lambda x: int_func(x), input_data)):
        print(word)


make_title()
