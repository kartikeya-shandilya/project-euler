
f(n, k) = sum(i=1,k,g(n,i))
g(n, k) = if(k==1|k==n,1,if(k<n-k,f(n-k,k),f(n-k,n-k)))
h(n) = f(n,n)

(18:29) gp > for(x=1,20,print(x," ",h(x)))
1 1
2 2
3 3
4 5
5 7
6 11
7 15
8 22
9 30
10 42
11 56
12 77
13 101
14 135
15 176
16 231
17 297
18 385
19 490
20 627