#include <iostream>
#include <string>
#include <unordered_map>
#include <set>
#include <limits>

#include "assignment3.cpp"

using namespace std; 

int main( int argc, char *argv[]){
    
    // Test Cases for part 1
    if( atoi( argv[1]) == 0){
        std::vector<std::vector<std::string>> graph;
        graph.push_back(std::vector<std::string>{"b", "c", "d"});
        graph.push_back(std::vector<std::string>{"a"});
        graph.push_back(std::vector<std::string>{"a"});
		graph.push_back(std::vector<std::string>{"a"});

        cout << runErrands(graph) << endl; // 4
    }
    else if( atoi( argv[1]) == 1){
        std::vector<std::vector<std::string>> graph;
        graph.push_back(std::vector<std::string>{"b"});
        graph.push_back(std::vector<std::string>{"a", "c"});
        graph.push_back(std::vector<std::string>{"b"});
        graph.push_back(std::vector<std::string>{"a"});

        cout << runErrands(graph) << endl; // 3
    }
    else if( atoi( argv[1]) == 2){
        std::vector<std::vector<std::string>> graph;
        graph.push_back(std::vector<std::string>{"b", "c"});
        graph.push_back(std::vector<std::string>{"a", "e"});
        graph.push_back(std::vector<std::string>{"a", "d"});
        graph.push_back(std::vector<std::string>{"c"});
        graph.push_back(std::vector<std::string>{"b"});
        cout << runErrands(graph) << endl; // 3

    }  
    else if( atoi( argv[1]) == 3){
        std::vector<std::vector<std::string>> graph;
        graph.push_back(std::vector<std::string>{"b", "c"});
        graph.push_back(std::vector<std::string>{"a", "c"});
        graph.push_back(std::vector<std::string>{"a", "b", "d", "e"});
        graph.push_back(std::vector<std::string>{"c", "e"});
        graph.push_back(std::vector<std::string>{"c", "d", "e"});
        graph.push_back(std::vector<std::string>{"f"});
        
        cout << runErrands(graph) << endl; // 5
    }  
    else if( atoi( argv[1]) == 4){
        std::vector<std::vector<std::string>> graph;
        graph.push_back(std::vector<std::string>{"b"});
        graph.push_back(std::vector<std::string>{"a", "d", "e"});
        graph.push_back(std::vector<std::string>{"d"});
        graph.push_back(std::vector<std::string>{"b", "e"});

        cout << runErrands(graph) << endl; // 4
    } 

    // Test cases for the LRU problem  
    else if( atoi( argv[1]) == 5){
        // case 1: ints only
        clipboard clip(2);

        clip.copy(1, 1);  // Clipboard is {1=1}
        int result1 = clip.paste(1); // Expected: 1
        cout << result1 << endl;
    }
    else if( atoi( argv[1]) == 6){
        // case 2: ints only
        clipboard clip(5);

        clip.copy(1, 1);  // Clipboard is {1=1}
        clip.copy(2, 2);  // Clipboard is {1=1, 2=2}
        clip.copy(3, 3);  // Clipboard is {1=1, 2=2, 3=3}
        clip.copy(4, 4);  // Clipboard is {1=1, 2=2, 3=3, 4=4}
        clip.copy(5, 5);  // Clipboard is {1=1, 2=2, 3=3, 4=4, 5=5}
        int result2a = clip.paste(1); // Expected: 1
        int result2b = clip.paste(2); // Expected: 2
        int result2c = clip.paste(3); // Expected: 3
        int result2d = clip.paste(4); // Expected: 4
        clip.copy(6, 6);  // Clipboard is {1=1, 2=2, 3=3, 4=4, 5=5} // evict 5
        
        int result2e = clip.paste(5); // should be -1
        cout << result2a << " " << result2b << " " << result2c << " " << result2d << " " << result2e << endl; // 1 2 3 4 -1
    }
    else if( atoi( argv[1]) == 7){
        // case 3: ints only
        clipboard clip(2);

        clip.copy(1, 1);  // Clipboard is {1=1}
        int result3a = clip.paste(1); // Expected: 1
        clip.copy(2, 2);  // Clipboard is {1=1, 2=2}
        clip.copy(3, 3);  // Clipboard is {1=1, 3=3} evict 2
        int result3b = clip.paste(2); // Expected: -1
        int result3c = clip.paste(3); // Expected: 3

        cout << result3a << " " << result3b << " " << result3c << endl; // 1 -1 3
    }  
    else if( atoi( argv[1]) == 8){
        // case 4: ints only -> edge case
        clipboard clip(1);

        clip.copy(1, 1);  // Clipboard is {1=1}
        int result4a = clip.paste(1); // Expected: 1
        clip.copy(2, 2);  // Clipboard is {2=2}
        int result4b = clip.paste(2); // Expected: 2
        int result4c = clip.paste(1); // Expected: -1
        
        cout << result4a << " " << result4b << " " << result4c  << endl; // 1 2 -1

    }  
    else if( atoi( argv[1]) == 9){
        // case 5: ints only
        clipboard clip(1);
        int result5a = clip.paste(1); // Expected: -1
        int result5b = clip.paste(2); // Expected: -1

        cout << result5a << " " << result5b << endl; // -1 -1
    }  

    return 0; 
}