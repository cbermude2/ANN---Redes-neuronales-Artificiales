*******************************************************
🧠 ANN - Redes Neuronales Artificiales
Tema 2: Componentes de red neuronal
*******************************************************
Práctica 1: Forward Pass Manual y Verificación de Trazabilidad
Definición del Escenario - Caso Spam: Imagina una red neuronal pequeña que recibe 2 características de un correo electrónico: frecuencia de palabras clave y presencia de caracteres especiales.
En l=1 tenemos: 
x = [0.8
     0.1]

W = [0.5   -0.2
     0.1    0.01]

b = [ 0.1
     -0.1]

Para l=2, tenemos:
W2=[0.7  −0.5]        
𝑏2=[0.2]

Arquitectura: Una capa oculta con l=2 neuronas, 
una capa de salida con 1 neurona, clasificación binaria

Activaciones: ReLU para la capa oculta y Sigmoide para la salida
