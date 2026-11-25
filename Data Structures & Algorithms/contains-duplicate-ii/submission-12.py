class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i in range(len(nums)):
            # 1. Si l'élément est déjà dans la fenêtre, on a trouvé un doublon proche
            if nums[i] in window:
                return True
            
            # 2. On ajoute l'élément actuel à la fenêtre
            window.add(nums[i])
            
            # 3. On maintient la taille de la fenêtre : 
            # Si on a dépassé k éléments, on retire le plus ancien
            if len(window) > k:
                window.remove(nums[i - k])
                
        return False