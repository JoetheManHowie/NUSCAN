#include "Util.h"

void quit()
{
	int systemRet = system("pause");
	exit(0);
}

double random_prob()
{
	return (double)(rand()/(double)RAND_MAX);
}

void dfs1(int v, bool *visited, vector<vector<int> > &rearr, stack<int> &S)
{
	visited[v] = true;
	for (int i = 0; i < rearr[v].size(); ++i)
	{
		int u = rearr[v][i];
		if (!visited[u])
		{
			dfs1(u, visited, rearr, S);
		}
	}
	S.push(v);
}

void dfs2(int v, int t, bool *visited, vector<vector<int> > &arr, int * scc_ids)
{
	visited[v] = true;
	scc_ids[v] = t;
	for (int i = 0; i < arr[v].size(); ++i)
	{
		int u = arr[v][i];
		if (!visited[u])
		{
			dfs2(u, t, visited, arr, scc_ids);
		}
	}
}

void kosaraju(vector<vector<int> >& arr, int vertex_num, int edge_num, int * scc_ids)
{
	vector<vector<int> > rearr;
	for (int i = 0; i < vertex_num; ++i)
		rearr.push_back(vector<int>());

	for (int i = 0; i < vertex_num; ++i)
	{
		for (int j = 0; j < arr[i].size(); ++j)
		{
			int v = arr[i][j];
			rearr[v].push_back(i);
		}
	}

	stack<int> S;
	while (!S.empty())
		S.pop();

	bool *visited = new bool[vertex_num];
	for (int i = 0; i < vertex_num; ++i)
		visited[i] = false;

	for (int i = 0; i < vertex_num; ++i)
	{
		if (!visited[i])
			dfs1(i, visited, rearr, S);
	}

	for (int i = 0; i < vertex_num; ++i)
		visited[i] = false;

	int t = 0;

	while (!S.empty())
	{
		int v = S.top();
		S.pop();

		if (!visited[v])
		{
			dfs2(v, t, visited, arr, scc_ids);
			t++;
		}
	}

	delete[] visited;
	visited = NULL;
}

BinHeap::BinHeap():bh(NULL), offset(NULL), position(NULL)
{

}

BinHeap::~BinHeap()
{
	delete[] offset;
	delete[] position;
}

//vec was ed[]
void BinHeap::init(vector<Node> const & vec, int n)
{
	bh = new vector<int> [n];
	if (bhList.size() != 0)
		bhList.clear();
	/*
	    step 1: put each element into its corresponding bin
	*/
	for(int i=0; i<n; i++)
	{
		bh[vec[i].ed].push_back(i);
	}

	/*
	    step 2: move the elements into a bar vector, noting their offsets for
	    each bin and their positions for each point

	    offset[i] denotes the position of the first element in the (i+1)th bin
	*/
	if(NULL == offset)
		offset = new int[n];
	if(NULL == position)
		position = new int[n];

	int count = 0;				//count current position
	for(int i=0; i<n; i++)
	{
		offset[i] = count;
		for(unsigned int j=0; j<bh[(n-1)-i].size(); j++)
		{
			bhList.push_back(bh[(n-1)-i][j]);
			position[bh[(n-1)-i][j]] = count;
			count++;
		}
	}

	delete[] bh;
}

int BinHeap::pop()
{

	int firstElement = bhList[offset[0]];
	offset[0]++;

	return firstElement;
}

void BinHeap::mod(int u, int bin, int n)
{
	bin--;	//remove the node itself

	/*
	    step 1: swap u and the last element of u's bin denoted as v
	*/

	int offsetNo = n - bin;		//calculate the offset number
	//because we put the bins in reverse order

	int v = bhList[offset[offsetNo]-1];

	bhList[position[u]] = v;
	bhList[offset[offsetNo]-1] = u;
	position[v] = position[u];
	position[u] = offset[offsetNo] - 1;

	/*
	    step 2: move the offset by minus 1
	*/

	offset[offsetNo] = offset[offsetNo] -1;

}

void BinHeap::printBinList()
{
	cout << "bhList:" << endl;
	for(unsigned int i=0; i<bhList.size(); i++)
	{
		cout << bhList[i] << " ";
	}
	cout << endl;
	cout << "offset:" <<endl;
	for(unsigned int i=0; i<bhList.size(); i++)
	{
		cout << offset[i] << " ";
	}
	cout << endl;
}