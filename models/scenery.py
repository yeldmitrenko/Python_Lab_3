from .film_equipment import FilmEquipment
from .enum_film_type import FilmType


class Scenery(FilmEquipment):
    def __init__(self, amount: int, price: int, installation_time_in_days: int, film_type: FilmType):
        super().__init__(amount)
        self.price = price
        self.installation_time_in_days = installation_time_in_days
        self.film_type = FilmType(film_type)

    def __str__(self) -> str:
        return f'price: {self.price}, installation_time_in_days: {self.installation_time_in_days}, type: {self.film_type}'


