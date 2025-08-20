'''
Practical Test: Write a function that calculates the factorial of a number and
demonstrate calling it in a main program.
'''

def fact(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * fact(n-1)

def factorial(no):
    if no < 0:
        return "Factorial of number less than 0 not possible."
    elif no == 0:
        return 1
    else:
        fact = 1
        for i in range(1, no+1):
            fact = fact * i
        
        return fact

def main():
    number = int(input("Enter number for which you want factorial:"))
    answer = fact(number)

    print(answer)

    a1 = int(input("Enter number: "))
    b1 = factorial(a1)
    print(b1)


if __name__ == '__main__':
    main()