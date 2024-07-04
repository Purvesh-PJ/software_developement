#ifndef TASKMANAGER_H
#define TASKMANAGER_H

#include "Task.h"
#include <vector>
#include <string>

class TaskManager {
    private:
    std::vector<Task> tasks;
    int nextId;

    public:
    TaskManager();

    void addTask(const std::string& description);
    void viewTasks() const;
    void deleteTask(int id);

};

#endif