#ifndef TASK_H
#define TASK_H

#include <string>

class Task {
    int id;
    public:
    int getId() const { return id; }
    std::string description;
    bool isCompleted;

    Task(int id, const std::string& description);

    void markAsCompleted();
    void display() const;


};

#endif