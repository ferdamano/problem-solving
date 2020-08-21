import re

def simplify(poly):
    vars = []
    sim = ""
    found = re.findall(r'([+,-]*)(\d*)([a-z]+)', poly) 
    vars = list(set([''.join(sorted(x[2])) for x in found]))
    for v in sorted(sorted(vars), key=len):
        ans = 0
        for f in found:
            if ''.join(sorted(f[2])) == v:
                op = -1 if f[0] == '-' else 1
                coef = 1 if not(f[1]) else int(f[1])
                ans += (coef * op)
        if ans != 0:
            if ans == -1:
                ans = "-"
            elif ans == 1:
                ans = "" if not(sim) else "+"
            elif ans > 1 and sim:
                ans = "+"+str(ans)
            else:
                ans = str(ans)
            sim += ans+v
    return sim