#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {

    int x,y,a,b,d;
    cin >> x >> y >> a >> b >> d;

    int m = abs(x - a) + abs(y - b);

    if ((d >= m) && (d - m) % 2 == 0) {
        cout << 'Y';
    } else {
        cout << 'N';
    }
}
