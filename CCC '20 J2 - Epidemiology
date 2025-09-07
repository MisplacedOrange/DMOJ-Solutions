#include <bits/stdc++.h>
using namespace std;

int main() {
	
    int p,n,r;
    
    cin >> p >> n >> r;

    int infect = n;
    int sum = infect;
    int days = 0;

    while (p >= sum) {
        infect *=r;
        sum += infect;
        days++;
    }
    cout << days;
}
