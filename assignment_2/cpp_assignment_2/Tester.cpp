#include <iostream>
#include <string>
#include <unordered_map>
#include <set>
#include <limits>

#include "assignment2.cpp"
#include "linkedList.h"

using namespace std; 

int main( int argc, char *argv[]){
    
    // Test Cases for Linked List
    if( atoi( argv[1]) == 0){
        LinkedList CycleList;
        CycleList.append(1);
        CycleList.append(2);
        CycleList.append(3);
        CycleList.append(4);
        CycleList.append(5);
        CycleList.createCycle(2)
        cout << detectCycle(CycleList) << endl;
    }
    else if( atoi( argv[1]) == 1){
        LinkedList CycleList;
        CycleList.append("a");
        CycleList.append("b");
        CycleList.append("c");
        CycleList.append("d");
        CycleList.append("e");
        CycleList.createCycle("b")

        cout << detectCycle(CycleList) << endl;
    }
    else if( atoi( argv[1]) == 2){
        LinkedList CycleList;
        CycleList.append("a");
        CycleList.append("a");
        CycleList.append("a");
        CycleList.append("a");
        CycleList.append("a");
        CycleList.createCycle("a")

        cout << detectCycle(CycleList) << endl;
    }  
    else if( atoi( argv[1]) == 3){
        LinkedList noCycleList;
        noCycleList.append("a");
        noCycleList.append("b");
        noCycleList.append("c");
        noCycleList.append("d");
        noCycleList.append("e");

        cout << detectCycle(noCycleList) << endl;
    }  
    else if( atoi( argv[1]) == 4){
        LinkedList noCycleList;

        cout << detectCycle(noCycleList) << endl;
    } 

    // Test cases for the graph problem  
    else if( atoi( argv[1]) == 5){
        // case 1: ints only
        std::unordered_map<std::string, std::unordered_map<std::string, int>> graph_test1 = {
            {"You", {{"Friend1", 2}, {"Friend2", 3}, {"Friend3", 4}}},
            {"Friend1", {{"You", 2}, {"Friend4", 1}}},
            {"Friend2", {{"You", 3}, {"Friend5", 2}}},
            {"Friend3", {{"You", 4}}},
            {"Friend4", {{"Friend1", 1}}},
            {"Friend5", {{"Friend2", 2}}}
        };

        std::set<std::string> currentFriends_test1 = {"Friend1", "Friend2"};
        std::string nextRecommendation = find_next_recommendation(graph_test1, currentFriends_test1);
        cout << nextRecommendation << endl;
    }
    else if( atoi( argv[1]) == 6){
        // case 2 ints and floats
        std::unordered_map<std::string, std::unordered_map<std::string, double>> graph_test2 = {
            {"You", {{"Friend1", 2.5}, {"Friend2", 3.0}, {"Friend3", 4.2}, {"Friend4", 1.8}}},
            {"Friend1", {{"You", 2.5}, {"Friend5", 3.1}}},
            {"Friend2", {{"You", 3.0}, {"Friend5", 2.8}}},
            {"Friend3", {{"You", 4.2}, {"Friend6", 2.3}}},
            {"Friend4", {{"You", 1.8}}},
            {"Friend5", {{"Friend1", 3.1}, {"Friend2", 2.8}}},
            {"Friend6", {{"Friend3", 2.3}}}
        };

        std::set<std::string> current_friends_test2 = {"Friend1", "Friend2", "Friend3"};

        std::string nextRecommendation = find_next_recommendation(graph_test2, current_friends_test2);
        cout << nextRecommendation << endl;
    }
    else if( atoi( argv[1]) == 7){
        // case 3
        std::unordered_map<std::string, std::unordered_map<std::string, double>> graph_test3 = {
            {"You", {}},
            {"Friend1", {}},
            {"Friend2", {}},
            {"Friend3", {}},
            {"Friend4", {}},
            {"Friend5", {}}
        };

        std::set<std::string> current_friends_test3;

        std::string nextRecommendation = find_next_recommendation(graph_test3, current_friends_test3);
        cout << nextRecommendation << endl;
    }  
    else if( atoi( argv[1]) == 8){
        // case 4
        std::unordered_map<std::string, std::unordered_map<std::string, double>> graph_test4 = {
            {"You", {{"Friend1", 2.5}}},
            {"Friend1", {{"You", 2.5}}},
            {"Friend2", {}},
            {"Friend3", {}},
            {"Friend4", {}},
            {"Friend5", {}}
        };

        std::set<std::string> current_friends_test4 = {"Friend1"};
        std::string nextRecommendation = find_next_recommendation(graph_test4, current_friends_test4);
        cout << nextRecommendation << endl;
    }  
    else if( atoi( argv[1]) == 9){
        
        std::unordered_map<std::string, std::unordered_map<std::string, double>> graph_test5 = {
            {"You", {{"Friend1", 3}, {"Friend2", 3}, {"Friend3", 3}, {"Friend4", 3}}},
            {"Friend1", {{"You", 3}, {"Friend5", 3}}},
            {"Friend2", {{"You", 3}, {"Friend6", 3}}},
            {"Friend3", {{"You", 3}, {"Friend7", 3}}},
            {"Friend4", {{"You", 3}, {"Friend8", 3}}},
            {"Friend5", {{"Friend1", 3}}},
            {"Friend6", {{"Friend2", 3}}},
            {"Friend7", {{"Friend3", 3}}},
            {"Friend8", {{"Friend4", 3}}}
        };

        std::set<std::string> current_friends_test5 = {"Friend1", "Friend2", "Friend3", "Friend4"};
        std::string nextRecommendation = find_next_recommendation(graph_test5, current_friends_test5);
        cout << nextRecommendation << endl;
    }  

    return 0; 
}