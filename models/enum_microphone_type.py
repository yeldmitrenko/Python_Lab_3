from enum import Enum, auto


class MicrophoneType(Enum):
    CONDENSER = auto()
    LAVALIER = auto()
    DYNAMIC = auto()
    GOOZE_NECK = auto()
