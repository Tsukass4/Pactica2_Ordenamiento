# ==============================================================================
# 1. Ordenamiento por Inserción (Insertion Sort)
# ==============================================================================

def insertion_sort(lista):
    """
    Ordena una lista utilizando el algoritmo de Inserción.
    Construye la lista ordenada un elemento a la vez.
    """
    # Iteramos sobre la lista, comenzando desde el segundo elemento (índice 1)
    for i in range(1, len(lista)):
        # Guardamos el valor actual para insertarlo en la posición correcta
        valor_actual = lista[i]
        # Inicializamos la posición para la comparación
        posicion = i

        # Movemos los elementos de la sublista ordenada que son mayores que
        # valor_actual una posición a la derecha.
        while posicion > 0 and lista[posicion - 1] > valor_actual:
            # Desplazamos el elemento a la derecha
            lista[posicion] = lista[posicion - 1]
            # Movemos la posición de comparación a la izquierda
            posicion = posicion - 1

        # Insertamos el valor_actual en su posición correcta en la sublista ordenada
        lista[posicion] = valor_actual
    
    return lista

# Ejemplo de Uso
if __name__ == '__main__':
    datos = [64, 25, 12, 22, 11]
    print("Datos originales:", datos)
    lista_ordenada = insertion_sort(datos)
    print("Insertion Sort:", lista_ordenada)
