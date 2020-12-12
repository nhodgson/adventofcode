def load_adapters(fname):
    with open(fname) as fid:
        lines = fid.readlines()

    return [int(x.strip()) for x in lines]

# trying to stick to pure Python, so avoiding numpy
def diff(arr):
    return [arr[i+1] - arr[i] for i in range(len(arr)-1)]

def get_n_combinations(adapters):
    
    # create counter to store how many 
    # combos of connections there are back to the device
    nc = {}
    
    # first connection must be ok
    if not adapters[1] - adapters[0] <= 3:
        raise ValueError('First adapter is not rated correctly!')
    else:
        nc[0] = 1
    
    # for each jolt, count how many previous possible 
    # connections there were for each possible connection
    for jolt in sorted(adapters):
        #print(nc)
        nc[jolt] = 0
        if jolt - 1 in nc:
            nc[jolt] += nc[jolt - 1]
        if jolt - 2 in nc:
            nc[jolt] += nc[jolt - 2]
        if jolt - 3 in nc:
            nc[jolt] += nc[jolt - 3]

    return nc[adapters[-1]]

adapters = load_adapters('advent_day10.txt')
adapters.sort()
adapters.append(adapters[-1] + 3)
adapters.insert(0,0)

vdiffs = diff(adapters)

n3 = vdiffs.count(3)
n1 = vdiffs.count(1)
ans = n1 * n3

print(f'Part 1: n1 * n3 = {ans}')

ncombos = get_n_combinations(adapters[1:])
print(f'Part 2: number of combinations = {ncombos}')

'''
# Example

[0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
1 can connect to 0 (1 connection)
4 can connect to 1 (1 connection)
5 can connect to 4 (1 connection)
6 can connect to 5 (1 connection) + 4 (1 connection) = 1 + 1 = 2 connections in total
[0, 1, 4, 5, 6]
[0, 1, 4, 6]
7 can connect to 6 (2 connections) + 5 (1 connection) + 4 (1 connection) = 2 + 1 + 1 = 4 connections in total
[0,1,4,5,6,7]
[0,1,4,6,7]
[0,1,4,5,7]
[0,1,4,7]
etc.
'''

    
	