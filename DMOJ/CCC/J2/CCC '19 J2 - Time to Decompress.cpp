#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int num;
        string symbol;
        cin >> num >> symbol; 
        for (int o = 0; o < num; o++) {
             cout << symbol;
        }
        cout << "\n";
    }
}
