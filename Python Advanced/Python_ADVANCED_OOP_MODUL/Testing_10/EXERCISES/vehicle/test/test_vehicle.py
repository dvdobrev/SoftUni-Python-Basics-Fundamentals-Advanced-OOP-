""" check(make) the vehicle order as root order to work the import"""

from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 200)

    def test_check_init_initilization(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_check_capacity_unchanged_when_fuel_changed(self):
        self.assertEqual(50, self.vehicle.capacity)
        self.vehicle.fuel = 20
        self.assertEqual(50, self.vehicle.capacity)

    def test_if_fuel_not_enough__when_drive_car(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(49)

        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_fuel_is_enough_to_drive(self):
        self.vehicle.drive(5)
        self.assertEqual(43.75, self.vehicle.fuel)

    def test_if_refuel_fuel_is_too_much(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_success(self):
        self.vehicle.drive(5)
        self.vehicle.refuel(5)
        self.assertEqual(48.75, self.vehicle.fuel)

    def test_str_dunder(self):
        self.assertEqual("The vehicle has 200 horse power with 50 fuel left and 1.25 fuel consumption",
                         self.vehicle.__str__())


if __name__ == '__main__':
    main()
