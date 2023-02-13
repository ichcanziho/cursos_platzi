# Curso Práctico de Estructuras de Datos y Algoritmos

## Objetivos del curso

## Tabla de contenidos:

### 1. [Introducción a los algoritmos](#1-introducción-a-los-algoritmos)
### 2. [Algoritmos de ordenamiento](#2-algoritmos-de-ordenamiento)
### 3. [Recursividad](#3-recursividad)
### 4. [Divide and conquer and dynamic programming](#4-divide-and-conquer-and-dynamic-programming)
### 5. [Greedy Algorithms](#5-greedy-algorithms)
### 6. [Grafos y árboles](#6-grafos-y-árboles)
### 7. [¿Cómo comparar ALgoritmos?](#7-cómo-comparar-algoritmos)
### 8. [¿Qué sigue?](#8-qué-sigue)

# 1. Introducción a los algoritmos

## 1.1 ¿Qué entiende una computadora?

Las computadoras nacen de la necesidad humana de tener herramientas que le permitan eficientar procesos.
Los algoritmos son series de pasos que transforman variables de entrada (inputs) mediante una serie lógica 
de pasos en variables de salida (outputs).

La información digital es almacenada a través de código binario (0s y 1s) esto debido a que los procesadores de las computadoras
están compuestos principalmente de transistores, elementos electrónicos que permiten el flujo de la corriente, dejando pasar
o bloqueando el paso del mismo. A este dato binario (0/1) se le conoce en informática como Bit y es la unidad mínima de información
que puede ser manejada. El diferente acomodo de los transistores le permite a la computadora una amplia gama de habilidades, desde
el almacenaje de información hasta operaciones aritméticas. 

El sistema binario solo puede tener 2 posibles números para cada posición posible. Cada posición representa la potencia en 2 de es posición.
De tal modo que la posición 0 podría llegar a almacenar hasta 2**1 = 2 mientras que la posición 2 podría tener un valor de almacentamiento de 2**2 = 4.
El número en decimal sería entonces 2**n - 1

![binario](imgs/binario1.png)

Ejemplo de conversión de un número binario a uno decimal:

![binario2](imgs/binario2.png)

