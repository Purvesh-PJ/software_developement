#include "../include/TaskManager.h"
#include <iostream>

int main () {
    
    TaskManager manager;
    int choice;

        do {
            std::cout << "########## TASK MANAGER ##########" << '\n';
            std::cout << "1] Add task\n2] View tasks\n3] Delete task\n4] Exit \n";
            std::cout << "##################################" << '\n';
            std::cout << "Enter a choice :" << std::endl;
            std::cin >> choice;

            switch (choice) {
                case 1: {
                    std::cin.ignore();
                    std::string description;
                    std::cout << "Enter Description: ";
                    std::getline(std::cin, description);
                    manager.addTask(description);
                    break;
                }

                case 2: {
                    manager.viewTasks();
                    break;
                }

                case 3: {
                    int id;
                    std::cout << "Enter task id to delete: ";
                    std::cin >> id;
                    manager.deleteTask(id);
                    break;
                }
            }
        } while(choice != 4);

    return 0;
}

/*
    Command for running program : g++ -I../include -o main main.cpp Task.cpp TaskManager.cpp
*/