def fib(nterms):
    # first two terms
    n1=0
    n2 =1
    count = 1
    if nterms == 1:
        return n1
    else:
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
        return n1
     

def main():
    nterms = eval(input("Enter the number of terms to get their :\n"))
    # check if the number of terms is valid
    if (nterms>0):
        result=fib(nterms)
        print("Fibonacci sequence upto",nterms,":", result)
    else:
        print("Fibonacci sequence not valid for negative numbers")
        print("Please enter positive numbers")

main() # Call the main function
#can you rpeat this program as long as suer says yes
