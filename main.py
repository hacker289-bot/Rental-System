# main.py
from read import read_data, Land
from operation import rent_land, return_land, display_land
from write import write_data, write_invoice, write_invoice_return, write_invoice_return_fined

class Land:
    def __init__(self, kitta_number, area, direction, number, cost, availability):
        self.kitta_number = int(kitta_number)
        self.area = area
        self.direction = direction
        self.number = int(number)
        self.cost = int(cost)
        self.available = availability == 'Available'

def read_data():
    lands = []
    with open('data.txt', 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            kitta_number, area, direction, number, cost, availability = line.strip().split(',')
            lands.append(Land(kitta_number, area, direction, number, cost, availability))
    return lands

def display_land(lands):
    for land in lands:
        print(f"Kitta Number: {land.kitta_number}, Area: {land.area}, Direction: {land.direction}, "
              f"Number: {land.number}, Cost: {land.cost}, Availability: {'Available' if land.available else 'Not Available'}")

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
        return input("Enter a value as per your required: ")

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
                    print(f"Kitta Number: {land.kitta_number}, Area: {land.area}, Direction: {land.direction}, "
                          f"Number: {land.number}, Cost: {land.cost}, Availability: {'Available' if land.available else 'Not Available' }")

            kitta_number = self.get_int_input("Fill out the kitta number to be rent: ")
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
            write_invoice_return_fined(kitta_number, self.new_method(area), customer_name, actual_duration, cost)
        else:
            print(return_land(self.lands, kitta_number))
            write_invoice_return(kitta_number, area, customer_name, actual_duration, cost)

        write_data(self.lands)

    def new_method(self, area):
        return area

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
