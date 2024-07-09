#include <iostream>
#include "../include/Bank.h"
#include "../include/Account.h"


int main (){
    
    int number, accountNumber;
    std::string name;
    double amount;
    Bank bank;

    do {
        std::cout << "========== BANK MANAGEMENT SYSTEM ==========" << std::endl;
        std::cout << "1] Create Account \n";
        std::cout << "2] Deposit Money \n";
        std::cout << "3] Withdraw Money \n";
        std::cout << "4] View Account Details \n";
        std::cout << "5] View All Accounts \n";
        std::cout << "6] Exit \n";
        std::cout << "============================================" << std::endl;
        std::cout << "Choose a number : ";
        std::cin >> number;

        switch (number) {
            case 1: {
                std::cout << "Enter a account number: ";
                std::cin >> accountNumber;
                std::cin.ignore(); // Ignore newline character
                std::cout << "Enter name: ";
                std::getline(std::cin, name);
                std::cout << "Enter initial balance: ";
                std::cin >> amount;
                bank.createAccount(Account(accountNumber, name, amount));
                break;
            }
            case 2: {
                std::cout << "Enter account number: ";
                std::cin >> accountNumber;
                std::cout << "Enter amount to deposit: ";
                std::cin >> amount;
                bank.deposit(accountNumber, amount);
                break;
            }
            case 3: {
                std::cout << "Enter account number: ";
                std::cin >> accountNumber;
                std::cout << "Enter amount to withdraw: ";
                std::cin >> amount;
                bank.withdraw(accountNumber, amount);
                break;
            }
            case 4: {
                std::cout << "Enter account number: ";
                std::cin >> accountNumber;
                bank.displayAccountDetails(accountNumber);
                break;
            }
            case 5: {
                bank.displayAllAccounts();
                break;
            }
         
        }
        
    } while(number != 6);

    return 0;
}