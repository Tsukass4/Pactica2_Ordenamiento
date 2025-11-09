# ==============================================================================
# 6. MergeSort
# ==============================================================================

def merge_sort(lista):
    """
    Ordena una lista utilizando el algoritmo de MergeSort.
    Utiliza la estrategia de 'divide y vencerás' para dividir y luego fusionar.
    """
    if len(lista) > 1:
        # 1. Dividir: Encontrar el punto medio de la lista
        mitad = len(lista) // 2
        sublista_izquierda = lista[:mitad]
        sublista_derecha = lista[mitad:]

        # 2. Conquistar (recursión): Ordenar ambas mitades
        merge_sort(sublista_izquierda)
        merge_sort(sublista_derecha)

        # 3. Fusionar (Merge): Fusionar las dos sublistas ordenadas
        i = j = k = 0
        
        # Copiar datos de las sublistas temporales a la lista original (lista)
        while i < len(sublista_izquierda) and j < len(sublista_derecha):
            # Comparamos el elemento más pequeño de cada sublista
            if sublista_izquierda[i] < sublista_derecha[j]:
                lista[k] = sublista_izquierda[i]
                i += 1
            else:
                lista[k] = sublista_derecha[j]
                j += 1
            k += 1

        # Comprobar si quedan elementos en la sublista izquierda y copiarlos
        while i < len(sublista_izquierda):
            lista[k] = sublista_izquierda[i]
            i += 1
            k += 1

        # Comprobar si quedan elementos en la sublista derecha y copiarlos
        while j < len(sublista_derecha):
            lista[k] = sublista_derecha[j]
            j += 1
            k += 1
            
    return lista

# Ejemplo de Uso
if __name__ == '__main__':
    datos = [64, 25, 12, 22, 11, 90, 37]
    print("Datos originales:", datos)
    lista_ordenada = merge_sort(datos)
    print("MergeSort:", lista_ordenada)
