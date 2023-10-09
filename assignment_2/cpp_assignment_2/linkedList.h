#include <iostream>

class Node {
public:
    int data;
    Node* next;

    Node(int val) : data(val), next(nullptr) {}
};

class LinkedList {
public:
    Node* head;

    LinkedList() : head(nullptr) {}

    void append(int data) {
        Node* newNode = new Node(data);
        if (!head) {
            head = newNode;
        } else {
            Node* current = head;
            while (current->next) {
                current = current->next;
            }
            current->next = newNode;
        }
    }

    void createCycle(int position) {
        if (position < 0) {
            return; // Invalid position
        }
        Node* current = head;
        Node* tail = nullptr;
        int index = 0;
        while (current) {
            if (index == position) {
                tail = current;
            }
            if (!current->next) {
                current->next = tail; // Create the cycle here
                return;
            }
            current = current->next;
            index++;
        }
    }

    void display() {
        Node* current = head;
        while (current) {
            std::cout << current->data << " -> ";
            current = current->next;
        }
        std::cout << "nullptr" << std::endl;
    }
};

bool hasCycle(LinkedList& linkedList) {
    Node* slow = linkedList.head;
    Node* fast = linkedList.head;

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            return true; // Cycle detected
        }
    }

    return false;
}
