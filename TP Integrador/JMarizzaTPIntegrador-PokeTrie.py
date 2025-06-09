import time
import sys

# --- Clases del Trie ---
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        word = word.lower()
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode()
            current_node = current_node.children[letter]
        current_node.end_of_word = True

    # --- NUEVA FUNCIÓN: searchWord para búsqueda exacta ---
    def search_word(self, word):
        word_normalized = word.lower()
        current_node = self.root
        for letter in word_normalized:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return False # La palabra no está en el Trie
        return current_node.end_of_word # Retorna True si es el final de una palabra

    def search_prefix(self, prefix):
        prefix_normalized = prefix.lower()
        current_node = self.root
        for letter in prefix_normalized:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return [] # Si el prefijo no existe, no hay sugerencias
        
        results = []
        # Renombramos 'children' a 'child_node' en la DFS para mayor claridad
        def search_path(node, current_path_suffix): 
            if node.end_of_word:
                results.append(prefix_normalized + current_path_suffix)
            for letter_key, child_node in node.children.items():
                search_path(child_node, current_path_suffix + letter_key)
                            
        search_path(current_node, "")
        return results

# --- Lista de Pokémon ---
kanto_pokemons = [
    "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree",
    "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot",
    "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok",
    "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina",
    "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable",
    "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat",
    "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat",
    "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck",
    "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag",
    "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop",
    "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool",
    "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash",
    "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo",
    "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder",
    "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee",
    "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute",
    "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung",
    "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela",
    "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu",
    "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar",
    "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto",
    "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte",
    "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno",
    "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo",
    "Mew"
]

# --- Funciones Auxiliares para Comparación ---

# Carga palabras en una lista (normalizándolas a minúsculas)
def load_list(words):
    return [word.lower() for word in words]

# Busca una palabra exacta en una lista (secuencialmente)
def search_list_exact(word_list, word):
    return word.lower() in word_list

# Busca prefijos en una lista, iterando sobre todos los elementos
def search_list_prefix(word_list, prefix):
    prefix_normalized = prefix.lower()
    results = [word for word in word_list if word.startswith(prefix_normalized)]
    return results

# Carga palabras en un conjunto (set), normalizándolas a minúsculas
def load_set(words):
    return {word.lower() for word in words}

# Busca una palabra exacta en un conjunto (hashing)
def search_set_exact(word_set, word):
    return word.lower() in word_set

# Busca prefijos en un conjunto, iterando sobre todos los elementos (ineficiente para set)
def search_set_prefix(word_set, prefix):
    prefix_normalized = prefix.lower()
    results = [word for word in word_set if word.startswith(prefix_normalized)]
    return results

# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    
    # --- PARTE 1: Pruebas de Rendimiento Comparativas ---
    num_runs = 100 # Número de veces que se repite cada operación para promediar

    print("--- INICIANDO PRUEBAS DE RENDIMIENTO COMPARATIVAS ---")
    print(f"Cargando {len(kanto_pokemons)} Pokémon. Cada prueba se repite {num_runs} veces para promediar.\n")

    # --- 1. Tiempo de Carga/Inserción ---
    print("1. Tiempo de Carga/Inserción (en segundos):")
    
    # Trie
    start_time = time.perf_counter()
    for _ in range(num_runs):
        trie_test_instance = Trie()
        for p_name in kanto_pokemons:
            trie_test_instance.insert(p_name)
    end_time = time.perf_counter()
    trie_load_time = (end_time - start_time) / num_runs
    print(f"   Trie: {trie_load_time:.8f}") # Aumentamos precisión para ver las diferencias

    # Lista
    start_time = time.perf_counter()
    for _ in range(num_runs):
        list_test_instance = load_list(kanto_pokemons)
    end_time = time.perf_counter()
    list_load_time = (end_time - start_time) / num_runs
    print(f"   Lista: {list_load_time:.8f}")

    # Set
    start_time = time.perf_counter()
    for _ in range(num_runs):
        set_test_instance = load_set(kanto_pokemons)
    end_time = time.perf_counter()
    set_load_time = (end_time - start_time) / num_runs
    print(f"   Set: {set_load_time:.8f}\n")

    # Pre-cargar las estructuras una vez para las pruebas de búsqueda
    trie_instance_for_search = Trie()
    for p_name in kanto_pokemons:
        trie_instance_for_search.insert(p_name)
    list_instance_for_search = load_list(kanto_pokemons)
    set_instance_for_search = load_set(kanto_pokemons)

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
    
    test_prefixes = ["char", "pika", "bulba", "z", "squ", "mewtwo", "xyz"] # Ejemplos de prefijos, incluyendo uno sin resultados

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

    # --- PARTE 2: Interfaz Interactiva de Búsqueda ---
    print("--- BUSCADOR DE POKÉMON (Interfaz Interactiva) ---")
    print("---------------------------------------------------\n")

    # Re-instanciamos un Trie para la interfaz interactiva
    trie = Trie()
    for pokemon_name in kanto_pokemons:
        trie.insert(pokemon_name)

    while True:
        user_input_prefix = input("Ingresá un prefijo para buscar tu Pokémon (o '0' para terminar): ")
        
        if user_input_prefix == "0":
            print("Gracias por usar la Pokédex. ¡Vuelve pronto!")
            break
        
        suggestions = trie.search_prefix(user_input_prefix)

        if suggestions:
            print("Te refieres a:")
            # Usamos .capitalize() para que las sugerencias se vean como nombres propios
            for s in suggestions:
                print(f" - {s.capitalize()}")
        else:
            print(f"No existen Pokémon con el prefijo '{user_input_prefix}'.")
        
        print("\n" + "-"*50 + "\n") # Separador para la próxima búsqueda
