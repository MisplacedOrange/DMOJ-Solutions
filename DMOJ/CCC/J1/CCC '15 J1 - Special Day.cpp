// w c++
#include <bits/stdc++.h>
#include <iostream>
using namespace std; int main() {int month = 0; int day = 0; cin >> month >> day; if (month > 2) {cout << "After";} else if (month < 2) {cout << "Before";} else if (month == 2) {if (day < 18) {cout << "Before";} else if (day > 18) {cout <<"After";} else {cout << "Special";}}}
