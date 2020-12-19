'''
Part 1 
======

In the initial state of the pocket dimension, almost all cubes start inactive. 
The only exception to this is a small flat region of cubes (your puzzle input); 
the cubes in this region start in the specified active (#) or inactive (.) 
state.

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors: any of the 26 other cubes where 
any of their coordinates differ by at most 1. For example, given the cube at 
x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at 
x=0,y=2,z=3, and so on.

During a cycle, all cubes simultaneously change their state according to the 
following rules:

    - If a cube is active and exactly 2 or 3 of its neighbors are also active, 
    the cube remains active. Otherwise, the cube becomes inactive.
    - If a cube is inactive but exactly 3 of its neighbors are active, the cube 
    becomes active. Otherwise, the cube remains inactive.

Starting with your given initial configuration, simulate six cycles. How many 
cubes are left in the active state after the sixth cycle?
'''
from itertools import product
import numpy as np

def get_input(fname):
    with open(fname) as fid:
        lines = fid.readlines()

    out = []
    for i, line in enumerate(lines):
        out.append([])
        for l in line.strip():
            if l == '.':
                out[i].append(0)
            else:
                out[i].append(1)

    return np.array(out)

# iterate over blocks
def update_state(input_state):
    ni, nj, nk = input_state.shape
    output_state = np.zeros_like(input_state)
    for i in range(1,ni):
        for j in range(1,nj):
            for k in range(1,nk):
                is_active = input_state[i,j,k]
                neighbors = input_state[i-1:i+2, j-1:j+2, k-1:k+2]
                n_active_neighbors = neighbors.sum() - is_active
                if is_active:
                    if n_active_neighbors in [2,3]:
                        output_state[i,j,k] = 1
                    else:
                        output_state[i,j,k] = 0
                else:
                    if n_active_neighbors == 3:
                        output_state[i,j,k] = 1
    return output_state

def nested_for_loop(r,n):
    p = [r for _ in range(n)]
    return product(*p)

def update_state_4d(input_state):

    dim = input_state.shape[0]
    if not all([i==dim for i in input_state.shape]):
        ValueError(f'Expect all dimensions are equal! Shape = {input_state.shape}')
    
    output_state = np.zeros_like(input_state)
    for c in nested_for_loop(range(1,dim),4):
        x,y,z,w = c
        
        is_active = input_state[x,y,z,w]
        neighbors = input_state[x-1:x+2, y-1:y+2, z-1:z+2, w-1:w+2]
        n_active_neighbors = neighbors.sum() - is_active
        if is_active:
            if n_active_neighbors in [2,3]:
                output_state[x,y,z,w] = 1
            else:
                output_state[x,y,z,w] = 0
        else:
            if n_active_neighbors == 3:
                output_state[x,y,z,w] = 1

    return output_state

def part_one(initial_state):

    idims = initial_state.shape[0]

    dims = idims * 5

    a = np.zeros((dims,dims,dims),dtype=int)

    # centre
    c = int(dims / 2)
    w = int(idims / 2)
    start = c - w
    stop = c + w 

    if idims % 2 != 0: stop += 1

    a[c, start:stop, start:stop] = initial_state

    output_state = a
    for _ in range(6):
        output_state = update_state(output_state)

    n_active = np.count_nonzero(output_state == 1) 

    return n_active 

def part_two(initial_state):

    idims = initial_state.shape[0]

    dims = idims * 5

    a = np.zeros((dims,dims,dims,dims),dtype=int)

    # centre
    c = int(dims / 2)
    w = int(idims / 2)
    start = c - w
    stop = c + w 

    if idims % 2 != 0: stop += 1

    a[c, start:stop, start:stop, c] = initial_state

    output_state = a
    for i in range(6):
        print(f'Iteration {i} / 6')
        output_state = update_state_4d(output_state)

    n_active = np.count_nonzero(output_state == 1) 

    return n_active 


initial_state = get_input('advent_day17.txt')
n_active = part_one(initial_state)
print(f'Part 1: Number of active positions = {n_active}')

n_active = part_two(initial_state)
print(f'Part 2: Number of active positions = {n_active}')