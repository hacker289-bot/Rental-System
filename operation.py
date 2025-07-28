# main.py

import csv

from write import write_invoice, write_invoice_return, write_invoice_return_fined

class Land:
    def __init__(self, kitta_number, area, direction, number, cost, availability):
        self.kitta_number = kitta_number
        self.area = area
        self.direction = direction
        self.number = number
        self.cost = cost
        self.available = availability

def read_data():
    lands = []
    with open("data.txt", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            availability = row["availability"] == "Available"
            land = Land(
                kitta_number=int(row["kitta_number"]),
                area=row["area"],
                direction=row["direction"],
                number=int(row["number"]),
                cost=int(row["cost"]),
                availability=availability
            )
            lands.append(land)
    return lands

def write_data(lands):
    with open("data.txt", "w", newline='') as file:
        fieldnames = ["kitta_number", "area", "direction", "number", "cost", "availability"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for land in lands:
            writer.writerow({
                "kitta_number": land.kitta_number,
                "area": land.area,
                "direction": land.direction,
                "number": land.number,
                "cost": land.cost,
                "availability": "Available" if land.available else "Not Available"
            })

def rent_land(lands, kitta_number):
    for land in lands:
        if land.kitta_number == kitta_number and land.available:
            land.available = False
            return f"Land {kitta_number} has been rented."
    return f"Land {kitta_number} is either not available or does not exist."

def return_land(lands, kitta_number):
    for land in lands:
        if land.kitta_number == kitta_number and not land.available:
            land.available = True
            return f"Land {kitta_number} has been returned."
    return f"Land {kitta_number} is either already available or does not exist."

def display_land(lands):
    print("\nList of lands:")
    for land in lands:
        status = "Available" if land.available else "Rented"
        print(f"Kitta Number: {land.kitta_number}, Area: {land.area}, Direction: {land.direction}, Number: {land.number}, Cost: {land.cost}, Status: {status}")

class TechnoPropertyNepal:
    def __init__(self):
        self.lands = read_data()

    def display_menu(self):
        print("*************************************************************************************")
        print("*                                                                                   *")
        print("*                           Techno Property Nepal                                   *")
        print("*                                                                                   *")
        print("*************************************************************************************")
        print("*************************     Welcome to the land rental System  ********************")
        print("                               Press 1-> To rent the land                            ")
        print("                               Press 2-> To return the land                          ")
        print("                               Press 3-> To display the land                         ")
        print("                               Press 4-> To exit the system                          ")
        return input("Enter a value as per your requirement: ")

    def get_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input, please enter a number.")

    def get_str_input(self, prompt):
        while True:
            value = input(prompt)
            if value.strip():
                return value
            else:
                print("Invalid input, please enter a non-empty string.")

    def handle_rent_land(self):
        while True:
            print("Available lands for rent:")
            for land in self.lands:
                if land.available:
                    print(f"Kitta Number: {land.kitta_number}, Area: {land.area}, Direction: {land.direction}, Number: {land.number}, Cost: {land.cost}, Status: {'Available' if land.available else 'Rented'}")

            kitta_number = self.get_int_input("Fill out the kitta number to be rented: ")
            customer_name = self.get_str_input("Enter your name: ")
            duration = self.get_int_input("Fill the duration of renting (months): ")

            for land in self.lands:
                if land.kitta_number == kitta_number:
                    area = land.area
                    cost = land.cost

            print(rent_land(self.lands, kitta_number))
            write_invoice(kitta_number, area, customer_name, duration, cost)
            write_data(self.lands)

            continue_renting = self.get_str_input("Do you want to continue renting (yes/no): ").lower()
            if continue_renting != 'yes':
                break

    def handle_return_land(self):
        kitta_number = self.get_int_input("Fill out the kitta number to return: ")
        customer_name = self.get_str_input("Enter your name: ")
        duration = self.get_int_input("Fill the duration of renting (months): ")
        actual_duration = self.get_int_input("Fill the actual duration of renting (months): ")

        for land in self.lands:
            if land.kitta_number == kitta_number:
                area = land.area
                cost = land.cost

        if actual_duration > duration:
            print(return_land(self.lands, kitta_number))
            write_invoice_return_fined(kitta_number, area, customer_name, actual_duration, cost)
        else:
            print(return_land(self.lands, kitta_number))
            write_invoice_return(kitta_number, area, customer_name, actual_duration, cost)

        write_data(self.lands)

    def handle_display_land(self):
        display_land(self.lands)

    def run(self):
        while True:
            choice = self.display_menu()
            if choice == '1':
                self.handle_rent_land()
            elif choice == '2':
                self.handle_return_land()
            elif choice == '3':
                self.handle_display_land()
            elif choice == '4':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice, please enter value 1, 2, 3, or 4.")

if __name__ == "__main__":
    tp_nepal = TechnoPropertyNepal()
    tp_nepal.run()
