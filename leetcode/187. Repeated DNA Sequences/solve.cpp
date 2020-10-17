#include <map>
using namespace std;


class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> answer;
        if(s.size() <=10){
            return answer;
        }
        
        int options = s.size() - 9;
        
        map<string, int> d;
        
        for(int i=0;i<options;i++){
            string substring = s.substr(i,10);
            d[substring] +=1;
        }
        
        for(auto &x:d){
            if(x.second > 1){
                answer.push_back(x.first);
            }
        }
	    
        return answer;
        
        
    }
};
