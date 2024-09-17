import os
import csv

filePath = 'products.csv'

def createCSV():
    if not os.path.exists(filePath):
        with open(filePath, 'w', newline='') as file:
            writer = csv.DictWriter(file, delimiter=',')
            header = ['name', 'quantity', 'price']
            writer.writerow(header)
            print("CSV file created.")
    else:
        print(f"Found existing '{filePath}'.")

def addProduct(name, quantity, price):
    try:
        with open(filePath, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([name, quantity, price])
        print(f"Added '{name}' with quantity '{quantity}' and price '{price}'.")
    except csv.Error as e:
        print(f"Error writing to '{filePath}': {e}")

def readProducts():
    try:
        with open(filePath, 'r', newline='') as file:
            reader = csv.DictReader(file, delimiter=',')
            print("\n========== Current Products ==========\n")
            for row in reader:
                print(f"{row['name']:15} {row['quantity']:3}kg Ksh.{row['price']}")
    except FileNotFoundError:
        print(f"Error: '{filePath}' not found")
    except csv.Error as e:
        print(f"Error reading '{filePath}': {e}")

def updateProduct(name, quantity, price):
    try:
        rows = []
        found = False
        with open(filePath, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'] == name:
                    row['quantity'] = quantity
                    row['price'] = price
                    found = True
                rows.append(row)
        if found:
            with open(filePath, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['name', 'quantity', 'price'])
                writer.writeheader()
                writer.writerows(rows)
            print(f"Updated '{name}' with quantity '{quantity}' and price '{price}'.")
        else:
            print(f"Product '{name}' not found.")
    except FileNotFoundError:
        print(f"Error: '{filePath}' not found.")
    except csv.Error as e:
        print(f"Error writing to '{filePath}': {e}")

def deleteProduct(name):
    try:
        rows = []
        found = False
        with open(filePath, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'] != name:
                    rows.append(row)
                else:
                    found = True
        if found:
            with open(filePath, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['name', 'quantity', 'price'])
                writer.writeheader()
                writer.writerows(rows)
            print(f"Deleted product '{name}'.")
        else:
            print(f"Product '{name}' not found.")
    except FileNotFoundError:
        print(f"Error: '{filePath}' not found.")
    except csv.Error as e:
        print(f"Error writing to '{filePath}': {e}")

def main():
    createCSV()
    while True:
        print("\n===== Product Management Menu =====")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            readProducts()
        elif choice == '2':
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            price = int(input("Enter product price: "))
            addProduct(name, quantity, price)
        elif choice == '3':
            name = input("Enter product name to update: ")
            quantity = int(input("Enter new product quantity: "))
            price = int(input("Enter new product price: "))
            updateProduct(name, quantity, price)
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
