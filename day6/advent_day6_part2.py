
def records_from_lines(lines):
    records = {}
    i = 0
    for line in lines:
        if line == '\n':
            i += 1
            continue
        
        try:
            records[i].append(line.strip())
        except KeyError:
            records[i] = [line.strip()]
    
    return records

def all_answers(l):  
    count = 0
    unique_ans = set(''.join(l))
    for ans in unique_ans:
        if all([ans in c for c in l]):
            count += 1
    return count

def all_answers2(l):  
    a = [set(x) for x in l]
    c = a[0]
    c.intersection_update(*a[1:])
    return len(c)

with open('advent_day6.txt') as fid:
    lines = fid.readlines()

records = records_from_lines(lines)

count = 0
count2 = 0 
for i in records:
    ua = all_answers(records[i])
    ua2 = all_answers2(records[i])
    count += ua
    count2 += ua2

print('Total: {}'.format(count))
print('Total: {}'.format(count2))