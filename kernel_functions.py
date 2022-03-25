import matplotlib.pyplot as plt
import numpy
import math
from PIL import Image
from scipy import ndimage

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