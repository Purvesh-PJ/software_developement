#include <iostream>


int main (){
    
    int number;

    do {
        std::cout << "========== BANK MANAGEMENT SYSTEM ==========" << std::endl;
        std::cout << "1] Create new accounts \n";
        std::cout << "2] View account details \n";
        std::cout << "3] Deposit money \n";
        std::cout << "4] Withdraw money \n";
        std::cout << "5] View all accounts \n";
        std::cout << "6] Exit \n";
        std::cout << "============================================" << std::endl;
        std::cout << "Choose a number : ";
        std::cin >> number;

        switch (number) {
            case 1: {
                break;
            }
            case 2: {
                break;
            }
            case 3: {
                break;
            }
            case 4: {
                break;
            }
            case 5: {
                break;
            }
         
        }
        
    } while(number != 6);

    return 0;
}