Mientras que el proceso de conversión de decimal a binario se basa en hacer divisiones entre 2
y anotar el módulo de la división ` (si la división es perfecta entonces su residuo es 0 de otro modo es 1) 

**¿Cómo se almacenan los textos en una computadora?**

Cada letra es almacenada numéricamente mediante un código llamado ASCII de tal forma que por ejemplo la letra: t tiene asociado
el valor 84, a su vez este valor es convertido a binario y esa es la representación binaria de la letra t.
Un documento es la concatenación de varias letras, y ya sabemos que cada letra es a su vez un número en binario.

Las imágenes a su vez son matrices bidimensionales donde cada celda contiene la información númerica de los componentes de color de cada pixel.
Para ello se ocupan los colores primarios Red Green Blue RGB y cada uno de ellos puede obtener un valor entre 0 y 255. La 
mezcla de estos colores forma el color único de cada pixel dentro de una imagen. 

![rgb](imgs/rgb.png)


## 1.2 Lenguajes de programación

Un lenguaje de programación es una forma de comunicarnos con una computadora, tablet o celular e indicarle qué queremos hacer.
Un lenguaje de programación es un lenguaje formal (o artificial, es decir, un lenguaje con reglas gramaticales bien definidas) que le proporciona a una persona, en este caso el programador, la capacidad de escribir (o programar) una serie de instrucciones o secuencias de órdenes en forma de algoritmos con el fin de controlar el comportamiento físico o lógico de un sistema informático,


El lenguaje máquina es directamente el que entiende una computadora y es directamente comunicado a través del sistema binario.

El lenjuage ensamblador consiste de un set de instrucciones que nos daba el fabricante del circuito integrado. Cada instrucción tenía una forma
de ser leía por el hardware del chip. El lenguaje ensamblador es sumamente eficiente, puesto que es un puente directo al CPU, pero no es muy
eficiente de leer e interpretar por humanos. 

![img](imgs/lp1.PNG)

Existen distintos tipos de lenguaje: principalmente de bajo nivel y de alto nivel. La diferencia se encuentra en lo cerca o lejos que estemos del hardware de nuestro equipo. Esta cercanía tiene que ver con el control que tengamos sobre el dispositivo, placa o controlador.

Encontramos diferentes lenguajes como C, C++, Java, PHP, Python, C#, ASP, entre otros.

## 1.3 Estructuras de datos

Cuando estamos resolviendo problemas a través de código será necesario en la mayoría de las ocasiones tener sistemas que nos permitan almacenar información. 
A esta forma ordenada, estructurada y eficiente de almacenar los datos es conocida como: estructura de datos. Generalmente, los lenguajes de programación
ya cuentan con varias estructuras de datos por defecto, entre las cuales podemos encontrar:

- Array
- Listas
- Listas enlazadas
- Árboles
- Grafos

Las estructuras de datos están divididas principalmente en dos grupos: `Lineales y no lineales`.

Lineales en dónde la información será guardará secuencialmente. No lineales como por ejemplo árboles, dónde se tiene un tronco principla y ramificaciones
que van surgiendo de este tronco, también podemos mencionar a los grafos que son puntos de información dispersos e interconectados entre sí.

A continuación mostraré varias estructuras de datos ejemplificados para solucionar esto:

![mapa](imgs/mapa1.PNG)

Yo Quiero llegar de mi casa a la escuela en la ruta más corta

Esto es una matriz de datos. La cual a su vez contiene lista de datos.


[
[1,0 CAFE], [1,1 COMD], [2,1 ESCL], 

[0,0 CASA], [1,0 NULL], [2,0 NULL], 

]

Esto es una **matriz de datos**
La cual a su vez contiene lista de datos

[

	[casa, cafe],
	
	[cafe,casa],
	
	[casa, comida],
	
	[comida,escuela],
	
	[casa,comida],
	
	[cafe,comida]

]

Esto es una
lista con índices

{

	casa:[0,0],
	
	cafe:[1,0],
	
	comd:[1,1],
	
	escl:[2,1]

}

**Mezcla de estructuras**

[

	ruta_1 [

		[casa, cafe],

		[cafe, comd],

		[comd, escl]

	],
	ruta_2 [
		[casa,comd],

		[comd,escl]
	]
]

## 1.4 Qué es un algoritmo?

Diferentes definiciones de Algoritmo

- **Algoritmo:** Conjunto ordenado de operaciones sistemáticas que permite hacer un cálculo y hallar la solución de un tipo de problema.
- **Algoritmo:** Se denomina algoritmo a un grupo finito de operaciones organizadas de manera lógica y ordenada que permite solucionar un determinado problema.
- **Algoritmo:** una serie de instrucciones o reglas establecidas que, por medio de una sucesión de pasos, permiten arribar a un resultado o solución.
- **Algoritmo:** una secuencia de instrucciones que representan un modelo de solución para determinado tipo de problemas. O bien como un conjunto de instrucciones que realizadas en orden conducen a obtener la solución de un problema.

### ¿Cómo se Diseña un Algoritmo?
En programación, un algoritmo establece, de manera genérica e informal, la secuencia de pasos o acciones que resuelve un determinado problema y, para representarlo, se utiliza, fundamentalmente, dos tipos de notación: pseudocódigo y diagramas de flujo.

### Partes de un Algoritmo
Todo algoritmo debe obedecer a la estructura básica de un sistema, es decir: entrada, proceso y salida.

### Características de los Algoritmos:
Las características fundamentales que debe cumplir todo algoritmo son:

1. Un algoritmo debe ser preciso e indicar el orden de realización de cada paso.

2. Un algoritmo debe estar definido. Si se sigue un algoritmo dos veces, se debe obtener el mismo resultado cada vez.

3. Un algoritmo debe ser finito. El algoritmo se debe terminar en algún momento; o sea, debe tener un número finito de pasos.

4. Un algoritmo debe ser legible: El texto que lo describe debe ser claro, tal que permita entenderlo y leerlo fácilmente.


## 1.5 Metodología para la construcción de un algoritmo

Pensar bien es hacerse buenas preguntas.

#### Definición del problema

- ¿Qué problema quiero resolver?
- ¿Qué resultado quiero lograr?
- ¿Qué quiero específicamente? Visualízalo

#### Análisis del problema

- ¿Qué necesito para alcanzar ese resultado?
- ¿Cómo obtengo eso que necesito?

#### Diseño del algoritmo

- Escribe el código paso a paso para alcanzar el resultado
- Verificación o pruebas

  - Conseguí el resultado:

    - ¿Es reutilizable, efectivo este código?
    - ¿Cómo lo puedo mejorar?
  - No conseguí el resultado:
    - Visualiza el paso a paso en tu mente (a veces da pereza lo es, a mí también pero hazlo)

#### Mejora del algoritmo
- ¿Qué me falta?
- ¿Qué hice mal?
- ¿Dónde está el error?
- ¿Qué necesito cambiar?

## 1.6 Variables y tipos de datos

- **Variables:** Nos sirven para almacenar los distintos tipos de datos.

- **Tipos de datos:** Así como en física contamos con las unidades de una magnitud en ciencia de la computación requiere saber qué tipo de variable va a ser trabajada.
En general te puedes encontrar con 2 tipos de datos:
  - **System-defined data types** (tipos de datos definidos por el sistema también conocidos como Primitivos)
  - **User-defined data types** (Tipos de datos definidos por el usuario).

![tipos_dato](imgs/tiposdato.png)
## 1.7 User defined data types

Uso de `User defined data types.` Cuando definimos un tipo de dato por nuestra cuenta, lo hacemos para hacer un mejor 
manejo de tipo de dato dentro de un proyecto, por ejemplo teniendo un proyecto basico tenemos muchos tipos de datos 
primitivos declarados los cuales son, int, float, char, etc. Bueno cuando se trabaja en proyectos grandes es 
un problema tener tantos datos primitivos, ya que seria practicamente una sopa de lo mismo por todos lados, entonces 
aquí es donde aplica el uso este tipo de datos, porque mediante a ellos podemos crear variables para definir el uso 
adecuado de la misma, como por ejemplo una variable para contador de la vida del personaje de un videojuego.

También existen el tipado estático y dinámico, en el estático el tipo de variable se conoce en el tiempo de compilación (compile-time) mientras que en el dinamico, se conoce en el tiempo de ejecuccion del programa(run-time).
Lenguajes de tipado estático: Java, C, C++, FORTRAN, Pascal, Scala
Lenguajes de tipado dinámico:JavaScript, Objective-C, PHP, Python, Ruby, Lisp,Tcl.

En Java, necesitas declarar el tipo de variable que es, antes de poder usarlo

## 1.8 Instalando Ubuntu Bash en Windows

Este curso se está haciendo desde Ubuntu 22, no ha sido necesario instalar ubuntu Bash.

Sin embargo, los pasos serían:

- Ir a actualizaciones y seguridad.
- Opciones de desarrollador
- Habilitar modo desarrollador
- Ir a panel de control
- Ir a programas
- Activar o desactivar características de Windows
- Aquí, busca la opción de “Windows Subsystem for Linux” y actívala, instala eso y permite que tu computadora se reinicie.

Luego, entra al menú inicio, escribe bash y sigue los pasos que te indique, en caso de que te diga que no tienes ninguna
distribución solo ve a la tienda de aplicaciones y descargaba Ubuntu para Windows.

![ubuntu](imgs/ubuntu.jpg)

Luego, ejecuta Ubuntu, crea tu usuario y contraseña y estás lista o listo para continuar.

![ubuntu](imgs/ubuntu2.jpg)

## 1.9 Creando nuestro user defined data type

[código completo de está clase](1_intro/1_user_define_data.py)

**Primer paso:** Definimos nuestro user defined data type utilizando una clase de python.
```python
class Clients:
	def __init__(self, name, client_id, credit, address):
		self.name = name
		self.client_id = client_id
		self.credit = credit
		self.address = address
