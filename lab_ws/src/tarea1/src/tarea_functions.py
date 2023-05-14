import numpy as np
from copy import copy

cos=np.cos; sin=np.sin; pi=np.pi

def Trasl(x,y,z):
    T = np.array([[1, 0, 0, x],
                  [0, 1, 0, y], 
                  [0, 0, 1, z],
                  [0, 0, 0, 1]])
    return T

def Rotx(ang):
    Tx = np.array([[1, 0, 0, 0],
                   [0, np.cos(ang), -np.sin(ang), 0],
                   [0, np.sin(ang),  np.cos(ang), 0],
                   [0, 0, 0, 1]])
    return Tx

def Rotz(ang):
    Tz = np.array([[np.cos(ang), -np.sin(ang), 0, 0],
                    [np.sin(ang),  np.cos(ang), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    return Tz

def Roty(ang):
    Ty = np.array([[np.cos(ang), 0, np.sin(ang), 0],
                    [0, 1, 0, 0],
                    [-np.sin(ang),  0, np.cos(ang), 0],
                    [0, 0, 0, 1]])
    return Ty


def dh(d, theta, a, alpha):
    """
    Calcular la matriz de transformacion homogenea asociada con los parametros
    de Denavit-Hartenberg.
    Los valores d, theta, a, alpha son escalares.
    """
    # Escriba aqui la matriz de transformacion homogenea en funcion de los valores de d, theta, a, alpha
    cth = np.cos(theta);    sth = np.sin(theta)
    ca = np.cos(alpha);  sa = np.sin(alpha)
    T = np.array([[cth, -ca*sth,  sa*sth, a*cth],
                    [sth,  ca*cth, -sa*cth, a*sth],
                    [0,        sa,     ca,      d],
                    [0,         0,      0,      1]])
    return T
    
    

def fkine_kukakr6(q):
    """
    Calcular la cinematica directa del robot UR5 dados sus valores articulares. 
    q es un vector numpy de la forma [q1, q2, q3, q4, q5, q6]
    """
    # Longitudes (en metros)
    l1 = 0.4
    l2 = 0.025
    l3 = 0.455
    l4 = 0.035
    l5 = 0.420
    l6 = 0.08

    # Matrices DH (completar), emplear la funcion dh con los parametros DH para cada articulacion
    T1 = dh(l1, pi+q[0], l2, -pi/2)
    T2 = dh(0, q[1], l3, 0)
    T3 = dh(0, -pi/2+q[2], l4, pi/2)
    T4 = dh(-l5, q[3], 0, -pi/2)
    T5 = dh(0, q[4], 0, pi/2)
    T6 = dh(-l6, q[5], 0, pi)
    # Efector final con respecto a la base
    T = T1 @ T2 @ T3 @ T4 @ T5 @ T6
    return T

def geometric_kuka(q):
    """
    Calcular la cinematica directa del robot UR5 dados sus valores articulares, con el metodo geometrico. 
    q es un vector numpy de la forma [q1, q2, q3, q4, q5, q6]
    """
    # Longitudes (en metros)
    l1 = 0.4
    l2 = 0.025
    l3 = 0.455
    l4 = 0.035
    l5 = 0.420
    l6 = 0.08

    r = l6 * sin(q[4])
    

    """
    #Posicion del efector final
    pos = np.array([[l2*cos(q[0]) + l3*cos(q[1] + q[0]) + l5*cos(q[2] + q[0] + q[1]) + l6 * cos(q[4])],
                    [- l2*sin(q[0]) - r * sin(q[3] + q[0])],
                    [l1 - l3*sin(q[1]) - l5*sin(q[2]) + l4 - r * cos(q[3])],
                    ])
    
    """

    T1 = Rotx(-pi/2) @ Roty(q[0]) @ Trasl(l2, -l1, 0)
    T2 = Rotz(-pi/2 + q[1]) @ Trasl(0, l3, 0) 
    T3 = Rotx(pi/2) @ Roty(q[2]) @ Trasl(l4, 0, 0)
    T4 = Rotx(-pi/2) @ Roty(-q[3]) @ Trasl(0, l5, 0)
    T5 = Rotx(pi/2)
    T6 = Rotx(pi) @ Roty(-q[4]) @ Rotz(-q[5]) @ Trasl(0, 0, l6)
    T = T1 @ T2 @ T3 @ T4 @ T5 @ T6
    return T