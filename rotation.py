import numpy as np

np.set_printoptions(precision=3, suppress=True)

def Rx(theta):
  return np.matrix([[      1      ,      0      ,      0      ],
                    [      0      , np.cos(theta), np.sin(theta)],
                    [      0      ,-np.sin(theta), np.cos(theta)]])

def Ry(theta):
  return np.matrix([[ np.cos(theta),      0      ,-np.sin(theta)],
                    [      0      ,      1      ,      0      ],
                    [ np.sin(theta),      0      , np.cos(theta)]])

def Rz(theta):
  return np.matrix([[ np.cos(theta),  np.sin(theta),     0      ],
                    [-np.sin(theta),  np.cos(theta),     0      ],
                  	[      0      ,      0       ,     1      ]])