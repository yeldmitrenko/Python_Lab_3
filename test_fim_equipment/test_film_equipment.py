import unittest
from managers.equipment_manager import EquipmentManager
from models.scenery import Scenery
from models.enum_film_type import FilmType
from models.enum_sort_order import SortOrder


class TestEquipmentManager(unittest.TestCase):

    def setUp(self) -> None:
        self.equipment_1 = Scenery(2, 56, 28, FilmType.HISTORICAL)
        self.equipment_2 = Scenery(3, 12, 3, FilmType.DOCUMENTARY)
        self.equipment = [self.equipment_1, self.equipment_2]

        self.manager = EquipmentManager()
        self.manager.add_equipment(self.equipment)

    def test_search_by_film_type(self):
        self.assertEqual(
            self.manager.search_by_film_type(FilmType.HISTORICAL), [self.equipment_1]
        )

    def test_sort_by_price(self):
        self.assertEqual(
           self.manager.sort_by_price(SortOrder.ASC), [self.equipment_2, self.equipment_1]
        )

    def test_sort_by_installation_time(self):
        self.assertEqual(
            self.manager.sort_by_installation_time(SortOrder.ASC), [self.equipment_2, self.equipment_1]
        )


class TestScenery(unittest.TestCase):

    def setUp(self) -> None:
        self.scenery = Scenery(2, 56, 28, FilmType.HISTORICAL)

    def test_str(self):
        self.assertEqual(
            str(self.scenery),
            f'price: {self.scenery.price}, installation_time_in_days: {self.scenery.installation_time_in_days},'
            f' type: {self.scenery.film_type}'
        )


if __name__ == '__main__':
    unittest.main()
