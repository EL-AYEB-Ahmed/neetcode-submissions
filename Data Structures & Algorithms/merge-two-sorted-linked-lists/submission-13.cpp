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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* p1 = list1;
        ListNode* p2 = list2;
        ListNode dummy(0); 
        ListNode* r = &dummy;

        while (p1 != nullptr && p2 != nullptr){
            if (p1->val < p2->val){
                r->next = p1;
                
                p1=p1->next;
            }
            else {
                r->next = p2;

                p2=p2->next;
            }
            r= r->next;
        }
        if (p1 != nullptr) {
            r->next = p1;
        } else {
            r->next = p2;
        }
        return dummy.next;
    }
};