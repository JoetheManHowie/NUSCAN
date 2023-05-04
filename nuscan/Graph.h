#ifndef _GRAPH_H
#define _GRAPH_H

#include <fstream>
#include <sstream>
#include <iostream>

#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include<cstring>

#include <time.h>
#include <cmath>

#include "Node.h"
#include "Edge.h"
#include "Util.h"

//class BinHeap;

using namespace std;

class Graph
{
private:
  
  string filename;
  
  int vsize; //size of vertices
  long long edgenum; //number of edges
  
  vector<Node> nodes;
  
  BinHeap binHeap;
  
  double eta;			// probability threshold  
  double epsilon;		// similarity threshold  
  int mu;				// neighbour threshold
  int thres;                    // threshold to use the normal jaccard
  
  string  epsilon_s, mu_s, eta_s, thres_s;
  
  //	int glo_count;
  
public:
  
  Graph();
  ~Graph();
  
  void readGraph(const string& filename);
  void readGraph(const string& filename, int prob);	// uniform probability
  void printGraph(int printLevel = 1);
  void initializeGraph(string eta, string epsilon, string mu, string thres); // added thres to param
  void localCluster(string eta_s, string epsilon_s, string mu_s, string thres_s);
  void outputLocalResult();
  void outputLocalCore();
  /*
    cluster core vertices in the graph. contains 3 steps.
    step 1: checkAndCluster		check each vertex u \in V in non-increasing order w.r.t. ed(u)
    step 2: chekcCore			for each vertex u in step 1, check if it is a core vertex
    step 3: clusterCore			if vertex u is a core vertex, then cluster it.
  */
  void checkClusterLocalCore();
  void checkLocalCore(int u);
  void clusterLocalCore(int u);
  /*
    compute the similarity between 2 neighbour nodes u, v
  */
  double computeSim(int u, int v_index, double epsilon, double eta);
  int find_u(vector<Edge> edges, int u);
  int find_bi(vector<Edge> edges, int value);
  /*
    2 function for disjoint set operations:
    find()
    union()
  */
  int find_subset(int x);
  void union_subset(int u, int v);
  /*
    cluster the rest nodes which are noncores
  */
  void ClusterNoncore(double e, double epsilon, int mu);
  void summarizeDirect();
  /*
    summerize the clusters with disjoint set and assign cluster_ids,
  */
  void summarizeCluster();
  /*
    below are testing functions
  */
  void testBinHeap();	
  void printPre();
  void printClusterResult();		//	the result shows all clusters and hubs & outliers
  void printClusterResultInFile();
  void printCore();
  void printSampledGraph();
  void printNumberClusters();
  void findHubsAndOutliers();
  void saveProbability();
  int number_of_samples;
};

#endif

