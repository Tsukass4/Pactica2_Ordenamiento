# ==============================================================================
# 10. Fusión de Múltiples Vías Balanceada (Balanced Multiway Merging) - Simulación Conceptual
#
# Algoritmo de ordenamiento externo. Utiliza k archivos de entrada y k de salida
# para fusionar k runs a la vez (k-way merge).
# ==============================================================================

import os
import random
import heapq # Necesario para la fusión de múltiples vías

# --- Funciones Auxiliares para Simulación de Archivos ---

def crear_archivo_datos(nombre_archivo, num_elementos=15):
    """Crea un archivo con números enteros aleatorios, simulando el archivo de entrada."""
    with open(nombre_archivo, 'w') as f:
        datos = [str(random.randint(1, 100)) for _ in range(num_elementos)]
        f.write('\n'.join(datos) + '\n')

def leer_datos_archivo(nombre_archivo):
    """Lee todos los números enteros de un archivo."""
    try:
        with open(nombre_archivo, 'r') as f:
            datos = [int(line.strip()) for line in f if line.strip()]
        return datos
    except FileNotFoundError:
        return []

def escribir_runs_a_archivo(nombre_archivo, runs):
    """Escribe una lista de runs (secuencias ordenadas) a un archivo."""
    with open(nombre_archivo, 'w') as f:
        for run in runs:
            # Escribimos los elementos del run, separados por comas
            f.write(','.join(map(str, run)) + '\n')
            
