# Curso Profesional de Machine Learning con Scikit-Learn


Scikit-Learn es una biblioteca de Python que ofrece un conjunto de algoritmos eficientes que pueden ser utilizados para realizar Machine Learning en un ambiente productivo. Con el Curso Profesional de Machine Learning con SciKit-Learn de Platzi aprenderemos a implementar los principales algoritmos disponibles en esta biblioteca.

## Objetivos del curso

- Iniciar un proyecto con Scikit-Learn
- Aplicar técnicas de regularización a regresiones
- Manejar datos atípicos
- Reducir la dimensionalidad

---------------

## Tabla de contenidos:

- [1. Aprender los conceptos clave](#1-aprender-los-conceptos-clave)
- [2. Iniciar un proyecto con sklearn](#2-iniciar-un-proyecto-con-sklearn)
- [3. Optimización de features](#3-optimización-de-features)
- [4. Regresiones robustas](#4-regresiones-robustas)
- [5. Métodos de ensamble aplicados a clasificación](#5-métodos-de-ensamble-aplicados-a-clasificación)
- [6. Clustering](#6-clustering)
- [7. Optimización paramétrica](#7-optimización-paramétrica)
- [8. Salida a producción](#8-salida-a-producción)
- [Conclusiones](#conclusiones)

# 1. Aprender los conceptos clave

## 1.1 Introducción:

Scikit-learn es una herramienta desarrollada en 2007 por David Cournapeau como un proyecto del Google Summer of Code
nace en un entorno academico universitario, pero crece a convertirse en proyectos profesionales utilizados en la industria.

### ¿Por qué usar Scikit-learn?

- Curva de aprendizaje suave.
- Es una biblioteca muy versátil.
- Comunidad de soporte.
- Uso en producción.
- Integración con librerías externas.

### Conociendo Scikit Learn

![portada](./imgs/im1.png "portada")

- [Clasificación.](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
    - Identificar a cuál categoría pertenece un objeto.
- [Regresión.](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
  - Predecir el valor continuo asociado a un objeto. 
- [Clustering.](https://scikit-learn.org/stable/modules/clustering.html#clustering)
  - Agrupación automática de objetos con características similares dentro de conjuntos.
- [Preprocesamiento.](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing)
  - Extracción de características y normalizado de variables. 
- [Reducción de dimensionalidad.](https://scikit-learn.org/stable/modules/decomposition.html#decompositions)
  - Reducción del número de variables aleatorias a ser considerado. 
- [Selección del modelo.](https://scikit-learn.org/stable/model_selection.html#model-selection)
  - Comparación, validación y elección de parámetros y modelos.

![cheetsheet](./imgs/im2.png "cheetsheet")

### Preguntas que nos haremos y resolveremos en el curso:

- ¿Cómo nos ayuda Scikit Learn en el preprocesamiento de datos?
- ¿Qué modelos podemos utilizar para resolver problemas específicos?
- ¿Cuál es el procedimiento a seguir para poder optmizar los modelos?

## 1.2 ¿Cómo aprenden las máquinas?

Los datos lo son todo, entré mejor conocidos y analizados los tengamos será más fácil llegar a tener modelos más robustos.

Dependiendo de la naturaleza y estructura que tengas los datos será necesaria utilizar un enfoque diferente de machine learning. 
Los principales enfoques de machine learning que existen son: 

- Aprendizaje supervisado (Algoritmos **por observación**):
    - Si de los datos se puede extraer con anticipación información precisa del resultado que esperamos.
- Aprendizaje por refuerzo (Algoritmos **por prueba y error**):
  - Si de los datos no se puede sacar exactamente la información que queremos predecir, pero si podemos dejar que el modelo tome decisiones y evalue si estas decisiones son buenas o malas.
- Aprendizaje no supervisado (Algoritmos **por descubrimiento**):
  - Cuando no se tiene ninguna información adicional sobre lo que esperamos, sino que los datos por sí solos nos van a revelar información relevante sobre su propia naturaleza y estructura.

### Alternativas al Machine Learning dentro de la Inteligencia Artificial
**Algoritmos evolutivos**

Son una serie de algoritmos heuristicos, en donde, en tu espacio de soluciones se explora las mejores candidatos, según se optimice cierta función de costo. Por ejemplo, se usa en la industría automotriz o de diseño aeroespacial para encontrar el mejor diseño que minimice, por ejemplo, la resistencia al aire.

**Lógica Difusa**

Es una generalización de la lógica clásica, pero en lugar de tener solo dos condiciones (verdadero, falso) [principio de tercero excluido], se tienen condiciones de verdad continuas. Por ejemplo, si 1 representa verdadero, y 0 representa falso, en la lógica difusa, el grado de verdad ahora puede tomar valores en el intervalo continuo de [0, 1]. Este enfoque tenía mucho auge en sistemas de control y robotica, antes del auge de las redes neuronales.

**Agentes y Sistemas expertos**

Para sistemas cuyas propiedades se puede describir por la interacción de agentes, se utiliza este enfoque para encontrar o describir comportamientos en el colectivo. (Por ejemplo, los mercados financieros compuestos por agentes economicos, vendedores y compradores, etc). La física estadística y los sistemas complejos también se ayudan de este enfoque.

## 1.3 Problemas que podemos resolver con Scikit-learn

Algunas limitaciones de Scikit-learn

1. No es una herramienta de Computer Vision.
   - Se necesita complementar con una herramienta adicional tales como [OpenCV](https://opencv.org/) o [TorchVision](https://pytorch.org/docs/stable/torchvision/index.html) que forma parte del proyecto de Pytorch.
2. No se puede correr en GPUs.
3. No es una herramienta de estadística avanzada.
4. No es muy flexible en temas de Deep Learning.

### Qué problemas podemos abordar con Scikit-learn?

- **Clasificaciones**: Necesitamos etiquetar nuestros datos para que encajen en alguna de ciertas categorías previamente definidas.
  - Ejemplos:
    - ¿Es cáncer o no es cáncer?
    - ¿La imagen pertenece a un Ave, Perro o Gato?
    - ¿A qué segmento de clientes pertenece determinado usuario?

- **Regresión**: Cuando necesitamos modelar el comportamiento de una variable continua, dadas otras variables correlaciones
  - Ejemplos:
    - Predecir el precio del dólar para el mes siguiente.
    - El total de calorías de una comida dados sus ingredientes.
    - La ubicación más probable de determinado objeto dentro de una imagen.

- **Clustering**: Queremos descubrir subconjuntos de datos similares dentro del dataset. Queremos encontrar valores que se salen del comportamiento global.
  - Ejemplo:
    - Identificar productos similares para un sistema de recomendación.
    - Descubrir el sitio ideal para ubicar paradas de buses según la densidad poblacional.
    - Segmentar imágenes según patrones de colores y geometrías.

## 1.4 Las matemáticas que vamos a necesitar

La cortina de fondo: Varias técnicas que usamos para que los computadores aprendan están inspiradas en el mundo natural.

- Redes neuronales artificiales: Están inspiradas en el cerebro humano.
- Aprendizaje por refuerzo: Está inspirado en las teorías de la psicología conductual.
- Algoritmos evolutivos: Los teorías de Charles Darwin.

Temas matemáticos generales a repasar:

- Funciones y trigonométrica.
- Algebra lineal.
- Optimización de funciones.
- Calculo diferencial.

Temas de probabilidad y estadistica a repasar:

- Probabilidad básica.
- Combinaciones y permutaciones.
- Variables aleatorias y distribuciones.
- Teorema de Bayes.
- Pruebas estadísticas.

> - La conclusión es que si no tienes buenas bases de matemáticas, es muy difícil tener un “entendimiento real” de machine learning e inteligencia artificial. Serán como “cajas negras”.
>
> - La estrategia del curso será de desarrollo de software y ciencia de la computación.
> - Scikit Learn nos ayudará a cubrir algunos vacios conceptuales de una manera que beneficie a nuestro modelo.

# 2. Iniciar un proyecto con sklearn

# 3. Optimización de features

# 4. Regresiones robustas

# 5. Métodos de ensamble aplicados a clasificación

# 6. Clustering

# 7. Optimización paramétrica

# 8. Salida a producción

# Conclusiones

