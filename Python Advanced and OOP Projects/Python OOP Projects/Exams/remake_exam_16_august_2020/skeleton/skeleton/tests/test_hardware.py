from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(TestCase):
    def setUp(self):
        self.h = Hardware("Test Hardware", "PowerHardware", 100, 200)
        self.s = Software("Test Software", "LightSoftware", 10, 20)

    def test_init(self):
        self.assertEqual("Test Hardware", self.h.name)
        self.assertEqual("PowerHardware", self.h.type)
        self.assertEqual(100, self.h.capacity)
        self.assertEqual(200, self.h.memory)
        self.assertEqual([], self.h.software_components)

    def test_install(self):
        self.h.install(self.s)
        self.assertEqual(1, len(self.h.software_components))

    def test_install_raises_exception(self):
        self.s2 = Software("Test2 Software", "LightSoftware", 1000, 2000)
        with self.assertRaises(Exception) as ex:
            self.h.install(self.s2)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_uninstall(self):
        self.h.install(self.s)
        self.h.uninstall(self.s)
        self.assertEqual(0, len(self.h.software_components))


if __name__ == '__main__':
    main()
