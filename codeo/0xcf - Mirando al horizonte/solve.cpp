#include <iostream>
#include <list>
using namespace std;

int main(){
  int c, n;
  cin >> c;
  for(int i=0; i<c;i++){
    cin >> n;
    int input[n];
    int output[n];

    for(int j=0; j<n; j++){ 
      cin >> input[j];
    }

    list<int> stack;

    for(int j=n-1;j>=0;j--){
      int current = input[j];
      output[j] = -1;
      while(!stack.empty()){

        int taller = stack.front();

        if(current < taller){
          output[j] = taller;
          break;
        } else{
          stack.pop_front();
        }

      }

      stack.push_front(current);

    }

    cout << "Case #" << i+1 << ":";
    for(int j=0; j<n; j++){
        cout << " " << output[j]; 
    }
    cout << endl;

  }
}
