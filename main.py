from utils import get_gas_price
from utils import get_kilowatt_price


class Car:
    def __init__(self, name: str, price: int, fuel_economy: float, service_cost: int):
        self.name = name
        self.price = price
        self.fuel_economy = fuel_economy  # l / 100km
        self.service_cost = service_cost

    def year_cost(self, mileage: int):
        return self.service_cost + self.fuel_cost(mileage)

    def total_cost(self, mileage: int, years: int):
        return self.price + years * self.fuel_cost(mileage)

    def fuel_cost(self, mileage: int):
        return mileage * self.fuel_economy / 100 * get_gas_price()

class ElectricCar(Car):
    def __init__(self, name: str, price: int, power_consumption: int, service_cost: int = 0):
        super().__init__(name, price, 0, service_cost)
        self.power_consumption = power_consumption #Wt / 1 km

    def fuel_cost(self, mileage: int):
        return mileage * self.power_consumption * get_kilowatt_price() / 1000


if __name__ == '__main__':
    toyota = Car('Toyota Corolla', price=25000, fuel_economy=10, service_cost=3000)

    prius = Car('Toyota Prius', price=60000, fuel_economy=3, service_cost=3000)

    tesla = ElectricCar('Tesla model 3', price=200000, power_consumption=150)

    for years in range(1, 100):
       toyota_cost = toyota.total_cost(10_000, years=years)
       prius_cost = prius.total_cost(10_000, years=years)
       tesla_coust = tesla.total_cost(10_000, years=years)
       if toyota_cost > prius_cost:
           print(f'Prius окупится за {years} лет')
           print(toyota_cost, prius_cost)
           break

