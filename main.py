#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Lab 2

from gl import Render
from texture import *
from math import *
from vector import *
from shaders import *

r = Render()

r.glCreateWindow(1024, 1024)

r.glClearColor(0, 0, 0)

r.glClear()

r.lookAt(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))

#Modelos con Shaders
r.setShader(planet_shader)
r.loadModel('./sphere.obj', translate=[512, 512, 0], scale=[500, 500, 500], rotate=(0, 0, 0))

r.glFinish("Lab_2.bmp")