def Math_operations(x, y):
    x = int(input(f"Enter the value of x: "))

    y = float(input(f"Enter the value of y: "))

    '''
    math_operations function takes two integers parameters
    user input is taken as x and y
    uses lambda fuction to calculate sum, product, quotient and difference of the numbers
    lambda arguments : expression
    lambda functions can take any number of arguments
   '''

    mySum = lambda x, y : x + y

    myProduct = lambda  x, y : x * y

    myQuotient = lambda  x, y : x / y

    myDifference = lambda  x, y : x - y
    #Return function
    return{
    "sum" : mySum(x, y),
    "product" : myProduct(x, y),
    "quotient" : myQuotient(x, y),
    "difference" : myDifference(x, y)
}

def main():
    result = Math_operations('x', 'y')
    print("Sum: ", result["sum"])
    print("Product: ", result["product"])
    print("Quotient: ", result["quotient"])
    print("Difference: ", result["difference"])

if __name__ == '__main__':
    main()

