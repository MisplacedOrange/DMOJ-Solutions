#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {

    int x,y,z = 1,t = 0;

    cin >> x >> y;

    for (int i = 0; i <= y; i++){
        t += x*z; 
        z *= 10;
    }
    cout << t;
}

    

