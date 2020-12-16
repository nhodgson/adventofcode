from operator import xor

with open('advent_day2.txt') as fid:
    lines = fid.readlines()

valid = []
for line in lines:
    rule, passwd = line.split(':')
    rng, letter = rule.split()
    rng_min, rng_max = [int(x) for x in rng.split('-')]
    n = passwd.count(letter)
    if n > rng_min or n < rng_max:
        valid.append(1)

test_lines = ['1-3 a: abcde',
'1-3 b: cdefg',
'2-9 c: ccccccccc',
] 
valid = []
for line in lines:
    rule, passwd = line.split(':')
    passwd = passwd.strip()
    rng, letter = rule.split()
    pos_1, pos_2 = [int(x) for x in rng.split('-')]

    if xor(passwd[pos_1 - 1] == letter, passwd[pos_2 - 1] == letter):
        valid.append(1)
