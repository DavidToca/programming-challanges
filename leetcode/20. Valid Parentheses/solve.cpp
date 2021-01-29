class Solution {
public:
    bool isValid(string s) {
        
        stack <char> pila;
        
        
        for(int i=0; i< s.size(); i++){
            char symbol = s[i];
            
            if(symbol == ')' || symbol == ']' || symbol == '}'){
                
                if(pila.empty()){
                    return false;
                }

                char ontop = pila.top();
                
                if(symbol == ')' and ontop != '('){
                    return false;
                }
                if(symbol == ']' and ontop != '['){
                    return false;
                }
                if(symbol == '}' and ontop != '{'){
                    return false;
                }
                pila.pop();
                
            } else {
                pila.push(symbol);
            }

        }
        
        return pila.size() == 0;
    }
};