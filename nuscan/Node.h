#ifndef _NODE_H
#define _NODE_H


#include "Edge.h"


class Node
{
public:
	std::vector<Edge> edges;

	int degree;					// the degree includes the node itself, i.e. the value equals 1 plus ordinary degree

	int sd;
	int ed;
	int pre;

	bool hasnt_been_visited;	//indicate whether the node is visited
	bool is_core;				//indicate whether a node is a local Core
	bool is_clustered;			//indicate whether a node is clustered

	int type;					// 0:undetermined	1: core 2: non-core 3: hub 4: vertex

	int cid;					//cluster id the node assigned
		 
	Node();
	~Node();

	void clearNode();

	//below is for sampling technique in global clustering
	int sdegree;
	bool is_global_core;
	bool is_deterministic_core;		

	int count_deterministic_core;	//count how many times the node is a determinic in N samples.
	int de_core_neighbors;
};

#endif
