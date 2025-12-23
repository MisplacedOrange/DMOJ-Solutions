#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {

    int n, store = 0;
    cin >> store;
    
     while (cin >> n) {
        if (store > n) {
            store += n;
        } else {
            cout << store;
            break;
        }
        
     }
}
