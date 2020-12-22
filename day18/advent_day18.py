import operator as op

def get_tests(fname='advent_day18_test.txt'):
    with open(fname) as fid:
        out = []
        for line in fid.readlines():
            expr, ans = line.strip().split('=')
            out.append((expr.strip(), int(ans)))

    return out

def get_input(fname='advent_day18.txt'):
    with open(fname) as fid:
        lines = fid.readlines()
    return [line.strip() for line in lines]

def find_parens(s):
    d = {}
    p = []
    for i, c in enumerate(s):
        if c == '(':
            p.append(i)
        elif c == ')':
            if len(p) == 0:
                raise Exception("No matching opening parentheses")
            d[p.pop()] = i

    if len(p) > 0:
        raise Exception("No matching closing parentheses")

    return sorted([k for k in d.items()], reverse=True)
    
OPS_MAP = {'+':op.add, '*': op.mul}

def parse(s):
    s = s.split()
    val = int(s[0])
    for i in range(0,len(s)-2,2):
        b = int(s[i+2])
        val = OPS_MAP[s[i+1]](val,b)

    return val

def evl(s):
    while find_parens(s) != []:
        p = find_parens(s)[0]
        i, j = [int(x) for x in p]
        print(i,j,s[i+1:j])
        ans = parse(s[i+1:j])
        s = s.replace(s[i:j+1], str(ans))
    return parse(s)

def run_tests():
    tests = get_tests()
    for test in tests:
        ans = test[1]
        s = test[0]
        assert evl(s) == ans

def part1():
    lines = get_input()
    ans = []
    for line in lines:
        ans.append(evl(line))
    return sum(ans)


ans = part1()
print(f'The answer to part 1 is: {ans}')