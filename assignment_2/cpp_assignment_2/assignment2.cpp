// reina's code
#include <string>
#include <map>
#include <vector>
#include <unordered_map>
#include <set>
#include <iostream>
#include "linkedList.h"

// the cycle one
bool hasccycle(LinkedList path) {
    // std::set of visited nodes
    std::set<Node*> visited;

    // address of current node
    Node* cur = path.head;
    while (cur) {
        // if find current node in visited nodes, return true
        if (visited.find(cur) != visited.end()) {
            return true;
        }

        // insert node into visited, move onto next node
        visited.insert(cur);
        cur = cur->next;
    }
    return false;
}

std::string detectCycle(LinkedList& linkedList) {
    if (hasccycle(linkedList)) {
        return "True";
    }
    return "False";
}

// double
std::string find_next_recommendation(std::unordered_map<std::string, std::unordered_map <std::string, double> >& graph,
                              const std::set<std::string>& currentFriends) 
{
    std::set<std::basic_string <char> > visited = currentFriends;
    visited.insert("You");

    int mn = INT16_MAX;
    std::string rec;
    for (auto it = graph["You"].begin(); it != graph["You"].end(); it++) {
        if (visited.find(it->first) != visited.end()) {
            for (auto itr = graph[it->first].begin(); itr != graph[it->first].end(); itr++) {
                if (visited.find(itr->first) == visited.end()) {
                    if (itr->second < mn) {
                        mn = itr->second;
                        rec = itr->first;
                    }
                }
            }
            continue;
        } 
        if (it->second < mn) {
            mn = it->second;
            rec = it->first;
        }
    }
    return rec;
}

// The friend one
std::string find_next_recommendation(std::unordered_map<std::string, std::unordered_map <std::string, int> >& graph,
                              const std::set<std::string>& currentFriends) 
{
    std::set<std::basic_string <char> > visited = currentFriends;
    visited.insert("You");

    int mn = INT16_MAX;
    std::string rec;
    for (auto it = graph["You"].begin(); it != graph["You"].end(); it++) {
        if (visited.find(it->first) != visited.end()) {
            for (auto itr = graph[it->first].begin(); itr != graph[it->first].end(); itr++) {
                if (visited.find(itr->first) == visited.end()) {
                    if (itr->second < mn) {
                        mn = itr->second;
                        rec = itr->first;
                    }
                }
            }
            continue;
        } 
        if (it->second < mn) {
            mn = it->second;
            rec = it->first;
        }
    }
    return rec;
}