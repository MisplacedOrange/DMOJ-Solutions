// w c++
#include <bits/stdc++.h>
#include <iostream>
using namespace std; 
int main() {
    // More than 25 Overweight
    // Between 18.5 and 25 (inclusive) Normal weight
   //Less than 18.5 Underweight

   double w = 0; double h = 0;

   cin >> w >> h;

   double bmi = w / (h*h);

   if (bmi > 25) {
        cout << "Overweight";
   } else if (bmi < 18.5) {
        cout << "Underweight";
   } else {
        cout << "Normal weight";
   }


   

  

}
