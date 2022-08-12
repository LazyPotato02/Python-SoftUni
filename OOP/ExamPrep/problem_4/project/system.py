from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = list()
    _software = list()

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name,capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name,capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.__check_hardware(hardware_name)
        if hardware is None:
            return "Hardware does not exist"
        software = ExpressSoftware(name,capacity_consumption, memory_consumption)
        try:
            hardware.install(software)
            System._software.append(software)
        except Exception:
            raise Exception("Software cannot be installed")

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.__check_hardware(hardware_name)
        if hardware is None:
            return "Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(software)
            System._software.append(software)
        except Exception:
            raise Exception("Software cannot be installed")

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        System.__validate_software_components(hardware_name, software_name)

    @staticmethod
    def analyze():
        mem_consumption = sum(sw.memory_consumption for sw in System._software)
        mem_capacity = sum(hw.memory for hw in System._hardware)
        space_consumption = sum(sw.capacity_consumption for sw in System._software)
        space_capacity = sum(hw.capacity for hw in System._hardware)
        retval = "System Analysis"
        retval += f'\nHardware Components: {len(System._hardware)}'
        retval += f'\nSoftware Components: {len(System._software)}'
        retval += f'\nTotal Operational Memory: {mem_consumption} / {mem_capacity}'
        retval += f'\nTotal Capacity Taken: {space_consumption} / {space_capacity}'
        return retval

    @staticmethod
    def system_split():
        retval = ''
        for hw in System._hardware:
            retval += hw.analyze() + '\n'
        return retval

    @classmethod
    def __check_hardware(cls, hardware_name):
        for hardware in cls._hardware:
            if hardware_name == hardware.name:
                return hardware
        return None

    @classmethod
    def __validate_software_components(cls, hardware_name, software_name):
        hardware = cls.__check_hardware(hardware_name)
        software = cls.__check_software(software_name)
        if hardware is None or software is None:
            return "Some of the components do not exist"
        hardware.uninstall(software)
        cls._software.remove(software)

    @classmethod
    def __check_software(cls, software_name):
        for software in cls._software:
            if software_name == software.name:
                return software
        return None
