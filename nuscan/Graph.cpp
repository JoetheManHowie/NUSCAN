#include "Graph.h"

Graph::Graph()
{
  edgenum = vsize = 0;
}

Graph::~Graph(){}

void Graph::readGraph(const string& filename)
{
  this->filename = filename;
  //cout<<"file name "<<filename<<endl;
  ifstream fp(filename.c_str());
  if (!fp)
    {
      cout << "Fail to open " << filename << endl;
#ifdef _MSC_VER
      quit();
#endif
    }
  
  string edge;		// get each edge
  
  int start;			// get each number of startNode
  int end;			// get each number of targetNode
  double prob;		// get the probability of correspoding edge
  
  int index = 0;			// the index of the node
  
  Node tmpNode;
  Edge tmpEdge;
  
  while (getline(fp, edge))
    {
      istringstream ss(edge);
      
      ss >> start >> end >> prob;
      
      if (start > index)
	{
	  tmpNode.degree = tmpNode.edges.size() + 1;		//for structural neighborhood (i.eta., closed neighborhood)
	  tmpNode.sd = 0;
	  tmpNode.ed = tmpNode.degree;
	  tmpNode.pre = index;
	  ++index;
	  
	  nodes.push_back(tmpNode);
	  edgenum += tmpNode.edges.size();
	  vsize += 1;
	  
	  tmpNode.clearNode();
	  index = start;
	}
      
      tmpEdge.setEdge(end, prob);
      
      tmpNode.edges.push_back(tmpEdge);
      
      
      //Edge tmpEdge(end, prob);
      //tmpNode.edges.push_back(tmpEdge);
      
    }
  
  tmpNode.degree = tmpNode.edges.size() + 1;		//for structural neighborhood (i.eta., closed neighborhood)
  tmpNode.sd = 0;
  tmpNode.ed = tmpNode.degree;
  tmpNode.pre = index;
  ++index;
  
  nodes.push_back(tmpNode);
  edgenum += tmpNode.edges.size();
  vsize += 1;
  
  edgenum /= 2;
  
  fp.close();
}

void Graph::readGraph(const string& filename, int prob)
{
  ifstream fp(filename.c_str());
  if (!fp)
    {
      cout << "Fail to open " << filename << endl;
      quit();
    }
  
  string line;		// get each line
  int tmp;			// get each number of targetNode
  int i = 0;			// the index of the node
  
  while (getline(fp, line))
    {
      istringstream ss(line);
      Node tmpNode;
      while (ss >> tmp)
	{
	  Edge tmpEdge(tmp);
	  tmpEdge.proba = 1;
	  
	  tmpNode.edges.push_back(tmpEdge);
	}
      
      tmpNode.degree = tmpNode.edges.size() + 1;		//for structural neighborhood (i.e., closed neighborhood)
      tmpNode.sd = 0;
      tmpNode.ed = tmpNode.degree;
      tmpNode.pre = i;
      ++i;
      
      nodes.push_back(tmpNode);
      
      edgenum += tmpNode.edges.size();
      vsize += 1;
    }
  
  edgenum /= 2;
  
  fp.close();
  
}

void Graph::printGraph(int printLevel)
{
  if (printLevel > 0)
    {
      cout << "vsize:" << vsize << endl;
      cout << "number of edges:" << edgenum << endl;
    }
  if (printLevel > 1)
    {
      for (int i = 0; i < vsize; i++)
	{
	  int degree = nodes[i].degree;
	  cout << "vertex: " << i << "\tdegree: " << degree << endl;
	  
	  if (printLevel > 2)
	    {
	      cout << "ed: " << nodes[i].ed << "\tsd: " << nodes[i].sd << "\tpre: " << nodes[i].pre << endl;
	      if (printLevel > 3)
		{
		  for (int j = 0; j < degree; j++)
		    {
		      cout << nodes[i].edges[j].end << " ";
		    }
		  cout << endl << endl;
		}
	    }
	}
    }
}

