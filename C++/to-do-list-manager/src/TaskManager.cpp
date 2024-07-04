#include "../include/TaskManager.h"
#include <algorithm>
#include <iostream>

TaskManager::TaskManager() : nextId(1) {};

void TaskManager::addTask(const std::string& description){
    tasks.push_back(Task(nextId++, description));
};

void TaskManager::viewTasks() const{
    for(const auto& task : tasks){
        task.display();
    }
};

void TaskManager::deleteTask(int id){
    tasks.erase(std::remove_if(tasks.begin(), tasks.end(), [id](const Task& task)
    { 
        return task.getId() == id; 
    }),
    tasks.end());
};