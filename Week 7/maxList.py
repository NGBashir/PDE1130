
# find the nth largest element in thelist
def find_n_max(theList, n):
    new_List=theList.copy()
    new_List.sort(reverse=True)
    #print (*new_List)
    return new_List[n-1]
    

# the main function
def main():
    myList=[10,5,7,8,20,40,100,60,-20,-100] # try to generate a random list instead
    num = eval(input("find the nth largest element in the list\n"))
    lenList=len(myList)
    if num>lenList:
        print(num, "is greater than the lists Length")
    else:
        result=find_n_max(myList, num)
        print(result, "is the", num, "th largest element in",*myList) 


answer="Y"
while (answer=="Y" or answer=="y"):
    main() # Call the main function
    answer= input("Do you want to repeat (Y|y)?")
