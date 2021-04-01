from models import FilmEquipment
from models import FilmType
from models.enum_sort_order import SortOrder
from typing import List


class EquipmentManager:

    def __init__(self):
        self.equipment = []

    def add_equipment(self, item: FilmEquipment):
        self.equipment.append(item)

    def add_equipment(self, equipment: List[FilmEquipment]):
        self.equipment += equipment

    def search_by_film_type(self, film_type: FilmType):
        new_equipment_list = list()
        for item in self.equipment:
            if item.film_type == film_type:
                new_equipment_list.append(item)
        self.equipment = new_equipment_list
        return new_equipment_list

    def sort_by_price(self, order: SortOrder):
        self.equipment.sort(key=lambda item: item.price, reverse=bool(order.value))
        new_equipment_list = self.equipment
        return new_equipment_list

    def sort_by_installation_time(self, order: SortOrder):
        self.equipment.sort(key=lambda item: item.installation_time_in_days, reverse=bool(order.value))
        new_equipment_list = self.equipment
        return new_equipment_list