void Graph::initializeGraph(string eta_s, string epsilon_s, string mu_s, string thres_s)
{
  this->eta_s = eta_s;
  this->epsilon_s = epsilon_s;
  this->mu_s = mu_s;
  this->thres_s = thres_s;
  this->eta = atof(eta_s.c_str());
  this->epsilon = atof(epsilon_s.c_str());
  this->mu = atoi(mu_s.c_str());
  this->thres = atoi(thres_s.c_str());
  // cout<<"init binHeap"<<endl;
  binHeap.init(nodes, vsize);
}

void Graph::localCluster(string eta_s, string epsilon_s, string mu_s, string thres_s)
{
  //cout<<"Init graph"<<endl;
  initializeGraph(eta_s, epsilon_s, mu_s, thres_s);
  //cout<<"check clusters "<<endl;
  checkClusterLocalCore();
  //cout<<"cluster non cores"<<endl;
  ClusterNoncore(eta, epsilon, mu);

  /////////////////////////////
  // label hubs and outliers //
  /////////////////////////////
  findHubsAndOutliers();
  //outputLocalCore();
  //outputLocalResult();
}

void Graph::saveProbability()
{
  ofstream fout((filename + "-" + eta_s + "-" + epsilon_s + "-" + mu_s + "-" + thres_s + ".prob_nuscan").c_str());
  for (int u = 0; u<vsize; u++)
    for (int i = 0; i<nodes[u].degree-1; i++)
        fout <<u << " "<<nodes[u].edges[i].end << " "<< nodes[u].edges[i].sigma<<" "<<nodes[u].edges[i].ku<<" "<<nodes[u].edges[i].time<<"\n";
}

void Graph::outputLocalResult()
{
  //cout<<" open function"<<endl; 
  ofstream fout((filename + "-" + eta_s + "-" + epsilon_s + "-" + mu_s + "-" + thres_s + ".cluster_nuscan").c_str());
  int  nodes_clustered=0;
  int ind_map=0, test_others=0;
  map<int, vector<int> > decypher;

  for (int i = 0; i <vsize; ++i)
    {
      if (!nodes[i].is_clustered)
	{
	  test_others++;
	  continue;
	}
      ind_map = nodes[i].cid;
      nodes_clustered++;
      //cout<<"node = "<<i<<" cid = "<<ind_map<<endl;

      vector<int> temp;
      temp = decypher[ind_map];
      temp.push_back(i);
      decypher[ind_map] = temp;

    }
  /*
  cout<<endl;
  cout<<"non-clustered node "<<test_others<<endl;
  cout<<"clustered node "<< nodes_clustered<<endl;
  */

  for (auto iter = decypher.begin(); iter != decypher.end(); ++iter)
    {
      //fout<<"cid: "<<iter->first<<endl;
      for (auto j = iter->second.begin(); j != iter->second.end(); ++j)
	{
	  fout << *j << " ";
	}
      fout <<"\n";
    }
  for (int i = 0; i < vsize; ++i)
    {
      if (nodes[i].type == 3)
	fout<<i<<" hub"<<endl;
      else if (nodes[i].type == 4)
	fout<<i<<" outlier"<<endl;
    }
}

void Graph::outputLocalCore()
{
  ofstream fout("local_cores.txt");
  
  for (int i = 0; i < vsize; ++i)
    {
      fout << "node[" << i << "]:\t";
      if (nodes[i].type == 1)
	fout << "c ";
      else if (nodes[i].type == 2)
	fout << "n ";
      else
	fout << "ud ";
      fout << endl;
    }
}

/*
  check each vertex u \in V in non-increasing order w.r.t. ed(u), and cluster the Core Vertices.
*/

void Graph::checkClusterLocalCore()
{
  //glo_count = 0;
  int u;
  //cout<<"check cluster local core of u = "<<u<<endl;
  for (int i = 0; i < vsize; i++)
    {
      u = binHeap.pop();
      //cout<<"on u = "<<u<<endl;
      checkLocalCore(u);
      
      if (nodes[u].sd >= mu)
	{
	  nodes[u].is_core = true;
	  clusterLocalCore(u);
	  nodes[u].is_clustered = true;
	}
    }
  //	cout << glo_count << endl;
}

/*
  check if vertex u is a Core Vertex
*/

