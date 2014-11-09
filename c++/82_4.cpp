#include <iostream>
#include <fstream>
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
 int i=1,j=0,k;
 int z=80;
 vector<string> v;
 char line[1024];
 int Arr[z+2][z];
 ifstream myfile ("82.txt");
 if(myfile.is_open()){
  while(myfile.getline(line,1024)){
   split(v, line, ',');
   for (j=0;j<z;j++) {
    Arr[i][j]=atoi(v[j].c_str());
   }
   i++;
  }
  myfile.close();
 }
 int Min[z+2][z],Temp[z+2];
 for(i=0;i<z;i++){
  Min[0][i]=-999999999;
  Min[z+1][i]=-999999999;
  Min[i+1][0]=Arr[i+1][0];
 }
 for(j=1,k=0;j<z;j++){
  for(i=1;i<z+1;i++){
   Temp[i]=Min[i][j-1]+Arr[i][j];
   if (Min[i][j-1]<0) Temp[i]=-999999999;
//   if(i<10 && j<10){ cout<<Arr[i][j]<<" "<<Temp[i]<<endl; }
  }
  Temp[0]=-999999999; Temp[z+1]=-999999999;
  int mini=999999999;
  for(i=1;i<z+1;i++){
   cout<<"for Min["<<i<<"]["<<j<<"] : "<<endl;
   mini=Temp[i];
   int temp=0;
   temp=Temp[i];
   for(k=i-1;k>0;k--){
    if (k==i-1) { cout<<"loop1"<<endl; }
    if (Min[k+1][j-1]>=0 && Temp[k]>=0) { temp=temp-Min[k+1][j-1]+Temp[k]; }
    if (temp<mini && temp>=0) { mini=temp; }
    cout<<temp<<endl;
   }
   temp=Temp[i];
   for(k=i+1;k<z+1;k++){
    if (k==i+1) { cout<<"loop2"<<endl; }
    if (Min[k-1][j-1]>=0 && Temp[k]>=0) { temp=temp-Min[k-1][j-1]+Temp[k]; }
    if (temp<mini && temp>=0) { mini=temp; }
    cout<<temp<<endl;
   }
   Min[i][j]=mini;
   cout<<"mini : "<<mini<<endl;
  }
 }
 int mini=999999999;
 for(k=1;k<z+1;k++){
  if((Min[k][z-1]<mini)&&(Min[k][z-1]>0)) mini=Min[k][z-1];
//  cout<<"Min["<<k<<"][z-1] : "<<Min[k][z-1]<<endl;
 }
 cout<<endl<<"Ans : "<<mini<<endl<<endl;
 int l,m=5;
 for(k=1;k<m+1;k++){
  for(l=0;l<m;l++){
   cout<<Arr[k][l]<<" ";
  }
  cout<<endl;
 }
 cout<<endl;
 for(k=1;k<m+1;k++){
  for(l=0;l<m;l++){
   cout<<Min[k][l]<<" ";
  }
  cout<<endl;
 }
 cout<<endl;
}
