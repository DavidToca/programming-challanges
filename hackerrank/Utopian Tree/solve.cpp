#include <bits/stdc++.h>

using namespace std;

// Complete the utopianTree function below.
int utopianTree(int n, vector<int> cycles) {
    return cycles[n];
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<int> cycles(61);
    cycles[0] = 1;
    for(int i=1; i<61;i++){
        if(i%2==0){
            cycles[i] = cycles[i-1] + 1;
        }
        else{
            cycles[i] = cycles[i-1] *2;
        }
    }

    for (int t_itr = 0; t_itr < t; t_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');


        int result = utopianTree(n, cycles);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

