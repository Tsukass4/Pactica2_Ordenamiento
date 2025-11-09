# ==============================================================================
# 4. Ordenamiento de Árbol (Tree Sort)
# ==============================================================================

# Implementación usando un Árbol Binario de Búsqueda (BST)
class Nodo:
    """Clase auxiliar para representar un nodo del Árbol Binario de Búsqueda."""
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar_nodo(raiz, valor):
    """Inserta un nuevo valor en el BST."""
    # Si la raíz es nula, creamos un nuevo nodo
    if raiz is None:
        return Nodo(valor)
    # Si el valor es menor, vamos a la izquierda
    if valor < raiz.valor:
        raiz.izquierda = insertar_nodo(raiz.izquierda, valor)
    # Si el valor es mayor o igual, vamos a la derecha
    else:
        raiz.derecha = insertar_nodo(raiz.derecha, valor)
    return raiz

def recorrido_inorden(raiz, lista_ordenada):
    """
    Realiza un recorrido In-Orden (izquierda, raíz, derecha) del BST.
    Este recorrido produce los elementos en orden ascendente.
    """
    if raiz:
        # 1. Recorrer subárbol izquierdo
        recorrido_inorden(raiz.izquierda, lista_ordenada)
        # 2. Visitar la raíz (agregar el valor a la lista)
        lista_ordenada.append(raiz.valor)
        # 3. Recorrer subárbol derecho
        recorrido_inorden(raiz.derecha, lista_ordenada)

def tree_sort(lista):
    """
    Ordena una lista utilizando el algoritmo de Ordenamiento de Árbol.
    Construye un BST y luego realiza un recorrido In-Orden.
    """
    if not lista:
        return []

    # 1. Construir el Árbol Binario de Búsqueda (BST)
    raiz = None
    for elemento in lista:
        # Insertamos cada elemento de la lista en el árbol
        raiz = insertar_nodo(raiz, elemento)

    # 2. Realizar el recorrido In-Orden para obtener la lista ordenada
    lista_ordenada = []
    recorrido_inorden(raiz, lista_ordenada)
    
    return lista_ordenada

# Ejemplo de Uso
if __name__ == '__main__':
    datos = [64, 25, 12, 22, 11, 90, 37]
    print("Datos originales:", datos)
    lista_ordenada = tree_sort(datos)
    print("Tree Sort:", lista_ordenada)
