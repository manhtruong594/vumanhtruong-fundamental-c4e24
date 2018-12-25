from random import *

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
        if (shapes[0]['rect'][2] + shapes[0]['rect'][0]) >= x >= shapes[0]['rect'][0] and (shapes[0]['rect'][3] + shapes[0]['rect'][1]) >= y >= shapes[0]['rect'][1]:
        if text == 'BLUE':
            return True 
        else:
            return False

    if (shapes[1]['rect'][2] + shapes[1]['rect'][0]) >= x >= shapes[1]['rect'][0] and (shapes[1]['rect'][3] + shapes[1]['rect'][1]) >= y >= shapes[1]['rect'][1]:
        if text == 'RED':
            return True 
        else:
            return False

    if (shapes[2]['rect'][2] + shapes[2]['rect'][0]) >= x >= shapes[2]['rect'][0] and (shapes[2]['rect'][3] + shapes[2]['rect'][1]) >= y >= shapes[2]['rect'][1]:
        if text == 'YELLOW':
            return True 
        else:
            return False

    if (shapes[3]['rect'][2] + shapes[3]['rect'][0]) >= x >= shapes[3]['rect'][0] and (shapes[3]['rect'][3] + shapes[3]['rect'][1]) >= y >= shapes[3]['rect'][1]:
        if text == 'GREEN':
            return True
        else:
            return False