# Árboles de Prefijos - Trie (Trabajo Práctico Integrador)

**Materia:** Programación I  
**Carrera:** Tecnicatura Universitaria en Programación  
**Universidad:** UTN  
**Estudiante:** Jonatan X. Marizza  
**Fecha:** Junio de 2025  

---

## Descripción del proyecto

Este proyecto implementa una estructura de datos **Trie** (árbol de prefijos) en Python, aplicada a un sistema de **autocompletado de nombres de Pokémon** de la región Kanto.

Además de la funcionalidad principal, el sistema realiza **comparaciones de rendimiento** entre el Trie y otras estructuras como listas y conjuntos (`set`) en operaciones de búsqueda exacta y por prefijo.

---

## Características

- Estructura Trie implementada desde cero.
- Inserción eficiente de palabras.
- Búsqueda exacta y autocompletado por prefijo.
- Interfaz interactiva de consola para probar el sistema.
- Pruebas de rendimiento frente a `list` y `set`.

---

## Estructuras utilizadas

- `TrieNode` y `Trie`: clases que conforman el árbol de prefijos.
- Algoritmo DFS (búsqueda en profundidad) para recorrer y sugerir palabras.
- Dataset: 151 Pokémon originales de la región Kanto.

---

## Pruebas y resultados

Se realizaron pruebas para:

- Medir el tiempo de inserción de datos en diferentes estructuras.
- Comparar tiempos de búsqueda exacta.
- Comparar tiempos de búsqueda por prefijo (autocompletado).

### Conclusiones:
- El **Trie** es más lento en la carga inicial debido a su estructura más compleja.
- Para **búsquedas exactas**, el `set` es más rápido (gracias a hashing).
- Para **autocompletado**, el **Trie es el más eficiente**, manteniendo tiempos constantes respecto al tamaño del conjunto.

---

## Cómo ejecutar

1. Asegurate de tener Python 3 instalado.
2. Cloná el repositorio o descargá el archivo `.py`.

```bash
python JMarizzaTPIntegrador-PokeTrie.py
```

3. El script ejecutará:
   - Pruebas de rendimiento (automáticas)
   - Interfaz interactiva de búsqueda por prefijo

---

## Ejemplo de uso

```
--- BUSCADOR DE POKÉMON (Interfaz Interactiva) ---
Ingresá un prefijo para buscar tu Pokémon (o '0' para terminar): char
Te refieres a:
 - Charmander
 - Charmeleon
 - Charizard
```

---

## Documentación

El proyecto está acompañado por una documentación en PDF donde se detalla:

- Marco teórico del Trie
- Complejidad algorítmica
- Metodología aplicada
- Resultados de pruebas
- Conclusiones y bibliografía
- Link al video: https://www.loom.com/share/b2e71de1fba3466f8a3dd84f219414dc?sid=bd252982-b33b-44ad-a3e5-2988e61c76ce
---

## Recursos utilizados

- Python 3.x
- `time.perf_counter()` para medición de rendimiento
- Algoritmos DFS para recorrido del Trie
- Dataset: Pokémon Kanto (151)
