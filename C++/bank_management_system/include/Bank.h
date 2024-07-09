#ifndef BANK_H
#define BANK_H
#include <vector>
#include "Account.h"

class Bank {
    
    public:
    
    void createAccount(const Account& account);
    void deposit(int AccountNumber, double balance);
    bool withdraw(int AccountNumber, double balance);
    void displayAccountDetails(int AccountNumber) const;
    void displayAllAccounts() const;

    private:
    
    std::vector <Account> accounts;
    Account* findAccount(int AccountNumber);
    const Account* findAccount(int accountNumber) const; 
    
};

#endif