#include "Node.h"

Node::Node()
{
	hasnt_been_visited = true;
	is_core = false;
	is_clustered = false;

	type = 0; 

	is_global_core = false;
	is_deterministic_core = false;

	count_deterministic_core = 0;
	sdegree = 1;
	de_core_neighbors = 1;
}

Node::~Node()
{
}

void Node::clearNode()
{
	edges.clear();
}
