#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "numero: ";
    cin >> n;

    int array[n];

    for (int i = 0; i < n; i++)
    {
        array[i] = i;
    }
    for (int i = 0; i < n; i++)
    {
        cout << array[i];
    }
    cout << "\n";
    return 0;
}