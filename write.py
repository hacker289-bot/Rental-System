import csv
from datetime import datetime

class Land:
    def __init__(self, kitta_number, area, direction, number, cost, available):
        self.kitta_number = kitta_number
        self.area = area
        self.direction = direction
        self.number = number
        self.cost = cost
        self.available = available

def write_data(lands):
    """
    Write land data to a CSV file named 'data.txt'.

    Parameters:
    lands (list of Land objects): List of land objects to write to the file.
    """
    try:
        with open("data.txt", "w", newline='') as file:
            fieldnames = ["kitta_number", "area", "direction", "number", "cost", "availability"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for land in lands:
                availability = "Available" if land.available else "Not Available"
                writer.writerow({
                    "kitta_number": land.kitta_number,
                    "area": land.area,
                    "direction": land.direction,
                    "number": land.number,
                    "cost": land.cost,
                    "availability": availability
                })
    except Exception as e:
        print(f"Error occurred while writing data: {e}")

def write_invoice(kitta_number, area, customer_name, duration, cost):
    """
    Write a rental invoice to a text file.

    Parameters:
    kitta_number (str): Kitta number of the land.
    area (str): Area of the land.
    customer_name (str): Name of the customer.
    duration (int): Duration of the rent in months.
    cost (int): Cost of renting per month.
    """
    try:
        current_datetime = datetime.now()
        total_cost = int(cost) * duration
        filename = f"Rent_{current_datetime.strftime('%Y%m%d_%H%M%S')}.txt"

        with open(filename, "w") as invoice_file:
            invoice_file.write("-" * 60 + "\n")
            invoice_file.write("                        Techno Property                           \n")
            invoice_file.write("                           INVOICE                                \n")
            invoice_file.write("-" * 60 + "\n")
            invoice_file.write(f"Invoice: {current_datetime.strftime('%Y-%m-%d-%H-%M-%S')}\t\t")
            invoice_file.write(f"Date: {current_datetime.strftime('%Y-%m-%d')}\n")
            invoice_file.write(f"Name of Customer: {customer_name}\t\t")
            invoice_file.write(f"     Time: {current_datetime.strftime('%H:%M:%S')}\n")
            invoice_file.write("-" * 60 + "\n")
            invoice_file.write(f"Kitta Number: {kitta_number}\n")
            invoice_file.write(f"Location: {area}\n")
            invoice_file.write(f"Duration of Rent: {duration} months\n")
            invoice_file.write("-" * 60 + "\n")
            invoice_file.write(f"{'PARTICULAR':<15} {'QUANTITY':<10} {'UNIT PRICE':<15} {'TOTAL':<10}\n")
            invoice_file.write(f"{'Rent':<15} {1:<10} {cost:<15} {total_cost:<10}\n")
            invoice_file.write("-" * 60 + "\n")
            invoice_file.write(f"Your payable amount is: {total_cost}\n")
            invoice_file.write("-" * 60 + "\n")
            invoice_file.write(f"        Thank You {customer_name} for renting.              \n")
            invoice_file.write(f"                 See you again!                             \n")

        # Optionally print the invoice content to the console
        with open(filename, "r") as invoice_file:
            print(invoice_file.read())

    except Exception as e:
        print(f"Error occurred while writing invoice: {e}")

def write_invoice_return(kitta_number, area, customer_name, duration, cost):
    """
    Write a return invoice to a text file.

    Parameters:
    kitta_number (str): Kitta number of the land.
    area (str): Area of the land.
    customer_name (str): Name of the customer.
    duration (int): Duration of the rent in months.
    cost (int): Cost of renting per month.
    """
    try:
        current_datetime = datetime.now()
        total_cost = int(cost) * duration
        filename = f"Return_{current_datetime.strftime('%Y%m%d_%H%M%S')}.txt"

        with open(filename, "w") as invoice_file:
            invoice_file.write("-" * 60 + "\n")
            invoice_file.write("                    Techno Property                       \n")
            invoice_file.write("                    RETURN INVOICE                        \n")
            invoice_file.write("-" * 60 + "\n")
            invoice_file.write(f"Date: {current_datetime.strftime('%Y-%m-%d')}\t\t")
            invoice_file.write(f"Time: {current_datetime.strftime('%H:%M:%S')}\n")
            invoice_file.write("-" * 60 + "\n")
            invoice_file.write(f"Kitta Number: {kitta_number}\n")
            invoice_file.write(f"Location: {area}\n")
            invoice_file.write(f"Duration of Rent: {duration} months\n")
            invoice_file.write(f"Total Cost: ${total_cost}\n")
            invoice_file.write(f"Returned By: {customer_name}\n")
            invoice_file.write("-" * 60 + "\n")
            invoice_file.write(f"        Thank You {customer_name} for returning.              \n")

        # Optionally print the return invoice content to the console
        with open(filename, "r") as invoice_file:
            print(invoice_file.read())

    except Exception as e:
        print(f"Error occurred while writing return invoice: {e}")

def write_invoice_return_fined(kitta_number, area, customer_name, duration, cost):
    """
    Write a fined return invoice to a text file.

    Parameters:
    kitta_number (str): Kitta number of the land.
    area (str): Area of the land.
    customer_name (str): Name of the customer.
    duration (int): Duration of the rent in months.
    cost (int): Cost of renting per month.
    """
    try:
        current_datetime = datetime.now()
        rent_cost = int(cost) * duration
        fine = 0.1 * rent_cost  # Calculate 10% of the rent cost as fine
        total_cost = rent_cost + fine
        filename = f"Return_Fined_{current_datetime.strftime('%Y%m%d_%H%M%S')}.txt"

        with open(filename, "w") as invoice_file:
            invoice_file.write("-" * 60 + "\n")
            invoice_file.write("                     Techno Property                        \n")
            invoice_file.write("                     RETURN INVOICE                         \n")
            invoice_file.write("-" * 60 + "\n")
            invoice_file.write(f"Date: {current_datetime.strftime('%Y-%m-%d')}\t\t")
            invoice_file.write(f"Time: {current_datetime.strftime('%H:%M:%S')}\n")
            invoice_file.write("-" * 60 + "\n")
            invoice_file.write(f"Kitta Number: {kitta_number}\n")
            invoice_file.write(f"Location: {area}\n")
            invoice_file.write(f"Duration of Rent: {duration} months\n")
            invoice_file.write(f"Rent Cost: ${rent_cost}\n")
            invoice_file.write(f"Fine: ${fine}\n")
            invoice_file.write(f"Total Cost: ${total_cost}\n")
            invoice_file.write(f"Returned By: {customer_name}\n")
            invoice_file.write("-" * 60 + "\n")

        # Optionally print the fined return invoice content to the console
        with open(filename, "r") as invoice_file:
            print(invoice_file.read())

    except Exception as e:
        print(f"Error occurred while writing fined return invoice: {e}")

# Example usage:
# lands = [Land("K123", "Area1", "North", 1, 1000, True), Land("K124", "Area2", "South", 2, 1500, False)]
# write_data(lands)
# write_invoice("K123", "Area1", "John Doe", 6, 1000)
# write_invoice_return("K123", "Area1", "John Doe", 6, 1000)
# write_invoice_return_fined("K123", "Area1", "John Doe", 6, 1000)
