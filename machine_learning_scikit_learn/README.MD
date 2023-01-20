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

## 2.1 Configuración de nuestro entorno Python

En este curso estaremos haciendo uso de varias librerías complementarías de python. 
Es por eso que es buena idea no tener necesariamente la versión más actualizada de python desde la página oficial.
Esto se debe a que existe una versión por ejemplo Python 3.12 actualmente, las librerias que usaremos toman un tiempo
en adaptar su código a la verisón más reciente de python, y por temas de compatilibdad sería una mejor idea tener una
versión instalada menos reciente que ya haya sido completamente probada por nuestras otras dependencias, en este caso por
ejemplo python 3.10.

Para verificar la versión de python que tenemos instalada:

```bash
python --version
```

Primero actualicemos nuestra gestor de instalador de paquetes de python:

```bash
python3 -m pip install --upgrade pip
```

Para este proyecto estaremos utilizando entornos virtuales de python, para encapsular nuestros paquetes.
Para más información sobre entornos virtuales, consulta el siguiente repositorio de ayuda:

[Entornos virutales en python](https://github.com/ichcanziho/cursos_platzi/tree/master/pip_entornos_curso)

Primer paso: Instalación de virtualenv en python:

```bash
python3 -m pip install virtualenv
```

Creando el entorno virtual:

```bash
python3 -m virtualenv skl_env
```

Activando el entorno virtual:

```bash
source skl_env/bin/activate
```

Comprobando que es un entorno virgen:

```bash
pip freeze
```

Como no hemos instalado ninguna dependencia externa entonces el comando anterior
no debería haber regresado nada. 

## 2.1 Instalación de librerías en python:

Instalación de librerías:
```bash
pip install numpy
pip install scipy
pip install joblib
pip install pandas
pip install matplotlib
pip install seaborn
pip install scikit-learn
```

Creación del archivo de requirements.txt

```bash
pip freeze > requirements.txt
```

Verificando que sklearn está activo sin problemas.

```python
import sklearn
print(sklearn.__version__)
```

## 2.3 Datasets que usaremos en el curso

> [Datasets e informacion sobre ellos en el repo](datasets)

- [World Happiness Report](https://www.kaggle.com/unsdsn/world-happiness): Es un dataset que desde el 2012 recolecta variables sobre diferentes países y las relaciona con el nivel de felicidad de sus habitantes.

> **Nota: Este data set lo vamos a utilizar para temas de regresiones**

- [The Ultimate Halloween Candy Power Ranking](https://www.kaggle.com/fivethirtyeight/the-ultimate-halloween-candy-power-ranking): Es un estudio online de 269 mil votos de más de 8371 IPs deferentes. Para 85 tipos de dulces diferentes se evaluaron tanto características del dulce como la opinión y satisfacción para generar comparaciones. 

> **Nota: Este dataset lo vamos a utilizar para temas de clustering**

- [Heart disease prediction](https://www.kaggle.com/c/SAheart): Es un subconjunto de variables de un estudio que realizado en 1988 en diferentes regiones del planeta para predecir el riesgo a sufrir una enfermedad relacionada con el corazón. 

> **Nota: Este data set lo vamos a utilizar para temas de clasificación.**


# 3. Optimización de features

## 3.1 ¿Cómo afectan nuestros features a los modelos de Machine Learning?

El éxito o fracaso de nuestros proyectos de machine learning, dependerá en gran medida de la calidad de los datos de entrada
con los que serán entrenados los mismos.

**¿Qué son los features?** Son los atributos de nuestro modelo que usamos para realizar una interferencia o predicción. Son las variables de entrada.

Más features simpre es mejor, ¿verdad?
**La respuesta corta es: NO**

En realidad si tenemos variables que son irrelevantes pasarán estas cosas:

- Se le abrirá el paso al ruido.
- Aumentará el costo computacional.
- Si introducimos demasiados features y estos tienen valores faltantes, se harán sesgos muy significativos y vamos a perder esa capacidad de predicción.

> Nota: Hacer una buena selección de nuestro features, hará que nuestros algoritmos corran de una manera mas eficiente.

Una de las formas de saber que nuestros features han sido bien seleccionados es con el **sesgo (bias)** y la **varianza**.

- Una mala selección de nuestro features nos puede llevar a alguno de esos dos escenarios indeseados.

![varianzas-vs-sesgo](https://imgur.com/hyJhWFL.png)

> Nota: El sesgo (bias) es la diferencia que hay entre nuestras predicciones y los valores reales.
> Por otro lado, la varianza es la distancia entre diferentes predicciones que pertenecen a la misma clase.

Algo que debemos que recordar es que nuestro modelo de ML puede caer en uno de 2 escenarios que debemos evitar:

![over-under-balan](https://imgur.com/rWib1tG.png)

- **Underfitting**: Significa que nuestro modelo es demasiado simple, en donde nuestro modelo no está captando los features y nuestra variable de salida, por lo cual debemos de investigar variables con mas significado o combinaciones o transformaciones para poder llegar a nuestra variable de salida.

- **Overfitting**: Significa que nuestro modelo es demasiado complejo y nuestro algoritmo va a intentar ajustarse a los datos que tenemos, pero no se va a comportar bien con los datos del mundo real. Si tenemos overfiting lo mejor es intentar seleccionar los features de una manera mas critica descartando aquellos que no aporten información o combinando algunos quedándonos con la información que verdaderamente importa.

> - Cuando tenemos un sesgo (bias) alto lo que se hace es añadir mas features, aumentar el numero de datos no ayudara mucho.
> - Cuando tenemos un varianza (variance) alto lo que se hace es aumentar el numero de datos para que nuestro modelo generalice mejor.

**¿Qué podemos hacer para solucionar estos problemas?**

- Aplicar técnicas reducción de la dimensionalidad. Utilizaremos el algoritmo de PCA.
- Aplicar la técnica de la regulación, que consiste en penalizar aquellos features que no le estén aportando o que le estén restando información a nuestro modelo.
- Balanceo: Se utilizará Oversampling y Undersampling en problemas de rendimiento donde tengamos un conjunto de datos que está desbalanceado, por ejemplo en un problema de clasificación donde tenemos muchos ejemplos de una categoría y muy pocos de otra.

## 3.2 Introducción al Algoritmo PCA (Principal Component Analysis)

**¿Por qué usaríamos este algoritmo?**

- Porque en machine learning es normal encontrarnos con problemas donde tengamos una enorme cantidad de features en donde hay relaciones complejas entre ellos y con la variable que queremos predecir.

**¿Cuando utilizar un algoritmo PCA?**
- Nuestro dataset tiene un número alto de features y no todos sean significativos.
- Hay una alta correlación entre los features.
- Cuando hay overfiting.
- Cuando implica un alto coste computacional.

**¿En quŕ consiste el algoritmo PCA?**

Básicamente en reducir la complejidad del problema:

1. Seleccionando solamente las variables relevantes.
2. Combinándolas en nuevas variables que mantengan la información más importante (varianza de los features).

![pca](./imgs/im4.png "pca")

**¿Cuáles son pasos para llevar a cabo el algoritmo PCA?**

1. Calculamos la matriz de covarianza para expresar las relaciones entre nuestro features.
2. Hallamos los vectores propios y valores propios de esta matriz, para medir la fuerza y variabilidad de estas relaciones.
3. Ordenamos y escogemos los vectores propios con mayor variabilidad, esto es, aportan más información.

**¿Qué hacer si tenemos una PC de bajos recursos?**

- Si tenemos un dataset demasiado exigente, podemos usar una variación como IPCA.
- Si nuestros datos no tienen una estructura separable linealmente, y encontramos un KERNEL que pueda mapearlos podemos usar KPCA.

### Conceptos a tener en cuenta:

**varianza:** Es el promedio de la suma de los cuadrados de la distancia entre un elemento y su promedio.

![varianza](./imgs/im5.png "varianza")

¿Qué pasa cuando los puntos se encuentran en un plano bidimensional?

![varianza](./imgs/im6.png "varianza")

Para ello puedo obtener la varianza en cada uno de los ejes, y-varianza y la x-varianza.

Sin embargo, la varianza por sí mismo no es completamente determinante, pues puede haber conjuntos diferentes que tengan la misma varianza, 
veamos el siguiente ejemplo: 

![varianza](./imgs/im7.png "varianza")

Tanto el conjunto de la izquierda como el de la derecha tienen inclinaciones diferentes, pero en terminos de x-varianza y y-varianza son lo
mismo. Para lidiar con esta situación usaremos la covarianza.

La covarianza es el promedio del producto de las coordenadas:

![varianza](./imgs/im8.png "varianza")

De esta forma podemos distinguir que la distribución de puntos del lado izquierdo tiene una covarianza negativa y del lado derecho es positiva.

Otros terminos que debo investigar:
- Eigenvectors
- Eigenvalues

Para más información y recordar PCA [Explicación PCA](https://www.youtube.com/watch?v=7My_PBhxeP4&t=0s)


## 3.3 Preparación de datos para PCA e IPCA

Empezamos importando los librerias que vamos a utilizar:

```python
import pandas as pd
from scipy.sparse.construct import random
import sklearn
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA

from sklearn.linear_model import LogisticRegression

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
```

Lectura del dataset y separación entre los datos independientes (predictores) y dependientes (target)

```python
df_heart = pd.read_csv('./datasets/heart.csv')
print(df_heart.head(5))
# Guardamos nuestro dataset sin la columna de target
df_features = df_heart.drop(['target'], axis=1)
# Este será nuestro dataset, pero sin la columna
df_target = df_heart['target']
```
Valor esperado:

```
   age  sex  cp  trestbps  chol  fbs  ...  exang  oldpeak  slope  ca  thal  target
0   52    1   0       125   212    0  ...      0      1.0      2   2     3       0
1   53    1   0       140   203    1  ...      1      3.1      0   0     3       0
2   70    1   0       145   174    0  ...      1      2.6      0   0     3       0
3   61    1   0       148   203    0  ...      0      0.0      2   1     3       0
4   62    0   0       138   294    1  ...      0      1.9      1   3     2       0

```

Normalización de datos (paso indispensable para utilizar de forma correcta PCA) y creación de datos particiones
de entrenamiento y testing.

```python
# Normalizamos los datos
df_features = StandardScaler().fit_transform(df_features)

# Partimos el conjunto de entrenamiento.
# Para añadir replicabilidad usamos el random state
X_train, X_test, y_train, y_test = train_test_split(df_features,
                                                    df_target,
                                                    test_size=0.3,
                                                    random_state=42)

print(X_train.shape)
print(y_train.shape)
```
Valor esperado
```
[5 rows x 14 columns]
(717, 13)
(717,)
```

Nota sobre el funcionamiento de StandardScaler de Sklearn
```
# La estandarizacion que hace sklearn con StandardScaler es: 
z = (x - u) / s
x = valor
u = media
s = desviacion estandar
```
**Partimos el conjunto de entrenamiento.**

- `X` representa los features. Normalmente, es una matriz, por eso la mayúscula.
- `y` representa el target. Siempre es un vector, nunca una matriz, por eso la minúscula.

**Para añadir replicabilidad usamos el random state**

- `random_state` es para dejar estáticos los valores aleatorios que te genera, de forma que al volverlo a correr siga trabajando con esos valores aleatorios y no te genere nuevos valores aleatorios.

## 3.4 Implementación del Algoritmo PCA e IPCA

Empecemos por instanziar un modelo de clasificación que nos sirva para comparar el rendimiento de nuestros nuevos features utilizando PCA

```python
# Configuración de la regresión logística
logistic = LogisticRegression(solver='lbfgs')
```

Ahora entrenemos a nuestro algoritmo PCA con nuestros datos de entrada, algo importante a mencionar es que por defecto el número de componentes que utiliza
PCA es el mínimo entre la cantidad de muestras y la cantidad de features, pero en general nosotros buscamos tener un valor más pequeño que el número de features
de tener el mismo entonces no tendría mucho sentido usar PCA.

```python
# PCA
# Llamamos y configuramos nuestro algoritmo PCA
# El número de componentes es opcional
# Si no le pasamos el número de componentes lo asignará de esta forma:
# a: n_components = min(n_muestras, n_features)
pca = PCA(n_components=3)
# Entrenando algoritmo de PCA
pca.fit(X_train)
```

Ahora que nuestro algoritmo de PCA ha sido entrenado, debemos transformar nuestros datos de dependientes (X) de entrenamiento y validación utilizando PCA esto
para que el modelo de regresión logística NO utilice las 13 features originales, sino en este caso solamente 3. 

```python
# Configuramos los datos de entrenamiento con PCA
df_train = pca.transform(X_train)
df_test = pca.transform(X_test)
# Entrenamos la regresion logistica con datos del PCA
logistic.fit(df_train, y_train)
```

Finalmente, podemos observar cuál es el Accuracy de nuestro modelo.

```python
# Calculamos nuestra exactitud de nuestra predicción
print('Score/Accuracy PCA: ', logistic.score(df_test, y_test))
```

Valor esperado:
```
Score/Accuracy PCA:  0.7857142857142857
```

Ahora podemos repetir la metodología pero para IPCA y comparar los resultados:

```python
# IPCA
# Haremos una comparación con incremental PCA, haremos lo mismo para el IPCA.
# El parámetro batch se usa para crear pequeños bloques,
# de esta forma podemos ir entrenandolos poco a poco y combinarlos en el resultado final
ipca = IncrementalPCA(n_components=3, batch_size=10)
# Entrenando algoritmo de IPCA
ipca.fit(X_train)

# Configuramos los datos de entrenamiento con IPCA
df_train = ipca.transform(X_train)
df_test = ipca.transform(X_test)
# Entrenamos la regresion logistica con datos del IPCA
logistic.fit(df_train, y_train)
print('Score/Accuracy IPCA: ', logistic.score(df_test, y_test))
```
Valor esperado:
```
Score/Accuracy IPCA:  0.8051948051948052
```

### Bonus: Comparar el accuracy de PCA e IPCA utilizando diferentes valores en `n_components`

```python
# Bonus
max_features = X_train.shape[1]  # El máximo número de features en este caso sería de 13
pca_data = {'accuracy': [],
            'n_components': []}
ipca_data = {'accuracy': [],
             'n_components': []}
# PCA
print("I'm running PCA")
for n in range(1, max_features+1):
    pca = PCA(n_components=n)
    pca.fit(X_train)
    df_train = pca.transform(X_train)
    df_test = pca.transform(X_test)
    logistic.fit(df_train, y_train)
    acccuracy = logistic.score(df_test, y_test)
    print(f"PCA with n_componentes = {n} give us {acccuracy} Accuracy")
    pca_data['accuracy'].append(acccuracy)
    pca_data['n_components'].append(n)

# IPC
print("I'm running IPCA")
for n in range(1, max_features+1):
    ipca = IncrementalPCA(n_components=n, batch_size=max_features+1)
    ipca.fit(X_train)
    df_train = ipca.transform(X_train)
    df_test = ipca.transform(X_test)
    logistic.fit(df_train, y_train)
    acccuracy = logistic.score(df_test, y_test)
    print(f"IPCA with n_componentes = {n} give us {acccuracy} Accuracy")
    ipca_data['accuracy'].append(acccuracy)
    ipca_data['n_components'].append(n)

plt.plot(pca_data['n_components'], pca_data['accuracy'], label='PCA')
plt.plot(ipca_data['n_components'], ipca_data['accuracy'], label='IPCA')
plt.title('N Components vs Accuracy - PCA vs IPCA')
plt.xlabel('Number of Components')
plt.ylabel('Accuracy of Logistic-Regression')
plt.legend()

plt.savefig("resultados.png")
plt.show()
plt.close()
```

Respuesta esperada:

![resultados](./1_optimización_de_features/resultados.png "resultados")

> ## Resumen

**En esta sección lo que hicimos fue:**

1. Configuración de la regresión logística
2. PCA
- Llamamos y configuramos nuestro algoritmo PCA. El número de componentes es opcional. Si no le pasamos el número de componentes lo asignará de esta forma: n_components = min(n_muestras, n_features)
- Entrenando algoritmo de PCA
- Configuramos los datos de entrenamiento con PCA
- Entrenamos la regresión logística con datos del PCA
- Calculamos nuestra exactitud de nuestra predicción
3. IPCA
- Haremos una comparación con incremental PCA, haremos lo mismo para el IPCA. El parámetro batch se usa para crear pequeños bloques, de esta forma podemos ir entrenandolos poco a poco y combinarlos en el resultado final
- Mismos pasos a partir del 2 que para PCA.

> ## Conclusión
>
> El rendimiento de los dos algoritmos es casi exactamente el mismo, pero hay que considerar que nuestro dataset tenia 13 fetures originalmente para intentar predecir una clasificación binaria y utilizando PCA, solo tuvimos que utilizar 3 features artificiales que fueron los que nos   devolvió PCA para llegar a un resultado coste computacional y estamos utilizando información que es realmente relevante para nuestro modelo. Finalmente, la gráfica revela que el mejor resultado de 
> clasificación se obtiene con PCA utilizando únicamente 7 componentes, demostrando que es completamente posible que un modelo con menos features pueda obtener resultados iguales o incluso mejores que un modelo con mayor cantidad de features.

[Código completo de está sección](1_optimización_de_features/pca.py)

# 4. Regresiones robustas

# 5. Métodos de ensamble aplicados a clasificación

# 6. Clustering

# 7. Optimización paramétrica

# 8. Salida a producción

# Conclusiones

https://github.com/francomanca93/machine-learning-profesional-con-scikit-learn/blob/main/proyecto.md

