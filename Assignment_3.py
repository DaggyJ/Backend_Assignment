def Math_operations(x, y):
    '''
    Math_operations function takes two integers parameters
    User_input is taken as x and y
    Lambda fuction calculates sum, product, quotient and difference of 'x' & 'y'. Lambda functions can take any number of arguments
    lambda arguments : expression
    Return function is use to return the results of sum, product, quotient and difference of 'x' & 'y'
    main function prints results of math_oparetions
   '''
   # x = int(input(f"Enter the value of x: "))
   # y = int(input(f"Enter the value of y: "))
    mySum = lambda x, y : x + y
    myProduct = lambda  x, y : x * y
    myQuotient = lambda  x, y : x / y
    myDifference = lambda  x, y : x - y

    return{
    "sum" : mySum(x, y),
    "product" : myProduct(x, y),
    "quotient" : myQuotient(x, y),
    "difference" : myDifference(x, y)
}

def main():
    result = Math_operations(x = int(input(f"Enter the value of x: ")), y = int(input(f"Enter the value of y: ")))
    print("Sum: ", result["sum"])
    print("Product: ", result["product"])
    print("Quotient: ", result["quotient"])
    print("Difference: ", result["difference"])

if __name__ == '__main__':
    main()
    