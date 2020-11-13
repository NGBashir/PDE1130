# gives you the factorial of a number n
def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

# the main function
def main():
    num = eval(input("Enter the number and we will tell you it Factorial: "))
    result = factorial(num)
    print("The factorial for", num, " is ",result)


answer="Y"
while (answer=="Y" or answer=="y"):
    main() # Call the main function
    answer= input("Do you want to repeat (Y|y)?")
