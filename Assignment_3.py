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


        #MATHS_OPARETOR THAT TAKES TWO NUMS
#Definiton of numbers
def Math_operations(num1, num2):
    '''
    math_operations function takes two integers parameters
    uses lambda fuction to calculate sum, product, quotient and difference of the numbers
    '''
    """"
    lambda arguments : expression
    lambda functions can take any number of arguments
    """
#Lambda functions 
    mySum = lambda num1, num2 : num1 + num2

    myProduct = lambda num1, num2 : num1 * num2

    myQuotient = lambda num1, num2 : num1 / num2

    myDifference = lambda num1, num2 : num1 - num2
    #Return function
    return{
    "sum" : mySum(num1, num2),
    "product" : myProduct(num1, num2),
    "quotient" : myQuotient(num1, num2),
    "difference" : myDifference(num1, num2)
}

def main():
    result = Math_operations(48, 12)
    print("Sum: ", result["sum"])
    print("Product: ", result["product"])
    print("Quotient: ", result["quotient"])
    print("Difference: ", result["difference"])

if __name__ == '__main__':
    main()

