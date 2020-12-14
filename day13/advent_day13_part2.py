'''
I can't claim victory today as I had took far too many hints
and sneak peaks!

buses = [(0, 13), (3, 41), (7, 37), (13, 659),
         (32, 19), (36, 23), (42, 29), (44, 409),
         (61, 17)]

where each tuple is (offset, bus_id)

find the first multiple of 13 that satisfies (t_0 + 3) % 41 == 0
now you have t_0 = 325 and t_3 = 328

what other numbers satisfy this condition? Once you know that it's

all t_0 += (13 * 41) * n for n=1,2,3...

life gets easier!  (apparently it's all here 
https://en.wikipedia.org/wiki/Chinese_remainder_theorem)

now move on

find n so that ((t_0 + 533*n) + 7) % 37 == 0

this is the new t_0 (t_0_new = t_0 + 533*n)

now we have t_0 = 81874 t_3 = 81877 and t_7 = 81811

numbers that statisfy all[(t_0 % 13 == 0), (t_3 % 41 == 0), (t_7 % 37)] are
t_0 += (13 * 41 * 37)*n for n=1,2,3...

etc.
'''

def find_t2(buses):
    """ The quick solution!
    """
    t = 0
    step = 1
    for offset, bus_id in buses:
        while (t + offset) % bus_id:
            t += step
        step *= bus_id   
    return t

def get_bus_ids(l):
    return [(i, int(t)) for i,t in enumerate(l.split(',')) if t != 'x']

def get_buses():
    with open('advent_day13.txt') as fid:
        lines = fid.readlines()
    return get_bus_ids(lines[1])

def get_test_cases():    
    with open('advent_day13_test_part2.txt') as fid:
        lines = fid.readlines()
    test_cases = []
    for i in range(0,len(lines),2):
        ans = int(lines[i].strip())
        bus_ids = get_bus_ids(lines[i+1])
        test_cases.append((ans, bus_ids))
    return test_cases

def test_departures(t, departures):
    for d in departures:
        if (t + d[0]) % d[1] != 0:
            return False
    return True

def find_t(buses):
    """ Brute force method
    
    Works on test cases, but is too slow for the problem case
    """
    n = 0
    while True:
        t = n * buses[0][1]
        if test_departures(t, buses):
            return t
        else:
            n += 1

def run_test_cases(func):
    test_cases = get_test_cases()
    for test_case in test_cases:
        ans = test_case[0]
        buses = test_case[1]
        assert(ans == func(buses))


buses = get_buses()
run_test_cases(find_t)
run_test_cases(find_t2)
t = find_t2(buses)
print(f'First timestamp that meets the criteria is {t}')