from random import *
from SeriousEx11 import is_inside

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    return [
            choice(['RED', 'BLUE', 'GREEN', 'YELLOW']),
            choice(['#C62828', '#4CAF50', '#FFD600', '#3F51B5']),
            randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    a = shapes[0]['rect']   #[20, 60, 100, 100]
    b = shapes[1]['rect']   #[140, 60, 100, 100]
    c = shapes[2]['rect']   #[20, 180, 100, 100]
    d = shapes[3]['rect']   #[140, 180, 100, 100]

