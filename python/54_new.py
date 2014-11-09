
from operator import itemgetter

seq = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']
vals = [5.0, 7.0, 9.0, 11.0, 11.5, 12.5, 13.0, 17.0, 18.0]

def repCards(h):
    h = h.replace('A','E')
    h = h.replace('T','A')
    h = h.replace('J','B')
    h = h.replace('Q','C')
    h = h.replace('K','D')
    return h

def value(h, i, f, s):
	val = vals.index(sum([j**2 for j in i]) + (f*6.5 + s*7.5))
	i_new=[]
	for j in i:	i_new.extend([j]*j)
	h_new = [(h[j][0],i_new[j]) for j in xrange(len(i_new))]
	h_new = sorted(h_new, key=itemgetter(1, 0))[::-1]
	add = ''.join([i[0] for i in h_new])
	return `val` + '.' + add

def evaluate(hands):
    flush = [i[-1] for i in hands] == [hands[0][-1]]*len(hands)
    straight = True
    info = []; last = '1'; cnt = 0
    for i in xrange(len(hands)):
        if last != hands[i][0]:
            if i!=0 : info.append(cnt)
            cnt = 1
        else: cnt += 1
        diff = seq.index(hands[i][0]) - seq.index(last)
        if i!=0 and diff!=1: straight = False
        last = hands[i][0]
    info.append(cnt)
    val = value(hands, info, flush, straight)
    return val

f = open('poker.txt')
ans = 0

for line in f:
    line = line.strip()
    elms = repCards(line).split(' ')
    h1 = sorted(elms[:5])
    h2 = sorted(elms[5:])
    ans += (evaluate(h1) > evaluate(h2))

print ans
