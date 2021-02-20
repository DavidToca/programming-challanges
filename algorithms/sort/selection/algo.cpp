#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> arr(n);

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    for (int next = 0; next < n; next++)
    {

        int biggest = next;

        for (int i = next + 1; i < n; i++)
        {
            if (arr[i] < arr[biggest])
            {
                biggest = i;
            }
        }

        swap(arr[biggest], arr[next]);
    }

    for (int i = 0; i < n; i++)
    {
        if (i > 0)
            cout << " ";

        cout << arr[i];
    }
    cout << endl;
    return 0;
}