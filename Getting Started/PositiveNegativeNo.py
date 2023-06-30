def positiveNegativeNo(num):
    if num > 0:
        print("Positive Number.")
    elif num < 0:
        print("Negative Number.")
    else:
        print("Zero.")

num = int(input("Enter a number : "))
positiveNegativeNo(num)