#include <iostream>

// Simple singly-linked list node
struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

// Singly-linked list with basic operations
class LinkedList {
public:
    LinkedList() : head(nullptr) {}
    ~LinkedList() { clear(); }

    // Insert at end
    void push_back(int val) {
        Node* node = new Node(val);
        if (!head) {
            head = node;
            return;
        }
        Node* cur = head;
        while (cur->next) cur = cur->next;
        cur->next = node;
    }

    // Print elements separated by arrows
    void print() const {
        Node* cur = head;
        while (cur) {
            std::cout << cur->data;
            if (cur->next) std::cout << " -> ";
            cur = cur->next;
        }
        std::cout << '\n';
    }

    // Iterative reverse: O(n) time, O(1) extra space
    void reverseIterative() {
        Node* prev = nullptr;
        Node* cur = head;
        while (cur) {
            Node* nxt = cur->next;
            cur->next = prev;
            prev = cur;
            cur = nxt;
        }
        head = prev;
    }

    // Recursive reverse helper: returns new head
    Node* reverseRecursiveHelper(Node* node) {
        if (!node || !node->next) return node; // base: empty or single node
        Node* newHead = reverseRecursiveHelper(node->next);
        node->next->next = node;
        node->next = nullptr;
        return newHead;
    }

    // Public recursive reverse
    void reverseRecursive() {
        head = reverseRecursiveHelper(head);
    }

    // Remove all nodes
    void clear() {
        Node* cur = head;
        while (cur) {
            Node* nxt = cur->next;
            delete cur;
            cur = nxt;
        }
        head = nullptr;
    }

private:
    Node* head;
};

int main() {
    LinkedList list;

    // Insert 1..9
    for (int i = 1; i <= 9; ++i) {
        list.push_back(i);
    }

    std::cout << "Original list:\n";
    list.print();

    // Iterative reverse
    list.reverseIterative();
    std::cout << "After iterative reverse:\n";
    list.print();

    // Reverse back using recursive reverse
    list.reverseRecursive();
    std::cout << "After recursive reverse (should restore original):\n";
    list.print();

    return 0;
}