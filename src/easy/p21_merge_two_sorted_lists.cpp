// two inputs: 
//       linked_list_1
//       linked_list_2

// output:
//   sorted linked_list
  
// Input:  
//      p
// //   1 -> 3 -> 4 -> null
//      q
// //   2 -> 5 -> 6 -> null
//      1 ->  2 -> 3 -> 4 -> 5 -> 6
// Output:
//   1 ->2 -> 3-> 4->5 -> 6

// smart pointer : https://www.geeksforgeeks.org/smart-pointers-cpp/
// ternary operator : http://www.cplusplus.com/articles/1AUq5Di1/

#include <iostream>
using namespace std;

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
 
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ostream& operator<<(ostream& os, ListNode* ptr)
{
    // ListNode* ptr = &node;
    while(ptr){
      os << ptr->val << ',';
      ptr = ptr->next;
    }
    return os;
}

class Solution {
public:
    //                          sorted
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // ListNode testNode = new ListNode();
        ListNode dummy(0);
        ListNode* ptr = &dummy;
        // while(list1->next){
        while(list1 && list2){
          if(list1->val < list2->val){
            ptr->next = list1;
            list1 = list1->next;
          }else{
            ptr->next = list2;
            list2 = list2->next;
          }
          ptr = ptr->next;
        }
        ptr->next = list1 ? list1 : list2;
        return dummy.next;
        // ListNode dummy(0);
    }
};


int main() {
  ListNode* l1  = new ListNode(1);
  l1->next= new ListNode(4);
  l1->next->next = new ListNode(7);
  // l1.next.next= new ListNode(3);
  ListNode* l2  = new ListNode(2);
  l2->next= new ListNode(8);
  l2->next->next = new ListNode(9);
  Solution S;
  ListNode* result = S.mergeTwoLists(l1,l2);
  
	//cout << l1->val<<l1->next;
  cout << result;
	return 0;
}

