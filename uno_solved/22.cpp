/*#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

vector<string>& aux_ftn(bool flag, int n, vector<string>* strings_false, vector<string>* strings_true)
{
	if (flag && !strings_true[n].empty())
	{
		return strings_true[n];
	}
	else if (!flag && !strings_false[n].empty())
	{
		return strings_false[n];
	}
	if (flag == true)
	{
		for (int i = 0; i < n; i++)
		{
			vector<string>& a = aux_ftn(false, n - i, strings_false, strings_true);
			vector<string>& b = aux_ftn(true, i, strings_false, strings_true);
			int size_a = a.size();
			int size_b = b.size();
			for (int j = 0; j < size_a; j++)
			{
				for (int k = 0; k < size_b; k++)
				{
					strings_true[n].push_back(a[j] + b[k]);
				}
			}
		}
		return strings_true[n];
	}
	else
	{
		vector<string>& a = aux_ftn(true, n-1, strings_false, strings_true);
		int size = a.size();
		for (int i = 0; i < size; i++)
		{
			strings_false[n].push_back("(" + a[i] + ")");
		}
		return strings_false[n];
	}
	
}
vector<string> generateParenthesis(int n)
{
	if (n == 0)
		return vector<string>();
	vector<string>* strings_false = new vector<string>[n + 1];
	strings_false[0].push_back("");
	strings_false[1].push_back("()");
	vector<string>* strings_true = new vector<string>[n + 1];
	strings_true[0].push_back("");
	strings_true[1].push_back("()");
	vector<string> myvec = aux_ftn(true, n, strings_false, strings_true);
	delete[] strings_false;
	delete[] strings_true;
	return myvec;
}

int main()
{
	vector<string> myvec = generateParenthesis(10);
	for (int i = 0; i < myvec.size(); i++)
	{
		cout << myvec[i]<<endl;
	}
}*/