void Graph::checkLocalCore(int u)
{
  if ((nodes[u].ed >= mu) && (nodes[u].sd < mu))
    {
      nodes[u].ed = nodes[u].degree;
      //nodes[u].sd = 0;							//NOTE: This is what the pSCAN paper use and it's wrong for not considering the node 
      //      u itself as N[u] (closed neighborhood). and this mistake can be easily found
      //		with the example in this paper's figure 2
      nodes[u].sd = 1;
      
      for (unsigned int i = 0; i < nodes[u].edges.size(); i++)
	{
	  int v = nodes[u].edges[i].end;
	  double sigma;
	  if (nodes[u].edges[i].sigma_has_been_computed == true)
	    sigma = nodes[u].edges[i].sigma;
	  else
	    {
	      /// replace with diff function call
	      sigma = computeSim(u, i, epsilon, eta);
	    }
	  if (sigma >= eta)
	    {
	      nodes[u].sd++;
	    }
	  else
	    {
	      //binHeap.mod(u, nodes[u].ed, vsize);		//ATTENTION: no need to resort the position of u here.
	      nodes[u].ed--;
	    }
	  if (nodes[v].hasnt_been_visited)
	    {
	      if (sigma >= eta)
		nodes[v].sd++;
	      
	      else
		{
		  binHeap.mod(v, nodes[v].ed, vsize);
		  nodes[v].ed--;					
		}
	    }
	  if ((nodes[u].ed < mu) || (nodes[u].sd > mu))
	    break;
	}
    }
  
  nodes[u].hasnt_been_visited = false;	//mark u as explored
  
  //return true;
}
/*
  cluster Core Vertex u
*/
void Graph::clusterLocalCore(int u)
{
  for (int i = 0; i < nodes[u].degree - 1; i++)
    {
      int v = nodes[u].edges[i].end;
      if (!nodes[u].edges[i].sigma_has_been_computed)	
	{
	  if ((find_subset(u) != find_subset(v)) && (nodes[v].ed >= mu))
	    {
	      /// replace with diff function
	      double sigma = computeSim(u, i, epsilon, eta);
	      if (nodes[v].hasnt_been_visited)
		{
		  if (sigma >= eta)
		    {
		      nodes[v].sd++;
		    }
		  else
		    {
		      binHeap.mod(v, nodes[v].ed, vsize);
		      nodes[v].ed--;
		    }
		}
	      if ((nodes[v].sd >= mu) && (sigma >= eta))
		{
		  union_subset(u, v);
		}
	    }
	}
      else
	{
	  if ((nodes[v].sd >= mu) && (nodes[u].edges[i].sigma >= eta))
	    {
	      //TODO join u, v
	      union_subset(u, v);
	    }
	}
    }
  
}

/*
  compute the similarity between 2 neighbour nodes u, v
*/
struct Prob {		// to record the probabilities of correspoding (u, v, w) pairs
  double pu;
  double pv;
  double p1;
  double p2;
  double p3;
  double p4;
};

//int Gcount = 0;

