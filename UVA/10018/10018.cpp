* Ernesto Carrion 
   Accepted
   carrion.silver@gmail.com */


#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <sstream>

using namespace std;


long long toL(string s){
  return atol(s.c_str());
}

string toS (long long l){
  stringstream ss;
  ss << l;
  return ss.str(); 
}

int main(){

  int cases, iterations = 0;
  long long number;
  string in, rev;

  cin >> cases;
  while (cases){
    cin >> in;
    number = toL(in);
    rev = in;
    reverse (rev.begin(), rev.end());
    while (in != rev || iterations == 0){
      //cout << in << " " << rev << endl;
      number += toL(rev);
      //cout << number << endl;
      in = toS(number);
      rev = in;
      //cout << in << " " << rev << endl;
      reverse(rev.begin(), rev.end());
      iterations++;
    }
    cout << iterations << " " << rev << endl;
    iterations = 0;
    cases--;
  }


  return 0;
}
