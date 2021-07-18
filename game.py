import coordinates
from coordinates import Coordinate

Coordinate.default_order = 'xy'


def squaredMap(screen_size):
    mapped_square = [
        {  # square1
            'min': Coordinate(0, 0),
            'max': Coordinate(screen_size['x'] / 3, screen_size['y'] / 3)
        },
        {  # square2
            'min': Coordinate(screen_size['x'] / 3, 0),
            'max': Coordinate(screen_size['x'] * 2 / 3, screen_size['y'] / 3)
        },
        {  # square3
            'min': Coordinate(screen_size['x'] * 2 / 3, 0),
            'max': Coordinate(screen_size['x'], screen_size['y'] / 3)
        },
        {  # square4
            'min': Coordinate(0, screen_size['y'] / 3),
            'max': Coordinate(screen_size['x'] / 3, screen_size['y'] * 2 / 3)
        },
        {  # square5
            'min': Coordinate(screen_size['x'] / 3, screen_size['y'] / 3),
            'max': Coordinate(screen_size['x'] * 2 / 3, screen_size['y'] * 2 / 3)
        },
        {  # square6
            'min': Coordinate(screen_size['x'] * 2 / 3, screen_size['y'] / 3),
            'max': Coordinate(screen_size['x'], screen_size['y'] * 2 / 3)
        },
        {  # square7
            'min': Coordinate(0, screen_size['y'] * 2 / 3),
            'max': Coordinate(screen_size['x'] / 3, screen_size['y'])
        },
        {  # square8
            'min': Coordinate(screen_size['x'] / 3, screen_size['y'] * 2 / 3),
            'max': Coordinate(screen_size['x'] * 2 / 3, screen_size['y'])
        },
        {  # square9
            'min': Coordinate(screen_size['x'] * 2 / 3, screen_size['y'] * 2 / 3),
            'max': Coordinate(screen_size['x'], screen_size['y'])
        },
    ]
    return mapped_square
