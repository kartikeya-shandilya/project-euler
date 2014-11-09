
global globalList, index
globalList=[{(1,0,0,0,0):1.0}]
cursor=0

def waysToPick():
	global cursor
	tempDict=globalList[cursor]
	for state in tempDict:
		prob=tempDict[state]
		for i in xrange(len(state)):
			if state[i]!=0:
				newState=[]
				for j in xrange(len(state)):
					if j<i: newState.append(state[j])
					elif j==i: newState.append(state[j]-1)
					else: newState.append(state[j]+1)
				newProb=prob*state[i]/(1.0*sum(state))
				newState=tuple(newState)
				if len(globalList)<(cursor+2):	globalList.append({})
				if newState not in globalList[cursor+1]: globalList[cursor+1][newState]=newProb
				else: globalList[cursor+1][newState]+=newProb
	cursor+=1

for k in xrange(16): waysToPick()

ans=0
for l in xrange(16):
	for tempState in globalList[l]:
		if sum(tempState)==1: ans+=globalList[l][tempState]

print ans-2
