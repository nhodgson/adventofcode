
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


with open('advent_day6_test.txt') as fid:
    lines = fid.readlines()

records = records_from_lines(lines)

count = 0
records_set = {}
for i in records:

    records_set[i] = set(''.join(records[i]))
    count += len(records_set[i])

print('Total: {}'.format(count))