#include <bits/stdc++.h>
#include <iostream>
#include <string>
using namespace std;

int main() {

    string prev,n;

    
    while (cin >> n && n != "99999") {
        
        while (n.length() < 5) n = "0" + n;

        int a = n[0] - '0';
        int b = n[1] - '0';
        string cde = n.substr(2, 3); 
        string rightorleft;

        if (a == 0 && b == 0) {
            rightorleft = prev;
        } else {
            rightorleft = ((a+b) % 2 == 0) ? "right" : "left";
            prev = rightorleft;
        }
        cout << rightorleft << " " << cde << "\n";
    }
        
}
