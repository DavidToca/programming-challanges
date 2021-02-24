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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode root = ListNode();

        ListNode *current;
        ListNode *l3;
        current = &root;

        while(l1 || l2){

            if (!l1){
                current->next = l2;
                return root.next;
            } else if(!l2){
                current->next = l1;
                return root.next;
            } else {

                if(l1->val < l2->val){
                    l3 = l1;
                    l1 = l1->next;
                } else {
                    l3 = l2;
                    l2 = l2->next;
                }
            }
            current->next = l3;
            current = current->next;
        }
        return root.next;
    }
};