```
**Segundo paso:** Para validar a nuestro UDDT  crearemos una función que reciba como parámetro de entrada un cliente y 
muestre su información por pantalla.

```python
def mostrar_cliente(cliente):
    print("*"*32)
    print("Nombre: ", cliente.name)
    print("Id: ", cliente.client_id)
    print("Crédito: ", cliente.credit)
    print("Dirección: ", cliente.address)
    print("*" * 32)
```

**Tercer paso:** Creamos nuestro punto de acceso y ejecutamos

```python
if __name__ == '__main__':
    usuario_a = Clients("Gabriel", "0000004", "1000000", "Xalapa, Veracruz")
    mostrar_cliente(cliente=usuario_a)
```
Ejecutar:

```bash
cd 1_intro
python3 1_user_define_data.py
```

Respuesta esperada:

```
********************************
Nombre:  Gabriel
Id:  0000004
Crédito:  1000000
Dirección:  Xalapa, Veracruz
********************************
```

## 1.10 Abstract Data Types básicos: Lists, Stacks, Queues

Muchas veces se confunden los **ADT (Abstract Data Types)** con las Estructuras de Datos.

Los `ADT` van a ser una representación de un set particular de comportamientos. Va a tener la capacidad de almacenar 
datos, pero además va a decirte cuál va a ser el comportamiento de los datos que tengas almacenados en él.

Un `stack (Una pila)` es una lista que implementa una política `LIFO`, Lifo significa `(Last In, First Out)` esto en 
español viene siendo Último en llegar, Primero en Salir. Un ejemplo de un stack puede estar siempre en tu día a día 
en el software, por ejemplo cuando utilizas el tabulador. 

Una estructura de datos va a ser una técnica o estrategia para implementar nuestro ADT.

De los tipos de datos abstractos más usados son: 
- Stack (o Pila que ya lo mencionábamos)
- Queue (Cola, este utiliza otro comportamiento que se llama `First in, First Out` la persona que llega al primero será 
la primera también en salir)
- Priority Queue (Cola de Prioridades, no es más que la misma cola, solo que el orden de entrada pasa a segundo término
y cada uno de los valores dentro del Queue va a tener asignado un peso o un valor que denote una importancia específica,
va a salir primero del Queue el que tenga mayor relevancia o importancia)
- Diccionarios (especie de lista que va a tener un índice)
- Trees (Árboles) 
- Graphs (Grafos).

[más información](https://www.geeksforgeeks.org/abstract-data-types/) 

#### Resumen

**Abstract Data Types (ADT) vs Data Structures (DS)**

- ADT
  - Representa un set particular de comportamientos
  - Es un tipo o clase para objetos cuyo comportamiento está definido por un conjunto de valores y un conjunto de operaciones
  - La definición de ADT solamente menciona que operaciones deben realizarse, pero no como estas operaciones serán implementadas
  - No se específica como los datos serán organizados en memoria y que algoritmos serán usados para implementar las operaciones
  - Por eso es llamado `Abstract`, nos da una vista independiente a la implementación.
  - **Ejemplo:**
    - Un stack es una lista que implementa una politica `Lifo` (last in firs out) en elementos agregados y eliminados.
    - Los valores pueden ser cualquier tipo > int, float, string etc
    - Las operaciones -> Apilar, Desapilar, is_empty
    - ADT comunes:
      - Stack
      - Queue
      - Priority Queue
      - Dict
      - Tree
      - Graphs
- DS
  - Es más concreta
  - Típicamente es una técnica o estrategia para implementar una ADT

  - **Ejemplo:**
    - Podemos usar una lista enlazada para implementar un stack
  - DS comunes:
    - Array
    - Linked List
    - Hash tables
    - Trees
## 1.11 Explicación gráfica Data Types Básicos

![lista](imgs/lista.png)

![stack](imgs/stack.png)

![queue](imgs/queue.png)


## 1.12 Glosario de funciones para Abstract Data Types

![ds](imgs/ds.jpg)

## 1.13 Creando tu primera Queue: Arrays

Problema:

Se necesita llevar el orden en el que en un restaurante llegan los clientes para poder atenderlos. El restaurante tiene
un cupo máximo de 5 personas y debe ser atendidos por orden de llegada.

Vamos a utilizar el Queue:

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|

La función DeQueue tiene como propósito remover y retornar el primer valor en la cola

| º  | 2 | 3 | 4 | 5 |
|----|---|---|---|---|

## 1.14 Creando tu primera Queue: Implementación.

Para crear una `Queue` debemos seguir los siguientes pasos:

1. Crear un pointer para saber que hay en front y rear
2. Colocar estos valores en -1 al inicializar
3. Incrementar en 1 el valor de “rear” cuando agregamos un elemento
4. Retornar el valor de front al quitar un elemento e incrementar en 1 el valor de front a usar dequeue.
5. Antes de agregar un elemento revisar si hay espacios
6. Antes de remover un elemento revisamos que existan elementos
7. Asegurarnos de que al remover todos los elementos resetear nuestro front y rear a -1

![queue](imgs/queue_python.jpg)

## 1.15 Creando tu primera Queue: Implementar la función enQueue

Crearemos una clase `MyQueue` dónde empezaremos creando una lista vacía de n elementos
y qué empiece el apuntador `rear` en -1
```python
class MyQueue:

    def __init__(self, queue_size: int = 5):
        self.queue = [0] * queue_size if queue_size != 0 else list()
        self.queue_size = queue_size
        self.rear = -1
