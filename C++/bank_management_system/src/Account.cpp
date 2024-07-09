#include "../include/Account.h"
#include <iostream>

using namespace std;

Account::Account() : AccountNumber(0), name(""), balance(0.0) {}
Account::Account(int AccountNumber, const std::string& name, double balance) : AccountNumber(AccountNumber), name(name), balance(balance) {}

void Account::deposit(double amount){
    balance += amount;
}

bool Account::withdraw(double amount){
    if(amount < balance){
        std::cerr << "Insufficient funds." << std::endl;
        return false;
    }
    balance -= amount;
    return true;
}

int Account::getAccountNumber() const{
    return AccountNumber;
}

string Account::getName() const {
    return name;
}

double Account::getBalance() const {
    return balance;
}

void Account::displayAccountDetails() const {
    std::cout << "Account Number: " << AccountNumber << std::endl;
    std::cout << "Name: " << name << std::endl;
    std::cout << "Balance: $" << balance << std::endl;
}

