from unittest import TestCase, main
from vehicle.project.vehicle import Vehicle


class TestVehicle(TestCase):
    FUEL = 100
    HORSEPOWER = 120
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSEPOWER)

    def test_vehicle_for_correct_values_at_initialization(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.HORSEPOWER, self.vehicle.horse_power)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_raises_error_when_fuel_is_not_enough(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(100)
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(error.exception))

    def test_drive_reduce_fuel_when_distance_is_reachable(self):
        distance = 50
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * distance
        self.vehicle.drive(distance)
        expected_result = self.FUEL - fuel_needed
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_drive_reduce_fuel_with_max_possible_distance(self):
        distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION
        self.vehicle.drive(distance)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_raises_error_when_capacity_overflows(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(self.vehicle.capacity + 1)

        self.assertEqual("Too much fuel", str(error.exception))

    def test_refuel_increases_fuel_in_the_car(self):
        fuel_amount = 20
        self.vehicle.fuel -= fuel_amount

        self.vehicle.refuel(fuel_amount)

        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_vehicle_str_returns_proper_string_message(self):
        actual_result = str(self.vehicle)
        expected = f"The vehicle has {self.HORSEPOWER} " \
                   f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"

        self.assertEqual(expected, actual_result)


if __name__ == "__main__":
    main()