double Graph::computeSim(int u, int v_index, double epsilon, double eta)
{
  clock_t start, stop;
  start =clock();
  int ku = 0;
  double prob = 0.0;
  int v = nodes[u].edges[v_index].end;
  bool norm_flag = false;
  //cout<<"u = "<<u<<", v = "<<v<<endl;
  if (nodes[u].edges[v_index].proba >= eta) 
    {
      vector<int> intersec_u_v(max(nodes[u].degree - 1, nodes[v].degree - 1));
      vector<int> symdiff_u_v(nodes[u].degree + nodes[v].degree);
      vector<int> union_u_v;
      
      vector<int> s1;
      vector<int> s2;
      vector<int>::iterator it;
      
      for (int i = 0; i < nodes[u].degree - 1; i++)
	{
	  if (nodes[u].edges[i].end != v)
	    s1.push_back(nodes[u].edges[i].end);
	}
      
      for (int i = 0; i < nodes[v].degree - 1; i++)
	{
	  if (nodes[v].edges[i].end != u)
	    s2.push_back(nodes[v].edges[i].end);
	}
      
      it = set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), intersec_u_v.begin());
      intersec_u_v.resize(it - intersec_u_v.begin());
      
      it = set_symmetric_difference(s1.begin(), s1.end(), s2.begin(), s2.end(), symdiff_u_v.begin());
      symdiff_u_v.resize(it - symdiff_u_v.begin());
      
      union_u_v.insert(union_u_v.end(), intersec_u_v.begin(), intersec_u_v.end());
      union_u_v.insert(union_u_v.end(), symdiff_u_v.begin(), symdiff_u_v.end());
      
      
      int kn = intersec_u_v.size() + 2;
      ku = union_u_v.size() + 2;
      
      // record the probabilities of correspoding (u, v, w) pairs, i.e. p1*p2, (1-p1)*p2, (1-p2)*p1, (1-p1)*(1-p2)
      map <int, Prob> w_probs;
      map <int, double> pu;
      map <int, double> pv;
      //cout<<"here"<<endl;
      for (int i = 0; i < nodes[u].degree - 1; i++)
	{
	  w_probs[nodes[u].edges[i].end].pu = nodes[u].edges[i].proba;
	  //cout<<"u = "<<u<<", w = "<<nodes[u].edges[i].end<<", p = "<<nodes[u].edges[i].proba<<endl;
	}
      
      for (int i = 0; i < nodes[v].degree - 1; i++)
	{
	  w_probs[nodes[v].edges[i].end].pv = nodes[v].edges[i].proba;
	  //cout<<"v = "<<v<<", w = "<<nodes[v].edges[i].end<<", p = "<<nodes[v].edges[i].proba<<endl;
	}
      
      for (map<int, Prob>::iterator it = w_probs.begin(); it != w_probs.end(); it++)
	{
	  double pu = it->second.pu;
	  double pv = it->second.pv;
	  
	  it->second.p1 = pu * pv;
	  it->second.p2 = (1 - pu) * pv;
	  it->second.p3 = (1 - pv) * pu;
	  it->second.p4 = (1 - pu) * (1 - pv);
	}
      /*
      for (int i = 0; i < symdiff_u_v.size(); i++)
	{
	  cout<<"symmetric difference "<<symdiff_u_v[i]<<endl;
	}
      for (int i = 0; i < intersec_u_v.size(); i++)
	{
	  cout<<"intersection "<<intersec_u_v[i]<<endl;
	}
      */
      
      // ------------------ BEG :: NORMAL INSERT -------------------
      //int thres = 32;//32 and 62;
      if(ku >= thres+2)
	{
	  //cout<<"1"<<endl;
	  //prob = normalSim(u, v_index, epsilon, eta);
	  // to use the sets made above write code in here, then it shouldn't be more than 50 lines//
	  double mean = 0;
	  double variance = 0;
	  double mean_i_sqr, mean_i;
	  double p1, p2, x1, x2;
	  int w;
	  for(int i = 0 ; i < kn - 2; i++)
	    {
	      w =  intersec_u_v[i];
	      ///p1 = get_uw_prob;
	      p1 = w_probs[w].pu;
	      ///p2 = get_vw_prob;
	      p2 = w_probs[w].pv;
	      x1 = (p1*(1-p2)+p2*(1-p1));
	      x2 = p1*p2;
	      mean_i = ( - epsilon * x1 + ( 1 - epsilon ) * x2 );
	      mean += mean_i;
	      mean_i_sqr = epsilon * epsilon * x1 + (1 - epsilon) * (1 - epsilon) * x2 ;
	      variance += mean_i_sqr - mean_i * mean_i ; 
	    }
	  double pj = 0;
	  for(int i = 0; i < symdiff_u_v.size(); i++)
	    {
	      // get the non zero prob, either uw or vw.
	      w = symdiff_u_v[i];
	      pj = max(w_probs[w].pu, w_probs[w].pv);
	      mean_i = - epsilon * pj ;
	      mean += mean_i;
	      mean_i_sqr = epsilon * epsilon * pj ;
	      variance += mean_i_sqr - mean_i * mean_i ;
	    }
	  double std = pow(variance, 0.5);
	  if (std == 0.0)
	    std = 0.000000000000001;
	  double P_threshold = (2*(epsilon -1) - mean )/ std;
	  //---------------------------------------------------//
	  // Get normal distribution for P[J_p >= P_threshold] //
	  //---------------------------------------------------//
	  // root2 ref: https://www.wolframalpha.com/input/?i=square+root+of+2
	  // erf() ref: https://www.cplusplus.com/reference/cmath/erf/
	  double erf_arg = ( P_threshold - mean ) / ( std * 1.4142135623730950488016887242096980785696718753769480731766797379 );
	  //variance * 1.4142135623730950488016887242096980785696718753769480731766797379 );
	  // src: https://statproofbook.github.io/P/norm-cdf.html
	  prob = 1 -  ( 0.5 * ( 1 + erf(erf_arg) ) ); 
	  
	  nodes[u].edges[v_index].sigma = prob;
	  //norm_flag = true;
	}
      // ------------------ END :: NORMAL INSERT -------------------
      else // dp protocol
	{
	  //cout<<"1"<<endl;
	  // fix denominator
	  double proaa = 0.0;
	  
	  if (1.0 * kn / ku >= epsilon)
	    {
	      // cout<<"fix denominator route"<<endl;
	      double **aa;
	      aa = new double *[2];
	      aa[0] = new double[ku + 1]();
	      aa[1] = new double[ku + 1]();
	      
	      aa[0][2] = 1;
	      
	      int m_min = ceil(kn * epsilon);
	      
	      int cb = 0;
	      for (int h = 1; h < ku - 1; h++)
		{
		  cb = 1 - cb;
		  
		  for (int m = 2; m < min(h + 3, kn + 1); m++)
		    {
		      int w = union_u_v[h - 1];
		      // cout<<"from union aa: w = "<<w<<endl;
		      aa[cb][m] = (w_probs[w].p1) * aa[1 - cb][m - 1]
			+ (w_probs[w].p2 + w_probs[w].p3 + w_probs[w].p4) * aa[1 - cb][m];
		    }
		}
	      
	      
	      for (int m = max(2, static_cast<int> (ceil(ku * epsilon))); m < kn + 1; m++)
		{
		  //				double tmp = 1.0 * m / ku;
		  //				if (tmp >= epsilon)
		  //				{
		  // cout<<"adding "<<aa[cb][m]<<endl;
		  proaa += aa[cb][m];
		  //				}
		}
	      
	      delete[] aa[0];
	      delete[] aa[1];
	      delete[] aa;
	    }
	  
	  if (proaa * nodes[u].edges[v_index].proba < eta) 
	    //if(1)
	    {
	      // cout<<"fix numerator route"<<endl;
	      // fix numerator
	      double **bb;
	      bb = new double *[2];
	      bb[0] = new double[ku + 1]();
	      bb[1] = new double[ku + 1]();
	      
	      bb[0][2] = 1;
	      
	      int cb = 0;
	      int n_max = int(kn / epsilon + 1);
	      
	      for (int h = 1; h < ku - 1; h++)
		{
		  cb = 1 - cb;
		  //for (int n = 0; n < min(h + 1, ku - 1); n++)
		  for (int n = 2; n < min(h + 3, ku + 1); n++)
		    {
		      if (n >= n_max)
			break;
		      else
			{
			  int w = union_u_v[h - 1];
			  // cout<<"from union bb: w = "<<w<<endl;
			  bb[cb][n] = (w_probs[w].p1 + w_probs[w].p2 + w_probs[w].p3) * bb[1 - cb][n - 1]
			    + w_probs[w].p4 * bb[1 - cb][n];
			}
		    }
		}
	      
	      double probb = 0.0;
	      
	      for (int n = 2; n < ku + 1; n++)
		{
		  double tmp = 1.0 * kn / n;
		  if (tmp >= epsilon)
		    {
		      // cout<<"adding "<<bb[cb][n]<<endl;
		      probb += bb[cb][n];
		    }
		}
	      
	      //if (probb < 0)
	      //cout << "biu" << endl;
	      //cout << probb << endl;
	      
	      
	      delete[] bb[0];
	      delete[] bb[1];
	      delete[] bb;
	      
	      if (probb >= eta)
		{
		  // cout<<"normal mode of operation"<<endl;
		  double ***x;		// 3-d DP array
		  
		  // create the 3-d array x
		  x = new double **[2];
		  for (int i = 0; i < 2; i++)
		    {
		      x[i] = new double *[kn + 1];
		      for (int j = 0; j < kn + 1; j++)
			{
			  x[i][j] = new double[ku + 1]();		//initialize all the array with 0
			  //x[i][j] = new double[ku + 1];
			}
		    }
		  
		  x[0][2][2] = 1;
		  
		  //calculate the intersection
		  int c = 0;
		  // cout<<"intersection part"<<endl;
		  for (int h = 1; h < kn - 1; h++)			// (ku+1)-2
		    {
		      c = 1 - c;
		      for (int m = 2; m < min(h + 3, kn + 1); ++m)
			{
			  int n_max = int(m / epsilon + 1);
			  for (int n = m; n < min(h + 3, kn + 1); n++)
			    {
			      if (h > intersec_u_v.size() && n >= n_max)
				break;
			      else
				{
				  int w = intersec_u_v[h - 1];
				  // cout<<"from intersection xx: w = "<<w<<endl;
				  x[c][m][n] = w_probs[w].p1 * x[1 - c][m - 1][n - 1] + (w_probs[w].p2 + w_probs[w].p3) * x[1 - c][m][n - 1]
				    + w_probs[w].p4 * x[1 - c][m][n];
				}
			    }
			}
		    }
		  
		  prob = 0.0;
		  // cout<<"intersection"<<endl;
		  for (int n = 2; n < kn + 1; n++)
		    {
		      for (int m = 0; m < min(n + 1, kn + 1); m++)
			{
			  double tmp = 1.0 * m / n;
			  if (tmp >= epsilon)
			    {
			      // cout<<"adding "<<x[c][m][n]<<endl;
			      prob += x[c][m][n];
			    }
			}
		    }
		  
		  if (prob >= eta)
		    {
		      // cout<<"union part"<<endl;
		      for (int h = kn - 1; h < ku - 1; h++)			// (ku+1)-2
			{
			  c = 1 - c;
			  for (int m = 2; m < min(h + 3, kn + 1); ++m)
			    {
			      int n_max = int(m / epsilon + 1);
			      for (int n = m; n < min(h + 3, ku + 1); n++)
				{
				  if (h > intersec_u_v.size() && n >= n_max)
				    break;
				  else
				    {
				      int w = union_u_v[h - 1];
				      // cout<<"from union xx: w = "<<w<<endl;
				      x[c][m][n] = w_probs[w].p1 * x[1 - c][m - 1][n - 1] + (w_probs[w].p2 + w_probs[w].p3) * x[1 - c][m][n - 1]
					+ w_probs[w].p4 * x[1 - c][m][n];
				    }
				}
			    }
			}
		      
		      //calculate the return value of probability
		      prob = 0.0;
		      for (int n = 2; n < ku + 1; n++)
			{
			  for (int m = 0; m < min(n + 1, kn + 1); m++)
			    {
			      double tmp = 1.0 * m / n;
			      if (tmp >= epsilon)
				{
				  prob += x[c][m][n];
				  // cout<<"adding "<<x[c][m][n]<<endl;
				}
			    }
			}
		    }
		  
		  
		  // free the memory of 3-d array x
		  for (int i = 0; i < 2; i++)
		    {
		      for (int j = 0; j < kn + 1; j++)
			{
			  delete[] x[i][j];
			}
		      delete[] x[i];
		    }
		  delete[] x;
		  
		}
	      else
		{
		  prob = probb;
		}
	    }		
	  else
	    {
	      prob = proaa;
	    }
	}
    }
  // end of eta check if statement
  /** 
      process return value
  */
  //  if(!norm_flag)
  //{
  nodes[u].edges[v_index].sigma = nodes[u].edges[v_index].proba * prob; 	//sigma here records the prob of > eplison
  //}
  nodes[u].edges[v_index].sigma_has_been_computed = true;
  
  prob = nodes[u].edges[v_index].sigma;
  
  int u_index = find_bi(nodes[v].edges, u);
  
  nodes[v].edges[u_index].sigma = prob;
  nodes[v].edges[u_index].sigma_has_been_computed = true;
  
  nodes[u].edges[v_index].ku = ku;
  nodes[v].edges[u_index].ku = ku;
  
  stop = clock();
  double the_time = (double)(stop - start)/CLOCKS_PER_SEC;
  nodes[u].edges[v_index].time = the_time;
  nodes[v].edges[u_index].time = the_time;
  return prob;
}

