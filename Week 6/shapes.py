# print the upper part triangle
def upperRightTriangle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print ("*", end="")
        print("\n")
    
# print the lower part triangle
def upperLowerTriangle(n):
    for i in range(n+1,1,-1):
        for j in range(1,i):
            print ("*", end="")
        print("\n")

# the main function
def main():
    num = eval(input("Enter the numberof lines to print the shape"))
    upperRightTriangle(num)
    upperLowerTriangle(num)
  
#program starts here and repeats as long as user types 'y'
answer="Y"
while (answer=="Y" or answer=="y"):
    main() # Call the main function
    answer= input("Do you want to repeat (Y|y)?")


#change * to nother charachter according t choice
