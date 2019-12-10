#include <iostream>

using namespace std;

int main()
{
    string s1 = "Hello", s2;
    char *s3 = "Hello";
    int i = 0;
    while(s1[i])
    {
        cout << s1[i] << endl;
        i++;
    }
    cout << s1[6] << endl;
    s2 = s1.c_str();
    cout << s2.size() << endl;
    //cout << s3.size() << endl;
    return 0;
}