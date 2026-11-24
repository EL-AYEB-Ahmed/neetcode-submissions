/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* p = head;
        int l = 0;
        
        // 1. Calcul de la longueur
        while (p != nullptr) {
            ++l;
            p = p->next;
        }
        
        // Position du nœud AVANT celui à supprimer
        int target = l - n - 1; 
        
        // CAS CRITIQUE : Si on doit supprimer la tête (l == n)
        if (target < 0) {
            ListNode* newHead = head->next;
            // delete head; // Optionnel : libérer la mémoire
            return newHead;
        }
        
        // 2. Repositionnement de p au début
        p = head;
        for (int i = 0; i < target; i++) {
            p = p->next;
        }
        
        // 3. Suppression du nœud suivant
        if (p->next != nullptr) {
            ListNode* toDelete = p->next;
            p->next = p->next->next;
            // delete toDelete; // Optionnel : libérer la mémoire
        }
        
        return head;
    }
};