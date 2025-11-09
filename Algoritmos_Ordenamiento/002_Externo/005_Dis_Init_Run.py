# ==============================================================================
# 12. Distribución de Secuencias Iniciales (Distribution of Initial Runs) - Simulación Conceptual
#
# Esta es la fase inicial de la mayoría de los algoritmos de ordenamiento externo.
# Consiste en crear 'runs' (secuencias ordenadas) en memoria y distribuirlos
# en los archivos de trabajo externos.
# ==============================================================================

import os
import random

# --- Funciones Auxiliares para Simulación de Archivos ---

def crear_archivo_datos(nombre_archivo, num_elementos=20):
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

# --- Algoritmo Principal ---

def distribucion_inicial_runs(archivo_entrada, archivos_trabajo, tamano_memoria=5):
    """
    Simula la fase de Distribución de Secuencias Iniciales.
    """
    print("--- Distribución de Secuencias Iniciales ---")
    
    datos = leer_datos_archivo(archivo_entrada)
    if not datos:
        print("El archivo de entrada está vacío.")
        return []
        
    runs = []
    
    # 1. Creación de Runs (Ordenamiento Interno)
    print(f"Creando runs con un tamaño de memoria de {tamano_memoria} elementos...")
    for i in range(0, len(datos), tamano_memoria):
        # Leemos un bloque de datos que cabe en la "memoria"
        bloque = datos[i:i + tamano_memoria]
        # Ordenamos el bloque internamente (simulando QuickSort o HeapSort)
        bloque.sort()
        runs.append(bloque)
        
    print(f"Runs creados: {runs}")
    
    # 2. Distribución de Runs
    num_archivos = len(archivos_trabajo)
    archivos_runs = [[] for _ in range(num_archivos)]
    
    print(f"Distribuyendo runs en {num_archivos} archivos de trabajo...")
    for i, run in enumerate(runs):
        # Distribuimos los runs de forma alternada (Round-Robin)
        indice_archivo = i % num_archivos
        archivos_runs[indice_archivo].append(run)
        
    # Escribimos los runs distribuidos a los archivos de trabajo
    for i, nombre_archivo in enumerate(archivos_trabajo):
        escribir_runs_a_archivo(nombre_archivo, archivos_runs[i])
        print(f"Runs escritos en {nombre_archivo}: {archivos_runs[i]}")
        
    return archivos_runs

# --- Ejemplo de Uso y Limpieza ---

if __name__ == '__main__':
    ARCHIVO_ENTRADA = 'datos_distribucion.txt'
    ARCHIVOS_TRABAJO = ['D1.txt', 'D2.txt', 'D3.txt']
    
    # Limpieza previa
    archivos_a_limpiar = [ARCHIVO_ENTRADA] + ARCHIVOS_TRABAJO
    for f in archivos_a_limpiar:
        if os.path.exists(f):
            os.remove(f)

    # Crear datos de entrada
    crear_archivo_datos(ARCHIVO_ENTRADA, num_elementos=15)
    
    # Ejecutar el algoritmo
    distribucion_inicial_runs(ARCHIVO_ENTRADA, ARCHIVOS_TRABAJO, tamano_memoria=4)
    
    # Limpieza final
    for f in archivos_a_limpiar:
        if os.path.exists(f):
            os.remove(f)
