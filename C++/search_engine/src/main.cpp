// main.cpp
#include <iostream>

void printNumbers(int count) {
    for (int i = 1; i <= count; ++i) {
        std::cout << "Number: " << i << std::endl;
    }
}

int main() {
    int num = 5; // Change this value to test different inputs
    std::cout << "Starting the program..." << std::endl;

    printNumbers(num);

    std::cout << "Ending the program." << std::endl;
    return 0;
}
