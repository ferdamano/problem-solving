def solution(a):
    sm_num = min(a)
    while not( all(x % sm_num == 0 for x in a)):
        a = sorted(a)
        lg_num = a[-1]
        sm_num = a[0]
        if lg_num % sm_num == 0:
            a[-1] = sm_num
        else:
            a[-1] = lg_num % sm_num
    return len(a) * sm_num