#include<iostream>
#include<fstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int split(vector<string>& v, const string& str, char c){
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

int minim(int a, int b,int c){
 int min=999999999;
 if((a<min)&&(a>-1)) { min=a; }
 if((b<min)&&(b>-1)) { min=b; }
 if((c<min)&&(c>-1)) { min=c; }
 return min;
}

int main(){
 int i=0,j=0,k;
 vector<string> v;
 char line[1024];
 int Arr[5][5];
 ifstream myfile ("82_2.txt");
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
 int Min[7][6],Temp[7];
 for(i=0;i<7;i++){
  Min[i+1][1]=Arr[i][0];
  Min[i][0]=-999;
  Min[81][i]=-999;
 }
 Min[0][0]=-999;

 for(j=1,k=0;j<5;){
  cout<<"Min ";
  for(i=0;i<6;i++){
   cout<<Min[i][j]<<" ";
  }
  cout<<endl;
  cout<<"Temp ";
  for(i=0;i<6;i++){
   Temp[i+1]=Min[i+1][j]+Arr[i][j];
   if (Min[i][j]<0) Temp[i+1]=-999;
   cout<<"("<<i+1<<")"<<Temp[i+1]<<" ";
  }
  cout<<endl;
  Temp[0]=-999; Temp[6]=-999;
  for(i=0;i<6;i++){
   Min[i+1][j+1]=minim(Arr[i][j]+Temp[i],Temp[i+1],Arr[i][j]+Temp[i+2]);
   cout<<"for"<<i<<" "<<j<<" "<<Arr[i][j]+Temp[i]<<" "<<Temp[i+1]<<" "<<Arr[i][j]+Temp[i+2]<<" >> "<<Min[i+1][j+1]<<endl;
  }
  j++; 
  cout<<endl;
 }
 for(k=0;k<7;k++){
  cout<<Min[k][5]<<" ";
 }
}

