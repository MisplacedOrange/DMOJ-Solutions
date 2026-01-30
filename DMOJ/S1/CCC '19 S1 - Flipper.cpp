#include <bits/stdc++.h>
#include <iostream>
#include <string>
using namespace std;

int main() {


    string sus;
    cin >> sus;

    int H = 0, V = 0;
    for (char c : sus) {
        if (c == 'H') {
            H++;
        } else {
            V++;
        }
    }

    H %= 2;
    V %= 2;

    if (H == 0 && V == 0) {
        cout << "1 2\n3 4\n";
    } else if (H == 1 && V == 0) {
        cout << "3 4\n1 2\n";
    } else if (H == 0 && V == 1) {
        cout << "2 1\n4 3\n";
    } else {
        cout << "4 3\n2 1\n";
    }

}
