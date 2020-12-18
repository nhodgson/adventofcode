import numpy as np

def get_fields(lines):
    fields = {}
    for line in lines:
        if line.strip() != '':
            field, vals = line.split(':')
            a = vals.strip().split(' or ')
            b = [[int(x) for x in i.split('-')] for i in a]
            fields[field] =  b 
        else:
            break
    return fields

def get_ticket(lines):
    for i, line in enumerate(lines):
        if line.startswith('your ticket'):
            break
    return [int(x) for x in lines[i+1].strip().split(',')]

def get_nearby_tickets(lines):
    for i, line in enumerate(lines):
        if line.startswith('nearby'):
            break
    tmp = lines[i+1:]
    nearby_tickets = []
    for ticket in tmp:
        nearby_tickets.append([int(x) for x in ticket.strip().split(',')])
    
    return nearby_tickets

def get_input(fname):
    with open(fname) as fid:
        lines = fid.readlines()
    
    fields = get_fields(lines)
    my_ticket = get_ticket(lines)
    nearby_tickets = get_nearby_tickets(lines)

    return fields, my_ticket, nearby_tickets

def expand_fields(fields):
    valid_numbers = []
    for field in fields:
        rng = fields[field]
        for r in rng:
            valid_numbers.extend(range(r[0], r[1]+1))
            
    return set(valid_numbers)

def count_invalid(fields, nearby_tickets):
    valid_numbers = expand_fields(fields)
    invalid_count = 0
    valid_tickets = []
    for i, ticket in enumerate(nearby_tickets):
        valid_ticket = True
        for val in ticket:
            if val not in valid_numbers:
                invalid_count += val
                valid_ticket = False
                break
        if valid_ticket:
            valid_tickets.append(i)

    return invalid_count, valid_tickets

def in_range(arr, bounds):
    a = np.logical_and(arr >= bounds[0], arr <= bounds[1])
    return a

def find_potential_fields(fields, valid_tickets):
    vt = np.array(valid_tickets)
    potential_fields = {i:[] for i in range(len(fields))}
    
    for i in range(len(fields)):
        for field in fields:
            lbounds, ubounds = fields[field]
            a = np.logical_or(in_range(vt[:,i],lbounds), 
                              in_range(vt[:,i], ubounds))
            if np.all(a):
                potential_fields[i].append(field)
                
    return potential_fields

def check_ans(ordered_names, fields, vt):
    for i, f in enumerate(ordered_names):
        lbounds, ubounds = fields[f]
        a = np.logical_or(in_range(vt[i,:],lbounds), 
                          in_range(vt[i,:], ubounds))
        assert(np.all(a))        


fields, my_ticket, nearby_tickets = get_input('advent_day16.txt')
invalid_count, valid_ticket_indx = count_invalid(fields, nearby_tickets)
print(f'Part 1 = {invalid_count}')

valid_tickets = np.array([nearby_tickets[i] for i in valid_ticket_indx])

pf = find_potential_fields(fields, valid_tickets)

indx = sorted(pf, key=lambda k: len(pf[k]))

for i in indx:
    curr_field = pf[i][0]
    for j in pf:
        if (curr_field in pf[j]) and (len(pf[j]) > 1):
            pf[j].remove(curr_field)

ans = 1
for i, f in pf.items():
    if f[0].startswith('departure'):
        ans *= my_ticket[i]

print(f'Part 2 = {ans}')