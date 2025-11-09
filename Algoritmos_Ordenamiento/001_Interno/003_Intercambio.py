# ==============================================================================
# 3. Ordenamiento por Intercambio (Bubble Sort)
# ==============================================================================

def bubble_sort(lista):
    """
    Ordena una lista utilizando el algoritmo de Intercambio (Burbuja).
    Compara repetidamente pares de elementos adyacentes y los intercambia si están en el orden incorrecto.
    """
    n = len(lista)
    # Bucle principal para controlar el número de pasadas
    for i in range(n - 1):
        # Bandera para optimización: si no hay intercambios en una pasada, la lista está ordenada
        intercambiado = False
        
        # Bucle interno para comparar y realizar intercambios
        # La última 'i' elementos ya están en su lugar correcto, por eso n - 1 - i
        for j in range(n - 1 - i):
            # Comparamos elementos adyacentes
            if lista[j] > lista[j + 1]:
                # Intercambiamos si el elemento actual es mayor que el siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        
        # Si no hubo intercambios en esta pasada, la lista ya está ordenada
        if not intercambiado:
            break
            
    return lista

# Ejemplo de Uso
if __name__ == '__main__':
    datos = [64, 25, 12, 22, 11]
    print("Datos originales:", datos)
    lista_ordenada = bubble_sort(datos)
    print("Bubble Sort (Intercambio):", lista_ordenada)
