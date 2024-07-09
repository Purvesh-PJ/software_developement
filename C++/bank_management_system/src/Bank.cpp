#include <iostream>
#include "../include/Bank.h"

void Bank::createAccount(const Account& account){
    accounts.push_back(account);
}

void Bank::deposit(int AccountNumber, double balance){
    Account* account = findAccount(AccountNumber);
    if(account != nullptr){
        account->deposit(balance);
    }
    else {
        std::cerr << "Account not found" << std::endl;
    }
}

bool Bank::withdraw(int AccountNumber, double balance){
    Account* account = findAccount(AccountNumber);
    if(account != nullptr){
        return account->withdraw(balance);
    }
    else {
        std::cerr << "Account not found" << std::endl;
        return false;
    }
}

void Bank::displayAccountDetails(int AccountNumber) const {
    const Account* account = findAccount(AccountNumber);
    if(account != nullptr){
        account->displayAccountDetails();
    }
    else {
        std::cerr << "Account not found." << std::endl;
    }
}

void Bank::displayAllAccounts() const {
    for(const auto& account : accounts){
        account.displayAccountDetails();
        std::cout << "-------------------------" << std::endl;
    }
}

Account* Bank::findAccount(int AccountNumber){
    for(auto& account : accounts){
        if(account.getAccountNumber() == AccountNumber){
            return &account;
        }
    }
    return nullptr;
}

const Account* Bank::findAccount(int accountNumber) const {
    for(const auto& account : accounts){
        if(account.getAccountNumber() == accountNumber){
            return &account;
        }
    }
    return nullptr;
}