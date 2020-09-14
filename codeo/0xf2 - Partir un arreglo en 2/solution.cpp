#include <iostream>
#include <cstdio>

using namespace std;

int main(){

    int n;
    cin >> n;
    int a[n];
    int s[n];
    for(int i=0;i<n;i++){
        cin >> a[i];
    }
    int suma = 0;
//    cout<<endl;
    for(int i=0;i<n;i++){
        suma+=a[i];
        s[i] = suma;
  //      cout << suma<< " ";
    }
    //cout <<endl;
    bool solution = false;
    for(int i=0;i<n-1;i++){
        if(s[i]<=0){
            continue;
        }

        int right = s[n-1] - s[i];
        if (right<0){
            cout << i+1 <<endl;
            solution = true;
            break;
        }

    }

    if (!solution){
        cout << "Impossible" <<endl;
    }

    return 0;
}
