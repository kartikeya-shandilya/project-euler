
def has_rec_sum(x, s, b=[]):
    if int(x) == s:
        return True
    elif int(x) < s:
        return False
    else:
        flag = False
        for i in range(len(x)):
            # print (x, s, b, 'for loop', i)
            new_x = x[i+1:]
            new_sum = s - int(x[:i+1])
            new_buf = b[:] + [int(x[:i+1])]
            if new_sum < 0:
                continue
            if has_rec_sum(new_x, new_sum, new_buf):
                flag = True
                break
        return flag

if __name__ == "__main__":
    ans = 0
    for i in range(1, 1000001):
        result = has_rec_sum(str(i * i), i)
        ans += i
        if result:
            print(str(i * i), i)
    print (ans)
