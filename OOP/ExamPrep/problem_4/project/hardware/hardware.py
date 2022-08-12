from math import floor

from project.software.express_software import ExpressSoftware
from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = list()

    @property
    def used_memory(self):
        return sum(sw.memory_consumption for sw in self.software_components)

    @property
    def used_capacity(self):
        return sum(sw.capacity_consumption for sw in self.software_components)

    def install(self, software) -> None:
        free_memory = self.memory - self.used_memory
        free_capacity = self.capacity - self.used_capacity
        if software.memory_consumption <= free_memory and software.capacity_consumption <= free_capacity:
            self.software_components.append(software)
        else:
            raise Exception('Software cannot be installed')

    def uninstall(self, software: Software):
        self.__validate_software(software)

    def analyze(self):
        express_sw_num = len([sw for sw in self.software_components if isinstance(sw, ExpressSoftware)])
        light_sw_num = len(self.software_components) - express_sw_num

        retval = f"Hardware Component - {self.name}"
        retval += f'\nExpress Software Components: {express_sw_num}'
        retval += f'\nLight Software Components: {light_sw_num}'
        retval += f'\nMemory Usage: {self.used_memory} / {self.memory}'
        retval += f'\nCapacity Usage: {self.used_capacity} / {self.capacity}'
        retval += f'\nType: {self.hardware_type}'
        retval += f'\nSoftware Components: {self.list_software_components()}'
        return retval

    def list_software_components(self):
        if self.software_components:
            return f"{', '.join([sw.name for sw in self.software_components])}"
        return 'None'

    def __validate_capacity(self, software):
        if software.capacity_consumption <= self.capacity or software.memory_consumption <= self.memory:
            return software
        else:
            raise Exception("Software cannot be installed")

    def __validate_software(self, software):
        if software in self.software_components:
            self.software_components.remove(software)
