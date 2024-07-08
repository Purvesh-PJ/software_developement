#include "../include/Task.h"
#include <iostream>

Task::Task(int id, const std::string& description) : id(id), description(description), isCompleted(false) {};

void Task::markAsCompleted(){
    isCompleted = true;
}

void Task::display() const {
    std::cout << id << ": " << description << (isCompleted ? "[Completed]" : "") << std::endl;
}