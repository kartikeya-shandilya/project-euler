
F = node(inf, False, False)
T = node(inf, True, True)

class node():
	def __init__(self, value, hi=nan, low=nan):
		self.value=value
		self.hi=hi
		self.low=low

def make_zdd(initial = init, condition, no):
	if no == 1:
		initial.hi = T
		initial.low = F
		return
	if condition:
		initial.low = node(condition[0])
		
	make_zdd()
		


def get_zdd(condition, no):
	cond = sorted(condition[x] + 10*x for x in xrange(condition))
	return make_zdd(cond, no)

