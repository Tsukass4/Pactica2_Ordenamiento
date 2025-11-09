# ==============================================================================
# 9. Fusión Natural (Natural Merging) - Simulación Conceptual
#
# Algoritmo de ordenamiento externo. Utiliza runs de longitud variable
# (runs naturales) en lugar de runs de longitud fija.
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

def obtener_runs_naturales(datos):
    """Identifica y extrae las secuencias ya ordenadas (runs naturales) de los datos."""
    runs = []
    if not datos:
        return runs
        
    run_actual = [datos[0]]
    for i in range(1, len(datos)):
        if datos[i] >= datos[i-1]:
            # El elemento actual es mayor o igual, continúa el run
            run_actual.append(datos[i])
        else:
            # El orden se rompe, el run actual termina
            runs.append(run_actual)
            run_actual = [datos[i]]
            
    # Agregar el último run
    runs.append(run_actual)
    return runs

# --- Algoritmo Principal ---

def natural_merging(archivo_entrada, archivo_salida, archivos_trabajo=['T1.txt', 'T2.txt']):
    """
    Simula la Fusión Natural.
    """
    print("--- Fusión Natural (Natural Merging) ---")
    
    # Paso 1: Distribución inicial de runs naturales
    datos = leer_datos_archivo(archivo_entrada)
    if not datos:
        print("El archivo de entrada está vacío.")
        return []
        
    runs_a_fusionar = obtener_runs_naturales(datos)
    
    # Escribimos los runs iniciales en el primer archivo de trabajo
    escribir_runs_a_archivo(archivos_trabajo[0], runs_a_fusionar)
    
    pasada = 0
    
    while len(runs_a_fusionar) > 1:
        pasada += 1
        print(f"\nPasada {pasada}: {len(runs_a_fusionar)} runs a fusionar.")
        
        # Alternamos los archivos de entrada y salida
        archivo_entrada_pasada = archivos_trabajo[(pasada - 1) % 2]
        archivo_salida_pasada = archivos_trabajo[pasada % 2]
        
        runs_a_fusionar = leer_runs_de_archivo(archivo_entrada_pasada)
        runs_salida = []
        
        # Fusionamos pares de runs
        i = 0
        while i < len(runs_a_fusionar):
            run1 = runs_a_fusionar[i]
            run2 = runs_a_fusionar[i + 1] if i + 1 < len(runs_a_fusionar) else []
            
            run_fusionado = fusionar_dos_runs(run1, run2)
            runs_salida.append(run_fusionado)
            
            i += 2
                
        # Escribimos los runs fusionados en el archivo de salida
        escribir_runs_a_archivo(archivo_salida_pasada, runs_salida)
        print(f"Runs fusionados en {archivo_salida_pasada}: {runs_salida}")
        
        runs_a_fusionar = runs_salida
        
    # El resultado final está en el último archivo de salida
    archivo_final = archivos_trabajo[(pasada) % 2]
    runs_finales = leer_runs_de_archivo(archivo_final)
    
    if runs_finales:
        resultado = runs_finales[0]
        escribir_runs_a_archivo(archivo_salida, [resultado])
        print(f"\nResultado final escrito en {archivo_salida}: {resultado}")
        return resultado
    return []

# --- Ejemplo de Uso y Limpieza ---

if __name__ == '__main__':
    ARCHIVO_ENTRADA = 'datos_natural_merging.txt'
    ARCHIVO_SALIDA = 'datos_natural_merging_ordenados.txt'
    ARCHIVOS_TRABAJO = ['T1_nm.txt', 'T2_nm.txt']
    
    # Limpieza previa
    archivos_a_limpiar = [ARCHIVO_ENTRADA, ARCHIVO_SALIDA] + ARCHIVOS_TRABAJO
    for f in archivos_a_limpiar:
        if os.path.exists(f):
            os.remove(f)

    # Crear datos de entrada (con algunos runs naturales para el ejemplo)
    with open(ARCHIVO_ENTRADA, 'w') as f:
        f.write('10\n20\n5\n15\n25\n30\n1\n2\n3\n')
    
    # Ejecutar el algoritmo
    natural_merging(ARCHIVO_ENTRADA, ARCHIVO_SALIDA, ARCHIVOS_TRABAJO)
    
    # Limpieza final
    for f in archivos_a_limpiar:
        if os.path.exists(f):
            os.remove(f)
