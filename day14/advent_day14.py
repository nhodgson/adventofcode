from itertools import product

def load_instructions(fname):
    with open(fname) as fid:
        lines = fid.readlines()
    
    instructions = []
    for line in lines:
        if line.startswith('mask'):
            mask = line.split('=')[1].strip()
            instructions.append(('mask', mask))
        elif line.startswith('mem'):
            start = line.index('[') + 1
            stop = line.index(']')
            address = line[start:stop]
            val = line.split('=')[1].strip()
            instructions.append(('mem', int(address), int(val)))
    return instructions

def apply_bit_mask(mask, val):
    bits = '{0:036b}'.format(val)
    bits_out = ''
    for i, m in enumerate(mask):
        if m != 'X':
            bits_out += m
        else:
            bits_out += bits[i]
    return int(bits_out, 2)

def apply_floating_bit_mask(mask, val):
    bits = '{0:036b}'.format(val)
    bits_out = ''
    for i, m in enumerate(mask):
        if m == '0':
            bits_out += bits[i]
        elif m in ['1', 'X']:
            bits_out += m
        else:
            ValueError('Unrecognised value')
    return bits_out

def generate_combos(bits):
    f_indx = [i for i, bit in enumerate(bits) if bit == 'X']
    
    bits_out_combos = []
    for combo in product(('0','1'),repeat=len(f_indx)):
        new_bits = list(bits)
        for i, b in enumerate(combo):
            new_bits[f_indx[i]] = b
        bits_out_combos.append(''.join(new_bits))

    return [int(b, 2) for b in bits_out_combos]

def run_instructions(instructions):
    mem = {}
    for i in instructions:
        if i[0] == 'mask':
            curr_mask = i[1]
        elif i[0] == 'mem':
            _, addr, val = i
            mem[addr] = apply_bit_mask(curr_mask, val)
        else:
            ValueError('Instruction not recognised, got {i[0]}')
    return mem

def run_instructions2(instructions):
    mem = {}
    for i in instructions:
        if i[0] == 'mask':
            curr_mask = i[1]
        elif i[0] == 'mem':
            _, addr, val = i
            b = apply_floating_bit_mask(curr_mask, addr)
            addrs = generate_combos(b)
            for addr in addrs:
                mem[addr] = val
        else:
            ValueError('Instruction not recognised, got {i[0]}')
    return mem

instructions = load_instructions('advent_day14.txt')
mem = run_instructions(instructions)

print('Part 1')
print(f'Sum of all values in memory = {sum(mem.values())}')

mem = run_instructions2(instructions)
print('Part 2')
print(f'Sum of all values in memory = {sum(mem.values())}')