// w c++
#include <bits/stdc++.h>
#include <iostream>
using namespace std; 
int main() {
    int limit = 0; int speed = 0;int difference = 0;
    cin >> limit >> speed;
    difference = speed - limit;

    if (speed <= limit) {
        cout << "Congratulations, you are within the speed limit!";
    } else if ((difference >= 1) && (difference <= 20)) {
        cout << "You are speeding and your fine is $100.";
    } else if ((difference >= 21) && (difference <= 30)) {
        cout << "You are speeding and your fine is $270.";
    } else if (difference >= 31) {
        cout << "You are speeding and your fine is $500.";
    }
}