```

Si el apuntador de la cantidad de elementos actual de la queue es igual al tamaño máximo del queue 
entonces la cola está llena, si no entonces procedemos a agregar dicho elemento a la siguiente posición
del queue.

```python
    def en_queue(self, value) -> None:
        if self.rear == self.queue_size - 1:
            print("la cola está llena")
        else:
            self.rear += 1
            self.queue[self.rear] = value
            print(f"Se ha añadido el valor: {value} - current queue: {self.queue}, rear {self.rear}")

```

## 1.16 Creando tu primera Queue: Implementar la función deQueue

Si la queue está en -1 es que está vacía, bien porque se acaba de crear, o porque se han eliminado elementos
hasta ya no tener ninguno. 

De otra forma, eliminamos siempre el primer elemento (puesto que la Queue es `FiFo`) y para conservar el largo
del arreglo añadimos un 0 al final del mismo. 

Finalmente, como hemos eliminado un elemento entonces disminuimos en 1 nuestro `rear`.

```python
    def de_queue(self) -> None:
        if self.rear == -1:
            print("la pila está vacia")
        else:
            print(f"Se ha eliminado el valor: {self.queue[0]}", end="")
            del self.queue[0]
            self.queue += [0]
            print(f" - current queue: {self.queue}, rear {self.rear}")
            self.rear -= 1
