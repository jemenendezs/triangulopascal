"""
Triángulo de Pascal
"""

def generar_triangulo_pascal(n):
    """
    Genera el triángulo de Pascal hasta la fila n
    
    Args:
        n: Número de filas a generar
    
    Returns:
        Lista de listas representando el triángulo
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    for i in range(1, n):
        fila = [1]  # Cada fila empieza con 1
        for j in range(1, i):
            fila.append(triangle[i-1][j-1] + triangle[i-1][j])
        fila.append(1)  # Cada fila termina con 1
        triangle.append(fila)
    
    return triangle

def imprimir_triangulo(triangle):
    """
    Imprime el triángulo de Pascal con alineación perfecta
    
    Args:
        triangle: Lista de listas del triángulo de Pascal
    """
    for i, fila in enumerate(triangle):
        # Espacios para centrar la fila
        espacios = ' ' * (len(triangle) - i - 1) * 2
        
        # Convertir cada número a string y unir con espacios
        fila_str = ' '.join(f'{num:4}' for num in fila)
        
        # Imprimir la fila
        print(espacios + fila_str)


# Programa principal
if __name__ == "__main__":
    print("=" * 50)
    print(" TRIÁNGULO DE PASCAL")
    print("=" * 50)
    
    try:
        num_filas = int(input("\nIngresa el número de filas a generar: "))
        if num_filas <= 0:
            print("Debe ser un número positivo.")
        else:
            pascal = generar_triangulo_pascal(num_filas)
            print(f"\nTriángulo de Pascal con {num_filas} filas:\n")
            imprimir_triangulo(pascal)
    except ValueError:
        print("Por favor, ingresa un número válido.")
