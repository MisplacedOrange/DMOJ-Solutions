#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {

    int p, score;
    cin >> p;

    vector<int> scores;
    set<int> everyscore;

    for (int i = 0; i < p; i++) {
        cin >> score;
        scores.push_back(score);
        everyscore.insert(score);
    }

    auto it = everyscore.rbegin();
    advance(it, 2);                 
    int third = *it; 

    int tie = 0;
    for (int s : scores) {
        if (s == third) tie++;
    }

    cout << third << " " << tie;

}
