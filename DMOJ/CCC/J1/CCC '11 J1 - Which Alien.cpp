// w c++
#include <bits/stdc++.h>
#include <iostream>
using namespace std; 
int main() {
    int attena = 0; int eyes = 0;
    cin >> attena >> eyes;

    if ((attena >= 3) && (eyes <= 4)) {
        cout << "TroyMartian" << endl;
        if ((attena <= 6) && (eyes >= 2)) {
        cout << "VladSaturnian" << endl;
        } else if ((attena <= 2) && (eyes <= 3)) {
        cout << "GraemeMercurian" << endl;
    }
    } else if ((attena <= 6) && (eyes >= 2)) {
        cout << "VladSaturnian" << endl;
        if ((attena <= 2) && (eyes <= 3)) {
        cout << "GraemeMercurian"<<endl;}
    } else if ((attena <= 2) && (eyes <= 3)) {
        cout << "GraemeMercurian"<<endl;
    }
}