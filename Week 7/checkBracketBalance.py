
# find the nth largest element in the
list
def check_balance(myinput):
    left=[]
    right=[]
    for i in range(0,len(myinput)):
        if myinput[i]=='[':
            left=left+['[']
        elif myinput[i]==']':
            if len(left)>len(right):
                right=right+[']']
        else:
            return False

    return(len(left)==len(right))
    

# the main function
def main():
   
    myinputSt = input("Enter a string containing only square brackets, [].\n The program checks whether the brackets are balanced or not.")
    print(myinputSt, " is balanced: ", check_balance(myinputSt))
    


answer="Y"
while (answer=="Y" or answer=="y"):
    main() # Call the main function
    answer= input("Do you want to repeat (Y|y)?")
