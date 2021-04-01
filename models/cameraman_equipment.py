from film_equipment import FilmEquipment


class CameramanEquipment(FilmEquipment):
    def __init__(self, amount: int, max_workload: float, max_height: float):
        super().__init__(amount)
        self.max_workload = max_workload
        self.max_height = max_height


class Tripod(CameramanEquipment):
    def __init__(self, amount: int, max_workload: float, max_height: float, sections_number: int):
        super().__init__(amount, max_workload, max_height)
        self.sections_number = sections_number


class RailSystem(CameramanEquipment):
    def __init__(self, amount: int, max_workload: float, max_height: float, road_length: float):
        super().__init__(amount, max_workload, max_height)
        self.road_length = road_length
