class Vehicle:
    def __init__(self):
        self.vehicle_type = ""

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self):
        self.year = ""
        self.make = ""
        self.model = ""
        self.doors = ""
        self.roof = ""

    def prompt_user_input(self):
        print("Enter car details:")
        self.vehicle_type = "car"
        self.year = input("Year: ")
        self.make = input("Make: ")
        self.model = input("Model: ")
        self.doors = input("Number of doors (2 or 4): ")
        while self.doors not in ["2", "4"]:
            print("Invalid input. Please enter 2 or 4.")
            self.doors = input("Number of doors (2 or 4): ")
        self.roof = input("Type of roof (solid or sun roof): ")
        while self.roof not in ["solid", "sun roof"]:
            print("Invalid input. Please enter solid or sun roof.")
            self.roof = input("Type of roof (solid or sun roof): ")

    def display_car_info(self):
        print("\nCar Information:")
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)


def main():
    car = Automobile()
    car.prompt_user_input()
    car.display_car_info()


if __name__ == "__main__":
    main()