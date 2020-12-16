from itertools import combinations

def find_invalid(numbers, preamble_len):
    for i in range(len(numbers) - preamble_len):
        subset = set(numbers[i:i+preamble_len])
        target = numbers[i+preamble_len]
        combos = [a+b for a,b in combinations(subset, 2)]
        if not target in combos:
            return target

def find_contiguous(numbers, target):
    n_numbers = len(numbers)
    for contig_len in range(2,len(numbers)):
        s = [sum(numbers[i:i+contig_len]) for i in range(n_numbers)]
        if target in s:
            i = s.index(target)
            block = numbers[i:i+contig_len]
            return min(block) + max(block)

with open('advent_day_9.txt') as fid:
    lines = fid.readlines()

numbers = [int(x.strip()) for x in lines]
target = find_invalid(numbers, preamble_len=25)
print('First # not meeting the requirements {}'.format(target))

ans = find_contiguous(numbers, target)
print('sum of min and max # in contigous block = {}'.format(ans))