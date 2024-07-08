#ifndef BANK_H
#define BANK_H

#include <vector>
#include "Account.h"

class Bank {
    
    public:
    
    void createAccount(const Account& account);
    void deposit(int AccountNumber, double balance);
    bool withdraw(int AccountNumber, double balance);
    void accountDetails(int AccountNumber) const;
    void displayAllAccounts() const;

    private:
    
    std::vector <Account> accounts;
    Account* findAccount(int AccountNumber);
    
};

#endif;