int Graph::find_u(vector<Edge> edges, int u)
{
  for (size_t i = 0; i < edges.size(); ++i)
    if (edges[i].end == u)
      return i;
  
  return -1;
}

int Graph::find_bi(vector<Edge> edges, int value)
{
  /*if (array == NULL || len <= 0)
    return -1;*/
  int len = edges.size();
  int low = 0;
  int high = len - 1;
  while (low <= high)
    {
      int mid = low + (high - low) / 2;
      if (edges[mid].end == value)
	return mid;
      else if (edges[mid].end > value)
	high = mid - 1;
      else
	low = mid + 1;
    }
  
  return -1;
}

int Graph::find_subset(int x)
{
  int r = x;
  while (nodes[r].pre != r)
    r = nodes[r].pre;
  
  int i = x, j;
  while (i != r)
    {
      j = nodes[i].pre;
      nodes[i].pre = r;
      i = j;
    }
  return r;
}

void Graph::union_subset(int u, int v)
{
  int fu = find_subset(u), fv = find_subset(v);
  if (fu != fv)
    nodes[fu].pre = fv;
}

void Graph::ClusterNoncore(double e, double epsilon, int mu)
{
  for (int u = 0; u < vsize; ++u)
     {
      if (nodes[u].is_core)
	{
	  nodes[u].type = 1;
	  for (int i = 0; i < nodes[u].degree - 1; ++i)
	    {
	      int v = nodes[u].edges[i].end;
	      if ((nodes[v].sd < mu) && !nodes[v].is_clustered)
		{
		  double sigma = nodes[u].edges[i].sigma;
		  if (sigma == 0)	//NOTE: sigma is double, if there's anything wrong, change this statement!!
		    // replace with different function
		    sigma = computeSim(u, i, epsilon, eta);
		  if (sigma >= e)
		    {
		      union_subset(u, v);	
		      nodes[v].is_clustered = true;
		      nodes[v].type = 2;
		    }
		}
	    }
	}
    }
  //summarizeCluster();
  summarizeDirect();
}
void Graph::summarizeDirect()
{
  for (int i = 0; i < vsize; ++i)
    {
      nodes[i].cid = find_subset(i);
    }
}

