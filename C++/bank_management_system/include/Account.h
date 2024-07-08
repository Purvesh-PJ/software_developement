#ifndef ACCOUNT_H
#define ACCOUNT_H

#include <string>

class Account {

    private:
        int AccountNumber;
        std::string name;
        double balance;

    public:
        Account();
        Account(int AccountNumber, const std::string& name, double balance);

        void deposit(double amount);
        bool withdraw(double amount);

        int getAccountNumber() const;
        std::string getName() const;
        double getBalance() const;
        void displayAccountDetails();
};


#endif;