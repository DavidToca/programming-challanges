const int min_int = -2147483648;
const int max_int = 2147483647;

using namespace std;

class Solution {
public:
    int reverse(int x) {
        string a = to_string(x);
        string sign = "";
        if(a[0] == '-'){
            sign = "-";
            a = a.substr(1);
        }
        std::reverse(a.begin(), a.end());

        sign.append(a);
        
        long answer = stol(sign);
        
        if(answer < min_int){
            return 0;
        }
        if(answer > max_int){
            return 0;
        }
        return int(answer);
    }
};