#include<iostream>
#include<fstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int split(vector<string>& v, const string& str, char c)
{
 v.clear();
 string::const_iterator s = str.begin();

 while(true){
  string::const_iterator begin = s;
  while(*s != c && s != str.end()){ ++s; }
  v.push_back(string(begin, s));

  if(s == str.end()){
   break;
  }

  if(++s == str.end()){
   v.push_back("");
   break;
  }

 }
 return v.size();
}

int main(){

 int i=0,j=0,k;
 vector<string> v;
 char line[1024];
 int Arr[5][5];

 ifstream myfile ("81_2.txt");
 if(myfile.is_open()){
  while(myfile.getline(line,1024)){
   split(v, line, ',');
   for (j=0;j<5;j++) {
    Arr[i][j]=atoi(v[j].c_str());
   }
   i++;
  }
  myfile.close();
 }

 int Min[6][6];
 for(i=0;i<6;i++){
   Min[0][i]=-1;
   Min[i][0]=-1;
 }
 Min[1][1]=131;
 Min[3][3]=-1;
 
 for(i=1,j=0,k=0;k<10;){
  k++;
  if(Min[3][3]==-1){
   i=j+1; j=0;
   while(i>=0){
    Min[i+1][j+1]=(Min[i][j+1]<Min[i+1][j])?
                    ((Min[i][j+1]!=-1)?(Min[i][j+1]+Arr[i][j]):(Min[i+1][j]+Arr[i][j]))
                   :((Min[i+1][j]!=-1)?(Min[i+1][j]+Arr[i][j]):(Min[i][j+1]+Arr[i][j]));
    cout<<i<<" "<<j<<" "<<Arr[i][j]<<" "<<Min[i+1][j+1]<<endl;
    i--; j++;
   }
   j--; cout<<endl;
  }
  else{
   j=i+1; i=4;
   while(j<=4){
    Min[i+1][j+1]=(Min[i][j+1]<Min[i+1][j])?
                    ((Min[i][j+1]!=-1)?(Min[i][j+1]+Arr[i][j]):(Min[i+1][j]+Arr[i][j]))
                   :((Min[i+1][j]!=-1)?(Min[i+1][j]+Arr[i][j]):(Min[i][j+1]+Arr[i][j]));
    cout<<i<<" "<<j<<" "<<Arr[i][j]<<" "<<Min[i+1][j+1]<<endl;
    i--; j++;
   }
   i++; cout<<endl;
  }
 }

}

