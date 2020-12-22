import operator as op

def prod(vals):
    ans = 1
    for v in vals:
        ans *= v
    return ans

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

def parse2(s):
    s = s.split('*')
    vals = [eval(x) for x in s]
    return prod(vals)

def evl(s):
    while find_parens(s) != []:
        p = find_parens(s)[0]
        i, j = [int(x) for x in p]
        ans = parse(s[i+1:j])
        s = s.replace(s[i:j+1], str(ans))
    return parse(s)

def evl2(s):
    while find_parens(s) != []:
        p = find_parens(s)[0]
        i, j = [int(x) for x in p]
        ans = parse2(s[i+1:j])
        s = s.replace(s[i:j+1], str(ans))
    return parse2(s)

def run_tests(fname):
    tests = get_tests(fname)
    for test in tests:
        ans = test[1]
        s = test[0]
        assert evl(s) == ans

def run_tests2(fname):
    tests = get_tests(fname)
    for test in tests:
        ans = test[1]
        s = test[0]
        assert evl2(s) == ans

def part1():
    lines = get_input()
    ans = []
    for line in lines:
        ans.append(evl(line))
    return sum(ans)

def part2():
    lines = get_input()
    ans = []
    for line in lines:
        ans.append(evl2(line))
    return sum(ans)

run_tests('advent_day18_test.txt')
run_tests2('advent_day18_test2.txt')

ans = part1()
print(f'The answer to part 1 is: {ans}')

ans = part2()
print(f'The answer to part 2 is: {ans}')