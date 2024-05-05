class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descripition_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print("里程数： ", self.odometer_reading)

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("shit")

    def increment_odometer(self, mileage):
        self.odometer_reading += mileage
        return self.odometer_reading


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # self.battery_size = 40
        self.battery = Battery()

    # def describe_battery(self):
    #     print("This car has a " + str(self.battery_size) + " kwh battery.")


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " kwh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(range)


if __name__ == '__main__':
    # my_car = Car('Tesla', 'Tesla3', '2020')
    # print(my_car.get_descripition_name())
    # print(my_car.read_odometer())
    # my_car.odometer_reading = 20
    # print(my_car.read_odometer())
    # my_car.update_odometer(1000)
    # print(my_car.read_odometer())
    # my_car.increment_odometer(200)
    # print(my_car.read_odometer())

    my_leaf = ElectricCar('BYD', 'Song', '2024')
    print(my_leaf.odometer_reading)
    # print(my_leaf.describe_battery())
    print(my_leaf.battery.describe_battery())
    print(my_leaf.battery.get_range())

