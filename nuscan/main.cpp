#include <iostream>

#include "Graph.h"


using namespace std;

void usage()
{
  printf("Usage: [1]exe [2]file-name [3]eta [4]epsilon [5]mu [6]thres [ [7]output ] \n"); // added thres to usage
}
void run(Graph& g, string eta, string epsilon, string mu, string thres) 
{
  g.localCluster(eta, epsilon, mu, thres); //
}
int main(int argc, char *argv[])
{
  if (argc < 6) // was 5, changed to 6
    {
      usage();
#ifdef _MSC_VER
      quit();
#endif
      return 0;
    }
  srand((unsigned)time(NULL));
  //srand(1);
  Graph g;
  /*
  if(argc == 5)
    printf("**** pscan_uncertain : %s, %s, %s, %s, %s *** ", argv[1], argv[2], argv[3], argv[4], "local");
  else
    printf("**** pscan_uncertain : %s, %s, %s, %s, %s *** ", argv[1], argv[2], argv[3], argv[4], argv[5]);

  cout << endl;
  */
  clock_t start, end1, end;
  start = clock();
  g.readGraph(argv[1]);
  end1 = clock();
  //printf("\t*** Finished loading graph!*** cost %lf s\n", (double)(end1 - start) / CLOCKS_PER_SEC);
  run(g, argv[2], argv[3], argv[4], argv[5]);
  end = clock();
  //printf("Total time without IO: %lf s\n\n", (double)(end - end1) / CLOCKS_PER_SEC);
  //cout<<"Algorithm has finished"<<endl;

  //cout<<"nothing after this.."<<endl;
  //g.findHubsAndOutliers();
  cout<<argv[2]<<" "; // eta value
  cout<<argv[3]<<" "; // epsilon value
  cout<<argv[4]<<" "; // mu value
  cout<<argv[5]<<" "; // thres t value
  cout<<(double)(end - end1) / CLOCKS_PER_SEC<<" "; // time elapsed
  g.printNumberClusters(); // number of cores (not clusters)
  g.summarizeCluster(); // more ... (clusters, hubs, outliers)
  // ---- so the output is:
  //-- eta epsilon mu time cores clusters hubs outliers
  //--------------

  if(argc == 7 && strcmp(argv[6], "output") == 0) // changed from argv[5] and argc == 6
    {
      g.outputLocalResult();
      g.saveProbability();
    }
  //cout<<argv[5]<<" ";
  cout<<endl;
  
#ifdef _MSC_VER
  quit();
#endif
  
  return 0;
}
