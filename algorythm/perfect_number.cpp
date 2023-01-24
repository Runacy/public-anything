#include <iostream>

template<class T> void print(const T& value) {
  std::cout << value << std::endl;
}


class Solution {
public:
    bool checkPerfectNumber(int num) {
        int sum = 0;

        for(int i=1;i<num/2+1;i++){
            if(num%i==0){ //約数かどうか判定する
                sum+=i;
            };
        }
        

        return sum == num;
        
    }
};