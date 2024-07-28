import os
import csv

filePath = 'products.csv'

def createCSV():
    if not os.path.exists(filePath):
        with open(filePath, 'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            header = (['name', 'quantity', 'price'])
            print("***********************************\n")
    else:
        print(f"Found existing '{filePath}'.")

def addProducts(name, quantity, price):
    try:
        with open(filePath, 'a', newline='') as file:
            writer = csv.writer(file)
            header = ([name, quantity, price])
            writer.writerow(header)

        print(f"Added '{name}' with quantity '{quantity}'.")
    except csv.Error as e:
        print(f"Error writing '{filePath}': {e}")

def readProducts():
    try:
        with open(filePath, 'r', newline='') as file:
            reader = csv.DictReader(file)
            print("\n========== Current Products ==========\n")
            for row in reader:
                print(f"{row['name']:20} {row['quantity']} {row['price']}")
    except FileNotFoundError:
        print(f"Error: '{filePath}' not found")
    except csv.Error as e:
        print(f"Error reading '{filePath}': {e}")

def updateProduct(name, newQuantity, price):
    try:
        rows = []
        with open(filePath, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'] == name:
                    row['quantity'] = newQuantity
                    row['price'] = price
                rows.append(row)
        with open(filePath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'quantity', 'price'])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Updated quantity for '{name}' to '{newQuantity}' & '{price}'.")
    except FileNotFoundError:
        print(f"Error: '{filePath}' not found.")
    except csv.Error as e:
        print(f"Error writing '{filePath}': {e}")
    

def deleteProduct(name):
    try:
        rows = []
        with open(filePath, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'] != name:
                    rows.append(row)
        with open(filePath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'quantity', 'price'])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Deleted product '{name}'.")
    except FileNotFoundError:
        print(f"Error: '{filePath}' not found.")
    except csv.Error as e:
        print(f"Error writing '{filePath}': {e}")

def main():
    createCSV()
    while True:
        print("\n===== Product Management Menu =====")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Product Quantity")
        print("4. Delete Product")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            readProducts()
        elif choice == '2':
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            price = int(input("Enter amount: Ksh."))
            addProducts(name, quantity, price)
        elif choice == '3':
            name = input("Enter product name to update: ")

            newQuantity = int(input("Enter new product quantity: "))
            price = int(input("Enter amount: Ksh."))
            updateProduct(name, newQuantity, price)
        elif choice == '4':
            name = input("Enter product name to delete: ")
            deleteProduct(name)
        elif choice == '5':
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Try Again.")

if __name__ == '__main__':
    main()
