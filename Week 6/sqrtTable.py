import math
# outputs the sqrt of numbers between 1 & n in a table format
def sqrtTable(n):
    result=1
    print ("Number \t\t\t Square root")
    for i in range(0,n+1):
       print (i,end="\t\t\t")
       print (math.sqrt(i))

# the main function
def main():
    num = eval(input("Enter the number to print sqrt table:\n"))
    sqrtTable(num)


answer="Y"
while (answer=="Y" or answer=="y"):
    main() # Call the main function
    answer= input("Do you want to repeat (Y|y)?")
