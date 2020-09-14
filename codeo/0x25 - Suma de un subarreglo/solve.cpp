#include <iostream>
#include <map>

using namespace std;

int main() {
  int len, c, q, p;
  cin >> len;
  int output[len];
  int current;

  cin >> output[0];
  for(int i=1;i<len; i++){
    int current;
    cin >> current;
    output[i] = current + output[i-1];
  }

  cin >> c;

  for(int i=0; i<c;i++){
    cin >> q;
    cin >> p;

    if(q == 0){
      cout << output[p] << endl;
    }
    else{
      cout << output[p] - output[q-1] << endl;
    }
  }

}
