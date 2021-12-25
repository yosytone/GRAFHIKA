from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *
from math import pi, sin, cos





def rotate(key, x, y):
    if key == GLUT_KEY_RIGHT:
        glRotate(-5, 0, 1, 0)
    elif key == GLUT_KEY_LEFT:
        glRotate(5, 0, 1, 0)
    elif key == GLUT_KEY_UP:
        glRotate(5, 1, 0, 0)
    elif key == GLUT_KEY_DOWN:
        glRotate(-5, 1, 0, 0)


angleHor = 20;
angleVert = 20;
dist = -2;
angleSpeed = 5;
distSpeed = 0.2;

def display():
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity();
	glRotatef(angleVert, 1, 0, 0)
	glRotatef(angleHor, 0, 1, 0)

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0, 0.922, 0.741)

	glBegin(GL_QUADS)

	glVertex3f(-0.5, -0.5, -0.5)
	glVertex3f(-0.5, 0.5, -0.5)
	glVertex3f(0.5, 0.5, -0.5)
	glVertex3f(0.5, -0.5, -0.5)

	glVertex3f(-0.5, -0.5, 0.5)
	glVertex3f(-0.5, 0.5, 0.5)
	glVertex3f(0.5, 0.5, 0.5)
	glVertex3f(0.5, -0.5, 0.5)

	glVertex3f(-0.5, -0.5, -0.5)
	glVertex3f(-0.5, 0.5, -0.5)
	glVertex3f(-0.5, 0.5, 0.5)
	glVertex3f(-0.5, -0.5, 0.5)

	glVertex3f(0.5, -0.5, -0.5)
	glVertex3f(0.5, 0.5, -0.5)
	glVertex3f(0.5, 0.5, 0.5)
	glVertex3f(0.5, -0.5, 0.5)

	glVertex3f(-0.5, -0.5, -0.5)
	glVertex3f(0.5, -0.5, -0.5)
	glVertex3f(0.5, -0.5, 0.5)
	glVertex3f(-0.5, -0.5, 0.5)

	glEnd()

	glBegin(GL_TRIANGLES)

	glVertex3f(-0.5, 0.5, -0.5)
	glVertex3f(0.5, 0.5, -0.5)
	glVertex3f(0, 0.75, -0.5)

	glVertex3f(-0.5, 0.5, 0.5)
	glVertex3f(0.5, 0.5, 0.5)
	glVertex3f(0, 0.75, 0.5)

	glEnd()

	glColor3f(0.361, 0.231, 0.016)

	glBegin(GL_QUADS)

	glVertex3f(0, 0.75, -0.5)
	glVertex3f(-0.6, 0.45, -0.5)
	glVertex3f(-0.6, 0.45, 0.5)
	glVertex3f(0, 0.75, 0.5)

	glVertex3f(0, 0.75, -0.5)
	glVertex3f(0.6, 0.45, -0.5)
	glVertex3f(0.6, 0.45, 0.5)
	glVertex3f(0, 0.75, 0.5)

	glVertex3f(-0.1, -0.5, 0.501)
	glVertex3f(-0.1, 0.1, 0.501)
	glVertex3f(-0.4, 0.1, 0.501)
	glVertex3f(-0.4, -0.5, 0.501)

	glVertex3f(0.1, -0.2, 0.501)
	glVertex3f(0.1, 0.2, 0.501)
	glVertex3f(0.4, 0.2, 0.501)
	glVertex3f(0.4, -0.2, 0.501)

	glVertex3f(-0.15, -0.2, -0.501)
	glVertex3f(-0.15, 0.2, -0.501)
	glVertex3f(0.15, 0.2, -0.501)
	glVertex3f(0.15, -0.2, -0.501)

	glVertex3f(-0.501, -0.2, -0.15)
	glVertex3f(-0.501, 0.2, -0.15)
	glVertex3f(-0.501, 0.2, 0.15)
	glVertex3f(-0.501, -0.2, 0.15)

	glVertex3f(0.501, -0.2, -0.15)
	glVertex3f(0.501, 0.2, -0.15)
	glVertex3f(0.501, 0.2, 0.15)
	glVertex3f(0.501, -0.2, 0.15)

	glEnd()

	glColor3f(0.702, 0.945, 1)

	glBegin(GL_QUADS);

	glVertex3f(0.13, -0.17, 0.502)
	glVertex3f(0.13, 0.17, 0.502)
	glVertex3f(0.37, 0.17, 0.502)
	glVertex3f(0.37, -0.17, 0.502)

	glVertex3f(-0.12, -0.17, -0.502)
	glVertex3f(-0.12, 0.17, -0.502)
	glVertex3f(0.12, 0.17, -0.502)
	glVertex3f(0.12, -0.17, -0.502)

	glVertex3f(-0.502, -0.17, -0.12)
	glVertex3f(-0.502, 0.17, -0.12)
	glVertex3f(-0.502, 0.17, 0.12)
	glVertex3f(-0.502, -0.17, 0.12)

	glVertex3f(0.502, -0.17, -0.12)
	glVertex3f(0.502, 0.17, -0.12)
	glVertex3f(0.502, 0.17, 0.12)
	glVertex3f(0.502, -0.17, 0.12)

	glEnd()

	glColor3f(0.71, 0.396, 0.263)


	glFlush()


def myinit():
	glEnable(GL_DEPTH_TEST)
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glFrustum(-1, 1, -1, 1, 1, 7)
	glTranslatef(0, 0, dist)





def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(0, 0);
    glutCreateWindow("House");
    glutDisplayFunc(display);
    myinit();

    glutSpecialFunc(rotate)

    glutMainLoop();




if __name__ == '__main__':
    main()