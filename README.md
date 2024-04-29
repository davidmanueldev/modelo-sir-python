# Modelo SIR en Transmisión de Enfermedades | Scipy

![image](https://github.com/davidmanueldev/modelo-sir-python/assets/129340427/9eb5670b-8072-4c58-aa7f-f0f7c7844c43)

## Introducción

En nuestra perfección del proyecto que se esta presentando esta
abarcado en un desarrollo del 40 % en el lenguaje de codificación con
el desarrollo de nuestras herramientas para un modelado matematico
con la ayuda de E. D. que nos ayudaran a convertir las variables de
interes con respecto al tiempo, como la cantidad de infectados.
Implementado en Python nos permitira ingresar valores sobre la
enfermedad y la poblacion en cuestion, calcularemos el crecimiento
que este tiene podremos evaluar los escenarios, eventos clave y
estrategias de intervención para obtener un mejor control sobre este.

### Modelo Epidemiológico
Por la siglas S.I.R podremomos obtener lo siguiente:

S = Número de personas `susceptibles`

I = Número de personas `infectadas`

R = Número de personas `recuperadas`

α:Tasa de transición de susceptibles a infectados por unidad de tiempo. Representa la tasa a la que los individuos susceptibles se infectan cuando entran en contacto con individuos infectados.

β : Tasa de recuperación de
individuos infectados por unidad
de tiempo. Representa la tasa a la
que los individuos infectados se
recuperan y se convierten en
recuperados.

## Fórmula Usada

![image](https://puntoseguido.upc.edu.pe/wp-content/uploads/2020/04/dos.png)

## Librerías Utilizadas
* Numpy
  * NumPy es una biblioteca para el lenguaje de programación Python que da soporte para crear vectores y matrices grandes multidimensionales, junto con una gran colección de funciones matemáticas de alto nivel para operar con ellas. 
  
* Matplotlib
  * Matplotlib es una biblioteca para la generación de gráficos en dos dimensiones, a partir de datos contenidos en listas o arrays en el lenguaje de programación Python. Proporciona una API, pylab, diseñada para recordar a la de MATLAB
  
* Scipy
  * SciPy es una biblioteca de Python para matemáticas, ciencia e ingeniería. SciPy contiene módulos para optimización, álgebra lineal, integración, interpolación, funciones especiales, FFT, procesamiento de señales y de imagen, resolución de Ecuaciones Diferenciales Ordinarias (ODEs) y mucho más.


>[!important]Para ejecutar este código, necesitas tener instaladas las bibliotecas de SciPy y Matplotlib. Puedes instalarlas con pip install scipy matplotlib.