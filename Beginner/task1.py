'''
Practical Test: Create a basic calculator that can perform addition, subtraction,
multiplication, and division.
'''

def main():

    while True:

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("\nChoose what you want to do:")

        input1 = float(input("\nEnter first number: "))
        input2 = float(input("Enter second number: "))

        if choice == '1':
            print(input1 + input2)
        elif choice == '2':
            print(input1 - input2)
        elif choice == '3':
            print(input1 * input2)
        elif choice == '4':
            print(input1 / input2)
        elif choice == '5':
            print("\nExiting")
            break
        else:
            print("Invalid input. Try with numbers")
            break

if __name__ == '__main__':
    main()