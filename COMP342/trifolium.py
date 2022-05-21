# Import libraries
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import math

# Set the width and height of the window with global variables
# Set the axis range globally using global variable axrng
global width
global height
global axrng
global a, b

# Initial values
width = 600
height = 600
axrng = 1.0


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set clear color


def plotpolar():
    glClear(GL_COLOR_BUFFER_BIT)

    # Plot axis lines for reference
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-axrng, 0)
    glVertex2f(axrng, 0)
    glVertex2f(0, axrng)
    glVertex2f(0, -axrng)
    glEnd()

    # Set point size and smoothen it to a circle
    glPointSize(3.0)
    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Plot polar equation for Trifolium
    for degree in range(0, 180):
        radian = degree * math.pi / 180

        r = -b*cos(radian) + 4*a*cos(radian)*sin(radian)**2
        x = r * math.cos(radian)
        y = r * math.sin(radian)

        glColor3f(0.0, 0.5, 0.0)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

        glFlush()


if __name__ == "__main__":

    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))

    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(540, 100)
    glutInitWindowSize(width, height)
    glutCreateWindow("Trifolium")
    glutDisplayFunc(plotpolar)
    init()
    glutMainLoop()
