
def repCards(p):
    p_new = []
    for c in p:
        c = c.upper()
        c = c.replace('A','E')
        c = c.replace('T','A')
        c = c.replace('J','B')
        c = c.replace('Q','C')
        c = c.replace('K','D')
        c = p_new.append(c)
    return p_new

seq = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']

def value(p, i, f, s):
    if f and s:
        return '8.' + p[-1][0]
    elif 4 in i:
        add = p[sum(i[:i.index(4)])][0]
        return '7.' + add
    elif (3 in i) and (2 in i):
        add = p[sum(i[:i.index(3)])][0]
        add += p[sum(i[:i.index(2)])][0]
        return '6.' + add
    elif f:
        add = p[4][0] + p[3][0] + p[2][0] + p[1][0] + p[0][0]
        return '5.' + add
    elif s:
        add = p[4][0]
        return '4.' + add
    elif 3 in i:
        add = p[sum(i[:i.index(3)])][0]
        add += (p[4][0] + p[3][0] + p[2][0] + p[1][0] + p[0][0]).replace(add,'')
        return '3.' + add
    elif len(i)==3 and (2 in i):
        add = p[sum(i[:i.index(1)])][0]
        add += (p[4][0] + p[3][0] + p[2][0] + p[1][0] + p[0][0]).replace(add,'')
        return '2.' + add
    elif 2 in i:
        add = p[sum(i[:i.index(2)])][0]
        add += (p[4][0] + p[3][0] + p[2][0] + p[1][0] + p[0][0]).replace(add,'')
        return '1.' + add
    else:
        add = p[4][0] + p[3][0] + p[2][0] + p[1][0] + p[0][0]
        return '.' + add

def evaluate(p):
    p = sorted(repCards(p))
    flush = [i[-1] for i in p] == [p[0][-1]]*len(p)
    straight = True
    info = []; last = '1'; cnt = 0
    for i in xrange(len(p)):
        if last != p[i][0]:
            if i!=0 : info.append(cnt)
            cnt = 1
        else: cnt += 1
        diff = seq.index(p[i][0]) - seq.index(last)
        if i!=0 and diff!=1: straight = False
        last = p[i][0]
    info.append(cnt)
    val = value(p, info, flush, straight)
    return val

f = open('C:\Users\Kartikeya\Documents\proe\poker.txt')
ans = 0

for line in f:
    line = line.strip()
    elms = line.split(' ')
    p1 = elms[:5]
    p2 = elms[5:]
    ans += (evaluate(p1) > evaluate(p2))

print ans
