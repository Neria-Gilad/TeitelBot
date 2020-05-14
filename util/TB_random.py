# this file exists so it will be simple to replace the randomness if needed
from random import choice


def tb_choice(list_of_anything):
    """
    :param list_of_anything: list of objects to choose from
    :return: one of the objects in the list
    """
    return choice(list_of_anything)
