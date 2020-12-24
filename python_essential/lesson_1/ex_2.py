from datetime import timedelta


def main():
    seconds = int(input('Enter time in milliseconds '))
    print(timedelta(seconds=seconds))


if __name__ == '__main__':
    main()