```

## 1.17 Creando tu primera: Queue: main code

[código completo](1_intro/2_queue.py)

Probemos nuestro código creando una instancia de nuestra clase `MyQueue` que tenga una capacidad máxima
de 5 elementos.

Probamos nuestros métodos `de_queue` y `en_queue` para eliminar y añadir elementos a la Queue

```python
if __name__ == '__main__':
    # Creando nuestro UDD 
    queue = MyQueue(5)
    # Probando el queue
    queue.de_queue()
    queue.en_queue(1)
    queue.en_queue(2)
    queue.de_queue()
    queue.de_queue()
    queue.de_queue()
    queue.en_queue(6)
    queue.en_queue(7)
    queue.en_queue(8)
    queue.en_queue(9)
    queue.de_queue()
    queue.de_queue()
    queue.de_queue()
    queue.en_queue(1)
    queue.en_queue(2)
```

Respuesta esperada:

``` commandline
la pila está vacia
Se ha añadido el valor: 1 - current queue: [1, 0, 0, 0, 0], rear 0
Se ha añadido el valor: 2 - current queue: [1, 2, 0, 0, 0], rear 1
Se ha eliminado el valor: 1 - current queue: [2, 0, 0, 0, 0], rear 1
Se ha eliminado el valor: 2 - current queue: [0, 0, 0, 0, 0], rear 0
la pila está vacia
Se ha añadido el valor: 6 - current queue: [6, 0, 0, 0, 0], rear 0
Se ha añadido el valor: 7 - current queue: [6, 7, 0, 0, 0], rear 1
Se ha añadido el valor: 8 - current queue: [6, 7, 8, 0, 0], rear 2
Se ha añadido el valor: 9 - current queue: [6, 7, 8, 9, 0], rear 3
Se ha eliminado el valor: 6 - current queue: [7, 8, 9, 0, 0], rear 3
Se ha eliminado el valor: 7 - current queue: [8, 9, 0, 0, 0], rear 2
Se ha eliminado el valor: 8 - current queue: [9, 0, 0, 0, 0], rear 1
Se ha añadido el valor: 1 - current queue: [9, 1, 0, 0, 0], rear 1
Se ha añadido el valor: 2 - current queue: [9, 1, 2, 0, 0], rear 2
```

# 2. Algoritmos de ordenamiento

## 2.1 Algoritmos de ordenamiento


## 2.2 Bubble sort

## 2.3 Bubble sort implementación

## 2.4 Bubble sort: main code

## 2.5 Insertion sort

## 2.6 Desafío: Implementa un algoritmo de ordenamiento

# 3. Recursividad

## 3.1 Recursividad

## 3.2 La función factorial, calculando el factorial recursivamente

## 3.3 Manejo de cadenas de caracteres

## 3.4 Arte: Generando arte recursivo

# 4. Divide and conquer and dynamic programming

## 4.1 Divide and conquer 

## 4.2 ¿Qué es la programación dinámica?

## 4.3 MergeSort

## 4.4 Desafío: Buscar el algoritmo más rápido de sort

## 4.5 Implementando QuickSort con Python

## 4.6 Implementando QuickSort con Python: main code

# 5. Greedy Algorithms

## 5.1 Qué son los greedy algorithm?

## 5.2 Ejercicio de programación greedy

## 5.3 Ejercicio de programación greedy: main code

# 6. Grafos y árboles

## 6.1 Grafos y sus aplicaciones

## 6.2 Árboles

# 7. ¿Cómo comparar Algoritmos?

## 7.1 ¿Cómo comparar algoritmos y ritmo de crecimiento?

# 8. ¿Qué sigue?

## 8.1 Cierre del curso y siguientes pasos

