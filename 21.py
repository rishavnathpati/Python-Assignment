class Calculator:
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

    def input_num():
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2

    while True:
        print("\n\nSelect operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("0. Exit")
        choice = input("Enter choice(1/2/3/4/0): ")
        if choice in ('1', '2', '3', '4', '0'):
            if choice == '0':
                break

            elif choice == '1':
                num1, num2 = input_num()
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                num1, num2 = input_num()
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                num1, num2 = input_num()
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                num1, num2 = input_num()
                print(num1, "/", num2, "=", divide(num1, num2))

        else:
            print("Invalid Input")
