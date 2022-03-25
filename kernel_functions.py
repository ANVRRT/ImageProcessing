import matplotlib.pyplot as plt
import numpy
import math
from PIL import Image
from scipy import ndimage

# Funcion hecha por Marco Almazan
# La funcion gaussian_blur recibe como parametros el valor de sigma y el tamaño del rango que tendremos para la matriz.
# Finalmente, regresa la matriz con los valores calculados por la funcion.
def gaussian_blur(sigma, size):
    # Se declara una matriz de zeros del tamaño indicado.
    matrix = numpy.zeros((size,size))
    # Ciclos for para llenar la matriz de valores.
    for x in range(-(size//2), size//2 + 1):
        for y in range(-(size//2), size//2 + 1):
            # Se calculan los valores de la matriz mediante la funcion descrita en el readme.
            matrix[x][y] = (
                            0.5
                            *math.pi*(math.pow(sigma,2))
                            *math.exp(
                                -(
                                    (math.pow(x,2))
                                    +(math.pow(y,2))
                                )
                                /(
                                    2
                                    *(math.pow(sigma,2))
                                )
                                )
                            )
    # Se regresa la matriz con los valores del kernel para poder aplicar el efecto.
    return matrix

# Funcion hecha por Alberto Navarrete
def laplace_sharpen(kernel_size):
    M = numpy.zeros((kernel_size,kernel_size))
    M[kernel_size//2][kernel_size//2] = 8
    M[kernel_size//2 + 1][kernel_size//2] = -1
    M[kernel_size//2 - 1][kernel_size//2] = -1
    M[kernel_size//2][kernel_size//2 + 1] = -1
    M[kernel_size//2][kernel_size//2 - 1] = -1
    M[kernel_size//2 + 1][kernel_size//2 + 1] = -1
    M[kernel_size//2 + 1][kernel_size//2 - 1] = -1
    M[kernel_size//2 - 1][kernel_size//2 + 1] = -1
    M[kernel_size//2 - 1][kernel_size//2 - 1] = -1
    return M

def laplace_sharpen2(kernel_size):
    M = numpy.zeros((kernel_size,kernel_size))
    M[kernel_size//2][kernel_size//2] = 5
    M[kernel_size//2 + 1][kernel_size//2] = -1
    M[kernel_size//2 - 1][kernel_size//2] = 0
    M[kernel_size//2][kernel_size//2 + 1] = -1
    M[kernel_size//2][kernel_size//2 - 1] = 0
    M[kernel_size//2 + 1][kernel_size//2 + 1] = -1
    M[kernel_size//2 + 1][kernel_size//2 - 1] = 0
    M[kernel_size//2 - 1][kernel_size//2 + 1] = 0
    M[kernel_size//2 - 1][kernel_size//2 - 1] = -1
    return M