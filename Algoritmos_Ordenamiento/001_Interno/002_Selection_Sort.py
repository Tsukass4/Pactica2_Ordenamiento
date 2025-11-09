# ==============================================================================
# 2. Ordenamiento por Selección (Selection Sort)
# ==============================================================================

def selection_sort(lista):
    """
    Ordena una lista utilizando el algoritmo de Selección.
    Encuentra el elemento mínimo y lo coloca al principio de la sublista no ordenada.
    """
    # Iteramos sobre toda la lista
    for i in range(len(lista)):
        # Asumimos que el elemento actual es el mínimo
        indice_minimo = i

        # Buscamos el elemento más pequeño en el resto de la lista no ordenada
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_minimo]:
                # Actualizamos el índice del elemento mínimo encontrado
                indice_minimo = j

        # Intercambiamos el elemento mínimo encontrado con el elemento en la posición 'i'
        # Esto coloca el elemento mínimo en la sublista ordenada
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    
    return lista

# Ejemplo de Uso
if __name__ == '__main__':
    datos = [64, 25, 12, 22, 11]
    print("Datos originales:", datos)
    lista_ordenada = selection_sort(datos)
    print("Selection Sort:", lista_ordenada)