def leer_runs_de_archivo(nombre_archivo):
    """Lee runs (secuencias ordenadas) de un archivo."""
    runs = []
    try:
        with open(nombre_archivo, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    # Convertimos la línea de texto (separada por comas) a una lista de enteros
                    run = [int(x) for x in line.split(',')]
                    runs.append(run)
        return runs
    except FileNotFoundError:
        return []

def fusionar_multiples_runs(runs):
    """Fusión de k runs ordenados (k-way merge) usando un min-heap."""
    
    # Inicializamos el heap con el primer elemento de cada run, junto con el índice del run y del elemento
    heap = []
    for i, run in enumerate(runs):
        if run:
            # (valor, índice_run, índice_elemento)
            heapq.heappush(heap, (run[0], i, 0))
            
    run_fusionado = []
    
    while heap:
        # Extraemos el elemento más pequeño del heap
        valor, run_idx, elem_idx = heapq.heappop(heap)
        run_fusionado.append(valor)
        
        # Si el run de donde vino el elemento tiene más elementos
        if elem_idx + 1 < len(runs[run_idx]):
            # Agregamos el siguiente elemento de ese run al heap
            siguiente_valor = runs[run_idx][elem_idx + 1]
            heapq.heappush(heap, (siguiente_valor, run_idx, elem_idx + 1))
            
    return run_fusionado

def distribucion_inicial_runs(datos, archivos_trabajo, tamano_memoria=5):
    """
    Crea runs ordenados internamente y los distribuye entre los archivos de trabajo.
    """
    runs = []
    
    # 1. Creación de Runs (Ordenamiento Interno)
    for i in range(0, len(datos), tamano_memoria):
        bloque = datos[i:i + tamano_memoria]
        bloque.sort()
        runs.append(bloque)
        
    # 2. Distribución de Runs
    num_archivos = len(archivos_trabajo)
    archivos_runs = [[] for _ in range(num_archivos)]
    
    for i, run in enumerate(runs):
        # Distribuimos los runs de forma alternada (Round-Robin)
        indice_archivo = i % num_archivos
        archivos_runs[indice_archivo].append(run)
        
    # Escribimos los runs distribuidos a los archivos de trabajo
    for i, nombre_archivo in enumerate(archivos_trabajo):
        escribir_runs_a_archivo(nombre_archivo, archivos_runs[i])
        
    return runs

# --- Algoritmo Principal ---

def balanced_multiway_merging(archivo_entrada, archivo_salida, k=3):
    """
    Simula la Fusión de Múltiples Vías Balanceada (k-way merge).
    """
    print(f"--- Fusión de Múltiples Vías Balanceada (k={k}) ---")
    
    # Archivos de trabajo: k de entrada (A) y k de salida (B)
    archivos_A = [f'A{i}_bmm.txt' for i in range(k)]
    archivos_B = [f'B{i}_bmm.txt' for i in range(k)]
    
    datos = leer_datos_archivo(archivo_entrada)
    if not datos:
        print("El archivo de entrada está vacío.")
        return []
        
    # Paso 1: Distribución inicial de runs
    runs_iniciales = distribucion_inicial_runs(datos, archivos_A, tamano_memoria=5)
    num_runs = len(runs_iniciales)
    
    pasada = 0
    
    # Alternamos entre los conjuntos de archivos A y B
    while num_runs > 1:
        pasada += 1
        print(f"\nPasada {pasada}: {num_runs} runs a fusionar.")
        
        # Determinamos los archivos de entrada y salida para esta pasada
        archivos_entrada = archivos_A if pasada % 2 != 0 else archivos_B
        archivos_salida = archivos_B if pasada % 2 != 0 else archivos_A
        
        # Leemos todos los runs de los archivos de entrada
        runs_entrada = []
        for nombre_archivo in archivos_entrada:
            runs_entrada.extend(leer_runs_de_archivo(nombre_archivo))
            
        runs_salida_distribuidos = [[] for _ in range(k)]
        
        # Fusionamos k runs a la vez y distribuimos el resultado
        i = 0
        j = 0 # Índice para distribuir en los archivos de salida
        num_runs = 0
        while i < len(runs_entrada):
            # Tomamos k runs para fusionar
            runs_a_fusionar = runs_entrada[i:i + k]
            
            # Realizamos la fusión de múltiples vías
            run_fusionado = fusionar_multiples_runs(runs_a_fusionar)
            
            # Distribuimos el run fusionado al archivo de salida 'j'
            runs_salida_distribuidos[j].append(run_fusionado)
            num_runs += 1
            
            i += k
            j = (j + 1) % k # Round-Robin para los archivos de salida
            
        # Escribimos los runs fusionados en los archivos de salida
        for idx, nombre_archivo in enumerate(archivos_salida):
            escribir_runs_a_archivo(nombre_archivo, runs_salida_distribuidos[idx])
            
    # El resultado final es el único run que queda
    archivo_final = archivos_A[0] if pasada % 2 == 0 else archivos_B[0]
    runs_finales = leer_runs_de_archivo(archivo_final)
    
    if runs_finales:
        resultado = runs_finales[0]
        escribir_runs_a_archivo(archivo_salida, [resultado])
        print(f"\nResultado final escrito en {archivo_salida}: {resultado}")
        return resultado
    return []

# --- Ejemplo de Uso y Limpieza ---

if __name__ == '__main__':
    ARCHIVO_ENTRADA = 'datos_bmm.txt'
    ARCHIVO_SALIDA = 'datos_bmm_ordenados.txt'
    K = 3
    ARCHIVOS_TRABAJO = [f'A{i}_bmm.txt' for i in range(K)] + [f'B{i}_bmm.txt' for i in range(K)]
    
    # Limpieza previa
    archivos_a_limpiar = [ARCHIVO_ENTRADA, ARCHIVO_SALIDA] + ARCHIVOS_TRABAJO
    for f in archivos_a_limpiar:
        if os.path.exists(f):
            os.remove(f)

    # Crear datos de entrada
    crear_archivo_datos(ARCHIVO_ENTRADA, num_elementos=15)
    
    # Ejecutar el algoritmo
    balanced_multiway_merging(ARCHIVO_ENTRADA, ARCHIVO_SALIDA, k=K)
    
    # Limpieza final
    for f in archivos_a_limpiar:
        if os.path.exists(f):
            os.remove(f)
