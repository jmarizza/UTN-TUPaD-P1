# search_utils.py

import time
from trie import Trie # Importamos la clase Trie de nuestro módulo trie.py

# --- Funciones Auxiliares para Comparación (Listas y Sets) ---

def load_list(words: list[str]) -> list[str]:
    """Carga palabras en una lista, normalizándolas a minúsculas."""
    return [word.lower() for word in words]

def search_list_exact(word_list: list[str], word: str) -> bool:
    """Busca una palabra exacta en una lista (secuencialmente)."""
    return word.lower() in word_list

def search_list_prefix(word_list: list[str], prefix: str) -> list[str]:
    """Busca prefijos en una lista, iterando sobre todos los elementos."""
    prefix_normalized = prefix.lower()
    results = [word for word in word_list if word.startswith(prefix_normalized)]
    return results

def load_set(words: list[str]) -> set[str]:
    """Carga palabras en un conjunto (set), normalizándolas a minúsculas."""
    return {word.lower() for word in words}

def search_set_exact(word_set: set[str], word: str) -> bool:
    """Busca una palabra exacta en un conjunto (hashing)."""
    return word.lower() in word_set

def search_set_prefix(word_set: set[str], prefix: str) -> list[str]:
    """
    Busca prefijos en un conjunto.
    Nota: La búsqueda por prefijo es ineficiente para sets, ya que requiere iterar
    sobre todos los elementos.
    """
    prefix_normalized = prefix.lower()
    results = [word for word in word_set if word.startswith(prefix_normalized)]
    return results

# --- Función Principal para Ejecutar las Pruebas ---

def run_performance_tests(pokemons: list[str], num_runs: int = 100):
    """
    Ejecuta un conjunto de pruebas de rendimiento comparando Trie, Listas y Sets
    para operaciones de carga, búsqueda exacta y búsqueda por prefijo.
    """
    print("--- INICIANDO PRUEBAS DE RENDIMIENTO COMPARATIVAS ---")
    print(f"Cargando {len(pokemons)} Pokémon. Cada prueba se repite {num_runs} veces para promediar.\n")

    # --- 1. Tiempo de Carga/Inserción ---
    print("1. Tiempo de Carga/Inserción (en segundos):")
    
    # Trie
    start_time = time.perf_counter()
    for _ in range(num_runs):
        trie_test_instance = Trie()
        for p_name in pokemons:
            trie_test_instance.insert(p_name)
    end_time = time.perf_counter()
    trie_load_time = (end_time - start_time) / num_runs
    print(f"   Trie: {trie_load_time:.8f}")

    # Lista
    start_time = time.perf_counter()
    for _ in range(num_runs):
        list_test_instance = load_list(pokemons)
    end_time = time.perf_counter()
    list_load_time = (end_time - start_time) / num_runs
    print(f"   Lista: {list_load_time:.8f}")

    # Set
    start_time = time.perf_counter()
    for _ in range(num_runs):
        set_test_instance = load_set(pokemons)
    end_time = time.perf_counter()
    set_load_time = (end_time - start_time) / num_runs
    print(f"   Set: {set_load_time:.8f}\n")

    # Pre-cargar las estructuras una vez para las pruebas de búsqueda
    trie_instance_for_search = Trie()
    for p_name in pokemons:
        trie_instance_for_search.insert(p_name)
    list_instance_for_search = load_list(pokemons)
    set_instance_for_search = load_set(pokemons)

    # --- 2. Tiempo de Búsqueda de Palabra Exacta ---
    print("2. Tiempo de Búsqueda de Palabra Exacta (en segundos):")
    
    test_word_exist = "Pikachu"
    test_word_non_exist = "Zarbi" # Una palabra que no existe

    # Búsqueda existente
    print(f"   Palabra existente ('{test_word_exist}'):")
    
    start_time = time.perf_counter()
    for _ in range(num_runs):
        trie_instance_for_search.search_word(test_word_exist)
    end_time = time.perf_counter()
    trie_search_exist_time = (end_time - start_time) / num_runs
    print(f"     Trie: {trie_search_exist_time:.8f}")

    start_time = time.perf_counter()
    for _ in range(num_runs):
        search_list_exact(list_instance_for_search, test_word_exist)
    end_time = time.perf_counter()
    list_search_exist_time = (end_time - start_time) / num_runs
    print(f"     Lista: {list_search_exist_time:.8f}")

    start_time = time.perf_counter()
    for _ in range(num_runs):
        search_set_exact(set_instance_for_search, test_word_exist)
    end_time = time.perf_counter()
    set_search_exist_time = (end_time - start_time) / num_runs
    print(f"     Set: {set_search_exist_time:.8f}\n")

    # Búsqueda no existente
    print(f"   Palabra no existente ('{test_word_non_exist}'):")

    start_time = time.perf_counter()
    for _ in range(num_runs):
        trie_instance_for_search.search_word(test_word_non_exist)
    end_time = time.perf_counter()
    trie_search_non_exist_time = (end_time - start_time) / num_runs
    print(f"     Trie: {trie_search_non_exist_time:.8f}")

    start_time = time.perf_counter()
    for _ in range(num_runs):
        search_list_exact(list_instance_for_search, test_word_non_exist)
    end_time = time.perf_counter()
    list_search_non_exist_time = (end_time - start_time) / num_runs
    print(f"     Lista: {list_search_non_exist_time:.8f}")

    start_time = time.perf_counter()
    for _ in range(num_runs):
        search_set_exact(set_instance_for_search, test_word_non_exist)
    end_time = time.perf_counter()
    set_search_non_exist_time = (end_time - start_time) / num_runs
    print(f"     Set: {set_search_non_exist_time:.8f}\n")


    # --- 3. Tiempo de Búsqueda por Prefijo / Autocompletado ---
    print("3. Tiempo de Búsqueda por Prefijo (Autocompletado) (en segundos):")
    
    test_prefixes = ["char", "pika", "bulba", "z", "squ", "mewtwo", "xyz"] # Ejemplos de prefijos

    for prefix_to_test in test_prefixes:
        print(f"   Prefijo: '{prefix_to_test}'")

        # Trie
        start_time = time.perf_counter()
        for _ in range(num_runs):
            trie_instance_for_search.search_prefix(prefix_to_test)
        end_time = time.perf_counter()
        trie_prefix_time = (end_time - start_time) / num_runs
        print(f"     Trie: {trie_prefix_time:.8f}")

        # Lista
        start_time = time.perf_counter()
        for _ in range(num_runs):
            search_list_prefix(list_instance_for_search, prefix_to_test)
        end_time = time.perf_counter()
        list_prefix_time = (end_time - start_time) / num_runs
        print(f"     Lista: {list_prefix_time:.8f}")

        # Set
        start_time = time.perf_counter()
        for _ in range(num_runs):
            search_set_prefix(set_instance_for_search, prefix_to_test)
        end_time = time.perf_counter()
        set_prefix_time = (end_time - start_time) / num_runs
        print(f"     Set: {set_prefix_time:.8f}\n")

    print("--- FIN DE PRUEBAS DE RENDIMIENTO ---\n")