void Graph::summarizeCluster()
{
  map<int, int> cluster_ids;
  int cluster_count = 1;
  for (int i = 0; i < vsize; ++i)
    {
      find_subset(i);
      if (cluster_ids.count(nodes[i].pre) == 0)
	{
	  cluster_ids[nodes[i].pre] = cluster_count;
	  nodes[i].cid = cluster_ids[nodes[i].pre];
	  cluster_count++;
	}
      else
	{
	  nodes[i].cid = cluster_ids[nodes[i].pre];
	}
    }
  //cout<<"number of clusters+outliers"<<cluster_count<<endl;
  
  int cluster_list[cluster_count];
  int cluster_real = 0;
  int hubs_c = 0;
  int outliers_c = 0;
  for (int i = 0; i < cluster_count; i++)
    cluster_list[i] = 0;
  for (int i = 0; i < vsize; i++)
      if (nodes[i].is_clustered)
	cluster_list[nodes[i].cid] = 1;
      else if(nodes[i].type == 3)
	cluster_list[nodes[i].cid] = 3;
      else if (nodes[i].type == 4)
	cluster_list[nodes[i].cid] = 4;

  for (int i = 0; i < cluster_count; i++)
      if (cluster_list[i] == 1)
	++cluster_real;
      else if (cluster_list[i] == 3) //hub
	++hubs_c;
      else if (cluster_list[i] == 4) //outlier
	++outliers_c;
  /////////////////////////
  cout<<cluster_real<<" "; // number of clusters
  cout<<hubs_c<<" "; // number of hubs
  cout<<outliers_c<<" "; // number of outliers 
  /////////////////////////
  //cout<<"number of clusters "<<cluster_real<<endl;
  //cout<<"number of hubs "<<hubs_c<<endl;  
  //cout<<"number of outliers "<<outliers_c<<endl;
}

