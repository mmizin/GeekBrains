def main():
    start = int(input("Start from: "))
    expected_result = int(input("Start from: "))
    day = 1

    while start < expected_result:
        start += start / 10
        day += 1

    print(f'On the {day} day our sportsman will get expected result.')


if __name__ == '__main__':
    main()
