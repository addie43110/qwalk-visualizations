'''
Class o' cubes.
'''
import numpy as np

class Cube():

    def __init__(self, x, y, z, size=1): # (x,y,z) is cube position

        vert = np.array(( # cube vertices from origin
            (-1,-1,-1),
            (-1,-1, 1),
            (-1, 1,-1),
            (-1, 1, 1),
            ( 1,-1,-1),
            ( 1,-1, 1),
            ( 1, 1,-1),
            ( 1, 1, 1)
        )) * size/2

        self.colours = np.array((
            (0,0,0),
            (0,0,1),
            (0,1,0),
            (0,1,1),
            (1,0,0),
            (1,0,1),
            (1,1,0),
            (1,1,1)
        ))

        self.surfaces = np.array((
            (0, 4, 6, 2),
            (3, 2, 6, 7),
            (7, 6, 4, 5),
            (5, 1, 3, 7),
            (1, 0, 2, 3),
            (5, 4, 0, 1)
        ))

        self.edges = np.array((
            (5, 7),
            (1, 5),
            (0, 1),
            (7, 6),
            (2, 3),
            (4, 5),
            (2, 6),
            (0, 2),
            (7, 3),
            (6, 4),
            (4, 0),
            (3, 1)
        ))

        self.vertices = np.add(
            vert, np.array([
                    (x,y,z) for i in range(len(vert))
                ])
            )

# source for cube layout:
# https://replit.com/talk/share/3D-Cube-In-OpenGL-Python/12195
