#include <iostream>
#include <string>
#include <unordered_map>
#include <set>
#include <vector>
#include <limits>

#include "assignment7.cpp"

int main( int argc, char *argv[]){
    if( atoi( argv[1]) == 0){
        std::vector<double> targetTreeCoordinates = {1.0, 1.0};
        std::vector<std::vector<double>> allTrees = {{2.0, 3.0}, {5.0, 5.0}, {1.0, 2.0}, {3.0, 1.0}, {4.0, 4.0}};
        std::vector<double> allHeights = {95.0, 103.56, 97.22, 107.39, 108.22};
        int k = 2;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }
    else if( atoi( argv[1]) == 1){ 
        std::vector<double> targetTreeCoordinates = {1.0, 1.0};
        std::vector<std::vector<double>> allTrees = {{2.0, 3.0}, {5.0, 5.0}, {1.0, 2.0}, {3.0, 1.0}, {4.0, 4.0}};
        std::vector<double> allHeights = {95.0, 103.56, 97.22, 107.39, 108.22};
        int k = 3;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }
    else if( atoi( argv[1]) == 2){
        std::vector<double> targetTreeCoordinates = {1.0, 1.0};
        std::vector<std::vector<double>> allTrees = {{2.0, 3.0}, {5.0, 5.0}, {1.0, 2.0}, {3.0, 1.0}, {4.0, 4.0}};
        std::vector<double> allHeights = {95.0, 103.56, 97.22, 107.39, 108.22};
        int k = 1;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 3){
        std::vector<double> targetTreeCoordinates = {1.0, 1.0};
        std::vector<std::vector<double>> allTrees = {{2.0, 3.0}, {5.0, 5.0}, {1.0, 2.0}, {3.0, 1.0}, {4.0, 4.0}};
        std::vector<double> allHeights = {95.0, 103.56, 97.22, 107.39, 108.22};
        int k = 6;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 4){
        std::vector<double> targetTreeCoordinates = {1.0, 1.0};
        std::vector<std::vector<double>> allTrees = {{2.0, 3.0}, {5.0, 5.0}, {1.0, 2.0}, {3.0, 1.0}, {4.0, 4.0}};
        std::vector<double> allHeights = {95.0, 103.56, 97.22, 107.39, 108.22};
        int k = 4;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    } 
    else if( atoi( argv[1]) == 5){
        std::vector<double> targetTreeCoordinates = {1.0, 1.0};
        std::vector<std::vector<double>> allTrees = {{2.0, 3.0}, {5.0, 5.0}, {1.0, 2.0}, {3.0, 1.0}, {4.0, 4.0}};
        std::vector<double> allHeights = {95.0, 103.56, 97.22, 107.39, 108.22};
        int k = 5;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }
    else if( atoi( argv[1]) == 6){
        std::vector<double> targetTreeCoordinates = {10.0, 15.0};
        std::vector<std::vector<double>> allTrees = {{20.0, 25.0}, {12.0, 12.0}, {12.0, 16.0}, {13.0, 14.0}, {15.0, 15.0}, {10.0, 10.0}};
        std::vector<double> allHeights = {55.0, 65.4, 78.9, 88.2, 111.0, 98.0};
        int k = 7;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }
    else if( atoi( argv[1]) == 7){
        std::vector<double> targetTreeCoordinates = {10.0, 15.0};
        std::vector<std::vector<double>> allTrees = {{20.0, 25.0}, {12.0, 12.0}, {12.0, 16.0}, {13.0, 14.0}, {15.0, 15.0}, {10.0, 10.0}};
        std::vector<double> allHeights = {55.0, 65.4, 78.9, 88.2, 111.0, 98.0};
        int k = 1;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 8){
        std::vector<double> targetTreeCoordinates = {10.0, 15.0};
        std::vector<std::vector<double>> allTrees = {{20.0, 25.0}, {12.0, 12.0}, {12.0, 16.0}, {13.0, 14.0}, {15.0, 15.0}, {10.0, 10.0}};
        std::vector<double> allHeights = {55.0, 65.4, 78.9, 88.2, 111.0, 98.0};
        int k = 2;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 9){
        std::vector<double> targetTreeCoordinates = {10.0, 15.0};
        std::vector<std::vector<double>> allTrees = {{20.0, 25.0}, {12.0, 12.0}, {12.0, 16.0}, {13.0, 14.0}, {15.0, 15.0}, {10.0, 10.0}};
        std::vector<double> allHeights = {55.0, 65.4, 78.9, 88.2, 111.0, 98.0};
        int k = 3;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 10){
        std::vector<double> targetTreeCoordinates = {10.0, 15.0};
        std::vector<std::vector<double>> allTrees = {{20.0, 25.0}, {12.0, 12.0}, {12.0, 16.0}, {13.0, 14.0}, {15.0, 15.0}, {10.0, 10.0}};
        std::vector<double> allHeights = {55.0, 65.4, 78.9, 88.2, 111.0, 98.0};
        int k = 4;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 11){
        std::vector<double> targetTreeCoordinates = {10.0, 15.0};
        std::vector<std::vector<double>> allTrees = {{20.0, 25.0}, {12.0, 12.0}, {12.0, 16.0}, {13.0, 14.0}, {15.0, 15.0}, {10.0, 10.0}};
        std::vector<double> allHeights = {55.0, 65.4, 78.9, 88.2, 111.0, 98.0};
        int k = 5;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 12){
        std::vector<double> targetTreeCoordinates = {10.0, 15.0};
        std::vector<std::vector<double>> allTrees = {{20.0, 25.0}, {12.0, 12.0}, {12.0, 16.0}, {13.0, 14.0}, {15.0, 15.0}, {10.0, 10.0}};
        std::vector<double> allHeights = {55.0, 65.4, 78.9, 88.2, 111.0, 98.0};
        int k = 6;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 13){
        std::vector<double> targetTreeCoordinates = {0.0, 0.0};
        std::vector<std::vector<double>> allTrees = {{3.0, 3.0}, {2.0, 2.0}, {1.0, 1.0}, {5.0, 5.0}};
        std::vector<double> allHeights = {10.0, 20.0, 30.0, 40.0};
        int k = 5;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 14){
        std::vector<double> targetTreeCoordinates = {0.0, 0.0};
        std::vector<std::vector<double>> allTrees = {{3.0, 3.0}, {2.0, 2.0}, {1.0, 1.0}, {5.0, 5.0}};
        std::vector<double> allHeights = {10.0, 20.0, 30.0, 40.0};
        int k = 1;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 15){
        std::vector<double> targetTreeCoordinates = {0.0, 0.0};
        std::vector<std::vector<double>> allTrees = {{3.0, 3.0}, {2.0, 2.0}, {1.0, 1.0}, {5.0, 5.0}};
        std::vector<double> allHeights = {10.0, 20.0, 30.0, 40.0};
        int k = 2;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 16){
        std::vector<double> targetTreeCoordinates = {0.0, 0.0};
        std::vector<std::vector<double>> allTrees = {{3.0, 3.0}, {2.0, 2.0}, {1.0, 1.0}, {5.0, 5.0}};
        std::vector<double> allHeights = {10.0, 20.0, 30.0, 40.0};
        int k = 3;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 17){
        std::vector<double> targetTreeCoordinates = {0.0, 0.0};
        std::vector<std::vector<double>> allTrees = {{3.0, 3.0}, {2.0, 2.0}, {1.0, 1.0}, {5.0, 5.0}};
        std::vector<double> allHeights = {10.0, 20.0, 30.0, 40.0};
        int k = 4;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 18){
        std::vector<double> targetTreeCoordinates = {5.5, 5.5};
        std::vector<std::vector<double>> allTrees = {{6.5, 6.5}, {8.5, 5.5}, {4.5, 4.0}, {10.0, 0.0}, {5.0, 2.0}, {6.0, 4.0}};
        std::vector<double> allHeights = {10.0, 20.0, 10.5, 21.0, 10.0, 20.0};
        int k = 7;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 19){
        std::vector<double> targetTreeCoordinates = {5.5, 5.5};
        std::vector<std::vector<double>> allTrees = {{6.5, 6.5}, {8.5, 5.5}, {4.5, 4.0}, {10.0, 0.0}, {5.0, 2.0}, {6.0, 4.0}};
        std::vector<double> allHeights = {10.0, 20.0, 10.5, 21.0, 10.0, 20.0};
        int k = 1;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 20){
        std::vector<double> targetTreeCoordinates = {5.5, 5.5};
        std::vector<std::vector<double>> allTrees = {{6.5, 6.5}, {8.5, 5.5}, {4.5, 4.0}, {10.0, 0.0}, {5.0, 2.0}, {6.0, 4.0}};
        std::vector<double> allHeights = {10.0, 20.0, 10.5, 21.0, 10.0, 20.0};
        int k = 2;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }
    else if( atoi( argv[1]) == 21){
        std::vector<double> targetTreeCoordinates = {5.5, 5.5};
        std::vector<std::vector<double>> allTrees = {{6.5, 6.5}, {8.5, 5.5}, {4.5, 4.0}, {10.0, 0.0}, {5.0, 2.0}, {6.0, 4.0}};
        std::vector<double> allHeights = {10.0, 20.0, 10.5, 21.0, 10.0, 20.0};
        int k = 3;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 22){
        std::vector<double> targetTreeCoordinates = {5.5, 5.5};
        std::vector<std::vector<double>> allTrees = {{6.5, 6.5}, {8.5, 5.5}, {4.5, 4.0}, {10.0, 0.0}, {5.0, 2.0}, {6.0, 4.0}};
        std::vector<double> allHeights = {10.0, 20.0, 10.5, 21.0, 10.0, 20.0};
        int k = 4;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 23){
        std::vector<double> targetTreeCoordinates = {5.5, 5.5};
        std::vector<std::vector<double>> allTrees = {{6.5, 6.5}, {8.5, 5.5}, {4.5, 4.0}, {10.0, 0.0}, {5.0, 2.0}, {6.0, 4.0}};
        std::vector<double> allHeights = {10.0, 20.0, 10.5, 21.0, 10.0, 20.0};
        int k = 5;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }  
    else if( atoi( argv[1]) == 24){
        std::vector<double> targetTreeCoordinates = {5.5, 5.5};
        std::vector<std::vector<double>> allTrees = {{6.5, 6.5}, {8.5, 5.5}, {4.5, 4.0}, {10.0, 0.0}, {5.0, 2.0}, {6.0, 4.0}};
        std::vector<double> allHeights = {10.0, 20.0, 10.5, 21.0, 10.0, 20.0};
        int k = 6;
        cout << predict_tree_height(targetTreeCoordinates, allTrees, allHeights, k) << endl;
    }
    else if( atoi( argv[1]) == 25){
        std::vector<int> unwrap = {1, 3, 2};
        int k = 1;
        cout << k_wrapped_books(unwrap, k) << endl;
    }
    else if( atoi( argv[1]) == 26){
        std::vector<int> unwrap = {4, 1, 2, 3};
        int k = 2;
        cout << k_wrapped_books(unwrap, k) << endl;
    }  
    else if( atoi( argv[1]) == 27){
        std::vector<int> unwrap = {1,2,3};
        int k = 1;
        cout << k_wrapped_books(unwrap, k) << endl;
    }
    else if( atoi( argv[1]) == 28){
        std::vector<int> unwrap = {4,8,1,3,2,5,6,7};
        int k = 3;
        cout << k_wrapped_books(unwrap, k) << endl;
    }  
    else if( atoi( argv[1]) == 29){
        std::vector<int> unwrap = {4,8,1,3,2,5,6,7};
        int k = 2;
        cout << k_wrapped_books(unwrap, k) << endl;
    }  
    else if( atoi( argv[1]) == 30){
        std::vector<int> unwrap = {4,8,1,3,2,5,6,7};
        int k = 4;
        cout << k_wrapped_books(unwrap, k) << endl;
    }
    else if( atoi( argv[1]) == 31){
        std::vector<int> unwrap = {4,8,1,3,2,5,6,7};
        int k = 1;
        cout << k_wrapped_books(unwrap, k) << endl;
    }
    else if( atoi( argv[1]) == 32){
        std::vector<int> unwrap = {4,8,1,3,2,5,6,7};
        int k = 0;
        cout << k_wrapped_books(unwrap, k) << endl;
    }
    else if( atoi( argv[1]) == 33){
        std::vector<int> unwrap = {1,5,2,4,3};
        int k = 5;
        cout << k_wrapped_books(unwrap, k) << endl;
    }  
    else if( atoi( argv[1]) == 34){
        std::vector<int> unwrap = {1,5,2,4,3};
        int k = 3;
        cout << k_wrapped_books(unwrap, k) << endl;
    }
    else if( atoi( argv[1]) == 35){
        std::vector<int> unwrap = {1,5,2,4,3};
        int k = 2;
        cout << k_wrapped_books(unwrap, k) << endl;
    }
    else if( atoi( argv[1]) == 36){
        std::vector<int> unwrap = {1,5,2,4,3};
        int k = 0;
        cout << k_wrapped_books(unwrap, k) << endl;
    }  
    else if( atoi( argv[1]) == 37){
        std::vector<int> unwrap = {1,5,2,4,3};
        int k = 1;
        cout << k_wrapped_books(unwrap, k) << endl;
    }
    else if( atoi( argv[1]) == 38){
        std::vector<int> unwrap = {10,6,1,4,8,9,2,3,5,7};
        int k = 3;
        cout << k_wrapped_books(unwrap, k) << endl;
    }  
    else if( atoi( argv[1]) == 39){
        std::vector<int> unwrap = {10,6,1,4,8,9,2,3,5,7};
        int k = 4;
        cout << k_wrapped_books(unwrap, k) << endl;
    } 
    else if( atoi( argv[1]) == 40){
        std::vector<int> unwrap = {10,6,1,4,8,9,2,3,5,7};
        int k = 2;
        cout << k_wrapped_books(unwrap, k) << endl;
    } 
    else if( atoi( argv[1]) == 41){
        std::vector<int> unwrap = {10,6,1,4,8,9,2,3,5,7};
        int k = 1;
        cout << k_wrapped_books(unwrap, k) << endl;
    } 
    else if( atoi( argv[1]) == 42){
        std::vector<int> unwrap = {10,6,1,4,8,9,2,3,5,7};
        int k = 0;
        cout << k_wrapped_books(unwrap, k) << endl;
    }
    else if( atoi( argv[1]) == 43){
        std::vector<int> unwrap = {10,6,1,4,8,9,2,3,5,7};
        int k = 7;
        cout << k_wrapped_books(unwrap, k) << endl;
    } 
    else if( atoi( argv[1]) == 44){
        std::vector<int> unwrap = {5,8,6,7,1,3,4,2};
        int k = 2;
        cout << k_wrapped_books(unwrap, k) << endl;
    } 
    else if( atoi( argv[1]) == 45){
        std::vector<int> unwrap = {5,8,6,7,1,3,4,2};
        int k = 1;
        cout << k_wrapped_books(unwrap, k) << endl;
    } 
    else if( atoi( argv[1]) == 46){
        std::vector<int> unwrap = {5,8,6,7,1,3,4,2};
        int k = 0;
        cout << k_wrapped_books(unwrap, k) << endl;
    } 
    else if( atoi( argv[1]) == 47){
        std::vector<int> unwrap = {5,8,6,7,1,3,4,2};
        int k = 3;
        cout << k_wrapped_books(unwrap, k) << endl;
    } 
    else if( atoi( argv[1]) == 48){
        std::vector<int> unwrap = {5,8,6,7,1,3,4,2};
        int k = 4;
        cout << k_wrapped_books(unwrap, k) << endl;
    } 
    else if( atoi( argv[1]) == 49){
        std::vector<int> unwrap = {1,2,3};
        int k = 0;
        cout << k_wrapped_books(unwrap, k) << endl;
    }  
    else if( atoi( argv[1]) == 50){
        std::string bracelet = "ccbbaa";
        int k = 3;
        cout << rearrange_bracelet(bracelet, k) << endl;
    } 
    else if( atoi( argv[1]) == 51){
        std::string bracelet = "eeefg";
        int k = 3;
        cout << rearrange_bracelet(bracelet, k) << endl;
    } 
    else if( atoi( argv[1]) == 52){
        std::string bracelet = "eeefg";
        int k = 2;
        cout << rearrange_bracelet(bracelet, k) << endl;
    } 
    else if( atoi( argv[1]) == 53){
        std::string bracelet = "aaadbbcc";
        int k = 3;
        cout << rearrange_bracelet(bracelet, k) << endl;
    } 
    else if( atoi( argv[1]) == 54){
        std::string bracelet = "ccbbaa";
        int k = 2;
        cout << rearrange_bracelet(bracelet, k) << endl;
    } 
    else if( atoi( argv[1]) == 55){
        std::string bracelet = "bcdedbb";
        int k = 2;
        cout << rearrange_bracelet(bracelet, k) << endl;
    } 
    else if( atoi( argv[1]) == 56){
        std::string bracelet = "bcdedbb";
        int k = 3;
        cout << rearrange_bracelet(bracelet, k) << endl;
    } 
    else if( atoi( argv[1]) == 57){
        std::string bracelet = "bcdedbbec";
        int k = 4;
        cout << rearrange_bracelet(bracelet, k) << endl;
    } 
    else if( atoi( argv[1]) == 58){
        std::string bracelet = "ajjabba";
        int k = 2;
        cout << rearrange_bracelet(bracelet, k) << endl;
    } 
    else if( atoi( argv[1]) == 59){
        std::string bracelet = "ajjabba";
        int k = 3;
        cout << rearrange_bracelet(bracelet, k) << endl;
    } 
     else if( atoi( argv[1]) == 60){
        std::string bracelet = "jkjkffjk";
        int k = 3;
        cout << rearrange_bracelet(bracelet, k) << endl;
    } 
    else if( atoi( argv[1]) == 61){
        std::string bracelet = "jkjkffjk";
        int k = 2;
        cout << rearrange_bracelet(bracelet, k) << endl;
    } 
    else if( atoi( argv[1]) == 62){
        std::string bracelet = "pggwswp";
        int k = 3;
        cout << rearrange_bracelet(bracelet, k) << endl;
    }
    else if( atoi( argv[1]) == 63){
        std::string bracelet = "pggwswp";
        int k = 4;
        cout << rearrange_bracelet(bracelet, k) << endl;
    }
    else if( atoi( argv[1]) == 64){
        std::string bracelet = "pggwswp";
        int k = 5;
        cout << rearrange_bracelet(bracelet, k) << endl;
    }
    else if( atoi( argv[1]) == 65){
        std::string bracelet = "igwiwatt";
        int k = 5;
        cout << rearrange_bracelet(bracelet, k) << endl;
    }
    else if( atoi( argv[1]) == 66){
        std::string bracelet = "abbccj";
        int k = 2;
        cout << rearrange_bracelet(bracelet, k) << endl;
    }
    else if( atoi( argv[1]) == 67){
        std::string bracelet = "abbccj";
        int k = 3;
        cout << rearrange_bracelet(bracelet, k) << endl;
    }
    else if( atoi( argv[1]) == 68){
        std::string bracelet = "abbccj";
        int k = 4;
        cout << rearrange_bracelet(bracelet, k) << endl;
    }
    else if( atoi( argv[1]) == 69){
        std::string bracelet = "abbccj";
        int k = 5;
        cout << rearrange_bracelet(bracelet, k) << endl;
    }
    else if( atoi( argv[1]) == 70){
        std::string bracelet = "ghghjhg";
        int k = 2;
        cout << rearrange_bracelet(bracelet, k) << endl;
    }
    else if( atoi( argv[1]) == 71){
        std::string bracelet = "lmnjjk";
        int k = 4;
        cout << rearrange_bracelet(bracelet, k) << endl;
    }
    else if( atoi( argv[1]) == 72){
        std::string bracelet = "lmnjjk";
        int k = 5;
        cout << rearrange_bracelet(bracelet, k) << endl;
    }
    else if( atoi( argv[1]) == 73){
        std::string bracelet = "lmnjjkc";
        int k = 6;
        cout << rearrange_bracelet(bracelet, k) << endl;
    }
    else if( atoi( argv[1]) == 74){
        std::string bracelet = "ywfyggt";
        int k = 5;
        cout << rearrange_bracelet(bracelet, k) << endl;
    }
    else if( atoi( argv[1]) == 75){
        std::string text = "ssiencss";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 76){
        std::string text = "ababab";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 77){
        std::string text = "sciences";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 78){
        std::string text = "aaaaa";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 79){
        std::string text = "abbabba";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 80){
        std::string text = "abcdefg";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 81){
        std::string text = "ababababab";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 82){
        std::string text = "abababab";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 83){
        std::string text = "ababab";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 84){
        std::string text = "babab";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 85){
        std::string text = "bababa";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 86){
        std::string text = "baba";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 87){
        std::string text = "bbbcccbbb";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 88){
        std::string text = "bbbcccbb";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 89){
        std::string text = "bbbcccb";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 90){
        std::string text = "bbbbbb";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 91){
        std::string text = "bbcbb";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 92){
        std::string text = "cgacga";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 93){
        std::string text = "acgacga";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 94){
        std::string text = "ffgffgffg";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 95){
        std::string text = "ffgffg";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 96){
        std::string text = "jklljk";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 97){
        std::string text = "ccggcc";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 98){
        std::string text = "ccgc";
        cout << second_longest_prefix(text) << endl;
    }
    else if( atoi( argv[1]) == 99){
        std::string text = "jjarjj";
        cout << second_longest_prefix(text) << endl;
    }
    return 0; 
    
}
