'''
Model Class

Produces a set of cubes arranged based upon an input matrix of statevectors.

Usage: Make one model for each set of statevectors.
'''

import numpy as np
import pygame

from cube import Cube
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Model():

    def round_remove_zeroes(self, np_dict):
        for a,d in np.ndenumerate(np_dict):
            for k,v in d.items():
                d[k] = round(v, 5)

        new_dict = {}
        for a,d in np.ndenumerate(np_dict):
            for k,v in d.items():
                if v:
                    new_dict[k] = v

        return new_dict


    def layers(self, data):
        n = int(np.cbrt(len(data))**2) # take square of the cubic root to get size of 2D layer
        return np.array([[data[i:i+n]] for i in range(0, len(data), n)]) # array of layer slices

    def process_statevector(self, state):
        np_dict_all = self.round_remove_zeroes(np.array(state.probabilities_dict([8,7,6,5,4,3,2,1,0])))

        np_dict = self.round_remove_zeroes(np.array(state.probabilities_dict([8,7,6,5,4,3])))

        data = np.around(np.array(state.probabilities([8,7,6,5,4,3])), 5)
        data = self.layers(data)
    ## toggled to linearize data ##
        # data = np.array([np.reshape(data[i], (4,4)) for i in range(len(data))])
    ##                           ##
        data = np.reshape(data, (64,))
        return data

    # build and populate space

    def __init__(self, statevector): # currently used for a 4x4x4 walk space.
        self.data = self.process_statevector(statevector)
        self.cubes = []
        count = 0
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    self.cubes.append(Cube(i,j,k, size=self.data[count]/max(self.data)))
                    count += 1



    def show_cubes(self):
        for i in range(len(self.data)):
            cube = self.cubes[i]
            glBegin(GL_QUADS)
            for surface in cube.surfaces:
              x = 0
              for vertex in surface:
                x += 1

                if self.data[i] != 0:
                    glColor4f(
                        cube.colours[x][2]*(1/(self.data[i]/max(self.data))),
                        0,
                        cube.colours[x][0]*(self.data[i]/max(self.data)),

                        self.data[i])


                    glVertex3fv(cube.vertices[vertex])

            glEnd()
            if self.data[i] != 0:
                glBegin(GL_LINES)
                for edge in cube.edges:
                  for vertex in edge:
                      glVertex3fv(cube.vertices[vertex])

                glEnd()


    def display_model(self, title=None):
        pygame.init()
        display = (1400, 800)
        w = pygame.display.set_mode(display,DOUBLEBUF|OPENGL)

        if title:
            pygame.display.set_caption(title)
        gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)

        glTranslatef(-1, -1,-10)

        # Rotation for displaying static images
        # glRotatef(40, 1, -1, 1)
        # glRotatef(-10, 0, 1, 0 )

        import time
        start = time.time()
        
        
        while time.time() < start + 10:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
              

            glRotatef(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            self.show_cubes()

                
            pygame.display.flip()
        

            pygame.time.wait(10)
    
        pygame.quit()
            


# source for display protocol:
# https://replit.com/talk/share/3D-Cube-In-OpenGL-Python/12195
