from film_equipment import FilmEquipment


class Camera(FilmEquipment):
    def __init__(self, amount: int, weight_in_grams: int, zoom: int, resolution: int):
        super().__init__(amount)
        self.weight_in_grams = weight_in_grams
        self.zoom = zoom
        self.resolution = resolution
