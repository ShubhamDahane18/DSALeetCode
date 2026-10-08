class Solution {
public:
    string removeOuterParentheses(string s) {
        string res = "";
        int cnt = 0;

        for(char &ch: s){
            if(ch == '('){
                if(cnt != 0) res.push_back(ch);
                cnt++;
            }
            else{
                if(cnt != 0){
                    cnt--;
                    if(cnt != 0) res.push_back(ch);
                }
            }
        }
        return res;
    }
};