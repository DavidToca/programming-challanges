class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 0){
            return "";
        }
        if(strs.size() == 1){
            return strs[0];
        }

        string response = "";

        string first_word = strs[0];

        for(int i=0;i<first_word.size();i++){

            char letter = first_word[i];

            for(int j=1; j<strs.size(); j++){
                string current_word = strs[j];
                if(i >= current_word.size()){
                    return response;
                }
                if(letter != current_word[i]){
                    return response;
                }
            }
            response.push_back(letter);
        }
        return response;

    }
};