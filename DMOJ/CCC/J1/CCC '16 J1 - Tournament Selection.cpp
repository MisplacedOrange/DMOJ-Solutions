// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
    char game;
    int count = 0;
    int group = 0;
	while (cin >> game) {
        if (game == 'W') {
            count++;
        }
        if (count == 0){
            group = -1;
        } else if (count == 1 ||count == 2) {
            group = 3;
        } else if (count == 3 ||count == 4) {
            group = 2;
        }
        else if (count == 5 ||count == 6) {
            group = 1;
        }
    }
    cout << group;
}
