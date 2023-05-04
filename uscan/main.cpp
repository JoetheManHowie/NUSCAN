#include <iostream>

#include "Graph.h"


using namespace std;

void usage()
{
	printf("Usage: [1]exe [2]file-name [3]eta [4]epsilon [5]mu [ [6]output ] \n");
}

void run(Graph& g, string eta, string epsilon, string mu) 
{
	g.localCluster(eta, epsilon, mu);
}

int main(int argc, char *argv[])
{
	if (argc < 5)
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
	run(g, argv[2], argv[3], argv[4]);
	
	end = clock();
	//printf("Total time without IO: %lf s\n\n", (double)(end - end1) / CLOCKS_PER_SEC);
	
	//g.printClusterResult();
	cout<<argv[2]<<" ";
	cout<<argv[3]<<" ";
	cout<<argv[4]<<" ";
	cout<<(double)(end - end1) / CLOCKS_PER_SEC<<" ";

	g.printNumberClusters();
	g.summarizeCluster();
	if(argc == 6 && strcmp(argv[5], "output") == 0)
	  {
	    g.outputLocalResult();
	    g.saveProbability();
	  }
	cout<<endl;
#ifdef _MSC_VER
	quit();
#endif

	return 0;
}
