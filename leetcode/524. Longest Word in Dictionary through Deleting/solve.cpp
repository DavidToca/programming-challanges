class Solution
{
public:
    bool match(string input, string target)
    {
        int input_index = 0;

        for (int i = 0; i < target.size(); i++)
        {

            bool matches = false;

            char letter = target[i];

            for (; input_index < input.size() && !matches; input_index++)
            {
                matches = letter == input[input_index];
            }

            if (!matches)
            {
                return false;
            }
        }
        return true;
    }

    string findLongestWord(string s, vector<string> &d)
    {

        string response = "";
        for (int i = 0; i < d.size(); i++)
        {

            if (match(s, d[i]))
            {
                if (response.size() < d[i].size())
                {
                    response = d[i];
                }
                else if (response.size() == d[i].size() && d[i].compare(response) < 0)
                {
                    response = d[i];
                }
            }
        }

        return response;
    }
};