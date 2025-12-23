#include <bits/stdc++.h>
using namespace std;

int main() {
	
    int s,m,l;
    cin >> s;
    cin >> m;
    cin >> l;

    int mood = 1*s+2*m+3*l;

    if (mood >= 10) {
        cout << "happy";
    } else {
        cout << "sad";
    }

}
