# interactive.py

from trie import Trie # Importamos la clase Trie
from datasets import KANTO_POKEMONS # Importamos la lista de Pokémon

def run_interactive_cli():
    """
    Ejecuta la interfaz de línea de comandos interactiva para buscar Pokémon.
    """
    print("--- BUSCADOR DE POKÉMON (Interfaz Interactiva) ---")
    print("---------------------------------------------------\n")

    # Instanciamos y cargamos el Trie para la interfaz interactiva
    trie = Trie()
    print("Cargando Pokémon en el Trie...")
    for pokemon_name in KANTO_POKEMONS:
        trie.insert(pokemon_name)
    print("Carga completa.\n")

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