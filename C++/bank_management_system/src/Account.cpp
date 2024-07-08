#include "Account.h"
#include <iostream>

using namespace std;

Account::Account() : AccountNumber(0), name(""), balance(0.0) {}
Account::Account(int AccountNumber, const std::string& name, double balance) : AccountNumber(AccountNumber), name(name), balance(balance) {}

void Account::deposit(double amount){

}

bool Account::withdraw(double amount){

}

int Account::getAccountNumber() const{

}

string Account::getName() const {

}

double Account::getBalance() const {

}

void Account::displayAccountDetails(){
}

void Account::displayAccountDetails() {

}