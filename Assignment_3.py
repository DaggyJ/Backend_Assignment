def Math_operations(x, y):
    '''
    Math_operations function takes two integers parameters x and y and returns the sum and product 
    Lambda fuction calculates sum, product of two parameters in the arguments
    lambda arguments : expression
   '''
    mySum = lambda x, y : x + y
    myProduct = lambda  x, y : x * y
    
    return{
    "sum" : mySum(x, y),
    "product" : myProduct(x, y),
}

def main():
    x = int(input(f"Enter the value of x: "))
    y = int(input(f"Enter the value of y: "))
    result = Math_operations(x, y)
    print("Sum: ", result["sum"])
    print("Product: ", result["product"])
if __name__ == '__main__':
    main()
    
