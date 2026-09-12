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

    // Print elements separated by spaces
    void print() const {
        Node* cur = head;
        while (cur) {
            std::cout << cur->data;
            if (cur->next) std::cout << " -> ";
            cur = cur->next;
        }
        std::cout << '\n';
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

    // Print the list
    std::cout << "Linked list contents:\n";
    list.print();

    // Destructor will free memory on exit
    return 0;
}