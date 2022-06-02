from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        ph1 = PowerHardware(name, capacity, memory)
        System._hardware.append(ph1)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hv1 = HeavyHardware(name, capacity, memory)
        System._hardware.append(hv1)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)

        except IndexError:
            return "Hardware does not exist"

        except Exception as ex:
            return str(ex)

        # searched_hardware = [h for h in System._hardware if h.name == hardware_name][0]
        # if not searched_hardware:
        #     return "Hardware does not exist"
        # es1 = ExpressSoftware(name, capacity_consumption, memory_consumption)
        #
        # if searched_hardware.software_can_be_installed(es1):
        #     searched_hardware.install(es1)
        #     System._software.append(es1)
        # else:
        #     return "Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)

        except IndexError:
            return "Hardware does not exist"

        except Exception as ex:
            return str(ex)

        # searched_hardware = [h for h in System._hardware if h.name == hardware_name][0]
        # if not searched_hardware:
        #     return "Hardware does not exist"
        # ls1 = LightSoftware(name, capacity_consumption, memory_consumption)
        #
        # if searched_hardware.software_can_be_installed(ls1):
        #     searched_hardware.install(ls1)
        #     System._software.append(ls1)
        # else:
        #     print("Software cannot be installed")

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            h = [h for h in System._hardware if h.name == hardware_name][0]
            s = [s for s in System._software if s.name == software_name][0]
            h.uninstall(s)
            System._software.remove(s)

        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        result += f"Total Operational Memory: {sum([h.used_memory for h in System._hardware])} / {sum([h.memory for h in System._hardware])}\n"
        result += f"Total Capacity Taken: {sum([c.used_capacity for c in System._hardware])} / {sum([c.capacity for c in System._hardware])}"  # !!!!Check for the Slasch N
        return result

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            result += f"Hardware Component - {h.name}\n"
            express_software_components = [s for s in h.software_components if
                                           s.__class__.__name__ == "ExpressSoftware"]
            result += f"Express Software Components: {len(express_software_components)}\n"
            light_software_components = [s for s in h.software_components if
                                         s.__class__.__name__ == "LightSoftware"]
            result += f"Light Software Components: {len(light_software_components)}\n"
            result += f"Memory Usage: {sum([s.memory_consumption for s in h.software_components])} / {h.memory}\n"
            result += f"Capacity Usage: {sum([s.capacity_consumption for s in h.software_components])} / {h.capacity}\n"
            result += f"Type: {h.type}\n"
            result_names = ', '.join([n.name for n in h.software_components])
            result += f"Software Components: {result_names if result_names else None}"

        return result


# System.register_power_hardware("HDD", 200, 200)
# System.register_heavy_hardware("SSD", 400, 400)
# print(System.analyze())
#
# System.register_light_software("HDD", "Test", 0, 10)
# print(System.register_express_software("HDD", "Test2", 100, 100))
#
# System.register_express_software("HDD", "Test3", 50, 100)
# System.register_light_software("SSD", "Windows", 20, 50)
# System.register_express_software("SSD", "Linux", 50, 100)
# System.register_light_software("SSD", "Unix", 20, 50)
#
# print(System.analyze())
# System.release_software_component("SSD", "Linux")
#
# print(System.system_split())
