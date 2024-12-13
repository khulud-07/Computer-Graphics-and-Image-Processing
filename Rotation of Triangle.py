import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def draw_axes():
    glColor3f(1.0, 1.0, 1.0)  # White color for axes
    glBegin(GL_LINES)
    glVertex2f(-10, 0)  # x-axis
    glVertex2f(10, 0)
    glVertex2f(0, -10)  # y-axis
    glVertex2f(0, 10)
    glEnd()


def basic_triangle(x1, y1, x2, y2, x3, y3):
    glColor3f(1.0, 0.0, 0.0)  # Red color for points
    glPointSize(5)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)  # (5, 4)
    glVertex2f(x2, y2)
   
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
   
    glVertex2f(x3, y3)
    glVertex2f(x1, y1)
    glEnd()


def rotated_triangle(x1, y1, x2, y2, x3, y3, angle_degrees):
    angle_radians = math.radians(angle_degrees)  # Convert angle to radians


    # Rotation formula for each vertex
    x1_rot = x1 * math.cos(angle_radians) - y1 * math.sin(angle_radians)
    y1_rot = x1 * math.sin(angle_radians) + y1 * math.cos(angle_radians)


    x2_rot = x2 * math.cos(angle_radians) - y2 * math.sin(angle_radians)
    y2_rot = x2 * math.sin(angle_radians) + y2 * math.cos(angle_radians)


    x3_rot = x3 * math.cos(angle_radians) - y3 * math.sin(angle_radians)
    y3_rot = x3 * math.sin(angle_radians) + y3 * math.cos(angle_radians)


    glColor3f(0.0, 0.0, 1.0)  # Blue color for the rotated triangle
    glBegin(GL_LINES)
    glVertex2f(x1_rot, y1_rot)
    glVertex2f(x2_rot, y2_rot)
    glVertex2f(x2_rot, y2_rot)
    glVertex2f(x3_rot, y3_rot)
    glVertex2f(x3_rot, y3_rot)
    glVertex2f(x1_rot, y1_rot)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
   
    draw_axes()
   
    basic_triangle(0, 0, 5, 2, 3, 3)
    rotated_triangle(0, 0, 5, 2, 3, 3, 80)
   
    glFlush()
    glutSwapBuffers()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -1, 1)
    glMatrixMode(GL_MODELVIEW)




glutInit()  # Initialize GLUT
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Plotting with PyOpenGL")
glEnable(GL_DEPTH_TEST)
glClearColor(0.0, 0.0, 0.0, 1.0)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
