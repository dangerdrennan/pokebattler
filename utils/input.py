# utils/input.py

import sys

def quit_decorator(func):
    def wrapper(*args, **kwargs):
        choice = func(*args, **kwargs)
        if choice.lower() == 'q':
            print("Come back soon!")
            sys.exit()
        return choice
    return wrapper

@quit_decorator
def get_input(prompt: str):
    return input(prompt)
