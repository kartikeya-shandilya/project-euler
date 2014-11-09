
#seq="UDDDUdddDDUDDddDdDddDDUDDdUUD"
seq="DdDddUUdD"

def trans(eq, cd):
    if cd == "D":
        return [3*eq[0], 3*eq[1]]
    if cd == "U":
        return [3*eq[0]/4.0, (3*eq[1]- 2)/4.0]
    if cd == "d":
        return[3*eq[0]/2.0, (3*eq[1] + 1)/2.0]

#st=[3,2]
st=[3,0]
print st,
for i in xrange(0,len(seq)):
    char = seq[len(seq)-i-1]
    st = trans(st, char)
    print char
    print st,

#init=10**15+1
init=10**6+1
while 1:
    if (init-st[1])/st[0] == int((init-st[1])/st[0]):
        print init
        break
    init+=1

