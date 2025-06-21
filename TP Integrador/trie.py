# trie.py

class TrieNode:
    """
    Representa un nodo individual en la estructura de datos Trie.
    """
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    """
    Implementa la estructura de datos Trie para almacenamiento y búsqueda eficiente
    de palabras y prefijos.
    """
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str):
        """
        Inserta una palabra en el Trie.
        Las palabras se normalizan a minúsculas antes de la inserción.
        """
        word = word.lower()
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode()
            current_node = current_node.children[letter]
        current_node.end_of_word = True

    def search_word(self, word: str) -> bool:
        """
        Busca una palabra exacta en el Trie.
        Retorna True si la palabra existe, False en caso contrario.
        """
        word_normalized = word.lower()
        current_node = self.root
        for letter in word_normalized:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return False 
        return current_node.end_of_word

    def search_prefix(self, prefix: str) -> list[str]:
        """
        Busca todas las palabras en el Trie que comienzan con el prefijo dado.
        Retorna una lista de palabras que coinciden con el prefijo.
        """
        prefix_normalized = prefix.lower()
        current_node = self.root
        for letter in prefix_normalized:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return [] # Si el prefijo no existe, no hay sugerencias
        
        results = []
        
        # Función auxiliar DFS para recolectar palabras a partir del nodo del prefijo
        def _search_path(node, current_path_suffix): 
            if node.end_of_word:
                results.append(prefix_normalized + current_path_suffix)
            for letter_key, child_node in node.children.items():
                _search_path(child_node, current_path_suffix + letter_key)
                    
        _search_path(current_node, "")
        return results