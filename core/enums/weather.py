# enums/weather.py

from enum import Enum, auto

class Weather(Enum):
    CLEAR_SKIES = auto()
    HARSH_SUNLIGHT = auto()
    RAIN = auto()
    SANDSTORM = auto()
    HAIL = auto()
    SNOW = auto()
    FOG = auto()
    EXTREMELY_HARSH_SUNLIGHT = auto()
    HEAVY_RAIN = auto()
    STRONG_WINDS = auto()
    