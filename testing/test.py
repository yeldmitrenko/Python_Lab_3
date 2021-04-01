from managers import EquipmentManager
from models import FilmType, Scenery
from models.enum_sort_order import SortOrder


class EquipmentTest:

    def __init__(self):
        pass

    def main(self) -> None:
        manager = EquipmentManager()
        manager.add_equipment([
            Scenery(2, 56, 28, FilmType.HISTORICAL),
            Scenery(3, 12, 3, FilmType.DOCUMENTARY),
            Scenery(6, 221, 64, FilmType.HISTORICAL)
        ])

        print('Unsorted:\n\t', '\n\t'.join([str(i) for i in manager.equipment]), '\n')
        print('Found by film type:\n\t', '\n\t'.join([str(i) for i in manager.search_by_film_type(FilmType.HISTORICAL)]), '\n')
        print('Sorted by price:\n\t', '\n\t'.join([str(i) for i in manager.sort_by_price(SortOrder.ASC)]), '\n')
        print('Sorted by installation time:\n\t', '\n\t'.join([str(i) for i in manager.sort_by_installation_time(SortOrder.ASC)]), '\n')
