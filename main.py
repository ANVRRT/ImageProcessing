from PIL import Image
from scipy import ndimage
from kernel_functions import *

"""
    Se carga la imagen desde el archivo

    :parametro filename: El nombre y path del archivo a cargar.
    :regresa: La imagen cargada.
"""
def load_image(filename):
    Is = Image.open(filename)
    I = Is.convert('L')
    I = numpy.asarray(I)
    I = I / 255.0
    return I

# Padding para la imagen en cuestion
def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value

# La funcion plot_image muestra la imagen con el filtro aplicado
def plot_image(image, kernel, label,coord):
    modified_image = ndimage.convolve(image, kernel, mode='constant', cval=0.0)
    plt.subplot(2, 4, coord)
    plt.imshow(modified_image)
    plt.xlabel(label)
    
# Main del programa
if __name__ == "__main__":

    # Listas de las funciones del kernel y las imagenes
    kernel_list = [gaussian_blur(9, 9), mexican_hat(2, 9), laplace_sharpen(9), laplace_sharpen2(9)] #3
    kernel_label_list = ["Gaussian Blur", "Mexican Hat", "Sharpen","Sharpen2"]
    image_list = [load_image('Images/sudoku.jpg'), load_image('Images/dogs.png')]

    # Seccion para aplicar y mostrar el filtro en las imagenes.

    plt.figure(figsize = (30,30))
    x=1

    for i in range (0, len(image_list)):
        for j in range (0, len(kernel_list)):
            plot_image(image_list[i],kernel_list[j],kernel_label_list[j],x)
            x+=1
    
    plt.grid(False)
    plt.show()

