from pathlib import Path

RAW_DATA_FOLDER = Path("original_files")
DATA_FOLDER = Path("data")

BACKGROUND_KEY_TO_STRING = {
    "blue": "Lençol Azul",
    "gray": "Lençol Cinza",
    "lightblue": "Lençol Azul Claro",
}

ILLUMINATION_TO_STRING = {
    "day": "Dia",
    "night": "Noite",
    "day": "Dia",
    "night": "Noite",
}

ENVIRONMENT_TO_STRING = {
    "inside": "Em Casa",
    "outside": "Fora de Casa",
}

OBJECT_CODE_TO_CLASS = {
    "switch": 0,
    "blackkc": 1,
    "orangekc": 2,
    "d6": 3,
    "d20": 4,
    "bluebs": 5,
    "brownbs": 6,
    "watch": 7,
    "phone": 8,
    "mic": 9,
}

CLASS_TO_OBJECT_NAME = {
    0: "Switch",
    1: "Black Keycap",
    2: "Orange Keycap",
    3: "d6",
    4: "d20",
    5: "Blue Body Spray",
    6: "Brown Body Spray",
    7: "Watch",
    8: "Wireless Phone",
    9: "Microphone",
}

MAP_COLUMN_TO_CONVERTER = {
    "background": lambda x: BACKGROUND_KEY_TO_STRING[x],
    "illumination": lambda x: ILLUMINATION_TO_STRING[x],
    "environment": lambda x: ENVIRONMENT_TO_STRING[x],
    "label_numeric": lambda x: CLASS_TO_OBJECT_NAME[x],
    "label_code": lambda x: CLASS_TO_OBJECT_NAME[OBJECT_CODE_TO_CLASS[x]],
}

__all__ = [
    "RAW_DATA_FOLDER",
    "BACKGROUND_KEY_TO_STRING",
    "ILLUMINATION_TO_STRING",
    "ENVIRONMENT_TO_STRING",
    "OBJECT_CODE_TO_CLASS",
    "CLASS_TO_OBJECT_NAME",
    "MAP_COLUMN_TO_CONVERTER",
]
