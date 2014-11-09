#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main() {
 int i=0,j=0;
 vector<span> v[16][16];
 string line;
 ifstream myfile ("18.txt");
 if(myfile.is_open()) {
  while (!myfile.eof()) {
   getline (myfile,line);
   split(v, line, '|');
   cout << line << endl;
  }
  myfile.close();
 }
}
