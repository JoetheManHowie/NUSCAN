#ifndef _EDGE_H
#define _EDGE_H

#include <vector>

class Edge
{
public:
	Edge(int end);
	Edge(int end, double proba);
	Edge();

	void setEdge(int end, double prob);

	bool compare(const int end);
	
	int end;
	double proba;			// the probability of the existance of this edge.
  double time;
  int ku;
  double sigma;			// the similarity between the nodes on this edge.
	bool sigma_has_been_computed;	

	//below is for sampling technique in global clustering
	int edge_exists;		// 0:not selected 1:exist -1:not exist

	int de_core_edge_count;	//count the times when u is a deterministic core and u,v are similar with this edge.
	bool de_core_similar;	//u is globally similar to v

	void resetEdge();
};

class edge_finder
{
public:
	edge_finder(const int a) :end(a){}
	bool operator() (Edge & edge)
	{
		if (this->end == edge.end)
			return true;
		else
			return false;
	}

private:
	int end;
};

#endif
