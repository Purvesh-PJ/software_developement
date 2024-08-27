// main.cpp
#include <iostream>

namespace numbers {

    class autoNum {
        private: 
            int num = 5;
        public:
            void giveNum(){
                std::cout << "num : " << num << std::endl;
            }

            void setNum(int num){
                this->num = num;
            }
    };

    void printNumbers(int count) {
        for (int i = 1; i <= count; ++i) {
            std::cout << "Number: " << i << std::endl;
        }
    }
}


int main() {
    int num = 5; // Change this value to test different inputs

    numbers::printNumbers(num);

    numbers::autoNum obj;
    obj.giveNum();
    obj.setNum(7);
    obj.giveNum();
    return 0;
}
