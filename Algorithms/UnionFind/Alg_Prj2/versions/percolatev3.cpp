//notes
//When you do a find, always do path compression







//PREPROCCESSORS
#include <fstream>
#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

//NAMESPACES
using namespace std;

//STRUCTURES

struct Point{
	bool isFull;
	Point * parent;
	int weight;
	Point()
	{
		weight = 1;
		isFull = false;
		parent = this;
	}
};

//FUNCTION PROTOTYPES
bool determine_percolation(Point *, int);
void print(const Point *, int);
void print_out(const Point *, int);
Point * find_root(Point* );
bool is_equal(Point, Point);
void tree_union(Point *, Point *);
void find_cluster(Point * , int);
int clusters(Point *, int);




//MAIN
int main(int argc, const char ** argv)
{
	try
	{
 		if(argc < 2)
		{
			cout << "usage:\n" << argv[0] << "<filename>\n" << "OR\n" << argv[0] << "<p> <n> <s>\n";
		}
		else if (argc == 2)
		{
			//opening of ifstream and grabing data.
			ifstream inFile (argv[1]);
			if( !inFile.is_open() )
			{
				cout << "The file " << argv[1] << " could not be opened\n";
			}
			else
			{
				
				//PRELIMINARY FILE LOADING AND SETUP
				//#################################################################################################################
				//Here we declare a count integer and two strings one is temporary and one will hold all the data 
				//the count will find the size o the matrix(which is assumed to be square)
				cout <<"loading data from file..." << endl;
				int count = 0;
				string temp;
				string array;
				while(getline(inFile,temp))
				{
					if(!temp.empty())
					{
						++count;
						array += temp;
					}
				}
				
				//this removes spaces and \n to make the cluster finding algorithm easier
				array.erase(remove(array.begin(),array.end(),' '),array.end());
				array.erase(remove(array.begin(),array.end(),'\n'),array.end());
				
				//make the Point array so that we can have parent pointer representation later 
				Point * set;
				set = new Point[array.length()];
				
				//Preserve the values in the array
				for(int i =0; i<array.length();i++)
				{
					if(array[i] == '1')
					{
						set[i].isFull = true;
					}
				}

				//##################################################################################################################

				//FIND ALL THE CLUSTERS
				cout << "The size of the matrix is\n" <<count << "x" << count << endl;
				print(set, count);
				print_out(set,count );

				find_cluster(set,count);
				cout << "The number of clusters is:\n";
				cout << clusters(set, count) << endl;

				//TEST STUFF
				

			}
		}
		else if(argc == 4)
		{
			double probability = atof(argv[1]);
			int numRuns = atoi(argv[2]);
			int size = atoi(argv[3]), numPercolations=0;

			//seed rand
			srand(time_t(NULL));
			
			for(int h = 0; h < numRuns; h++)
			{
				//make an size^2 length array to stand in for the matrix
				Point * set = new Point[size*size];
				
				//random number to do probabilities
				double randomFloat;

				//fill the array using the given probability
				for(int i = 0; i<size*size;i++)
				{
					//random number between (0,1)
					randomFloat = ((double) rand() / (RAND_MAX));
					//if the random number is greater than the probability then close the cell
					if(randomFloat > probability)
					{
						set[i].isFull = true;
					}
				}

				//print the matrix
				
				print_out(set, size);

                cout << endl;
				
				//find the clusters
				find_cluster(set, size);


				if(determine_percolation(set,size))
				{
					numPercolations++;
				}


				for(int i = 0 ; i < size*size; i++)
				{
					if(&set[i] == find_root(&set[size*(size-1)]))
					{
						cout << i << endl;
					}	
				}
				
				
			}
			cout <<"Given probability:" << argv[1] <<endl<< "Number of runs:" << argv[2] << endl << "size of matrix:"<< argv[3] << endl
				<< "The percolaton rate is " <<  numPercolations/static_cast<double>(numRuns)<< endl;
			
		}
	}
	catch(string error)
	{
		cout << "An exception occured\n" <<error;
	}
	return 0;
}

