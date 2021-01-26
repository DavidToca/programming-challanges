class Solution {
public:
    int romanToInt(string s) {

        map<char, int> equivalence {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        reverse(s.begin(), s.end());

        int last_number = 1; 
        int response = 0;
        for(int i=0; i<s.size(); i++){
            int roman = equivalence[s[i]];

            if(last_number > roman){
                response -= roman;
            } else {
                response += roman;
            }

            last_number = roman;
        }
        return response;

    }
};

