
import sys
import pandas as pd
from collections import Counter

rows = []
for x in xrange(1,16):
	for y in xrange(x+1,16):
		for z in xrange(y+1,16):
			rows.append({'x':x, 'y':y, 'z':z, 'sum':x+y+z, 'product':x*y*z})

df = pd.DataFrame(rows)
df0 = df.copy() 
#print len(df)

scnt = Counter(df['sum'])
pcnt = Counter(df['product'])
invsums = [k for k in scnt.keys() if scnt[k]==1]
df = df[~df['sum'].isin(invsums)]
#print len(df)

invprod = {k for k in pcnt.keys() if pcnt[k]==1}
sumprod = {s:set(df[df['sum']==s]['product']) for s in scnt.keys()}
invsums = []
for s in scnt.keys():
	if len(invprod.intersection(sumprod[s])):
		invsums.append(s)

df = df[~df['sum'].isin(invsums)]
#print len(df)

scnt = Counter(df['sum'])
pcnt = Counter(df['product'])
invprod = {k for k in pcnt.keys() if pcnt[k]==1}
df = df[~df['product'].isin(invprod)]
#print len(df)

scnt = Counter(df['sum'])
invsums = [k for k in scnt.keys() if scnt[k]==1]
df = df[df['sum'].isin(invsums)]

print df

invprods = set(df0[df0['sum']==12]['product'])
#print df0[df0['product'].isin(invprods)].sort('product')


