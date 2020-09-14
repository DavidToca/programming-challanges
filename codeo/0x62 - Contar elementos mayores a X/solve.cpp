#include <iostream>
#include <cstdio>

using namespace std;

int main(){

    int n,c,x;

    cin >> n;

    int a[n];
    for(int i=0;i<n;i++){
        cin >> a[i];
    }
    cin >> c;
    for(int i=0;i<c;i++){
        cin >> x;
        int r = 0;
        for(int j=0;j<n;j++){
            if(a[j]> x){
                r++;
            }
        }
        cout << r <<endl;
    }

    return 0;
}
