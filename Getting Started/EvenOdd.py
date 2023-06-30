# Find whether the number is even or odd

def evenOdd(num):
    if num%2 == 0:
        print("Even Number.")
    else:
        print("Odd Number.")

num = int(input("Enter a numner: "))
evenOdd(num)