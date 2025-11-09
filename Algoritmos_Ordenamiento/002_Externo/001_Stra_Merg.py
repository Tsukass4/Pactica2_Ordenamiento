# ==============================================================================
# 8. Fusión Directa (Straight Merging) - Simulación Conceptual
#
# Algoritmo de ordenamiento externo. Simula el proceso de fusión de runs
# de longitud fija (comenzando en 1) que se duplica en cada pasada.
# ==============================================================================

import os
import random

# --- Funciones Auxiliares para Simulación de Archivos ---

def crear_archivo_datos(nombre_archivo, num_elementos=10):
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

def fusionar_dos_runs(run1, run2):
    """Fusión simple de dos runs ordenados en un nuevo run ordenado."""
    i = j = 0
    run_fusionado = []
    
    # Mientras haya elementos en ambos runs
    while i < len(run1) and j < len(run2):
        if run1[i] <= run2[j]:
            run_fusionado.append(run1[i])
            i += 1
        else:
            run_fusionado.append(run2[j])
            j += 1
            
    # Agregar los elementos restantes
    run_fusionado.extend(run1[i:])
    run_fusionado.extend(run2[j:])
    
    return run_fusionado

# --- Algoritmo Principal ---

def straight_merging(archivo_entrada, archivo_salida, archivos_trabajo=['T1.txt', 'T2.txt']):
    """
    Simula la Fusión Directa.
    Comienza con runs de longitud 1 y duplica la longitud en cada pasada.
    """
    print("--- Fusión Directa (Straight Merging) ---")
    
    # Paso 1: Distribución inicial de runs de longitud 1
    datos = leer_datos_archivo(archivo_entrada)
    if not datos:
        print("El archivo de entrada está vacío.")
        return []
        
    # Cada elemento es un run de longitud 1
    runs_iniciales = [[x] for x in datos]
    
    # Escribimos los runs iniciales en el primer archivo de trabajo
    escribir_runs_a_archivo(archivos_trabajo[0], runs_iniciales)
    
    longitud_run = 1
    pasada = 0
    
    while longitud_run < len(datos):
        pasada += 1
        print(f"\nPasada {pasada}: Longitud de Run = {longitud_run}")
        
        # Alternamos los archivos de entrada y salida
        archivo_entrada_pasada = archivos_trabajo[(pasada - 1) % 2]
        archivo_salida_pasada = archivos_trabajo[pasada % 2]
        
        runs_a_fusionar = leer_runs_de_archivo(archivo_entrada_pasada)
        runs_salida = []
        
        # Fusionamos pares de runs
        i = 0
        while i < len(runs_a_fusionar):
            run1 = runs_a_fusionar[i]
            # Tomamos el segundo run, si existe
            run2 = runs_a_fusionar[i + 1] if i + 1 < len(runs_a_fusionar) else []
            
            run_fusionado = fusionar_dos_runs(run1, run2)
            runs_salida.append(run_fusionado)
            
            # Avanzamos dos posiciones (un par de runs)
            i += 2
                
        # Escribimos los runs fusionados en el archivo de salida
        escribir_runs_a_archivo(archivo_salida_pasada, runs_salida)
        print(f"Runs fusionados en {archivo_salida_pasada}: {runs_salida}")
        
        # Duplicamos la longitud del run para la siguiente pasada
        longitud_run *= 2
        
    # El resultado final está en el último archivo de salida
    archivo_final = archivos_trabajo[(pasada) % 2]
    runs_finales = leer_runs_de_archivo(archivo_final)
    
    if runs_finales:
        resultado = runs_finales[0]
        # Escribimos el resultado final en el archivo de salida
        escribir_runs_a_archivo(archivo_salida, [resultado])
        print(f"\nResultado final escrito en {archivo_salida}: {resultado}")
        return resultado
    return []

# --- Ejemplo de Uso y Limpieza ---

if __name__ == '__main__':
    ARCHIVO_ENTRADA = 'datos_straight_merging.txt'
    ARCHIVO_SALIDA = 'datos_straight_merging_ordenados.txt'
    ARCHIVOS_TRABAJO = ['T1_sm.txt', 'T2_sm.txt']
    
    # Limpieza previa
    archivos_a_limpiar = [ARCHIVO_ENTRADA, ARCHIVO_SALIDA] + ARCHIVOS_TRABAJO
    for f in archivos_a_limpiar:
        if os.path.exists(f):
            os.remove(f)

    # Crear datos de entrada
    crear_archivo_datos(ARCHIVO_ENTRADA, num_elementos=10)
    
    # Ejecutar el algoritmo
    straight_merging(ARCHIVO_ENTRADA, ARCHIVO_SALIDA, ARCHIVOS_TRABAJO)
    
    # Limpieza final
    for f in archivos_a_limpiar:
        if os.path.exists(f):
            os.remove(f)
