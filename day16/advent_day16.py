
def get_fields(lines):
    """
    """
    fields = []
    for line in lines:
        if line.strip() != '':
            field, vals = line.split(':')
            a = vals.strip().split(' or ')
            b = [[int(x) for x in i.split('-')] for i in a]
            fields.append((field, b)) 
        else:
            break
    return fields

def get_ticket(lines):
    """
    """
    for i, line in enumerate(lines):
        if line.startswith('your ticket'):
            break
    return [int(x) for x in lines[i+1].strip().split(',')]

def get_nearby_ticket(lines):
    """
    """
    for i, line in enumerate(lines):
        if line.startswith('nearby'):
            break
    tmp = lines[i+1:]
    nearby_tickets = []
    for ticket in tmp:
        nearby_tickets.append([int(x) for x in ticket.strip().split(',')])
    
    return nearby_tickets

def get_input(fname):
    """
    """
    with open(fname) as fid:
        lines = fid.readlines()
    
    fields = get_fields(lines)
    my_ticket = get_ticket(lines)
    nearby_tickets = get_nearby_ticket(lines)

    return fields, my_ticket, nearby_tickets

def expand_fields(fields):
    valid_numbers = []
    for field in fields:
        f = field[1]
        for i in range(len(f)):
            valid_numbers.extend(list(range(f[i][0],f[i][1])))
    return set(valid_numbers)

fields, my_ticket, nearby_tickets = get_input('advent_day16.txt')

valid_numbers = expand_fields(fields)
invalid_count = 0
for ticket in nearby_tickets:
    for val in ticket:
        if val not in valid_numbers:
            invalid_count += val

print(f'Part 1 = {invalid_count}')