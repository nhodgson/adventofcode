def count_trees(lines, slope):
    n = 0
    m = 0
    max_lines = len(lines)
    width = len(lines[0])
    values = []

    for i in range( int((max_lines - 1)/slope[1])):

        n += slope[0]
        m += slope[1]
        if n >= width:
            n = n - width

        values.append(lines[m][n])

    return values.count('#')


with open('advent_day3.txt') as fid:
    lines = fid.readlines()

lines = [l.strip() for l in lines]

max_lines = len(lines)
width = len(lines[0])

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
ans = []
for slope in slopes:
    ans.append(count_trees(lines, slope))


