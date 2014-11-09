
from random import randint

def getNum():
  all_num = []
  while 1:
    x = randint(0,999)
    if 1000-x in all_num:
      break
    all_num.append(x)
  return len(all_num)+1

tot_seen = 0
max_iter = 1000000

for i in xrange(max_iter):
  tot_seen += getNum()

print tot_seen/(1.0*max_iter)
