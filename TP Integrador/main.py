# main.py

import sys
from datasets import KANTO_POKEMONS
from search_utils import run_performance_tests
from interactive import run_interactive_cli

def display_menu():
    """Muestra el menú principal de opciones."""
    print("="*50)
    print("          P R O Y E C T O   P O K É D E X")
    print("="*50)
    print("1. Ejecutar Pruebas de Rendimiento Comparativas")
    print("2. Iniciar Buscador Interactivo de Pokémon")
    print("0. Salir")
    print("="*50)

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Selecciona una opción: ").strip()

        if choice == '1':
            run_performance_tests(KANTO_POKEMONS)
        elif choice == '2':
            run_interactive_cli()
        elif choice == '0':
            print("Saliendo de la aplicación. ¡Hasta luego!")
            sys.exit(0)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
        
        input("\nPresiona Enter para continuar...") # Pausa para ver los resultados