import os
import csv
import logging
from datetime import datetime

filePath = 'Store.csv'
backupPath = 'Backup_Store.csv'

# To check user logs throughout the program.
logging.basicConfig(filename='store_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def createCSV():
    if not os.path.exists(filePath):
        with open(filePath, 'w', newline='') as file:
            writer = csv.DictWriter(file, delimiter=',')
            header = ['name', 'quantity', 'price', 'expiry_date']
            writer.writerow(header)
            print("CSV file created.")
            logging.info("CSV file created.")
    else:
        print(f"Found existing '{filePath}'.")
        logging.info(f"Found existing '{filePath}'.")

def productExists(name):
    try:
        with open(filePath, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'].lower() == name.lower():
                    return True
        return False
    except FileNotFoundError:
        print(f"Error: '{filePath}' not found.")
        logging.error(f"Error: '{filePath}' not found.")
        return False

def addProduct(name, quantity, price, expiry_date):
    if quantity < 0 or price < 0:
        print("Quantity and price must be non-negative.")
        return

    if not name.strip():
        print("Product name cannot be empty.")
        return

    if productExists(name):
        print(f"Product '{name}' already exists.")
        return

    try:
        with open(filePath, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, quantity, price, expiry_date])
        print(f"'{name}' '{quantity}kg' @ 'Ksh.{price}' added successfully.")
        logging.info(f"Product '{name}' added successfully.")
    except csv.Error as e:
        print(f"Error writing to '{filePath}': {e}")
        logging.error(f"Error writing to '{filePath}': {e}")

def readProducts():
    try:
        with open(filePath, 'r', newline='') as file:
            reader = csv.DictReader(file, delimiter=',')
            print("\n========== Current Products ==========\n")
            for row in reader:
                print(f"{row['name']:15} {row['quantity']:3}kg  Ksh.{row['price']} Exp: {row['expiry_date']}")
        logging.info("Products viewed successfully.")
    except FileNotFoundError:
        print(f"Error: '{filePath}' not found")
        logging.error(f"Error: '{filePath}' not found")
    except csv.Error as e:
        print(f"Error reading '{filePath}': {e}")
        logging.error(f"Error reading '{filePath}': {e}")

def updateProduct(name, quantity, price, expiry_date):
    if not productExists(name):
        print(f"Product '{name}' not found in your store.")
        logging.warning(f"Product '{name}' not found in your store.")
        return

    try:
        if quantity < 0 or price < 0:
            print("Quantity and price must be non-negative.")
            return

        rows = []
        with open(filePath, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'].lower() == name.lower():
                    row['quantity'] = quantity
                    row['price'] = price
                    row['expiry_date'] = expiry_date
                rows.append(row)

        with open(filePath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'quantity', 'price', 'expiry_date'])
            writer.writeheader()
            writer.writerows(rows)

        print(f"'{name}' '{quantity}kg' for 'Ksh.{price}' updated successfully.")
        logging.info(f"Product '{name}' updated successfully.")
    except FileNotFoundError:
        print(f"Error: '{filePath}' not found in your store.")
        logging.error(f"Error: '{filePath}' not found in your store.")
    except csv.Error as e:
        print(f"Error writing to '{filePath}': {e}")
        logging.error(f"Error writing to '{filePath}': {e}")

def deleteProduct(name):
    try:
        rows = []
        found = False
        with open(filePath, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'].lower() != name.lower():
                    rows.append(row)
                else:
                    found = True
        if found:
            with open(filePath, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['name', 'quantity', 'price', 'expiry_date'])
                writer.writeheader()
                writer.writerows(rows)
            print(f"'{name}' deleted successfully.")
            logging.info(f"Product '{name}' deleted successfully.")
        else:
            print(f"Product '{name}' not found in your store.")
            logging.warning(f"Product '{name}' not found in your store.")
    except FileNotFoundError:
        print(f"Error: '{filePath}' not found.")
        logging.error(f"Error: '{filePath}' not found.")
    except csv.Error as e:
        print(f"Error writing to '{filePath}': {e}")
        logging.error(f"Error writing to '{filePath}': {e}")

def backupCSV():
    try:
        with open(filePath, 'r') as original_file:
            with open(backupPath, 'w', newline='') as backup_file:
                writer = csv.writer(backup_file)
                for line in original_file:
                    backup_file.write(line)
        print(f"Backup created at '{backupPath}'.")
        logging.info(f"Backup created at '{backupPath}'.")
    except FileNotFoundError:
        print(f"Error: '{filePath}' not found.")
        logging.error(f"Error: '{filePath}' not found.")
    except Exception as e:
        print(f"Error during backup: {e}")
        logging.error(f"Error during backup: {e}")

def main():
    createCSV()
    while True:
        print("\n===== Product Management Menu =====")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Backup Data")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            readProducts()
        elif choice == '2':
            name = input("Enter product name: ")
            if not name.strip():
                print("Product name cannot be empty.")
                continue
            try:
                quantity = int(input("Enter product quantity: "))
                price = float(input("Enter product price: Ksh. "))
                expiry_date = input("Enter product expiry date (YYYY-MM-DD): ")
                # Validate date format
                datetime.strptime(expiry_date, '%Y-%m-%d')
                addProduct(name, quantity, price, expiry_date)
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue
        elif choice == '3':
            name = input("Enter product name to update: ")
            if not productExists(name):
                print(f"Product '{name}' not found.")
                continue
            try:
                quantity = int(input("Enter new product quantity: "))
                price = float(input("Enter new product price: Ksh. "))
                expiry_date = input("Enter new product expiry date (YYYY-MM-DD): ")
                # Validate date format
                datetime.strptime(expiry_date, '%Y-%m-%d')
                updateProduct(name, quantity, price, expiry_date)
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue
        elif choice == '4':
            name = input("Enter product name to delete: ")
            deleteProduct(name)
        elif choice == '5':
            backupCSV()
        elif choice == '6':
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
