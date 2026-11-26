from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # On utilise un defaultdict pour éviter de vérifier si la clé existe
        anagrams_map = defaultdict(list)
        
        for s in strs:
            # On trie le mot pour créer une clé unique : "eat" -> "aet", "tea" -> "aet"
            # Le tri transforme le mot en liste, on le rejoint en chaîne pour qu'il soit hashable
            sorted_word = "".join(sorted(s))
            
            # On ajoute le mot original au groupe correspondant à sa version triée
            anagrams_map[sorted_word].append(s)
            
        # On retourne uniquement les listes de valeurs du dictionnaire
        return list(anagrams_map.values())
