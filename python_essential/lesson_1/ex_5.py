def main():
    revenues = float(input('Enter your revenues: '))
    expenses = float(input('Enter your expenses: '))

    if revenues > expenses:
        print(f"Congrats, your profit is {revenues - expenses}$")
        print(f'Return on sales equal: {int((revenues - expenses) / revenues * 100)}%')

        employees_count = input("Enter number of employees that works for company: ")
        print(f'Profit of the company per employee equal: {float((revenues - expenses) / float(employees_count))}')
    else:
        print(f'Unfortunately you don\'t have profit, your loss is {revenues - expenses}$')


if __name__ == '__main__':
    main()