/*
  below are testing functions
*/
void Graph::testBinHeap()
{
  binHeap.printBinList();
  binHeap.mod(12, 3, 13);	// u is the 12th vertex, ed(u)=3, number of vertice n is 13
  binHeap.printBinList();
  
  int a = binHeap.pop();
  int b = binHeap.pop();
  cout << a << " " << b << endl;
}

void Graph::printPre()
{
  for (int i = 0; i < vsize; i++)
    cout << i << ' ';
  cout << endl;
  for (int i = 0; i < vsize; i++)
    cout << nodes[i].pre << ' ';
  cout << endl;
}

/*
  the result shows all clusters and hubs & outliers
*/
void Graph::printClusterResult()
{
  cout << "type  " << "node " << "\tcid \tdegree \tpre \tvisid\tclusd\tcore" << endl;
  for (int i = 0; i < vsize; ++i)
    {
      if (nodes[i].is_core)
	cout << "c ";
      else
	cout << "n ";
      cout << "node[" << i << "]:\t" << nodes[i].cid << "\t";	// << endl;
      cout << nodes[i].degree << "\t" << nodes[i].pre << "\t" << nodes[i].hasnt_been_visited
	   << "\t" << nodes[i].is_clustered << "\t" << nodes[i].is_core << endl;
    }
}

