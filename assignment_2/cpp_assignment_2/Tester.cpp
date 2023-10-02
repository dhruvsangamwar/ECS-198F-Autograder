#include <iostream>
#include "isValidBracelet.cpp"
#include <string>

using namespace std; 

int main( int argc, char *argv[]){
    
    if( atoi( argv[1]) == 0){
        std::vector<string> arr = {"red_left", "blue_left", "blue_right", "red_right"};
        cout << isValidBracelet(arr) << endl;
    }
    else if( atoi( argv[1]) == 1){
        std::vector<string> arr = {"red_left", "blue_right"};
        cout << isValidBracelet(arr) << endl;

    }
    else if( atoi( argv[1]) == 2){
        std::vector<string> arr = {"red_left", "red_right", "blue_left", "blue_right"};
        cout << isValidBracelet(arr) << endl;
    }  
    else if( atoi( argv[1]) == 3){
        std::vector<string> arr = {};
        cout << isValidBracelet(arr) << endl;
    }  
    else if( atoi( argv[1]) == 4){
        std::vector<string> arr = {"red_left", "blue_left", "yellow_left", "yellow_right", "blue_right", "red_right"};
        cout << isValidBracelet(arr) << endl;
    }  

    return 0; 
}