# Procesamiento de Imágenes
## Introducción
## Intención
## Modo de Trabajo e Integrantes
Los integrantes del equipo 4 son:
Marco Antonio Almazán Martínez A01769046
Ángel Nolasco Serrano A01365726
Alberto Navarrete Ramírez A01422954

El modo de trabajo fue totalmente virtual haciendo uso de reuniones en zoom y de github para el control de versiones en el código. Por otro lado, la división del trabajo fue equitativa, ya que cada miembro del equipo realizó un kernel para aplicar los filtros correspondientes a cada imagen.
## Descripción del Entregable
## ¿Qué es Convolución y su Descripción?
## ¿Qué es Kernel y su Descripción?
En el procesamiento de imágenes un concepto muy utilizado es el de "Kernel", este significa núcleo más especificamente podemos describir al "Kernel" como una matriz de valores que es usada para el desenfoque, enfoque, realce, detección de bordes, entre otros filtros que se aplican en las imágenes. Esto se logra realizando la convolución, la cuál previamente definimos, esta convolución es entre el kernel y la imagen, logrando así aplicar los filtros previamente mencionados.
## ¿Qué es Padding y su descripción?
Cuando se realiza el proceso de convolución, las imágenes pueden llegar a perder gran cantidad de pixeles en los bordes o margenes de la imagen en cuestión. Por lo tanto, para reducir o no presentar pérdidas mientras más capas se aplican, es agregar un padding incrementando el tamaño de la imagen con la finalidad de no perder ningún píxel.
## Funciones de Kernel utilizadas
Cómo previamente lo mencionamos el Kernel es una matriz que se usa para la aplicación de filtros en las imágenes, es por ello que para los diferentes filtros existen diferentes valores en las matrices, para ello se pueden utilizar funciones matemáticas que modelen cierto fenómeno que al ser múltiplicado por los píxeles de la imagen pueden producir diversos efectos. Como lo mencionamos anteriormente, se realizaron 3 filtros para el procesamiento de imágenes, en este caso utilizamos : gaussian blur (aplica el filtro de desenfoque), ricker wavelet(aplica la detección de bordes, mientras que desenfoca un poco el centro), sharpen (nitidez de la imagen).
### Gaussian Blur (Desenfoque Gaussiano)
### Ricker Wavelet (Mexican Hat)
### Sharpen Function 
