class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head || !head->next) return;

        // 1. Trouver le milieu de la liste (Slow & Fast pointers)
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // 2. Inverser la seconde moitié
        // On coupe la liste en deux : la première finit à 'slow', la seconde commence à 'slow->next'
        ListNode* prev = nullptr;
        ListNode* curr = slow->next;
        slow->next = nullptr; // On coupe officiellement la liste en deux

        while (curr != nullptr) {
            ListNode* nextTemp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextTemp;
        }
        // 'prev' est maintenant la tête de la seconde moitié inversée

        // 3. Fusionner les deux listes (Interleave)
        ListNode* first = head;
        ListNode* second = prev;
        while (second != nullptr) {
            // Sauvegarde des nœuds suivants
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;

            // On lie le premier au second
            first->next = second;
            // On lie le second au suivant du premier
            second->next = tmp1;

            // On avance les pointeurs pour le prochain cycle
            first = tmp1;
            second = tmp2;
        }
    }
};