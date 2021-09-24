def t_size(tt):
    sum = 0
    for i in range(len(tt)):
        if tt[i] != None:
            sum += 1
    return sum

def t_count(tt, el):
    sum = 0
    for i in range(len(tt)):
        if el == tt[i]:
            sum += 1
    return sum

def t_pop(tt):
    return tt.pop()


