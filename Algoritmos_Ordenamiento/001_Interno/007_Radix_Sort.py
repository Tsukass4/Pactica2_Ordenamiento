# ==============================================================================
# 7. RadixSort
# ==============================================================================

def _counting_sort_radix(lista, exp):
    """
    Función auxiliar de Ordenamiento por Conteo para RadixSort.
    Ordena la lista basándose en el dígito representado por 'exp'.
    """
    n = len(lista)
    # Lista de salida temporal
    salida = [0] * n
    # Array de conteo (para dígitos 0 a 9)
    conteo = [0] * 10

    # 1. Contar la frecuencia de cada dígito en la posición actual
    for i in range(n):
        # Obtener el dígito actual: (lista[i] // exp) % 10
        indice = (lista[i] // exp) % 10
        conteo[indice] += 1

    # 2. Modificar el array de conteo para que contenga la posición real
    # de este dígito en la lista de salida (acumulativo)
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # 3. Construir la lista de salida
    # Recorremos la lista original de atrás hacia adelante para mantener la estabilidad
    i = n - 1
    while i >= 0:
        # Obtener el dígito actual
        indice = (lista[i] // exp) % 10
        # Colocar el elemento en su posición correcta en la salida
        salida[conteo[indice] - 1] = lista[i]
        # Decrementar el conteo para el siguiente elemento con el mismo dígito
        conteo[indice] -= 1
        i -= 1

    # 4. Copiar la lista de salida a la lista original
    for i in range(n):
        lista[i] = salida[i]
        
    return lista

def radix_sort(lista):
    """
    Ordena una lista de números enteros no negativos utilizando el algoritmo de RadixSort.
    Funciona procesando dígitos individuales de derecha a izquierda (LSD Radix Sort).
    """
    if not lista:
        return []

    # 1. Encontrar el número máximo para saber cuántos dígitos procesar
    max_val = max(lista)
    
    # 2. Inicializar el exponente (exp) a 1 (para el dígito de las unidades)
    exp = 1
    
    # 3. Iterar mientras el exponente sea menor o igual al valor máximo
    while max_val // exp > 0:
        # Llamar a la función de ordenamiento por conteo (Counting Sort)
        # para ordenar la lista basada en el dígito actual (determinado por exp)
        lista = _counting_sort_radix(lista, exp)
        # Mover al siguiente dígito (decenas, centenas, etc.)
        exp *= 10
        
    return lista

# Ejemplo de Uso
if __name__ == '__main__':
    # RadixSort funciona mejor con enteros no negativos
    datos = [170, 45, 75, 90, 802, 24, 2, 66] 
    print("Datos originales:", datos)
    lista_ordenada = radix_sort(datos)
    print("RadixSort:", lista_ordenada)