bool determine_percolation(Point *set, int size)
{
	for(int i = 0; i < size; i++)
	{
		int count = 0;
		//find the root of each node in the last row
		//the address of the last row is (size*size)-size +i
		//if the site is open
		if(set[size*size-size+i].isFull == false)
		{
			for(int j = 0; j< size; j++)
       		{
		        if(&set[j] == find_root(&set[size*size-size+i]))
			    {
		           	cout << "Matrix Percolates" << endl;
               	    return true;
               	}
	        }
		}
		else
		{
			continue;
		}
    }
    return false;
}

//print() for Point array
//outputs the array in the form of a matrix
void print(const Point * set, int size)
{
	for(int i = 0; i<(size*size); i++)
	{

		if( (i+1) % size == 0 )
		{
			cout << ((set[i].isFull) ? '1':'0') << "\n" ;
		}
		else 
		{
			cout << ((set[i].isFull) ? '1':'0'); 
		}
		
	}
}

//This function prints out the ppm file of the matrix
void print_out(const Point * set, int size)
{
	ofstream outFile ("grid.ppm");
	outFile << "P3" << endl;
	outFile << size << " " <<size << endl;
	outFile << 1 <<endl << endl;
	for(int i = 0; i<(size*size); i++)
	{
		if( (i+1) % size == 0 )
		{
			outFile << ((set[i].isFull) ? "1":"0") << "\n" ;
		}
		else 
		{
			outFile << ((set[i].isFull) ? "1 ":"0 "); 
		}
		
	}
	outFile.close();
}
//finds the root of a point
//practices compression
Point * find_root(Point *p)
{
	if(p->parent == p)
	{
		return p;
	}
	else
	{
		p->parent = find_root(p->parent);
		return p->parent;
	}

}

//takes two points and checks their isFull value
//returns true if equal, false if not
bool is_equal(Point p, Point q)
{
	if(p.isFull == q.isFull)
	{
		return true;
	}
	else
	{
		return false;
	}
}


//merges a smaller tree to a bigger tree
//accepts two roots only
void tree_union(Point * root1, Point * root2)
{
	if(root1->parent != root1 || root2->parent != root2)
	{
		throw "Error: attempted merge with non root, in function union(Point *, Point *) arguments must be root";

	}
	else
	{
		root2->parent = root1;
		root1->weight+= root2->weight;
	}
}

//finds an edge between points if there is one and unions
void find_cluster(Point * set, int size)
{
	//some Point pointers for possible roots
	Point * root1 = NULL;
	Point * root2 = NULL;

	//loop through the set
	for(int index = 0; index < size*size; index++)
	{
		//if we are checking the first index then there are no connections to consider
		if(index == 0)
		{
			continue;
		}
		//elseif we are checking an index less than size we only need to check the point to the left since there will be no upper point(still in top row)
		else if(index < size)
		{
			//check left
			if(is_equal(set[index],set[index-1]))
			{
				set[index].parent = &set[index-1];
				set[index-1].weight++;
				find_root(&set[index]);
			}
		}
	
		//else if the point is on the far left side then only check up
		else if(index % size == 0)
		{
			//check up
			if(is_equal(set[index],set[index-size]))
			{
				set[index].parent = &set[index-size];
				set[index-size].weight++;
				find_root(&set[index]);
			}
		}
		else
		{
			//check up
			if(is_equal(set[index],set[index-size]))
			{
				set[index].parent = &set[index-size];
				set[index-size].weight++;
				find_root(&set[index]);
				//check left
				if(is_equal(set[index],set[index-1]))
				{
					root1 = find_root(&set[index]);
					root2 = find_root(&set[index-1]);
					tree_union(root1,root2);
					find_root(&set[index]);
					find_root(&set[index-1]);
				}
			}
			//check left
			else if(is_equal(set[index],set[index-1]))
			{
				set[index].parent = &set[index-1];
				set[index-1].weight++;
				find_root(&set[index]);
			}
		}
		find_root(&set[index]);
	}
}

int clusters(Point * set, int size)
{
	int clusters = 0;
	for(int i = 0; i < size*size; i++)
	{
		if(set[i].parent== &set[i]) 
		{ 
			clusters+=1;
		}
	}
	return clusters;
}


