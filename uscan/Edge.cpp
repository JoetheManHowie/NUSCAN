#include "Edge.h"

Edge::Edge(int end)
{
	this->end = end;
	this->proba = 1;
	this->sigma = 0;
	this->sigma_has_been_computed = false;
	this->edge_exists = 0;
	this->de_core_edge_count = 0;
	this->de_core_similar = false;
}

Edge::Edge(int end, double proba)
{
	this->end = end;
	this->proba = proba;
	this->sigma = 0;
	this->sigma_has_been_computed = false;
	this->edge_exists = 0;
	this->de_core_edge_count = 0;
	this->de_core_similar = false;
}

Edge::Edge()
{
	this->sigma = 0;
	this->sigma_has_been_computed = false;
	this->edge_exists = 0;
	this->de_core_edge_count = 0;
	this->de_core_similar = false;
}

bool Edge::compare(const int end)
{
	if (this->end == end)
		return true;
	else
		return false;
}

void Edge::setEdge(int end, double prob)
{
	this->end = end;
	this->proba = prob;
}


void Edge::resetEdge()
{
	sigma = 0;
	sigma_has_been_computed = false;
	edge_exists = 0;
}
