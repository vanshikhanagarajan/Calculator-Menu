
while True:
    print("\n===== MENU-DRIVEN CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even or Odd")
    print("6. Check Prime Number")
    print("7. Check Armstrong Number")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum =", a + b)

    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Difference =", a - b)

    elif choice == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Product =", a * b)

    elif choice == 4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if b != 0:
            print("Quotient =", a / b)
        else:
            print("Division by zero is not possible.")

    elif choice == 5:
        n = int(input("Enter a number: "))

        if n % 2 == 0:
            print(n, "is an Even number")
        else:
            print(n, "is an Odd number")

    elif choice == 6:
        n = int(input("Enter a number: "))

        if n < 2:
            print(n, "is not a Prime number")
        else:
            for i in range(2, n):
                if n % i == 0:
                    print(n, "is not a Prime number")
                    break
            else:
                print(n, "is a Prime number")

    elif choice == 7:
        n = int(input("Enter a number: "))

        if n < 0:
            print(n, "is not an Armstrong number")
        else:
            temp = n
            digits = len(str(n))
            total = 0

            while temp > 0:
                digit = temp % 10
                total = total + digit ** digits
                temp = temp // 10

            if total == n:
                print(n, "is an Armstrong number")
            else:
                print(n, "is not an Armstrong number")

    elif choice == 8:
        print("Exiting calculator...")
        break

    else:
        print("Invalid choice! Please try again.")
