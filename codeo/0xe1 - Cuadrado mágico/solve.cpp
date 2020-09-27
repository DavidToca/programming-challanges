#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n, sum, magic=-1;
  cin >> n;

  int square[n][n];

  vector<int> cols(n, 0);
  vector<int> rows(n, 0);
  int diag1=0, diag2=0;

  for(int row=0;row<n;row++){
    for(int col=0;col<n;col++){
      cin >> square[row][col];
      int current = square[row][col];
      cols[col] += current;
      rows[row] += current;
      if(row==col){
        diag1+=current;
      }

      if(col== (n-1-row) ){
        diag2+=current;
      }

    }
  }

  magic = diag1;

  if(magic != diag2){
    cout << "No";
    return 0;
  }

  for(int i=0;i<n;i++){
    if(rows[i]!=magic){
      cout << "No";
      return 0;
    }
    if(cols[i]!=magic){
      cout << "No";
      return 0;
    }
  }
  cout << "Yes";

}