void Graph::printClusterResultInFile()
{
  ofstream fout("output.txt");
  /* if (!fp)
     {
     cout << "Fail to open " << filename << endl;
     quit();
     }*/
  
  for (int i = 0; i < vsize; ++i)
    {
      if (nodes[i].is_core)
	fout << "c ";
      else
	fout << "n ";
      fout << "node[" << i << "]:\t" << nodes[i].cid << "\t";	// << endl;
      fout << nodes[i].degree << "\t" << nodes[i].pre << "\t" << nodes[i].hasnt_been_visited
	   << "\t" << nodes[i].is_clustered << "\t" << nodes[i].is_core << endl;
    }
  
}

void Graph::printCore()
{
  cout << "type  " << "node " << "\tcid \tdegree \tpre \tvisid\tclusd\tcore\tcount" << endl;
  for (int i = 0; i < vsize; ++i)
    {
      if (nodes[i].is_deterministic_core)
	cout << "c ";
      else
	cout << "n ";
      cout << "node[" << i << "]:\t" << nodes[i].cid << "\t";	// << endl;
      cout << nodes[i].degree << "\t" << nodes[i].pre << "\t" << nodes[i].hasnt_been_visited
	   << "\t" << nodes[i].is_clustered << "\t" << nodes[i].is_core << "\t" << nodes[i].count_deterministic_core << endl;
    }
  
}

void Graph::printSampledGraph()
{
  for (unsigned int i = 0; i < nodes.size(); ++i)
    for (unsigned int j = 0; j < nodes[i].edges.size(); ++j)
      if (nodes[i].edges[j].edge_exists == 1)
	cout << i << "---" << nodes[i].edges[j].end << endl;
}
void Graph::printNumberClusters()
{
  int count = 0;
  for(int i = 0; i < vsize; i++)
    {
      if(nodes[i].type == 1) // count cores!!!!!
	++count;
    }
  cout<<count<<" ";
  //cout<<"number of cores "<<count<<endl;
}
void Graph::findHubsAndOutliers()
{
  int last_c = -1;
  int curr_c;// = 0;
  bool flag_hub = false;
  for (int i = 0; i < vsize; i++)
    {
      if (!nodes[i].type == 1)
	{
	  last_c = -1;
	  flag_hub = false;
	  for (int j = 0; j < nodes[i].degree-1; j++)
	    {
	      if (nodes[nodes[i].edges[j].end].is_clustered)
		{
		  if (last_c == -1)
		    last_c = nodes[nodes[i].edges[j].end].cid;
		  else
		    {
		      curr_c = nodes[nodes[i].edges[j].end].cid;
		      if (last_c != curr_c)
			{
			  flag_hub = true;
			  break;
			}
		      last_c = curr_c;
		    }
		}
	    }
	  
	  if (flag_hub)
	    nodes[i].type = 3;
	  else
	    nodes[i].type = 4;
	}
    }
}
