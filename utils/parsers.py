# utils/parsers.py

import re
from utils.input import get_input

def choose_lead_pokemon():
    choice = get_input("")
    choice = " ".join(choice)
    indices = re.findall(r'\d+', choice)[:2]
    if len(indices) != 2:
        raise Exception("You need to pick exactly two indexes.")
    if len([int(index) for index in indices if 1 <= int(index) <= 3]) > 2:
        raise Exception("Incorrect values parsed in user choice.")
    return indices
