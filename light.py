from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *
from math import pi, sin, cos

def mouse(button, state, x, y):
   global spin
   if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
       spin = (spin + 30) % 360
       glutPostRedisplay()

def rotate(key, x, y):
    if key == GLUT_KEY_RIGHT:
        glRotate(-5, 0, 1, 0)
    elif key == GLUT_KEY_LEFT:
        glRotate(5, 0, 1, 0)
    elif key == GLUT_KEY_UP:
        glRotate(5, 1, 0, 0)
    elif key == GLUT_KEY_DOWN:
        glRotate(-5, 1, 0, 0)


def draw_sphere(r, nx, ny, mx=0, my=0, mz=0):
    dnx = 1.0 / nx
    dny = 1.0 / ny
    glBegin(GL_QUAD_STRIP)
    piy = pi * dny
    pix = pi * dnx
    for iy in range(ny):
        diy = iy
        ay = diy * piy
        sy = sin(ay)
        cy = cos(ay)
        ty = diy * dny
        ay1 = ay + piy
        sy1 = sin(ay1)
        cy1 = cos(ay1)
        ty1 = ty + dny
        for ix in range(nx):
            ax = 2.0 * ix * pix
            sx = sin(ax)
            cx = cos(ax)
            x = r * sy * cx
            y = r * sy * sx
            z = r * cy
            tx = ix * dnx
            glNormal3f(x + mx, y + my, z + mz)
            glTexCoord2f(tx, ty)
            glVertex3f(x + mx, y + my, z + mz)
            x = r * sy1 * cx
            y = r * sy1 * sx
            z = r * cy1
            glNormal3f(x + mx, y + my, z + mz)
            glTexCoord2f(tx, ty1)
            glVertex3f(x + mx, y + my, z + mz)
    glEnd()


global ambient
global lightpos


def move_light(key, x, y):
    if key == GLUT_KEY_UP:
            lightpos[1] += 0.1

    elif key == GLUT_KEY_LEFT:
            lightpos[0] -= 0.1
    elif key == GLUT_KEY_RIGHT:
            lightpos[0] += 0.1
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)
    glutPostRedisplay()


def light():
    global ambient
    global lightpos
    ambient = (1.0, 1.0, 1.0, 1)
    lightpos = [0, 0, 1, 0]
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)


def show():
    white = (1.0, 1.0, 1.0)
    black = (0, 0, 0)
    red = (0.5, 0.0, 0.0)
    glClearColor(*black, 0.0)
    glClear(GL_COLOR_BUFFER_BIT or GL_DEPTH_BUFFER_BIT)
    glColor3f(*red)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, red)
    draw_sphere(0.7, 100, 100)
    glFlush()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("light")
    glutDisplayFunc(show)
    glutIdleFunc(show)
    glutSpecialFunc(move_light)
    # glutSpecialFunc(rotate)
    #glutMouseFunc(mouse)
    light()
    glutMainLoop()


if __name__ == '__main__':
    main()