# Procesamiento de Imágenes
## Introducción
## Intención
Este repositorio denominado como ImageProcessing, tiene como proposito el poder incorporar diversos conceptos relacionados con Visión Computacional por medio de Python integrando lo aprendido en la unidad de formación de nombre "Herramientas computacionales: el arte de la programación (Gpo 100)" con clave "TC1001S.100" con el equipo asignado en la misma unidad de formación.
Esto se realizó utilizando el lenguaje de programación python, así como la herramientas Git y Github para control de versiones.
## Modo de Trabajo e Integrantes
Los integrantes del equipo 4 son:
#### Marco Antonio Almazán Martínez A01769046
#### Ángel Nolasco Serrano A01365726
#### Alberto Navarrete Ramírez A01422954

El modo de trabajo fue totalmente virtual haciendo uso de reuniones en zoom y de github para el control de versiones en el código. Por otro lado, la división del trabajo fue equitativa, ya que cada miembro del equipo realizó un kernel para aplicar los filtros correspondientes a cada imagen.
## Descripción del Entregable
En este entregable podemos observar distintas integraciones de Modelos de Machine learning utilizando modelación matricial convolucional para el manipulamiento de imágenes aplicando 3 Kernels distintos:

    - Gaussian Blur (Desenfoque Gaussiano)
    - Ricker Wavelet (Mexican Hat)
    - Shaarpen Function (Laplace)

Para poder demostrar la aplicación de estos modelos de procesamiento de imagenes, se utilizaron distintas librerias dentro de python como: Pillow, scipy, matplotlib, numpy y math; las cuales son librerias relacionadas con matemáticas y manipulación de matrices.
## ¿Qué es Convolución y su Descripción?
En imágenes, se le conoce como convolución al tratamiento de una matríz por otra. La imagen es representada por una matríz, al igual que
el kernel a utilizar. Normalmente se utiliza en procesamiento de imágenes para la aplicación de filtros y efectos visuales 
## ¿Qué es Kernel y su Descripción?
En el procesamiento de imágenes un concepto muy utilizado es el de "Kernel", este significa núcleo más especificamente podemos describir al "Kernel" como una matriz de valores que es usada para el desenfoque, enfoque, realce, detección de bordes, entre otros filtros que se aplican en las imágenes. Esto se logra realizando la convolución, la cuál previamente definimos, esta convolución es entre el kernel y la imagen, logrando así aplicar los filtros previamente mencionados.
## ¿Qué es Padding y su descripción?
Cuando se realiza el proceso de convolución, las imágenes pueden llegar a perder gran cantidad de pixeles en los bordes o margenes de la imagen en cuestión. Por lo tanto, para reducir o no presentar pérdidas mientras más capas se aplican, es agregar un padding incrementando el tamaño de la imagen con la finalidad de no perder ningún píxel.
## Funciones de Kernel utilizadas
Cómo previamente lo mencionamos el Kernel es una matriz que se usa para la aplicación de filtros en las imágenes, es por ello que para los diferentes filtros existen diferentes valores en las matrices, para ello se pueden utilizar funciones matemáticas que modelen cierto fenómeno que al ser múltiplicado por los píxeles de la imagen pueden producir diversos efectos. Como lo mencionamos anteriormente, se realizaron 3 filtros para el procesamiento de imágenes, en este caso utilizamos : gaussian blur (aplica el filtro de desenfoque), ricker wavelet(aplica la detección de bordes, mientras que desenfoca un poco el centro), sharpen (nitidez de la imagen). A continuación, se definen cada una de estas funciones a detalle.
### Gaussian Blur (Desenfoque Gaussiano)
El desenfoque gaussiano o gaussian blur consiste en la aplicación de una función matemática a una imagen con el fin de aplicar el filtro de desenfoque. Se llama desenfoque gaussiano, ya que la función matemática que lo realiza fue generada por el matemático y científico Carl Friedrich Gauss. La función matemática que modela este filtro en dos dimensiones esta dada por la siguiente función: 

                                  G(x,y) = (0.5 * (pi * sigma^2)) * exp(-(x^2 + y^2) / (2*sigma^2))

Finalmente, al realizar dicho efecto en python con la función previamente mencionada se obtiene el siguiente resultado, teniendo en cuenta una sigma con valor de 9 y un rango de valores para "x" y "y" desde -4 hasta 4. A continuación, se muestran la imágenes originales y la imágenes con el filtro aplicado para ver las diferencias.

#### Imágenes Originales
![sudoku](https://user-images.githubusercontent.com/57366623/160148671-61c91105-3d51-4586-8344-f7ba226baaed.jpg) 
![dogs](https://user-images.githubusercontent.com/57366623/160148765-ab0e3b9c-792a-44a2-a149-b27be12cdd17.png)

#### Imágenes con Filtro Aplicado
![image](https://user-images.githubusercontent.com/57366623/160152844-a1989c64-5b6c-44b4-8a24-3f0c56b6c993.png)
![image](https://user-images.githubusercontent.com/57366623/160152986-02dc293d-7a62-411d-9913-0ba17bd75976.png)

### Ricker Wavelet (Mexican Hat)
Ondícula de fase cero, la segunda derivada de la función gaussiana o la tercera derivada de la función de densidad de probabilidad normal. La ondícula de Ricker se utiliza a menudo en modelado y fabricación de sismogramas sintéticos. Tiene adaptaciones y usos para 2D y 3D. En términos de procesamiento de imagen, puede ser utilizada para técnicas de "feature point detection", "local area detection", etcétera
### Sharpen Function 
Esta función tiene como propóstio el encontrar diversas pareas en el cual cambiaron las imagenes de una manera rápida gracias a sus filtros de ruido los cuales presentan una sensibilidad alta.

#### Imágenes con Filtro Aplicado
![image](https://user-images.githubusercontent.com/58310509/160154670-e6f01707-f02c-40a7-ad3a-2add9c11edcd.png)
