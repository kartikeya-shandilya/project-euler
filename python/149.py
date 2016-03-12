
class fib_gen(object):
    def __init__(self):
        self.s_cache = [0]
        for i in xrange(1, 55+1):
            num = (100003 - 200003*i + 300007*i**3) % 10**6 - 500000
            self.s_cache.append(num)

    def get(self, i):
        if i <= 55:
            return self.s_cache[i]
        else:
            num = (self.s_cache[32] + self.s_cache[1]) % 10**6 - 500000
            self.s_cache = self.s_cache[1:]+[num]
            return num

# populate 2000x2000 matrix
seq = fib_gen()
fib_mat = []
for i in xrange(2000):
    fib_mat.append([])
    for j in xrange(2000):
        n = i*2000 + j + 1
        fib_mat[i].append(seq.get(n))


class max_sum(object):
    def __init__(self):
        self.max_sofar = 0
        self.max_incl = 0

    def next(self, i):
        self.max_incl = max(i, self.max_incl+i)
        self.max_sofar = max(self.max_sofar, self.max_incl)
        return self.max_sofar

# H search
max_res = 0
for row in fib_mat:
    tmp_max = 0
    max_s = max_sum()
    for elm in row:
        tmp_max = max_s.next(elm)
    max_res = max(max_res, tmp_max)
print 'max_h = %s' % max_res

# V search
max_res = 0
for i in xrange(2000):
    col = [row[i] for row in fib_mat]
    tmp_max = 0
    max_s = max_sum()
    for elm in col:
        tmp_max = max_s.next(elm)
    max_res = max(max_res, tmp_max)
print 'max_v = %s' % max_res


def is_valid(cell, n=2000):
    chk_x = cell[0] >= 0 and cell[0] < 2000
    chk_y = cell[1] >= 0 and cell[1] < 2000
    return chk_x and chk_y


def add_cell(cell1, cell2):
    cell_x = cell1[0] + cell2[0]
    cell_y = cell1[1] + cell2[1]
    return [cell_x, cell_y]


def get_diag(cell, flag, stage, limit, move, shift, n=2000):
    cells = []
    while is_valid(cell):
        cells.append(cell)
        cell = add_cell(cell, move[flag])
    if cells[-1] == limit:
        stage = 1 - stage
    cell = add_cell(cells[-1], shift[flag == stage])
    flag = 1-flag
    return cells, cell, flag, stage


def get_cell(elm, fib_mat=fib_mat):
    return fib_mat[elm[0]][elm[1]]

# D search
flag = 1; stage = 1;
cell = [0, 0]; limit = [1999,0];
move = [[1, -1], [-1, 1]]
shift = [[1, 0], [0, 1]]
max_res = 0
while cell!=[1999, 1999]:
    diag, cell, flag, stage = get_diag(cell, flag, stage, limit, move, shift)
    tmp_max = 0
    max_s = max_sum()
    for elm in diag:
        num = get_cell(elm)
        tmp_max = max_s.next(num)
    max_res = max(max_res, tmp_max)
print 'max_d = %s' % max_res

# Anti-D search
flag = 1; stage = 1;
cell = [0, 1999]; limit = [0,0];
move = [[-1, -1], [1, 1]]
shift = [[0, -1], [1, 0]]
max_res = 0
while cell!=[1999, 0]:
    diag, cell, flag, stage = get_diag(cell, flag, stage, limit, move, shift)
    tmp_max = 0
    max_s = max_sum()
    for elm in diag:
        num = get_cell(elm)
        tmp_max = max_s.next(num)
    max_res = max(max_res, tmp_max)
print 'max_ad = %s' % max_res
