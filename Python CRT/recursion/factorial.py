'''
write a py prog to calculate factorial of n using recursion
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
n= int(input("Enter a number: "))
if n< 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {n} is: {factorial(n)}")
