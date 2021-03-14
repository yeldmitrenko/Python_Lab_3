from film_equipment import FilmEquipment
from enum_microphone_type import MicrophoneType
from enum_headphones import HeadphonesType


class AudioEquipment(FilmEquipment):
    def __init__(self, amount: int, brand: str = ''):
        super().__init__(amount)
        self.brand = brand


class Microphone(AudioEquipment):
    def __init__(self, amount: int, microphone_type: MicrophoneType, brand: str = ''):
        super().__init__(amount, brand)
        self.microphone_type = MicrophoneType(microphone_type)


class Headphones(AudioEquipment):
    def __init__(self, amount: int, headphones_type: HeadphonesType, brand: str = ''):
        super().__init__(amount, brand)
        self.headphones_type = HeadphonesType(headphones_type)
