# ==============================================================================
# 5. QuickSort
# ==============================================================================

def quick_sort(lista):
    """
    Función principal para QuickSort.
    Utiliza la estrategia de 'divide y vencerás' de forma recursiva.
    """
    # Llamada a la función auxiliar que realiza el ordenamiento
    return _quick_sort_aux(lista, 0, len(lista) - 1)

def _quick_sort_aux(lista, inicio, fin):
    """Función auxiliar recursiva de QuickSort."""
    # Condición de parada: si el inicio es menor que el fin, hay elementos para ordenar
    if inicio < fin:
        # 1. Particionar: Obtener el índice del pivote después de la partición
        indice_pivote = _particion(lista, inicio, fin)
        
        # 2. Conquistar (recursión): Ordenar la sublista izquierda (elementos menores al pivote)
        _quick_sort_aux(lista, inicio, indice_pivote - 1)
        
        # 3. Conquistar (recursión): Ordenar la sublista derecha (elementos mayores al pivote)
        _quick_sort_aux(lista, indice_pivote + 1, fin)
    
    # Devolvemos la lista (ya ordenada in-place)
    return lista

def _particion(lista, inicio, fin):
    """
    Función de partición de QuickSort.
    Selecciona un pivote y reordena la sublista para que todos los elementos
    menores que el pivote estén a su izquierda y los mayores a su derecha.
    """
    # Seleccionamos el último elemento como pivote
    pivote = lista[fin]
    # 'i' es el índice del elemento más pequeño encontrado hasta ahora
    i = inicio - 1

    # Recorremos la sublista desde el inicio hasta el elemento anterior al pivote
    for j in range(inicio, fin):
        # Si el elemento actual es menor o igual al pivote
        if lista[j] <= pivote:
            # Incrementamos el índice del elemento más pequeño
            i = i + 1
            # Intercambiamos lista[i] y lista[j]
            lista[i], lista[j] = lista[j], lista[i]

    # Intercambiamos el pivote (lista[fin]) con el elemento en lista[i + 1]
    # Esto coloca el pivote en su posición final
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    
    # Devolvemos la posición final del pivote
    return i + 1

# Ejemplo de Uso
if __name__ == '__main__':
    datos = [64, 25, 12, 22, 11, 90, 37]
    print("Datos originales:", datos)
    lista_ordenada = quick_sort(datos)
    print("QuickSort:", lista_ordenada)
