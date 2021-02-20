class Solution
{
public:
    string minRemoveToMakeValid(string s)
    {
        string response;

        stack<int> checkstack;

        deque<int> delstack;

        for (int i = 0; i < s.size(); i++)
        {
            if (s.at(i) == ')')
            {

                if (checkstack.empty())
                {
                    delstack.push_back(i);
                }
                else
                {
                    checkstack.pop();
                    delstack.pop_back();
                }
            }
            else if (s.at(i) == '(')
            {
                delstack.push_back(i);
                checkstack.push(i);
            }
        }

        for (int i = 0; i < s.size(); i++)
        {
            if (!delstack.empty() && delstack.front() == i)
            {
                delstack.pop_front();
            }
            else
            {
                response.push_back(s.at(i));
            }
        }

        return response;
    }
};