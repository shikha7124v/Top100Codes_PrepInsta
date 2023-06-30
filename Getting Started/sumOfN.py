# Sum of n natural numbers 

def sumOfN(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    print("sum = ", sum)

num = int(input("Enter the number upto which you want sum: "))
sumOfN(num)

# Method 2

print(int(num*(num+1)/2))

# Method 3 : Using Recursion 

def getSum(n):
    if n == 1:
        return 1
    return n + getSum(n-1)

n = int(input("Enter a no. : "))
print(getSum(n))