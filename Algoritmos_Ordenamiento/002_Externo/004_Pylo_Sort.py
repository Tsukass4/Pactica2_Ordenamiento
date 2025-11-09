# ==============================================================================
# 11. Ordenamiento Polifásico (Polyphase Sort) - Simulación Conceptual
#
# Algoritmo de ordenamiento externo. Se basa en la distribución inicial de runs
# según números de Fibonacci generalizados y la fusión de runs de los archivos
# no vacíos al archivo vacío.
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
    
    heap = []
    for i, run in enumerate(runs):
        if run:
            heapq.heappush(heap, (run[0], i, 0))
            
    run_fusionado = []
    
    while heap:
        valor, run_idx, elem_idx = heapq.heappop(heap)
        run_fusionado.append(valor)
        
        if elem_idx + 1 < len(runs[run_idx]):
            siguiente_valor = runs[run_idx][elem_idx + 1]
            heapq.heappush(heap, (siguiente_valor, run_idx, elem_idx + 1))
            
    return run_fusionado

def distribucion_inicial_runs_simple(datos, archivos_trabajo, tamano_memoria=5):
    """
    Crea runs ordenados internamente y los distribuye entre los archivos de trabajo.
    (Simplificación de la distribución de Fibonacci para el concepto)
    """
    runs = []
    
    # 1. Creación de Runs (Ordenamiento Interno)
    for i in range(0, len(datos), tamano_memoria):
        bloque = datos[i:i + tamano_memoria]
        bloque.sort()
        runs.append(bloque)
        
    # 2. Distribución de Runs (Simulación de distribución Fibonacci para 3 archivos)
    # Una distribución ideal para 3 archivos (k=3) sería 5, 3, 2 runs.
    # Aquí distribuimos los runs disponibles de forma que uno quede "vacío" o con menos runs.
    num_archivos = len(archivos_trabajo)
    archivos_runs = [[] for _ in range(num_archivos)]
    
    # Distribuimos los runs en proporciones aproximadas (ejemplo: 50%, 30%, 20%)
    total_runs = len(runs)
    
    # Usamos una distribución simple para el ejemplo conceptual
    for i, run in enumerate(runs):
        indice_archivo = i % (num_archivos - 1) # Distribuimos en todos menos el último
        archivos_runs[indice_archivo].append(run)
        
    # Escribimos los runs distribuidos a los archivos de trabajo
    for i, nombre_archivo in enumerate(archivos_trabajo):
        escribir_runs_a_archivo(nombre_archivo, archivos_runs[i])
        
    return runs

# --- Algoritmo Principal ---

def polyphase_sort_concepto(archivo_entrada, archivo_salida, num_archivos=3):
    """
    Simula el concepto de Ordenamiento Polifásico.
    """
    print(f"--- Ordenamiento Polifásico (Concepto con {num_archivos} archivos) ---")
    
    # Archivos de trabajo
    archivos_trabajo = [f'P{i}_pps.txt' for i in range(num_archivos)]
    
    datos = leer_datos_archivo(archivo_entrada)
    if not datos:
        print("El archivo de entrada está vacío.")
        return []
        
    # Paso 1: Distribución inicial (Simplificada)
    runs_iniciales = distribucion_inicial_runs_simple(datos, archivos_trabajo, tamano_memoria=5)
    
    # El archivo de salida inicial (el "vacío" o el que recibe la fusión)
    archivo_salida_idx = num_archivos - 1
    
    pasada = 0
    
    while sum(len(leer_runs_de_archivo(f)) for f in archivos_trabajo) > 1:
        pasada += 1
        print(f"\nPasada {pasada}")
        
        # Archivos de entrada: todos excepto el de salida
        archivos_entrada_idx = [i for i in range(num_archivos) if i != archivo_salida_idx]
        
        runs_entrada_list = [leer_runs_de_archivo(archivos_trabajo[i]) for i in archivos_entrada_idx]
        
        # En Polyphase, se fusiona el número mínimo de runs disponibles en los archivos de entrada
        # Aquí, por simplicidad, fusionaremos el número de runs del archivo con menos runs
        min_runs = min(len(r) for r in runs_entrada_list)
        
        runs_salida = []
        
        # Fusionamos 'min_runs' veces
        for i in range(min_runs):
            # Tomamos el i-ésimo run de cada archivo de entrada
            runs_a_fusionar = [r[i] for r in runs_entrada_list]
            
            # Realizamos la fusión de múltiples vías
            run_fusionado = fusionar_multiples_runs(runs_a_fusionar)
            runs_salida.append(run_fusionado)
            
        # Escribimos los runs fusionados en el archivo de salida
        escribir_runs_a_archivo(archivos_trabajo[archivo_salida_idx], runs_salida)
        print(f"Runs fusionados en {archivos_trabajo[archivo_salida_idx]}: {runs_salida}")
        
        # Actualizamos los archivos de entrada (eliminando los runs que se fusionaron)
        for idx, runs_list in zip(archivos_entrada_idx, runs_entrada_list):
            runs_restantes = runs_list[min_runs:]
            escribir_runs_a_archivo(archivos_trabajo[idx], runs_restantes)
            
        # El archivo de salida se convierte en un archivo de entrada
        # El archivo que se vació (el que tenía los runs que se fusionaron) se convierte en el nuevo archivo de salida
        # (Esta es la parte clave del Polyphase: el archivo que se vacía se convierte en el de salida)
        
        # Buscamos el archivo que se vació (el que tiene 0 runs restantes)
        nuevo_archivo_salida_idx = -1
        for idx in archivos_entrada_idx:
            if not leer_runs_de_archivo(archivos_trabajo[idx]):
                nuevo_archivo_salida_idx = idx
                break
        
        if nuevo_archivo_salida_idx != -1:
            archivo_salida_idx = nuevo_archivo_salida_idx
        else:
            # Si no se vació ninguno (lo cual es un caso límite en la simulación simple),
            # alternamos al siguiente archivo de trabajo.
            archivo_salida_idx = (archivo_salida_idx + 1) % num_archivos
            
    # El resultado final está en el único archivo que queda con runs
    archivo_final = ""
    for f in archivos_trabajo:
        runs_finales = leer_runs_de_archivo(f)
        if runs_finales:
            archivo_final = f
            break
            
    if archivo_final:
        resultado = leer_runs_de_archivo(archivo_final)[0]
        escribir_runs_a_archivo(archivo_salida, [resultado])
        print(f"\nResultado final escrito en {archivo_salida}: {resultado}")
        return resultado
    return []

# --- Ejemplo de Uso y Limpieza ---

if __name__ == '__main__':
    ARCHIVO_ENTRADA = 'datos_pps.txt'
    ARCHIVO_SALIDA = 'datos_pps_ordenados.txt'
    NUM_ARCHIVOS = 3
    ARCHIVOS_TRABAJO = [f'P{i}_pps.txt' for i in range(NUM_ARCHIVOS)]
    
    # Limpieza previa
    archivos_a_limpiar = [ARCHIVO_ENTRADA, ARCHIVO_SALIDA] + ARCHIVOS_TRABAJO
    for f in archivos_a_limpiar:
        if os.path.exists(f):
            os.remove(f)

    # Crear datos de entrada
    crear_archivo_datos(ARCHIVO_ENTRADA, num_elementos=15)
    
    # Ejecutar el algoritmo
    polyphase_sort_concepto(ARCHIVO_ENTRADA, ARCHIVO_SALIDA, num_archivos=NUM_ARCHIVOS)
    
    # Limpieza final
    for f in archivos_a_limpiar:
        if os.path.exists(f):
            os.remove(f)
