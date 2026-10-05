# Triángulo de Pascal

Proyecto en Python para generar e imprimir el triángulo de Pascal con un número determinado de filas.

## Descripción

Este repositorio contiene una implementación simple y clara del algoritmo del triángulo de Pascal. La aplicación permite:

- Generar una matriz triangular con los valores del triángulo de Pascal.
- Mostrar la salida centrada y formateada en consola.
- Validar la entrada para asegurar que el usuario ingrese un número positivo.

## Funcionalidad

El programa calcula cada fila del triángulo usando la relación:

- El primer y último valor de cada fila son `1`.
- Los valores internos se calculan como la suma de los dos números superiores.

## Requisitos

- Python 3.x

## Ejecución

1. Clona este repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta:

```bash
python triangulo_pascal.py
```

4. Ingresa la cantidad de filas que deseas generar.

## Ejemplo

```bash
Triángulo de Pascal
Ingresa el número de filas a generar: 6
```

Salida esperada:

```text
==================================================
 TRIÁNGULO DE PASCAL
==================================================

Triángulo de Pascal con 6 filas:

             1
           1    1
         1    2    1
       1    3    3    1
     1    4    6    4    1
   1    5   10   10    5    1
```

## Estructura del proyecto

```text
triangulopascal/
├── README.md
├── triangulo_pascal.py
├── LICENSE
```

## Autor

Proyecto desarrollado en Python para practicar la generación de patrones numéricos y la lógica de programación.
