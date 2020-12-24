def main():
    num = input('Enter your number: ')
    numbers = []

    for _ in num:
        numbers.append(int(_))

    print(max(numbers))


if __name__ == '__main__':
    main()
