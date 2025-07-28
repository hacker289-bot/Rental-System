import csv

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
