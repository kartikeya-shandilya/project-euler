
import operator
from pprint import pprint
from random import shuffle, randint

# define game
sq = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

CC = ['GO', 'JAIL', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
CH = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'nextR', 'nextR','nextU', 'min3', 1, 2, 3, 4, 5, 6]
shuffle(CC); shuffle(CH);

nextR = {'CH1':'R2', 'CH2':'R3', 'CH3':'R1'}
nextU = {'CH1':'U1', 'CH2':'U2', 'CH3':'U1'}
min_3 = {'CH1':'T1', 'CH2':'D3', 'CH3':'CC3'}

# util functions
def dice():
        return randint(1,4) + randint(1,4)

def f_CH(frm,to):
        if to in sq:
                return to
        elif to=='nextR':
                return nextR[frm]
        elif to=='nextU':
                return nextU[frm]
        elif to=='min_3':
                return min_3[frm]
        return frm

def f_CC(frm,to):
        if to in sq:
                return to
        return frm

# initialize counts
me = 0; counts = {};
for i in sq:
        counts[i] = 0

# run simulation
for i in xrange(10**6):
        roll = dice()
        last = sq[me]
        me = (me + roll)%40
        here = sq[me]
        if   here[:2]=='CH':
                dest = f_CH(here,CH[0])
                CH = CH[1:] + [CH[0]]
        elif here[:2]=='CC':
                dest = f_CC(here,CC[0])
                CC = CC[1:] + [CC[0]]
        elif here=='G2J':
                dest = 'JAIL'
        else:
                dest = here
        me = sq.index(dest)
        #print 'last, roll, here, CH[-1], CC[-1], dest', last, roll, here, CH[-1], CC[-1], dest
        counts[dest] += 1

pprint(sorted(counts.iteritems(),key=operator.itemgetter(1)))

