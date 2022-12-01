#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Lab 2

import random

def setColor(r, g, b):
    return bytes([int(b), int(g), int(r)])


def planet_shader(**kwargs):

    y = kwargs['x']
    x = kwargs['y']
    height = kwargs['height']
    width = kwargs['width']
    intensity = kwargs['intensity']

    x_1, y_1 = (width // 2), (height // 2)
    x_2, y_2 = ((x - x_1) / x_1), ((y - y_1) / y_1)
    distance = ((((x_2 ** 2) + (y_2 ** 2)) ** 0.5))

    factor = (1 - distance)
    if ((175 <= y <= 200) or (300 <= y <= 325) or (425 <= y <= 450) or (550 <= y <= 575) or (675 <= y <= 700) or (800 <= y <= 825)):
        r, g, b = round(221 * factor), round(167 * factor), round(113 * factor)
    elif ((200 <= y <= 225) or (275 <= y <= 300) or (450 <= y <= 475) or (525 <= y <= 550) or (700 <= y <= 725) or (775 <= y <= 800)):
        r, g, b = round(206 * factor), round(223 * factor), round(224 * factor)
    elif ((225 <= y <= 275) or (475 <= y <= 525)):
        r, g, b = round(229 * factor), round(119 * factor), round(63 * factor)
    else:
        r, g, b = round(248 * factor), round(188 * factor), round(125 * factor)

    return setColor(r * intensity, g * intensity, b * intensity)