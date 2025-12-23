#include <bits/stdc++.h>
using namespace std;

int main() {
	
    int check1=0;int check2=0;int check3=0;
    cin >> check1 >> check2 >> check3;
    int check0 = check1 + check2;
    
    if (check0 >= check3) {
        cout << check0;
        return 0;
    } else {
        check0 += check2;
        if (check0 >= check3) {
            cout << check0;
            return 0;
        } else {
            check0 += check2;
            if (check0 >= check3) {
                cout << check0;
                return 0;
            } else {
                cout << "Who knows...";
                return 0;
            }
    }
    }
    // Who knows...
}
