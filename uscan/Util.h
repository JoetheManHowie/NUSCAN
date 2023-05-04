#ifndef _UTIL_H
#define _UTIL_H

#include <cstdlib>
#include <vector>
#include <iostream>
#include <stack>

#include "Node.h"

using namespace std;


void quit();

double random_prob();

void kosaraju(vector<vector<int> > &arr, int vertex_num, int edge_num, int *scc_ids);

class BinHeap
{
private:
	vector<int> *bh;
	vector<int> bhList;
	int *offset;
	int *position;

public:
	BinHeap();
	~BinHeap();

	void init(vector<Node> const &, int);
	//void reInit(vector<Node> const & vec, int n);
	int pop();
	void mod(int u, int bin, int n);


	void printBinList();

	//int find(int);
};

#endif