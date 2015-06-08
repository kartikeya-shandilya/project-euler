#! /usr/bin/env python
from math import sqrt
from time import time
def pg():
	lim=raw_input("\nGenerate prime numbers up to what number? : ")
	sqrtlim=sqrt(float(lim))
	pp=2
	ep=[pp]
	ss=[pp]
	pp+=1
	i=0
	rss=[ss[0]]
	tp=[pp]
	xp=[]
	pp+=ss[0]
	npp=pp
	tp.append(npp)
	rss.append(rss[i]*tp[0])
	bt=time()
	while npp<int(lim):
		i+=1
		while npp<rss[i]+1:
			for n in ss:
				npp=pp+n
				if npp>int(lim): break
				if npp<=rss[i]+1: pp=npp
				sqrtnpp=sqrt(npp)
				test=True
				for q in tp:
					if sqrtnpp<q: break
					elif npp%q==0:
						test=False
						break
				if test:
					if npp<=sqrtlim: tp.append(npp)
					else: xp.append(npp)
			if npp>int(lim): break
		if npp>int(lim): break
		lrpp=pp
		nss=[]
		while pp<(rss[i]+1)*2-1:
			for n in ss:
				npp=pp+n
				if npp>int(lim): break
				sqrtnpp=sqrt(npp)
				test=True
				for q in tp:
					if sqrtnpp<q: break
					elif npp%q==0:
						test=False
						break
				if test:
					if npp<=sqrtlim: tp.append(npp)
					else: xp.append(npp)
				if npp%tp[0]!=0:
					nss.append(npp-lrpp)
					lrpp=npp
				pp=npp
			if npp>int(lim): break
		if npp>int(lim): break
		ss=nss
		ep.append(tp[0])
		del tp[0]
		rss.append(rss[i]*tp[0])
		npp=lrpp
	et=time()
	i=nss=npp=n=sqrtnpp=test=q=r=lrpp=rss=ss=pp=sqrtlim=0
	tt=et-bt
	ep.reverse()
	[tp.insert(0,a) for a in ep]
	tp.reverse()
	[xp.insert(0,a) for a in tp]
	print "\nIt took",tt,"seconds to generate the prime set up to: ",lim,"\nwith",len(xp),"members."
	et=bt=ep=tp=a=tt=lim=0
	return xp
def ui(a):
	m="\nDo you wish to review the numbers? Enter y for yes or q to quit. "
	n="From: "
	o="To: "
	p="or"
	q="is out of the range of the set generated."
	r="and"
	s="There are none between"
	t="\nPlease pick between 0"
	u="\nThey are the"
	v="th thru"
	w="th members."
	x="\nPlease choose a number that is less than"
	y="a prime number."
	z="\nThere are"
	A="members of the prime set"
	C="Make a selection or enter q to quit. "
	f=raw_input(m)
	while f!='q':
		if f=='y':
			print "\nChoose a category:"
			print "a) Pick a range of indexes of members of the prime number set."
			print "b) Pick a range of numbers to view prime numbers in that range."
			print "d) Input a number to check its membership in the prime number set."
			print "e) Get the number of members in the prime set up to a particular number."
			print "f) Get the number of members in the prime set between a range of numbers."
			print "v) View 100 primes at a time."
			f=raw_input(C)
			if f=='a':
				print t,r,len(a)
				f=raw_input(n)
				g=raw_input(o)
				if int(g)<int(f):
					h=f
					f=g
					g=h
				if int(f)<0 or int(g)>len(a): print f,p,g,q
				elif f==g: print s,f,r,g
				else: print [a[h] for h in range(int(f),int(g))],"\n",u,str(int(f)+1)+v,str(g)+w
			if f=='b':
				print t,r,a[len(a)-1]+1
				f=raw_input(n)
				g=raw_input(o)
				if int(g)<int(f):
					h=f
					f=g
					g=h
				if int(f)<0 or int(g)>a[len(a)-1]+1: print f,p,g,q
				elif f==g: print s,f,r,g
				else:
					i=0
					while a[i]<int(f): i+=1
					j=i
					while i<len(a) and a[i]<=int(g):
						print a[i],
						i+=1
					print u,str(int(j)+1)+v,str(i)+w
			if f=='d':
				print x,a[len(a)-1]+1
				f=raw_input("What number do you want to check? ")
				for g in a:
					if int(g)==int(f): print f,"is",y
					if int(g)>int(f): print f,"is not",y
					if int(f)<0 or int(g)>=int(f): break
				if int(f)>g+1 or int(f)<0: print f,q
			if f=='e':
				print x,a[len(a)-1]+2
				f=raw_input(o)
				if -1<int(f)<a[len(a)-1]+2:
					g=0
					while a[g]<=int(f):
						g+=1
						if g==len(a): break
					print z,g,A,"up to",f
				else: print f,q
			if f=='f':
				print t,r,a[len(a)-1]+1
				f=raw_input(n)
				g=raw_input(o)
				if int(g)<int(f):
					h=f
					f=g
					g=h
				i=0
				if int(f)<0 or int(g)>a[len(a)-1]+1: print f,p,g,q
				elif f==g: print s,f,r,g
				else:
					for j in a:
						if int(f)<=int(j)<=int(g): i+= 1
						elif int(j)>int(g): break
					print z,i,A,"from",f, "thru",g
			if f=='v':
				g=0
				h=1
				while f!='q' and g<len(a):
					i=h*100
					for g in range(100*(h-1),i):
						if g==len(a):
							i=len(a)
							break
						print a[g],
					print u,str(100*(h-1)+1)+v,str(i)+w
					h+=1
					if g==len(a): break
					f=raw_input("\nView the next 100 members or enter q to quit. ")
		f=raw_input(m)
def run(a='r'):
	while a is 'r':
		a=raw_input("\nEnter r to run prime generator. ")
		if a!='r': return
		b=pg()
		ui(b)
if __name__ == "__main__":
	run()
	print "\n"*5,"Don't go away mad...Just go away.","\n"*5
	raw_input()

