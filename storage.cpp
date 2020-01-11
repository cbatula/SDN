#include <bits/stdc++.h> 
using namespace std; 
  
const int SIZE = 32;	//Always make sure SECTION * SIZE is 256
const int SECTION = 8;	//Need to change the assignment functions for different SECTION values 
//USE AN ARRAY FOR ASSIGNMENT? ONLY ONE DIVISION WOULD BE NECESSARY
static int counter = 1;

union TrieNode 
{ 
    union TrieNode *children[SECTION][SIZE];	//HOW THE FUCK DO I INITIALIZE THIS?
    struct TrieEndNode *children[SECTION][SIZE]; 
}; 

struct TrieEndNode 
{ 
    bool isOld; 
    int in_value;
    int out_value;
}; 

   
struct TrieNode *getNode(void)
{ 
    struct TrieNode *pNode =  new TrieNode;
  
    pNode->isOld = false;	//SEE: DEFINITION
    for (int i = 0; i < SECTION; i++)
        for (int j = 0; j < SIZE; i++)
            pNode->children[i][j] = NULL;
  
    return pNode;
}

bool search(struct TrieNode *root, int ip[4])
{ 

	struct TrieNode *it = root; 
	for (int i = 0; i < 4; i++) 
	{ 

		if()
		{
			return false //increment root
		}
		
	}
	
	return true;
}
