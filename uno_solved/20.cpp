/*#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

int aux_ftn(char c, int i, const string& s)
{
	if (c == '(')
	{
		i++;
		while (1)
		{
			i = aux_ftn(s[i], i, s);
			if (i == -1 || s[i] == '}' || s[i] == ']')
				return -1;
			else if (s[i] == ')')
				break;
		}
		return i + 1;
	}
	if (c == '[')
	{
		i++;
		while (1)
		{
			i = aux_ftn(s[i], i, s);
			if (i == -1 || s[i] == ')' || s[i] == '}')
				return -1;
			else if (s[i] == ']')
				break;
		}
		return i + 1;
	}
	if (c == '{')
	{
		i++;
		while (1)
		{
			i = aux_ftn(s[i], i, s);
			if (i == -1 || s[i] == ')' || s[i] == ']')
				return -1;
			else if (s[i] == '}')
				break;
		}
		return i + 1;
	}
	else if (c == 0)
		return -1;
	else
		return i;
}

bool isValid(string s)
{
	int len = s.length();

	int a = 0;
	int b = 0;
	int c = 0;
	int i_prev = 0;
	for (int i = 0; i < len;)
	{
		i = aux_ftn(s[i], i, s);
		if (i == i_prev)
			return false;
		if (i == -1)
			return false;
		i_prev = i;
	}
	return true;
}

int main()
{
	cout << is_valid("");
}
*/