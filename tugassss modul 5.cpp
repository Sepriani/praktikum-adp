#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> A, B;
    int num;

    // Mengisi array A
    cout << "Masukkan elemen array A (0-9, ketik -1 untuk berhenti): ";
    while (true) {
        cin >> num;
        if (num == -1) break;
        A.push_back(num);
    }

    // Mengisi array B
    cout << "Masukkan elemen array B (0-9, ketik -1 untuk berhenti): ";
    while (true) {
        cin >> num;
        if (num == -1) break;
        B.push_back(num);
    }

    // Mencari elemen yang hanya ada di A
    vector<int> onlyInA;
    for (int i : A) {
        if (find(B.begin(), B.end(), i) == B.end()) {
            onlyInA.push_back(i);
        }
    }

    // Mencari elemen yang hanya ada di B
    vector<int> onlyInB;
    for (int i : B) {
        if (find(A.begin(), A.end(), i) == A.end()) {
            onlyInB.push_back(i);
        }
    }

    // Mencari elemen yang ada di A dan B
    vector<int> inAandB;
    for (int i : A) {
        if (find(B.begin(), B.end(), i) != B.end()) {
            inAandB.push_back(i);
        }
    }

    // Menampilkan hasil
    cout << "Elemen yang hanya ada di A: ";
    for (int i : onlyInA) {
        cout << i << " ";
    }
    cout << endl;

    cout << "Elemen yang hanya ada di B: ";
    for (int i : onlyInB) {
        cout << i << " ";
    }
    cout << endl;

    cout << "Elemen yang ada di A dan B: ";
    for (int i : inAandB) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}