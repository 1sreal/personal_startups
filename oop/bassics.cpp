#include <iostream>
using namespace std;
//a short program that takes the users age and returns the year they were born

 
int main(){
    int c_year, c_age, b_year;
    c_year = 2023;
    cout << "Enter your age: "<< endl;
    cin >> c_age;
    b_year = c_year - c_age;
    cout<< "Your year of birth is "<< b_year<< endl;
    return 0;
}