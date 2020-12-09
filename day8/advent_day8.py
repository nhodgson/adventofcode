
def run_boot(instructions):
    indx = 0
    acc = 0
    n_instructions = len(instructions)
    
    while True:

        if indx == n_instructions:
            return acc, True

        op, val, visited = instructions[indx]
        
        if visited:
            return acc, False
        else:
            instructions[indx][2] = True

        if op == 'nop':
            indx += 1
        
        elif op == 'jmp':
            indx += val

        elif op == 'acc': 
            acc += val
            indx += 1
        else:
            ValueError('op not recognised')


def load_instructions():
    with open('advent_day8.txt') as fid:
        lines = fid.readlines()

    lines = [l.strip().split() for l in lines]

    instructions = [[i[0], int(i[1]), False] for i in lines]

    return instructions

instructions = load_instructions()
#acc, completed = run_boot(instructions)

n  = [i for i, v in enumerate(instructions) if v[0] in ('nop','jmp')]

for indx in n:
    i = load_instructions()
    if i[indx][0] == 'nop':
        i[indx][0] = 'jmp'
    elif i[indx][0] == 'jmp':
        i[indx][0] = 'nop'
    else:
        pass
    acc, completed = run_boot(i)
    if completed:
        break

print('Value of acc = {}'.format(acc))