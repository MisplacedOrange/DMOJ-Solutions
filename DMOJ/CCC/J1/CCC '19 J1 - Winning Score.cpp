#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {

    int x, y, z, a, b, c;
    cin >> x >> y >> z;
    cin >> a >> b >> c;

    int atotal = x*3+y*2+z;
    int btotal = a*3+b*2+c;

    if (atotal > btotal) {
        cout << 'A';
    } else if (atotal < btotal) {
        cout << 'B';
    } else {
        cout << 'T';
    }


}
