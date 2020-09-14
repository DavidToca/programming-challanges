#include <iostream>

using namespace std;

int main(){
    
    long long n, a, last;

    cin >> n;

    if(n == 0){
        cout << "Ordenado";
    }
    cin >> last;
    n = n + 1;
    for(int i=1;i<n;i++){
        cin >> a;
        
        if(last > a){
            cout << "Desordenado";
            return 0;
        }
        last = a;
    }

    cout << "Ordenado";
    return 0;
}
